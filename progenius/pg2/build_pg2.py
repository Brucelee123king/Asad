"""Add Pro Genius PMA 159 questions 1-500 (pg2/out/c*.json) to progenius/pg_final.json.
Same as an existing MCQ (agent 'match' or same question+answer) -> raise its repeat count; new -> appended (fills parts of 50)."""
import json, os, re, glob
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H)
base = json.load(open(os.path.join(P, 'pg_final_base.json'), encoding='utf8'))
Q = [list(x) for x in base]
norm = lambda s: re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()
key = lambda q, a: norm(q) + '|' + norm(a)
seen = {key(x[1], x[2][x[3]]): i for i, x in enumerate(Q)}
nm = nn = nd = 0
for f in sorted(glob.glob(os.path.join(H, 'out', 'c*.json')), key=lambda s: int(re.findall(r'c(\d+)', s)[-1])):
    for it in json.load(open(f, encoding='utf8')):
        m = it.get('match')
        if isinstance(m, int) and 0 <= m < len(base):
            Q[m][6] += 1; nm += 1; continue
        k = key(it['question'], it['options'][it['correct']])
        if k in seen:
            Q[seen[k]][6] += 1; nd += 1; continue
        seen[k] = len(Q)
        Q.append(['Pro Genius Academy', it['question'], it['options'], it['correct'], it['why'], it['rel'], 1]); nn += 1
json.dump(Q, open(os.path.join(P, 'pg_final.json'), 'w', encoding='utf8'), ensure_ascii=False)
print('base %d, matched existing %d, repeated inside new %d, new %d -> %d MCQs, %d tests' % (len(base), nm, nd, nn, len(Q), (len(Q) + 49) // 50))
