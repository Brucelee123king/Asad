# -*- coding: utf-8 -*-
QS = []


def add(t, n, q, opts, ci, reason, fact):
    QS.append(("Forces Academy Intelligence Test %d" % t,
               "(Forces Academy Test %d · Q%d) %s" % (t, n, q),
               opts, ci, reason, fact))


# ---------------------------------------------------------------- TEST 7
T = 7
add(T, 1, "Which letter comes next in the following series: C, F, J, M, Q, ?",
    ["S", "U", "T", "R"], 2,
    "The gaps alternate +3, +4: C to F is 3, F to J is 4, J to M is 3, M to Q is 4. Next gap is +3, so Q + 3 = T.",
    "Tip: when letter gaps repeat in a pattern, write each letter as a number (A=1) and look at the differences.")
add(T, 2, "Which number comes next: 51, 41, 33, 27, ?",
    ["21", "22", "23", "25"], 2,
    "Differences are -10, -8, -6, so the next difference is -4: 27 - 4 = 23.",
    "Tip: when the differences themselves change by a constant amount, the series is a second-order pattern.")
add(T, 3, "Two traders earned a profit of Rs.160. One got 70%. How many rupees did the other get?",
    ["Rs.112", "Rs.52", "Rs.48", "Rs.30"], 2,
    "The other trader gets 100% - 70% = 30% of 160, which is 0.30 x 160 = 48.",
    "Tip: when shares of a total are given in percent, the remaining share is simply 100 minus the known percent.")
add(T, 4, "NORTH is to 51398 as THORN is to:",
    ["98531", "89135", "98135", "98315"], 2,
    "N=5, O=1, R=3, T=9, H=8. THORN is T,H,O,R,N = 9,8,1,3,5 = 98135.",
    "Tip: in coding questions, first write down the letter-to-digit table from the given word, then re-read it for the new word.")
add(T, 5, "What is different from the others?",
    ["CRICKET", "TENNIS", "SQUASH", "BADMITON", "FOOTBALL"], 4,
    "Cricket, tennis, squash and badminton are all played with a bat or racket, while football is played with the feet and no bat or racket.",
    "Tip: for odd-one-out questions, look for the shared feature of the majority (equipment, category, place) and find who lacks it.")
add(T, 6, "LOST means the opposite of:",
    ["WIN", "DOWN", "FOUND", "MAT", "HIGH"], 2,
    "The opposite of lost (misplaced) is found.",
    "Tip: check the part of speech first, because the opposite of a word in a sentence must fit the same sense.")
add(T, 7, "Sky is to Earth as Ceiling is to:",
    ["ROOF", "DOWN", "FLOOR", "MAT", "HIGH"], 2,
    "The sky is above the earth; a ceiling is above the floor, so the pairing matches.",
    "Tip: in analogies, state the relationship in a sentence first (above / below, part / whole) and then apply it.")
add(T, 8, "Which letter comes next in the following series: D, G, J, M, P, ?",
    ["R", "T", "Q", "S"], 3,
    "Each letter moves forward by 3: D, G, J, M, P, then P + 3 = S.",
    "Tip: a constant gap between letters means a simple arithmetic pattern; count the skipped letters carefully.")
add(T, 9, "Which number comes next: 43, 33, 38, 30, 34, ?",
    ["26", "28", "31", "29"], 1,
    "The changes alternate and shrink: -10, +5, -8, +4, then -6. So 34 - 6 = 28.",
    "Tip: if the numbers zigzag, look at the differences between neighbours; they may form two separate patterns.")
add(T, 10, "A trader invested Rs.2490 in a business but he had a loss of 100/3 percent. What was he left with after the loss?",
    ["Rs.830", "Rs.1660", "Rs.2407", "Rs.1900"], 1,
    "100/3 percent is one third. A third of 2490 is 830, so he was left with 2490 - 830 = 1660.",
    "Tip: 33 and one third percent is the same as the fraction one third, which makes mental maths easy.")
add(T, 11, "Iqbal, Asif and Mahmood are standing in a row. Iqbal is standing in front of Mahmood. Asif is standing behind Iqbal. Mahmood is standing in front of Asif. Who is standing in the middle?",
    ["IQBAL", "ASIF", "MAHMOOD"], 2,
    "The order from the front is Iqbal, then Mahmood, then Asif, so Mahmood is in the middle.",
    "Tip: draw a quick line of positions and place each person as the clues are read.")
add(T, 12, "Teachers are respected because:",
    ["They look after their families well", "They earn clean money", "They educate children", "They read books"], 2,
    "Teachers are respected mainly for their service of educating children and shaping society.",
    "Tip: in reasoning questions choose the cause most directly linked to the role itself.")
add(T, 13, "Which letter comes next in the following series: D, H, M, P, U, ?",
    ["Z", "X", "W", "V"], 2,
    "Split the series into two: D, M, U (gaps +9, +8) and H, P, then W (gaps +8, +7). The next letter is W.",
    "Tip: in alternating letter series, separate the odd and even positions into two sequences.")
