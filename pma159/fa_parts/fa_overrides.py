"""Corrections found by the independent blind check and the web fact-check.
Labels match the start of each question text."""
A = "(Forces Academy Academic · "
REMOVE = [
    "(Forces Academy Test 4 · Q7)",    # Date/Calendar/Year/Day/Minute: calendar vs minute, no single defensible odd one
    "(Forces Academy Test 7 · Q5)",    # sports odd-one-out: key (badminton) and logic (football) disagree
    "(Forces Academy Test 13 · Q18)",  # K LL MMM NNN? : question is garbled
    "(Forces Academy Test 14 · Q5)",   # paired series with no clear rule
    "(Forces Academy Test 14 · Q20)",  # all four are units of weight; no clean odd one
    A + "Line 106)",                   # '25th Prime Minister': numbering differs by source
    A + "Exam World 52)",              # Musharraf Chief Executive period: chart and Wikipedia disagree
    A + "Line 61)",                    # Quaid in Congress 1904-1920: start year disputed (1904 vs 1906)
]
# label -> dict of changes: correct (index), reason, rel, append_reason
FIX = {
    "(Forces Academy Test 1 · Q19)": {
        "correct": 0,
        "reason": "Easy and light both mean not hard or heavy to deal with, and rough is closest to hard (a rough surface feels hard and coarse). The paper's answer key gives Hard.",
    },
    "(Forces Academy Test 3 · Q20)": {
        "correct": 1,
        "reason": "The differences are 10, 8, 6, 4, so the next difference is 2: 6 - 2 = 4.",
    },
    "(Forces Academy Test 12 · Q18)": {
        "append_reason": " Another reading of the gaps (2, 3, 5, 8) would give T, but the paper's answer key is U.",
    },
    "(Forces Academy Test 13 · Q21)": {
        "append_reason": " Another reading of the gaps (2, 3, 5, 8) would give T, but the paper's answer key is U.",
    },
    A + "Sheet Q8)": {"rel": "Nishan-e-Haider was instituted in 1957 (applied from 1947) and was first awarded, after death, to Captain Raja Muhammad Sarwar Shaheed for his action in July 1948."},
    A + "Sheet Q10)": {"rel": "Saudi Arabia is the largest exporter of crude oil, while the United States is now the largest oil producer, followed by Russia and Saudi Arabia."},
    A + "Sheet Q14)": {"rel": "Sher Shah Suri (1540-45) rebuilt and extended the old highway from Sonargaon in Bengal towards the north-west; the name Grand Trunk Road came in the British period."},
    A + "Sheet Q16)": {"rel": "Zaid bin Haritha was freed and adopted by the Prophet before prophethood, and he is the only companion named in the Quran (Surah Al-Ahzab, 33:37)."},
    A + "Sheet Q23)": {"rel": "Hummingbirds are the only birds able to sustain backward flight."},
    A + "Sheet Q27)": {"rel": "Khairpur acceded at about the same time (early October 1947). Junagadh's ruler announced accession in September 1947, but India took over the state in November 1947. Kalat joined in March 1948."},
    A + "Sheet Q31)": {"rel": "Jamil Dehlavi directed the film Jinnah (1998), and Akbar S. Ahmed co-wrote the screenplay."},
    A + "Sheet Q35)": {
        "reason": "Mussolini founded the Fascist movement in Italy in 1919 (Fasci Italiani di Combattimento) and became Prime Minister in 1922.",
        "rel": "The Fascist movement became the National Fascist Party in 1921; Hitler later led the Nazi Party, a German variant of fascism.",
    },
    A + "Sheet Q36)": {"rel": "Sources differ: some date the start of the Russian Civil War from the Bolshevik takeover in November 1917, others (such as Britannica) from 1918; it ended around 1922."},
    A + "Sheet Q39)": {"rel": "The 49th parallel forms the western and central part of the Canada-US border; the Durand Line is the Pakistan-Afghanistan border."},
    A + "Sheet Q40)": {
        "reason": "In the Rann of Kutch dispute Pakistan claimed that the boundary ran along the 24th parallel line, so this is the line linked with the Rann boundary.",
        "rel": "A tribunal in 1968 largely rejected Pakistan's claim to half of the Rann; the Sir Creek boundary at its western end is still disputed.",
    },
    A + "Exam World 9)": {"rel": "Jinnah, together with Tilak, was the main architect of the Lucknow Pact."},
    A + "Exam World 31)": {"reason": "The war began in October 1947 and the UN-brokered ceasefire took effect on 1 January 1949; it is usually called the 1947-48 war."},
    A + "Exam World 42)": {"rel": "Junejo took office as Prime Minister in March 1985 after the party-less elections and was dismissed by Zia in May 1988."},
    A + "Exam World 46)": {"rel": "In 1997 the PML-N won a heavy majority (about 137 of 217 seats) and, with its allies, a two-thirds majority."},
    A + "Line 11)": {"rel": "Sir Syed was made a Companion of the Star of India (CSI) in 1869 and knighted (KCSI) in 1888."},
    A + "Line 20)": {"rel": "Pakistan's first TV station opened in Lahore on 26 November 1964, and colour transmission began on 25 December 1976."},
    A + "Line 56)": {"rel": "Umar bin Abdul Aziz (reigned 717-720) is popularly called the fifth Rightly Guided Caliph, though this is an honorary title."},
    A + "Line 57)": {"rel": "China's army (PLA) has about 2 million active troops, and India's army has about 1.45 million."},
    A + "Line 75)": {"rel": "The President is the constitutional Supreme Commander of the armed forces; the 27th Amendment (November 2025) created the post of Chief of Defence Forces."},
    A + "Line 79)": {"rel": "Direct Crown rule began in 1858; counting from the war of 1857 to independence in 1947 gives about 90 years."},
    A + "Line 81)": {"rel": "Pakistan and Yemen were admitted to the United Nations together on 30 September 1947; the UN itself was founded on 24 October 1945."},
    A + "Line 82)": {"reason": "Iqbal received his PhD from the University of Munich in Germany (his thesis was completed around 1907-08)."},
    A + "Line 101)": {"reason": "Khawaja Muhammad Asif is the Defence Minister (again since March 2024; he also held the post in 2013-2017 and 2022-2023)."},
    A + "Line 104)": {"reason": "Jameel Ahmad has been Governor of the State Bank of Pakistan since August 2022."},
    A + "Line 113)": {"reason": "Australia is the smallest of the seven continents, with an area of about 7.7 million sq km."},
}
