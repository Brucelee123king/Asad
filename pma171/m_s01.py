MATCH = [
    (1, 129),
    (2, 416),
    (5, 386),
    (9, 546),
    (12, 203),
    (13, 109),
    (14, 154),
    (17, 397),
    (20, 53),
]

NEW = [
    (3, "Pakistan Studies", "On which date was the Objectives Resolution passed by the Constituent Assembly of Pakistan?", "12 March 1949", ["7 March 1949", "23 March 1956", "14 August 1948"],
     "Liaquat Ali Khan moved the Objectives Resolution on 7 March 1949 and the Constituent Assembly passed it on 12 March 1949. 7 March is only the day it was presented. 23 March 1956 is when the first constitution came into force, and 14 August 1948 is the first Independence Day.", 0),
    (7, "Verbal: English", "Choose the synonym of INCESSANT.", "Ceaseless", ["Occasional", "Intermittent", "Brief"],
     "Incessant means continuing without stopping, so ceaseless (never stopping) is the synonym. Occasional, intermittent and brief all describe things that stop or happen only now and then, so they are opposite in meaning.", 0),
    (8, "Pakistan Studies", "In which district of Balochistan did Pakistan conduct its nuclear tests on 28 May 1998?", "Chagai", ["Kharan", "Gwadar", "Turbat (Kech)"],
     "The five tests of 28 May 1998 (Chagai-I) were done in the Ras Koh Hills of Chagai District, Balochistan. Kharan was the site of the single follow-up test on 30 May, and Gwadar and Turbat were not test sites.", 0),
    (10, "Pakistan Studies", "On which date did Fatima Jinnah (Madar-e-Millat) die?", "9 July 1967", ["11 September 1967", "9 July 1965", "11 September 1948"],
     "Fatima Jinnah died in Karachi on 9 July 1967 and is buried next to the Quaid at Mazar-e-Quaid. 11 September 1948 is the death date of Quaid-e-Azam, and the other dates are wrong mixes of these days and years.", 0),
    (11, "Pakistan Studies", "Who led the Aligarh Movement?", "Sir Syed Ahmad Khan", ["Allama Muhammad Iqbal", "Maulana Muhammad Ali Jauhar", "Nawab Salimullah Khan"],
     "Sir Syed Ahmad Khan started the Aligarh Movement after 1857 to bring modern education to Muslims, and founded the MAO College at Aligarh. Iqbal was a poet-philosopher, Jauhar led the Khilafat Movement, and Salimullah Khan hosted the founding of the Muslim League in 1906.", 0),
    (15, "Islamiat", "In which year of Prophethood (Nabuwwat) did the Holy Prophet (PBUH) migrate from Makkah to Madinah?", "13th year", ["10th year", "11th year", "15th year"],
     "The Hijrah took place in 622 CE, which was the 13th year after the first revelation. The 10th year was the Year of Grief (Aam-ul-Huzn), the 11th year saw the first meeting with people of Yathrib, and by the 15th year the Prophet (PBUH) was already in Madinah.", 0),
    (16, "General Knowledge", "What is the capital of Belgium?", "Brussels", ["Antwerp", "Amsterdam", "Geneva"],
     "Brussels has been the capital of Belgium since 1830 and is also the main seat of the European Union. Antwerp is a large Belgian port city but not the capital, Amsterdam is the capital of the Netherlands, and Geneva is a city in Switzerland.", 0),
    (18, "Verbal: English", "Fill in the blank with the correct preposition: The fridge is ___ the kitchen.", "in", ["on", "at", "into"],
     "We use 'in' for something inside a room or enclosed space, so the fridge is in the kitchen. 'On' is for surfaces, 'at' is for a point or place, and 'into' shows movement, so they do not fit here.", 0),
]

SKIPPED = {
    4: "Number of manasik (rites) of Hajj is not fixed; books count them differently (fard, wajib, sunnah lists vary), so no indisputable answer.",
    6: "Sources disagree on how many physical regions Pakistan has (3, 4, 6 or 7 depending on the book), so the answer is disputed.",
    19: "Unclear question (football, cricket, hockey - which is different); options and intended answer unknown. Existing index 277 (odd one out Cricket, Football, Hockey, Chess = Chess) may be the same question.",
}