add(T, 14, "A meal always involves:",
    ["TABLE", "DISHES", "HUNGER", "FOOD", "WATER"], 3,
    "A meal by definition consists of food; the other items may or may not be present.",
    "Tip: choose the item that is essential, not just commonly present.")
add(T, 15, "Three shareholders earned a profit of Rs.900 in their business. One got 20% of the profit, the other got 45% of the profit. How many rupees were the share of the third?",
    ["Rs.180", "Rs.405", "Rs.315", "Rs.585"], 2,
    "The third gets 100 - 20 - 45 = 35 percent, and 35 percent of 900 is 315.",
    "Tip: subtract the given percentages from 100 first, then take the remaining percent of the total.")
add(T, 16, "OCTOBER is to NOVEMBER as SUNDAY is to:",
    ["FRIDAY", "SATURDAY", "MONDAY", "TUESDAY", "WEDNESDAY"], 2,
    "November is the month that follows October, and Monday is the day that follows Sunday.",
    "Tip: time-sequence analogies usually ask for the next item in the cycle.")
add(T, 17, "SICK means the same as:",
    ["HEALTHY", "FEVER", "DIRTY", "COUGH", "ILL"], 4,
    "Sick and ill are synonyms.",
    "Tip: a symptom such as fever or cough is not a synonym; look for a word that can replace the original in any sentence.")
add(T, 18, "Which letter comes next in the following series: A, E, I, M, Q, ?",
    ["T", "V", "U", "W"], 2,
    "Each letter is 4 places after the previous one: Q + 4 = U.",
    "Tip: A, E, I, M, Q, U steps by four; the vowels A, E, I appear because 4 happens to land on them early.")
add(T, 19, "Travelling at a speed of 120 km/hour, how much time would be taken to cover a road that is 24 km long?",
    ["5 minutes", "12 minutes", "20 minutes", "30 minutes"], 1,
    "Time = distance / speed = 24 / 120 = 0.2 hour, which is 0.2 x 60 = 12 minutes.",
    "Tip: remember time = distance divided by speed, and convert hours to minutes by multiplying by 60.")
add(T, 20, "In a class of 100 students, 40% failed in English and 70% in Urdu. Were there any who failed both in English and Urdu?",
    ["Yes", "No", "Cannot say"], 0,
    "40 + 70 = 110, which is more than 100 students, so at least 10 students must have failed both subjects.",
    "Tip: if the percentages of two groups add up to more than 100, the groups must overlap.")
add(T, 21, "Which letter comes next in the following series: R, O, L, I, F, ?",
    ["D", "B", "C", "E"], 2,
    "Each letter moves back by 3: R, O, L, I, F, then F - 3 = C.",
    "Tip: a series can run backwards through the alphabet; watch for a constant negative gap.")
add(T, 22, "Kalam lifted 20kg more than Kalim. Shakir lifted more than Kalim. Sabir lifted less than Shakir. Is it possible that Shakir and Sabir lifted the same amount of load?",
    ["YES", "NO", "CANNOT SAY"], 1,
    "Sabir lifted less than Shakir, so they cannot have lifted the same amount.",
    "Tip: a statement using less than or more than rules out equality directly.")
add(T, 23, "If Aslam is taller than Hafeez and Hafeez is shorter than Mani, then Aslam is the tallest:",
    ["TRUE", "FALSE", "UNCERTAIN"], 2,
    "We know Aslam is above Hafeez and Mani is above Hafeez, but Aslam and Mani are not compared, so we cannot tell who is tallest.",
    "Tip: a conclusion is certain only if every comparison needed is stated in the premises.")
add(T, 24, "Which number comes next: 2500, 500, 100, 20, ?",
    ["5", "4", "2", "10"], 1,
    "Each number is divided by 5: 2500, 500, 100, 20, then 20 / 5 = 4.",
    "Tip: when numbers fall fast, test division before subtraction.")
add(T, 25, "What is different from the rest?",
    ["SWIM", "WALK", "RUN", "GYMNASTIC", "GAME"], 4,
    "Swim, walk, run and gymnastic are physical exercises or movements, while game is a general term for a competitive activity.",
    "Tip: look for the item that is a broader category than the rest.")
add(T, 26, "NEAR means the opposite of:",
    ["CLOSE", "ROAD", "SPEED", "FAR", "DISTANCE"], 3,
    "The opposite of near is far.",
    "Tip: avoid synonyms such as close, which mean the same thing, when an opposite is asked.")
add(T, 27, "Which number comes next: 92, 46, 48, 24, 26, ?",
    ["28", "12", "13", "52"], 2,
    "The pattern alternates: divide by 2, then add 2. 92 / 2 = 46, +2 = 48, /2 = 24, +2 = 26, /2 = 13.",
    "Tip: alternating operations (divide, then add) are common; test each step separately.")
