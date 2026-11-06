"""Apply recheck results to pma159/corrections.json (patched by test key + question id; copies in VB-/NV- follow the source)."""
import json, glob, os
H = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(H, '..', 'pma159', 'corrections.json')
key = {x['id']: x for x in json.load(open(os.path.join(H, 'key.json')))}
where = json.load(open(os.path.join(H, 'where.json')))
dump = json.load(open('/tmp/all_dump.json'))
corr = json.load(open(C))
SKIP = {'M2922', 'M6469', 'M12879'}          # reviewed: keep the app answer
MANUAL = {
 'M446': {'question': "Who was the last Chief Minister of Khyber Pakhtunkhwa before governor's rule began on 11 October 2026?",
          'options': ["Sohail Afridi", "Ali Amin Gandapur", "Mahmood Khan", "Pervez Khattak"], 'correct': 0,
          'facts': "Sohail Afridi (PTI) was Chief Minister of KP from 15 October 2025. On 11 October 2026 the federal government imposed governor's rule in KP, and Governor Faisal Karim Kundi took charge."},
 'M132': {'options': ["π/3 ≈ 1.047 rad", "π/4 ≈ 0.785 rad", "π/2 ≈ 1.571 rad", "π/6 ≈ 0.524 rad"], 'correct': 3,
          'facts': "30° × π/180 = π/6 radians ≈ 0.524 rad."},
}
res = {}
for f in sorted(glob.glob(os.path.join(H, 's2out', 't*.json'))):
    for r in json.load(open(f)): res[r['id']] = r   # later rounds (t21+) override
n = 0; log = []
for mid, r in res.items():
    if mid in SKIP: continue
    k = key[mid]
    if mid in MANUAL: patch = dict(MANUAL[mid])
    elif r['verdict'] == 'change' and isinstance(r.get('ans'), int) and 0 <= r['ans'] < len(k['o']) and r['ans'] != k['c']:
        patch = {'correct': r['ans'], 'facts': r['note']}
    elif r['verdict'] == 'none' and r.get('fix'):
        o = list(k['o']); o[k['c']] = r['fix']; patch = {'options': o, 'correct': k['c'], 'facts': r['note']}
    else: continue
    for tk, i in where[mid]:
        if tk.startswith(('VB-', 'NV-')): continue
        q = dump[tk][i]; qid = str(q['id'])
        p = dict(patch)
        if 'question' in p and tk[0].isdigit(): p['question'] = q['question'].split(')')[0] + ') ' + p['question'] if q['question'].startswith('(') else p['question']
        corr.setdefault(tk, {}).setdefault(qid, {}).update(p); n += 1
    log.append('%s | %s | %s -> %s' % (mid, k['q'], k['o'][k['c']], (patch.get('options') or k['o'])[patch['correct']]))
json.dump(corr, open(C, 'w'), ensure_ascii=False, indent=0)
open(os.path.join(H, 'CHANGES.md'), 'w').write('# Answers changed by the full recheck\n\n' + '\n'.join('- ' + l for l in log) + '\n')
print(n, 'patches,', len(log), 'MCQs changed')
