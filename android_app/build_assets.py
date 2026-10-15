#!/usr/bin/env python3
"""Copies HabitFlow and the classic boards into app/src/main/assets (run before gradle)."""
import os, re, shutil
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
out = os.path.join(here, 'app/src/main/assets')
shutil.rmtree(out, ignore_errors=True); os.makedirs(out)

# HabitFlow app (app.html, css/, js/, icon.png)
hf = os.path.join(here, 'habitflow')
for name in os.listdir(hf):
    if name == 'tests': continue
    s = os.path.join(hf, name)
    (shutil.copytree if os.path.isdir(s) else shutil.copy)(s, os.path.join(out, name))

GLUE = ("<script>window.__u=(function(){try{var s=JSON.parse(localStorage.getItem('ht.session')||sessionStorage.getItem('ht.session')||'null');"
        "return s&&s.user&&!s.guest?'u:'+s.user.toLowerCase()+'::':'guest::'}catch(e){return ''}})();"
        "try{window.Android&&Android.orient('%s')}catch(e){}</script>")
# (source, asset name, orientation or None, classic board needing a per-user key prefix)
PAGES = [
  (os.path.join(here, 'pages/login.html'), 'index.html', None, False),
  (os.path.join(here, 'pages/home.html'), 'home.html', None, False),
  (os.path.join(here, 'pages/custom.html'), 'custom.html', 'portrait', False),
  (os.path.join(root, 'habit_tracker.html'), 'ultimate.html', 'landscape', True),
  (os.path.join(root, 'digital_habit_tracker.html'), 'digital.html', 'portrait', True),
  (os.path.join(root, 'task_tracker.html'), 'task.html', 'portrait', True),
]
for src, name, orient, prefix in PAGES:
    t = open(src, encoding='utf-8').read()
    if prefix:
        t = re.sub(r"const KEY='", "const KEY=(window.__u||'')+'", t)
        t = t.replace('Math.max(.45,', 'Math.max(.2,')
    if orient:
        t = t.replace('</head>', (GLUE % orient) + '\n</head>', 1)
    open(os.path.join(out, name), 'w', encoding='utf-8').write(t)
print('assets:', sorted(os.listdir(out)))
