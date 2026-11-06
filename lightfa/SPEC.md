# Light Forces Academy MCQs (new category in the Asadullah Notes PMA app)

Sources (folder /home/user/Asad/lightfa): pdf/seerah.pdf (77 MCQs with options and answers), pdf/lc100.pdf (100 short
question/answer pairs, no options), pdf/experiences.pdf (11 students' PMA 159 test experiences, remembered questions).
Text copies: seerah_raw.txt, lc100_raw.txt, exp_raw.txt (watermark letters like "L", "IG", "ESTABLISHED", "EXCELLENCE",
"IN EDUCATION" are noise). Read the PDF pages with the Read tool when the text is garbled.

Write ONE JSON file (path given in your task): a list of MCQs, each
{"question": str, "options": [4 strings], "correct": 0-3, "why": str, "rel": str, "rep": int, "src": str, "note": str}
- The answer MUST be correct for TODAY, 25 October 2026. If the PDF's answer is wrong or outdated, use the correct one and
  say so in "note" (e.g. "PDF said X"). Office holders: search the latest news (deferred tool: ToolSearch "select:WebSearch").
  Pakistan facts to remember: KP is under Governor's rule since 11 Oct 2026 (check), 27th Amendment Nov 2025 changed
  military posts; Field Marshal Asim Munir is COAS and Chief of Defence Forces.
- Verify every answer you are not 100% sure of with web search (2 sources). If sources disagree or the question is unclear, leave it out and list it in your reply.
- 4 options, exactly one right, wrong options plausible but clearly wrong; spread the correct position over A-D.
  For seerah.pdf keep the PDF's own options (fix only if two could be right or the key is wrong).
- "why": simple English, 2-4 short sentences: why the answer is right AND one short part on why the other options are wrong.
- "rel": 1-2 related, similar facts that help to remember (correct facts only).
- "rep": for experiences only: (number of write-ups that asked it) - 1, else 0. Write a repeated question once.
- "src": e.g. "seerah 12", "lc100 33", "exp 4".
- For experiences: turn every clear remembered academic/verbal question into a full MCQ; skip vague ones (no options known
  AND no clear answer). Do not invent questions the write-ups did not mention.
- No "<" or ">" characters. Plain text. Validate the JSON with python3 (list, fields, 4 options, correct in 0-3, no duplicate options).
Reply SHORT: count written, PDF answers you changed (with reason), items left out (with reason).
