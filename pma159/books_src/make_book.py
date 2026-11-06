"""Generic: python3 make_book.py <dir> <pdf>  -> books/<dir> (encrypted pages + OCR text). Same as make_scanned_pdf.py."""
import os, glob, re, json, io, secrets, hashlib, base64, csv, subprocess
from concurrent.futures import ThreadPoolExecutor
import cv2
from PIL import Image
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.environ['OMP_THREAD_LIMIT'] = '1'
import sys
DIR = sys.argv[1]
SRC = sys.argv[2]
out = '/home/user/Asad/pma159/books/' + DIR
W0 = 'work_' + DIR
import shutil
shutil.rmtree(W0, ignore_errors=True); os.makedirs(W0 + '/r'); os.makedirs(W0 + '/f')
os.makedirs(out, exist_ok=True)
subprocess.run(['pdftoppm', '-r', '120', '-png', SRC, W0 + '/r/p'], check=True)
fs = sorted(glob.glob(W0 + '/r/p-*.png'), key=lambda f: int(re.search(r'(\d+)\.png', f).group(1)))
pw = json.load(open('/home/user/keystore/book_passwords.json'))['bk_issb130'].encode()
salt = secrets.token_bytes(16); ITER = 100000
g = AESGCM(hashlib.pbkdf2_hmac('sha256', pw, salt, ITER, 32))
M = 34
import numpy as np
def deskew(im):
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    sm = cv2.resize(g, None, fx=0.35, fy=0.35)
    bw = (sm < 150).astype(np.uint8) * 255
    best, ba = -1, 0.0
    h, w = bw.shape; c = (w / 2, h / 2)
    for a in np.arange(-4, 4.01, 0.25):
        r = cv2.warpAffine(bw, cv2.getRotationMatrix2D(c, a, 1), (w, h), flags=cv2.INTER_NEAREST)
        sc = np.var(r.sum(axis=1).astype(np.float64))
        if sc > best: best, ba = sc, a
    if abs(ba) < 0.25: return im
    H, W = im.shape[:2]
    return cv2.warpAffine(im, cv2.getRotationMatrix2D((W / 2, H / 2), ba, 1), (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


def one(a):
    i, f = a
    im = cv2.imread(f)
    im = deskew(im)
    im = cv2.copyMakeBorder(im, M, M, M, M, cv2.BORDER_CONSTANT, value=(255, 255, 255)); H, W = im.shape[:2]
    cv2.rectangle(im, (16, 16), (W - 17, H - 17), (30, 74, 46), 5); cv2.rectangle(im, (27, 27), (W - 28, H - 28), (80, 160, 200), 2)
    cv2.imwrite(W0 + '/f/p-%03d.png' % i, im)
    # OCR for search (on the bordered page so coordinates match)
    try:
        t = subprocess.run(['tesseract', W0 + '/f/p-%03d.png' % i, 'stdout', '--psm', '3', 'tsv'], capture_output=True, timeout=180).stdout.decode('utf8', 'ignore')
    except Exception:
        t = ''
    ws = []
    for r in csv.DictReader(io.StringIO(t), delimiter='\t', quoting=csv.QUOTE_NONE):
        x = (r.get('text') or '').strip()
        if not x or float(r.get('conf', '-1')) < 40: continue
        l, tp, w, h = [int(r[k]) for k in ('left', 'top', 'width', 'height')]
        ws.append([x, round(l / W, 4), round(tp / H, 4), round(w / W, 4), round(h / H, 4)])
    p = Image.open(W0 + '/f/p-%03d.png' % i).convert('RGB'); p = p.resize((900, round(p.height * 900 / p.width)), Image.LANCZOS)
    b = io.BytesIO(); p.save(b, 'WEBP', quality=66, method=6)
    iv = secrets.token_bytes(12)
    open(out + '/p%03d.bin' % i, 'wb').write(iv + g.encrypt(iv, b.getvalue(), ('%s/%d' % (DIR, i)).encode()))
    return i, ws, p.size


with ThreadPoolExecutor(3) as ex:
    res = list(ex.map(one, enumerate(fs, 1)))
T = {str(i): ws for i, ws, _ in res}
data = json.dumps(T, separators=(',', ':'), ensure_ascii=False).encode(); iv = secrets.token_bytes(12)
open(out + '/text.bin', 'wb').write(iv + g.encrypt(iv, data, (DIR + '/text').encode()))
wh = res[0][2]
json.dump({'id': 'bk_issb130', 'n': len(fs), 'salt': base64.b64encode(salt).decode(), 'iter': ITER, 'wh': list(wh)}, open(out + '/meta.json', 'w'))
shutil.rmtree(W0, ignore_errors=True)
print('DONE', DIR, len(fs), 'pages', sum(len(v) for v in T.values()), 'words', wh)
