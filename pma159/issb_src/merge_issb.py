"""Merge the per-part ISSB extracts (issb/out/partNN.json) into pma159/issb_src/final.json.
usage: python3 merge_issb.py <dir with partNN.json>"""
import json, glob, os, re, sys
src = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))


def norm(t):
    return re.sub(r'[^a-z0-9؀-ۿ]+', '', str(t).lower())


def key(x):
    if isinstance(x, str):
        return norm(x)
    if isinstance(x, dict):
        return norm(x.get('w') or x.get('s') or x.get('q') or x.get('title') or json.dumps(x, sort_keys=True))
    return norm(json.dumps(x))


def uniq(items, cap):
    seen, out = set(), []
    for x in items:
        if x in (None, '', {}, []):
            continue
        if isinstance(x, dict) and not any(str(v).strip() for v in x.values()):
            continue
        k = key(x)
        if not k or k in seen:
            continue
        seen.add(k); out.append(x)
    return out[:cap]


LISTS = ['overview', 'kit', 'docs', 'dos', 'donts']
SECS = ['intelligence', 'wat', 'srt', 'sct_en', 'sct_ur', 'pointer', 'picture', 'opi', 'biodata', 'selfdesc', 'essay', 'mechanical',
        'gd', 'lecturette', 'planning', 'pgt', 'hgt', 'command', 'iot', 'fgt', 'outdoor_other',
        'interview_dp', 'interview_psy', 'interview_gto', 'conference']
CAP = {'tips': 25, 'words': 300, 'items': 300, 'topics': 200, 'samples': 80, 'questions': 200, 'examples': 20, 'obstacles': 30}
acc = {k: [] for k in LISTS}
sec = {k: {} for k in SECS}
days = {}
xp = []
for f in sorted(glob.glob(os.path.join(src, 'part*.json'))):
    try:
        d = json.load(open(f, encoding='utf8'))
    except Exception as e:
        print('skip', f, e); continue
    for k in LISTS:
        acc[k] += [x for x in d.get(k, []) if isinstance(x, str)]
    for dk, dv in (d.get('days') or {}).items():
        m = re.search(r'(\d)', dk)
        if m and isinstance(dv, list):
            days.setdefault('Day ' + m.group(1), []).extend(dv)
    for s in SECS:
        v = d.get(s)
        if isinstance(v, dict):
            for sub, arr in v.items():
                if isinstance(arr, list):
                    sec[s].setdefault(sub, []).extend(arr)
    xp += [e for e in d.get('experiences', []) if isinstance(e, dict) and e.get('summary')]
out = {k: uniq(v, 40 if k == 'overview' else 25) for k, v in acc.items()}
out['days'] = {k: uniq(days[k], 12) for k in sorted(days)}
for s in SECS:
    o = {}
    for sub, arr in sec[s].items():
        if sub == 'personal_topics':
            sub = 'topics'
        cap = CAP.get(sub, 100)
        o.setdefault(sub, []).extend(arr)
    for sub in list(o):
        o[sub] = uniq(o[sub], CAP.get(sub, 100))
        if not o[sub]:
            del o[sub]
    if o:
        out[s] = o
out['experiences'] = uniq(xp, 40)
json.dump(out, open(os.path.join(here, 'final.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
for k, v in out.items():
    print(k, len(v) if isinstance(v, list) else {a: len(b) for a, b in v.items()} if isinstance(v, dict) else v)
