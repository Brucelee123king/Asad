# Forces Academy MCQ conversion: shared spec

You turn scanned Forces Academy (Lahore) practice material into MCQs for a quiz website. Another process merges your file with others, so follow the format exactly.

## Output
Write ONE Python file (path given in your assignment) that defines `QS = [ ... ]`, a list of 6-tuples:

```python
QS = [
 (section, question, options, correct_index, reason, related_fact),
]
```
- `section`: string given in your assignment (e.g. "Forces Academy Intelligence Test 5").
- `question`: the full question text in English, written out completely so it can be read without the paper. Start with the label given in your assignment, for example `(Forces Academy Test 5 · Q12) Which letter comes next: A, C, F, J, ?`. For series, write the whole series in the sentence.
- `options`: list of 3 to 5 strings. If the paper prints options (A, B, C, D, E or 1 to 5), copy them IN THE SAME ORDER without the letter prefix. If the paper gives no options (fill-in-the-blank, "which letter/number comes next", "write the answer"), create 4 options: the correct answer plus 3 plausible distractors (typical wrong answers someone might compute), and place the correct one at varying positions (do not always put it first).
- `correct_index`: 0-based index of the correct option.
- `reason`: 1 to 3 plain English sentences explaining why the correct answer is correct (show the pattern or working, e.g. "Differences are +2, +3, +4, so next is +5: 19 + 5 = 24.").
- `related_fact`: ONE short sentence that adds useful knowledge: for puzzles a tip about this question type or the underlying rule (e.g. "Tip: in alternating series, split the terms into two separate sequences."); for academic questions a relevant extra fact (dates, names, places).
- Do NOT use the characters `<`, `>` or `&` anywhere (use "and", "less than", "greater than"). Use plain ASCII quotes inside Python strings correctly (use double quotes for strings that contain an apostrophe).

## Answers
- Solve every question yourself, carefully, step by step. Where an answer key sheet is named in your assignment, read it and compare. Key layout for the handwritten grids: the answers run down a column, so for a 3-column key row r column c is question (c-1)*10 + r (column 1 = Q1-10, column 2 = Q11-20, column 3 = Q21-30; a 9-column key covers Q1-90). Letters refer to the option letters printed on the paper (numbers 1-5 refer to numbered options). Some key entries are written as the actual value (a number or word) instead of a letter.
- If your own careful answer and the key disagree, re-check both. The handwriting can be misread and the key can be wrong. Use the answer that is actually correct; mention the disagreement in your final report (test, question, what you chose, what the key says).
- If a question is illegible, truncated or truly ambiguous (no defensible single answer), SKIP it and list it in your final report instead of guessing.
- Use real, current, correct facts. If a source line is outdated or wrong, use the correct fact and say so in the related_fact (for example "Some notes say X, the accepted figure is Y").
- Keep the original question numbering in the label so the user can match it to the paper.

## Checking
Run `python3 /home/user/Asad/pma159/check_fa.py <your file>` and fix every reported problem before finishing. It checks the tuple shape, option counts, the correct index, and forbidden characters.

## Final report (keep it short)
Return: the file path, the number of questions written, the list of skipped questions with the reason, and the list of key disagreements. Do not paste the questions back.

## Where the source files are
- Big PDF (38 pages, read with the Read tool and the `pages` parameter, max 20 pages per call): `/root/.claude/uploads/01989231-deb6-55a8-8bef-d084da768c53/44ebd253-Verbal_answers_Questions.pdf`
  - Pages 1 to 19 are handwritten answer-key sheets: p1 = Test 1 key (Q1-90, 9 columns), p2 = Test 9 key, p3 = Test 7 key, p4 = Test 6 key, p5 = Test 10 key, p6 = Test 3 key, p7 = Test 8 key, p8 = Test 4 key, p9 = Test 5 key, p10 = Test 14 key, p11 = Test 2 key (grid headed V.2 with columns 10..70, answers are option numbers), p12 = Test 11 key, p13 = Test 15 key (photo is upside down), p14 = Test 16 key, p15 = Test 12 key, p16 = Test 13 key, p17 = Test 17 key (four columns, Q1-40), p18 = Test 20 key (answers written as words), p19 = Test 15 key (clean copy).
  - Pages 20 to 38 are the question papers: p20 = Test 1 (Q1-37, with handwritten answers in blue), p21 = Test 2, p22 = Test 3, p23 = Test 4, p24 = Test 5, p25 = Test 6, p26 = Test 7, p27 = Test 8, p28 = Test 9, p29 = Test 10, p30 = Test 11, p31 = Test 12, p32 = Test 13, p33 = Test 14, p34 = Test 15, p35 = Test 16, p36 and p37 = Test 17 (Q1-16 then Q17-40), p38 = Test 20.
- Extra photos (read directly with the Read tool): folder `/root/.claude/uploads/01989231-deb6-55a8-8bef-d084da768c53/`
  - `1af2cd54-image.jpg` = Test 1 Q1-41 (photo), `8eb85226-image.jpg` = Test 1 continued, Q42-80 (photo).
  - `b92b2019-image.jpg` = Test 11, `af3bb31b-image.jpg` and `9f3dca53-image.jpg` = Test 13, `d3199318-image.jpg` = Test 8, `96a3536c-image.jpg` = Test 16, `198e8bc6-image.jpg` = Test 12 (these duplicate PDF papers; use them only if the PDF page is hard to read).
  - `ed211744-image.jpg`, `704005cd-image.jpg`, `232b1d7d-image.jpg` = screenshots of one-line academic facts (numbered lines 1-23, 81-113, and 51-81 respectively).
  - `f50312de-image.jpg`, `af829de0-image.jpg`, `00981f67-image.jpg` = Exam World charts: pre-partition history, post-partition history, and 1988-2007 political events.
- Academic list PDF (2 pages, questions with the answer written in brackets): `/root/.claude/uploads/01989231-deb6-55a8-8bef-d084da768c53/ee49cebd-CamScanner_07-30-2025_12.37.pdf`
