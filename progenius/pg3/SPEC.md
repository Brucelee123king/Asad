# Task: read YOUR pages of a Pro Genius PDF (page images) and turn every question into a checked MCQ
Pages: /home/user/Asad/pma165/pg/p-NN.png (view them with the Read tool). Each page has items "Qn. question / Answer: ... / Explanation: ...". A question may start at the bottom of one page and its answer be on the next page: take items whose QUESTION NUMBER is printed on your pages; read the next page too if its answer continues there.
Also read /home/user/Asad/progenius/pg3/existing_pg.txt: the 681 MCQs ALREADY in the app (index <TAB> question => answer).
For EVERY item:
0. MATCH: if it asks the same thing as an existing MCQ (same meaning AND same answer), set "match": that index (number), else null. Still write the MCQ.
1. CHECK THE ANSWER. Today is 1 November 2026. If the printed answer is wrong or outdated, use the correct one, "status":"fixed" + short "note". If unsure (very recent events, disputed), keep it, "status":"unsure" + note. Else "ok". Maths items: solve them yourself.
2. Clear question in simple English (keep the meaning).
3. Exactly 4 options: the correct answer (short) + 3 believable wrong options of the same kind (no "All of the above", no two right options). Correct one in a random position.
4. "why": 1-2 short sentences (use the printed explanation if right). 5. "rel": one short related fact (different from why).
Output: /home/user/Asad/progenius/pg3/out/c<N>.json = JSON list in question-number order, each {"id":"C<question number>","question","options":[4],"correct":0-3,"why","rel","status","note","match":null|index}.
Validate with python (valid JSON, 4 different options, correct 0-3). Do not edit other files. Reply SHORT: question numbers covered, count, matches, fixed ids with one line each, unsure count.
