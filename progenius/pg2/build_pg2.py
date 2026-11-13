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
DUP = json.load(open(os.path.join(H, 'dups.json'))) if os.path.exists(os.path.join(H, 'dups.json')) else {}
byq = {norm(x[1]): i for i, x in enumerate(Q)}
for f in sorted(glob.glob(os.path.join(H, 'out', 'c*.json')), key=lambda s: int(re.findall(r'c(\d+)', s)[-1])):
    for it in json.load(open(f, encoding='utf8')):
        m = it.get('match')
        if isinstance(m, int) and 0 <= m < len(base):
            Q[m][6] += 1; nm += 1; continue
        nq = norm(it['question'])
        if nq in DUP and DUP[nq] in byq:
            Q[byq[DUP[nq]]][6] += 1; nd += 1; continue
        k = key(it['question'], it['options'][it['correct']])
        if k in seen:
            Q[seen[k]][6] += 1; nd += 1; continue
        seen[k] = len(Q); byq.setdefault(nq, len(Q))
        Q.append(['Pro Genius Academy', it['question'], it['options'], it['correct'], it['why'], it['rel'], 1]); nn += 1

# Pro Genius "Solved Academic Experience" PDF (pg3/out/c*.json): match = index in the list above (after pg2); why = PDF explanation word for word
SKIP3 = {'C35', 'C28'}   # C35 is C1 printed twice; C28 had no real question in the PDF
n3m = n3n = 0
for f in sorted(glob.glob(os.path.join(P, 'pg3', 'out', 'c*.json'))):
    for it in json.load(open(f, encoding='utf8')):
        if it['id'] in SKIP3: continue
        m = it.get('match')
        if isinstance(m, int) and 0 <= m < len(Q):
            Q[m][6] += 1; n3m += 1; continue
        k = key(it['question'], it['options'][it['correct']])
        if k in seen: Q[seen[k]][6] += 1; n3m += 1; continue
        seen[k] = len(Q)
        Q.append(['Pro Genius Academy', it['question'], it['options'], it['correct'], it['why'], it['rel'], 1]); n3n += 1
print('pg3: matched %d, new %d' % (n3m, n3n))
json.dump(Q, open(os.path.join(P, 'pg_final.json'), 'w', encoding='utf8'), ensure_ascii=False)
print('base %d, matched existing %d, repeated inside new %d, new %d -> %d MCQs, %d tests' % (len(base), nm, nd, nn, len(Q), (len(Q) + 49) // 50))
