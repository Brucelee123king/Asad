# Task: turn Q+answer+facts items into 4-option MCQs (Pakistan PMA / Forces Academy exam app)
Input file (JSON list): items with src, num, question, answer (a sentence), facts (source's related facts).
TODAY IS OCT 2026. Answers must be correct for Oct 2026. Source PDFs claim to be verified, but verify current-affairs / date-sensitive / number items with WebSearch (do real searches for office holders, recent events, statistics) and flag disagreements.
For EVERY input item write one output object:
{"src","num","question","options":[4 strings],"correct":0-3,"why":"1-2 short sentences explaining why the answer is right","rel":"1-2 short related exam facts","problem":"(only if needed)"}
Rules:
- question: keep the source wording (fix obvious typos only). Do not merge or drop items. If two items in YOUR slice are the same question, still output both.
- options: correct option = SHORT clean answer text (a name, number, year, place... not a sentence, no "as of ..." qualifiers). Add 3 plausible WRONG options of the same type (real, believable distractors: same kind of thing, similar magnitude; for numbers use nearby sensible values; for names use real people/places often confused with it). Wrong options must be definitely wrong. No "All of the above"/"None". Put the correct option at a RANDOM position (spread 0..3 roughly evenly).
- If the question has no single clean answer (ambiguous, opinion, 'list', or a count that depends on classification), pick the most standard answer, make wrong options clearly different, and set "problem" explaining. If the source's answer is outdated/wrong for Oct 2026, use the right one and set "problem" saying so.
- why/rel: simple English, factual, built from the source's answer/facts plus what you verified; for date-sensitive answers write "As of Oct 2026".
- Output file as named in your prompt, a JSON list with exactly one object per input item (same order). Validate the JSON with python before replying. Do not edit other files. Final reply: 3 lines (count, count with problems, anything uncertain).
