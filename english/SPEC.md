# Task: check English MCQs and write a short reason for each (for PMA students, simple English)
Input: /home/user/Asad/english/chunks/<NAME>.json = list of {"n","q","options":[A,B,C,D],"key":"A-D" (the book's answer),"expl" (book explanation, may be empty),"passage" (reading passage text for comprehension questions, else null)}.
For EVERY item:
1. Solve it yourself (grammar/vocabulary/comprehension). For comprehension use only the passage.
2. If the book key is right, keep it. If the book key is clearly wrong, use the right option and say why in "note". If two options are equally right or the question is broken, set "skip": true with a note.
3. "reason" = 1-2 short simple sentences: the rule or meaning that makes the answer right (you may reuse the book explanation). For comprehension, quote the idea from the passage.
4. "question": the question text, cleaned (keep blanks as ___). For comprehension items start the question with the passage title in brackets, e.g. "[Passage 1 - Discipline and Performance] The central idea of the passage is that discipline:"; and put the full passage text in "passage".
Do not use the characters < > in any text (write "less than" or similar if needed).
Output: write /home/user/Asad/english/out/<NAME>.json = list of {"src":"<NAME>-<n>","question","options":[4 strings],"correct":0-3,"book_key":"A-D","reason","passage":null|"...","skip":false,"note":""}. Validate with python (valid JSON, 4 options, correct in 0-3). Do not edit other files. Reply in 3 lines: count, how many book keys you changed (list n), how many skipped (list n).
