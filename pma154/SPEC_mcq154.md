# Turn PMA 154 test-experience questions into MCQs (Hakeem Force Academy section)

Input: a JSON Lines file. Each line is one question that candidates remembered from the PMA initial test (Pakistan Military Academy, ASRC centres, tests of 2022 to 2024). Fields:
- `id`: integer input id (you must use it, see below)
- `q`: the question in English; `also_asked_as`: other wordings
- `repeat`: in how many candidate experiences it appeared
- `candidate_answers`: answers candidates wrote (may be wrong, outdated or empty); `sure`: a candidate sounded sure
- `kind`: verbal (intelligence test) or academic

The website already has 5720 MCQs on these topics. They are listed, one per line as `<number><TAB><question>`, in `/home/user/Asad/pma154/hk_existing.txt`.

## Step 1 for EVERY input line: is it already on the site?
Search `hk_existing.txt` with `grep -i` for one or two distinctive keywords of the question (try a synonym too, for example "capital" plus the country, or the key number). If an existing question asks the SAME fact (same answer, wording may differ; the same calculation with the same numbers), do NOT write an MCQ. Add `(<existing number>, <input id>)` to `DUPS`. Different numbers or a different fact (e.g. capital of Nepal vs capital of Bhutan, 90% of 90 vs 80% of 90) is NOT a duplicate.
Also merge lines inside your own input that ask the same fact into ONE MCQ (put all their ids in its `ids` list).

## Step 2: write MCQs for the rest
Write ONE Python file (path given in your assignment) defining:

QS = [ (section, question, options, correct_index, reason, related_fact, ids), ... ]
DUPS = [ (existing_number, input_id), ... ]

- `section`: always "Hakeem Force Academy".
- `question`: complete, clear English question. No label, no repeat number.
- `options`: 4 options (3 to 5 allowed): the correct answer plus 3 plausible wrong answers of the same type. Vary the position of the correct option.
- `correct_index`: 0-based index of the correct option.
- `reason`: 1 to 3 plain English sentences explaining why the answer is correct (show working for maths and series).
- `related_fact`: ONE sentence with a useful related fact.
- `ids`: list of the input ids this MCQ covers.
- Do NOT use the characters `<`, `>` or `&` anywhere. Use correct Python string quoting (double quotes for strings with an apostrophe).

## Correctness rules (very important)
1. Every answer must be correct TODAY (October 2026). Candidates wrote between 2022 and 2026, so anything that changes over time must be updated to the current answer and the old answer mentioned in related_fact (current office holders: President, PM, CMs, governors, chiefs, ministers, UN Secretary-General; records, rankings, champions, populations, seat counts). For every time-sensitive or doubtful fact you MUST use WebSearch (standard mode). WebSearch is a deferred tool: first call ToolSearch with query `select:WebSearch` to load it. Do not answer such items from memory.
2. Stable facts (history, geography, Islamic history, science): use your knowledge, but WebSearch anything you are not completely sure of. If sources disagree on a classic textbook answer, use the answer most Pakistani textbooks give and say in related_fact that sources differ.
3. Solve every maths, percentage, age, day, direction and series question yourself, step by step; use YOUR correct answer, not the candidate's.
4. If a line is too vague, garbled, incomplete, an instruction rather than a question, or has no single defensible answer, SKIP it (list it in your report). Do not guess.
5. Search only where needed (there is a search budget).

## Check and report
Run `python3 /home/user/Asad/pma154/check154.py <your file>` and fix every problem. Reply SHORT: file path, MCQs written, dups found, input lines, number skipped. Do not paste questions back.
