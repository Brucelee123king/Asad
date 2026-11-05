"""Adds essay groups + how-to-start outlines to final.json (keys esg, urg, esG, esT).
usage: python3 essay_guide.py   (edits final.json in place)"""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(here, 'final.json'); d = json.load(open(p, encoding='utf8'))
EN = {
 'army': [0,55,56,57,58,87,108,109,110,111,112,113],
 'me': [1,2,3,4,5,6,7,10,18,20,24,40,41,97,98,99,100,101,102,103,106,140,141,142,143,144,145,146,147,148],
 'pak': [13,26,27,28,30,48,51,52,61,62,64,65,66,67,68,69,72,83,84,85,86,114,115,116,117,118,120,123],
 'soc': [12,21,22,36,43,50,59,60,75,76,77,78,80,104,105,107,121,135,136,137,138,139],
 'edu': [11,23,37,38,42,53,54,70,71,73,74,125,126,127,128,129],
 'sci': [14,15,16,29,31,39,79,124,130,131,132,133,134],
 'wis': [8,9,17,19,25,32,33,34,35,44,45,46,47,49,63,81,82,88,89,90,91,92,93,94,95,96,119,122,149]}
UR = {
 'army': [0,13,45,46,47,48,49,50],
 'me': [1,2,3,4,5,6,7,8,9,10,11,12],
 'pak': [38,39,40,41,42,43,44,51,52,53,54,55,56,57,58,59,60,61,68,69],
 'soc': [14,15,16,34,64],
 'edu': [17,18,19,20,21,22,23],
 'sci': [62,63,65,66,67],
 'wis': [24,25,26,27,28,29,30,31,32,33,35,36,37]}
def flat(G, n):
    out = [None]*n
    for g, ix in G.items():
        for i in ix:
            assert out[i] is None, (g, i); out[i] = g
    assert None not in out, [i for i, x in enumerate(out) if x is None]
    return out
