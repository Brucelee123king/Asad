# Merge paraphrased repeats found by the review of hk_final4 (dup_pairs_text.json: pairs of question texts).
# Earlier-placed MCQ is kept; repeat counts are added. hk_final4/hk_origin4 -> hk_final5/hk_origin5
import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = json.load(open('hk_final6.json')); org = json.load(open('hk_origin6.json'))
idx = {x[1]: i for i, x in enumerate(f)}
par = list(range(len(f)))
def fd(i):
    while par[i] != i: par[i] = par[par[i]]; i = par[i]
    return i
miss = 0
for a, b in json.load(open('dup_pairs_text.json')):
    if a in idx and b in idx:
        x, y = fd(idx[a]), fd(idx[b])
        if x != y: par[max(x, y)] = min(x, y)
    else: miss += 1
groups = {}
for i in range(len(f)): groups.setdefault(fd(i), []).append(i)
out = []; oo = []
for i, x in enumerate(f):
    if fd(i) != i: continue
    x = list(x); x[6] = sum(f[j][6] for j in groups[i]); out.append(x); oo.append(org[i])
json.dump(out, open('hk_final7.json', 'w'), ensure_ascii=False); json.dump(oo, open('hk_origin7.json', 'w'))
print(len(f), '->', len(out), 'pairs not found (removed by overrides):', miss)