add(T, 28, "All birds have wings. Some insects have wings. X has wings, therefore it is a bird?",
    ["TRUE", "FALSE", "UNCERTAIN"], 2,
    "Having wings is shared by birds and some insects, so X could be either; we cannot conclude it is a bird.",
    "Tip: from all A are B you cannot reverse to all B are A.")
add(T, 29, "What will be the area of a rectangle that is 16 feet long and 12 feet wide?",
    ["56 square feet", "192 square feet", "144 square feet", "28 square feet"], 1,
    "Area = length x width = 16 x 12 = 192 square feet.",
    "Tip: area is length times width, while 2 x (length + width) is the perimeter.")
add(T, 30, "ARMY is to SOLDIER as NAVY is to:",
    ["PILOT", "SAILOR", "CAPTAIN", "GENERAL"], 1,
    "A soldier serves in the army and a sailor serves in the navy.",
    "Tip: in this analogy the second word is the ordinary member of the first.")

# ---------------------------------------------------------------- TEST 8
T = 8
add(T, 1, "Which letter comes next in the following series: S, Q, N, L, I, ?",
    ["H", "F", "G", "E"], 2,
    "Gaps alternate -2, -3: S to Q is 2, Q to N is 3, N to L is 2, L to I is 3, then -2 gives G.",
    "Tip: alternating gaps in letter series repeat in pairs; list the gaps.")
add(T, 2, "Which number comes next: 28, 19, 12, 7, ?",
    ["3", "5", "2", "4"], 3,
    "Differences are -9, -7, -5, so the next is -3: 7 - 3 = 4.",
    "Tip: the differences decrease by 2 each time, a typical second-order series.")
add(T, 3, "Three oranges cost Rs.6. How much will 1 and a half dozen cost?",
    ["Rs.18", "Rs.24", "Rs.36", "Rs.54"], 2,
    "One orange costs Rs.2. One and a half dozen is 18 oranges, so 18 x 2 = Rs.36.",
    "Tip: find the unit price first, and remember a dozen is 12.")
add(T, 4, "AGREED is to 157224 as GEARED is to:",
    ["521754", "521724", "251724", "542271"], 1,
    "A=1, G=5, R=7, E=2, D=4. GEARED = G,E,A,R,E,D = 5,2,1,7,2,4 = 521724.",
    "Tip: repeated letters, like the two E's, must give the same digit.")
add(T, 5, "NARROW is to WIDE as THIN is to:",
    ["FAT", "WEIGHT", "MAN", "PRESENT"], 0,
    "Narrow and wide are opposites, and the opposite of thin is fat.",
    "Tip: first decide whether the relation is synonym or antonym.")
add(T, 6, "WAR means the opposite of:",
    ["SUFFERING", "JOY", "CRUELTY", "FIGHT", "PEACE"], 4,
    "The opposite of war is peace.",
    "Tip: the opposite of war-like states such as conflict is peace, not merely happiness.")
add(T, 7, "Which of the following is different from the rest?",
    ["YACHT", "STEAMER", "SHIP", "AIRCRAFT"], 3,
    "Yacht, steamer and ship travel on water, while an aircraft travels in the air.",
    "Tip: group items by the medium they operate in (land, water, air).")
add(T, 8, "Which letter comes next in the following series: X, T, P, L, H, ?",
    ["E", "C", "D", "F"], 2,
    "Each letter moves back by 4: X, T, P, L, H, then H - 4 = D.",
    "Tip: count backwards carefully when letters step down.")
add(T, 9, "Which number comes next: 229, 222, 37, 32, 8, ?",
    ["3", "5", "6", "4"], 1,
    "The numbers fall in pairs by 7, 5 and 3: 229 - 7 = 222, 37 - 5 = 32, so 8 - 3 = 5.",
    "Tip: the amount subtracted shrinks by 2 each pair (7, 5, 3).")
add(T, 10, "What is the area of a rectangle that is 6 feet long and 4 feet wide?",
    ["10 square feet", "20 square feet", "24 square feet", "48 square feet"], 2,
    "Area = 6 x 4 = 24 square feet.",
    "Tip: perimeter would be 2 x (6 + 4) = 20, a common wrong answer.")
add(T, 11, "If Ahmed is older than Kamal and Kamal is younger than Imran, then Ahmed is:",
    ["Older (than Imran)", "Just as old as Imran", "Younger than Imran", "Cannot say"], 3,
    "Both Ahmed and Imran are older than Kamal, but Ahmed and Imran are not compared directly.",
    "Tip: two people both above a third cannot be ranked against each other.")
add(T, 12, "Sun gives light because:",
    ["People", "Gases burn on its surface", "Crops need sunshine", "It is daytime"], 1,
    "The sun is a star where nuclear reactions heat gases so strongly that they glow and give off light.",
    "Tip: the sun's energy comes from nuclear fusion of hydrogen into helium.")
