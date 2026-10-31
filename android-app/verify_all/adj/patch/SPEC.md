# Turn adjudication verdicts into exact patches
Each input line is a JSON record of an MCQ (q, opts, marked answer letter, reason "facts", related fact "rel") plus an adjudicator verdict (CHANGE <letter> or REWRITE) and note.
For every record write one JSON object per line to the output file:
{"n":<n>,"q":<question text, unchanged unless the note says it is wrong>,"opts":[full final options list, same number of options as input>= 4],"ok":<0-based index of the correct option>,"facts":<reason, corrected so it matches the answer; keep original style, one or two sentences>,"rel":<related fact, keep or fix>}
Rules:
- Keep the question's repeat suffix exactly as is, e.g. " (127)" or " (Repeated in N tests)" - copy it unchanged at the end of q.
- Change as little as needed. Keep unchanged options exactly. For junk/duplicate options, replace with plausible real distractors of the same kind. The right answer must be indisputable for Pakistan exams, October 2026.
- If you cannot make a clean indisputable fix, write {"n":<n>,"skip":"reason"} instead.
- Facts and rel must be accurate and correct for Oct 2026. WebSearch is allowed if needed (deferred tool, load with ToolSearch select:WebSearch) but may be refused; then use sure knowledge only.
Reply only with the output path and line count.
