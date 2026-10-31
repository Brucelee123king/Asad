# Build Hakeem data = PMA 149 MCQs (counts increased by PMA 150 repeats) + new PMA 150 MCQs
import json, glob, runpy, re, collections, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
hk = json.load(open('../pma152/hk_final5.json', encoding='utf8'))
un = json.load(open('unmatched.json', encoding='utf8'))
add = {int(k): set(v) for k, v in json.load(open('hk_add.json')).items()}
new = []; ndup = 0
mq = set(json.load(open('matched_q.json', encoding='utf8')))
skip_ids = {i for i, c in enumerate(un) if c['q'] in mq}
for f in sorted(glob.glob('mcq_out/m_*.py')):
    m = runpy.run_path(f)
    for e, i in m.get('DUPS', []):
        if 0 <= e < len(hk) and 0 <= i < len(un) and i not in skip_ids: add.setdefault(e, set()).update(un[i]['all_exps']); ndup += 1
    for t in m['QS']:
        t = list(t); t[6] = [i for i in t[6] if i not in skip_ids]
        if t[6]: new.append(t)
try: ov = json.load(open('hk153_overrides.json', encoding='utf8'))
except FileNotFoundError: ov = {"remove": [], "fix": {}}
# merge new MCQs that ask exactly the same question
def norm(q): return re.sub(r'[^a-z0-9]+', ' ', q.lower()).strip()
byq = collections.OrderedDict()
for sec, q, o, a, why, rel, ids in new:
    if any(q.startswith(r) for r in ov['remove']): continue
    k = norm(q)
    if k in byq: byq[k][6] = sorted(set(byq[k][6]) | set(ids))
    else: byq[k] = [sec, q, o, a, why, rel, list(ids)]
# merge near-duplicate new MCQs (same correct answer, same numbers, similar wording) and
# fold new MCQs that repeat an existing MCQ into that MCQ's count
STOPW = set("the a an of is was in on for to what which who whom does do did are were name any has have had be as at by from and or it its this that with how many much when where why whose will would can could should there their they them we you your i he she his her our us me my called known first current currently present as of 2026 october".split())
def tk(s): return frozenset(w for w in re.sub(r"[^a-z0-9 ]+", ' ', s.lower()).split() if w not in STOPW)
def nums(s): return tuple(sorted(re.findall(r'\d+', re.sub(r'\b(as of|in) (october )?2026\b', '', s.lower()))))
def ans(x): return re.sub(r'[^a-z0-9]+', ' ', x[2][x[3]].lower()).strip()
vals = list(byq.values()); par = list(range(len(vals)))
def fd(i):
    while par[i] != i: par[i] = par[par[i]]; i = par[i]
    return i
grp = collections.defaultdict(list)
for i, x in enumerate(vals): grp[(ans(x), nums(x[1]))].append(i)
for ids in grp.values():
    for p in range(len(ids)):
        for q in range(p + 1, len(ids)):
            A, B = tk(vals[ids[p]][1]), tk(vals[ids[q]][1])
            if A and B and len(A & B) / len(A | B) >= 0.4: par[fd(ids[q])] = fd(ids[p])
merged = collections.OrderedDict()
for i, x in enumerate(vals):
    r = fd(i)
    if r in merged: merged[r][6] = sorted(set(merged[r][6]) | set(x[6]))
    else: merged[r] = list(x)
hkg = collections.defaultdict(list)
for i, x in enumerate(hk): hkg[(ans(x), nums(x[1]))].append(i)
nfold = 0; keep = []
for x in merged.values():
    hit = None
    for i in hkg.get((ans(x), nums(x[1])), []):
        A, B = tk(x[1]), tk(re.sub(r'\s*\(\d+\)\s*$', '', hk[i][1]))
        if A and B and len(A & B) / len(A | B) >= 0.5: hit = i; break
    if hit is None: keep.append(x); continue
    nfold += 1
    for j in x[6]:
        if 0 <= j < len(un): add.setdefault(hit, set()).update(un[j]['all_exps'])
print('near-duplicate merge:', len(vals), '->', len(merged), '; folded into existing:', nfold)
out_new = []
for sec, q, o, a, why, rel, ids in keep:
    f = next((v for k, v in ov['fix'].items() if q.startswith(k)), None)
    if f:
        o = f.get('options', o); a = f.get('correct', a); why = f.get('reason', why); rel = f.get('rel', rel); q = f.get('question', q)
    exps = set()
    for i in ids:
        if 0 <= i < len(un): exps.update(un[i]['all_exps'])
    out_new.append([sec, q, o, a, why, rel, max(1, len(exps))])
out_new.sort(key=lambda x: -x[6])
final = []
for i, x in enumerate(hk):
    x = list(x); x[6] = x[6] + len(add.get(i, ()))
    f = next((v for k, v in ov['fix'].items() if x[1].startswith(k)), None)
    if f:
        x[1] = f.get('question', x[1]); x[2] = f.get('options', x[2]); x[3] = f.get('correct', x[3]); x[4] = f.get('reason', x[4]); x[5] = f.get('rel', x[5])
    final.append(x)
final += out_new
json.dump(final, open('hk_final6.json', 'w', encoding='utf8'), ensure_ascii=False)
json.dump(json.load(open('../pma152/hk_origin5.json')) + [153] * len(out_new), open('hk_origin6.json', 'w'))
print('existing', len(hk), 'raised', len(add), '(writer dups', ndup, ') new', len(out_new), 'total', len(final), 'blocks', (len(final) + 49) // 50)
print('top existing now:', [(x[6], x[1][:30]) for x in final[:5]])
