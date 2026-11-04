import json, html, re
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
                                                 "What is the synonym of Refrain?", "Identify the odd one out: Islamabad, Karachi, Quetta and Lahore.",
                                                 "Who invented the World Wide Web (WWW)?"])]
ADV = ["Practice basic mathematics and percentages.", "Prepare alphabetical series and coding/decoding.", "Practice mirror images and figure patterns.",
       "Revise Pakistan Studies and Islamic Studies.", "Improve your speed and time management."]

e = html.escape

import os as _os
_HERE=_os.path.dirname(_os.path.abspath(__file__))
VQ=json.load(open(_os.path.join(_HERE,'exp_verbal.json'),encoding='utf8'))
NQ=json.load(open(_os.path.join(_HERE,'exp_nonverbal.json'),encoding='utf8'))
def vq_html():
    out=''
    for q in VQ:
        lines=q['q'].split('\n');qt=e(lines[0])
        for x in lines[1:]:
            if re.fullmatch(r'[A-Z_ ]{1,15}',x.strip()) or re.fullmatch(r'[A-Z0-9_ ]{1,15}',x.strip()) and len(x.split())>=3:qt+='<span class="ax-qg">%s</span>'%e(x)
            else:qt+=' '+e(x)
        ops=''.join('<span class="ax-op" data-k="%s"><i>%s</i>%s</span>'%(k,k,e(v)) for k,v in q['opts'].items())
        out+='<div class="ax-q"><b>%d.</b> %s<div class="ax-ops">%s</div><button type="button" class="ax-ab" data-axa="%s">👁 Show answer</button></div>'%(q['n'],qt,ops,q['ans'])
    return out
def nv_html():
    return ''.join('<div class="ax-q ax-nv"><b>%d.</b><img loading="lazy" alt="Non-verbal question %d" data-axi="expimg/nv%02d.webp"><button type="button" class="ax-ab" data-axa="%s" data-nv="1">👁 Show answer</button></div>'%(q['n'],q['n'],q['n'],q['ans']) for q in NQ)
def ol(xs, start=1):
    return '<ol start="%d">' % start + ''.join('<li>%s</li>' % e(x) for x in xs) + '</ol>'
def sec(ic, title, sub, body, op=False):
    return ('<div class="ax-s%s"><button type="button" class="ax-sh"><span class="ax-si">%s</span><span class="ax-st"><b>%s</b><small>%s</small></span><span class="ax-ar">▸</span></button><div class="ax-sb">%s</div></div>'
            % (' open' if op else '', ic, e(title), e(sub), body))

TEST = ('<div class="ax-hero"><div class="ax-k">🪖 PMA 159 LONG COURSE</div><h2>My Complete Test Experience</h2>'
        '<div class="ax-meta"><span>👤 Asadullah</span><span>📍 D.I. Khan</span><span>📅 03 Nov 2026</span><span>⏰ 07:00 – 09:00 AM</span></div>'
        '<div class="ax-pass">✅ Alhamdulillah, PASSED! ❤️🇵🇰</div></div>'
        + sec('🔤', 'Verbal Intelligence', '%d questions with answers' % len(VQ),
              '<p>These are the verbal questions that came in my test. Try each one, then tap Show answer.</p>' + vq_html())
        + sec('🧩', 'Non-Verbal Intelligence', '%d figures with answers' % len(NQ),
              '<p>These are the non-verbal figures that came in my test. Find the missing figure, then tap Show answer.</p>' + nv_html())
        + sec('📚', 'Academic Portion', '30 questions • Easy',
              '<p>Academic portion was comparatively easy and covered Pakistan Studies, Islamic Studies, General Knowledge, History and Current Affairs.</p>'
              + ''.join('<h4>%s</h4>%s' % (e(t), ol(q, st)) for (t, q), st in zip(AC, (1, 5, 20))))
        + sec('💡', 'Overall Experience & Advice', '7 tips',
              '<p>Overall, the test was moderate and manageable. Verbal required quick calculations and logical thinking, while Non-Verbal required concentration and pattern recognition. Academic was mostly based on Pakistan Studies, Islamic Studies, General Knowledge and History.</p>'
              + '<ul class="ax-ok"><li><b>⏰ Time management is the MOST important. Focus on managing your time more than anything else.</b></li><li><b>📱 The whole paper came from this app. Not a single question came from outside. Prepare everything given in this app.</b></li>' + ''.join('<li>%s</li>' % e(a) for a in ADV) + '</ul><p class="ax-end">Best of luck to all PMA 159 candidates!<br>🇵🇰 Pakistan Army Zindabad!</p>'))

