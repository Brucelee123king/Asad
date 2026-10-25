"""Verbal tests (VB-1, VB-2 ...): copies of all verbal MCQs from every category except Hakeem.
Sources: PMA 159 sections 'Verbal: ...', Forces Academy 'Intelligence Test ...', 100 Most Repeated (IV), and the questions found verbal
in 1000 MCQs, Pro Genius and PMA 158 (../verbal/out/*.json, refs 'TESTKEY#id'). The originals stay where they are.
The same question (same wording ignoring order/brackets, same answer) is written once; its repeat counts are added and shown in brackets."""
import json, os, re, glob, hashlib
STOP = set('what which who whom is are was were the of a an in on at to for by as do does did name called known following from with and or be been has have had s'.split())
def strip(q):
    s = re.sub(r'^\s*\((?:Original MCQ #\d+|[^)]*·[^)]*)\)\s*', '', str(q), flags=re.I)
    w = 1; m = re.search(r'\s*\((?:Repeated in\s+)?(\d+)(?:\s+(?:tests?|times))?\)\s*$', s, re.I)
    if m: w = max(1, int(m.group(1))); s = s[:m.start()]
    return s.strip(), w
def norm(s):
    t = [x for x in re.sub(r'[^a-z0-9]+', ' ', s.lower().replace('%', ' percent ')).split() if x not in STOP]
    return ' '.join(sorted(x for x in t if not re.search(r'\d', x))) + '#' + ' '.join(x for x in t if re.search(r'\d', x))
def ans(q):
    try: return re.sub(r'[^a-z0-9]+', ' ', str(q['options'][q['correct']]).lower()).strip()
    except Exception: return ''
def make(ALL, base_dir):
    pick = []
    for k, v in ALL.items():
        p = k.split('-')[0]
        for q in v:
            sec = q.get('sec', '') or ''
            if (p == 'PMA' and sec.startswith('Verbal')) or (p == 'FA' and 'Intelligence Test' in sec) or p == 'IV': pick.append(q)
    refs = set()
    for f in glob.glob(os.path.join(base_dir, '..', 'verbal', 'out', '*.json')): refs |= set(json.load(open(f))['verbal'])
    for k, v in ALL.items():
        for q in v:
            if '%s#%d' % (k, q['id']) in refs: pick.append(q)
    groups = {}
    for q in pick:
        if not q.get('question') or not q.get('options'): continue
        core, w = strip(q['question'])
        key = norm(core) + '|' + ans(q)
        g = groups.setdefault(key, {'w': 0, 'best': None, 'score': -1, 'core': core})
        g['w'] += w
        sc = len(str(q.get('facts', ''))) + len(str(q.get('rel', '')))
        if sc > g['score']: g.update(best=q, score=sc, core=core)
    out = []
    for key, g in groups.items():
        q = dict(g['best']); q['question'] = g['core'] + (' (%d)' % g['w'] if g['w'] > 1 else '')
        q['sec'] = 'Verbal'; q['pma'] = True; q.pop('rep', None); q.pop('nv', None)
        out.append(q)
    out.sort(key=lambda q: hashlib.md5(q['question'].encode('utf8')).hexdigest())   # mixed, but the same order every build
    tests = {}
    for n in range((len(out) + 49) // 50):
        tests['VB-%d' % (n + 1)] = [dict(e, id=i + 1) for i, e in enumerate(out[n * 50:(n + 1) * 50])]
    return tests, len(pick), len(out)
