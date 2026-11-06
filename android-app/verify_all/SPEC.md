# Blind answer check of exam MCQs (full audit)

You get a text file of numbered multiple-choice questions. The answers are NOT shown. Solve EVERY question independently and carefully. The questions come from a Pakistani exam-preparation app (PMA / ISSB / Forces Academy initial test: Pakistan Studies, Islamiat, general knowledge, current affairs, English, maths, verbal and non-verbal intelligence puzzles, science, Constitution of Pakistan).

Rules
- Maths, series, percentages, ages, speeds, days of the month, directions, letter puzzles: work them out step by step (days of month: shift by the remainder after dividing the gap by 7).
- Facts: answer from reliable knowledge. For anything that can change or that you are not 100% sure of (office holders, records, rankings, recent events, dates, numbers, article numbers, counts) use WebSearch (a deferred tool: first call ToolSearch with query `select:WebSearch`). "Current" means TODAY, October 2026. You have a large budget: search whenever there is real doubt, do not guess.
- Flawed question: if no option is correct, two options are correct, the question is ambiguous, or the answer is disputed among reliable sources, answer X and say why in the note.
- Do not skip any number. Work through the whole file.

Output: write the file given in your assignment, one line per question, exactly:
<number>: <letter A-E or X> | <high|medium|low> | <short note, only when useful (always when X or low)>
Example:
1712: B | high |
1713: X | medium | two options correct: both Lahore and Karachi fit
Reply only with the output path and the number of lines written.
