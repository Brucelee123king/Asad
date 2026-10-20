#!/usr/bin/env python3
"""Builds the offline web bundle for the Android app.

Input : ../source/index.html   (corrected website file; ../original/index.html is the untouched backup)
Output: ../app/src/main/assets/www/  (index.html + css/ + fonts/ + webfonts/ + error.html)

What changes in index.html (everything else is byte-identical):
  * Tailwind Play CDN script + inline tailwind.config  -> pre-compiled css/tailwind.css (same utilities, no runtime compiler)
  * Google Fonts <link>s (Inter, Plus Jakarta Sans)    -> local @font-face (css/fonts.css, fonts/*.woff2)
  * Font Awesome 6.4.0 CDN <link>                       -> local css/fontawesome.css + webfonts/fa-solid-900.woff2 (+ regular)
  * Netlify analytics/HUD <script> (after </html>)      -> removed (needs the network, not needed in the app)
  * viewport meta: zoom disabled; small <style>/<script> block for touch-action + low-end-device mode + theme bridge

Needs a node folder with: tailwindcss@3.4.17 @fortawesome/fontawesome-free@6.4.0 @fontsource/inter @fontsource/plus-jakarta-sans
(see tools/package.json; run `npm install` there). usage: python3 build_web.py [node_dir]
"""
import os, re, shutil, subprocess, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, 'source', 'index.html')   # corrected site (original/ is the untouched backup)
WWW = os.path.join(ROOT, 'app', 'src', 'main', 'assets', 'www')
NODE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'node')

html = open(SRC, encoding='utf8').read()
orig_len = len(html)

# ---------- 1. tailwind: compile once from the real HTML ----------
os.makedirs(os.path.join(WWW, 'css'), exist_ok=True)
cfg = os.path.join(HERE, 'tailwind.config.js')
open(cfg, 'w').write("module.exports = { content: [%r], theme: { extend: { fontFamily: { sans: ['Inter', 'sans-serif'] } } } }\n" % SRC)
inp = os.path.join(HERE, 'tailwind.in.css')
open(inp, 'w').write('@tailwind base;\n@tailwind components;\n@tailwind utilities;\n')
subprocess.check_call([os.path.join(NODE, 'node_modules', '.bin', 'tailwindcss'), '-c', cfg, '-i', inp,
                       '-o', os.path.join(WWW, 'css', 'tailwind.css'), '--minify'], cwd=NODE)

# ---------- 2. fonts ----------
fdir = os.path.join(WWW, 'fonts'); os.makedirs(fdir, exist_ok=True)
face = []
for fam, pkg, weights in (('Inter', 'inter', (300, 400, 500, 600, 700)),
                          ('Plus Jakarta Sans', 'plus-jakarta-sans', (400, 500, 600, 700, 800))):
    for w in weights:
        fn = '%s-latin-%d-normal.woff2' % (pkg, w)
        shutil.copy(os.path.join(NODE, 'node_modules', '@fontsource', pkg, 'files', fn), os.path.join(fdir, fn))
        face.append("@font-face{font-family:'%s';font-style:normal;font-weight:%d;font-display:swap;src:url(../fonts/%s) format('woff2')}" % (fam, w, fn))
open(os.path.join(WWW, 'css', 'fonts.css'), 'w').write('\n'.join(face) + '\n')

# ---------- 3. font awesome (solid is the only style the app uses; regular kept for safety) ----------
wdir = os.path.join(WWW, 'webfonts'); os.makedirs(wdir, exist_ok=True)
fa = os.path.join(NODE, 'node_modules', '@fortawesome', 'fontawesome-free')
for fn in ('fa-solid-900.woff2', 'fa-regular-400.woff2'):
    shutil.copy(os.path.join(fa, 'webfonts', fn), os.path.join(wdir, fn))
css = open(os.path.join(fa, 'css', 'all.min.css'), encoding='utf8').read()
# drop brands + v4-compat @font-face (not shipped); keep solid/regular; woff2 only
css = re.sub(r'@font-face\{font-family:"Font Awesome 6 (?:Brands|Free)";font-style:normal;font-weight:400;font-display:block;src:url\([^}]*fa-(?:brands-400|regular-400)[^}]*\}', lambda m: m.group(0) if 'regular-400' in m.group(0) else '', css)
css = re.sub(r'@font-face\{font-family:"FontAwesome";[^}]*\}', '', css)
css = re.sub(r'@font-face\{font-family:"Font Awesome 5 Brands";[^}]*\}', '', css)
css = re.sub(r'url\((\.\./webfonts/[^)]*?)\.ttf\) format\("truetype"\)', '', css)
css = re.sub(r',\s*(?=\})', '', css)
open(os.path.join(WWW, 'css', 'fontawesome.css'), 'w').write(css)

# ---------- 4. rewrite index.html ----------
def cut(pattern, repl='', count=1, flags=re.S):
    global html
    new, n = re.subn(pattern, repl, html, count=count, flags=flags)
    assert n == count, (pattern, n)
    html = new

LINKS = ('<link rel="stylesheet" href="css/fonts.css">\n'
         '    <link rel="stylesheet" href="css/fontawesome.css">\n'
         '    <link rel="stylesheet" href="css/tailwind.css">\n')
