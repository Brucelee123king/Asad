import json,re,collections,sys
R=json.load(open('/home/user/Asad/android-app/all_unique.json'))['recs']
D=collections.defaultdict(list)
def add(k,n,f,i,t): D[k].append((n,f,i,t))
for r in R:
    n=r['n'];q=r['q'];o=r['opts']
    fields=[('q',None,q)]+[('opts',i,x) for i,x in enumerate(o)]+[('facts',None,r.get('facts') or ''),('rel',None,r.get('rel') or '')]
    for f,i,t in fields:
        if not isinstance(t,str): add('nonstring',n,f,i,repr(t));continue
        if '  ' in t: add('double_space',n,f,i,t)
        if t!=t.strip(): add('edge_space',n,f,i,t)
        if re.search(r'[\[\]]|=>|Answer:|\(Original MCQ',t) and not(f=='q' and t.startswith('(Original MCQ #')): add('marker',n,f,i,t)
        if re.search(r'[ÂÃ�​‎‏﻿\xa0]|Ã|â€',t): add('encoding',n,f,i,t)
        if t.count('(')!=t.count(')') or t.count('[')!=t.count(']'): add('bracket_mismatch',n,f,i,t)
        if t.count('"')%2: add('quote_mismatch',n,f,i,t)
    if re.search(r'\s(rd|th|st|nd)\s*\??$',q): add('stuck_ordinal',n,'q',None,q)
    if re.search(r'\s[A-Za-z]\s*\??$',q) and not re.search(r'\b(Plan|Vitamin|Part|Class|Grade|Type|Group|Section|Article|Zone|Category|Block)\s[A-Z]\??$',q): add('stray_letter_end',n,'q',None,q)
    if re.search(r'\d(rd|th|st|nd)\b',q) is None and re.search(r'\d\s(rd|th|st|nd)\b',q): add('spaced_ordinal',n,'q',None,q)
    body=re.sub(r'^\(Original MCQ #\d+\)\s*','',q)
    if body==q and r['src']=='orig': add('orig_marker_missing',n,'q',None,q)
    if not body.rstrip().endswith('?') and re.match(r'(?i)(what|which|who|whom|whose|when|where|why|how|is|are|was|were|do|does|did|can|in which|name the)\b',body) and not body.rstrip().endswith(('.',':','_')): add('no_qmark',n,'q',None,q)
    if re.match(r'^\s*\d+[\.\)]\s',body) : add('lead_number_q',n,'q',None,q)
    for i,x in enumerate(o):
        if re.match(r'^\s*(\(?[A-Ha-h1-9]\)|[A-Ha-h1-9][\.\):]|\d+\.)\s',x): add('opt_prefix',n,'opts',i,x)
        if not x.strip(): add('opt_empty',n,'opts',i,x)
        if len(x)>150: add('opt_long',n,'opts',i,x)
        if len(x.strip())>8 and x.strip().lower() in body.lower(): add('opt_in_question',n,'opts',i,x)
    nz=[x.strip().lower() for x in o]
    if len(set(nz))<len(nz): add('opt_dup',n,'opts',None,' | '.join(o))
    if len(o)!=4: add('opt_count',n,'opts',None,str(len(o)))
    if not isinstance(r['ok'],int) or not 0<=r['ok']<len(o): add('bad_ok',n,'ok',None,str(r['ok']))
    if re.search(r'\b(\w+)\s+\1\b',q,re.I): add('repeated_word',n,'q',None,q)
if __name__=='__main__':
    for k,v in sorted(D.items()):
        print(k,len(v))
        for x in v[:int(sys.argv[1]) if len(sys.argv)>1 else 3]: print('   ',x[0],x[1],x[2],repr(x[3][:140]))
