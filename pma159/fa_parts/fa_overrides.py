"""Corrections found by the independent blind check. Labels match the start of each question text."""
REMOVE = [
    "(Forces Academy Test 4 · Q7)",    # Date/Calendar/Year/Day/Minute: calendar vs minute, no single defensible odd one
    "(Forces Academy Test 7 · Q5)",    # sports odd-one-out: key (badminton) and logic (football) disagree
    "(Forces Academy Test 13 · Q18)",  # K LL MMM NNN? : question is garbled
    "(Forces Academy Test 14 · Q5)",   # paired series with no clear rule
    "(Forces Academy Test 14 · Q20)",  # all four are units of weight; no clean odd one
    "(Forces Academy Academic · Line 106)",  # '25th Prime Minister': numbering differs by source
]
# label -> dict of changes: correct (index), reason, rel
FIX = {
    "(Forces Academy Test 1 · Q19)": {
        "correct": 0,
        "reason": "Easy and light both mean not hard or heavy to deal with, and rough is closest to hard (a rough surface feels hard and coarse). The paper's answer key gives Hard.",
    },
    "(Forces Academy Test 3 · Q20)": {
        "correct": 1,
        "reason": "The differences are 10, 8, 6, 4, so the next difference is 2: 6 - 2 = 4.",
    },
    "(Forces Academy Test 12 · Q18)": {
        "append_reason": " Another reading of the gaps (2, 3, 5, 8) would give T, but the paper's answer key is U.",
    },
    "(Forces Academy Test 13 · Q21)": {
        "append_reason": " Another reading of the gaps (2, 3, 5, 8) would give T, but the paper's answer key is U.",
    },
    "(Forces Academy Academic · Exam World 52)": {
        "rel": "Musharraf kept the title of Chief Executive until 2002 in some accounts, but the chart counts it until he became President in June 2001.",
    },
}
