"""Academic section: copies of every academic MCQ of the app sorted by subject, tests of 50: AC-<subject no>-<part>.
Same question (same wording + same answer) is written once; its repeat counts are added. Labels: ac_labels.json (reviewed),
new MCQs fall back to ac_rules.cls. Verbal-looking items go to the Verbal section instead (vb_build)."""
import json, os, re, hashlib, glob
import vb_build, vb_types, ac_rules
SUBJ = [('eng', 'English'), ('math', 'Maths'), ('pak', 'Pakistan Studies'), ('gk', 'General Knowledge'), ('isl', 'Islamiat'), ('cur', 'Current Affairs'), ('sci', 'Everyday Science')]
SKIP = {'NV', 'PB', 'VB', 'IV', 'PV', 'AC'}
def make(ALL, base_dir):
    lab = json.load(open(os.path.join(base_dir, 'ac_labels.json')))
    refs = set()
    for f in glob.glob(os.path.join(base_dir, '..', 'verbal', 'out', '*.json')): refs |= set(json.load(open(f))['verbal'])
    pool = {}
    for k, v in ALL.items():
        p = k.split('-')[0]
        if p in SKIP or k.startswith('NV') or k.startswith('VB'): continue
        for q in v:
            if not q.get('question') or not q.get('options') or q.get('nv'): continue
            sec = q.get('sec', '') or ''
            if (p == 'PMA' and sec.startswith('Verbal')) or (p == 'FA' and 'Intelligence Test' in sec) or ('%s#%d' % (k, q['id'])) in refs: continue
            core, w = vb_build.strip(q['question'])
            if vb_types.classify(dict(q, question=core), strict=True): continue
            key = vb_build.norm(core) + '|' + vb_build.ans(q)
            h = hashlib.md5(key.encode('utf8')).hexdigest()[:12]
            rp = max(w, int(q.get('rep') or 1))
            g = pool.get(h)
            if not g:
                a = str(q['options'][q['correct']]) if 0 <= q.get('correct', -1) < len(q['options']) else ''
                g = pool[h] = {'w': 0, 'best': q, 'core': core, 'score': -1, 't': lab.get(h) or ac_rules.cls({'q': core, 'a': a, 'sec': sec})}
            g['w'] += rp
            sc = len(str(q.get('facts', ''))) + len(str(q.get('rel', '')))
            if sc > g['score']: g.update(best=q, score=sc, core=core)
    by = {}
    for h, g in pool.items():
        if g['t'] not in dict(SUBJ): continue
        q = dict(g['best']); q['question'] = g['core'] + (' (%d)' % g['w'] if g['w'] > 1 else '')
        q['sec'] = 'Academic: ' + dict(SUBJ)[g['t']]; q['pma'] = True; q.pop('rep', None); q['w'] = g['w']
        by.setdefault(g['t'], []).append(q)
    tests = {}
    for i, (sid, name) in enumerate(SUBJ):
        lst = sorted(by.get(sid, []), key=lambda q: (-q['w'], hashlib.md5(q['question'].encode('utf8')).hexdigest()))
        for n in range((len(lst) + 49) // 50):
            tests['AC-%d-%d' % (i + 1, n + 1)] = [dict({kk: vv for kk, vv in e.items() if kk != 'w'}, id=j + 1) for j, e in enumerate(lst[n * 50:(n + 1) * 50])]
    return tests
