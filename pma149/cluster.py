import json,glob,re,collections,sys
rows=[]
for f in sorted(glob.glob('extract/ex_*.jsonl')):
    for l in open(f,encoding='utf8'):
        l=l.strip()
        if l:
            r=json.loads(l); r['file']=f; rows.append(r)
STOP=set("the a an of is was in on for to what which who whom does do did are were name any has have had be as at by from and or it its this that with how many much when where why whose will would can could should there their they them we you your i he she his her our us me my".split())
def toks(s):
    s=s.lower().replace('%',' percent ')
    s=re.sub(r"[^a-z0-9 ]+",' ',s)
    out=[]
    for w in s.split():
        if w in STOP: continue
        if len(w)>3 and w.endswith('ies'): w=w[:-3]+'y'
        elif len(w)>3 and w.endswith('s') and not w.endswith('ss'): w=w[:-1]
        out.append(w)
    return out
for r in rows:
    t=toks(r['q']); r['t']=t
    r['nums']=tuple(sorted(w for w in t if re.search(r'\d',w)))
    r['set']=frozenset(w for w in t if not re.search(r'\d',w))
# union-find on exact key first, then Jaccard within same nums
parent=list(range(len(rows)))
def find(x):
    while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
def union(a,b):
    a,b=find(a),find(b)
    if a!=b: parent[b]=a
bykey=collections.defaultdict(list)
for i,r in enumerate(rows): bykey[(r['nums'],tuple(sorted(r['set'])))].append(i)
for ids in bykey.values():
    for j in ids[1:]: union(ids[0],j)
# Jaccard among distinct keys sharing a content word (inverted index)
keys=list(bykey.keys())
inv=collections.defaultdict(list)
for ki,(nums,st) in enumerate(keys):
    for w in st: inv[w].append(ki)
done=set()
TH=float(sys.argv[1]) if len(sys.argv)>1 else 0.75
for ki,(nums,st) in enumerate(keys):
    st=frozenset(st)
    if not st: continue
    cand=collections.Counter()
    for w in st:
        if len(inv[w])>400: continue
        for kj in inv[w]:
            if kj>ki: cand[kj]+=1
    for kj,c in cand.items():
        n2,s2=keys[kj]
        if n2!=nums: continue
        inter=len(st&frozenset(s2)); uni=len(st|frozenset(s2))
        if uni and inter/uni>=TH and min(len(st),len(s2))>=2:
            union(bykey[keys[ki]][0],bykey[keys[kj]][0])
cl=collections.defaultdict(list)
for i,r in enumerate(rows): cl[find(i)].append(i)
clusters=[]
for ids in cl.values():
    exps=sorted({rows[i]['exp'] for i in ids})
    qs=collections.Counter(rows[i]['q'].strip() for i in ids)
    ans=collections.Counter(rows[i]['a'].strip() for i in ids if rows[i].get('a','').strip())
    sure=[rows[i]['a'].strip() for i in ids if rows[i].get('a','').strip() and rows[i].get('ok',True)]
    clusters.append({
        'q':qs.most_common(1)[0][0],
        'variants':[q for q,_ in qs.most_common(4)],
        'repeat':len(exps),'mentions':len(ids),'exps':exps[:12],
        'answers':[a for a,_ in ans.most_common(3)],
        'confident_answer':bool(sure),
        'kind':collections.Counter(rows[i].get('kind','academic') for i in ids).most_common(1)[0][0],
    })
clusters.sort(key=lambda c:(-c['repeat'],-c['mentions'],c['q'].lower()))
json.dump(clusters,open('clusters.json','w'),ensure_ascii=False,indent=0)
rc=collections.Counter(min(c['repeat'],10) for c in clusters)
print(len(rows),'mentions ->',len(clusters),'clusters; repeat histogram (10 = 10+):',sorted(rc.items()))
for c in clusters[:12]: print(c['repeat'],c['mentions'],c['q'],'|',c['answers'][:1])
