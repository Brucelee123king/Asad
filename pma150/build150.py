# Build Hakeem data = PMA 149 MCQs (counts increased by PMA 150 repeats) + new PMA 150 MCQs
import json, glob, runpy, re, collections, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
hk = json.load(open('../pma149/hk_final.json', encoding='utf8'))
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
try: ov = json.load(open('hk150_overrides.json', encoding='utf8'))
except FileNotFoundError: ov = {"remove": [], "fix": {}}
# merge new MCQs that ask exactly the same question
def norm(q): return re.sub(r'[^a-z0-9]+', ' ', q.lower()).strip()
byq = collections.OrderedDict()
for sec, q, o, a, why, rel, ids in new:
    if any(q.startswith(r) for r in ov['remove']): continue
    k = norm(q)
    if k in byq: byq[k][6] = sorted(set(byq[k][6]) | set(ids))
    else: byq[k] = [sec, q, o, a, why, rel, list(ids)]
out_new = []
for sec, q, o, a, why, rel, ids in byq.values():
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
    final.append(x)
final += out_new
json.dump(final, open('hk_final2.json', 'w', encoding='utf8'), ensure_ascii=False)
print('existing', len(hk), 'raised', len(add), '(writer dups', ndup, ') new', len(out_new), 'total', len(final), 'blocks', (len(final) + 49) // 50)
print('top existing now:', [(x[6], x[1][:30]) for x in final[:5]])
