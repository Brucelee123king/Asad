import re, runpy, sys
m = runpy.run_path(sys.argv[1]); MATCH = m.get("MATCH", []); NEW = m.get("NEW", [])
SECS = {"Pakistan Studies","Verbal: Maths & Reasoning","Islamiat","General Knowledge","Verbal: English","Maths & Science","Current Affairs"}
bad = 0
for t in MATCH:
    if not (isinstance(t, tuple) and len(t) == 2 and all(isinstance(x, int) for x in t) and 0 <= t[1] < 332): print("bad MATCH", t); bad += 1
for t in NEW:
    p = []
    if not (isinstance(t, tuple) and len(t) == 7): print("NEW needs 7 fields", str(t)[:60]); bad += 1; continue
    n, sec, q, ok, wrong, why, rep = t
    if sec not in SECS: p.append("bad section")
    if not (isinstance(wrong, list) and len(wrong) == 3): p.append("need 3 wrong options")
    elif len({ok, *wrong}) != 4: p.append("duplicate options")
    if not isinstance(rep, int): p.append("rep int")
    for f in (q, ok, why, *wrong):
        if re.search(r"[<>&]", str(f)): p.append("forbidden char"); break
        if not str(f).strip(): p.append("empty field"); break
    if p: print(f"#{n}", "; ".join(p)); bad += 1
print(len(MATCH), "match,", len(NEW), "new,", bad, "problems")