add(T, 13, "Which letter comes next in the following series: A, Z, B, Y, C, ?",
    ["W", "D", "X", "V"], 2,
    "Two series run together: A, B, C going forward and Z, Y, X going backward. After C comes X.",
    "Tip: when letters jump from the start to the end of the alphabet, think of two interleaved series.")
add(T, 14, "A mother is always (?) than her daughter:",
    ["Wiser", "Taller", "Stouter", "Older", "Wrinkled"], 3,
    "A mother is always older than her daughter; the other qualities may differ.",
    "Tip: choose the quality guaranteed by the relationship itself.")
add(T, 15, "Which one of the following is the smallest?",
    ["73", "7.3", "0.073", "0.73", "0.1"], 2,
    "Comparing the values: 0.073 is less than 0.1, 0.73, 7.3 and 73, so it is smallest.",
    "Tip: compare decimals place by place; more leading zeros means a smaller number.")
add(T, 16, "Tail is to ANIMAL as Beak is to:",
    ["EAT", "FLY", "BIRD", "CHIRP"], 2,
    "A tail is a body part of an animal and a beak is a body part of a bird.",
    "Tip: part-to-whole analogies pair a body part with the creature that has it.")
add(T, 17, "Which one of the following is different from the rest?",
    ["CROW", "PARROT", "OWL", "LION", "SPARROW"], 3,
    "Crow, parrot, owl and sparrow are birds, while a lion is a mammal.",
    "Tip: check class (bird, mammal, fish) when animals are listed.")
add(T, 18, "Which letter comes next in the following series: H, J, K, M, N, ?",
    ["O", "Q", "P", "R"], 2,
    "The gaps alternate +2, +1: H to J is 2, J to K is 1, K to M is 2, M to N is 1, so N + 2 = P.",
    "Tip: write down each gap and look for the repeating pair.")
add(T, 19, "A man had a wife, two sons and their wives and two grandsons. How many were they in all?",
    ["6", "7", "8", "9"], 2,
    "Man 1 + wife 1 + two sons 2 + their wives 2 + two grandsons 2 = 8.",
    "Tip: do not forget to count the man himself in family-count questions.")
add(T, 20, "HIGH is to LOW as COWARD is to:",
    ["ENEMY", "MISTER", "WEAK", "BRAVE", "STRONG"], 3,
    "High and low are opposites; the opposite of coward is brave.",
    "Tip: the opposite of coward is brave, whereas strong is a different quality.")
add(T, 21, "Which letter comes next in the following series: A, G, H, N, O, ?",
    ["S", "T", "U", "V"], 2,
    "The gaps alternate +6, +1: A to G is 6, G to H is 1, H to N is 6, N to O is 1, so O + 6 = U.",
    "Tip: alternating large and small gaps usually mean two linked patterns.")
add(T, 22, "A man bought some chairs for Rs.3500 and sold them for Rs.5500. He earned a profit of Rs.100 per chair. How many chairs did he buy?",
    ["15", "20", "25", "35"], 1,
    "Total profit = 5500 - 3500 = 2000. At Rs.100 per chair, the number of chairs = 2000 / 100 = 20.",
    "Tip: total profit divided by profit per item gives the number of items.")
add(T, 23, "PERMANENT is the opposite of:",
    ["PART-TIME", "LEVER", "CHANGING", "TEMPORARY", "STEADY"], 3,
    "Permanent means lasting for ever; its opposite is temporary.",
    "Tip: changing is similar in idea but temporary is the true antonym.")
add(T, 24, "Which number comes next: 130, 81, 45, 20, ?",
    ["9", "4", "11", "6"], 1,
    "Differences are 49, 36, 25, which are 7 squared, 6 squared and 5 squared. Next is 4 squared = 16: 20 - 16 = 4.",
    "Tip: differences that look like perfect squares (49, 36, 25, 16) are a clue.")
add(T, 25, "Which one of the following is different from the rest?",
    ["PEAR", "POTATO", "ORANGE", "BANANA", "APPLE"], 1,
    "Pear, orange, banana and apple are fruits, while potato is a vegetable.",
    "Tip: classify by food group when a list mixes fruits and vegetables.")
add(T, 26, "NEVER means the opposite of:",
    ["SELDOM", "ALWAYS", "NOW", "WILL", "FORGET"], 1,
    "The opposite of never is always.",
    "Tip: seldom is only close to never, but always is the exact opposite.")
add(T, 27, "Which number comes next: 19, 10, 15, 7, 11, 4, ?",
    ["8", "7", "9", "1"], 1,
    "Take alternate terms: 19, 15, 11 fall by 4, so the next is 7 (the other series 10, 7, 4 falls by 3).",
    "Tip: for zigzag series, separate odd and even positions and find the next term of the right series.")
add(T, 28, "SKY is HIGH as EARTH is:",
    ["ROUND", "FLAT", "LOW", "GLOBE"], 2,
    "The sky is high and the earth is low by comparison.",
    "Tip: in this analogy the second word describes the position of the first.")
