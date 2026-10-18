S = "Hakeem Force Academy"
QS = []
def A(q, opts, ci, reason, fact, ids):
    QS.append((S, q, opts, ci, reason, fact, ids))

A("What does WWW stand for?", ["World Wide Web", "World Web Wire", "Wide World Web", "Web World Wide"], 0,
  "WWW is the abbreviation of World Wide Web, the system of linked pages accessed through the internet.",
  "The World Wide Web was invented by Tim Berners-Lee in 1989.", [1045])
A("In which direction of Pakistan does the Chinese region of Xinjiang lie?", ["South", "North", "West", "East"], 1,
  "Xinjiang lies to the north (north-east) of Pakistan and meets Gilgit-Baltistan at the Khunjerab Pass.",
  "The Karakoram Highway links Pakistan with Xinjiang through the Khunjerab Pass.", [927, 2923])
A("In which Hijri year was the Battle of Yamama fought?", ["9 AH", "10 AH", "11 AH", "13 AH"], 2,
  "The Battle of Yamama was fought against the false prophet Musaylima in 11 AH (632 CE) in the caliphate of Hazrat Abu Bakr (RA).",
  "After heavy losses of Quran memorisers in this battle, the Quran was first compiled in book form.", [2621])
A("By what other name is Hazrat Yaqoob (AS) known?", ["Israel", "Zulkifl", "Idris", "Ayyub"], 0,
  "Yaqoob (AS) is also called Israel, meaning servant of Allah, and his descendants are the Bani Israel.",
  "Hazrat Yusuf (AS) was the son of Hazrat Yaqoob (AS).", [3352, 5495])
A("What was the relation of Hazrat Yaqoob (AS) to Hazrat Ismail (AS)?", ["Nephew", "Son", "Brother", "Grandson"], 0,
  "Yaqoob (AS) was the son of Ishaq (AS), who was the younger brother of Ismail (AS), so Yaqoob was Ismail's nephew.",
  "Both Ishaq and Ismail were sons of Hazrat Ibrahim (AS).", [3920])
A("On which date (day) of Ramadan is Youm-e-Furqan observed?", ["1st Ramadan", "10th Ramadan", "17th Ramadan", "27th Ramadan"], 2,
  "Youm-e-Furqan marks the Battle of Badr, which was fought on 17 Ramadan 2 AH.",
  "Badr is called the day of distinction between truth and falsehood.", [2902])
A("How many Nobel Prizes in Physics has Pakistan won so far?", ["None", "One", "Two", "Three"], 1,
  "Dr Abdus Salam won the Nobel Prize in Physics in 1979, which is Pakistan's only Nobel in Physics.",
  "Malala Yousafzai later won the Nobel Peace Prize in 2014.", [2206])
A("Ali is 4 years old and he is 4 years younger than his sister. When Ali is 8 years old, how old will his sister be?", ["10", "12", "16", "8"], 1,
  "Sister is 4 + 4 = 8 years old now, so she is 4 years older than Ali. When Ali is 8, she will be 8 + 4 = 12.",
  "The age difference between two people always stays the same.", [341])
A("Zabihullah (the one sacrificed for Allah) is the title of which prophet?", ["Hazrat Ishaq (AS)", "Hazrat Ismail (AS)", "Hazrat Yaqoob (AS)", "Hazrat Yusuf (AS)"], 1,
  "Hazrat Ismail (AS) is called Zabihullah because he was offered for sacrifice by his father Ibrahim (AS) in obedience to Allah.",
  "Hazrat Ibrahim (AS) is called Khalilullah and Hazrat Ismail (AS) is the ancestor of the Arab tribes.", [1493, 5498, 466, 191, 5499, 241])
A("Which is the oldest of these heavenly books?", ["Quran", "Injeel", "Taurat", "Zabur"], 2,
  "The Taurat was revealed to Hazrat Musa (AS), before the Zabur (Dawood AS), the Injeel (Isa AS) and the Quran (Muhammad PBUH).",
  "The Quran is the last of the heavenly books.", [4672])
A("What is the well-known title of Hazrat Zaid bin Haritha (RA)?", ["Hibb Rasulullah (beloved of the Prophet)", "Siddiq", "Zun-Noorain", "Saifullah"], 0,
  "Hazrat Zaid (RA) was so dear to the Holy Prophet (PBUH) that he was called Hibb Rasulullah.",
  "He is the only Companion whose name is mentioned in the Quran (Surah Al-Ahzab).", [4004])
