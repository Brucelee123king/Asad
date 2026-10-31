# Format QA report

Data: 8931 records, not modified. Scripts: qa/scan.py (defects), qa/spell.py (spelling, whitelist.txt), qa/make_fixes.py (outputs).

## Counts per defect type (raw hits)

- bad_ok: 0 - invalid ok index
- bracket_mismatch: 8 - unbalanced brackets
- double_space: 0 - double spaces
- edge_space: 0 - leading/trailing space
- encoding: 0 - mixed-encoding chars
- lead_number_q: 0 - leading "12." in question
- marker: 4 - leftover markers [ ] => Answer:
- no_qmark: 9 - no "?" (8 are "(current affairs)" suffix, 1 series)
- nonstring: 0 - non-string fields
- opt_count: 178 - records with 3 or 5 options (22 have 3, 156 have 5, mostly Forces Academy)
- opt_dup: 1 - duplicate options
- opt_empty: 0 - empty options
- opt_in_question: 140 - option text (>8 chars) also in question (mostly legit)
- opt_long: 49 - options >150 chars
- opt_prefix: 15 - option starts with A)/1. (all false positives: initials like "A. K. Huq")
- quote_mismatch: 5 - odd number of double quotes
- repeated_word: 2 - repeated word in question
- spaced_ordinal: 0 - digit + spaced ordinal
- stray_letter_end: 83 - question ends with single letter (almost all legit: A/B/x/y in maths/reasoning)
- stuck_ordinal: 0 - question ends with stuck rd/th/st

## Proposed fixes (format_fixes.json): 4
- 2x "Surah An-Naml, =)" -> "Surah An-Naml" (#113, #173)
- 2x "lonian" -> "Ionian" (#570, #928)

## Not applied (need human decision)
- 17 OCR garbles in facts ("/slamabad" for Islamabad etc.) in facts_candidates_not_applied.json; facts were not to be touched.
- Many other garbled facts (e.g. #194, #254, #450 "<i] A ee nO", #830, #865 "astronom Wy") need source text.
- Q prefixes: "(Original MCQ #n)" on all 1000 src=orig and none elsewhere; "(Forces Academy Test t · Qn)" on all 771 FA. Consistent.
- 8 questions end "(current affairs)" without "?" (#1229-1236); #6729 series question has no "?".
- Forces Academy questions with options embedded in q text (e.g. #1821 "A. K, B. L, C. M"); 178 records with 3/5 options.
- Options with same text as question/odd distractors in src=orig (e.g. #570 "The National Assembly", #173 duplicate An-Naml, #6816 Ff/Ee/Ed/EE case-only dup).
- Quote mismatch #70,#76,#186,#205: curly open quote with straight close quote (cosmetic).
- Spelling: British spellings (metres, centre, colour) used consistently, left alone. Deliberate misspelling options (e.g. #1284, #2722, #3197, #6831) are intended. Whitelist in whitelist.txt.
