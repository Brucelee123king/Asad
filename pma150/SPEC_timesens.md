# Current-affairs web check (today is October 2026)

Each line of your input is a multiple-choice question from a quiz for Pakistani test candidates, with options and `[current answer: X]`.
Your job: make sure the marked answer is TRUE TODAY (October 2026) and that the question has exactly one correct option.

1. First load WebSearch: call ToolSearch with query `select:WebSearch`.
2. For EVERY line whose answer can change over time (office holders, chairmen, champions, records, rankings, populations, latest events), run a WebSearch (standard mode) and confirm the answer with recent, reliable sources (news from 2026, official sites, Wikipedia). Stable historical facts that only mention a title (e.g. "first Governor General") need no search.
3. Write the output file (path in your assignment), one line per input line:
<number>: OK
or
<number>: FIX <letter of the correct option> | <short reason with source and date>
or
<number>: NEWOPT <correct answer text> | <short reason with source and date>   (when no option is correct today)
or
<number>: DROP | <reason>   (when you cannot confirm any answer)
Reply only with the output path and the counts of OK / FIX / NEWOPT / DROP.