A("Who is the Prime Minister of New Zealand (as of October 2026)?", ["Chris Hipkins", "Jacinda Ardern", "Christopher Luxon", "Bill English"], 2,
  "Christopher Luxon of the National Party has been Prime Minister since November 2023 and is still in office in October 2026.",
  "Jacinda Ardern (until January 2023) and Chris Hipkins (until November 2023) held the post earlier; the next election is on 7 November 2026.", [455, 99])
A("What is the meaning of the word 'zenith' (also its synonym)?", ["Peak or highest point", "Lowest point", "Middle part", "Edge"], 0,
  "Zenith means the highest point, peak or summit of something.",
  "In astronomy the zenith is the point in the sky directly above the observer.", [3789, 1554])
A("What is the antonym of 'zenith'?", ["Nadir", "Summit", "Apex", "Peak"], 0,
  "Zenith means the highest point, so its opposite is nadir, the lowest point.",
  "Apex, summit and peak are synonyms of zenith.", [3468])
A("What is the value of any non-zero number raised to the power zero?", ["0", "1", "The number itself", "Undefined"], 1,
  "By the law of exponents a^0 = a^n / a^n = 1 for any non-zero number a.",
  "The expression 0 to the power 0 is treated as undefined or indeterminate in basic algebra.", [887, 1064])
A("Which Indian mathematician is credited with formalising the rules of arithmetic with zero in 628 CE?", ["Brahmagupta", "Euclid", "Al-Khwarizmi", "Pythagoras"], 0,
  "Brahmagupta, in his Brahmasphutasiddhanta, gave the first clear rules for using zero in calculations.",
  "Sources differ on who first invented the zero symbol; some credit Aryabhata and earlier Indian scholars.", [5076])
A("3x - 5x + 2 is an example of what?", ["Algebraic expression", "Equation", "Identity", "Inequality"], 0,
  "It has variables and constants joined by operations but no equals or inequality sign, so it is an algebraic expression (it simplifies to -2x + 2).",
  "An equation needs an equals sign, such as 3x - 5x + 2 = 0.", [1602])
A("If A = 3 and B = 4, what is A x B?", ["7", "1", "12", "34"], 2,
  "A x B = 3 x 4 = 12.", "Multiplication is commutative, so A x B equals B x A.", [2370])
A("If A = {1, 2, 3, 4} and B = {1, 5, 2, 4}, what is A - B?", ["{3}", "{5}", "{1, 2, 4}", "{3, 5}"], 0,
  "A - B contains the elements of A that are not in B. Only 3 is in A but not in B.",
  "B - A would be {5}.", [2372])
A("If x = 9y and y = 1/3, what is x?", ["3", "9", "1/3", "27"], 0,
  "x = 9 x 1/3 = 3.", "Substitute the given value first, then multiply.", [2446])
A("If x = 9y + 1 and y = 1/3, what is x?", ["3", "4", "10", "9"], 1,
  "x = 9 x 1/3 + 1 = 3 + 1 = 4.", "Always do multiplication before addition.", [891])
A("If Y = 4X and X = 2, what is Y?", ["6", "8", "2", "16"], 1,
  "Y = 4 x 2 = 8.", "Here 4 is the coefficient of X.", [2451])
A("In the expression 7X + 4, what is 7 called?", ["Coefficient", "Constant", "Variable", "Exponent"], 0,
  "The number multiplying the variable X is its coefficient; 4 is the constant term.",
  "X is the variable of the expression.", [2460])
A("What is (3 + 2i)(2i - 3)?", ["-13", "13", "-5", "-9 + 4i"], 0,
  "Expand: 3(2i) - 9 + 4i^2 - 6i = 6i - 9 - 4 - 6i = -13, since i^2 = -1.",
  "(a + b)(b - a) = b^2 - a^2, giving (2i)^2 - 3^2 = -4 - 9 = -13.", [3264])
A("What is -10 - 10?", ["0", "-20", "20", "-100"], 1,
  "Subtracting 10 from -10 moves further down the number line to -20.", "Two negative numbers added give a larger negative number.", [3265])
A("What is 1/10 of 90?", ["3", "9", "30", "10"], 1,
  "90 divided by 10 = 9.", "One tenth of a number is the same as 10 percent of it.", [564])
