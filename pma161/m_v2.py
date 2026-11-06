S = "Hakeem Force Academy"
QS = []
def add(q, opts, ans, why, rel, ex=-1):
    QS.append((S, q, list(opts), opts.index(ans), why, rel, ex))

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
DAYFACT = "Days: shift by the remainder after dividing the gap between the two dates by 7 (gap 7, 14, 21 gives the same day)."
def dayopts(correct):
    i = DAYS.index(correct)
    return [DAYS[(i + k) % 7] for k in (0, 1, 3, 5)]

def dayq(d1, w1, d2, ex, printed_ok=True, printed=None):
    gap = d2 - d1
    r = gap % 7
    i = DAYS.index(w1)
    c = DAYS[(i + r) % 7] if gap >= 0 else DAYS[(i + r) % 7]
    why = "The gap is %d days and %d mod 7 = %d, so the day moves %d step(s) ahead of %s, which gives %s." % (abs(gap), abs(gap), abs(gap) % 7, r, w1, c) if gap >= 0 else "The 2nd date is %d days earlier; %d mod 7 = %d, so go back %d day(s) from %s (same as %d ahead), which gives %s." % (-gap, -gap, (-gap) % 7, (-gap) % 7, w1, r, c)
    if not printed_ok:
        why += " The source statement (%s) is wrong." % printed
    o = dayopts(c)
    # shuffle deterministically
    k = (d1 + d2) % 4
    o = o[k:] + o[:k]
    add("If the %s day of a month is %s, what day will the %s day be?" % (ordn(d1), w1, ordn(d2)), o, c, why, DAYFACT, ex)

def ordn(n):
    if 10 <= n % 100 <= 20: s = "th"
    else: s = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return "%d%s" % (n, s)

# 51
add("A train covers 120 km in 1 hour and 40 minutes. How much distance will it cover in 15 minutes (at the same speed)?",
    ["18 km", "30 km", "20 km", "15 km"], "18 km",
    "1 hour 40 minutes = 100 minutes, so speed = 120/100 = 1.2 km per minute; in 15 minutes: 1.2 x 15 = 18 km. The printed answer 30 km in the source is wrong.",
    "Find the speed per minute first, then multiply by the minutes.")
# 52
add("If yesterday was Friday, what day will tomorrow be?", ["Sunday", "Saturday", "Monday", "Friday"], "Sunday",
    "Yesterday Friday means today is Saturday, so tomorrow is Sunday.",
    "Yesterday, today and tomorrow are three consecutive days; tomorrow is 2 days after yesterday.")
# 53
dayq(4, "Sunday", 14, -1, False, "14th is Monday")
# 54
add("A car is moving at 120 km/h. How much distance does it cover in 10 minutes?", ["20 km", "12 km", "10 km", "30 km"], "20 km",
    "10 minutes = 1/6 hour, and 120 x 1/6 = 20 km.", "Km per minute = km/h divided by 60 (120 km/h = 2 km per minute).")
# 55
add("What is 120 x 7?", ["840", "780", "820", "860"], "840", "120 x 7 = 12 x 7 x 10 = 84 x 10 = 840.",
    "Multiply the non-zero part first, then add the zero back.", 2234)
# 56
dayq(28, "Monday", 8, 1954)
# 57
add("A man walks 20 km in 1 hour and 40 minutes. How much time will he take to cover 1 km?", ["5 minutes", "4 minutes", "6 minutes", "8 minutes"], "5 minutes",
    "100 minutes / 20 km = 5 minutes per km.", "Time per km = total time divided by total km.", 1704)
# 58
add("Ahmad walks towards the north and then turns left. In which direction is he facing now?", ["West", "East", "South", "North"], "West",
    "Facing north, the left hand side is west.", "Facing north: left is west, right is east. Facing south: left is east, right is west.", 2203)
# 59
dayq(2, "Friday", 23, 1434)
# 60
add("Ali is 5 years old and his sister Sidra is twice his age. How old will Sidra be when Ali is 11 years old?", ["16 years", "22 years", "18 years", "14 years"], "16 years",
    "Sidra is 10 now, so she is 5 years older than Ali. When Ali is 11, Sidra is 11 + 5 = 16.",
    "The age difference between two people never changes.")
# 61
dayq(1, "Monday", 13, 671)
# 62
add("What is a quarter of 120?", ["30", "40", "25", "60"], "30", "120 / 4 = 30.", "A quarter is 25 percent, and half of a half.", 383)
# 63
add("In a class of 500 students, 340 are boys. What percentage are boys?", ["68%", "60%", "70%", "34%"], "68%",
    "340/500 x 100 = 68%.", "Percentage = part/total x 100; out of 500, each student is 0.2 percent.", 1840)
# 64
add("If 1 dozen pencils cost Rs 60, what is the cost of 5 pencils?", ["Rs 25", "Rs 30", "Rs 20", "Rs 12"], "Rs 25",
    "1 dozen = 12 pencils, so one pencil costs 60/12 = Rs 5; 5 pencils cost Rs 25.", "One dozen = 12, a half dozen = 6, a gross = 144.", 2474)
