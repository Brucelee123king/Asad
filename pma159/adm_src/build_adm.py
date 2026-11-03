import json, html
V = ["What is 90% of 90?", "What is 90% of 60?", "What is the log of 100?", "Find one-third of 10% of 90.", "Find one-third of 10% of 120.",
     "What is one-quarter of one-tenth of 120?", "If 5 persons write 5 pages in 5 minutes, how much time will 1 person take to write 1 page?",
     "A class has 500 students, 340 boys and 160 girls. Find the percentage of girls.", "Today is Monday. What day will it be after 15 days?",
     "A train moves twice as fast as a car. If the car moves at 60 km/h, how far will the train travel in 30 minutes?",
     "A man walks North, turns left and then turns left again. What is his final direction?",
     "Rida is 5 years old and Ali is 3 times her age. What will be Ali's age when Rida is 20?", "Rearrange the letters: PDOLERA.",
     "ROUGH : SMOOTH :: CRUDE : ?", "PRESENT : PAST :: PRECEDING : ?", "Find the next term: 1Z, 3X, 5V, 7T, __?",
     "Find the letters that look the same in a mirror: MVTWTVM.", "Find a word using the 18th, 5th, 19th and 20th letters.",
     "Find the odd one out: Monkey, Chimpanzee, Panda.", "Find the odd one out: Football and other given options.",
     "A committee has 24 members, including 6 males. Find the female percentage.", "There are 30 passengers and 2/3 are males. Find the number of females.",
     "Why do we boil milk?", "Why do parents send their children to school?"]
N = ["Mirror image questions.", "Clockwise rotation.", "Anticlockwise rotation.", "Missing figures.", "Complete the missing parts of pictures.",
     "Triangle, square and rectangular shape patterns.", "Arrange the arrows in the correct sequence.", "Identify the next figure in a series.",
     "Identify similar and different figures.", "Figure rotation and shape recognition."]
AC = [("🕌 Islamic Studies", ["Against whom was Ghazwa Badr fought?", "Which Ghazwa is also called Ghazwa Ahzab?", "Who was the adopted son of Prophet Muhammad ﷺ?",
                             "What was the main objective of the Khilafat Movement?"]),
      ("🇵🇰 Pakistan Studies & History", ["What is the longest river of Pakistan?", "On which date did Pakistan join the UN?",
                                         "Which agreement was signed after the 1965 Indo-Pak War?", "Who was the first Chief Justice of Pakistan?",
                                         "Who became Prime Minister after Liaquat Ali Khan?", "Who was the head of state under the 1973 Constitution?",
                                         "When did the Partition of Bengal take place?",
                                         "Who was the British Prime Minister at the time of the Partition of the Subcontinent?",
                                         "Which rivers were given to Pakistan under the Indus Waters Treaty?",
                                         "Through which route did invaders enter the Subcontinent?", "What was the price paid by Gulab Singh to purchase Kashmir?",
                                         "Who built the Badshahi Mosque?", "When were the Minto-Morley Reforms introduced?",
                                         "When did the Chauri Chaura Incident take place?", "When was the Ottoman Empire founded?"]),
      ("🌍 General Knowledge & Current Affairs", ["Where is NATO Headquarters located?", "Which is the largest planet in the Solar System?",
                                                 "Which planet has the highest number of moons?", "What is the capital of Ghana?",
                                                 "Lira is the currency of which country?", "Who is the current President of France?",
                                                 "What is the plain face count of a prism?", "What is the antonym of Modesty?",
                                                 "What is the synonym of Refrain?", "Identify the odd one out: Islamabad, Karachi, Quetta and Lahore."])]
ADV = ["Practice basic mathematics and percentages.", "Prepare alphabetical series and coding/decoding.", "Practice mirror images and figure patterns.",
       "Revise Pakistan Studies and Islamic Studies.", "Improve your speed and time management."]

e = html.escape
def ol(xs, start=1):
    return '<ol start="%d">' % start + ''.join('<li>%s</li>' % e(x) for x in xs) + '</ol>'