A("What is 1/3 of 10% of 90?", ["3", "9", "30", "27"], 0,
  "10% of 90 = 9, and 1/3 of 9 = 3.", "The order of taking the fraction and percentage does not change the result.", [103])
A("What is 1/3 of 10% of 99?", ["3.3", "33", "9.9", "0.33"], 0,
  "10% of 99 = 9.9, and 1/3 of 9.9 = 3.3.", "99 is divisible by 3, so 1/3 of 99 = 33.", [3271])
A("What is 1/3 of 90?", ["3", "9", "30", "270"], 2,
  "90 divided by 3 = 30.", "A third of 90 is ten times a third of 9.", [67])
A("What is 2 + 3/3?", ["3", "2", "5/3", "1"], 0,
  "Division comes first: 3/3 = 1, then 2 + 1 = 3.", "BODMAS gives division priority over addition.", [715])
A("What is 2/2 + 1?", ["1", "2", "3", "1.5"], 1,
  "2/2 = 1 and 1 + 1 = 2.", "Any non-zero number divided by itself is 1.", [3282])
A("What is 2/3 of 30?", ["10", "15", "20", "25"], 2,
  "1/3 of 30 = 10, so 2/3 of 30 = 20.", "2/3 of 30 plus 1/3 of 30 gives the whole 30.", [3283])
A("What is 20% of 50?", ["5", "10", "20", "25"], 1,
  "20% of 50 = 20/100 x 50 = 10.", "20% equals one fifth.", [3284])
A("What is 25% of 75?", ["18.75", "20", "15", "25"], 0,
  "25% is one quarter: 75 / 4 = 18.75.", "25% of 80 is 20.", [1052])
A("What is 25% of 80?", ["15", "25", "20", "40"], 2,
  "25% is one quarter: 80 / 4 = 20.", "25% equals 1/4.", [1053])
A("What is 2x + 3x + 1?", ["5x + 1", "6x", "5x", "6x + 1"], 0,
  "Add the like terms: 2x + 3x = 5x, so the result is 5x + 1.", "Only like terms can be combined.", [3288])
A("What is 2 x 3 - 2 x 2?", ["2", "6", "10", "0"], 0,
  "Multiply first: 6 - 4 = 2.", "This equals 2(3 - 2) = 2.", [3291])
A("What is 4x - 1 if x = 2?", ["6", "9", "7", "8"], 2,
  "4 x 2 - 1 = 8 - 1 = 7.", "Substitute first, then multiply, then subtract.", [3297])
A("What is 54% of 90?", ["48.6", "54", "50.4", "46.8"], 0,
  "54/100 x 90 = 48.6.", "50% of 90 is 45.", [3301])
A("What is 60% of 70?", ["36", "42", "40", "46"], 1,
  "60/100 x 70 = 42.", "10% of 70 is 7, so 60% is 6 x 7.", [3303])
A("What is 70% of 80?", ["54", "58", "56", "60"], 2,
  "70/100 x 80 = 56.", "70% of 80 equals 80% of 70.", [1055])
A("What is 80% of 10?", ["8", "80", "2", "0.8"], 0,
  "80/100 x 10 = 8.", "10% of 10 is 1.", [3305])
A("What is 80% of 40?", ["30", "34", "36", "32"], 3,
  "80/100 x 40 = 32.", "80% equals 4/5.", [3306])
A("What is 80% of 75?", ["60", "55", "65", "50"], 0,
  "80/100 x 75 = 60.", "80% equals 4/5 and 75 x 4 / 5 = 60.", [3307])
A("What is 80% of 90?", ["70", "72", "74", "81"], 1,
  "80/100 x 90 = 72.", "10% of 90 is 9, so 80% is 8 x 9.", [269])
A("What is 9% of 9?", ["0.81", "8.1", "0.9", "81"], 0,
  "9/100 x 9 = 81/100 = 0.81.", "1% of 9 is 0.09.", [3308])

DUPS = [(937, 2168), (1391, 4436), (1063, 5497), (1538, 4053), (1204, 3255),
        (1493, 5269), (1493, 5270), (327, 1243), (73, 4989), (821, 5202),
        (89, 1027), (756, 3088), (756, 3109), (875, 5009), (875, 5222),
        (906, 4055), (417, 5501), (417, 5502), (417, 5205), (417, 5505),
        (417, 467), (417, 5206), (23, 54), (1656, 87), (3, 1), (737, 396)]