add(T, 29, "A man bought 2 dozen eggs at the rate of Rs.10 per dozen and 36 eggs at the rate of Rs.12 per dozen. How many rupees did he pay in all?",
    ["Rs.44", "Rs.56", "Rs.60", "Rs.68"], 1,
    "Two dozen at Rs.10 cost Rs.20. 36 eggs are 3 dozen at Rs.12, costing Rs.36. Total = 20 + 36 = Rs.56.",
    "Tip: convert everything to dozens before multiplying by the rate.")
add(T, 30, "A person who flies an AIRCRAFT is called:",
    ["PARATROOPER", "DRIVER", "CAPTAIN", "PILOT"], 3,
    "A person who flies an aircraft is a pilot.",
    "Tip: captain is a rank, while pilot is the name of the job.")

# ---------------------------------------------------------------- TEST 9
T = 9
add(T, 1, "Which letter comes next in the following series: B, E, G, J, L, ?",
    ["M", "N", "O", "P"], 2,
    "The gaps alternate +3, +2: B to E is 3, E to G is 2, G to J is 3, J to L is 2, so L + 3 = O.",
    "Tip: alternating gaps of 3 and 2 repeat; add the next gap in turn.")
add(T, 2, "Which number comes next: 34, 24, 16, 10, 6, ?",
    ["2", "3", "4", "5"], 2,
    "Differences are -10, -8, -6, -4, so the next is -2: 6 - 2 = 4.",
    "Tip: differences that shrink by 2 each step form a second-order series.")
add(T, 3, "If you can buy 4 pencils for Rs.6, how many can you buy for Rs.18?",
    ["9", "12", "16", "24"], 1,
    "Rs.18 is three times Rs.6, so you get 3 x 4 = 12 pencils.",
    "Tip: use ratios, because tripling the money triples the quantity.")
add(T, 4, "DERANGE is to 4371563 as GRAND is to:",
    ["67154", "67145", "76154"], 0,
    "D=4, E=3, R=7, A=1, N=5, G=6. GRAND = G,R,A,N,D = 6,7,1,5,4 = 67154.",
    "Tip: build the letter-digit table first, then translate the new word.")
add(T, 5, "DANGEROUS means the opposite of:",
    ["BRAVE", "COWARDLY", "THREATENING", "SAFE", "FEAR"], 3,
    "The opposite of dangerous is safe.",
    "Tip: threatening is a synonym, not an antonym.")
add(T, 6, "DARK is to NIGHT as DAY is to:",
    ["SHINE", "WHITE", "LIGHT", "SUN"], 2,
    "Darkness is associated with night, and light is associated with day.",
    "Tip: this is a characteristic-of analogy.")
add(T, 7, "Which one of the following is different from the rest?",
    ["HOUSE", "BUILDING", "HUT", "VILLA"], 1,
    "House, hut and villa are specific types of homes to live in, while building is a general term for any structure.",
    "Tip: spot the word that is a general category rather than a specific kind.")
add(T, 8, "Which letter comes next in the following series: C, F, H, K, M, ?",
    ["N", "O", "P", "Q"], 2,
    "The gaps alternate +3, +2: C to F is 3, F to H is 2, H to K is 3, K to M is 2, so M + 3 = P.",
    "Tip: write each letter as a number and list the gaps.")
add(T, 9, "Which number comes next: 30, 27, 24, 21, ?",
    ["20", "19", "18", "17"], 2,
    "Each number falls by 3, so 21 - 3 = 18.",
    "Tip: a constant difference means an arithmetic series.")
add(T, 10, "If pencils sell at Rs.10 per dozen and the price of one sharpener is Rs.2, what will be the price of 24 pencils and one dozen sharpeners?",
    ["Rs.34", "Rs.44", "Rs.46", "Rs.54"], 1,
    "24 pencils are 2 dozen = Rs.20. One dozen sharpeners = 12 x 2 = Rs.24. Total = Rs.44.",
    "Tip: convert to the unit used in the price (dozens) before multiplying.")
add(T, 11, "If March comes before April and April comes after July, write 6 as your answer, otherwise write the last letter of the month that comes at the end of the year.",
    ["6", "R", "H", "D"], 1,
    "April does not come after July, so the condition is false. The month at the end of the year is December, whose last letter is R.",
    "Tip: check the condition first; both parts must be true for the first answer.")
add(T, 12, "If Anwar is a student and all students are lazy then he:",
    ["Is lazy", "May be lazy", "Is not lazy", "Cannot be lazy"], 0,
    "All students are lazy and Anwar is a student, so Anwar is lazy.",
    "Tip: a universal statement (all) applies to every member of the group.")
add(T, 13, "Which letter comes next: Z, W, T, Q, N, ?",
    ["L", "K", "J", "M"], 1,
    "Each letter moves back by 3: Z, W, T, Q, N, then N - 3 = K.",
    "Tip: count back three places in the alphabet each time. (This question is handwritten on the paper as number 13.)")