# tailwind cdn script + inline tailwind.config script
cut(r'<script src="https://cdn\.tailwindcss\.com"></script>', '')
cut(r'<script>\s*tailwind\.config = \{.*?\}\s*</script>', '')
# google fonts (head) + font awesome
cut(r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^>]*>', LINKS)
cut(r'<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/6\.4\.0/css/all\.min\.css">', '')
# second google fonts block (Plus Jakarta Sans)
cut(r'<link rel="preconnect" href="https://fonts\.googleapis\.com"><link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*', '')
cut(r'<link href="https://fonts\.googleapis\.com/css2\?family=Plus\+Jakarta\+Sans[^>]*>', '')
# netlify hud script
cut(r'<script async src="/\.netlify/scripts/hud[^>]*></script>', '')
# viewport: no zoom
cut(r'<meta name="viewport" content="width=device-width, initial-scale=1\.0">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">')
# android helpers (first thing in <head> after viewport)
ANDROID = open(os.path.join(HERE, 'android_head.html'), encoding='utf8').read()
cut(r'(<meta name="theme-color"[^>]*>)', lambda m: m.group(1) + '\n' + ANDROID)

html = html.replace('</head>', '<link rel="icon" href="data:,">\n</head>', 1)  # no /favicon.ico request
# ---------- 4b. performance fixes (app bundle only; see qa/perf_report.md) ----------
def rep(old, new):
    global html
    assert html.count(old) == 1, old
    html = html.replace(old, new)
# parallax vars were written on <html> every frame -> whole-document style recalc. Write them only on the two consumers.
rep("var R=document.documentElement,tx=0",
    "var R={style:{setProperty:function(a,b){var t=document.getElementById('obj3d'),l=document.getElementById('liquidBg');if(t)t.style.setProperty(a,b);if(l)l.style.setProperty(a,b)}}},tx=0")
# no animation loop on low-end phones, and pause it while the app is in the background
rep("function loop(now){\n    var idle=", "function loop(now){\n    if(document.hidden){running=0;return}\n    var idle=")
rep("if(!matchMedia('(prefers-reduced-motion:reduce)').matches)requestAnimationFrame(loop);",
    "var running=0,go=!matchMedia('(prefers-reduced-motion:reduce)').matches&&!document.documentElement.classList.contains('lite');\n  function start(){if(go&&!running){running=1;requestAnimationFrame(loop)}}\n  document.addEventListener('visibilitychange',start);start();")
# bug found by QA: if the timer hits 0 while the "Submit?" popup is open, the popup stayed on top of the results
rep("                    clearInterval(timerInterval);\n                    autoSubmitQuiz();",
    "                    clearInterval(timerInterval);\n                    closeSubmitModal();\n                    autoSubmitQuiz();")
# --- phone smoothness (user report: laggy on a real phone) ---
# 1) the glass blocks put backdrop-filter:blur on the header, every card and hundreds of list buttons, with !important: the biggest GPU cost
#    on a phone. Add a stylesheet at the END of <body> (wins by specificity) that turns blur/backdrop/drop-shadow filters off.
TAIL = ('<style id="android-perf">'
        'html.lite body *,html.lite body *::before,html.lite body *::after{-webkit-backdrop-filter:none!important;backdrop-filter:none!important}'
        'html.lite body .st,html.lite body .fi,html.lite body .o3,html.lite body #auth .bl{filter:none!important}'
        'html.lite body *{-webkit-tap-highlight-color:transparent}'
        '</style>')
assert html.count('</body>') == 1
html = html.replace('</body>', TAIL + '</body>')
# 2) no pointer-tracking work for touch
rep("document.addEventListener('pointermove',function(e){lx=e.clientX", "document.addEventListener('pointermove',function(e){if(e.pointerType==='touch')return;lx=e.clientX")
# 3) big data tables: JSON.parse of a string is about 3x faster than evaluating the same object literal
import json as _json
for _n in ('PMA_DATA', 'FA_DATA', 'HK_DATA', 'MR_DATA', 'CN_DATA', 'IV_DATA', 'LC_DATA'):
    _a = 'const %s = ' % _n
    _i = html.index(_a) + len(_a)
    _val, _end = _json.JSONDecoder().raw_decode(html, _i)   # literal is pure JSON (written with json.dumps)
    html = html[:_i] + 'JSON.parse(' + _json.dumps(_json.dumps(_val, ensure_ascii=False, separators=(',', ':'))) + ')' + html[_end:]
assert 'cdn.tailwindcss.com' not in html and 'googleapis' not in html and 'cloudflare' not in html and 'netlify/scripts' not in html
open(os.path.join(WWW, 'index.html'), 'w', encoding='utf8').write(html)
shutil.copy(os.path.join(HERE, 'error.html'), os.path.join(WWW, 'error.html'))
print('index.html %d -> %d bytes' % (orig_len, len(html)))
for root, _, files in os.walk(WWW):
    for f in sorted(files):
        p = os.path.join(root, f); print('%8d %s' % (os.path.getsize(p), os.path.relpath(p, WWW)))
