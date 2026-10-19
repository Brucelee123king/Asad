S = "Hakeem Force Academy"
DAYFACT = "Days: shift by the remainder after dividing the gap by 7 (going back in the month means subtract the remainder)."
def D(q, opts, a, why, rel, ex):
    return (S, q, opts, a, why, rel, ex)
W = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def day(q, opts, a, why, ex):
    return D(q, opts, a, why, DAYFACT, ex)
QS = [
# 2
day("If yesterday was Sunday, what day will be the day after tomorrow?", ["Tuesday", "Wednesday", "Thursday", "Monday"], 1,
    "Yesterday Sunday means today is Monday; the day after tomorrow is Monday + 2 = Wednesday.", 11),
# 3
day("If the 4th day of a month is Friday, what day will the 19th day be?", ["Friday", "Saturday", "Sunday", "Monday"], 1,
    "The gap is 19 - 4 = 15 days; 15 divided by 7 leaves 1, so Friday + 1 = Saturday.", 1637),
# 4
D("What is 90% of 90?", ["81", "80", "9", "89"], 0, "90% of 90 = 90 x 90 / 100 = 81.",
  "Shortcut: x% of y equals y% of x, so 90% of 90 is 9 x 9 = 81.", 0),
# 5
D("What is one third of 10% of 90?", ["3", "9", "30", "2"], 0, "10% of 90 = 9, and one third of 9 = 3.",
  "10% of a number: move the decimal point one place to the left.", -1),
# 6
D("What is one third of 10% of 120?", ["12", "4", "3", "40"], 1, "10% of 120 = 12, and one third of 12 = 4.",
  "Work from the inside out: first the percentage, then the fraction.", 260),
# 7
D("How many months of a year have 31 days?", ["Six", "Seven", "Five", "Eight"], 1,
  "January, March, May, July, August, October and December have 31 days, so there are seven.",
  "Knuckle trick: every knuckle is a 31-day month and every gap is a shorter month (July and August are both 31).", 5),
# 8
D("If 1 man writes 5 papers in 5 minutes, how long will 1 man take to write 1 paper?", ["5 minutes", "1 minute", "25 minutes", "10 minutes"], 1,
  "1 man writes 5 papers in 5 minutes, so he writes 1 paper per minute.",
  "Rate = work divided by time; find the rate of one worker first.", 1633),
# 9
D("Out of 500 students, 360 are boys. What is the percentage of girls?", ["28%", "72%", "36%", "14%"], 0,
  "Girls = 500 - 360 = 140; 140 / 500 x 100 = 28%.",
  "Percentage = part / total x 100; for a part of 500, divide the part by 5.", 685),
# 10
D("What is the value of 2 + 2/2?", ["3", "2", "4", "1"], 0, "Division comes first: 2/2 = 1, then 2 + 1 = 3.",
  "BODMAS: Brackets, Orders, Division and Multiplication, then Addition and Subtraction.", 3),
# 11
D("What is a quarter of one tenth of 120?", ["3", "30", "12", "4"], 0, "One tenth of 120 = 12, and a quarter of 12 = 3.",
  "Quarter of a number is the number divided by 4; one tenth is divided by 10.", 9),
# 12
D("There are 30 passengers in a bus and 2/3 of them are men. What is the percentage of women?", ["66.67%", "33.33%", "20%", "10%"], 1,
  "Men = 20, women = 10; 10 / 30 x 100 = 33.33%.",
  "If 2/3 is one group, the rest is 1/3, which is 33.33%.", 1539),
# 13
D("Ali bought a pen for Rs 30 and sold it for Rs 40. What is the profit percentage?", ["10%", "25%", "33.33%", "40%"], 2,
  "Profit = 40 - 30 = 10; profit % = 10 / 30 x 100 = 33.33%.",
  "Profit % is always calculated on the cost price, not the selling price.", 20),
# 14a
D("Point out the odd one out: Angle, Rectangle, Square, Hexagon.", ["Angle", "Rectangle", "Square", "Hexagon"], 0,
  "Rectangle, square and hexagon are closed shapes (polygons); an angle is not a shape.",
  "In odd-one-out questions, find the property that three items share.", 1461),
# 14b
D("Which one is different: Cricket, Football, Tennis, Baseball?", ["Cricket", "Football", "Tennis", "Baseball"], 1,
  "Cricket, tennis and baseball are played with a bat or racket; football is mainly played with the foot.",
  "Look for the equipment or the way the game is played.", 1517),
# 14c
D("Point out the odd one out: Wheat, Hay, Rice, Barley.", ["Wheat", "Hay", "Rice", "Barley"], 1,
  "Wheat, rice and barley are food grains for humans; hay is dried grass used as animal fodder.",
  "Group by use: grains for food versus fodder.", 1684),
# 14d
D("Which one is different from the others: Monkey, Ape, Chimpanzee, Panda, Baboon?", ["Monkey", "Ape", "Panda", "Baboon"], 2,
  "Monkey, ape, chimpanzee and baboon are primates; the panda is a bear.",
  "Primates include monkeys, apes, baboons and humans.", -1),
# 14e
D("Point out the odd one out: America, Africa, Asia, Euro.", ["America", "Africa", "Asia", "Euro"], 3,
  "America, Africa and Asia are continents; the Euro is a currency (the continent is Europe).",
  "There are seven continents: Asia, Africa, North America, South America, Antarctica, Europe and Australia.", 1963),
# 15
day("If the 4th day of a month is Tuesday, what day will the 26th day be?", ["Tuesday", "Wednesday", "Thursday", "Monday"], 1,
    "The gap is 26 - 4 = 22 days; 22 divided by 7 leaves 1, so Tuesday + 1 = Wednesday.", 1638),
# 16
D("There are 30 passengers in a bus and 2/3 of them are men. How many women are there?", ["20", "15", "10", "5"], 2,
  "Men = 2/3 of 30 = 20, so women = 30 - 20 = 10.",
  "Find the fraction of the other group as 1 minus the given fraction.", 4932),
# 17
D("A man walked towards the north, then turned left. After some time he turned right. What is his present direction?", ["North", "West", "East", "South"], 0,
  "North, then left gives West, then right from West gives North.",
  "Left turn: N to W to S to E. Right turn: N to E to S to W.", 259),
# 18a
D("Complete the series: 115, 55, 170, 65, 235, ?", ["70", "75", "85", "80"], 1,
  "Two series are mixed: 115, 170, 235 (add 55, then 65) and 55, 65, 75 (add 10), so the missing term is 75.",
  "If a series looks random, separate the alternate terms into two series.", 1415),
# 18b
D("Complete the series: 66, 63, 57, 45, ?", ["33", "21", "27", "25"], 1,
  "The differences are 3, 6, 12 (doubling), so the next difference is 24 and 45 - 24 = 21.",
  "Check differences first; if they double, the series is a doubling-difference series.", 1513),
# 18c
D("Complete the series: 2, 6, 14, 30, 62, ?", ["94", "124", "126", "120"], 2,
  "Each term is double the previous plus 2: 62 x 2 + 2 = 126.",
  "Terms are 2^n - 2 for n = 2, 3, 4...: 4-2, 8-2... so after 62 (64-2) comes 128-2 = 126.", 700),
# 18d
D("Complete the series: B, E, J, Q, ?", ["X", "Y", "Z", "W"], 2,
  "Letter positions are 2, 5, 10, 17 with gaps 3, 5, 7, so the next gap is 9 and 17 + 9 = 26 = Z.",
  "Letter series: convert letters to numbers (A=1 ... Z=26) and study the gaps.", 1564),
# 18e
D("Complete the series: A, C, F, J, O, ?", ["T", "U", "V", "S"], 1,
  "Positions are 1, 3, 6, 10, 15 (gaps 2, 3, 4, 5), so the next gap is 6 and 15 + 6 = 21 = U.",
  "Gaps that increase by 1 are the triangular numbers 1, 3, 6, 10, 15, 21.", 384),
# 18f
D("Complete the series: L, M, N, ?", ["P", "O", "Q", "K"], 1,
  "The letters are consecutive in the alphabet, so after N comes O.",
  "Simple consecutive series go forward one letter at a time.", 1654),
# 19
day("If the 4th day of a month is Sunday, what day will the 19th day be?", ["Sunday", "Tuesday", "Monday", "Saturday"], 2,
    "The gap is 15 days; 15 divided by 7 leaves 1, so Sunday + 1 = Monday.", 5049),
# 20
day("If the 14th day of a month is Sunday, what day will the 4th day be?", ["Wednesday", "Thursday", "Friday", "Tuesday"], 1,
    "The gap is 10 days backwards; 10 divided by 7 leaves 3, so Sunday - 3 = Thursday.", -1),
# 21a
D("Why do parents give education to their children?", ["To groom them", "To keep them busy", "To make them tired", "To get them married"], 0,
  "Education develops and grooms a child into a capable and responsible person.",
  "In such questions choose the most natural and purposeful answer.", 4013),
# 21b
D("Why do we boil milk?", ["To make it sweet", "To kill germs", "To make it cold", "To make it thick"], 1,
  "Boiling kills harmful germs (bacteria), making the milk safe to drink.",
  "Pasteurisation is a similar heating process used for packaged milk.", 1),
# 22
day("If yesterday was Friday, what day will be the day after tomorrow?", ["Sunday", "Monday", "Tuesday", "Friday"], 1,
    "Yesterday Friday means today is Saturday; the day after tomorrow is Saturday + 2 = Monday.", 14),
# 23
D("A train's speed is twice that of a car. If the car covers 60 km in one hour, how much distance will the train cover in 30 minutes?", ["30 km", "60 km", "120 km", "90 km"], 1,
  "Train speed = 2 x 60 = 120 km/h; in 30 minutes (half an hour) it covers 60 km.",
  "Distance = speed x time; convert minutes into hours first.", 4032),
# 24a
D("A bat cannot see; a snake cannot what?", ["Hear", "Smell", "Crawl", "Taste"], 0,
  "A snake has no outer ears and cannot hear airborne sound well, so the answer is hear (note: in reality a bat can see; it also uses echolocation).",
  "Snakes sense vibrations through the ground and use their tongue to smell.", 100),
# 24b
D("What is the sound made by an eagle called?", ["Scream", "Roar", "Bark", "Hoot"], 0,
  "The call of an eagle is described as a scream.",
  "Other animal sounds: lion roars, owl hoots, dog barks.", 562),
# 25
D("What is half of 9/90?", ["1/5", "0.05", "0.5", "0.2"], 1,
  "9/90 = 0.1, and half of 0.1 = 0.05 = 1/20 (so the source statement of 1/5 or 0.2 is wrong).",
  "Simplify the fraction first: 9/90 = 1/10.", -1),
# 26
D("In a class of 1500 students, 1200 are present. What is the percentage of absent students?", ["80%", "25%", "20%", "30%"], 2,
  "Absent = 1500 - 1200 = 300; 300 / 1500 x 100 = 20%.",
  "Present % + absent % = 100%, so 80% present means 20% absent.", 1472),
# 27
D("My brother's sister is your mother. Taking me as a male, what am I to you?", ["Father", "Uncle", "Nephew", "Grandfather"], 1,
  "My brother's sister is my own sister, and she is your mother, so I am your mother's brother, that is, your maternal uncle.",
  "Brother's sister means own sister (or oneself if female).", 190),
# 28
day("If the 1st day of a month is Monday, what day will the 12th day be?", ["Thursday", "Saturday", "Friday", "Sunday"], 2,
    "The gap is 11 days; 11 divided by 7 leaves 4, so Monday + 4 = Friday (the source statement of Saturday is wrong).", 785),
# 29
D("If 5 men write 5 pages in 5 minutes, how long will 1 man take to write 1 page?", ["1 minute", "5 minutes", "25 minutes", "10 minutes"], 1,
  "Each man writes 1 page in 5 minutes (5 men write 5 pages in the same 5 minutes).",
  "When workers and work are equal, each worker does one unit in the given time.", 1910),
# 30
D("A train's speed is double that of a car, and the car travels 30 km in 1 hour. How much distance will the train cover in 30 minutes?", ["15 km", "30 km", "60 km", "45 km"], 1,
  "Train speed = 2 x 30 = 60 km/h; in half an hour it covers 30 km.",
  "Distance = speed x time; 30 minutes is half an hour.", 1780),
# 31
D("If a man travels 90 km in 1 hour and 40 minutes, in how many minutes will he cover 1 km?", ["0.9 minute", "1.11 minutes", "1 minute", "1.5 minutes"], 1,
  "Time is 100 minutes for 90 km, so 1 km takes 100 / 90 = 1.11 minutes (the source value 0.9 is wrong).",
  "Minutes per km = total minutes / total km.", 2440),
# 32
D("What is 80% of 90?", ["72", "70", "75", "8"], 0, "80% of 90 = 80 x 90 / 100 = 72.",
  "80% = 4/5, and 4/5 of 90 = 72.", 1745),
# 33
D("In a classroom, out of 1500 students 1200 are present. What is the percentage of present students?", ["20%", "75%", "80%", "85%"], 2,
  "1200 / 1500 x 100 = 80%.",
  "Simplify first: 1200/1500 = 4/5 = 80%.", 4),
# 34
day("If the 2nd day of a month is Monday, what day will the 12th day be?", ["Wednesday", "Friday", "Thursday", "Saturday"], 2,
    "The gap is 10 days; 10 divided by 7 leaves 3, so Monday + 3 = Thursday (the source statement of Friday is wrong).", 786),
# 36
day("If the 2nd day of a month is Sunday, what day will the 23rd day be?", ["Sunday", "Monday", "Saturday", "Friday"], 0,
    "The gap is 21 days, which is exactly 3 weeks, so the day stays Sunday.", -1),
# 37
D("What is the value of (2 + 2)?", ["4", "8", "6", "2"], 0, "Adding the numbers in the bracket gives 2 + 2 = 4 (the source statement of 8 is wrong).",
  "Brackets are solved first.", -1),
# 38
D("What is one third of 120?", ["30", "60", "40", "36"], 2, "120 / 3 = 40.", "A third is the number divided by 3.", 417),
# 39
D("If one dozen pencils cost Rs 27, what is the price of 4 pencils?", ["Rs 9", "Rs 6", "Rs 12", "Rs 7"], 0,
  "One dozen = 12 pencils; price of 1 pencil = 27 / 12 = 2.25; 4 pencils = Rs 9.",
  "4 pencils is a third of a dozen, so the price is a third of 27.", 2475),
# 40
D("Ali moves towards the north, after some time he turns left, then turns left again. What is his present direction?", ["East", "West", "South", "North"], 2,
  "North, then left gives West, then left again gives South.",
  "Two left turns make a U-turn (opposite direction).", 377),
# 41
D("Out of 500 students, 340 are present. What is the percentage of absent students?", ["68%", "32%", "34%", "40%"], 1,
  "Absent = 500 - 340 = 160; 160 / 500 x 100 = 32%.",
  "Present is 68%, so absent is 100 - 68 = 32%.", 10),
# 42
D("A train is moving at a speed of 90 km/h. How much distance will it cover in 12 minutes?", ["15 km", "18 km", "20 km", "12 km"], 1,
  "12 minutes = 1/5 hour; 90 / 5 = 18 km.",
  "Convert minutes to hours: 12 minutes is 1/5 of an hour.", 271),
# 43
D("A man covers 20 km in one hour and 40 minutes. In how many minutes will he cover 1 km?", ["0.2 minute", "5 minutes", "4 minutes", "2 minutes"], 1,
  "Total time is 100 minutes for 20 km, so 1 km takes 100 / 20 = 5 minutes (the source value 0.2 is wrong).",
  "1 hour 40 minutes = 100 minutes.", 1704),
# 44
day("If the 15th day of a month is Monday, what day will the 4th day be?", ["Wednesday", "Thursday", "Friday", "Tuesday"], 1,
    "The gap is 11 days backwards; 11 divided by 7 leaves 4, so Monday - 4 = Thursday.", 5214),
# 45
D("In a class of 24 students, 1/4 are male. What is the percentage of females?", ["25%", "75%", "66.67%", "80%"], 1,
  "Males = 24 / 4 = 6, females = 18; 18 / 24 x 100 = 75%.",
  "If 1/4 are male, then 3/4 = 75% are female.", 1471),
# 46
D("A man walks towards the north, then turns left, then turns right. What is his present direction?", ["West", "East", "North", "South"], 2,
  "North, left gives West, then right from West gives North again.",
  "A left turn followed by a right turn returns to the original direction.", 259),
# 47
D("What will be the third letter when the word AUGMENTED is arranged alphabetically?", ["D", "E", "G", "A"], 1,
  "Alphabetical order: A, D, E, E, G, M, N, T, U; the third letter is E.",
  "Write the letters in order and count carefully; repeated letters count twice.", 1983),
# 48
D("An aeroplane flies in the air mainly because of which force?", ["Lift", "Gravity", "Friction", "Magnetism"], 0,
  "The shape of the wings produces lift, which overcomes weight so the aeroplane flies.",
  "Four forces on a plane: lift, weight, thrust and drag.", 4182),
# 49
D("Vehicle is to wheels as sound is to what?", ["Waves", "Speakers", "Echo", "Silence"], 0,
  "A vehicle moves on wheels, and sound travels as waves.",
  "Analogy questions: find the relationship in the first pair and apply it to the second.", 3357),
# 50
D("After how many years does a leap year normally come?", ["2 years", "3 years", "4 years", "5 years"], 2,
  "A leap year (366 days) comes every 4 years, for example 2024 and 2028.",
  "Century years are leap years only if divisible by 400.", 797),
]