d['esg'] = flat(EN, len(d['essays'])); d['urg'] = flat(UR, len(d['urdu']))
d['esG'] = [['army','🪖 Army'],['me','👤 Personal'],['pak','🇵🇰 Pakistan'],['soc','👥 Society'],['edu','🎓 Education'],['sci','🔬 Science & Tech'],['wis','💡 Sayings & Values']]
# how-to-start outline per group: [ [step, what to write]... ], start line ({T} = topic)
d['esT'] = {
 'army': {'en': [['Introduction','Open with a strong line about the Army and say what the topic means to you.'],['Point 1','The role and duty: defence of borders and of the nation.'],['Point 2','Real examples: 1965 war, operations against terrorism, help in floods and earthquakes.'],['Point 3','Your own link: why you want to serve, what qualities you bring.'],['Conclusion','A short pledge: you are ready to serve Pakistan with honour.']],
          'ur': [['تمہید','کسی شعر یا مضبوط جملے سے آغاز کریں اور موضوع کی اہمیت بتائیں۔'],['پہلا نکتہ','پاک فوج کا فرض: سرحدوں اور قوم کا دفاع۔'],['دوسرا نکتہ','مثالیں: 1965 کی جنگ، دہشت گردی کے خلاف آپریشن، سیلاب اور زلزلے میں مدد۔'],['تیسرا نکتہ','آپ کا اپنا تعلق: آپ فوج میں کیوں آنا چاہتے ہیں۔'],['اختتام','عزم کے ساتھ ختم کریں کہ آپ وطن کی خدمت کے لیے تیار ہیں۔']],
          's': 'A nation is only as strong as the men who stand guard at its borders, and "{T}" reminds me why I want to be one of them.',
          'su': 'کسی قوم کی طاقت اس کے محافظوں سے ہوتی ہے، اور "{T}" مجھے یاد دلاتا ہے کہ میں بھی ان میں شامل ہونا چاہتا ہوں۔'},
 'me': {'en': [['Introduction','Set the scene: when, where and who. One or two lines only.'],['Point 1','What happened, or describe the person / thing clearly.'],['Point 2','How you felt and what you did.'],['Point 3','What you learned from it.'],['Conclusion','How it shaped you today and links to your aim of joining the Army.']],
        'ur': [['تمہید','وقت، جگہ اور لوگ: مختصر تعارف۔'],['پہلا نکتہ','کیا ہوا، یا اس شخص / چیز کا صاف بیان۔'],['دوسرا نکتہ','آپ نے کیا محسوس کیا اور کیا کیا۔'],['تیسرا نکتہ','آپ نے اس سے کیا سیکھا۔'],['اختتام','اس نے آج آپ کو کیسا بنایا اور فوج میں آنے کے مقصد سے تعلق۔']],
        's': 'Every person has a few things in life that shape who they become. For me, "{T}" is one of them.',
        'su': 'ہر انسان کی زندگی میں کچھ باتیں ایسی ہوتی ہیں جو اسے بدل دیتی ہیں۔ میرے لیے "{T}" انہی میں سے ایک ہے۔'},
 'pak': {'en': [['Introduction','Explain the topic in simple words and say why it matters for Pakistan.'],['Point 1','Causes or background.'],['Point 2','Effects on people and the country.'],['Point 3','Practical solutions: government, society and youth.'],['Conclusion','End with hope: Pakistan can overcome this with unity and hard work.']],
         'ur': [['تمہید','موضوع کو آسان الفاظ میں بیان کریں اور پاکستان کے لیے اس کی اہمیت بتائیں۔'],['پہلا نکتہ','اسباب یا پس منظر۔'],['دوسرا نکتہ','لوگوں اور ملک پر اثرات۔'],['تیسرا نکتہ','عملی حل: حکومت، معاشرہ اور نوجوان۔'],['اختتام','امید کے ساتھ ختم کریں: اتحاد اور محنت سے ہم کامیاب ہوں گے۔']],
         's': 'Pakistan is a country full of potential, but "{T}" is a subject every young Pakistani must understand.',
         'su': 'پاکستان بے پناہ صلاحیتوں کا ملک ہے، لیکن "{T}" ایسا موضوع ہے جسے ہر نوجوان کو سمجھنا چاہیے۔'},
 'soc': {'en': [['Introduction','Define the topic and say where we see it in our society.'],['Point 1','The good side, or the reasons behind it.'],['Point 2','The bad side, or the problems it creates.'],['Point 3','Your balanced opinion with one example.'],['Conclusion','What we should do, as individuals and as a society.']],
         'ur': [['تمہید','موضوع کی وضاحت کریں اور بتائیں کہ ہمارے معاشرے میں یہ کہاں نظر آتا ہے۔'],['پہلا نکتہ','اچھا پہلو یا اس کی وجوہات۔'],['دوسرا نکتہ','برا پہلو یا اس سے پیدا ہونے والے مسائل۔'],['تیسرا نکتہ','ایک مثال کے ساتھ آپ کی متوازن رائے۔'],['اختتام','ہمیں فرد اور معاشرے کے طور پر کیا کرنا چاہیے۔']],
         's': 'A society is shaped by the habits and values of its people, and "{T}" shows this clearly.',
         'su': 'معاشرہ اپنے لوگوں کی عادات اور اقدار سے بنتا ہے، اور "{T}" اس کی واضح مثال ہے۔'},
 'edu': {'en': [['Introduction','Say why education is the key to progress.'],['Point 1','The present situation in Pakistan.'],['Point 2','The main problems or arguments on both sides.'],['Point 3','Your suggestions to improve it.'],['Conclusion','Educated youth will build a strong Pakistan.']],
         'ur': [['تمہید','بتائیں کہ تعلیم ترقی کی کنجی ہے۔'],['پہلا نکتہ','پاکستان میں موجودہ صورتحال۔'],['دوسرا نکتہ','بڑے مسائل یا دونوں طرف کے دلائل۔'],['تیسرا نکتہ','بہتری کے لیے آپ کی تجاویز۔'],['اختتام','تعلیم یافتہ نوجوان ہی مضبوط پاکستان بنائیں گے۔']],
         's': 'Education is the foundation of every strong nation, and "{T}" is an important part of that story.',
         'su': 'تعلیم ہر مضبوط قوم کی بنیاد ہے، اور "{T}" اسی کہانی کا اہم حصہ ہے۔'},
 'sci': {'en': [['Introduction','Say how science or technology has changed our daily life.'],['Point 1','Benefits, with a simple example.'],['Point 2','Harms or dangers.'],['Point 3','How to use it wisely (students, parents, government).'],['Conclusion','Technology is a good servant but a bad master.']],
         'ur': [['تمہید','بتائیں کہ سائنس اور ٹیکنالوجی نے روزمرہ زندگی کیسے بدل دی۔'],['پہلا نکتہ','فوائد، ایک آسان مثال کے ساتھ۔'],['دوسرا نکتہ','نقصانات یا خطرات۔'],['تیسرا نکتہ','اسے سمجھداری سے کیسے استعمال کریں۔'],['اختتام','ٹیکنالوجی اچھی خادم ہے مگر بری آقا۔']],
         's': 'Science has changed the way we live, learn and talk, and "{T}" is one of the clearest examples of this change.',
         'su': 'سائنس نے ہمارے جینے، سیکھنے اور بات کرنے کا انداز بدل دیا ہے، اور "{T}" اس کی واضح مثال ہے۔'},
 'wis': {'en': [['Introduction','Explain the meaning of the saying or value in your own words.'],['Point 1','An example from Islam or history.'],['Point 2','An example from daily life or your own life.'],['Point 3','Why it matters for a student and a future officer.'],['Conclusion','Repeat the main idea in one strong line.']],
         'ur': [['تمہید','اس قول یا خوبی کا مطلب اپنے الفاظ میں بیان کریں۔'],['پہلا نکتہ','اسلام یا تاریخ سے ایک مثال۔'],['دوسرا نکتہ','روزمرہ زندگی یا اپنی زندگی سے مثال۔'],['تیسرا نکتہ','ایک طالب علم اور مستقبل کے افسر کے لیے اس کی اہمیت۔'],['اختتام','مرکزی خیال کو ایک مضبوط جملے میں دہرائیں۔']],
         's': 'Some lessons never get old. "{T}" is one of them, and it has guided great people throughout history.',
         'su': 'کچھ سبق کبھی پرانے نہیں ہوتے۔ "{T}" بھی انہی میں سے ایک ہے۔'}}
json.dump(d, open(p, 'w', encoding='utf8'), ensure_ascii=False)
print('ok', {k: len(v) for k, v in EN.items()})
