# Turn extracted PMA 149 questions into MCQs

Your input is a JSON Lines file. Each line is one distinct question that candidates remembered from the PMA initial test (Pakistan Military Academy, ASRC centres, tests held in 2021-22): fields
- `q`: the question in English
- `also_asked_as`: other wordings of the same question seen
- `repeat_estimate`: in how many different candidate experiences it appeared (an upper-bound estimate; wordings were merged automatically)
- `experiences`: the experience numbers
- `candidate_answers`: answers candidates wrote (may be wrong, may be outdated, may be empty)
- `sure`: true when a candidate sounded sure of the answer
- `kind`: verbal (intelligence test) or academic

Write ONE Python file (path given in your assignment) defining `QS = [ ... ]`, a list of 7-tuples:

(section, question, options, correct_index, reason, related_fact, repeat)

- `section`: always "Hakeem Force Academy".
- `question`: complete, clear English question. No label and no repeat note inside it (the site adds "(Repeated in N tests)" itself).
- `options`: 4 options (3 to 5 allowed): the correct answer plus 3 plausible wrong answers of the same type (similar years, neighbouring names, typical mistakes). Vary the position of the correct option.
- `correct_index`: 0-based index of the correct option.
- `reason`: 1 to 3 plain English sentences explaining why the answer is correct (show working for maths and series).
- `related_fact`: ONE sentence with a useful related fact.
- `repeat`: integer, the number of DISTINCT experiences the question appeared in. If you merge near-duplicate lines, use the size of the union of their `experiences` lists.
- Do NOT use the characters `<`, `>` or `&` anywhere. Use correct Python string quoting.

## Correctness rules (very important)
1. Every answer must be correct TODAY (October 2026). Candidates wrote their answers in 2021-22, so anything that changes over time must be updated to the current answer, and the old answer mentioned in related_fact. Examples: current Chief Minister of Punjab is Maryam Nawaz (not Usman Buzdar), current office holders (President, Prime Minister, Chief Justice, army chief, governors, ministers), latest records and rankings, population ranking (India is now the most populous country), current champions and winners, current figures (seat counts, populations, prices). For every time-sensitive or doubtful fact you MUST use the WebSearch tool (standard mode) and rely on a reliable source. Do not answer such items from memory.
2. For stable facts (history, geography, Islamic history, science) use your knowledge but double-check anything you are not completely sure of with WebSearch. If sources disagree on a classic textbook answer, use the answer most Pakistani textbooks give and say in related_fact that sources differ.
3. Solve every maths, percentage, age, day, direction and series question yourself, step by step. Check the candidate answer; use YOUR correct answer. If a verbal puzzle is garbled, incomplete or has no defensible single answer, SKIP it.
4. If the question is too vague, a duplicate of another question in your file, or you cannot find a reliable answer, SKIP it and list it in your report. Do not guess. Merge true duplicates into one MCQ.
5. Keep search use reasonable: search only where needed (time-sensitive or doubtful facts), because there is a per-session search budget.

## Check and report
Run `python3 /home/user/Asad/pma149/check_hk.py <your file>` and fix every problem. Reply (short) with: the file path, number of MCQs written, number of input lines, the skipped questions with a reason (very short), and the questions whose answer you changed from the candidates' answer because it was outdated or wrong (question and new answer).


## Extra rules for this batch (phase 2: questions mentioned in only one experience)
- WebSearch is a deferred tool in your environment: before using it, call ToolSearch with the query `select:WebSearch` so that its schema is loaded. Then use it for every time-sensitive or doubtful fact (office holders, records, rankings, currencies, populations, recent events, anything dated after 2020). Do NOT skip searching because the tool "was not loaded".
- The file /home/user/Asad/pma149/phase1_questions.txt lists the questions that already have MCQs (one per line). Before writing an MCQ, run a quick `grep -i` on a distinctive keyword of your question in that file. If the same fact is already covered there, SKIP yours (do not write a duplicate). If your question is a different fact or a different number or version of a similar question, write it.
- These questions were each noted by a single candidate, so some are fragments or garbled. Write an MCQ only when you can state ONE clear, correct, defensible answer. Otherwise skip it and list it in your report.
- "repeat" for every MCQ in this batch is 1 (or the number of distinct experiences if you merge duplicates inside your own file).
