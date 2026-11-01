# Task: turn YOUR chunk of Pro Genius PMA 159 questions (question + answer, no options) into checked MCQs
Input: /home/user/Asad/progenius/pg2/c<N>.json = list of items {"id","q" (question),"ans" (answer as printed),"facts" (list of notes)}. Items are Pakistan Military Academy (PMA) Long Course initial-test questions.
Also read /home/user/Asad/progenius/pg2/existing_pg.txt: the 299 MCQs ALREADY in the app (index <TAB> question => answer).
For EVERY item:
0. MATCH: if the item asks the same thing as an existing MCQ (same meaning AND same answer, wording may differ), set "match": that index (number). Otherwise "match": null. Still write the MCQ below either way.
1. CHECK THE ANSWER. Today is 1 November 2026. Use your knowledge carefully (Pakistan affairs, Islamiat, GK, current affairs, English, maths, science). Solve maths/reasoning yourself. If the printed answer is wrong or outdated, use the correct answer, "status":"fixed" with a short "note". If you cannot be sure (very recent 2026 events, opinion items), keep the printed answer, "status":"unsure" with a note. Otherwise "status":"ok".
2. Write a clear question in simple English (fix spelling/grammar; keep the meaning). Turn statements/topics like "Army chief during 1965 war" into a real question. Opinion items ("Why is milk boiled?") become a fair MCQ with one clearly best answer.
3. Exactly 4 options: the correct answer (short, no "as of" text) + 3 believable wrong options of the same kind (no "All of the above", no joke options, no two options that could both be right). Correct one in a random position.
4. "why": 1-2 short sentences why the answer is correct (use the notes if right).
5. "rel": one short related fact (different from "why"; the notes' extra facts are good for this).
Output: /home/user/Asad/progenius/pg2/out/c<N>.json = JSON list, same order as input, each {"id","question","options":[4],"correct":0-3,"why","rel","status":"ok|fixed|unsure","note","match":null|index}.
Validate with python at the end (valid JSON, same count as input, 4 options each, correct 0-3, no duplicate options). Write the file in parts while you work, final file complete. Do not edit other files. Reply SHORT: count written, number of matches, list of "fixed" ids with one line each, count of "unsure".
