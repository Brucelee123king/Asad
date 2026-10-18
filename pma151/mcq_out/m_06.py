S = "Hakeem Force Academy"
QS = []

def ant(word, right, wrong, pos, reason, rel, ids, q=None):
    opts = list(wrong)
    opts.insert(pos, right)
    QS.append((S, q or "What is the antonym of " + word + "?", opts, pos, reason, rel, ids))

ant("coma", "Consciousness", ["Sleepiness", "Dizziness", "Fatigue"], 0, "A coma is a state of deep unconsciousness, so its opposite is consciousness (being awake and aware).", "The word coma comes from the Greek koma, meaning deep sleep.", [895])
ant("competent", "Incompetent", ["Capable", "Skilful", "Efficient"], 0, "Competent means having the ability to do something well; the opposite is incompetent, meaning lacking ability.", "Competent and capable are synonyms, so they cannot be the antonym.", [463])
ant("contiguous", "Separate", ["Adjacent", "Touching", "Neighbouring"], 0, "Contiguous means sharing a common border or touching; the opposite is separate or detached.", "Pakistan and India are contiguous countries because they share a border.", [896])
ant("despite", "Because of", ["In spite of", "Notwithstanding", "Regardless of"], 0, "Despite means in spite of something; the opposite idea is because of, which gives a cause.", "Despite, in spite of and notwithstanding all mean the same thing.", [3139])
ant("divide", "Unite", ["Separate", "Split", "Partition"], 0, "Divide means to split into parts; the opposite is unite, to join together.", "Unity is one of the three guiding principles of the Quaid-e-Azam: Unity, Faith and Discipline.", [897])
ant("eliminated", "Included", ["Removed", "Excluded", "Discarded"], 0, "Eliminated means removed or left out; the opposite is included or retained.", "Eliminate comes from the Latin eliminare, meaning to drive out of doors.", [3142])
ant("evidently", "Obscurely", ["Clearly", "Plainly", "Obviously"], 0, "Evidently means in a clear and obvious way; the opposite is obscurely, meaning in an unclear way.", "Evidently, obviously and clearly are synonyms of each other.", [3145])
ant("fertile", "Barren", ["Productive", "Fruitful", "Rich"], 0, "Fertile land or a fertile mind produces plenty; the opposite is barren, which produces nothing.", "Sterile is also accepted as an antonym of fertile, so sources may give either word.", [205])
ant("foe", "Friend", ["Enemy", "Rival", "Opponent"], 0, "A foe is an enemy; the opposite is a friend.", "Foe and enemy are synonyms, as are ally and friend.", [3147])
ant("foremost", "Last", ["Leading", "Chief", "Principal"], 1, "Foremost means first in position or importance; the opposite is last (hindmost).", "Foremost, leading and chief are all synonyms.", [468])
ant("friendly", "Hostile", ["Kind", "Cordial", "Amiable"], 2, "Friendly means kind and welcoming; the opposite is hostile, meaning unfriendly or aggressive.", "Hostile comes from the Latin hostis, meaning enemy.", [150])
ant("glory", "Disgrace", ["Honour", "Fame", "Renown"], 1, "Glory means high honour and fame; the opposite is disgrace or shame.", "Glory and honour are synonyms.", [470])
ant("improvement", "Deterioration", ["Progress", "Betterment", "Advancement"], 3, "Improvement means becoming better; the opposite is deterioration, meaning becoming worse.", "Progress and betterment are synonyms of improvement.", [3152])
ant("impudent", "Respectful", ["Insolent", "Cheeky", "Rude"], 0, "Impudent means rude and disrespectful; the opposite is respectful or polite.", "Impudent, insolent and cheeky are synonyms.", [3153])
ant("inaccuracy", "Precision", ["Error", "Mistake", "Fault"], 2, "Inaccuracy means lack of correctness; the opposite is precision or accuracy.", "Error, mistake and fault are synonyms of inaccuracy.", [900])
ant("isolation", "Companionship", ["Seclusion", "Solitude", "Loneliness"], 1, "Isolation means being alone and apart from others; the opposite is companionship or togetherness.", "Isolation, seclusion and solitude are close synonyms.", [901])
ant("mild", "Harsh", ["Gentle", "Soft", "Tender"], 3, "Mild means gentle or not severe; the opposite is harsh, meaning severe or rough.", "Some candidates remembered tamed here, but tamed is not the standard antonym of mild.", [903])
ant("modern", "Ancient", ["Recent", "Latest", "Current"], 0, "Modern means belonging to the present or recent time; the opposite is ancient, meaning belonging to the distant past.", "Old-fashioned is another antonym of modern.", [472])
ant("multitude", "Handful", ["Crowd", "Throng", "Mass"], 2, "A multitude is a very large number of people or things; the opposite is a handful, a very small number.", "Multitude, crowd and throng are synonyms.", [3156])
ant("normally", "Abnormally", ["Usually", "Regularly", "Commonly"], 0, "Normally means in the usual way; the opposite is abnormally, meaning in an unusual way.", "Usually, regularly and commonly are synonyms of normally.", [904])
ant("nourishment", "Starvation", ["Food", "Nutrition", "Sustenance"], 1, "Nourishment is the food needed for life and growth; the opposite is starvation, the lack of food.", "Nutrition and sustenance are synonyms of nourishment.", [3157])
ant("pragmatic", "Idealistic", ["Practical", "Realistic", "Sensible"], 0, "Pragmatic means dealing with things in a practical way; the opposite is idealistic, based on ideals rather than reality.", "Pragmatic, practical and realistic are synonyms.", [3160])
ant("prosperous", "Impoverished", ["Wealthy", "Thriving", "Flourishing"], 3, "Prosperous means rich and successful; the opposite is impoverished, meaning poor.", "Prosperous, wealthy and thriving are synonyms.", [908])
ant("protect", "Endanger", ["Defend", "Guard", "Shield"], 0, "To protect is to keep safe from harm; the opposite is to endanger, to put in harm's way.", "Defend, guard and shield are synonyms of protect.", [206])
ant("purification", "Contamination", ["Cleansing", "Refinement", "Filtration"], 1, "Purification means making something clean; the opposite is contamination, making it impure.", "Pollution is another antonym of purification.", [3164])
ant("recalcitrant", "Obedient", ["Stubborn", "Defiant", "Unruly"], 2, "Recalcitrant means stubbornly resisting authority; the opposite is obedient or compliant.", "Candidates remembered willing or ready, which are also close in meaning to obedient.", [3166])
ant("refuse", "Accept", ["Decline", "Reject", "Deny"], 0, "To refuse is to say no to something offered; the opposite is to accept.", "Refuse as a noun means rubbish, but in this question it is the verb.", [3167])
ant("retrieve", "Lose", ["Recover", "Regain", "Fetch"], 1, "To retrieve is to get something back; the opposite is to lose it.", "Recover and regain are synonyms of retrieve.", [909])
ant("shameful", "Honourable", ["Disgraceful", "Dishonourable", "Scandalous"], 0, "Shameful means causing shame; the opposite is honourable, deserving respect.", "Shameful, disgraceful and scandalous are synonyms.", [3169])
ant("strict", "Lenient", ["Stern", "Rigid", "Severe"], 3, "Strict means demanding obedience to rules; the opposite is lenient, meaning easy-going or merciful.", "Strict, stern and rigid are synonyms.", [3170])
ant("superiority", "Inferiority", ["Supremacy", "Dominance", "Excellence"], 2, "Superiority means being higher in quality or rank; the opposite is inferiority.", "The terms inferiority complex and superiority complex were popularised by the psychologist Alfred Adler.", [100])
ant("underhand", "Honest", ["Secretive", "Sly", "Deceitful"], 0, "Underhand means done in a secret or dishonest way; the opposite is honest or open.", "Aboveboard is the usual one-word opposite of underhand.", [3175])
ant("virtue", "Vice", ["Goodness", "Morality", "Purity"], 1, "Virtue means moral goodness; the opposite is vice, meaning immoral behaviour.", "The pair virtue and vice is a classic antonym pair.", [3177])
ant("timely", "Untimely", ["Prompt", "Punctual", "Opportune"], 0, "Timely means happening at the right moment; the opposite is untimely, happening at the wrong moment.", "Prompt, punctual and opportune are close synonyms of timely.", [911])
ant("apposite", "Irrelevant", ["Relevant", "Suitable", "Apt"], 2, "Apposite means very appropriate or relevant to the matter; the opposite is irrelevant or inapt.", "Apposite, apt and pertinent are synonyms.", [894, 3614],
    q="What is the antonym (opposite) of apposite?")