MED = ('<div class="ax-hero" style="background:linear-gradient(135deg,#075985,#0284c7)"><div class="ax-k">🩺 INITIAL MEDICAL</div><h2>Initial Medical</h2>'
       '<div class="ax-meta"><span>📅 03 Nov 2026</span><span>📍 D.I. Khan</span></div><div class="ax-pass">✅ Alhamdulillah, PASSED!</div></div>'
       ''
       + sec('🩺', 'What is usually checked', 'General guide',
             '<ul class="ax-ok"><li><b>Eyesight</b>: checked without glasses.</li><li><b>Height</b>: see the Eligibility step in the Roadmap.</li>'
             '<li><b>Weight / BMI</b>: check yours in the BMI tab.</li><li><b>Flat feet</b>: the arch of the foot is checked.</li>'
             '<li><b>Knock knees</b>: stand with feet together; they check if the knees touch.</li><li><b>Chest</b>: chest size and expansion are measured.</li></ul><p class="ax-sm">General guide only; follow the instructions at your centre.</p>', True))

PHY = ('<div class="ax-hero" style="background:linear-gradient(135deg,#9a3412,#ea580c)"><div class="ax-k">🏃 INITIAL PHYSICAL TEST</div><h2>Initial Physical Test</h2>'
       '<div class="ax-pass" style="background:#ffedd5;color:#9a3412">🔒 Coming soon</div></div><div class="ax-note">My physical test has not happened yet. I will share my experience here after it, In shaa Allah.</div>')

INT = ('<div class="ax-hero" style="background:linear-gradient(135deg,#5b21b6,#8b5cf6)"><div class="ax-k">🗣️ INITIAL INTERVIEW</div><h2>Initial Interview</h2>'
       '<div class="ax-pass" style="background:#ede9fe;color:#5b21b6">🔒 Coming soon</div></div><div class="ax-note">My interview has not happened yet. I will share my experience here after it, In shaa Allah.</div>')

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
    ('t', '📝', 'Initial Test', '03 Nov 2026 • D.I. Khan • %d questions shared' % (len(VQ)+len(NQ)+30), 'done', '#16a34a', '#22c55e', TEST),
    ('m', '🩺', 'Initial Medical', '03 Nov 2026 • what they checked', 'done', '#0284c7', '#38bdf8', MED),
    ('p', '🏃', 'Initial Physical Test', 'Coming soon', 'lock', '#ea580c', '#fb923c', PHY),
    ('i', '🗣️', 'Initial Interview', 'Coming soon', 'lock', '#7c3aed', '#a855f7', INT),
    ('s', '🎖️', 'ISSB', 'Later • 4-day guide coming', 'lock', '#b45309', '#f59e0b', ISSB)]
data = {k: {'ic': ICO[k], 't': t, 'd': d, 's': s, 'a': a, 'b': b, 'h': h} for k, ic, t, d, s, a, b, h in STAGES}

import os; tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'adm_tpl.html')).read()
out = tpl.replace('@@DATA@@', json.dumps(data, ensure_ascii=False))
open('/home/user/Asad/pma159/adm_block.html', 'w').write(out)
print(len(out))
