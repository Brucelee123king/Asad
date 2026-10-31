import json,re,collections,sys
un=json.load(open('unmatched.json'))
STOP=set("the a an of is was in on for to what which who whom does do did are were name any has have had be as at by from and or it its this that with how many much when where why whose will would can could should there their they them we you your i he she his her our us me my".split())
def tk(s): return [w for w in re.sub(r"[^a-z0-9 ]+",' ',s.lower()).split() if w not in STOP and len(w)>2]
df=collections.Counter(w for c in un for w in set(tk(c['q'])))
for i,c in enumerate(un): c['id']=i
def sk(c):
    t=sorted(set(tk(c['q'])),key=lambda w:(df[w],w))
    # most informative token that is shared with others groups similar questions together
    t2=[w for w in t if df[w]>1] or t or ['~']
    return (t2[0],c['q'].lower())
N=int(sys.argv[1]) if len(sys.argv)>1 else 100
items=sorted(un,key=sk)
for k in range(0,len(items),N):
    with open('mcq_in/b_%02d.jsonl'%(k//N+1),'w') as f:
        for c in items[k:k+N]:
            f.write(json.dumps({"id":c['id'],"q":c['q'],"also_asked_as":c['variants'][1:],"repeat":c['repeat'],"candidate_answers":c['answers'],"sure":c['confident_answer'],"kind":c['kind']},ensure_ascii=False)+'\n')
print(len(items),'items in',(len(items)+N-1)//N,'batches')
