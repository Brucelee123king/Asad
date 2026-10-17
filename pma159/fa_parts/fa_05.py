# Forces Academy Intelligence Tests 15, 16, 17, 20
QS = []

def _add(test, n, text, opts, ci, reason, fact):
    sec = "Forces Academy Intelligence Test %d" % test
    label = "(Forces Academy Test %d · Q%d) " % (test, n)
    QS.append((sec, label + text, opts, ci, reason, fact))

D15 = "Which one of the following is different? "
T = 15
_add(T, 1, D15 + "A. MNO, B. STW, C. XYZ, D. EFG, E. BCD", ["MNO", "STW", "XYZ", "EFG", "BCD"], 1,
     "MNO, XYZ, EFG and BCD are three consecutive letters of the alphabet. STW skips a letter (S, T, then W).",
     "Tip: in letter-group questions first check whether the letters are consecutive, then check gaps and direction.")
_add(T, 2, D15 + "A. EVU, B. RHI, C. OLK, D. SHG, E. HSR", ["EVU", "RHI", "OLK", "SHG", "HSR"], 1,
     "EVU, OLK, SHG and HSR all end with two letters in backward alphabetical order (V U, L K, H G, S R). RHI ends with H I, which goes forward.",
     "Tip: compare the direction of movement inside each group, not only the letters themselves.")
_add(T, 3, D15 + "A. PQO, B. KJL, C. UYW, D. SRT, E. FEG", ["PQO", "KJL", "UYW", "SRT", "FEG"], 0,
     "KJL, SRT and FEG each go one step back then two steps forward (-1, +2). PQO goes forward then back (+1, -2), the reverse of that pattern, which is the answer given in the key.",
     "Tip: write the step sizes between neighbouring letters, as in +1, -2, to spot the odd group.")
_add(T, 4, D15 + "A. LLMN, B. UUVW, C. CCDE, D. GGHI, E. RRRS", ["LLMN", "UUVW", "CCDE", "GGHI", "RRRS"], 4,
     "The others repeat the first letter twice and then follow with the next two consecutive letters. RRRS repeats its first letter three times.",
     "Tip: count repeated letters as well as the order of the alphabet.")
_add(T, 5, D15 + "A. Boy, B. Girl, C. Woman, D. Lady, E. Female", ["Boy", "Girl", "Woman", "Lady", "Female"], 0,
     "Girl, woman, lady and female all refer to the female sex. A boy is male.",
     "Tip: in word odd-one-out questions look for a shared category such as gender, material or function.")
_add(T, 6, D15 + "A. Picture, B. Painting, C. Photography, D. Poster", ["Picture", "Painting", "Photography", "Poster"], 2,
     "Picture, painting and poster are finished visual items. Photography is the art or process of taking photographs, not an item.",
     "Tip: separate objects from activities or processes when finding the odd one out.")
_add(T, 7, D15 + "A. Tobacco, B. Pipe, C. Cigarette, D. Cigar", ["Tobacco", "Pipe", "Cigarette", "Cigar"], 1,
     "Tobacco, cigarette and cigar are all made of tobacco. A pipe is only a device in which tobacco is smoked.",
     "Tip: ask what each item is made of or what it is used for.")
_add(T, 8, D15 + "A. Stationary, B. Eraser, C. Pen, D. Paper", ["Stationary", "Eraser", "Pen", "Paper"], 0,
     "Eraser, pen and paper are all items of stationery. The word given, stationary, means not moving and is a different word.",
     "Tip: stationery with an e means writing materials, stationary with an a means not moving.")
_add(T, 9, D15 + "A. Feathers, B. Hair, C. Grass, D. Wool", ["Feathers", "Hair", "Grass", "Wool"], 2,
     "Feathers, hair and wool grow on the bodies of animals or birds. Grass is a plant.",
     "Tip: classify by origin, such as animal, plant or mineral.")
_add(T, 10, D15 + "A. Circle, B. Square, C. Triangle, D. Hexagon", ["Circle", "Square", "Triangle", "Hexagon"], 0,
     "Square, triangle and hexagon are polygons with straight sides and corners. A circle has a curved boundary and no corners.",
     "Tip: a polygon needs at least three straight sides.")
_add(T, 11, D15 + "A. Leprosy, B. Typhoid, C. Vomiting, D. Asthma", ["Leprosy", "Typhoid", "Vomiting", "Asthma"], 2,
     "Leprosy, typhoid and asthma are diseases. Vomiting is a symptom, not a disease in itself.",
     "Tip: distinguish a disease from a symptom of a disease.")
_add(T, 12, D15 + "A. Silver, B. Mercury, C. Gold, D. Iron", ["Silver", "Mercury", "Gold", "Iron"], 1,
     "Silver, gold and iron are solid metals at room temperature. Mercury is a liquid metal.",
     "Tip: mercury is the only metal that is liquid at normal room temperature.")
_add(T, 13, D15 + "A. Live, B. Die, C. Exist, D. Be", ["Live", "Die", "Exist", "Be"], 1,
     "Live, exist and be all mean to have life or being. Die means the opposite, to stop living.",
     "Tip: look for an antonym hidden among synonyms.")
_add(T, 14, D15 + "A. Hard, B. Stiff, C. Unbending, D. Flexible", ["Hard", "Stiff", "Unbending", "Flexible"], 3,
     "Hard, stiff and unbending describe something rigid. Flexible means able to bend easily.",
     "Tip: three synonyms and one antonym is a very common pattern.")
_add(T, 15, D15 + "A. Sports, B. Teem, C. Game, D. Team", ["Sports", "Teem", "Game", "Team"], 1,
     "Sports, game and team all belong to the field of games and play. Teem (to be full of) is unrelated.",
     "Tip: teem and team sound alike but have different meanings.")
