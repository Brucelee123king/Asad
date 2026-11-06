MATCH = [
    (79, 268), (81, 144), (82, 292), (84, 198), (85, 52), (88, 191),
]
NEW = [
    (80, "Islamiat", "Kaleemullah (Kalimullah), meaning the one who spoke with Allah, is the title of which Prophet?", "Hazrat Musa (A.S.)",
     ["Hazrat Ibrahim (A.S.)", "Hazrat Isa (A.S.)", "Hazrat Nuh (A.S.)"],
     "Hazrat Musa (A.S.) is called Kalimullah because Allah spoke to him directly (Quran 4:164, 7:144).", 0),
    (83, "Pakistan Studies", "Who was the first Commander-in-Chief of the Pakistan Army after independence in 1947?", "General Sir Frank Messervy",
     ["General Sir Douglas Gracey", "General Muhammad Ayub Khan", "General Sir Claude Auchinleck"],
     "Frank Messervy, a British officer, was the first C-in-C from 15 August 1947 to February 1948. Douglas Gracey succeeded him and Ayub Khan was the first Pakistani C-in-C in 1951.", 0),
    (86, "Verbal: English", "The word Mantaq (Urdu) means:", "Logic",
     ["Grammar", "Poetry", "Philosophy of religion"],
     "Mantaq is the Arabic and Urdu word for logic, the science of correct reasoning.", 0),
    (87, "Pakistan Studies", "Harappa, in Punjab, Pakistan, is the type site of which ancient civilization?", "Indus Valley Civilization (Bronze Age)",
     ["Mesopotamian Civilization", "Egyptian Civilization", "Gandhara Civilization"],
     "Harappa gave its name to the Harappan or Indus Valley Civilization, a Bronze Age civilization, first excavated from 1920-21.", 0),
    (89, "Islamiat", "The tribes of Aus and Khazraj, who became the Ansar, lived in which city?", "Madina (Yathrib)",
     ["Makkah", "Taif", "Khaybar"],
     "Aus and Khazraj were the two main Arab tribes of Yathrib, later called Madina. They became the Ansar (helpers) after the Hijrah.", 0),
    (91, "Maths & Science", "What is the formula for the circumference of a circle with radius r?", "2 pi r",
     ["pi r squared", "pi d squared", "4 pi r"],
     "Circumference = 2 x pi x r = pi x diameter. Pi r squared is the area.", 0),
]
SKIPPED = {
    77: "ambiguous: Makki surah count is 86 in common lists but 85 or 90 in others",
    78: "topic-only: no clear word or options given",
    90: "ambiguous: question unclear (year of Hijrat or 13th year of Nabuwat); existing 441 asks 622 AD",
}
