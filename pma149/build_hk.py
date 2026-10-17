"""Builds hk_final.json: merged Hakeem MCQs plus manual additions and fixes, sorted by repeat count (most repeated first)."""
import json
items = json.load(open('hk_merged_stage1.json', encoding='utf8'))
SEC = "Hakeem Force Academy"
extra = [
 [SEC, "How many faces does a triangular prism have?", ["5", "4", "6", "8"], 0,
  "A triangular prism has two triangular bases and three rectangular side faces: 2 + 3 = 5 faces.",
  "It also has 9 edges and 6 vertices. Candidates gave different answers (3, 4, 5, 6) because the paper did not name the prism type; the triangular prism is the usual one.", 27],
 [SEC, "Who was elected Chief Minister of Khyber Pakhtunkhwa in October 2025, succeeding Ali Amin Gandapur?", ["Sohail Afridi", "Mahmood Khan", "Pervez Khattak", "Amir Haider Khan Hoti"], 0,
  "Sohail Afridi of PTI was elected Chief Minister of Khyber Pakhtunkhwa in October 2025.",
  "When the candidates sat the test in 2021 the Chief Minister was Mahmood Khan. The post has been changing in the news, so check the latest position before an exam.", 10],
]
items += extra
try:
    ov = json.load(open('hk_overrides.json', encoding='utf8'))
except FileNotFoundError:
    ov = {"remove": [], "fix": {}}
out = []
for it in items:
    q = it[1]
    if any(q.startswith(r) for r in ov["remove"]): continue
    f = next((v for k, v in ov["fix"].items() if q.startswith(k)), None)
    if f:
        if "correct" in f: it[3] = f["correct"]
        if "options" in f: it[2] = f["options"]
        if "reason" in f: it[4] = f["reason"]
        if "rel" in f: it[5] = f["rel"]
        if "question" in f: it[1] = f["question"]
    out.append(it)
order = sorted(range(len(out)), key=lambda i: (-out[i][6], i))
final = [out[i] for i in order]
json.dump(final, open('hk_final.json', 'w', encoding='utf8'), ensure_ascii=False)

# ---- true repeat counts from the clusters (the helpers only saw the first 12 experience numbers) ----
import re, collections
STOP = set("the a an of is was in on for to what which who how many much does do did are were name why when where whom".split())
def toks(s):
    s = s.lower().replace('%', ' percent ')
    return frozenset(w for w in re.sub(r'[^a-z0-9.]', ' ', s).split() if w not in STOP)
clusters = json.load(open('clusters.json', encoding='utf8'))
ctok = []
for c in clusters:
    ctok.append([toks(v) for v in [c['q']] + c['variants'][1:2]])
inv = collections.defaultdict(list)
for ci, ts in enumerate(ctok):
    for w in ts[0]: inv[w].append(ci)
def nums(ts): return {w for w in ts if re.search(r'\d', w)}
changed = 0
for it in final:
    base = re.sub(r' \(\d+\)$', '', it[1])
    qt = toks(base)
    if not qt: continue
    cand = collections.Counter()
    for w in qt:
        if len(inv[w]) > 500: continue
        for ci in inv[w]: cand[ci] += 1
    tot = 0
    for ci, _ in cand.items():
        for ts in ctok[ci]:
            jac = len(qt & ts) / max(1, len(qt | ts))
            if jac >= 0.7 and nums(qt) == nums(ts):
                tot += clusters[ci]['repeat']; break
    if tot > it[6]:
        it[6] = tot; changed += 1
final.sort(key=lambda x: -x[6])
json.dump(final, open('hk_final.json', 'w', encoding='utf8'), ensure_ascii=False)
print("repeat counts raised for", changed, "MCQs; top:", [(f[6], f[1][:40]) for f in final[:12]])

print(len(final), "MCQs;", (len(final) + 49) // 50, "blocks; top repeats:", [f[6] for f in final[:8]], "; singles:", sum(1 for f in final if f[6] == 1))