_add(T, 16, D15 + "A. August, B. September, C. October, D. November", ["August", "September", "October", "November"], 0,
     "September, October and November all end in the letters ber. August does not.",
     "Tip: September to December get their names from Latin numbers (septem, octo, novem, decem).")
_add(T, 17, "All the rivers have? A. Towns, B. Bridge, C. Banks, D. Fish", ["Towns", "Bridge", "Banks", "Fish"], 2,
     "Every river, without exception, has banks on its sides. Not every river has towns, bridges or fish.",
     "Tip: choose the option that is always true, not just sometimes true.")
_add(T, 18, "ABD is to CBA as QRT is to?", ["SRQ", "TRQ", "SQR", "QRS"], 0,
     "ABD to CBA: first letter +2 (A to C), middle letter unchanged (B), last letter -3 (D to A). Apply this to QRT: Q+2 = S, R stays R, T-3 = Q, giving SRQ.",
     "Tip: compare each letter position separately to find the shift for that position.")
_add(T, 19, "What number comes next in the series: 8, 5, 3, 2, ?", ["0", "1", "2", "-1"], 1,
     "The differences are 3, 2, 1, so the next difference is 1 (the gaps themselves shrink by 1). 2 - 1 = 1.",
     "Tip: when the differences form their own pattern, extend the pattern of differences.")
_add(T, 20, "What is the smallest even number (counting zero as an even whole number)?", ["2", "1", "-2", "0"], 3,
     "Zero is divisible by 2 with no remainder, so it is an even number, and it is the smallest non-negative even number.",
     "Tip: some tests consider only positive numbers and give 2, but the key for this test counts zero.")
_add(T, 21, "What do you find once in a year and twice in a week?", ["The letter E", "The letter A", "Sunday", "The letter K"], 0,
     "The word YEAR contains the letter E once and the word WEEK contains it twice.",
     "Tip: riddles of this kind are often about the letters inside the words themselves.")
_add(T, 22, "Train is to track as bus is to?", ["Driver", "Road", "Station", "Ticket"], 1,
     "A train runs on a track and a bus runs on a road. Both pairs show a vehicle and the path it travels on.",
     "Tip: in analogy questions state the relationship in a sentence, then apply it to the second pair.")
_add(T, 23, "If 8 men out of 10 are bald, how many out of 1000 are not bald?", ["800", "100", "200", "20"], 2,
     "2 out of every 10 are not bald, which is 20 percent. 20 percent of 1000 is 200.",
     "Tip: work out the complement (not bald) first, then scale up.")
_add(T, 24, "What comes next in the series: 1, 2, 6, 12, 36, ?  (multiplying by 2, then 3, alternately)", ["108", "48", "72", "42"], 2,
     "The multipliers alternate x2, x3, x2, x3: 1x2 = 2, 2x3 = 6, 6x2 = 12, 12x3 = 36, so next is 36x2 = 72.",
     "Tip: if neither the differences nor a single ratio fit, try alternating operations.")
_add(T, 25, "Arrival is the opposite of? A. Reach, B. Departure, C. Away", ["Reach", "Departure", "Away"], 1,
     "Arrival means coming to a place and departure means leaving it, so they are opposites.",
     "Tip: reach is a synonym of arrival, not an antonym.")
_add(T, 26, "6 is to F as 11 is to? A. K, B. L, C. M", ["K", "L", "M"], 0,
     "F is the 6th letter of the alphabet, so the pair is number to its letter. The 11th letter is K.",
     "Tip: remember A=1, E=5, J=10, O=15, T=20 and Z=26 as quick anchors.")
_add(T, 27, "Aslam is four times as old as Ashraf. If the sum of their ages is 60 years, how old is Ashraf? A. 48 yrs, B. 12 yrs, C. 72 yrs", ["48 yrs", "12 yrs", "72 yrs"], 1,
     "Let Ashraf be x, so Aslam is 4x and x + 4x = 60, which gives 5x = 60 and x = 12.",
     "Tip: 48 is Aslam's age, so check which person the question asks about.")
_add(T, 28, "If 1/8 of a number is 6, what is the number? A. 14, B. 48, C. 42", ["14", "48", "42"], 1,
     "The number is 6 x 8 = 48.",
     "Tip: to find the whole from a fraction, multiply by the denominator.")
_add(T, 29, "Which one of the following is a prime number? A. 7, B. 8, C. 16, D. 12", ["7", "8", "16", "12"], 0,
     "7 has only two factors, 1 and 7. The others are even numbers greater than 2, so they have more factors.",
     "Tip: 2 is the only even prime number.")
_add(T, 30, "32% of 25 is? A. 16, B. 8, C. 4", ["16", "8", "4"], 1,
     "32 percent of 25 is 32/100 x 25 = 8.",
     "Tip: 25 is one quarter of 100, so 32% of 25 is 32 divided by 4 = 8.")

# ---------------- Test 16 ----------------
T = 16
S16 = "What number comes next in the following series? "
_add(T, 1, S16 + "11, 17, 23, ?", ["27", "28", "29", "35"], 2,
     "Each term increases by 6: 11, 17, 23, so next is 29.", "Tip: check for a constant difference first.")
_add(T, 2, S16 + "23, 19, 15, 11, ?", ["9", "8", "7", "6"], 2,
     "Each term decreases by 4, so next is 11 - 4 = 7.", "Tip: a constant negative difference gives a descending series.")
_add(T, 3, S16 + "6/11, 5/10, 4/9, 3/8, ?", ["1/6", "2/7", "2/8", "3/7"], 1,
     "The numerator falls by 1 each time and the denominator falls by 1 each time, so after 3/8 comes 2/7.",
     "Tip: in fraction series treat the numerators and denominators as two separate series.")
