"""Validate a Forces Academy question file: python3 check_fa.py <file.py>"""
import re, runpy, sys
mod = runpy.run_path(sys.argv[1])
QS = mod["QS"]
bad = 0
for i, t in enumerate(QS, 1):
    where = f"#{i} {str(t[1])[:60]!r}"
    if len(t) != 6: print(where, "-> needs 6 fields"); bad += 1; continue
    sec, q, opts, ans, why, rel = t
    probs = []
    if not (isinstance(opts, list) and 3 <= len(opts) <= 5): probs.append("3-5 options required")
    elif len(set(map(str.strip, opts))) != len(opts): probs.append("duplicate options")
    elif not (isinstance(ans, int) and 0 <= ans < len(opts)): probs.append("bad correct index")
    for f in (q, why, rel, *opts):
        if re.search(r"[<>&]", str(f)): probs.append("contains < > or & : " + str(f)[:40]); break
    for name, f in (("question", q), ("reason", why), ("related", rel)):
        if not str(f).strip(): probs.append("empty " + name)
    if probs: print(where, "->", "; ".join(probs)); bad += 1
print(f"{len(QS)} questions, {bad} with problems")
