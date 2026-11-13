import subprocess, csv, io, json, os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.environ['OMP_THREAD_LIMIT'] = '1'
os.makedirs('ocr', exist_ok=True)


def one(n):
    o = 'ocr/%03d.json' % n
    if os.path.exists(o):
        return
    f = 'c/p-%03d.png' % n
    W, H = Image.open('f/p-%03d.png' % n).size
    try:
        out = subprocess.run(['tesseract', f, 'stdout', '--psm', '11', 'tsv'], capture_output=True, timeout=180).stdout.decode('utf8', 'ignore')
    except Exception:
        out = ''
    ws = []
    for r in csv.DictReader(io.StringIO(out), delimiter='\t', quoting=csv.QUOTE_NONE):
        t = (r.get('text') or '').strip()
        if not t or float(r.get('conf', '-1')) < 35:
            continue
        x, y, w, h = [int(r[k]) for k in ('left', 'top', 'width', 'height')]
        ws.append([t, round((x + 46) / W, 4), round((y + 46) / H, 4), round(w / W, 4), round(h / H, 4)])
    # reading order: rows (by y, grouped within ~half a line) then x
    ws.sort(key=lambda a: (round(a[2] / 0.008), a[1]))
    json.dump(ws, open(o, 'w'))
    print(n, len(ws), flush=True)


with ThreadPoolExecutor(4) as ex:
    list(ex.map(one, range(2, 95)))
print('ALL DONE', flush=True)
