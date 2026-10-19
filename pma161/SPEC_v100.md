# Turn the "100 most important verbal questions" list into MCQs (Hakeem Force Academy section)

Audience: candidates of the Pakistan Army PMA initial test (verbal intelligence part).

## Files
- Source: /home/user/Asad/pma161/src_text.txt. It is a candidate list of 100 numbered items. Most are STATEMENTS that give a question and its answer (for example "90% of 90 is 81." or "If 4th day of month is Friday then 19th day will be Saturday."). Some statements are WRONG on purpose or by mistake (for example "2+2/2=3" is right but "If 1st day of month is Monday, then the 12th day will be Saturday" is wrong), some say "not confirmed". Solve every item yourself.
- Existing site MCQs (6423, one per line `<number><TAB><question>`): /home/user/Asad/pma161/hk_existing.txt
- Output: a Python file (path in your assignment) with `QS = [...]`, each item a 7-tuple:
  ("Hakeem Force Academy", question, [option1, option2, option3, option4], correct_index (0-based), reason, related_fact, existing_number)
- Validate with `python3 /home/user/Asad/pma161/check161.py <your file>` and fix every problem.

## Rules
- Make exactly one MCQ per source question, in the source order. Do NOT invent MCQs of your own that are not in the list. Items that contain several questions (for example item 14 odd-one-out lines, item 18 series, item 21, item 24, item 95) become one MCQ per sub-question.
- Turn each statement into a clear question with 4 options: the correct answer plus plausible wrong ones. Use the wording style "If the 4th day of a month is Friday, what day will the 19th day be?". Keep every number of the source. The correct answer is the TRUE answer that you work out, not necessarily the one printed. If the printed answer is wrong, use the true one and say in the reason what the correct working is (and that the source statement is wrong).
- If an item cannot be given exactly one defensible answer (not enough data, ambiguous, for example item 1 about the 2nd day of the next month, items 69/70 which depend on options, item 83 and 88 with no answer, item 84), you may reword it into a well-defined question only when the meaning stays the same; otherwise skip it and list its number in your reply.
- reason: show the working in one or two sentences (the calculation, or the rule). related_fact: one useful extra fact or a shortcut for this question type (for example "Days: shift by the remainder after dividing the gap by 7").
- existing_number: if hk_existing.txt already has an MCQ asking the SAME question (same numbers, same answer; wording may differ), put its number; otherwise -1. Search with `grep -i` for key words and numbers (for example "90% of 90", "Friday" together with the day numbers). Different numbers is NOT the same question. Be careful and precise here: the repeat count shown on the site is taken from this existing MCQ.
- Do not use the characters < > & anywhere.
- Reply SHORT: output path, number of MCQs, number matched to existing, skipped item numbers. Do not paste MCQs.
