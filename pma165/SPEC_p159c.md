# Add a solved-academic PDF to the PMA 159 MCQ section

Source: /home/user/Asad/pma165/pg/p-02.png ... p-12.png (page images of a PDF "PMA 159 Long Course - Initial Test Solved Academic Experience"; each page shows about 6 items: "Qn. question", "Answer: ...", "Explanation: ..."). Use the Read tool to view each page image of your range (it displays images). Page 1 is only an introduction.

Existing PMA 159 MCQs (332): /home/user/Asad/pma165/pma159_existing.txt, one per line `<index><TAB><question>  => <correct answer>`.

## Your job
1. Transcribe every item (Q number, question, the author's answer) in your pages. Number items by the printed Q number.
2. For EACH item decide:
   - MATCH: the existing list already has an MCQ asking the SAME fact (same content and same correct answer; wording may differ; for maths and days questions the numbers must be the same). Search with `grep -i` for key words, numbers and synonyms. Output `(q_number, existing_index)`.
   - NEW: otherwise write `(q_number, section, question, correct_answer, [wrong1, wrong2, wrong3], reason, rep)` with rep 0. section is one of: "Pakistan Studies", "Verbal: Maths & Reasoning", "Islamiat", "General Knowledge", "Verbal: English", "Maths & Science", "Current Affairs".
   - The correct answer must be TRUE today (October 2026). The author's answer can be wrong or outdated: solve maths yourself; verify facts, office holders and records with WebSearch (a deferred tool: first call ToolSearch with query `select:WebSearch`) when there is any doubt (for example "Deputy Prime Minister of Pakistan as of October 2026", the first Chief Justice, coastline length, Chief Ministers). If the author's answer is wrong use the true one and say so in the reason. Make three plausible wrong options. If an item has no single defensible answer, skip it and report its number.
   - reason: one or two clear English sentences with the key fact or working (improve the author's explanation).
   - Do not use the characters < > & anywhere. Do not add questions that are not in the PDF. If the same question appears twice in your pages, write it once and give the extra count as rep.
3. Output file (path in your assignment): Python with `MATCH = [...]`, `NEW = [...]`, and `ITEMS = {q_number: "short text"}` for all items you saw. Validate with `python3 /home/user/Asad/pma165/check165.py <file>`. Reply SHORT: items seen, MATCH count, NEW count, skipped numbers with reason.
