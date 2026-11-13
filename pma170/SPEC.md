# Add the MCQs of the user's PDF (PMA ALL Centers Academic) to the PMA 159 MCQ section

Context: the site has 623 existing PMA 159 MCQs (list: /home/user/Asad/pma170/pma159_existing.txt, one per line `<index><TAB><question>  => <correct answer>`, indexes 0..622). The PDF text was parsed into /home/user/Asad/pma170/items.json: id, text (the question), answer (the PDF's answer), facts (the PDF's "Related Facts"), count (how often the same question appears in the PDF). The PDF has NO options. You get a SLICE of item ids.

## For each item decide MATCH, NEW or SKIP
- MATCH: the existing list already has an MCQ that asks the SAME fact (same content AND same correct answer; wording may differ; for maths/day questions the numbers must be the same). grep -i with keywords/synonyms (several tries). Output `(item_id, existing_index)`. The repeat count rises by the item count automatically.
- NEW: write `(item_id, section, question, correct_answer, [wrong1, wrong2, wrong3], reason, rep)` with rep = count - 1.
  - section one of: "Pakistan Studies", "Verbal: Maths & Reasoning", "Islamiat", "General Knowledge", "Verbal: English", "Maths & Science", "Current Affairs".
  - Turn the PDF question into a clear, complete, indisputable exam MCQ with exactly 3 plausible wrong options. The correct answer must be short (a name, number, year, place), taken from the PDF answer but CHECKED: verify facts with WebSearch (deferred tool: first ToolSearch with query `select:WebSearch`) on at least one reliable source, two for current-affairs or surprising claims. Answers must be right for TODAY, October 2026 (KP under Governor's rule since 11 Oct 2026; 27th Amendment Nov 2025; Field Marshal Asim Munir is COAS and CDF). If the PDF answer is wrong, use the right one and say so in your report.
  - reason = the PDF "Related Facts" rewritten as one to three clear English sentences (key fact first). The user wants these shown after the answer.
  - Do not use the characters < > & anywhere. Do not invent questions that are not in the PDF.
- SKIP (put in SKIPPED with reason): items marked AMBIGUOUS/DISPUTED/incomplete in the PDF where no single indisputable answer can be fixed, incomplete English sentences without options, metric-dependent ("smallest dam", "hottest country") etc.
## Output
Write Python file `/home/user/Asad/pma170/m_sNN.py` (NN = slice number) with `MATCH = [...]`, `NEW = [...]`, `SKIPPED = {item_id: "reason"}`. Validate with `python3 /home/user/Asad/pma170/check170.py /home/user/Asad/pma170/m_sNN.py` and fix problems. Reply SHORT: item count, MATCH, NEW, skipped ids with reason, any PDF answers you corrected, and weakly verified items.
