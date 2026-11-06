import re, runpy, sys
m = runpy.run_path(sys.argv[1]); QS = m["QS"]; DUPS = m.get("DUPS", [])
bad = 0
for i, t in enumerate(QS, 1):
    w = f"#{i} {str(t[1])[:60]!r}"; p = []
    if len(t) != 7: print(w, "-> needs 7 fields"); bad += 1; continue
    sec, q, o, a, why, rel, ids = t
    if sec != "Hakeem Force Academy": p.append("wrong section")
    if not (isinstance(o, list) and 3 <= len(o) <= 5): p.append("3-5 options")
    elif len(set(map(str.strip, o))) != len(o): p.append("duplicate options")
    elif not (isinstance(a, int) and 0 <= a < len(o)): p.append("bad index")
    if not (isinstance(ids, list) and ids and all(isinstance(x, int) for x in ids)): p.append("ids must be a non-empty list of input ids")
    for f in (q, why, rel, *o):
        if re.search(r"[<>&]", str(f)): p.append("forbidden char: " + str(f)[:40]); break
    for n, f in (("question", q), ("reason", why), ("related", rel)):
        if not str(f).strip(): p.append("empty " + n)
    if p: print(w, "->", "; ".join(p)); bad += 1
for d in DUPS:
    if not (isinstance(d, tuple) and len(d) == 2 and all(isinstance(x, int) for x in d)): print("bad DUPS entry", d); bad += 1
print(f"{len(QS)} questions, {len(DUPS)} dups, {bad} with problems")
