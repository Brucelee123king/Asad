"""Signed self-update for the app shell.
usage: sign_shell.py <www/index.html> <publish_dir> <base_url> [prev_dir]
 - adds a small loader at the top of the page (inside the APK copy)
 - writes shell.html (same text) and shell.json {v,h,sig} to <publish_dir>; sig = ECDSA P-256 / SHA-256 signature of shell.html
   made with /home/user/keystore/shell_sign_priv.pem (private key never goes to GitHub).
The app downloads shell.html after a launch, checks the signature with the public key inside the loader, keeps it and uses it
from the next launch. A wrong signature is ignored. Two failed launches in a row bring back the built-in page."""
import sys, os, json, hashlib, time, base64
from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives import hashes, serialization
www, pub, base = sys.argv[1:4]; prev = sys.argv[4] if len(sys.argv) > 4 else ''
key = serialization.load_pem_private_key(open('/home/user/keystore/shell_sign_priv.pem', 'rb').read(), None)
nums = key.public_key().public_numbers()
b64u = lambda n: base64.urlsafe_b64encode(n.to_bytes(32, 'big')).decode().rstrip('=')
jwk = {'kty': 'EC', 'crv': 'P-256', 'x': b64u(nums.x), 'y': b64u(nums.y)}
html = open(www, encoding='utf8').read()
if '/*SHELLUPD*/' in html: raise SystemExit('already has loader')
h = hashlib.sha1(html.encode('utf8')).hexdigest()[:12]
v = int(os.environ.get('SHELL_V') or time.strftime('%Y%m%d%H%M'))
pj = os.path.join(prev, 'shell.json') if prev else ''
if pj and os.path.exists(pj):
    try:
        o = json.load(open(pj))
        if o.get('h') == h: v = o['v']
    except Exception: pass
LOADER = r"""<script>/*SHELLUPD*/(function(){var V=%d,B='%s',K=%s,L=localStorage;
try{var sv=+L.getItem('shell_v')||0,h=L.getItem('shell_html'),t=+L.getItem('shell_try')||0;
if(h&&sv>V&&!window.__shellW){if(t>=2){L.removeItem('shell_html');L.removeItem('shell_v');L.removeItem('shell_try')}
else{L.setItem('shell_try',String(t+1));window.__shellW=1;document.open();document.write(h);document.close();return}}}catch(e){}
function u8(s){s=s.replace(/-/g,'+').replace(/_/g,'/');var b=atob(s),a=new Uint8Array(b.length);for(var i=0;i<b.length;i++)a[i]=b.charCodeAt(i);return a}
function chk(x,sig){return crypto.subtle.importKey('jwk',K,{name:'ECDSA',namedCurve:'P-256'},false,['verify']).then(function(k){
 return crypto.subtle.verify({name:'ECDSA',hash:'SHA-256'},k,u8(sig),new TextEncoder().encode(x))})}
window.addEventListener('load',function(){setTimeout(function(){try{if(window.FB&&document.getElementById('auth'))L.setItem('shell_try','0')}catch(e){}
if(navigator.onLine===false||!window.crypto||!crypto.subtle)return;
fetch(B+'shell.json?'+Date.now(),{cache:'no-store'}).then(function(r){return r.json()}).then(function(j){var cur=Math.max(V,+L.getItem('shell_v')||0);
if(!(j.v>cur)||!j.sig)return;
return fetch(B+'shell.html?'+j.v,{cache:'no-store'}).then(function(r){return r.text()}).then(function(x){
 if(x.length<50000||x.indexOf('SHELLUPD')<0)return;
 return chk(x,j.sig).then(function(ok){if(ok){L.setItem('shell_html',x);L.setItem('shell_v',String(j.v))}})})}).catch(function(){})},6000)});
})();</script>""" % (v, base, json.dumps(jwk, separators=(',', ':')))
i = html.index('<head>') + len('<head>')
out = html[:i] + LOADER + html[i:]
# the page is written into the still running start page: this tail makes the browser swallow the rest of the old page as plain text (display:none), so only one copy of the app runs
out = out.rstrip() + '<plaintext style="display:none"></plaintext>'
sig = key.sign(out.encode('utf8'), ec.ECDSA(hashes.SHA256()))
r, s_ = utils.decode_dss_signature(sig)
raw = r.to_bytes(32, 'big') + s_.to_bytes(32, 'big')          # WebCrypto expects r||s
open(www, 'w', encoding='utf8').write(out)
os.makedirs(pub, exist_ok=True)
open(os.path.join(pub, 'shell.html'), 'w', encoding='utf8').write(out)
json.dump({'v': v, 'h': h, 'sig': base64.urlsafe_b64encode(raw).decode().rstrip('=')}, open(os.path.join(pub, 'shell.json'), 'w'))
print('signed shell update: version', v)
