# Paid Non Verbal Booklet (Pro Genius): out/*.json (one per problem) -> progenius/pb_final.json (list of nv question dicts)
import json, glob, os, re
H = os.path.dirname(os.path.abspath(__file__))
ORDER = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']
NAME = {'S1': 'Odd Man Out', 'S2': 'Analogy', 'S3': 'Mirror Images', 'S4': 'Difference and Matrix', 'S5': 'Complete the Sequence', 'S6': 'Direction and Mixed'}
DROP = set(json.load(open(os.path.join(H, 'drop.json')))) if os.path.exists(os.path.join(H, 'drop.json')) else set()
items = []
for f in glob.glob(os.path.join(H, 'out', 'S*_*.json')):
    e = json.load(open(f)); m = re.match(r'(S\d)_(\d+)', os.path.basename(f))
    key = '%s_%02d' % (m.group(1), int(m.group(2)))
    if key in DROP: continue
    o = e['options']; c = int(e['correct'])
    if not (2 <= len(o) <= 8 and 0 <= c < len(o) and all(str(x).startswith('<svg') for x in o)): print('skip bad', key); continue
    q = re.sub(r'\s*\((odd man out|odd one out)\)', '', (e.get('question') or '').strip(), flags=re.I) or 'Choose the correct figure.'
    items.append((ORDER.index(m.group(1)), int(m.group(2)), {
        'question': '%s (%s, Problem %d)' % (q.rstrip('.'), NAME[m.group(1)], int(m.group(2))),
        'options': o, 'correct': c, 'facts': e.get('why', ''), 'rel': e.get('trick', ''), 'nv': True, 'kind': e.get('kind', ''),
        'stem': e.get('stem_groups') or [], 'noq': bool(e.get('noq')) or (len(e.get('stem_groups') or []) == 1 and len((e.get('stem_groups') or [[]])[0]) == 1 and (e.get('kind') == 'matrix' or '>?<' in e['stem_groups'][0][0])), 'pma': True, 'sec': 'Paid Non Verbal Booklet: ' + NAME[m.group(1)], 'rep': 1}))
items.sort(key=lambda x: (x[0], x[1]))
out = [x[2] for x in items]
json.dump(out, open(os.path.join(H, '..', 'pb_final.json'), 'w'), ensure_ascii=False)
print(len(out), 'questions ->', 'progenius/pb_final.json')