ant("appropriate", "Inappropriate", ["Suitable", "Fitting", "Proper"], 0, "Appropriate means suitable for the situation; the opposite is inappropriate or unsuitable.", "Suitable, fitting and proper are synonyms of appropriate.", [293])
QS.append((S, "What is the synonym (closest meaning) of appropriate?", ["Unsuitable", "Suitable", "Improper", "Irrelevant"], 1,
 "Appropriate means right for a particular situation, which is the meaning of suitable.", "Fitting and proper are also synonyms of appropriate.", [3256, 3721]))

QS.append((S, "Which Surah of the Holy Quran was revealed immediately after Surah An-Naml (the Ant) in the commonly given order of revelation?",
 ["Surah Al-Qasas", "Surah Ash-Shu'ara", "Surah Al-Ankabut", "Surah Al-Isra"], 0,
 "In the commonly used (Egyptian) order of revelation, Surah An-Naml is the 48th Surah revealed and Surah Al-Qasas follows it.",
 "Sources differ slightly on the exact order of revelation, but both An-Naml and Al-Qasas are Makki Surahs.", [1182]))
QS.append((S, "What is the supreme law (apex law) of Pakistan?",
 ["The Government of India Act 1935", "The Constitution of 1973", "The Objectives Resolution", "The Constitution of 1962"], 1,
 "The Constitution of the Islamic Republic of Pakistan, adopted in 1973, is the supreme law of the country and all other laws must conform to it.",
 "The 1973 Constitution was passed under Prime Minister Zulfikar Ali Bhutto and has 280 Articles.", [3182]))
