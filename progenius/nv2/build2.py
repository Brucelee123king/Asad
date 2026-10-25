"""Non Verbal = the first 19 (nv_final_19.json) + the 13 Pro Genius analogy questions (nv2/out/q1..q13.json).
The answer must equal the shaded answer of the PDF (answer_key.json)."""
import json,os
d=os.path.dirname(os.path.abspath(__file__))
base=json.load(open(os.path.join(d,'..','nv_final_19.json')))
key=json.load(open(os.path.join(d,'answer_key.json')))
out=list(base)
for n in range(1,14):
    q=json.load(open(os.path.join(d,'out','q%d.json'%n)))
    assert q['correct']=='ABCDE'.index(key[str(n)]),(n,q['correct'],key[str(n)])
    assert len(q['options'])==5 and all(s.startswith('<svg') for s in q['options'])
    assert len(q['stem_groups'])==2 and all(s.startswith('<svg') for g in q['stem_groups'] for s in g)
    out.append({'question':'The first shape changes in some way to become the second shape. Which option replaces the question mark? (Pro Genius Analogy Q%d)'%n,
                'options':q['options'],'correct':q['correct'],'facts':q['why'].strip(),'rel':q['trick'].strip(),'nv':True,
                'stem':q['stem_groups'],'pma':True,'sec':'Non Verbal','rep':1})
json.dump(out,open(os.path.join(d,'..','nv_final.json'),'w'),ensure_ascii=False)
print(len(out))