_add(T, 4, S16 + "1/3, 5, 1/7, 9, 1/11, ?", ["15", "1/13", "13", "12"], 2,
     "Alternate terms form two series: the fractions 1/3, 1/7, 1/11 and the whole numbers 5, 9, and the next is 13 (add 4).",
     "Tip: in alternating series split the terms into two separate sequences.")
_add(T, 5, S16 + "8, 4, 16, 8, 64, ?", ["128", "32", "16", "72"], 1,
     "The pattern is divide by 2, multiply by 4, divide by 2, multiply by 8, divide by 2: 8/2 = 4, 4x4 = 16, 16/2 = 8, 8x8 = 64, 64/2 = 32.",
     "Tip: when the pattern repeats an operation every second step, find it first, then follow the other operation separately.")
_add(T, 6, S16 + "3, 5, 3/5, 7, 11, ?", ["7/11", "11/7", "18", "13"], 0,
     "The terms come in groups of three: the first two numbers and then their fraction (3, 5, 3/5), then (7, 11, 7/11).",
     "Tip: mixed series of whole numbers and fractions are often built from repeating groups.")
_add(T, 7, S16 + "2/31, 3/52, 4/73, ?", ["5/84", "5/94", "6/94", "5/104"], 1,
     "The numerators go up by 1 (2, 3, 4, 5) and the denominators go up by 21 (31, 52, 73, 94), so next is 5/94.",
     "Tip: work out the difference of the top and bottom numbers separately.")
_add(T, 8, S16 + "93, 2, 73, 1, 63, 3, 33, 2, ?", ["23", "13", "3", "43"], 1,
     "Subtract ten times the number that follows: 93 - 20 = 73, 73 - 10 = 63, 63 - 30 = 33, 33 - 20 = 13.",
     "Tip: in interleaved series one set of numbers can control the change in the other set.")
_add(T, 9, S16 + "1/2, A/B, 3, C, 4/5, D/E, ?", ["F", "6", "5/6", "G"], 1,
     "The pattern is number pair, letter pair, number, letter, so the terms run 1/2, A/B, 3, C, 4/5, D/E, 6, F and the next is 6.",
     "Tip: when numbers and letters are mixed, follow the numbers and the letters as two interleaved sequences.")
_add(T, 10, S16 + "34/65, 23/54, 67/98, 45/?", ["45/66", "45/76", "45/87", "45/56"], 1,
     "In every fraction the denominator is the numerator plus 31 (34+31 = 65, 23+31 = 54, 67+31 = 98), so 45+31 = 76.",
     "Tip: compare the top and bottom of each fraction with each other.")
_add(T, 12, S16 + "2, 1, 3, 4, 7, ?", ["10", "11", "12", "9"], 1,
     "Each term is the sum of the two before it: 2+1 = 3, 1+3 = 4, 3+4 = 7, so next is 4+7 = 11.",
     "Tip: this is a Fibonacci-type series where each term is the sum of the previous two.")

D16 = "Which one of the following is different? "
_add(T, 13, D16 + "A. Young, B. Lovely, C. Beautiful, D. Handsome, E. Pretty", ["Young", "Lovely", "Beautiful", "Handsome", "Pretty"], 0,
     "Lovely, beautiful, handsome and pretty all describe good looks. Young describes age.", "Tip: group words by what they describe.")
_add(T, 14, D16 + "A. Month, B. Season, C. Year, D. Day, E. Week", ["Month", "Season", "Year", "Day", "Week"], 1,
     "Month, year, day and week are fixed units of time measured by the calendar. A season is a part of the year with a particular climate and has no fixed number of days.",
     "Tip: the four seasons are summer, autumn, winter and spring.")
_add(T, 15, D16 + "A. GHI, B. JKL, C. NOP, D. QST, E. UVW", ["GHI", "JKL", "NOP", "QST", "UVW"], 3,
     "The others are three consecutive letters of the alphabet. QST skips R.", "Tip: check for a skipped letter in letter-group questions.")
_add(T, 16, D16 + "A. Green, B. Red, C. Dark, D. Yellow, E. Brown", ["Green", "Red", "Dark", "Yellow", "Brown"], 2,
     "Green, red, yellow and brown are colours. Dark describes shade, not a particular colour.", "Tip: dark and light are shades that can apply to any colour.")
_add(T, 17, D16 + "A. Camel, B. Ox, C. Horse, D. Donkey, E. Mule", ["Camel", "Ox", "Horse", "Donkey", "Mule"], 4,
     "Camel, ox, horse and donkey are natural animal species. A mule is a hybrid, the offspring of a male donkey and a female horse.",
     "Tip: a hinny is the opposite cross, a male horse and a female donkey.")
_add(T, 18, D16 + "A. Hand, B. Arm, C. Body, D. Wrist, E. Fingers", ["Hand", "Arm", "Body", "Wrist", "Fingers"], 2,
     "Hand, arm, wrist and fingers are all parts of the arm. Body is the whole that contains them.", "Tip: whole versus part is a common way to make an odd one out.")
_add(T, 19, D16 + "A. Hot, B. Steam, C. Water, D. Ice, E. Vapour", ["Hot", "Steam", "Water", "Ice", "Vapour"], 0,
     "Steam, water, ice and vapour are forms of water. Hot is only a quality.", "Tip: water exists as solid (ice), liquid and gas (steam or vapour).")
_add(T, 20, D16 + "A. Square, B. Line, C. Triangle, D. Circle, E. Rectangle", ["Square", "Line", "Triangle", "Circle", "Rectangle"], 1,
     "Square, triangle, circle and rectangle are closed shapes enclosing an area. A line does not enclose any area.", "Tip: a closed shape has an inside and an outside.")