QS.append((S, "What is the arithmetic mean of 24 and 26?", ["24", "26", "25", "50"], 2,
 "Mean = (24 + 26) / 2 = 50 / 2 = 25.", "The arithmetic mean of two numbers lies exactly halfway between them.", [3187]))
QS.append((S, "What is the arithmetic mean of 24 and 36?", ["28", "32", "60", "30"], 3,
 "Mean = (24 + 36) / 2 = 60 / 2 = 30.", "The arithmetic mean is the sum of the values divided by how many there are.", [3188]))
QS.append((S, "What is the arithmetic mean of 8 and 36?", ["22", "20", "24", "44"], 0,
 "Mean = (8 + 36) / 2 = 44 / 2 = 22.", "The geometric mean of 8 and 36 is different: it is the square root of 288, about 16.97.", [3189]))

DUPS = [(2616, 462), (528, 3186), (271, 6), (271, 4408), (271, 4561), (1190, 207), (1190, 3181),
 (348, 1686), (1902, 2190), (219, 210), (1802, 2226), (182, 1145), (863, 2791), (1039, 4130), (1039, 4131),
 (411, 1122), (1617, 1500), (727, 3459), (727, 161), (727, 3985), (1620, 3578), (702, 2642), (838, 515),
 (2162, 2157), (1712, 1779), (1442, 4713)]
