import json,os
out=[]
second={}
for f in os.listdir('prev'):
    if f.startswith('second_') and f.endswith('.json'):
        for x in json.load(open('prev/'+f)): second[x['num']]=x
for n in range(1,23):
    d=json.load(open(f'out/q{n}.json'))
    q=("Q%d. Find the figure that comes next in the series."%n) if d['type']=='series' else ("Q%d. Find the odd shape out."%n)
    why=d['why'].strip()
    s=second.get(n)
    if os.environ.get('DROP') and str(n) in os.environ['DROP'].split(','): continue
    out.append({'question':q,'options':d['options'],'correct':d['correct'],'facts':why,'rel':d['trick'].strip(),'nv':True,'stem':d['stem_groups'],'pma':True,'sec':'Non Verbal','rep':1})
json.dump(out,open('../nv_final.json','w'),ensure_ascii=False)
print(len(out))
