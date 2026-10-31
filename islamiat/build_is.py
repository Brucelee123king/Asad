"""Islamiat MCQs PMA = MCQs written from the user's 3 note pages (notes_p1..3.jpg) by agents (SPEC.md), checked by a 2nd agent.
out/a.json + out/b.json -> is_final.json (mixed order, same every build). Shown in 'Academic PMA MCQs' (IS-n tests of 50)."""
import json, os, glob, hashlib
d = os.path.dirname(os.path.abspath(__file__))
out, seen = [], set()
for f in sorted(glob.glob(os.path.join(d, 'out', '*.json'))):
    for x in json.load(open(f, encoding='utf8')):
        q = x['question'].strip(); k = q.lower()
        if k in seen: continue
        seen.add(k)
        assert len(x['options']) == 4 and 0 <= x['correct'] < 4, q
        c = lambda t: str(t).strip().replace('<', '(').replace('>', ')')
        out.append({'question': c(q), 'options': [c(o) for o in x['options']], 'correct': x['correct'], 'facts': c(x['why']),
                    **({'rel': c(x['rel'])} if x.get('rel') else {}), 'pma': True, 'sec': 'Islamiat', 'rep': 1})
out.sort(key=lambda q: hashlib.md5(q['question'].encode('utf8')).hexdigest())
json.dump(out, open(os.path.join(d, 'is_final.json'), 'w'), ensure_ascii=False)
print('Islamiat MCQs:', len(out))
