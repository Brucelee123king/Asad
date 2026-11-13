import json,re,collections
f=json.load(open('../pma151/hk_final3.json'))
STOP=set("the a an of is was in on for to what which who whom does do did are were name any has have had be as at by from and or it its this that with how many much when where why whose will would can could should there their they them we you your i he she his her our us me my called known first current currently present as of 2026 october pakistan".split())
def tk(s): return frozenset(w for w in re.sub(r"[^a-z0-9 ]+",' ',re.sub(r'\s*\(\d+\)\s*$','',s).lower()).split() if w not in STOP)
def nums(s): return tuple(sorted(re.findall(r'\d+',re.sub(r'\b(as of|in) (october )?2026\b','',s.lower()))))
def ans(x): return re.sub(r'[^a-z0-9]+',' ',x[2][x[3]].lower()).strip()
T=[tk(x[1]) for x in f]; N=[nums(x[1]) for x in f]; A=[ans(x) for x in f]
pairs=set()
by=collections.defaultdict(list)
for i in range(len(f)): by[A[i]].append(i)
for ids in by.values():
    for a in range(len(ids)):
        for b in range(a+1,len(ids)):
            i,j=ids[a],ids[b]
            if N[i]!=N[j] or not T[i] or not T[j]: continue
            if len(T[i]&T[j])/len(T[i]|T[j])>=0.25: pairs.add((i,j))
inv=collections.defaultdict(list)
for i,t in enumerate(T):
    for w in t: inv[w].append(i)
for i in range(len(f)):
    c=collections.Counter(j for w in T[i] if len(inv[w])<300 for j in inv[w] if j>i)
    for j,k in c.items():
        if N[i]==N[j] and len(T[i]&T[j])/len(T[i]|T[j])>=0.6: pairs.add((i,j))
pairs=sorted(pairs)
print(len(pairs),'candidate pairs')
L="ABCDE"
with open('pairs.txt','w') as o:
    for i,j in pairs:
        o.write('%d|%d\n  A: %s [ans: %s]\n  B: %s [ans: %s]\n'%(i,j,f[i][1],f[i][2][f[i][3]],f[j][1],f[j][2][f[j][3]]))