_add(T, 21, D16 + "A. Little, B. Rare, C. Less, D. Inferior, E. Few", ["Little", "Rare", "Less", "Inferior", "Few"], 3,
     "Little, rare, less and few all refer to small quantity or amount. Inferior refers to lower quality.", "Tip: separate words about quantity from words about quality.")
_add(T, 22, D16 + "A. RUS, B. FHG, C. MON, D. QSR, E. TVU", ["RUS", "FHG", "MON", "QSR", "TVU"], 0,
     "FHG, MON, QSR and TVU all follow the pattern +2, -1 between letters (F+2 = H, H-1 = G, and so on). RUS goes +3, -2.",
     "Tip: write the jump between each pair of letters to find the common pattern.")
_add(T, 23, D16 + "A. ABCACB, B. NOPNPO, C. RSTSTR, D. GHIGIH, E. KLMKML", ["ABCACB", "NOPNPO", "RSTSTR", "GHIGIH", "KLMKML"], 2,
     "In the others, three consecutive letters are followed by the same three with the last two swapped (ABC ACB, NOP NPO, GHI GIH, KLM KML). RSTSTR repeats the letters as S T R, which is a rotation instead.",
     "Tip: compare the second half of each string with the first half.")
_add(T, 24, D16 + "A. TSUS, B. NMOM, C. DCEC, D. HGJG, E. RQSQ", ["TSUS", "NMOM", "DCEC", "HGJG", "RQSQ"], 3,
     "TSUS, NMOM, DCEC and RQSQ all follow -1, +2, -2 between letters. HGJG goes -1, +3, -3, so it is different.",
     "Tip: the third letter in each group steps forward by 2 from the second letter in the other groups.")
_add(T, 25, D16 + "A. Play, B. Cricket, C. Swimming, D. Football, E. Child", ["Play", "Cricket", "Swimming", "Football", "Child"], 4,
     "Play, cricket, swimming and football are all sports or games. Child is a person.", "Tip: look for the item that is not an activity.")
_add(T, 26, D16 + "A. Two, B. Double, C. Pair, D. Three, E. Couple", ["Two", "Double", "Pair", "Three", "Couple"], 3,
     "Two, double, pair and couple all mean 2. Three is a different number.", "Tip: check whether most words share the same number.")
_add(T, 27, D16 + "A. STVU, B. HIJK, C. IJKL, D. OPQR, E. EFGH", ["STVU", "HIJK", "IJKL", "OPQR", "EFGH"], 0,
     "The others are four consecutive letters of the alphabet. STVU has the order S, T, V, U, which is not consecutive.", "Tip: look for a swapped or skipped letter.")
_add(T, 28, D16 + "A. Kingdom, B. State, C. Province, D. Citizen, E. Country", ["Kingdom", "State", "Province", "Citizen", "Country"], 3,
     "Kingdom, state, province and country are territories or political regions. A citizen is a person who lives in one.", "Tip: a place and a person are different kinds of noun.")
_add(T, 29, D16 + "A. Run, B. Flow, C. Swim, D. Fast, E. Move", ["Run", "Flow", "Swim", "Fast", "Move"], 3,
     "Run, flow, swim and move are verbs of motion. Fast is an adjective or adverb describing speed.", "Tip: look for a different part of speech.")
_add(T, 30, D16 + "A. DBC, B. MLK, C. ONM, D. CBA, E. ZYX", ["DBC", "MLK", "ONM", "CBA", "ZYX"], 0,
     "MLK, ONM, CBA and ZYX are each three consecutive letters in backward order. DBC is not in a consecutive order.", "Tip: check whether groups of letters run forwards or backwards.")

# ---------------- Test 17 ----------------
T = 17
_add(T, 1, "We read newspaper because: A. It is a good hobby, B. These give us knowledge, C. One learns how to read, D. These are motivating, E. These help us to get job",
     ["It is a good hobby", "These give us knowledge", "One learns how to read", "These are motivating", "These help us to get job"], 1,
     "The main purpose of a newspaper is to inform, so the best reason is that it gives knowledge.", "Tip: choose the most general and direct reason in cause-and-reason questions.")
_add(T, 2, "Which statement is correct? A. A son is always better educated than his father, B. A son is always more healthier than his father, C. A son is always younger than his father, D. A son is always less tall than his father, E. A son is always wiser than his father",
     ["A son is always better educated than his father", "A son is always more healthier than his father", "A son is always younger than his father",
      "A son is always less tall than his father", "A son is always wiser than his father"], 2,
     "A father is by definition born before his son, so the son is always younger. The other statements may be true sometimes but not always.", "Tip: the word always makes a statement false if there is even one exception.")
_add(T, 3, "If clock A goes faster than clock B and clock C keeps time with clock A, then: A. C is slower than B, B. B keeps time with C, C. C is faster than B, D. B may be faster or slower than C, E. B and C keeps time with A",
     ["C is slower than B", "B keeps time with C", "C is faster than B", "B may be faster or slower than C", "B and C keeps time with A"], 2,
     "C keeps the same time as A, and A is faster than B, so C is faster than B.", "Tip: replace equal items with each other and the comparison carries over.")
_add(T, 4, "2 is to 5 as K is to?", ["M", "N", "L", "P"], 1,
     "The step from 2 to 5 is +3. Moving 3 letters on from K (L, M, N) gives N.", "Tip: when numbers and letters are mixed, apply the same step to both.")
