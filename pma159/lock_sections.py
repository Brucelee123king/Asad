"""Lock the main categories (online version).
Each category's tests are gzip + AES-256-GCM encrypted (key = PBKDF2-SHA256 of that category's password) and written as
data/<cat>.json; the page (shell) only holds empty placeholders and downloads/decrypts a category after the right password.
usage: python3 lock_sections.py plain.html all_dump.json passwords.json out_dir base_url [prev_dir]
  out_dir/index.html, out_dir/data/<cat>.json, out_dir/lock.json   (lock.json = current version of every category)
  prev_dir (the already published folder): a category whose data AND password did not change keeps its old file/version."""
import sys, json, gzip, os, base64, re, secrets, hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
plain, dump, pwf, outdir, base = sys.argv[1:6]
prev = sys.argv[6] if len(sys.argv) > 6 else None
if not base.endswith('/'): base += '/'
html = open(plain, encoding='utf8').read()
ALL = json.load(open(dump, encoding='utf8'))
PW = json.load(open(pwf, encoding='utf8'))
ITER, EXPIRY_DAYS = 100000, int(os.environ.get('EXPIRY_DAYS', '7'))
def cat(k):
    p = k.split('-')[0]
    return {'PMA': 'pma', 'FA': 'fa', 'HK': 'hk', 'MR': 'hk', 'CN': 'cn', 'IV': 'iv', 'LC': 'lc', 'PG': 'pg', 'PF': 'pg', 'NV': 'nv'}.get(p, 'o')
groups = {}
for k, v in ALL.items(): groups.setdefault(cat(k), {})[k] = v
assert set(groups) == set(PW), (set(groups), set(PW))
b64 = lambda b: base64.b64encode(b).decode()
os.makedirs(os.path.join(outdir, 'data'), exist_ok=True)
meta, versions, reused = {}, {}, []
for cid, data in groups.items():
    pw = re.sub(r'[^A-Z0-9]', '', PW[cid].upper())
    pt = json.dumps(data, ensure_ascii=False, separators=(',', ':')).encode('utf8')
    file = None
    if prev:
        pf = os.path.join(prev, 'data', cid + '.json')
        if os.path.exists(pf):
            try:
                old = json.load(open(pf)); k = hashlib.pbkdf2_hmac('sha256', pw.encode(), base64.b64decode(old['salt']), old['iter'], 32)
                if gzip.decompress(AESGCM(k).decrypt(base64.b64decode(old['iv']), base64.b64decode(old['ct']), None)) == pt: file = old; reused.append(cid)
            except Exception: pass
    if file is None:
        salt, iv = secrets.token_bytes(16), secrets.token_bytes(12)
        key = hashlib.pbkdf2_hmac('sha256', pw.encode(), salt, ITER, 32)
        ct = AESGCM(key).encrypt(iv, gzip.compress(pt, 9, mtime=0), None)
        file = {'v': hashlib.sha256(ct).hexdigest()[:12], 'salt': b64(salt), 'iv': b64(iv), 'iter': ITER, 'ct': b64(ct)}
    json.dump(file, open(os.path.join(outdir, 'data', cid + '.json'), 'w'), separators=(',', ':'))
    versions[cid] = file['v']
    meta[cid] = {'n': {k: len(v) for k, v in data.items()}, 'u': {k: sorted({e.get('sec', '') for e in v}) for k, v in data.items()}}
json.dump({'v': versions}, open(os.path.join(outdir, 'lock.json'), 'w'), separators=(',', ':'))
a = html.index('const ALL = ')
b = html.index('const HK_META = ', a)
c = html.index('/* answer audit corrections', b)
d = html.index('Object.keys(CORR).forEach(function (k)', c)
e = html.index('\n', d)
helpers = html[b:c]
stub_js = ("window.__mkStubs=function(id){var c=window.__LOCK.cats[id],o={};Object.keys(c.n).forEach(function(k){var u=c.u[k]&&c.u[k].length?c.u[k]:[''],a=[];"
           "for(var i=0;i<c.n[k];i++)a.push({id:i+1,question:'',options:[],correct:0,facts:'',sec:u[i%u.length],pma:true});o[k]=a});return o};\n        "
           "const ALL = (function(){var o={};Object.keys(window.__LOCK.cats).forEach(function(id){var s=window.__mkStubs(id);Object.keys(s).forEach(function(k){o[k]=s[k]})});return o})();\n        ")
new = ('window.__LOCK = ' + json.dumps({'base': base, 'expiryDays': EXPIRY_DAYS, 'cats': meta}, separators=(',', ':')) + ';\n        ' + stub_js + helpers)
html = html[:a] + new + html[e:]
block = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lock_block.html'), encoding='utf8').read()
_d3 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'd3_block.html'), encoding='utf8').read().rstrip()
_tail = _d3[-80:]
assert html.count(_tail) == 1
m = html.index(_tail) + len(_tail)
cfg = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'firebase_config.json'), encoding='utf8').read()
access = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'access_block.html'), encoding='utf8').read().replace('__FBCFG__', json.dumps(json.loads(cfg)))
html = html[:m] + '\n' + block + '\n' + access + html[m:]
PRE = ('<style id="acPre">html:not(.acok) body{background:#ddd6fe!important}'
       'html:not(.acok) body>header,html:not(.acok) body>main,html:not(.acok) body>footer,html:not(.acok) #modal-submit-confirm,html:not(.acok) #obj3d,html:not(.acok) #liquidBg,html:not(.acok) #srchModal,html:not(.acok) #rngModal{display:none!important}</style>')
assert html.count('</head>') == 1
html = html.replace('</head>', PRE + '</head>', 1)
open(os.path.join(outdir, 'index.html'), 'w', encoding='utf8').write(html)
adm = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'admin.html'), encoding='utf8').read().replace('__FBCFG__', json.dumps(json.loads(cfg)))
open(os.path.join(outdir, 'admin.html'), 'w', encoding='utf8').write(adm)
print('written', outdir, 'shell', len(html), 'bytes; reused unchanged:', reused, '; versions', versions)
