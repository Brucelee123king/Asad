# Blind answer check (stage 1) for the PMA preparation app
Input: /home/user/Asad/recheck/in/s<NN>.json = list of {"id","q","o":[options]} (the app's answer is NOT shown on purpose).
Today is 1 November 2026. For EVERY item choose the correct option yourself (Pakistan affairs, Islamiat, GK, current affairs, English grammar/vocabulary, maths, reasoning; solve maths/reasoning properly).
Output /home/user/Asad/recheck/out/s<NN>.json = JSON list, same order, each {"id","a": index 0-based of your answer (or -1 if no option is correct), "conf": "high"|"med"|"low", "ch": true if the answer can change with time (office holders, records, latest events, counts like districts) else false}.
Work in batches of ~60 items: append each batch to the output file with python so nothing is lost. Do not use web search in this stage. Do not edit other files. Final reply SHORT: count done, how many low-confidence.