_add(T, 5, "Parents give education to their children because: A. Children want it, B. It is a custom, C. It gives them better chances in life, D. It makes them obedient, E. It gives employment to teachers",
     ["Children want it", "It is a custom", "It gives them better chances in life", "It makes them obedient", "It gives employment to teachers"], 2,
     "The real purpose of education is to improve a child's opportunities and future.", "Tip: pick the reason that best explains the underlying purpose.")
_add(T, 6, "TIME is to EMIT as 4375 is to?", ["5734", "5743", "3457", "7345"], 0,
     "EMIT is TIME written backwards, so reverse 4375 to get 5734.", "Tip: a reversal pattern applies equally to letters and digits.")
_add(T, 7, "Which one of the following is different? A. South-West, B. North-East, C. North-West, D. East-West, E. South-East",
     ["South-West", "North-East", "North-West", "East-West", "South-East"], 3,
     "South-West, North-East, North-West and South-East are the four intermediate (diagonal) directions. East-West is a pair of opposite cardinal directions, not a single direction.", "Tip: the four intermediate directions lie halfway between the cardinal points.")
_add(T, 8, "Which statement is correct? A. Two is equal to the difference between three and four, B. Two is less than the difference between three and four, C. Two is greater than the difference between three and four, D. Two may be less than or greater than the difference between three and four, E. None of the statement is correct",
     ["Two is equal to the difference between three and four", "Two is less than the difference between three and four", "Two is greater than the difference between three and four",
      "Two may be less than or greater than the difference between three and four", "None of the statement is correct"], 2,
     "The difference between three and four is 1, and 2 is greater than 1.", "Tip: calculate the quantity in the statement before comparing.")
_add(T, 9, "Which one of the following is different from the rest? A. House, B. Mountain, C. River, D. Forest, E. Sea",
     ["House", "Mountain", "River", "Forest", "Sea"], 0,
     "Mountain, river, forest and sea are natural features. A house is man-made.", "Tip: natural versus man-made is a common category split.")
_add(T, 10, "STUN is to NUTS as POTS is to?", ["SPOT", "STOP", "TOPS", "OPTS"], 1,
     "NUTS is STUN written backwards, so POTS reversed is STOP.", "Tip: spelling a word backwards often produces another real word.")
_add(T, 11, "About the word FLOWER which one of the following statement is true? A. O comes after L and E, B. E comes before R and W, C. L comes after E and before F, D. W is in the middle of R and L, E. None of the statement is correct",
     ["O comes after L and E", "E comes before R and W", "L comes after E and before F", "W is in the middle of R and L", "None of the statement is correct"], 3,
     "In F-L-O-W-E-R, L is 2nd and R is 6th, and W is 4th, so W lies between L and R. The other statements fail, for example E is after O and W.", "Tip: write out the letters with their positions before checking each statement.")
_add(T, 12, "EF is to DG as JK is to?", ["IL", "KJ", "HM", "LI"], 0,
     "E-1 = D and F+1 = G. Apply the same to JK: J-1 = I and K+1 = L.", "Tip: letters moving outward from the centre form a mirror-like pair pattern.")
_add(T, 13, "If a man goes 10 yards due north, then 10 yards due east, then 10 yards due south, then 10 yards due west, then: A. he is South of his starting place, B. he is north of his starting place, C. he has back to his starting place, D. he is south east of his starting place, E. he is west of his starting place",
     ["he is South of his starting place", "he is north of his starting place", "he has back to his starting place", "he is south east of his starting place", "he is west of his starting place"], 2,
     "North and south cancel out, and east and west cancel out, so he ends where he began.", "Tip: equal and opposite moves on each axis cancel.")
_add(T, 14, "What number when taken away from 12 gives 3 less than one-third of 27?", ["9", "3", "6", "4"], 2,
     "One-third of 27 is 9, and 3 less than 9 is 6. So 12 - x = 6, giving x = 6.", "Tip: break wordy questions into small steps.")
_add(T, 15, "Even is to Uneven as Violent is to: A. Aggressive, B. Friendly, C. Responsible, D. Sadest, E. Unkind",
     ["Aggressive", "Friendly", "Responsible", "Sadest", "Unkind"], 1,
     "Even and uneven are opposites, so we need the opposite of violent, and friendly (gentle) is the best match. Aggressive and unkind are similar to violent.", "Tip: identify whether the first pair is synonyms or antonyms.")
_add(T, 16, "Bird is to Cage as Prisoner is to: A. Chains, B. Court, C. Freedom, D. Cell, E. Police",
     ["Chains", "Court", "Freedom", "Cell", "Police"], 3,
     "A bird is kept in a cage and a prisoner is kept in a cell.", "Tip: this is an object and its place of confinement.")
_add(T, 17, "If A is as tall as D, C is shorter than A, B is taller than D, then: A. A is taller than B, B. C is as tall as D, C. B may be taller or shorter than C, D. C is shorter than D, E. B is shorter than A",
     ["A is taller than B", "C is as tall as D", "B may be taller or shorter than C", "C is shorter than D", "B is shorter than A"], 3,
     "A and D are equal in height and C is shorter than A, so C is shorter than D. Also B is taller than D, so B is taller than A as well.", "Tip: substitute equal items and chain the comparisons.")
_add(T, 18, "1/3 is to 9 as 1/2 is to:", ["2", "4", "8", "1/4"], 1,
     "1/3 becomes 9, which is the square of its reciprocal (3 squared). The reciprocal of 1/2 is 2, and 2 squared is 4.", "Tip: try squares, cubes and reciprocals for pairs that link a fraction to a whole number.")
_add(T, 19, "SPHERE is to CIRCLE as CUBE is to: A. Cuboid, B. Angle, C. Square, D. Point, E. None",
     ["Cuboid", "Angle", "Square", "Point", "None"], 2,
     "A sphere is the three-dimensional form of a circle, so the matching two-dimensional form of a cube is a square.", "Tip: the question prints SRHERE, which is a typing error for SPHERE.")
