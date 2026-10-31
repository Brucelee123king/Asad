"""Builds format_fixes.json (q/opts/rel only, sure fixes), facts_candidates.json (NOT applied) and format_report.md."""
import json,collections,re,scan
R={r['n']:r for r in scan.R}
fixes=[];facts=[]
def fx(n,field,idx,old,new,why):
    cur=R[n]['q'] if field=='q' else R[n]['opts'][idx]
    assert old==cur,(n,old,cur)
    fixes.append(dict(n=n,field=field,index=idx,old=old,new=new,why=why))
for n in (113,173): fx(n,'opts',2,'Surah An-Naml, =)','Surah An-Naml','stray ", =)" characters after option text')
for n,i in((570,2),(928,2)): fx(n,'opts',i,R[n]['opts'][i],R[n]['opts'][i].replace('lonian','Ionian'),'OCR: lowercase L instead of capital I in "Ionian"')
# facts: leading-slash/l-for-I OCR garbles (candidates only, user said do not touch facts)
pat=re.compile(r'(?<![A-Za-z])/(slamabad|qbal|gbal|qgbal|srael|taly|smail|shaq|tcame|mtiaz)')
mp={'slamabad':'Islamabad','qbal':'Iqbal','gbal':'Iqbal','qgbal':'Iqbal','srael':'Israel','taly':'Italy','smail':"Ismail",'shaq':'Ishaq','tcame':'It came','mtiaz':'Imtiaz'}
for r in scan.R:
    for m in pat.finditer(r['facts'] or ''):
        facts.append(dict(n=r['n'],field='facts',index=None,old=m.group(0),new=mp[m.group(1)],why='OCR: "/" for capital I (candidate, facts not applied)'))
json.dump({'fixes':fixes},open('format_fixes.json','w'),indent=1,ensure_ascii=False)
json.dump({'facts_candidates':facts},open('facts_candidates_not_applied.json','w'),indent=1,ensure_ascii=False)
D=scan.D
notes={'double_space':'double spaces','edge_space':'leading/trailing space','encoding':'mixed-encoding chars','stuck_ordinal':'question ends with stuck rd/th/st','spaced_ordinal':'digit + spaced ordinal','lead_number_q':'leading "12." in question','opt_empty':'empty options','nonstring':'non-string fields','bad_ok':'invalid ok index',
'opt_prefix':'option starts with A)/1. (all false positives: initials like "A. K. Huq")','stray_letter_end':'question ends with single letter (almost all legit: A/B/x/y in maths/reasoning)','no_qmark':'no "?" (8 are "(current affairs)" suffix, 1 series)','opt_count':'records with 3 or 5 options (22 have 3, 156 have 5, mostly Forces Academy)','opt_dup':'duplicate options','opt_long':'options >150 chars','opt_in_question':'option text (>8 chars) also in question (mostly legit)','marker':'leftover markers [ ] => Answer:','bracket_mismatch':'unbalanced brackets','quote_mismatch':'odd number of double quotes','repeated_word':'repeated word in question'}
L=['# Format QA report','','Data: 8931 records, not modified. Scripts: qa/scan.py (defects), qa/spell.py (spelling, whitelist.txt), qa/make_fixes.py (outputs).','','## Counts per defect type (raw hits)','']
for k in sorted(notes): L.append(f'- {k}: {len(D.get(k,[]))} - {notes[k]}')
L+=['',f'## Proposed fixes (format_fixes.json): {len(fixes)}','- 2x "Surah An-Naml, =)" -> "Surah An-Naml" (#113, #173)','- 2x "lonian" -> "Ionian" (#570, #928)','',
'## Not applied (need human decision)',
f'- {len(facts)} OCR garbles in facts ("/slamabad" for Islamabad etc.) in facts_candidates_not_applied.json; facts were not to be touched.',
'- Many other garbled facts (e.g. #194, #254, #450 "<i] A ee nO", #830, #865 "astronom Wy") need source text.',
'- Q prefixes: "(Original MCQ #n)" on all 1000 src=orig and none elsewhere; "(Forces Academy Test t · Qn)" on all 771 FA. Consistent.',
'- 8 questions end "(current affairs)" without "?" (#1229-1236); #6729 series question has no "?".',
'- Forces Academy questions with options embedded in q text (e.g. #1821 "A. K, B. L, C. M"); 178 records with 3/5 options.',
'- Options with same text as question/odd distractors in src=orig (e.g. #570 "The National Assembly", #173 duplicate An-Naml, #6816 Ff/Ee/Ed/EE case-only dup).',
'- Quote mismatch #70,#76,#186,#205: curly open quote with straight close quote (cosmetic).',
'- Spelling: British spellings (metres, centre, colour) used consistently, left alone. Deliberate misspelling options (e.g. #1284, #2722, #3197, #6831) are intended. Whitelist in whitelist.txt.']
open('format_report.md','w').write('\n'.join(L)+'\n')
print(len(fixes),len(facts))