add(T, 14, "How many letters of the word CENTRAL are also found in the word DISCOVER?",
    ["2", "3", "4", "5"], 1,
    "DISCOVER contains C, E and R from CENTRAL; N, T, A and L are missing. So the answer is 3.",
    "Tip: check each letter of the first word against the second, one by one.")
add(T, 15, "Twelve years ago Akhtar was half of his present age. What will be his age after 12 years?",
    ["24", "30", "36", "48"], 2,
    "If x is his age, x - 12 = x / 2, so x = 24. After 12 years he will be 24 + 12 = 36.",
    "Tip: set up a simple equation instead of guessing ages.")
add(T, 16, "RED is to BLOOD as WHITE is to:",
    ["CLEAR", "WATER", "MILK", "SILK", "COW"], 2,
    "Blood is red and milk is white, so the pairing is an object and its colour.",
    "Tip: this is a colour-association analogy.")
add(T, 17, "MAN is to MASCULINE as WOMAN is to:",
    ["INTUITIVE", "MADAME", "FEMININE", "GIRL"], 2,
    "Masculine is the adjective for a man and feminine is the adjective for a woman.",
    "Tip: match the type of word, here an adjective.")
add(T, 18, "Which letter comes next in the following series: D, F, I, M, R, ?",
    ["V", "W", "X", "Y"], 2,
    "The gaps increase by 1 each time: +2, +3, +4, +5, and the next is +6: R + 6 = X.",
    "Tip: gaps that grow by one each step are a common letter pattern.")
add(T, 19, "A family consists of a man, his two wives, three daughters, four sons and their wives. How many members are there in the whole family?",
    ["10", "12", "14", "16"], 2,
    "Man 1 + two wives 2 + three daughters 3 + four sons 4 + sons' wives 4 = 14.",
    "Tip: list each group and add; include the man himself.")
add(T, 20, "FAST means the opposite of:",
    ["QUICK", "SLOW", "SPEED", "HUNGRY", "DULL"], 1,
    "The opposite of fast is slow.",
    "Tip: quick and speed are synonyms, so they cannot be the answer.")
add(T, 21, "Which letter comes next in the following series: A, B, I, J, Q, ?",
    ["R", "S", "Z", "P"], 0,
    "The gaps alternate +1, +7: A to B is 1, B to I is 7, I to J is 1, J to Q is 7, so Q + 1 = R.",
    "Tip: pairs of consecutive letters separated by a big gap are a classic pattern.")
add(T, 22, "If three is subtracted from 12, then what will be one third of the remaining?",
    ["3", "4", "9", "5"], 0,
    "12 - 3 = 9, and one third of 9 is 3.",
    "Tip: follow the order of operations given in the sentence.")
add(T, 23, "BOTTLE is to CORK as BOX is to:",
    ["FIGHT", "LID", "HAT", "CRATE"], 1,
    "A cork closes a bottle, and a lid closes a box.",
    "Tip: this is an object and its closing part.")
add(T, 24, "Which number comes next: 11, 6, 7, 3, 5, ?",
    ["1", "2", "4", "3"], 1,
    "The changes follow a pattern: -5, +1, -4, +2, -3. So 5 - 3 = 2.",
    "Tip: when the differences alternate in sign, look at the sequence of subtracted and added amounts separately.")
add(T, 25, "Which group of letters is different from the others?",
    ["ACBC", "MCPO", "XZYZ", "JLK"], 1,
    "ACBC, XZYZ and JLK(L) follow the same pattern of one letter, one ahead, one in between, repeating the middle one; MCPO does not follow it.",
    "Tip: compare the position patterns inside each group, not the letters themselves.")
add(T, 26, "FOOT is to LEG as HAND is to:",
    ["BODY", "FINGER", "TALL", "LIMB", "ARM"], 4,
    "The foot is attached to the leg, and the hand is attached to the arm.",
    "Tip: this is a body-part connection analogy.")
add(T, 27, "Which number comes next: 18, 13, 9, 6, 4, ?",
    ["1", "2", "3", "5"], 2,
    "The differences are -5, -4, -3, -2, so the next is -1: 4 - 1 = 3.",
    "Tip: the differences decrease by one each time.")
add(T, 28, "INFANCY is to CHILDHOOD as ADOLESCENCE is to:",
    ["ADULTERY", "MATURITY", "SINCERE", "INTELLIGENCE", "YOUTH"], 4,
    "Stages of life follow in order: infancy, childhood, adolescence, then youth.",
    "Tip: the sequence of human life stages is infancy, childhood, adolescence, adulthood, old age.")
add(T, 29, "What number when multiplied by 3 gives one less than 10?",
    ["2", "3", "4", "7"], 1,
    "One less than 10 is 9, and 9 / 3 = 3.",
    "Tip: work backwards by dividing the result by the multiplier.")
