# Write MCQs on the Constitutions of Pakistan (1956, 1962, 1973) for the Hakeem Force Academy section

Audience: candidates of the Pakistan Army PMA initial test and ISSB. MCQs must be factual, exam style, with exactly one defensible answer.

## Files
- Source list (96 MCQs from a candidate PDF, answers marked by its author, SOME ARE WRONG): /home/user/Asad/pma160/src_mcqs.json (fields id, src, q, opts, ans letter). Text artefacts: superscripts such as "rd", "th", "st" were lost or stuck to words ("Constitution, of 1962 was made on rd").
- Existing site MCQs (6423, one per line `<number><TAB><question>`): /home/user/Asad/pma160/hk_existing.txt
- Output: a Python file (path in your assignment) defining `QS = [...]`, each item a 7-tuple:
  ("Hakeem Force Academy", question, [option1, option2, option3, option4], correct_index (0-based), reason, related_fact, existing_number)
  - 4 options (3 or 5 only when natural), no duplicate options. Do not use the characters < > & anywhere.
  - reason: one or two sentences explaining WHY the answer is correct (cite the article/date). related_fact: one extra true fact about the same topic that helps remembering.
  - existing_number: if hk_existing.txt already has an MCQ asking the SAME fact (same answer, wording may differ), put its number here; otherwise -1. Search with `grep -i` using one or two distinctive keywords (also try synonyms). A different fact (e.g. another article or another year) is NOT the same.
- Validate with: `python3 /home/user/Asad/pma160/check160.py <your file>` and fix every problem.

## Rules
- Every fact must be correct today (October 2026). Verify with WebSearch (a deferred tool: first call ToolSearch with query `select:WebSearch`) whenever you are not 100% sure: article numbers, dates, counts of articles, seats, ages, durations, amendment contents. Wikipedia pages "Constitution of Pakistan", "Constitution of Pakistan of 1956", "1962" and the list of amendments are good sources. Official wording: the 1973 Constitution has 280 articles, 12 parts, 7 schedules (check), Senate 96 seats, National Assembly 336 seats (266 general, 60 women, 10 non-Muslims, after the 25th Amendment of 2018) etc. Mention in the reason when a number changed by an amendment.
- Do not write an MCQ if the fact is disputed or you cannot verify it.
- Same style of question every time: "Under which Article of the 1973 Constitution ...?", "In which year ...?". No "all of the above" or "none of the above" options. Distractors must be plausible (nearby articles, years, numbers).
- Do not repeat the same fact twice within your file. Do not copy the source questions of another assigned part.
- Reply SHORT: output path, number of MCQs, number found in the existing list. Do not paste MCQs.
