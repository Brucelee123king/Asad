# Second duplicate pass: merges paraphrased repeats listed in r2_same.txt (index pairs into hk_final_dedup.json).
# The earlier-placed MCQ is kept, repeat counts are added. -> hk_final_dedup2.json + hk_origin2.json
import json,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
f=json.load(open('hk_final_dedup.json')); org=json.load(open('hk_origin.json'))
par=list(range(len(f)))
def fd(i):
    while par[i]!=i: par[i]=par[par[i]]; i=par[i]
    return i
for l in open('r2_same.txt'):
    if 'SAME' in l:
        i,j=map(int,l.split()[0].split('|')); a,b=fd(i),fd(j)
        if a!=b: par[max(a,b)]=min(a,b)
groups={}
for i in range(len(f)): groups.setdefault(fd(i),[]).append(i)
out=[];oo=[]
for i,x in enumerate(f):
    if fd(i)!=i: continue
    x=list(x); x[6]=sum(f[j][6] for j in groups[i]); out.append(x); oo.append(org[i])
json.dump(out,open('hk_final_dedup2.json','w'),ensure_ascii=False); json.dump(oo,open('hk_origin2.json','w'))
print(len(f),'->',len(out),{p:oo.count(p) for p in (149,150,151)})