def sec(ic, title, sub, body, op=False):
    return ('<div class="ax-s%s"><button type="button" class="ax-sh"><span class="ax-si">%s</span><span class="ax-st"><b>%s</b><small>%s</small></span><span class="ax-ar">▸</span></button><div class="ax-sb">%s</div></div>'
            % (' open' if op else '', ic, e(title), e(sub), body))

TEST = ('<div class="ax-hero"><div class="ax-k">🪖 PMA 159 LONG COURSE</div><h2>My Complete Test Experience</h2>'
        '<div class="ax-meta"><span>👤 Asadullah</span><span>📍 D.I. Khan</span><span>📅 03 Nov 2026</span><span>⏰ 07:00 – 09:00 AM</span></div>'
        '<div class="ax-pass">✅ Alhamdulillah, PASSED! ❤️🇵🇰</div></div>'
        + sec('🔤', 'Verbal Intelligence', '24 questions • Moderate',
              '<p>Verbal portion was moderate. Most questions were based on basic mathematics, analytical reasoning, alphabetical series and general IQ.</p>' + ol(V), True)
        + sec('🧩', 'Non-Verbal Intelligence', '10 patterns • Moderate',
              '<p>Non-verbal portion was moderate and included different figure-based questions.</p>' + ol(N))
        + sec('📚', 'Academic Portion', '29 questions • Easy',
              '<p>Academic portion was comparatively easy and covered Pakistan Studies, Islamic Studies, General Knowledge, History and Current Affairs.</p>'
              + ''.join('<h4>%s</h4>%s' % (e(t), ol(q, st)) for (t, q), st in zip(AC, (1, 5, 20))))
        + sec('💡', 'Overall Experience & Advice', '6 tips',
              '<p>Overall, the test was moderate and manageable. Verbal required quick calculations and logical thinking, while Non-Verbal required concentration and pattern recognition. Academic was mostly based on Pakistan Studies, Islamic Studies, General Knowledge and History.</p>'
              + '<ul class="ax-ok"><li><b>⏰ Time management is the MOST important. Focus on managing your time more than anything else.</b></li>' + ''.join('<li>%s</li>' % e(a) for a in ADV) + '</ul><p class="ax-end">Best of luck to all PMA 159 candidates!<br>🇵🇰 Pakistan Army Zindabad!</p>'))

MED = ('<div class="ax-hero" style="background:linear-gradient(135deg,#075985,#0284c7)"><div class="ax-k">🩺 INITIAL MEDICAL</div><h2>Initial Medical</h2>'
       '<div class="ax-meta"><span>📅 03 Nov 2026</span><span>📍 D.I. Khan</span></div><div class="ax-pass">✅ Alhamdulillah, PASSED!</div></div>'
       '<div class="ax-note">✍️ My full medical experience is coming soon.</div>'
       + sec('🩺', 'What is usually checked', 'General guide',
             '<ul class="ax-ok"><li><b>Eyesight</b>: checked without glasses.</li><li><b>Height</b>: see the Eligibility step in the Roadmap.</li>'
             '<li><b>Weight / BMI</b>: check yours in the BMI tab.</li><li><b>Flat feet</b>: the arch of the foot is checked.</li>'
             '<li><b>Knock knees</b>: stand with feet together; they check if the knees touch.</li><li><b>Chest</b>: chest size and expansion are measured.</li></ul><p class="ax-sm">General guide only; follow the instructions at your centre.</p>', True))