add(T, 30, "Which one of the following is different from the rest?",
    ["SING", "CALL", "HEAR", "SPEAK"], 2,
    "Sing, call and speak are all ways of making sounds with the voice, while hear is a way of receiving sounds.",
    "Tip: separate actions of producing from actions of receiving.")

# ---------------------------------------------------------------- TEST 10
T = 10
add(T, 1, "Which letter comes next in the following series: D, G, K, N, R, ?",
    ["S", "T", "U", "V"], 2,
    "The gaps alternate +3, +4: D to G is 3, G to K is 4, K to N is 3, N to R is 4, so R + 3 = U.",
    "Tip: alternating gaps of 3 and 4 repeat in turn.")
add(T, 2, "Which number comes next: 81, 64, 49, 36, ?",
    ["16", "24", "25", "20"], 2,
    "These are perfect squares in descending order: 9 squared, 8 squared, 7 squared, 6 squared, and next is 5 squared = 25.",
    "Tip: learn the squares up to 20 to spot these series quickly.")
add(T, 3, "If apples are sold for Rs.15 per kg, how many grams can you buy for Rs.6?",
    ["250 grams", "400 grams", "600 grams", "900 grams"], 1,
    "Rs.6 / Rs.15 = 0.4 kg, which is 400 grams.",
    "Tip: 1 kg equals 1000 grams, so convert at the end.")
add(T, 4, "TRIP is to DAY as CALENDAR is to:",
    ["YEAR", "WEEK END", "MARCH", "CENTURY"], 0,
    "A trip is measured in days, and a calendar is measured in a year.",
    "Tip: this is a unit-of-measure analogy; match the unit that the object covers.")
add(T, 5, "CLOCK is to DAY as CALENDAR is to:",
    ["YEAR", "WEEK END", "MARCH", "CENTURY"], 0,
    "A clock tracks the hours of a day, and a calendar tracks the days of a year.",
    "Tip: a clock tracks the day, a calendar tracks the year.")
add(T, 6, "Which one of the following is different from the rest?",
    ["SELL", "SMUGGLE", "CHEAT", "STEAL", "BRIBE"], 0,
    "Smuggle, cheat, steal and bribe are illegal or dishonest acts, while selling is a normal lawful activity.",
    "Tip: look for the lawful item among a list of crimes.")
add(T, 7, "A person who writes poems is called:",
    ["PHILOSPHER", "LITERATE", "POET", "SINGER", "DOCTOR"], 2,
    "A poet writes poems.",
    "Tip: Allama Iqbal, the national poet of Pakistan, is a famous example.")
add(T, 8, "Which letter comes next in the following series: C, D, G, J, K, ?",
    ["L", "M", "N", "O"], 2,
    "The gaps are +1, +3, +3, +1, then +3: K + 3 = N.",
    "Tip: when no single gap repeats, list all the gaps and look for the cycle.")
add(T, 9, "Which number comes next: 14, 10, 7, 5, ?",
    ["3", "4", "2", "1"], 1,
    "Differences are -4, -3, -2, so the next is -1: 5 - 1 = 4.",
    "Tip: differences falling by one each step lead to a simple next difference.")
add(T, 10, "What will be the third angle of a triangle whose two angles are 45 degrees and 60 degrees?",
    ["65 degrees", "90 degrees", "75 degrees", "105 degrees"], 2,
    "The angles of a triangle add to 180 degrees: 180 - 45 - 60 = 75 degrees.",
    "Tip: the angles in any triangle always add up to 180 degrees.")
add(T, 11, "If day before yesterday was FRIDAY, tomorrow would be:",
    ["SATURDAY", "MONDAY", "POET", "SINGER", "DOCTOR"], 1,
    "If the day before yesterday was Friday, yesterday was Saturday and today is Sunday, so tomorrow is Monday.",
    "Tip: count forward from the known day one step at a time.")
add(T, 12, "People buy food because:",
    ["They have money", "They want to entertain others", "They are hungry", "They need to eat it"], 3,
    "Food is a basic need of the body, so people buy it because they need to eat it, whether or not they feel hungry at the moment.",
    "Tip: when options overlap, the key answer is the most general and necessary reason.")
add(T, 13, "Which letter comes next in the following series: B, E, F, J, K, ?",
    ["N", "O", "P", "Q"], 2,
    "The gaps are +3, +1, +4, +1, +5, so the next gap pattern gives K + 5 = P.",
    "Tip: letter gaps that interleave +1 with growing gaps (3, 4, 5) are a common pattern.")
add(T, 14, "Clouds are formed because:",
    ["We need water", "Water evaporates", "There is no sun", "Chemical changes take place in the atmosphere"], 1,
    "Water from the seas, rivers and land evaporates, rises, cools and condenses into tiny droplets that make clouds.",
    "Tip: this process is part of the water cycle: evaporation, condensation, precipitation.")