_add(T, 20, "If L is to 1, T is to 2, E is to 3, R is to 4, add up the digits for the word LETTER, divide the total by 5 and give the result as your answer.",
     ["2", "3", "4", "15"], 1,
     "LETTER = L1 + E3 + T2 + T2 + E3 + R4 = 15, and 15 divided by 5 = 3.", "Tip: write each letter's value under it before adding.")
_add(T, 21, "(2/4) is to (1:2) as (18/24) is to?", ["3:4", "9:12", "6:8", "2:3"], 0,
     "2/4 is reduced to its simplest ratio 1:2, so 18/24 in simplest form is 3:4.", "Tip: divide top and bottom by their highest common factor, here 6.")
_add(T, 22, "Which of the following words has P but not A, has E but not D, has C but not L, has O but not I? A. Possible, B. Police, C. Pagoda, D. Pocket, E. Please",
     ["Possible", "Police", "Pagoda", "Pocket", "Please"], 3,
     "POCKET has P, E, C and O, and has no A, D, L or I. Possible has no C, police has I, pagoda has A and D, and please has A.", "Tip: eliminate options one condition at a time.")
_add(T, 23, "What number when added to 14 gives 12 less than 30?", ["16", "18", "4", "2"], 2,
     "12 less than 30 is 18, so 14 + x = 18 and x = 4.", "Tip: compute the right-hand side first, then solve.")
_add(T, 24, "People smoke because: A. They get pleasure from it, B. They want to show off, C. It is a fashion these days, D. It makes them social, E. It is good for health",
     ["They get pleasure from it", "They want to show off", "It is a fashion these days", "It makes them social", "It is good for health"], 0,
     "The most common reason smokers give is the pleasure or relief they feel, driven by nicotine. Smoking is not good for health.", "Tip: smoking is a leading cause of lung cancer and heart disease worldwide.")
_add(T, 25, "Three men A, B, C are standing in a row so that A and C are standing to the left of B, and B and A are standing to the right of C. Who is standing in the middle? (the paper prints A and B in the first part, which is a typing slip for A and C)",
     ["B", "C", "A", "Cannot be determined"], 2,
     "A and C are left of B, so B is last. B and A are right of C, so C is first. That leaves A in the middle: C, A, B.", "Tip: draw a row and place each person using one clue at a time.")
_add(T, 26, "Which would be the middle letter if the letters of the word SUBORDINATE are arranged in an alphabetical order?", ["N", "O", "D", "I"], 0,
     "The 11 letters in order are A, B, D, E, I, N, O, R, S, T, U. The 6th (middle) letter is N.", "Tip: for 11 items the middle one is the 6th.")
_add(T, 27, "Nazar is 2/3 times younger than his elder brother. His brother Rab Nawaz is 21 years old, what is the age of Nazar?", ["7", "14", "31", "12"], 1,
     "Nazar's age is 2/3 of 21 = 14 years.", "Tip: 7 is one third of 21 and 14 is two thirds, so read the fraction carefully.")
_add(T, 28, "People buy cars: A. To sell them at profit, B. So that they reach places quickly",
     ["To sell them at profit", "So that they reach places quickly", "To pollute the environment"], 1,
     "The usual purpose of buying a car is transport, to reach places quickly and comfortably.", "Tip: choose the most common, general purpose in these items.")
_add(T, 29, "63 is to 9 as 71 is to?", ["7", "8", "10", "17"], 1,
     "63 gives 9 as the sum of its digits (6 + 3 = 9). So 71 gives 7 + 1 = 8.", "Tip: the digit-sum relation is common in number analogies.")
_add(T, 30, "FOUR is to ELEVEN as THREE is to?", ["TWELVE", "NINE", "TEN", "FIVE"], 2,
     "FOUR means 4 and ELEVEN means 11, which is 7 more. THREE means 3, and 3 + 7 = 10, which is TEN.", "Tip: convert number words into numbers before looking for the rule.")
_add(T, 31, "COMPARE is to 7324615 as OPERA is to?", ["34516", "34561", "43516", "34156"], 0,
     "C=7, O=3, M=2, P=4, A=6, R=1, E=5. So O=3, P=4, E=5, R=1, A=6, giving 34516.", "Tip: build a letter-to-digit table from the given word first.")
_add(T, 32, "If A is greater than B and B is less than C; then: A. A is equal to C, B. C is greater than A, C. A is greater than C, D. One cannot say whether A is equal to, greater than or less than C",
     ["A is equal to C", "C is greater than A", "A is greater than C", "One cannot say whether A is equal to, greater than or less than C"], 3,
     "Both A and C are greater than B, but nothing links A and C directly, so their order cannot be decided.", "Tip: two items that are both bigger than a third cannot be ranked against each other.")
_add(T, 33, "If the following are arranged in order of size, what would come in the middle? A. Book, B. Word, C. Chapter, D. Sentence, E. Paragraph",
     ["Book", "Word", "Chapter", "Sentence", "Paragraph"], 4,
     "In increasing order: word, sentence, paragraph, chapter, book. The middle one is paragraph.", "Tip: sort the full list first, then pick the centre item.")
_add(T, 34, "Which one of the following is different from the rest? A. KOOL, B. LOOM, C. NOOS, D. MOON, E. WOOX",
     ["KOOL", "LOOM", "NOOS", "MOON", "WOOX"], 2,
     "In KOOL, LOOM, MOON and WOOX the first and last letters are consecutive in the alphabet (K L, L M, M N, W X). In NOOS, N and S are not consecutive.", "Tip: look at the outer letters when the middle letters repeat.")
