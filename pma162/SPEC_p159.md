# Merge a new PMA 159 experience file into the PMA 159 MCQ section

Context: the site has 269 existing PMA 159 MCQs (list: /home/user/Asad/pma162/pma159_existing.txt, one per line `<index><TAB><question>  => <correct answer>`). A new candidate file ("PMA 159 Experience", 74 MCQs with 4 options and the author's answer and a short Roman-Urdu explanation) is parsed in /home/user/Asad/pma162/src_items.json (fields n, q, opts, ans letter, ans_text, expl).

For EACH source item in your range decide:
1. MATCH: the existing list already has an MCQ that asks the SAME fact (same question content and same correct answer; the wording may differ; for maths/days/percentage questions the numbers must be the same). Use `grep -i` on pma159_existing.txt with key words and numbers (also try synonyms and the answer). Different numbers or a different fact is NOT a match. Output `(source_n, existing_index)`.
2. NEW: no such MCQ exists. Write a new MCQ in the site's format: `(source_n, section, question, correct_answer, [wrong1, wrong2, wrong3], reason, 0)`.
   - section must be one of: "Pakistan Studies", "Verbal: Maths & Reasoning", "Islamiat", "General Knowledge", "Verbal: English", "Maths & Science", "Current Affairs".
   - The correct answer must be TRUE today (October 2026). The author's marked answer can be wrong or outdated: solve maths yourself; verify facts, office holders and records with WebSearch (a deferred tool: first call ToolSearch with query `select:WebSearch`) when there is any doubt. Keep the author's 4 options when they are fine (correct answer plus the 3 others), otherwise improve the wrong options so exactly one is right.
   - reason: one or two clear English sentences with the working or the key fact (translate and improve the author's Roman Urdu explanation).
   - Do not use the characters < > & anywhere. Do not add MCQs of your own that are not in the source file. If an item has no single defensible answer, skip it and report its number.
   - If two source items in your range are the same question, write it once and give the repeat count as the last number (the number of EXTRA times it appears), otherwise 0.

## Output
A Python file (path in your assignment) defining `MATCH = [...]` and `NEW = [...]`. Validate with `python3 /home/user/Asad/pma162/check162.py <your file>`. Every source item in your range must be accounted for exactly once (MATCH, NEW or skipped). Reply SHORT: output path, number of MATCH, number of NEW, skipped numbers.
