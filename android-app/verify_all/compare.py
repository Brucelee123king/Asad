import json,glob,re,collections
r={x['n']:x for x in json.load(open('all_unique.json'))['recs']}
ans={}
for f in sorted(glob.glob('verify_all/out/b_*.txt')):
    for l in open(f):
        m=re.match(r'\s*(\d+):\s*([A-EX])\s*\|\s*(\w+)\s*\|\s*(.*)',l)
        if m: ans[int(m[1])]=(m[2],m[3],m[4].strip())
agree=[];dis=[];low=[];x=[];missing=[]
for n,q in r.items():
    if n not in ans: missing.append(n);continue
    a,c,note=ans[n]
    if a=='X': x.append(n)
    elif 'ABCDE'.index(a)!=q['ok']: dis.append(n)
    elif c=='low': low.append(n)
    else: agree.append(n)
print(dict(total=len(r),answered=len(ans),agree=len(agree),disagree=len(dis),lowagree=len(low),X=len(x),missing=len(missing)))
json.dump(dict(dis=dis,low=low,x=x,missing=missing),open('verify_all/flags.json','w'))