_add(T, 35, "You should not tell lies because: A. People will not trust you, B. You will always be found out, C. It is bad to do so, D. Truth is bitter, E. You will be punished",
     ["People will not trust you", "You will always be found out", "It is bad to do so", "Truth is bitter", "You will be punished"], 2,
     "The basic reason not to lie is moral: it is wrong. The other reasons are consequences that may or may not follow.", "Tip: the answer that states the principle is better than one that states a possible consequence.")
_add(T, 36, "What letter group comes next in the following series? JKLMNOPQ, JKLOPQ, JKPQ, ?", ["JQ", "JKQ", "JP", "KQ"], 0,
     "Each step removes the middle letters: JKLMNOPQ, JKLOPQ, JKPQ, then JQ.", "Tip: look at which letters disappear from the middle at each step.")
_add(T, 37, "If B and C are at equal distances from A, B is south-west of A and A is south-east of C, then: A. C is north of B, B. B is south east of C, C. A is north west of B, D. C is south west of A",
     ["C is north of B", "B is south east of C", "A is north west of B", "C is south west of A"], 0,
     "Put A at the centre: B is south-west and C is north-west (since A is south-east of C) at the same distance. So C lies directly north of B.", "Tip: draw a quick compass sketch with A at the origin.")
_add(T, 38, "Which one of the following is different? A. Teacher, B. Patient, C. Lawyer, D. Doctor, E. Medicine",
     ["Teacher", "Patient", "Lawyer", "Doctor", "Medicine"], 4,
     "Teacher, patient, lawyer and doctor are all people. Medicine is a thing.", "Tip: check for person versus thing.")
_add(T, 39, "Which one of the following is different? A. Lion, B. Wolf, C. Cat, D. Goat, E. Tiger",
     ["Lion", "Wolf", "Cat", "Goat", "Tiger"], 3,
     "Lion, wolf, cat and tiger are meat-eating (carnivorous) animals. A goat eats plants.", "Tip: diet is a useful category for animal odd-one-out questions.")
_add(T, 40, "GREEN is to GRASS, CLEAR is to: A. Crystal, B. Light, C. Dark, D. Close, E. Tone",
     ["Crystal", "Light", "Dark", "Close", "Tone"], 0,
     "Green is the typical colour of grass, and clear is the typical quality of crystal.", "Tip: this analogy links a quality to the thing most known for it.")

# ---------------- Test 20 ----------------
T = 20
_add(T, 1, "Re-arrange the letters ARTGN and find the middle letter.", ["R", "G", "A", "N"], 2,
     "ARTGN rearranges to GRANT, whose middle (third) letter is A.", "Tip: unscramble the word first, then count to the centre.")
_add(T, 2, "Which country is this, re-arranged: MERYGAN?", ["Germany", "Armenia", "Myanmar", "Gambia"], 0,
     "The letters of MERYGAN can be rearranged to form GERMANY.", "Tip: Berlin is the capital of Germany.")
_add(T, 3, "What is the last letter if DASAL is re-arranged?", ["L", "S", "A", "D"], 3,
     "DASAL rearranges to SALAD, so the last letter is D.", "Tip: try common words that use all of the given letters.")
_add(T, 5, "If the 7th of the month falls 2 days preceding Sunday, then what is the day which follows the 21st of the same month?", ["Friday", "Sunday", "Saturday", "Monday"], 2,
     "Two days before Sunday is Friday, so the 7th is a Friday. The 14th and 21st are also Fridays, so the day following the 21st is Saturday.", "Tip: dates 7 days apart fall on the same weekday.")
_add(T, 6, "How many letters are there after K and before T in the following series: AABKMXJTTC?", ["2", "4", "3", "5"], 2,
     "Between K and the first T come M, X and J, which is 3 letters.", "Tip: read the series positions and count only the letters between the two markers.")
_add(T, 7, "If three days later the day after tomorrow is Friday, then what was yesterday?", ["Friday", "Thursday", "Sunday", "Saturday"], 3,
     "The day after tomorrow is today + 2, and three days later is today + 5. If that is Friday, today is Sunday, so yesterday was Saturday.", "Tip: add up all the day shifts to find the offset from today.")
_add(T, 8, "If 25th December is Sunday then 25th January will be?", ["Tuesday", "Wednesday", "Thursday", "Monday"], 1,
     "There are 31 days from 25 December to 25 January and 31 = 4 x 7 + 3, so it is three days after Sunday, which is Wednesday.", "Tip: reduce the number of days to the remainder when divided by 7.")
_add(T, 9, "If 3 days after tomorrow is Wednesday, then what will be the day before yesterday?", ["Monday", "Tuesday", "Thursday", "Friday"], 2,
     "Three days after tomorrow is today + 4. If that is Wednesday, today is Saturday, so the day before yesterday is Thursday.", "Tip: find today first, then move backwards.")
_add(T, 10, "If 15th of February in a leap year is Sunday, then what will be the 15th of the next month?", ["Sunday", "Tuesday", "Monday", "Saturday"], 2,
     "February has 29 days in a leap year, so 15 March is 29 days later. 29 = 4 x 7 + 1, so it is one day after Sunday, which is Monday.", "Tip: a leap year has 366 days and a February with 29 days.")
_add(T, 11, "Arrange BROTHER in alphabetical order and then indicate the letter left of the middle letter.", ["E", "H", "O", "R"], 1,
     "In alphabetical order it is B, E, H, O, R, R, T. The middle (4th) letter is O and the letter to its left is H.", "Tip: with 7 letters the middle is the 4th.")
