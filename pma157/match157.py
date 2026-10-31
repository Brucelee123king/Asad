# match PMA150 clusters to existing Hakeem MCQs (hk_final.json)
import json,re,collections,sys
sys.path.insert(0,'.')
STOP=set("the a an of is was in on for to what which who whom does do did are were name any has have had be as at by from and or it its this that with how many much when where why whose will would can could should there their they them we you your i he she his her our us me my".split())
def toks(s):
    s=s.lower().replace('%',' percent ')
    s=re.sub(r"[^a-z0-9 ]+",' ',s); out=[]
    for w in s.split():
        if w in STOP: continue
        if len(w)>3 and w.endswith('ies'): w=w[:-3]+'y'
        elif len(w)>3 and w.endswith('s') and not w.endswith('ss'): w=w[:-1]
        out.append(w)
    return out
def key(q):
    t=toks(re.sub(r'\s*\(\d+\)\s*$','',q))
    return tuple(sorted(w for w in t if re.search(r'\d',w))), frozenset(w for w in t if not re.search(r'\d',w))
hk=json.load(open('../pma156/hk_final7.json'))
hkk=[key(x[1]) for x in hk]
inv=collections.defaultdict(list)
for i,(n,s) in enumerate(hkk):
    for w in s: inv[w].append(i)
cl=json.load(open('clusters.json'))
TH=float(sys.argv[1]) if len(sys.argv)>1 else 0.6
matched=collections.defaultdict(set); unmatched=[]
for c in cl:
    best=(0,None)
    for v in c['variants']:
        n,s=key(v)
        if not s: continue
        cand=collections.Counter(i for w in s for i in inv[w])
        for i,_ in cand.items():
            if hkk[i][0]!=n: continue
            j=len(s&hkk[i][1])/len(s|hkk[i][1])
            if j>best[0]: best=(j,i)
    if best[0]>=TH and (best[0]==1.0 or min(len(key(c['q'])[1]),len(hkk[best[1]][1]))>=2):
        matched[best[1]].update(c['all_exps']); c['hk']=best[1]
    else: unmatched.append(c)
json.dump({str(k):sorted(v) for k,v in matched.items()},open('hk_add.json','w'))
json.dump([c['q'] for c in cl if 'hk' in c],open('matched_q.json','w'),ensure_ascii=False)
# NOTE: unmatched.json is frozen (writer ids refer to it); do not rewrite it
if not __import__('os').path.exists('unmatched.json'): json.dump(unmatched,open('unmatched.json','w'),ensure_ascii=False,indent=0)
print('clusters',len(cl),'matched to existing',len(cl)-len(unmatched),'(',len(matched),'HK MCQs get extra counts ) unmatched',len(unmatched))
print('unmatched repeat>=2:',sum(1 for c in unmatched if c['repeat']>=2),' singles:',sum(1 for c in unmatched if c['repeat']==1))
