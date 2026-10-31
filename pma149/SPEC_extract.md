# Extract questions from PMA 149 test experiences

The input chunk is text from a PDF of test experiences written by candidates who sat the PMA initial test (Pakistan Military Academy, ASRC centres). Each experience starts with "Experience No <n>" and is separated by lines of "=====". Candidates write in English, Roman Urdu and mixed language. They list the questions they remember from three parts: Verbal intelligence (percentages, days, series, analogies, odd-one-out, directions, coding), Non-verbal (usually only described in general) and Academic (Pakistan Studies, Islamiat, general knowledge, current affairs, maths and English).

## Your job
Read EVERY experience in your chunk and extract EVERY distinct question or question-like item that a candidate remembers, with the answer if the candidate gave one. Write one JSON object per line (JSON Lines) to the output file named in your assignment:

{"exp": <experience number as integer>, "q": "<the question rewritten as one clear English question>", "a": "<the answer exactly as the candidate gave it, or empty string>", "ok": <true if the candidate sounds sure or gives a plain answer, false if they say 'confirm it', 'not sure', 'check it', or a doubtful answer>, "kind": "<verbal|academic>"}

## Rules
- Rewrite each question into clear, complete English, in the same words for the same question every time (this is how duplicates are found later). Examples: "why we boil milk" -> "Why do we boil milk?"; "90% of 90" -> "What is 90% of 90?"; "capital of Ghana" -> "What is the capital of Ghana?"; "pak jb UNO ka member bana" -> "In which year did Pakistan become a member of the United Nations?". Keep all numbers and names exactly. For series and puzzles keep the full data: "Which number comes next: 2, 4, 8, 16, ?".
- Skip greetings, thanks, advice, contact details, passed/failed status, names of candidates, medical test details, interview details, and any line that is not a question or fact the paper asked about.
- A fact written without a question (for example "Gold symbol Au" or "Quaid joined Muslim League 1913") counts as a question: rewrite it as the question it answers and put the stated fact in "a".
- If the candidate gives several questions on one line, make one object per question. If a candidate says a question type appeared (for example "5 to 6 questions on days") without giving any example, skip it. If they give an example, extract the example.
- Do not invent answers. If no answer is given, use "".
- Do not skip an experience: even if you find nothing, move on, but do read each one.
- Mark "kind" as "verbal" for intelligence-test items (maths, percentages, series, analogies, odd one out, relationships, directions, days and dates, coding) and "academic" for everything else (including English grammar and vocabulary).

## Output and reply
Write ONLY valid JSON Lines (one object per line, no commentary, no code fences) to your output file. Check at the end with: python3 -c "import json,sys;[json.loads(l) for l in open(sys.argv[1])]" <file> . Reply with only the number of questions written and the number of experiences read. Do not read any file other than your chunk and this spec.