add(T, 15, "If mangoes sell at Rs.12 per kg, how much can be bought for Rs.768?",
    ["56 kg", "64 kg", "72 kg", "84 kg"], 1,
    "768 / 12 = 64 kg.",
    "Tip: quantity equals total money divided by the price per unit.")
add(T, 16, "TRIANGLE is to PRISM as CIRCLE is to:",
    ["CIRCUMFERENCE", "SPHERE", "RADIUS", "CYLINDER"], 3,
    "A prism is a triangle extended into three dimensions with the same cross-section, and a cylinder is a circle extended the same way.",
    "Tip: the key sheet gives sphere here, but a prism has constant triangular cross-sections just as a cylinder has circular ones.")
add(T, 17, "RECEDE is to PROCEED as STOP is to:",
    ["PREVENT", "BOTTLE", "GONE", "GO"], 3,
    "Recede and proceed are opposites, and the opposite of stop is go.",
    "Tip: recede means to move back, and proceed means to move forward.")
add(T, 18, "Which letter comes next in the following series: A, W, B, V, C, ?",
    ["B", "D", "U", "T"], 2,
    "Two series run together: A, B, C going forward and W, V, then U going backward.",
    "Tip: interleaved series run in turn, one forward and one backward.")
add(T, 19, "If one dozen pencils can be bought for Rs.15, how much will 72 pencils cost?",
    ["Rs.60", "Rs.75", "Rs.90", "Rs.180"], 2,
    "72 pencils are 6 dozen, so the cost is 6 x 15 = Rs.90.",
    "Tip: convert the total number to dozens first.")
add(T, 20, "Which one of the following is different from the rest?",
    ["TONGUE", "ANKLE", "KNEE", "FOOT", "TOE"], 0,
    "Ankle, knee, foot and toe are all parts of the leg, while the tongue is in the mouth.",
    "Tip: group body parts by the area they belong to.")
add(T, 21, "Which letter comes next in the following series: B, E, H, K, N, ?",
    ["O", "P", "Q", "R"], 2,
    "Each letter moves forward by 3: N + 3 = Q.",
    "Tip: a constant gap makes this one of the easiest letter series.")
add(T, 22, "Which figure represents the smallest amount?",
    ["10", "0.09", "0.9", "1.1", "3.1"], 1,
    "Comparing decimals: 0.09 is less than 0.9, 1.1, 3.1 and 10, so it is the smallest.",
    "Tip: a decimal with more leading zeros after the point is smaller.")
add(T, 23, "EXTRAVAGANT means the opposite:",
    ["MISER", "HUMBLE", "ECONOMICAL", "POOR", "WASTEFUL"], 2,
    "Extravagant means spending too much, and its opposite is economical, spending carefully.",
    "Tip: the key sheet gives miser, but economical is the matching adjective, and wasteful is a synonym of extravagant.")
add(T, 24, "Which number comes next: 48, 24, 12, 6, ?",
    ["2", "3", "4", "0"], 1,
    "Each number is half of the previous one, so 6 / 2 = 3.",
    "Tip: halving each time makes a geometric series with ratio one half.")
add(T, 25, "A bird does not always have:",
    ["WING", "EYES", "FEET", "A NEST", "A BILL"], 3,
    "Every bird has wings, eyes, feet and a bill, but not every bird builds or lives in a nest all the time.",
    "Tip: the key sheet gives a bill, but a bill (beak) is a defining feature of all birds, so a nest is the best answer.")
add(T, 26, "BEGIN is to END as NORTH is to:",
    ["SOUTH WEST", "WEST", "SOUTH EAST", "EAST", "SOUTH"], 4,
    "Begin and end are opposites, and the opposite direction of north is south.",
    "Tip: the four cardinal directions form two opposite pairs: north and south, east and west.")
add(T, 27, "Which number comes next: 42, 30, 20, 12, ?",
    ["4", "6", "8", "10"], 1,
    "Differences are -12, -10, -8, so the next is -6: 12 - 6 = 6.",
    "Tip: these numbers are products of consecutive integers (7x6, 6x5, 5x4, 4x3, 3x2).")
add(T, 28, "Which one of the following is different from the rest?",
    ["TREE", "STEM", "ROOT", "BRANCH", "LEAF"], 0,
    "Stem, root, branch and leaf are parts of a plant, while the tree is the whole plant.",
    "Tip: look for the whole among a list of parts.")
add(T, 29, "Which number is missing in the following series: 98, 70, ?, 14",
    ["28", "42", "56", "35"], 1,
    "The series falls by 28 each time: 98, 70, 42, 14.",
    "Tip: find the common difference from the two known neighbours (98 - 70 = 28).")
add(T, 30, "BAIT is to FISH as GUN is to:",
    ["HUNT", "TRIGGER", "SHOT", "BULLET"], 3,
    "Bait is the thing used to catch a fish, and a bullet is the thing fired from a gun to hit a target.",
    "Tip: this analogy links a tool to what it is used to capture.")