PHY = ('<div class="ax-hero" style="background:linear-gradient(135deg,#9a3412,#ea580c)"><div class="ax-k">🏃 INITIAL PHYSICAL TEST</div><h2>Initial Physical Test</h2>'
       '<p>After the medical, they check your fitness with running and some exercises.</p><div class="ax-pass" style="background:#ffedd5;color:#9a3412">⏳ My physical test is next • my notes coming after</div></div>'
       + sec('🏋️', 'Events usually taken', '5 events', '<ul class="ax-ok"><li><b>1.6 km run</b>: about 8 minutes</li><li><b>Push-ups</b>: about 15 in 2 minutes</li>'
             '<li><b>Sit-ups</b>: about 20 in 2 minutes</li><li><b>Chin-ups</b>: about 3</li><li><b>Ditch jump</b>: about 7 × 7 feet</li></ul>'
             '<p class="ax-sm">Commonly reported numbers; follow the instructions at your centre.</p>', True)
       + sec('📅', 'How to prepare', '6 tips', '<ul class="ax-ok"><li>Run every day; build up slowly</li><li>Push-ups and sit-ups daily, with correct form</li>'
             '<li>Practise chin-ups on a bar</li><li>Sleep well and eat healthy food</li><li>Wear proper running shoes</li><li>Warm up before; do not get injured before the test</li></ul>'))

INT = ('<div class="ax-hero" style="background:linear-gradient(135deg,#5b21b6,#8b5cf6)"><div class="ax-k">🗣️ INITIAL INTERVIEW</div><h2>Initial Interview Guide</h2>'
       '<p>A short one-to-one talk with an officer. They check your confidence, honesty, family background and why you want to join.</p><div class="ax-pass" style="background:#ede9fe;color:#5b21b6">🔒 Coming soon • my notes after my interview</div></div>'
       + sec('❓', 'Most asked questions', 'With tips', '<ul class="ax-qa">'
             '<li><b>Tell me about yourself.</b><span>Name, city, education, family in 2 lines, hobbies, why Army.</span></li>'
             '<li><b>Why do you want to join the Army?</b><span>Your own honest reason: service, discipline, leadership.</span></li>'
             '<li><b>What does your father do?</b><span>Simple and honest; show respect.</span></li>'
             '<li><b>Your strengths and weaknesses?</b><span>One strength with an example; one weakness you are improving.</span></li>'
             '<li><b>Any current affairs?</b><span>Know Pakistan\'s main leaders and recent big news.</span></li></ul>', True)
       + sec('🗣️', 'Make your introduction', '1 minute', '<p>Prepare these 6 lines and practise them aloud:</p><ol><li>My name is…</li><li>I am from (city)…</li><li>I studied (FA/FSc, marks)…</li><li>My family: my father is…</li><li>My hobbies are…</li><li>I want to join the Army because…</li></ol>')
       + sec('🚪', 'Inside the room: step by step', '5 steps', '<ol><li><b>Knock and ask:</b> "May I come in, Sir?" Wait for permission.</li><li><b>Greet:</b> "Assalam o Alaikum, Sir." Stand straight.</li>'
             '<li><b>Sit when told:</b> only sit after "Have a seat". Thank him.</li><li><b>Answer:</b> short, honest and clear. Say "Sir" politely.</li><li><b>Leave:</b> "Thank you, Sir." Stand, push the chair back, walk out calmly.</li></ol>')
       + sec('📁', 'Documents to carry', 'Checklist', '<ul class="ax-ok"><li>Call letter / roll number slip</li><li>Original CNIC or B-form</li><li>Matric certificate and marks sheet</li><li>FA/FSc certificate or result card</li><li>Domicile</li><li>Passport-size photos</li><li>Black pen and a file</li></ul><p class="ax-sm">Carry originals and 2 photocopies. Check your call letter for the exact list.</p>')
       + sec('👔', 'Dress and body language', '6 tips', '<ul class="ax-ok"><li>Clean, ironed simple shirt</li><li>Polished formal shoes</li><li>Short, clean haircut</li><li>Sit straight, do not lean</li><li>Calm eye contact</li><li>Clear voice, not too fast</li></ul>')
       + sec('📚', 'Topics to prepare', '6 topics', '<ul class="ax-ok"><li><b>About you:</b> intro, family, education, hobbies, strengths</li><li><b>Army & PMA:</b> why Army, ranks, PMA Kakul, Nishan-e-Haider</li>'
             '<li><b>Pakistan:</b> leaders, provinces, capital, key dates</li><li><b>Current affairs:</b> big national news of the last 3 months</li><li><b>Islamiat:</b> basic duties, Kalimas, prayers</li><li><b>Hobbies:</b> know your hobby well; they ask about it</li></ul>')
       + sec('❌', 'Common mistakes', 'Avoid these', '<ul class="ax-no"><li>A memorised speech that sounds like a robot</li><li>Lying about marks or family</li><li>Looking down, no eye contact</li><li>Saying "I don\'t know" without trying</li><li>Talking too long</li><li>Arguing with the officer</li></ul>'
             '<p><b>Instead:</b> be natural, honest and short. If you don\'t know, say "Sorry Sir, I don\'t know, but I will learn."</p>')
       + sec('🗓️', '7-day practice plan', 'One task a day', '<ol><li>Write your self intro</li><li>Practise it aloud 10 times</li><li>Learn the most asked questions</li><li>Current affairs and Pakistan facts</li><li>Mock interview with a friend</li><li>Dress and body language practice</li><li>Rest, check documents, sleep early</li></ol>')
       + sec('⏰', 'Day before and on the day', 'Checklist', '<p><b>🌙 Day before:</b> iron clothes, polish shoes, haircut, pack documents, sleep early.</p><p><b>☀️ On the day:</b> light breakfast, reach early, stay calm, phone silent, smile and be polite.</p>')
       + '<p class="ax-sm">General guidance, not official rules.</p>')