# 65
add("A train covers 120 km in one hour. How much distance will it cover in 12 minutes?", ["24 km", "20 km", "12 km", "30 km"], "24 km",
    "12 minutes = 1/5 hour, and 120/5 = 24 km.", "12 minutes is one fifth of an hour.", 2437)
# 66
add("After arranging the letters of RAPISS, it becomes the name of a country, city, ocean or state. Which one is it?", ["City", "Country", "Ocean", "State"], "City",
    "The word is a scrambled PARIS (the extra S in the source spelling is a typo), the capital city of France. So it is a city.",
    "Anagram questions: look for a familiar name first, then check that every letter is used.")
# 67
add("Dog is to bitch as horse is to what?", ["Mare", "Foal", "Stallion", "Filly"], "Mare",
    "A bitch is a female dog; the female horse is a mare.", "Male horse: stallion; young horse: foal; young female: filly.", 2040)
# 68
dayq(4, "Monday", 18, -1)
# 71
dayq(2, "Friday", 14, 1430)
# 72
add("What will be the last letter of UTYEAB after arranging its letters alphabetically?", ["Y", "U", "T", "E"], "Y",
    "Alphabetical order is A, B, E, T, U, Y, so the last letter is Y.", "Letters of the alphabet end with Z; Y is the later of the letters U, T, E, A, B, Y.", 1406)
# 73
add("What will be the 3rd letter of the word Managment when its letters are arranged alphabetically?", ["E", "G", "A", "M"], "E",
    "Letters of Managment: A, A, E, G, M, M, N, N, T in alphabetical order, so the 3rd letter is E. The source answer G is wrong (G is 4th). The same answer E applies to the correctly spelled MANAGEMENT.",
    "Write the letters in order, keeping repeated letters, and count carefully.", 788)
# 74
add("A person purchased a book for Rs 500 and sold it for Rs 700. What is the profit percentage?", ["40%", "28.5%", "20%", "30%"], "40%",
    "Profit = 200; profit % = 200/500 x 100 = 40%.", "Profit % is always calculated on the cost price.", 1395)
# 75
add("What is one tenth of 90?", ["9", "90", "0.9", "10"], "9", "90/10 = 9.", "One tenth means divide by 10, which moves the decimal one place left.", 196)
# 76
add("What is one tenth of 120?", ["12", "1.2", "10", "120"], "12", "120/10 = 12.", "One tenth means divide by 10, which moves the decimal one place left.", 50)
# 77
add("If yesterday was Monday, what day will be the day after tomorrow?", ["Thursday", "Wednesday", "Friday", "Tuesday"], "Thursday",
    "Yesterday Monday means today is Tuesday; tomorrow is Wednesday and the day after tomorrow is Thursday.",
    "Day after tomorrow is 3 days after yesterday.")
# 78
add("If a helicopter needs 50 gallons of fuel to move 320 km, how many gallons will it need to move 400 km?", ["62.5 gallons", "60 gallons", "64 gallons", "55 gallons"], "62.5 gallons",
    "Fuel per km = 50/320; for 400 km: 50 x 400/320 = 62.5 gallons.", "Direct proportion: more distance needs proportionally more fuel.", 1811)
# 79
add("Amjad and Ahmad kept 24 balls together. Amjad kept 3 times as many as Ahmad. How many balls did Ahmad keep?", ["6", "8", "12", "4"], "6",
    "Let Ahmad have x; Amjad has 3x, so 4x = 24 and x = 6.", "For a ratio 1:3 the total has 4 parts; divide the total by 4.", 1851)
# 80
add("A boy is 3 years old and his sister is 3 times his age. How old will his sister be when the boy is 11 years old?", ["17 years", "33 years", "20 years", "14 years"], "17 years",
    "The sister is 9 now, so she is 6 years older. When the boy is 11, she is 17.", "The age difference stays constant.", 781)
# 81
add("What is 20% of one tenth of 90?", ["1.8", "18", "0.18", "9"], "1.8", "One tenth of 90 = 9; 20% of 9 = 1.8.", "20% is one fifth, so divide by 5.", 2881)
# 82
add("What is the sister of my brother's son to me?", ["Niece", "Aunt", "Cousin", "Nephew"], "Niece",
    "My brother's son's sister is my brother's daughter, who is my niece.", "Brother's or sister's son is a nephew; daughter is a niece.", 1921)
# 83
add("A boy has an average of 50 marks in 5 tests. How many marks must he score in the 6th test to raise his average to 70?", ["170", "120", "70", "100"], "170",
    "Total of 5 tests = 250. Total needed for 6 tests = 70 x 6 = 420. Next test = 420 - 250 = 170 (not possible if each test is out of 100, but this is the mathematical answer).",
    "Needed score = new average x number of tests minus the current total.", 2341)
