import json,re,glob,sys
f=json.load(open('hk_final.json',encoding='utf8'))
L="ABCDE"
ans={}
for fn in sorted(glob.glob('verify_hk/answers_*.txt')):
    off=840 if fn.endswith('_5.txt') else 0
    for line in open(fn,encoding='utf8'):
        m=re.match(r'\s*(\d+):\s*([A-EX])\s*\|\s*(\w+)\s*\|?\s*(.*)',line)
        if m: ans[off+int(m.group(1))]=(m.group(2),m.group(3),m.group(4).strip())
dis=[]
for n,(sec,q,o,a,why,rel,rep) in enumerate(f,1):
    if n not in ans: continue
    l,c,note=ans[n]
    if l!=L[a]: dis.append((n,L[a],l,c,note))
print(len(ans),'answers read;',len(dis),'disagreements')
for n,mine,theirs,c,note in dis:
    sec,q,o,a,why,rel,rep=f[n-1]
    print(f"#{n} ours={mine}({o[a][:30]}) blind={theirs}({c}) | {q[:110]} | note: {note[:170]}")
