"""Lock the main categories: encrypt each category's tests with its own password (AES-256-GCM, key from PBKDF2-SHA256).
usage: python3 lock_sections.py plain.html all_dump.json passwords.json out.html
The output page only contains empty placeholders for the tests; the real MCQs are ciphertext until the right password is typed."""
import sys, json, gzip, os, base64, re, secrets, hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
plain, dump, pwf, out = sys.argv[1:5]
html = open(plain, encoding='utf8').read()
ALL = json.load(open(dump, encoding='utf8'))
PW = json.load(open(pwf, encoding='utf8'))
ITER = 100000
def cat(k):
    p = k.split('-')[0]
    if p == 'PMA': return 'pma'
    if p == 'FA': return 'fa'
    if p in ('HK', 'MR', 'CN', 'IV'): return 'hk'
    if p == 'LC': return 'lc'
    if p in ('PG', 'PF'): return 'pg'
    if p == 'NV': return 'nv'
    return 'o'
groups = {}
for k, v in ALL.items(): groups.setdefault(cat(k), {})[k] = v
assert set(groups) == set(PW), (set(groups), set(PW))
b64 = lambda b: base64.b64encode(b).decode()
cats = {}
for cid, data in groups.items():
    pw = re.sub(r'[^A-Z0-9]', '', PW[cid].upper())
    salt, iv = secrets.token_bytes(16), secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac('sha256', pw.encode(), salt, ITER, 32)
    raw = gzip.compress(json.dumps(data, ensure_ascii=False, separators=(',', ':')).encode('utf8'), 9, mtime=0)
    cats[cid] = {'salt': b64(salt), 'iv': b64(iv), 'iter': ITER, 'ct': b64(AESGCM(key).encrypt(iv, raw, None)), 'n': {k: len(v) for k, v in data.items()}}
stubs = {}
for k, v in ALL.items():
    stubs[k] = [{'id': e.get('id', i + 1), 'question': '', 'options': [], 'correct': 0, 'facts': '', 'sec': e.get('sec', ''), 'pma': bool(e.get('pma'))} for i, e in enumerate(v)]
a = html.index('const ALL = ')
b = html.index('const HK_META = ', a)
c = html.index('/* answer audit corrections', b)
d = html.index('Object.keys(CORR).forEach(function (k)', c)
e = html.index('\n', d)
helpers = html[b:c]
new = ('const ALL = ' + json.dumps(stubs, ensure_ascii=False, separators=(',', ':')) + ';\n        ' + helpers +
       'window.__LOCK = ' + json.dumps({'cats': cats}, separators=(',', ':')) + ';')
html = html[:a] + new + html[e:]
block = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lock_block.html'), encoding='utf8').read()
_d3 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'd3_block.html'), encoding='utf8').read().rstrip()
_tail = _d3[-80:]
assert html.count(_tail) == 1
m = html.index(_tail) + len(_tail)
html = html[:m] + '\n' + block + html[m:]
open(out, 'w', encoding='utf8').write(html)
print('locked page written', out, len(html), {c: len(v) for c, v in groups.items()})
