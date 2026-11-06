"""English PMA MCQs = checked MCQs from 'PMA Initial Test English From Every Corner' (topic 1-225 + mock 1-75) and the
synonym/antonym list (english/out/*.json). Skipped items are left out. The same question is written once with its count in brackets.
Order is mixed (all types together) and the same every build. Output: english/en_final.json"""
import json, os, glob, re, hashlib
d = os.path.dirname(os.path.abspath(__file__))
items = []
for f in sorted(glob.glob(os.path.join(d, 'out', '*.json'))):
    f2 = os.path.join(d, 'out2', os.path.basename(f))
    if os.path.exists(f2): f = f2  # out2 = same MCQs with detailed 'why' (correct + why others wrong) and 'rel'
    for x in json.load(open(f, encoding='utf8')):
        if x.get('skip'): continue
        q = x['question'].strip()
        if x.get('passage'):
            q = re.sub(r'^\[[^\]]*\]\s*', '', q)
            q = 'Read the passage: ' + re.sub(r'\s+', ' ', x['passage'].split('\n', 1)[-1]).strip() + '  QUESTION: ' + q
        items.append({'question': q, 'options': x['options'], 'correct': x['correct'], 'facts': (x.get('why') or x['reason']).strip().replace('<', '(').replace('>', ')'), 'rel': (x.get('rel') or '').strip().replace('<', '(').replace('>', ')'), 'w': int(x.get('count', 1) or 1)})
groups = {}
for it in items:
    k = re.sub(r'[^a-z0-9]+', ' ', it['question'].lower()).strip() + '|' + re.sub(r'[^a-z0-9]+', ' ', str(it['options'][it['correct']]).lower()).strip()
    g = groups.get(k)
    if g: g['w'] += it['w']
    else: groups[k] = dict(it)
out = []
for g in groups.values():
    q = g['question'] + (' (%d)' % g['w'] if g['w'] > 1 else '')
    out.append({'question': q, 'options': g['options'], 'correct': g['correct'], 'facts': g['facts'], **({'rel': g['rel']} if g['rel'] else {}), 'pma': True, 'sec': 'English', 'rep': g['w']})
out.sort(key=lambda q: hashlib.md5(q['question'].encode('utf8')).hexdigest())
json.dump(out, open(os.path.join(d, 'en_final.json'), 'w'), ensure_ascii=False)
print('English MCQs:', len(out), 'from', len(items))