ISSB = ('<div class="ax-hero" style="background:linear-gradient(135deg,#92400e,#f59e0b)"><div class="ax-k">🎖️ ISSB</div><h2>ISSB</h2><p>The 4-day selection board after the interview.</p>'
        '<div class="ax-pass" style="background:#fef3c7;color:#92400e">🔒 Coming soon</div></div><div class="ax-note">I will share my ISSB guide and experience here, In shaa Allah.</div>')

def svg(body):
    return '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + body + '</svg>'
ICO = {
  't': svg('<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9z"/><path d="M8.5 12l2 2 4-4"/><path d="M8.5 17h7"/>'),
  'm': svg('<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/><path d="M6.5 12h3l1.5-2.5 2 5 1.5-2.5h3"/>'),
  'p': svg('<circle cx="14.5" cy="4.5" r="1.8" fill="#fff"/><path d="M8 21l3-6 3 2v5"/><path d="M11 15l1.5-6 3.5 3h3"/><path d="M12.5 9L9 8.5 6.5 11"/>'),
  'i': svg('<path d="M4 5h11a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2H9l-4 3v-3H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"/><path d="M19 9h1a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-1v3l-4-3h-3"/>'),
  's': svg('<path d="M8 2l4 6 4-6"/><circle cx="12" cy="14.5" r="6"/><path d="M12 11.5l1 2 2.2.3-1.6 1.5.4 2.2-2-1.1-2 1.1.4-2.2-1.6-1.5 2.2-.3z" fill="#fff" stroke-width="1"/>'),
}

STAGES = [
    ('t', '📝', 'Initial Test', '03 Nov 2026 • D.I. Khan • 63 questions shared', 'done', '#16a34a', '#22c55e', TEST),
    ('m', '🩺', 'Initial Medical', '03 Nov 2026 • what they checked', 'done', '#0284c7', '#38bdf8', MED),
    ('p', '🏃', 'Initial Physical Test', 'Next • run and exercises', 'next', '#ea580c', '#fb923c', PHY),
    ('i', '🗣️', 'Initial Interview', 'Coming soon • guide inside', 'lock', '#7c3aed', '#a855f7', INT),
    ('s', '🎖️', 'ISSB', 'Later • 4-day guide coming', 'lock', '#b45309', '#f59e0b', ISSB)]
data = {k: {'ic': ICO[k], 't': t, 'd': d, 's': s, 'a': a, 'b': b, 'h': h} for k, ic, t, d, s, a, b, h in STAGES}

import os; tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'adm_tpl.html')).read()
out = tpl.replace('@@DATA@@', json.dumps(data, ensure_ascii=False))
open('/home/user/Asad/pma159/adm_block.html', 'w').write(out)
print(len(out))
