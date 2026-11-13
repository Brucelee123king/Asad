# Add friends' PMA 159 test-experience write-ups to the PMA 159 MCQ section

Context: the site has 645 existing PMA 159 MCQs (list: /home/user/Asad/pma171/pma159_existing.txt, one per line `<index><TAB><question>  => <correct answer>`). The raw write-ups (October 2026 initial tests) are in /home/user/Asad/pma171/raw.txt. The cleaned, de-duplicated list of remembered questions is /home/user/Asad/pma171/items.json (id, text, count = how many write-ups asked it). You get a SLICE of item ids. Candidates give almost no options or answers.

## For each item in your slice decide MATCH or NEW
- MATCH: the existing list already has an MCQ that asks the SAME fact (same content AND same correct answer; wording may differ; for maths and day questions the numbers must be the same). grep -i with keywords/numbers/synonyms (several tries). Output `(item_id, existing_index)`.
- NEW: write `(item_id, section, question, correct_answer, [wrong1, wrong2, wrong3], reason, rep)` with rep = count - 1 (so rep 0 if the item was asked once).
  - section one of: "Pakistan Studies", "Verbal: Maths & Reasoning", "Islamiat", "General Knowledge", "Verbal: English", "Maths & Science", "Current Affairs".
  - The question must be a clear, complete, indisputable exam MCQ. Use the raw.txt context to understand the intended question. Work out the correct answer yourself and VERIFY EVERY FACT with WebSearch on at least TWO different sites (deferred tool: first ToolSearch with query `select:WebSearch`); answers must be right for TODAY, October 2026 (office holders: search for the latest news; note KP is under Governor's rule since 11 Oct 2026, the 27th Amendment of Nov 2025 changed the judiciary/military posts, Field Marshal Asim Munir is Chief of Army Staff and Chief of Defence Forces). If two reliable sources disagree or the question stays unclear, SKIP it and report why.
  - Three plausible wrong options. reason = simple English, 2-4 short sentences: why the correct answer is right (key fact or the working) AND one short part on why the other options are wrong.
  - Do not use the characters < > & anywhere. Do not invent questions that the write-ups did not mention.
## Output
Write Python file `/home/user/Asad/pma171/m_sNN.py` (NN = your slice number) with `MATCH = [...]`, `NEW = [...]`, `SKIPPED = {item_id: "reason"}`. Validate with `python3 /home/user/Asad/pma171/check171.py /home/user/Asad/pma171/m_sNN.py` and fix problems. Reply SHORT: item count, MATCH, NEW, skipped ids with reason.

Extra notes for this batch (write-ups N67-N76):
- Items marked (unclear) or (check): decide carefully; SKIP if the intended question cannot be made clear and indisputable.
- 'World's largest city by population': use the latest UN World Urbanization Prospects (2025) result; say 'according to the UN (2025)' in the question if needed.
- Office holders (Air Chief, CM Balochistan): must be correct for 25 October 2026 - search the latest news.
- An existing MCQ with the same fact but a WRONG or outdated answer is NOT a match: write a NEW correct one and add a line to your reply 'FIX existing index N: ...'.
