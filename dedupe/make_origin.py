# Which PMA each kept MCQ first appeared in (149 / 150 / 151). Same grouping as apply.py.
import json,re,glob,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
f=json.load(open('../pma151/hk_final3.json')); d=json.load(open('hk_final_dedup.json'))
par=list(range(len(f)))
def fd(i):
    while par[i]!=i: par[i]=par[par[i]]; i=par[i]
    return i
for fn in sorted(glob.glob('r_*.txt')):
    for l in open(fn):
        m=re.match(r'\s*(\d+)\|(\d+)\s+SAME',l)
        if m:
            a,b=fd(int(m.group(1))),fd(int(m.group(2)))
            if a!=b: par[max(a,b)]=min(a,b)
roots=[i for i in range(len(f)) if fd(i)==i]
assert len(roots)==len(d) and all(f[r][1]==x[1] for r,x in zip(roots,d))
org=[149 if r<1676 else 150 if r<3201 else 151 for r in roots]
json.dump(org,open('hk_origin.json','w'))
print({p:org.count(p) for p in (149,150,151)})
