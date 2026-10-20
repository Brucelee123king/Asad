import re,collections,json,scan
from spellchecker import SpellChecker
sp=SpellChecker()
wl=set(w.strip().lower() for w in open('/home/user/Asad/android-app/qa/whitelist.txt') if w.strip()) if __import__('os').path.exists('/home/user/Asad/android-app/qa/whitelist.txt') else set()
cnt=collections.Counter();ex={};cap=collections.Counter()
for r in scan.R:
    for f,i,t in [('q',None,re.sub(r'^\([^)]*\)\s*','',r['q']))]+[('opts',j,x) for j,x in enumerate(r['opts'])]+[('facts',None,r['facts'] or ''),('rel',None,r['rel'] or '')]:
        for m in re.finditer(r"[A-Za-z][A-Za-z'’\-]*[A-Za-z]|[A-Za-z]",t):
            w=m.group(0)
            if len(w)<4: continue
            for p in re.split(r"[-]",w):
                p=p.replace("’","'")
                if p.endswith("'s"):p=p[:-2]
                pl=p.lower()
                if len(p)<4 or pl in wl or pl in sp: continue
                if p[0].isupper() : cap[pl]+=1;continue
                cnt[pl]+=1; ex.setdefault(pl,(r['n'],f,t[:100]))
json.dump({'lower':cnt.most_common(),'cap':cap.most_common()},open('/tmp/claude-0/spell_raw.json','w'))
print(len(cnt),len(cap))
for w,c in cnt.most_common(400): print(w,c,ex[w][0],sp.correction(w))
