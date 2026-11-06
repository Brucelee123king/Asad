"""Academic pool: every non-verbal-intelligence MCQ in the app, de-duplicated (same question + same answer = one item).
usage: python3 ac_pool.py all_dump.json out_pool.json   -> [{"h": hash, "q": question, "o": options, "a": answer text, "src": [key#id,...], "w": repeat}]"""
import json, sys, os, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vb_build, vb_types
ALL = json.load(open(sys.argv[1], encoding='utf8'))
refs = set()
import glob
for f in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'verbal', 'out', '*.json')): refs |= set(json.load(open(f))['verbal'])
SKIP = {'NV', 'PB', 'VB', 'IV', 'PV'}
pool = {}
for k, v in ALL.items():
    p = k.split('-')[0]
    if p in SKIP: continue
    for q in v:
        if not q.get('question') or not q.get('options') or q.get('nv'): continue
        sec = q.get('sec', '') or ''
        if (p == 'PMA' and sec.startswith('Verbal')) or (p == 'FA' and 'Intelligence Test' in sec) or ('%s#%d' % (k, q['id'])) in refs: continue
        core, w = vb_build.strip(q['question'])
        if vb_types.classify(dict(q, question=core), strict=True): continue   # goes to the Verbal section
        key = vb_build.norm(core) + '|' + vb_build.ans(q)
        h = hashlib.md5(key.encode('utf8')).hexdigest()[:12]
        g = pool.get(h)
        if not g:
            g = pool[h] = {'h': h, 'q': core, 'o': q['options'], 'a': str(q['options'][q['correct']]) if 0 <= q.get('correct', -1) < len(q['options']) else '', 'src': [], 'w': 0, 'sec': sec}
        g['src'].append('%s#%d' % (k, q['id'])); g['w'] += max(w, int(q.get('rep') or 1) if p not in ('O',) else 1)
json.dump(list(pool.values()), open(sys.argv[2], 'w', encoding='utf8'), ensure_ascii=False)
print(len(pool), 'unique academic MCQs')
