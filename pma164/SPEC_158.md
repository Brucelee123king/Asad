# Turn the "PMA 158 Long Course" experience list into MCQs

Audience: candidates of the Pakistan Army PMA initial test.

## Files
- Source: /home/user/Asad/pma164/clean.txt. A candidate list of numbered items (1 to 226): short questions, many with the author's answer in brackets, some without any answer. The author's answers can be wrong, doubtful or outdated ("current" office holders). Some items are partial or vague.
- Output: a Python file (path in your assignment) with `QS = [...]`, each item a 7-tuple:
  ("PMA 158 Long Course", question, [option1, option2, option3, option4], correct_index (0-based), reason, related_fact, repeat_count)
- Validate with `python3 /home/user/Asad/pma164/check164.py <your file>` and fix every problem.

## Rules
- Make one MCQ per source item in the source order (keep the order). Do NOT invent MCQs that are not in the list. If an item contains several questions, make one MCQ per question.
- Write a clear exam-style question with 4 options (the correct answer plus 3 plausible wrong ones). Keep every number and name of the source.
- The correct answer must be TRUE today (October 2026). Solve maths, days of the month (shift by remainder mod 7), directions, series and letter puzzles yourself. Verify facts with WebSearch (a deferred tool: first call ToolSearch with query `select:WebSearch`): office holders (Chief Ministers, ministers, army/naval chiefs, Foreign Ministers), records, dates, numbers (area of Pakistan, peaks, battles, nuclear tests, Islamic history numbers such as Badr 313, number of ghazwas, number of Prophets named in the Quran). Where the printed answer is wrong or outdated use the true answer and say so in the reason.
- If an item is too vague, has no single defensible answer, or its answer is disputed among sources (for example the exact number of Quran copies of Hazrat Usman, who was "first Chief Justice", "first Chief of Army Staff"), either reword it into a well-defined question (only when the meaning stays the same, for example "Who was the first Pakistani Commander-in-Chief of the Pakistan Army?") or skip it and list its number in your reply.
- reason: one or two clear English sentences with the working or the key fact. related_fact: one more true fact that helps remember it.
- repeat_count: 1 normally. If the same question appears twice in your range write it once with the number of appearances.
- Do not use the characters < > & anywhere.
- Reply SHORT: output path, number of MCQs, skipped item numbers with a few words of reason. Do not paste MCQs.
