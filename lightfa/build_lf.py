"""Light Forces Academy MCQs: out/s1+s2 (Seerah PDF), out/l1+l2 (159 LC 100 MCQs PDF), out/e1+e2 (Test Experiences PDF),
written and answer-checked by agents (SPEC.md) and audited. -> lf_final.json {"exp", "lc", "seerah"} in the site's MCQ format.
A question asked in several write-ups is written once with its count in brackets."""
import json, os, re
d = os.path.dirname(os.path.abspath(__file__))
def load(names):
    out, seen = [], set()
    for n in names:
        p = os.path.join(d, 'out', n + '.json')
        if not os.path.exists(p): continue
        for x in json.load(open(p, encoding='utf8')):
            q = x['question'].strip(); k = re.sub(r'[^a-z0-9]+', ' ', q.lower()).strip()
            if k in seen: continue
            seen.add(k)
            assert len(x['options']) == 4 and 0 <= int(x['correct']) < 4, q
            c = lambda t: str(t).strip().replace('<', '(').replace('>', ')')
            rep = int(x.get('rep', 0) or 0)
            o = {'question': c(q) + (' (%d)' % (rep + 1) if rep > 0 else ''), 'options': [c(t) for t in x['options']], 'correct': int(x['correct']),
                 'facts': c(x['why']), 'pma': True, 'sec': 'Light Forces Academy', 'rep': rep}
            if x.get('rel'): o['rel'] = c(x['rel'])
            out.append(o)
    return out
res = {'exp': load(['e1', 'e2']), 'lc': load(['l1', 'l2']), 'seerah': load(['s1', 's2'])}
json.dump(res, open(os.path.join(d, 'lf_final.json'), 'w'), ensure_ascii=False)
print({k: len(v) for k, v in res.items()})