_add(T, 12, "Which letter is next to the middle letter between H and P?", ["K", "L", "N", "M"], 3,
     "From H to P the letters are H, I, J, K, L, M, N, O, P (9 letters). The middle one is L, and the letter next to it is M.", "Tip: count the letters including both ends before finding the middle.")
_add(T, 13, "It takes two minutes to boil an egg. How many minutes to boil 5 eggs together?", ["10 mins", "5 mins", "2 mins", "7 mins"], 2,
     "The eggs boil at the same time in the same pot, so 5 eggs together also take 2 minutes.", "Tip: some questions test whether a task scales with the number of items.")
_add(T, 14, "Amjad is taller than Asif, Akram is taller than Amjad. Who is the shortest?", ["Amjad", "Akram", "Asif", "Cannot say"], 2,
     "Akram is taller than Amjad, who is taller than Asif, so Asif is the shortest.", "Tip: write the names in order of height to see the shortest.")
_add(T, 15, "If Ali is brother of the son of Salman's son, what relation is Ali to Salman?", ["Son", "Nephew", "Grandson", "Brother"], 2,
     "Salman's son has a son, and Ali is that boy's brother, so Ali is also a son of Salman's son. That makes him Salman's grandson.", "Tip: work from the innermost relation outwards.")
_add(T, 16, "X and Y are brothers, B is A's brother but A is the mother of X, what is B to Y?", ["Father", "Brother", "Cousin", "Uncle"], 3,
     "A is the mother of X and Y, and B is her brother, so B is the maternal uncle of Y.", "Tip: your mother's brother is your maternal uncle (mama).")
_add(T, 17, "A husband and his wife have five married sons who have two children each. How many total family members are there?", ["12", "17", "22", "32"], 2,
     "Husband and wife are 2, five sons make 7, their five wives make 12, and 5 x 2 = 10 grandchildren make 22.", "Tip: do not forget the daughters-in-law when counting the family.")
_add(T, 18, "Today is Maria's birthday, one year after today she will be twice as old as she was 10 years ago. How old is she now?", ["22", "20", "21", "19"], 2,
     "Let her age now be x. Then x + 1 = 2(x - 10), so x + 1 = 2x - 20 and x = 21.", "Tip: the key sheet shows 22, but checking the equation gives 21.")
_add(T, 19, "A man walked 1 km towards south and then turned right and walked another 1 km, in which direction is he?", ["East", "North", "South", "West"], 3,
     "Facing south, his right hand points west, so after turning right he walks west.", "Tip: facing south, right is west and left is east.")
_add(T, 20, "Time on Ali's watch is quarter to three. If the hour hand is pointing towards east, then where is the minute hand pointing?", ["East", "North", "West", "South"], 2,
     "At quarter to three the hour hand is almost at 3 and points east, while the minute hand is at 9, exactly opposite, so it points west.", "Tip: the 3 and 9 on a clock face are opposite each other.")
_add(T, 21, "A man walked 10 m towards east and then 5 m to North and then 10 m towards West, how far is he from the starting point?", ["10 m", "25 m", "15 m", "5 m"], 3,
     "The east and west moves cancel, so only the 5 m north remains. He is 5 m from the start.", "Tip: opposite movements cancel on each axis.")
_add(T, 22, "If London is to Thames then Lahore is to ____?", ["Indus", "Chenab", "Ravi", "Jhelum"], 2,
     "The River Thames flows through London and the River Ravi flows by Lahore.", "Tip: the five rivers of Punjab are Jhelum, Chenab, Ravi, Beas and Sutlej.")
_add(T, 23, "If K-2 is mountain then Gobi is ____?", ["Desert", "Lake", "River", "Plateau"], 0,
     "K-2 is a mountain and the Gobi is a desert in Asia, mainly in Mongolia and northern China.", "Tip: K2 is the second highest mountain in the world.")
_add(T, 24, "Which one is different? Camel, Donkey, Bull, Mare", ["Camel", "Mare", "Donkey", "Bull"], 1,
     "Camel, donkey and bull are general or male animal names, while a mare is specifically a female horse.", "Tip: the key for this test chose mare as the odd one.")
_add(T, 25, "If a = 3, b = 4 and c = 5 then a squared + b squared + 2abc = ?", ["145", "49", "120", "125"], 0,
     "9 + 16 + 2 x 3 x 4 x 5 = 9 + 16 + 120 = 145.", "Tip: follow the order of operations and do the product 2abc before adding.")
_add(T, 26, "Smile: Glad then Sadness: ____?", ["Happy", "Gloomy", "Joyful", "Cheerful"], 1,
     "Glad is a word that goes with smile, so a word that goes with sadness is gloomy.", "Tip: this analogy matches a thing with a word of the same mood.")
_add(T, 27, "What comes next: 7/49, 6/36, ____, 4/16?", ["4/25", "5/30", "5/25", "5/20"], 2,
     "Each fraction is a number over its own square (7/49, 6/36, 4/16), so the missing one is 5/25.", "Tip: look at how the denominator relates to the numerator.")
_add(T, 28, "What is 30% of 30?", ["3", "9", "30", "90"], 1,
     "30 percent of 30 is 0.30 x 30 = 9.", "Tip: 10 percent of a number is that number divided by 10.")
_add(T, 29, "If straight: Curve then decent: ____?", ["Polite", "Honest", "Indecent", "Proper"], 2,
     "Straight and curve are opposites, so the opposite of decent is indecent (rude).", "Tip: the first pair tells you the relationship is antonyms.")
_add(T, 30, "Which is different: Triangle, Rectangle, Square, Circle?", ["Triangle", "Rectangle", "Square", "Circle"], 3,
     "Triangle, rectangle and square are polygons with straight sides. A circle is a curved shape with no sides.", "Tip: look for curved versus straight edges.")
