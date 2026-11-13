import json, glob, os, re, hashlib, base64, secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
os.chdir(os.path.dirname(os.path.abspath(__file__)))
out = '/home/user/Asad/pma159/books/issb130'
meta = json.load(open(out + '/meta.json'))
pw = json.load(open('/home/user/keystore/book_passwords.json'))['bk_issb130'].encode()
g = AESGCM(hashlib.pbkdf2_hmac('sha256', pw, base64.b64decode(meta['salt']), meta['iter'], 32))
T = {}
for f in sorted(glob.glob('ocr/*.json')):
    n = int(re.search(r'(\d+)', os.path.basename(f)).group(1))
    T[str(n)] = json.load(open(f))
data = json.dumps(T, separators=(',', ':'), ensure_ascii=False).encode('utf8')
iv = secrets.token_bytes(12)
open(out + '/text.bin', 'wb').write(iv + g.encrypt(iv, data, b'issb130/text'))
print(len(T), 'pages', len(data) // 1024, 'KB')
