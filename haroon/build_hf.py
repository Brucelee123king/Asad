# Haroon Force Academy: out/c1..c7.json (checked MCQs) -> hf_final.json [[sec, q, options, correct, why, rel, rep], ...]
# The same question (same words ignoring order/punctuation/small words, same answer) is written once with a count.
import json, glob, os, re, random
H = os.path.dirname(os.path.abspath(__file__))
STOP = set('what which who whom is are was were the of a an in on at to for by as do does did name called known following from with and or be been has have had s its this that how many much'.split())
def norm(s):
    t = [x for x in re.sub(r'[^a-z0-9]+', ' ', s.lower()).split() if x not in STOP]
    return ' '.join(sorted(t))
def ans(o): return re.sub(r'[^a-z0-9]+', ' ', str(o).lower()).strip()
SEC = {'T1': 'Haroon Forces Academy MCQs', 'A': 'Sir Haroon MCQs for PMA 158', 'B': 'Important MCQs for PMA 158', 'C': 'Current Affairs 2026'}
items = []
for i in range(1, 8):
    f = os.path.join(H, 'out', 'c%d.json' % i)
    if not os.path.exists(f): print('missing', f); continue
    items += json.load(open(f))
groups = {}; order = []
for e in items:
    o = e['options']; c = int(e['correct'])
    if len(o) != 4 or not 0 <= c < 4: print('bad', e.get('id')); continue
    key = norm(e['question']) + '|' + ans(o[c])
    if key not in groups: groups[key] = {'e': e, 'n': 0}; order.append(key)
    groups[key]['n'] += 1
out = []
for k in order:
    e = groups[k]['e']; part = e['id'].split('-')[1]; sec = SEC['T1'] if e['id'].startswith('T1') else SEC.get(part, 'Haroon Forces Academy MCQs')
    out.append([sec, e['question'].strip(), e['options'], int(e['correct']), e.get('why', ''), e.get('rel', ''), groups[k]['n']])
json.dump(out, open(os.path.join(H, 'hf_final.json'), 'w'), ensure_ascii=False)
print(len(items), 'MCQs ->', len(out), 'distinct;', sum(1 for x in out if x[6] > 1), 'repeated')
