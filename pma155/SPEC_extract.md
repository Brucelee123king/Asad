# Extract questions from PMA 155 "important MCQs with answers"

The input chunk is text of a PDF: lists of numbered short questions with the answer written next to them (formats like `12) : Question? (Answer)` or `12. Question?` followed by `A. Answer`). The numbering restarts several times (different lists). Lines can wrap over two lines. Some answers are outdated (for example office holders), wrong, or marked "confirm it". Urdu script was already removed. Roman Urdu and spelling mistakes are common.

## Your job
Read EVERY item in your chunk and write one JSON object per line (JSON Lines) to the output file in your assignment:

{"exp": <chunk number * 1000 + running item count (1, 2, 3 ...) of YOUR chunk, a new value for every item>, "q": "<question rewritten as one clear English question>", "a": "<the answer as given, or empty string>", "ok": <true if plain answer, false if 'confirm it', doubtful or visibly garbled>, "kind": "<verbal|academic>"}

## Rules
- Rewrite each question into clear, complete English with correct spelling, in the same words for the same question every time (duplicates are matched later). Examples: "Capial of Argentina?" -> "What is the capital of Argentina?"; "90% of 90? (81)" -> "What is 90% of 90?"; "Pak Joined UNO? (30 September 1947)" -> "On what date did Pakistan join the United Nations?". Keep all numbers and names exactly. Keep full data of puzzles.
- A line that is only a fact/title with a hint (e.g. "Israel Was Title Of? (Hazrat Yaqoob AS)") becomes "Israel was the title of which prophet?" with the answer in "a".
- Skip lines that are not questions (headers, contact numbers, "Regards", "Prepared by"). Do not skip any real question. If an item is garbled beyond understanding, skip it.
- Do not invent answers. Mark "kind" "verbal" for maths, percentages, days, letters, series, directions, coding; otherwise "academic".

## Output and reply
Write ONLY valid JSON Lines. Check with: python3 -c "import json,sys;[json.loads(l) for l in open(sys.argv[1])]" <file>. Reply with only the number of questions written. Do not read any file other than your chunk and this spec.
