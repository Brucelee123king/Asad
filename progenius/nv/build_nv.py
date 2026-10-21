import json,os
out=[]
second={}
for f in os.listdir('prev'):
    if f.startswith('second_') and f.endswith('.json'):
        for x in json.load(open('prev/'+f)): second[x['num']]=x
for n in range(1,23):
    d=json.load(open(f'out/q{n}.json'))
    q=("Find the figure that comes next in the series. (PDF Q%d)"%n) if d['type']=='series' else ("Find the odd shape out. (PDF Q%d)"%n)
    why=d['why'].strip()
    s=second.get(n)
    if os.environ.get('DROP') and str(n) in os.environ['DROP'].split(','): continue
    if n in (3,8,9): why+=' (This puzzle is hard to read: please also check with your answer key.)'
    out.append({'question':q,'options':d['options'],'correct':d['correct'],'facts':why,'rel':d['trick'].strip(),'nv':True,'stem':d['stem_groups'],'pma':True,'sec':'Non Verbal','rep':1})
json.dump(out,open('../nv_final.json','w'),ensure_ascii=False)
print(len(out))
