H = "Hakeem Force Academy"
def syn(w, ans, wrong, ids, rel):
    opts = [ans] + wrong
    return (H, f"Which word is closest in meaning (synonym) to '{w}'?", opts, 0,
            f"'{w.capitalize()}' means almost the same as '{ans}'.", rel, ids)
QS = [
 (H, "What comes next in the series: X1, YY3, ZZZ5, ?", ["AAAA7", "BBBB7", "AAA7", "AAAA6"], 0,
  "The letters go X, Y, Z, A in order and each letter is repeated one more time (1, 2, 3, 4 times). The numbers go up by 2: 1, 3, 5, 7, so the next term is AAAA7.",
  "After Z the alphabet starts again from A in such series.", [995]),
 (H, "What comes next in the series: Z1, X3, U6, Q10, L15, ?", ["G20", "F21", "E21", "F20"], 1,
  "Letters move back by 2, 3, 4, 5 and then 6 places: Z, X, U, Q, L, F. Numbers go up by 2, 3, 4, 5, 6: 1, 3, 6, 10, 15, 21, so the next term is F21.",
  "The numbers 1, 3, 6, 10, 15, 21 are called triangular numbers.", [1188]),
 (H, "What is the common short form (abbreviation) of Saudi Arabia?", ["UAE", "KSA", "SAR", "SDA"], 1,
  "Saudi Arabia is officially the Kingdom of Saudi Arabia, so its short form is KSA.",
  "SAR is the code for the Saudi riyal, the currency of Saudi Arabia.", [259]),
 (H, "How many sides does a pentagon have?", ["Six", "Four", "Five", "Eight"], 2,
  "The word pentagon comes from the Greek penta meaning five, so it has five sides.",
  "The sum of the interior angles of a pentagon is 540 degrees.", [577]),
 (H, "Between which two countries was the Tashkent Agreement signed in January 1966?", ["Pakistan and Afghanistan", "India and China", "Pakistan and India", "Pakistan and Iran"], 2,
  "The Tashkent Agreement ended the 1965 war between Pakistan and India, with the Soviet Union mediating.",
  "It was signed by Ayub Khan and Lal Bahadur Shastri, who died in Tashkent soon afterwards.", [459]),
 (H, "What is the value of cosec x multiplied by sin x?", ["0", "1", "tan x", "cos x"], 1,
  "Cosec x is 1 divided by sin x, so cosec x times sin x equals 1 over sin x times sin x, which is 1.",
  "Similarly sec x times cos x is 1 and cot x times tan x is 1.", [241]),
 (H, "What is the value of sin 0 degrees?", ["1", "0", "0.5", "Undefined"], 1,
  "On the unit circle the angle 0 degrees points along the x-axis, where the y-coordinate (sine) is 0.",
  "The value of cos 0 degrees is 1.", [907]),
 (H, "Ali is 6 years old and his sister is twice his age. How old is the sister?", ["8 years", "10 years", "14 years", "12 years"], 3,
  "Sister's age = 2 x 6 = 12 years.",
  "The age difference between them is 6 years and it never changes.", [442]),
 (H, "Which place in Pakistan is famous for making small arms (weapons) in home industry?", ["Darra Adam Khel", "Sialkot", "Gujranwala", "Wah Cantt"], 0,
  "Darra Adam Khel, south of Peshawar in Khyber Pakhtunkhwa, is well known for its local small arms workshops.",
  "Sialkot is instead famous for sports goods and surgical instruments.", [1126, 1289]),
 (H, "What part of speech is the word 'between'?", ["Preposition", "Noun", "Adverb only", "Conjunction"], 0,
  "'Between' shows the relation of a noun or pronoun to another word, as in 'between the two houses', so it is a preposition.",
  "'Among' is used for more than two things, while 'between' is normally used for two.", [178]),
 (H, "Which game is the national sport of Pakistan?", ["Cricket", "Kabaddi", "Squash", "Hockey"], 3,
  "Field hockey is officially recognised as the national sport of Pakistan.",
  "Cricket is the most popular sport in Pakistan, but it is not the official national sport.", [994]),
 (H, "Which country is generally credited with starting modern football (soccer)?", ["Brazil", "Germany", "England", "Italy"], 2,
  "Modern football rules were first written down in England in 1863 when the Football Association was formed.",
  "Sources differ because older ball games existed in China, but textbooks give England as the home of modern football.", [1215]),
 (H, "Which British commander defeated Tipu Sultan in the Third Anglo-Mysore War (1790-92)?", ["Lord Cornwallis", "Robert Clive", "Lord Dalhousie", "Warren Hastings"], 0,
  "Lord Cornwallis led the British forces and Tipu had to sign the Treaty of Seringapatam in 1792.",
  "Tipu Sultan was finally killed in 1799 in the Fourth Anglo-Mysore War, when Lord Wellesley was Governor-General.", [166, 1320]),
 syn("embellish", "adorn", ["spoil", "hide", "reduce"], [871], "Its opposite is a word such as 'disfigure'."),
 syn("specify", "state clearly", ["ignore", "confuse", "cancel"], [874], "The noun form is 'specification'."),
 syn("weird", "strange", ["ordinary", "pleasant", "famous"], [876], "Its opposite is 'normal'."),
 syn("affection", "fondness", ["hatred", "anger", "fear"], [261], "Its opposite is 'dislike' or 'hatred'."),
 syn("contemporary", "modern", ["ancient", "old-fashioned", "rare"], [1024], "It can also mean living or existing at the same time."),
 syn("dearth", "scarcity", ["abundance", "luxury", "surplus"], [1025], "Its opposite is 'abundance'."),
 syn("absolute", "complete", ["partial", "doubtful", "weak"], [1026], "An absolute monarch has complete power."),
 syn("spontaneous", "impulsive", ["planned", "forced", "careful"], [1028], "Its opposite is 'planned' or 'deliberate'."),
 syn("supervision", "oversight", ["neglect", "freedom", "defeat"], [1029], "The person who supervises is called a supervisor."),
]
# fix correct index variety
import random as _r
_new = []
for i, (s, q, o, a, w, r, ids) in enumerate(QS):
    if q.startswith("Which word is closest"):
        k = i % len(o); o = o[:]; o[0], o[k] = o[k], o[0]; a = k
    _new.append((s, q, o, a, w, r, ids))
QS = _new
DUPS = [(979,1193),(2828,633),(5150,467),(185,315),(903,1133),(751,40),(751,265),(4805,65),(3902,1049),(3902,390),
(1567,176),(279,430),(1208,686),(2773,1300),(4014,1089),(868,566),(868,822),(1632,352),(1632,700),(1632,277),(1632,1117),
(4731,260),(1614,433),(3338,747),(815,1392),(815,1426),(5011,167),(5011,1324),(5011,312),(3281,1205),(3281,1330),(3017,653),
(5633,305),(4005,237),(4297,43),(1155,238),(5644,872),(1156,873),(4896,875),(2205,239),(4212,262),(1153,121),(1082,1027),(1166,1030)]
