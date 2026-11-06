import json, random, sys
sys.path.insert(0, '.')
from questions import Q

parts_size = 50
data = []
for i, (sec, q, ok, wrong, why, rep) in enumerate(Q):
    opts = [ok] + list(wrong)
    random.Random(i * 7919 + 13).shuffle(opts)
    data.append({"s": sec, "q": q, "o": opts, "a": opts.index(ok), "e": why, "r": rep})
parts = [data[i:i + parts_size] for i in range(0, len(data), parts_size)]
print(len(data), "questions,", len(parts), "parts", [len(p) for p in parts])
tpl = open('template.html', encoding='utf8').read()
open('pma159_mcq_test.html', 'w', encoding='utf8').write(tpl.replace('/*DATA*/', json.dumps(parts, ensure_ascii=False)))
