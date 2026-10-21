# Task: read page images of a scanned "Famous Thousand+ Academic MCQs" list (Pro Genius Students) and turn every question into a 4-option MCQ
The pages are JPG images (Read tool shows images). Each page lists numbered questions (numbering continues across pages, e.g. "9. quit India movement date?") with a short answer line under each. Some questions/answers are messy, abbreviated, misspelt, or hand-written-style. Ignore the header/footer ad text.
TODAY IS OCT 2026. Answers must be correct for Oct 2026. For current-affairs / office-holders / statistics / anything uncertain use WebSearch (real searches) and flag disagreements with the source answer.
For EVERY numbered question on your pages (do not skip any, do not merge) write one object:
{"num": <question number as printed>, "page": <page number>, "question": "clean question text (fix spelling, keep meaning)", "options": [4 strings], "correct": 0-3, "why": "1-2 short sentences why the answer is right", "rel": "1-2 short related exam facts", "problem": "(only if needed)"}
Rules:
- The source's short answer is the starting point; if it is wrong/outdated/unclear, give the right answer for Oct 2026 and describe in "problem".
- Correct option = SHORT clean answer (name, number, year, place). Add 3 plausible WRONG options of the same type (real, believable distractors; definitely wrong). No "All of the above". Put the correct option at a RANDOM position (spread 0..3).
- Vocabulary questions (e.g. "alter mean") -> make a meaning MCQ (options = 4 meanings/synonyms). Maths/English/current-affairs all fine.
- Questions with no single clean answer (opinion, 'list all', depends on definition): choose the standard exam answer and set "problem". If a question is unreadable, set "problem":"unreadable" and make your best reconstruction or skip only if truly impossible (then include {"num","page","skip":"reason"}).
- why/rel simple English, factual; for date-sensitive answers write "As of Oct 2026".
Output: JSON list ordered by num, in the file named in your prompt. Validate with python (each non-skip item has 4 distinct options and correct in 0..3). Do not edit other files. Final reply: 3 lines: count written, count with problem, count skipped.
