# Duplicate check for the Hakeem Force Academy quiz

Each record in your input file has a header line `i|j` and two questions A and B (with their marked answers).
Decide for EVERY record whether A and B are the SAME question, i.e. a student who knows the answer to one automatically knows the other: same fact asked, same correct answer, only the wording differs (e.g. "Why do we boil milk?" vs "Why is milk boiled?"; "antonym of wild" vs "opposite of wild").
They are DIFFERENT if they ask a different fact or a different calculation, even with the same numbers or same answer (e.g. "percentage present" vs "how many absent"; "1200 present" vs "1200 female" is DIFFERENT wording of a different situation -> DIFF; "capital of X" vs "X is the capital of which country" -> DIFF; "who founded" vs "when founded" -> DIFF; different numbers -> DIFF).
If they are the same question but the marked answers disagree, still write SAME and add a note with the correct answer.

Write the output file (path in your assignment), one line per record, exactly:
i|j SAME
or
i|j DIFF
(optionally followed by ` | note`). Do not skip any record. Reply only with the output path and the number of SAME lines.
