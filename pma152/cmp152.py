import json,re,glob
f=json.load(open('hk_final4.json')); L="ABCDE"; ans={}
for fn in sorted(glob.glob('verify/answers_*.txt')):
    for line in open(fn):
        m=re.match(r'\s*(\d+):\s*([A-EX])\s*\|\s*(\w+)\s*\|?\s*(.*)',line)
        if m: ans[int(m.group(1))]=(m.group(2),m.group(3),m.group(4).strip())
dis=[(n,L[f[n-1][3]],*ans[n]) for n in sorted(ans) if ans[n][0]!=L[f[n-1][3]]]
print(len(ans),'answers;',len(dis),'disagreements')
for n,mine,l,c,note in dis:
    x=f[n-1]; print(f"#{n} ours={mine}({x[2][x[3]][:35]}) blind={l}({c}) | {x[1][:120]} | opts={[o[:25] for o in x[2]]} | {note[:150]}")
