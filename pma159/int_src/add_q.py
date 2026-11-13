"""Adds repeated initial-interview questions (admin's list, Nov 2026) to final.json. Safe to run again."""
import json, os
here = os.path.dirname(os.path.abspath(__file__)); p = os.path.join(here, 'final.json')
d = json.load(open(p, encoding='utf8'))
NEW = [
 ('Family', "What are your father's and mother's names?", "Say both names clearly and correctly, with your father's profession in one line if asked."),
 ('Education', 'What is your favourite subject, and why?', 'Pick a subject you are really good at and give one real reason. Be ready for 2-3 questions from that subject.'),
 ('Family', 'What is your rank among your siblings?', 'Say it simply, for example "I am the second of four: one elder brother, two younger sisters."'),
 ('About you', 'What is your favourite colour?', 'Give a short honest answer. If asked why, give one simple reason. Some officers ask the meaning or the colours of the national flag next.'),
 ('About you', 'Who is your favourite personality, and why?', 'Choose someone you really know about (for example Quaid-e-Azam, Allama Iqbal or a Nishan-e-Haider). Know 3-4 facts about their life and one quality you want to learn.'),
 ('Current affairs', 'Which newspaper do you read?', 'Only name a newspaper you really read. Read it for a few weeks before the interview; they will ask about today\'s headlines.'),
 ('Current affairs', 'Who is the editor of your favourite newspaper?', "Check the editor's name in your newspaper (it is printed in the paper) before the interview."),
 ('Current affairs', 'What is the price of your newspaper, and which part do you read most?', "Know today's price of the paper you read. Name the part you really read (editorials, national news, sports) and one thing you read in it recently."),
 ('Current affairs', 'What does NEWS stand for?', 'A popular saying is North, East, West, South: news from all directions. Strictly, "news" simply comes from the word "new".'),
 ('Family', "What is your father's salary?", "Answer honestly and calmly with an approximate figure. There is no right or wrong amount; they check honesty and confidence."),
 ('Hobbies & sports', 'Why do you like this game?', 'Give 2 real reasons (fitness, teamwork, discipline). Know its basic rules, number of players and a famous Pakistani player.'),
 ('About you', 'What is your weight, height, age and place of birth?', 'Know your exact weight (kg), height (feet/inches and cm), date of birth with age, and city/district of birth.'),
 ('Education', 'What were your matric and FSc roll numbers and percentages?', 'Learn your roll numbers, marks and percentages by heart. Officers sometimes check them against your form.'),
 ('Islamiat', "Calculate the zakat on your father's salary (savings).", 'Zakat is 2.5% (1/40) of savings above nisab kept for one lunar year. Example: Rs 1,00,000 saved for a year → Rs 2,500.'),
 ('Hobbies & sports', 'Who is your best friend?', 'Give the name, how long you have known them and what they do. Be ready for "good and bad qualities of your best friend".'),
]
have = {q.lower() for c in d['questions'] for q in d['questions'][c]}
n = 0
for cat, q, tip in NEW:
    if q.lower() in have: continue
    d['questions'].setdefault(cat, []).insert(0, q); d['answers'][q] = tip; n += 1
json.dump(d, open(p, 'w', encoding='utf8'), ensure_ascii=False)
print('added', n, {c: len(v) for c, v in d['questions'].items()})
