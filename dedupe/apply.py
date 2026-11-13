import json,re,glob,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
f=json.load(open('../pma151/hk_final3.json'))
par=list(range(len(f)))
def fd(i):
    while par[i]!=i: par[i]=par[par[i]]; i=par[i]
    return i
same=0
for fn in sorted(glob.glob('r_*.txt')):
    for l in open(fn):
        m=re.match(r'\s*(\d+)\|(\d+)\s+SAME',l)
        if m:
            i,j=int(m.group(1)),int(m.group(2)); same+=1
            a,b=fd(i),fd(j)
            if a!=b: par[max(a,b)]=min(a,b)
groups={}
for i in range(len(f)): groups.setdefault(fd(i),[]).append(i)
out=[]
for i,x in enumerate(f):
    if fd(i)!=i: continue
    x=list(x); x[6]=sum(f[j][6] for j in groups[i]); out.append(x)
json.dump(out,open('hk_final_dedup.json','w'),ensure_ascii=False)
big=sorted((len(g),f[r][1][:60]) for r,g in groups.items() if len(g)>2)[-10:]
print('SAME pairs',same,'; MCQs',len(f),'->',len(out),'; removed',len(f)-len(out),'; blocks',(len(out)+49)//50)
print('largest groups:',big)
