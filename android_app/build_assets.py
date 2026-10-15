#!/usr/bin/env python3
"""Copies every page into app/src/main/assets, adding the app glue
(per-user data prefix + screen orientation). Run before gradle."""
import os, re
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
out = os.path.join(here, 'app/src/main/assets')
os.makedirs(out, exist_ok=True)

GLUE = ("<script>window.__u=(function(){try{var s=JSON.parse(localStorage.getItem('ht.session')||sessionStorage.getItem('ht.session')||'null');"
        "return s&&s.user&&!s.guest?'u:'+s.user+'::':'guest::'}catch(e){return ''}})();"
        "try{window.Android&&Android.orient('%s')}catch(e){}</script>")

# (source, asset name, orientation, needs per-user key prefix)
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
    if orient or prefix or name == 'custom.html':
        t = t.replace('</head>', (GLUE % (orient or 'portrait')) + '\n</head>', 1)
    open(os.path.join(out, name), 'w', encoding='utf-8').write(t)
    print('wrote', name)
