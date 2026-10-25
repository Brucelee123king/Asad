"""Non Verbal = nv_final_32.json (19 first + 13 Pro Genius) + Forces Academy picture tests (nv3/out/<TYPE>_<NN>.json), Type I, II, III in order.
Answers are the book answers (answer_key.json)."""
import json,os,glob
d=os.path.dirname(os.path.abspath(__file__))
base=json.load(open(os.path.join(d,'..','nv_final_32.json')))
key=json.load(open(os.path.join(d,'answer_key.json')))
drop=set(json.load(open(os.path.join(d,'drop.json')))) if os.path.exists(os.path.join(d,'drop.json')) else set()
Q={'analogy':'Figure 1 is to figure 2 as figure 3 is to which option?','odd':'Which one is different from the rest?','matrix':'Choose the missing figure.','series':'Choose the missing figure.'}
out=list(base);n=0
for T in ('I','II','III'):
    for k in range(1,31):
        f=os.path.join(d,'out','%s_%02d.json'%(T,k))
        if not os.path.exists(f) or '%s_%02d'%(T,k) in drop: continue
        q=json.load(open(f))
        assert q['correct']==key[T][str(k)]-1,(T,k,q['correct'],key[T][str(k)])
        assert 2<=len(q['options'])<=8 and all(s.startswith('<svg') for s in q['options'])
        assert all(s.startswith('<svg') for g in q['stem_groups'] for s in g)
        out.append({'question':'%s (Forces Academy Picture Test %s, Q%d)'%(Q.get(q['kind'],'Choose the correct figure.'),T,k),
                    'options':q['options'],'correct':q['correct'],'facts':q['why'].strip(),'rel':q['trick'].strip(),'nv':True,
                    'stem':q['stem_groups'],'noq':bool(q.get('noq')),'pma':True,'sec':'Non Verbal','rep':1});n+=1
json.dump(out,open(os.path.join(d,'..','nv_final.json'),'w'),ensure_ascii=False)
print('added',n,'total',len(out))
