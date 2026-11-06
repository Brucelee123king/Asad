"""Verbal tests: copies of the verbal MCQs from EVERY category (the originals stay where they are), sorted by type,
one test per type (VB-<n>, n = position in vb_types.TYPES, a test may have more than 50 MCQs).
Sources: verbal sections (PMA 'Verbal: ...', Forces Academy 'Intelligence Test', 100 Most Repeated, 105 Verbal by PGS, the
items marked verbal in ../verbal/out) are all taken; every other category (Hakeem, 1000 MCQs, Pro Genius, PMA 158, Light Forces...)
gives only questions that clearly match a verbal type (strict rules in vb_types.py). English, Islamiat, Constitution are skipped.
The same question (same wording ignoring order/brackets, same answer) is written once; its repeat counts are added in brackets.
Non Verbal: the Pro Genius Paid Non Verbal Booklet picture questions (PB-) are copied into extra NV- tests."""
import json, os, re, glob, hashlib
import vb_types
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
NV_TYPES = [('odd', 'Odd One Out'), ('analogy', 'Analogy'), ('series', 'Complete the Series'), ('matrix', 'Missing Figure and Matrix'), ('mirror', 'Mirror Images')]
def nv_type(q):
    k = q.get('kind') or ''
    if k in ('odd', 'analogy', 'series', 'matrix', 'mirror'): return k
    s = str(q.get('question', '')).lower()
    if 'mirror' in s: return 'mirror'
    if 'different' in s or 'odd' in s: return 'odd'
    if 'is to' in s or 'changes in some way' in s: return 'analogy'
    if 'series' in s or 'sequence' in s or 'comes next' in s: return 'series'
    return 'matrix'
SKIP = {'NV', 'PB', 'VB', 'EN', 'IS', 'CN'}
def make(ALL, base_dir):
    refs = set()
    for f in glob.glob(os.path.join(base_dir, '..', 'verbal', 'out', '*.json')): refs |= set(json.load(open(f))['verbal'])
    groups = {}; npick = 0
    for k, v in ALL.items():
        p = k.split('-')[0]
        if p in SKIP: continue
        for q in v:
            if not q.get('question') or not q.get('options') or q.get('nv'): continue
            sec = q.get('sec', '') or ''
            isv = (p == 'PMA' and sec.startswith('Verbal')) or (p == 'FA' and 'Intelligence Test' in sec) or p in ('IV', 'PV') or ('%s#%d' % (k, q['id'])) in refs
            core, w = strip(q['question'])
            t = vb_types.classify(dict(q, question=core), strict=not isv)
            if not t: continue
            npick += 1
            key = norm(core) + '|' + ans(q)
            g = groups.setdefault(key, {'w': 0, 'best': None, 'score': -1, 'core': core, 't': t, 'v': isv})
            g['w'] += w
            if isv and not g['v']: g['t'] = t; g['v'] = True
            sc = len(str(q.get('facts', ''))) + len(str(q.get('rel', '')))
            if sc > g['score']: g.update(best=q, score=sc, core=core)
    by = {}
    for g in groups.values():
        q = dict(g['best']); q['question'] = g['core'] + (' (%d)' % g['w'] if g['w'] > 1 else '')
        q['sec'] = 'Verbal: ' + vb_types.NAMES[g['t']]; q['pma'] = True; q.pop('rep', None); q.pop('nv', None)
        by.setdefault(g['t'], []).append(q)
    tests = {}
    for i, (tid, name) in enumerate(vb_types.TYPES):
        lst = sorted(by.get(tid, []), key=lambda q: hashlib.md5(q['question'].encode('utf8')).hexdigest())
        if lst: tests['VB-%d' % (i + 1)] = [dict(e, id=j + 1) for j, e in enumerate(lst)]
    # Non Verbal: all picture questions (Non Verbal + copies of the Paid Non Verbal Booklet), one test per type (NV-n, n = position in NV_TYPES)
    pics = []
    for k in sorted([k for k in ALL if k.startswith('NV-')], key=lambda x: int(x.split('-')[1])): pics += ALL[k]
    for k in sorted([k for k in ALL if k.startswith('PB-')], key=lambda x: int(x.split('-')[1])): pics += ALL[k]
    nvb = {}
    for q in pics:
        t = nv_type(q); nvb.setdefault(t, []).append(q)
    for i, (tid, name) in enumerate(NV_TYPES):
        lst = nvb.get(tid, [])
        if lst: tests['NV-%d' % (i + 1)] = [dict(e, id=j + 1, sec='Non Verbal: ' + name) for j, e in enumerate(lst)]
    return tests, npick, sum(len(v) for k, v in tests.items() if k.startswith('VB-'))