# 84
add("My age is 10 years and my brother is 2 times my age. What will be the ratio of my age to my brother's age after 10 years?", ["2:3", "3:2", "1:2", "1:1"], "2:3",
    "Brother is 20 now. After 10 years I am 20 and he is 30, so the ratio is 20:30 = 2:3 (the reverse order gives 3:2).",
    "Add the same years to both ages before finding the ratio; never add years to the ratio itself.", 2793)
# 85
dayq(3, "Friday", 23, 2251)
# 86
add("Ali is 5 years old and his sister is 3 times his age. What will be the age of his sister when Ali is 10 years old?", ["20 years", "25 years", "30 years", "15 years"], "20 years",
    "The sister is 15 now, so she is 10 years older than Ali. When Ali is 10, she is 20.", "The age difference stays constant.", 2551)
# 87
dayq(4, "Tuesday", 12, -1)
# 88
add("Saleem has an average of 60 in 4 subjects. His average drops to 58 after the next test. How many marks did he score in that test?", ["50", "48", "52", "58"], "50",
    "Total of 4 = 240. Total of 5 = 58 x 5 = 290. Next test = 290 - 240 = 50. (The source asks to find the grade; the marks are the only value that can be worked out.)",
    "New test marks = new average x new count minus old total.", 5593)
# 89
add("10 men dig a well in 5 days. How many days will 5 men take to dig it?", ["10 days", "20 days", "5 days", "2.5 days"], "10 days",
    "Work = 10 x 5 = 50 man-days; with 5 men: 50/5 = 10 days. The source answer 20 is wrong.", "Fewer men take proportionally more days (inverse proportion): men x days = constant.", 2921)
# 90
add("Salman is 4 years old and Ali's age is twice Salman's age. What will be Ali's age when Salman is 12 years old?", ["16 years", "24 years", "20 years", "12 years"], "16 years",
    "Ali is 8 now, 4 years older than Salman. When Salman is 12, Ali is 16.", "The age difference stays constant.", 2901)
# 91
add("Akbar is older than Ahmad. Umair is older than Akbar. Who is the eldest?", ["Umair", "Akbar", "Ahmad", "Cannot be said"], "Umair",
    "Order from eldest: Umair, Akbar, Ahmad.", "Write the names in a line from oldest to youngest to solve ranking questions.", 2482)
# 92
add("Adil is 5 years old and his sister is 3 times his age. What will be the age of his sister when Adil is 15 years old?", ["25 years", "45 years", "30 years", "20 years"], "25 years",
    "Sister is 15 now, 10 years older than Adil. When Adil is 15, she is 25.", "The age difference stays constant.", 2181)
# 93
add("What is 80% of 80?", ["64", "60", "72", "80"], "64", "80% of 80 = 0.8 x 80 = 64.", "80% = 4/5, so divide by 5 and multiply by 4.", 691)
# 94
add("What is 90% of 70?", ["63", "61", "65", "7"], "63", "90% of 70 = 70 - 10% of 70 = 70 - 7 = 63.", "90% = whole minus 10 percent.", 261)
# 95
add("Write the word formed from the numbers 18, 5, 19, 20 (A=1, B=2, and so on).", ["REST", "RENT", "REAT", "PEST"], "REST",
    "18 = R, 5 = E, 19 = S, 20 = T, so the word is REST.", "Position shortcuts: A=1, E=5, J=10, O=15, T=20, Z=26.", 698)
# 96
add("The sister of my brother is your mother. What is your relation to me?", ["Nephew or niece", "Uncle", "Cousin", "Brother"], "Nephew or niece",
    "My brother's sister is my sister (taking me as male), and she is your mother, so I am your mother's brother and you are my nephew or niece.",
    "Your mother's brother is your maternal uncle; his children's relation to you is cousin, and you are his nephew or niece.")
# 97
add("Adnan walks 10 meters towards the north, then towards the south. After this he turns back and then turns left. In which direction is he facing now?", ["West", "East", "North", "South"], "West",
    "After walking south he faces south; turning back he faces north; turning left from north he faces west.", "Turning back means a 180 degree turn; left of north is west.", 5478)
# 98
add("A train covers 20 km in one hour. How much distance does it cover in 1 minute?", ["1/3 km (about 0.33 km)", "0.2 km", "0.5 km", "3 km"], "1/3 km (about 0.33 km)",
    "20 km / 60 minutes = 1/3 km = 0.333 km. The printed answer 0.3 km is only a rounded value.", "Km per minute = km/h divided by 60.", 2694)
# 99
add("What is 60% of 9?", ["5.4", "6.4", "5", "54"], "5.4", "60% of 9 = 0.6 x 9 = 5.4.", "60% = 3/5, so 9 x 3 / 5 = 5.4.", 3994)
# 100
add("What is 80% of 10?", ["8", "80", "0.8", "7"], "8", "80% of 10 = 0.8 x 10 = 8.", "Percent of 10: move the decimal one place and multiply (10% of 10 = 1).")
