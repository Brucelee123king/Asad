# 105 Verbal Repeated Questions by Pro Genius Students (PDF: progenius/v105/src.pdf)
# The PDF gives only the question and the answer. Options were written here; every answer was
# re-worked by hand. PDF mistakes fixed: Q26 (21 not 24), Q46 (S not R, same as Q42), Q55 (Friday not
# Saturday), Q93 (D not E). Q72 had no answer (60 km). Output: progenius/pv_final.json
import json, os
SEC = '105 Verbal by PGS'
Q = []
def q(text, opts, ans, why, rel):
    assert ans in opts, (text, ans)
    Q.append([SEC, text, opts, opts.index(ans), why, rel, 1])

# Age problems
q("If Ali's present age is 5 years and Sidra is twice Ali's age, what will be Sidra's age when Ali is 11 years old?", ['22', '16', '15', '18'], '16',
  "Sidra is 10 now, so she is 5 years older than Ali. When Ali is 11, Sidra is 11 + 5 = 16. The age difference never changes, so 22 (double of 11) is wrong.",
  "In age questions, first find the age difference: it stays the same for life.")
q("A boy is 3 years old and his sister is 3 times his age. What will be his sister's age when the boy is 11?", ['33', '17', '19', '14'], '17',
  "Sister is 9, which is 6 years more than the boy. When he is 11 she is 11 + 6 = 17. 33 (3 x 11) is wrong because the 'times' rule is only true today.",
  "Age ratios change every year, but the difference in years stays fixed.")
q("My age is 10 years and my brother is 2 times my age. What will be the ratio of our ages after 10 years?", ['1:2', '2:3', '3:4', '2:1'], '2:3',
  "Now: 10 and 20. After 10 years: 20 and 30. 20 : 30 = 2 : 3. 1:2 is today's ratio, not the ratio after 10 years.",
  "Add the same years to both ages before making the ratio.")
q("Ali is 5 years old and his sister is 3 times his age. What will be his sister's age when Ali is 10?", ['30', '20', '25', '15'], '20',
  "Sister is 15, so she is 10 years older. When Ali is 10 she is 10 + 10 = 20. 30 (3 x 10) wrongly keeps the 'times' rule.",
  "Age difference = 15 - 5 = 10 years, and it never changes.")
q("Salman is 4 years old and Ali is twice Salman's age. When Salman is 12, what will be Ali's age?", ['24', '16', '20', '14'], '16',
  "Ali is 8, so he is 4 years older. When Salman is 12, Ali is 12 + 4 = 16. 24 wrongly doubles 12.",
  "Twice the age is true only today; the gap of 4 years stays.")
q("Adil is 5 years old and his sister is 3 times his age. What will be his sister's age when Adil is 15?", ['45', '25', '30', '20'], '25',
  "Sister is 15, so she is 10 years older. When Adil is 15 she is 15 + 10 = 25. 45 (3 x 15) is wrong.",
  "Always add the fixed age gap to the new age.")
# Direction sense
q("A man walked towards North, then turned left. After some time he turned right. What is his present direction?", ['West', 'North', 'East', 'South'], 'North',
  "From North a left turn faces West; a right turn from West faces North again.",
  "A left turn and then a right turn cancel each other.")
q("Ali moves towards North. After some time he turns left and then again turns left. What is his present direction?", ['West', 'East', 'South', 'North'], 'South',
  "North, left = West, left again = South. Two left turns make a U-turn.",
  "Two turns in the same direction (left-left or right-right) = facing the opposite way.")
q("A man walks towards North, then turns left, then turns right. What is his present direction?", ['North', 'West', 'East', 'South'], 'North',
  "North, left = West, right = North. The two opposite turns cancel.",
  "Left then right (or right then left) brings you back to your first direction.")
q("Ahmad walks towards North and then turns left. What is his present direction?", ['East', 'West', 'South', 'North'], 'West',
  "When you face North, your left hand points West.",
  "Facing North: right = East, left = West, behind = South.")
q("Adnan walks 10 metres towards North, then towards South. After this he turns back and then moves towards his left. What is his present direction?", ['East', 'West', 'North', 'South'], 'West',
  "He faces South, turns back so he faces North, then turns left: facing North, left is West.",
  "'Turn back' means a 180 degree turn.")
# Ranking
q("Frank is taller than John, and Ralph is taller than Frank. Who is the shortest?", ['Frank', 'Ralph', 'John', 'Cannot be found'], 'John',
  "Order: Ralph > Frank > John, so John is the shortest.",
  "Write the names in one line from tallest to shortest to solve ranking questions.")
q("Azhar was born in 2000 and Javed in 2005. Aslam is older than Javed but younger than Azhar. Who is the oldest?", ['Javed', 'Aslam', 'Azhar', 'All same'], 'Azhar',
  "The person born first is the oldest. Azhar (2000) is older than Aslam, and Aslam is older than Javed (2005).",
  "Earlier year of birth = older person.")
q("Ali is younger than Ahmad, and Yaqoob is older than Ahmad. Who is the youngest?", ['Ahmad', 'Yaqoob', 'Ali', 'Cannot be found'], 'Ali',
  "Order: Yaqoob > Ahmad > Ali, so Ali is the youngest.",
  "Younger than the middle person who is himself younger than the oldest = youngest.")
# Percentage
q("90% of 90 is", ['72', '81', '80', '90'], '81', "0.9 x 90 = 81.", "Trick: 90% of a number = number minus 10% of it (90 - 9 = 81).")
q("80% of 90 is", ['72', '81', '70', '64'], '72', "0.8 x 90 = 72.", "80% = 4/5, and 4/5 of 90 = 72.")
q("80% of 80 is", ['60', '64', '72', '56'], '64', "0.8 x 80 = 64.", "8 x 8 = 64, so 80% of 80 = 64.")
q("90% of 70 is", ['63', '60', '72', '56'], '63', "0.9 x 70 = 63.", "70 - 10% of 70 (7) = 63.")
q("60% of 9 is", ['5.4', '6', '4.5', '5'], '5.4', "0.6 x 9 = 5.4.", "Find 10% first (0.9), then multiply by 6.")
q("80% of 10 is", ['8', '0.8', '80', '9'], '8', "0.8 x 10 = 8.", "Any % of 10 = that % divided by 10.")
q("One third of 10% of 90 is", ['9', '3', '30', '6'], '3', "10% of 90 = 9; one third of 9 = 3.", "Solve 'of' questions from the end: the last number first.")
q("One third of 10% of 120 is", ['12', '4', '40', '6'], '4', "10% of 120 = 12; one third of 12 = 4.", "'Of' means multiply.")
q("20% of one tenth of 90 is", ['18', '1.8', '9', '0.9'], '1.8', "One tenth of 90 = 9; 20% of 9 = 1.8.", "20% is the same as one fifth.")
q("Out of 500 students, 360 are boys. What is the percentage of girls?", ['72%', '28%', '36%', '14%'], '28%',
  "Girls = 500 - 360 = 140. 140 / 500 x 100 = 28%. 72% is the percentage of boys.", "Boys % + Girls % must always be 100%.")
q("There are 30 passengers in a bus and 2/3 of them are men. What is the percentage of women?", ['66.67%', '33.33%', '30%', '20%'], '33.33%',
  "Women are 1/3 of the passengers, and 1/3 = 33.33%.", "2/3 = 66.67% and 1/3 = 33.33%.")
q("In a class of 500, 340 are boys. Find the percentage of boys.", ['32%', '68%', '34%', '64%'], '68%', "340 / 500 x 100 = 68%.", "Dividing by 500 and multiplying by 100 is the same as dividing by 5.")
q("In a class of 1500 students, 1200 are present. What is the percentage of absent students?", ['80%', '20%', '30%', '25%'], '20%',
  "Absent = 300. 300 / 1500 x 100 = 20%. 80% is the present percentage.", "Present % + Absent % = 100%.")
q("In a classroom of 1500 students, 1200 are present. Find the percentage of present students.", ['20%', '80%', '75%', '85%'], '80%', "1200 / 1500 x 100 = 80%.", "1200/1500 = 4/5 = 80%.")
q("Out of 500 students, 340 are present. What is the percentage of absent students?", ['68%', '32%', '34%', '16%'], '32%', "Absent = 160. 160 / 500 x 100 = 32%.", "First find the number absent, then the percentage.")
# Mirror
q("Which word looks the same in a mirror?", ['PAKISTAN', 'TITITIT', 'ARMY', 'CADET'], 'TITITIT',
  "T and I are symmetrical letters, and TITITIT reads the same from both sides, so its mirror image is the same word.",
  "Letters that look the same in a mirror: A, H, I, M, O, T, U, V, W, X, Y.")
# Series and maths
q("Complete the series: 115, 55, 170, 65, 235, ?", ['75', '70', '300', '85'], '75',
  "Two series: 55, 65, 75 (+10) and 115 + 55 = 170, 170 + 65 = 235. The missing term is 75.", "Check alternate terms when a series jumps up and down.")
q("Complete the series: 66, 63, 57, 45, ?", ['24', '21', '33', '30'], '21',
  "Differences are 3, 6, 12, then 24 (doubling). 45 - 24 = 21. The PDF wrote 24, which is the difference, not the next number.", "Doubling differences: 3, 6, 12, 24.")
q("Complete the series: 2, 6, 14, 30, 62, ?", ['124', '126', '94', '128'], '126', "Each term x 2 + 2: 62 x 2 + 2 = 126.", "Differences 4, 8, 16, 32, 64 also give 126.")
q("What comes next: 3, 7, 14, 18, 36, 40, ?", ['44', '80', '72', '76'], '80', "Pattern: +4, x2, +4, x2, +4, x2. 40 x 2 = 80.", "Mixed patterns often repeat two steps.")
q("Quarter of one tenth of 120 is", ['12', '3', '30', '4'], '3', "One tenth of 120 = 12; a quarter of 12 = 3.", "Quarter = 1/4.")
q("Quarter of 120 is", ['40', '30', '12', '24'], '30', "120 / 4 = 30.", "Quarter = divide by 4.")
q("One tenth of 90 is", ['10', '9', '0.9', '90'], '9', "90 / 10 = 9.", "One tenth = divide by 10.")
q("One tenth of 120 is", ['10', '12', '1.2', '20'], '12', "120 / 10 = 12.", "Move the decimal one place left.")
q("One third of 120 is", ['30', '40', '60', '12'], '40', "120 / 3 = 40.", "One third = divide by 3.")
q("Half of 9/90 is", ['1/10', '1/20', '1/5', '9/45'], '1/20', "9/90 = 1/10; half of 1/10 = 1/20 = 0.05.", "Simplify the fraction first.")
q("120 x 7 =", ['740', '840', '820', '960'], '840', "120 x 7 = 840.", "12 x 7 = 84, then add the zero.")
q("1 + 2/2 =", ['1.5', '2', '3', '1'], '2', "Division first: 2/2 = 1, then 1 + 1 = 2.", "BODMAS: Division comes before Addition.")
q("2(2 + 2) =", ['6', '8', '4', '16'], '8', "Bracket first: 2 + 2 = 4, then 2 x 4 = 8.", "BODMAS: Brackets first.")
q("Half of a quarter is", ['1/4', '1/8', '1/6', '1/2'], '1/8', "1/2 x 1/4 = 1/8.", "'Of' means multiply.")
# Alphabet series
q("Complete the series: B, E, J, Q, ?", ['X', 'Z', 'Y', 'W'], 'Z', "Positions 2, 5, 10, 17: add 3, 5, 7, then 9. 17 + 9 = 26 = Z.", "Write letter positions (A=1 ... Z=26) to solve letter series.")
q("Complete the series: A, C, F, J, O, ?", ['T', 'U', 'V', 'S'], 'U', "Positions 1, 3, 6, 10, 15: add 2, 3, 4, 5, then 6. 15 + 6 = 21 = U.", "Increasing gaps of 1 are common in letter series.")
q("Complete the series: L, M, N, ?", ['P', 'O', 'Q', 'K'], 'O', "Simple alphabetical order: L, M, N, O.", "O is the 15th letter.")
q("If Z = 2 and X = 5, then which comes next?", ['U = 9', 'V = 8', 'W = 7', 'T = 11'], 'U = 9',
  "Letters go back with growing gaps (Z to X is 2 back, X to U is 3 back) and numbers grow with growing gaps (2 to 5 is +3, 5 to 9 is +4). So the next is U = 9.",
  "In growing-gap series both the letter gap and the number gap go up by 1 each step.")
q("Z = 3, X = 5, V = 7, T = 9. Find the next.", ['S = 10', 'R = 11', 'Q = 11', 'R = 12'], 'R = 11', "Letters go back by 2 (Z, X, V, T, R) and numbers go up by 2 (3, 5, 7, 9, 11).", "Check the letter rule and the number rule separately.")
q("What comes next: A, E, K, ?", ['R', 'S', 'Q', 'T'], 'S', "Positions 1, 5, 11: add 4, 6, then 8. 11 + 8 = 19 = S.", "Gaps going up by 2 (4, 6, 8).")
q("Complete the series: AB/A, BC/B, CD/C, ?", ['DE/E', 'DE/D', 'CE/D', 'EF/E'], 'DE/D', "Each term moves one letter forward: DE / D.", "Look at every part of the term separately.")
q("Complete the series: H, F, D, ?", ['A', 'B', 'C', 'E'], 'B', "Each letter goes back by 2: H, F, D, B.", "Backward series: subtract the same gap.")
q("Complete the series: J, H, F, D, ?", ['C', 'B', 'A', 'E'], 'B', "Back by 2 each time: J, H, F, D, B.", "Same rule as H, F, D, B.")
q("Complete the series: A, E, K, ?", ['R', 'S', 'T', 'Q'], 'S',
  "Same question as before: positions 1, 5, 11, gaps 4, 6, 8, so 19 = S. The PDF wrote R here, which does not fit the pattern.", "Repeated in the notes twice with two answers; S is correct.")
# Time sequence
q("How many months have 31 days?", ['6', '7', '8', '5'], '7', "January, March, May, July, August, October and December = 7 months.", "Knuckle trick: every knuckle month has 31 days.")
q("A leap year comes after how many years?", ['3', '4', '5', '2'], '4', "A year is about 365 days and 6 hours. 4 x 6 hours = 1 extra day, so every 4th year has 366 days.", "In a leap year February has 29 days.")
q("If yesterday was Sunday, then the day after tomorrow will be", ['Tuesday', 'Wednesday', 'Thursday', 'Monday'], 'Wednesday', "Today is Monday, tomorrow Tuesday, the day after tomorrow Wednesday.", "Find 'today' first in day questions.")
q("If yesterday was Friday, tomorrow will be", ['Saturday', 'Sunday', 'Monday', 'Thursday'], 'Sunday', "Today is Saturday, so tomorrow is Sunday.", "Yesterday + 2 days = tomorrow.")
q("If the 28th day of a month is Sunday, then the 2nd day will be", ['Monday', 'Tuesday', 'Sunday', 'Wednesday'], 'Tuesday', "28 - 2 = 26 days back. 26 = 3 weeks + 5 days. 5 days before Sunday is Tuesday.", "Remove full weeks (7 days) and count only the remainder.")
q("If the 4th day of a month is Tuesday, then the 26th day will be", ['Tuesday', 'Wednesday', 'Thursday', 'Monday'], 'Wednesday', "26 - 4 = 22 = 3 weeks + 1 day. Tuesday + 1 = Wednesday.", "Same weekday repeats every 7 days.")
q("If the 4th day of a month is Sunday, the 19th day will be", ['Sunday', 'Monday', 'Tuesday', 'Saturday'], 'Monday', "19 - 4 = 15 = 2 weeks + 1 day. Sunday + 1 = Monday.", "4, 11, 18 are Sundays, so 19 is Monday.")
q("If the 14th day of a month is Sunday, the 4th day will be", ['Wednesday', 'Thursday', 'Friday', 'Tuesday'], 'Thursday', "14 - 4 = 10 = 1 week + 3 days back. 3 days before Sunday is Thursday.", "7th is also Sunday, so 4th is 3 days before it.")
q("If the 1st day of a month is Monday, then the 12th day will be", ['Saturday', 'Friday', 'Thursday', 'Monday'], 'Friday',
  "12 - 1 = 11 = 1 week + 4 days. Monday + 4 = Friday. (The PDF wrote Saturday, which is one day off.)", "1st and 8th are Mondays, so the 12th is Friday.")
q("If the 2nd day of a month is Monday, then the 12th day will be", ['Wednesday', 'Thursday', 'Friday', 'Tuesday'], 'Thursday', "12 - 2 = 10 = 1 week + 3 days. Monday + 3 = Thursday.", "2nd and 9th are Mondays.")
q("If the 2nd day of a month is Sunday, the 23rd day will be", ['Monday', 'Sunday', 'Saturday', 'Tuesday'], 'Sunday', "23 - 2 = 21 = exactly 3 weeks, so the same day: Sunday.", "Any gap of 7, 14, 21 or 28 days gives the same weekday.")
q("If the 15th day of a month is Monday, the 4th day of the month is", ['Wednesday', 'Thursday', 'Friday', 'Monday'], 'Thursday', "15 - 4 = 11 = 1 week + 4 days back. 4 days before Monday is Thursday.", "8th is Monday, so 4th is 4 days earlier.")
q("If the 2nd day of a month is Friday, then the 23rd day will be", ['Thursday', 'Friday', 'Saturday', 'Sunday'], 'Friday', "23 - 2 = 21 = 3 full weeks, so the same day: Friday.", "Exact weeks keep the same weekday.")
q("If the 4th day of a month is Sunday, the 14th day is", ['Tuesday', 'Wednesday', 'Thursday', 'Monday'], 'Wednesday', "14 - 4 = 10 = 1 week + 3 days. Sunday + 3 = Wednesday.", "11th is Sunday, so 14th is Wednesday.")
# Dozen
q("If one dozen pencils cost Rs 27, then the price of 4 pencils is", ['Rs 8', 'Rs 9', 'Rs 12', 'Rs 6'], 'Rs 9', "4 is one third of 12, so the price is 27 / 3 = Rs 9.", "1 dozen = 12.")
q("If 1 dozen pencils cost Rs 60, the price of 5 pencils will be", ['Rs 30', 'Rs 25', 'Rs 20', 'Rs 24'], 'Rs 25', "One pencil = 60 / 12 = Rs 5, so 5 pencils = Rs 25.", "Find the price of one item first (unitary method).")
q("If one dozen eggs cost Rs 24, then the price of 7 eggs is", ['Rs 12', 'Rs 14', 'Rs 16', 'Rs 21'], 'Rs 14', "One egg = 24 / 12 = Rs 2, so 7 eggs = Rs 14.", "Unitary method: one item first, then multiply.")
q("One dozen pencils cost Rs 15. What is the price of 72 pencils?", ['Rs 60', 'Rs 90', 'Rs 75', 'Rs 120'], 'Rs 90', "72 pencils = 6 dozen. 6 x 15 = Rs 90.", "72 / 12 = 6 dozen.")
# Blood relations
q("If my brother's sister is your mother, who am I to you?", ['Father', 'Uncle', 'Cousin', 'Brother'], 'Uncle',
  "My brother's sister is my sister. My sister is your mother, so I am your mother's brother: your (maternal) uncle.", "Mother's brother = maternal uncle (Mamun).")
q("The sister of my brother's son is my", ['Daughter', 'Niece', 'Sister', 'Cousin'], 'Niece', "My brother's son's sister is my brother's daughter, who is my niece.", "Brother's or sister's daughter = niece.")
q("My sister is your mother. What is your relation to me?", ['Cousin', 'Nephew or niece', 'Brother', 'Son'], 'Nephew or niece', "You are my sister's child, so you are my nephew (boy) or niece (girl).", "Sister's son = nephew, sister's daughter = niece.")
q("A is the father of B, but B is not A's son. What is B to A?", ['Son', 'Daughter', 'Nephew', 'Brother'], 'Daughter', "A child of a father who is not his son must be his daughter.", "Read the 'not' carefully in relation questions.")
# Time, speed, distance
q("A train's speed is twice that of a car. If the car covers 60 km in one hour, how much distance will the train cover in 30 minutes?", ['30 km', '60 km', '120 km', '90 km'], '60 km', "Train speed = 120 km/h. In half an hour it covers 120 / 2 = 60 km.", "Distance = Speed x Time.")
q("A train's speed is double that of a car, and the car travels 30 km in 1 hour. How much distance will the train cover in 30 minutes?", ['60 km', '30 km', '15 km', '45 km'], '30 km', "Train speed = 60 km/h. In 30 minutes it covers 30 km.", "30 minutes = half an hour.")
q("A train is moving at 90 km/h. How much distance will it cover in 12 minutes?", ['15 km', '18 km', '20 km', '9 km'], '18 km', "12 minutes = 1/5 hour. 90 / 5 = 18 km.", "Change minutes to hours by dividing by 60.")
q("If a helicopter needs 50 gallons to fly 320 km, how many gallons does it need to fly 400 km?", ['60', '62.5', '64', '70'], '62.5', "50 / 320 x 400 = 62.5 gallons.", "Direct proportion: more distance, more fuel.")
q("A man walks 20 km in 1 hour 40 minutes. How much time will he take to cover 1 km?", ['4 minutes', '5 minutes', '6 minutes', '10 minutes'], '5 minutes', "1 hour 40 minutes = 100 minutes. 100 / 20 = 5 minutes per km.", "Convert hours to minutes first.")
q("A bus moves at 60 km/h and a train moves at twice that speed. How much distance does the train cover in 30 minutes?", ['30 km', '60 km', '120 km', '90 km'], '60 km', "Train speed = 120 km/h. In half an hour: 60 km. (The PDF does not show the answer.)", "Same as the train and car question: double speed, half time.")
# Profit and loss
q("Ali bought a pen for Rs 30 and sold it for Rs 40. What is his profit percentage?", ['25%', '33.33%', '10%', '40%'], '33.33%', "Profit = Rs 10. 10 / 30 x 100 = 33.33%.", "Profit % is always on the cost price.")
q("A person bought a book for Rs 500 and sold it for Rs 700. Find the profit percentage.", ['28.57%', '40%', '20%', '35%'], '40%', "Profit = Rs 200. 200 / 500 x 100 = 40%.", "28.57% would be wrongly using the selling price.")
# Analogy and classification
q("A bat cannot see, and a snake cannot", ['Smell', 'Hear', 'Taste', 'Feel'], 'Hear', "Snakes have no outer ears and cannot hear sound in the air the way we do; they feel vibrations.", "Bats use echoes (echolocation) to move in the dark.")
q("Find the odd one: Angle, Rectangle, Square, Hexagon", ['Square', 'Angle', 'Hexagon', 'Rectangle'], 'Angle', "Rectangle, square and hexagon are closed shapes (polygons); an angle is not a shape.", "A hexagon has 6 sides.")
q("Find the odd one: Cricket, Football, Tennis, Baseball", ['Cricket', 'Football', 'Tennis', 'Baseball'], 'Football', "Cricket, tennis and baseball are played with a bat or racket; football is played with the feet.", "Hockey is the national game of Pakistan.")
q("Find the odd one: Wheat, Hay, Rice, Maize", ['Wheat', 'Hay', 'Rice', 'Maize'], 'Hay', "Wheat, rice and maize are grains (food crops); hay is dried grass for animals.", "Wheat is the main food crop of Pakistan.")
q("Find the odd one: Monkey, Ape, Chimpanzee, Panda", ['Monkey', 'Ape', 'Chimpanzee', 'Panda'], 'Panda', "Monkey, ape and chimpanzee are primates; the panda is a bear.", "The giant panda mainly eats bamboo.")
q("Find the odd one: America, Africa, Asia, Euro", ['America', 'Africa', 'Asia', 'Euro'], 'Euro', "America, Africa and Asia are continents; the euro is a currency.", "Asia is the largest continent.")
q("The sound of an eagle is called a", ['Hoot', 'Scream', 'Chirp', 'Coo'], 'Scream', "An eagle screams (also called a screech). An owl hoots, a pigeon coos and small birds chirp.", "Animal sounds are common in verbal tests.")
q("An aeroplane flies due to", ['Weight', 'Lift', 'Drag', 'Gravity'], 'Lift', "The wings make lift, the upward force that keeps the aeroplane in the air.", "The four forces on a plane: lift, weight, thrust and drag.")
q("Vehicle is to wheels as sound is to", ['Ears', 'Waves', 'Noise', 'Speed'], 'Waves', "A vehicle moves on wheels; sound travels as waves.", "Sound cannot travel in a vacuum.")
q("Dog is to bitch as horse is to", ['Colt', 'Mare', 'Pony', 'Stallion'], 'Mare', "A female dog is a bitch; a female horse is a mare.", "A young horse is a foal; a young male horse is a colt.")
q("Parents give education to their children", ['To get money', 'To groom them', 'To keep them busy', 'To show others'], 'To groom them', "The main aim of education is to groom children into good, skilled people.", "In 'why' questions, choose the main and most sensible reason.")
q("We boil milk", ['To make it sweet', 'To kill germs', 'To make it thick', 'To cool it'], 'To kill germs', "Boiling kills harmful germs and makes milk safe to drink.", "Pasteurisation also heats milk to kill germs.")
q("Why do people read newspapers?", ['To pass time', 'To get knowledge', 'To sleep', 'To learn cooking'], 'To get knowledge', "Newspapers give news and knowledge about the world.", "Choose the main purpose, not a side use.")
q("Why do people use cars?", ['To show off', 'To travel', 'To play', 'To sleep'], 'To travel', "The main use of a car is travelling from one place to another.", "Main purpose questions have one sensible answer.")
q("Why do girls wear glasses?", ['For fashion', 'For eyesight', 'For sunlight', 'For reading only'], 'For eyesight', "Glasses are mainly worn to correct eyesight.", "Short sight and long sight are corrected with lenses.")
q("Why do women go to the bazaar?", ['For walking', 'For shopping', 'For meeting', 'For eating'], 'For shopping', "A bazaar is a market, and people go there mainly for shopping.", "Bazaar = market.")
q("What will be the last letter of UTYEAB after arranging it alphabetically?", ['U', 'Y', 'T', 'E'], 'Y', "Arranged: A, B, E, T, U, Y. The last letter is Y.", "Write the letters in A to Z order before answering.")
q("What will be the 3rd letter of the word MANAGEMENT when its different letters are arranged alphabetically?", ['G', 'M', 'N', 'T'], 'G',
  "Different letters in order: A, E, G, M, N, T. The 3rd is G. (If every letter is counted, including repeats, the 3rd letter would be E.)", "Read whether the question counts repeated letters.")
q("What will be the second letter when AUGMENTED is arranged alphabetically?", ['E', 'D', 'G', 'A'], 'D',
  "Arranged: A, D, E, E, G, M, N, T, U. The 2nd letter is D. (The PDF wrote E, which is the 3rd letter.)", "AUGMENTED has the letters A, U, G, M, E, N, T, E, D.")
q("Arrange RAPIS. It is the name of a", ['Country', 'City', 'Ocean', 'State'], 'City', "RAPIS rearranged gives PARIS, a city (the capital of France).", "Paris is on the River Seine.")
q("Arrange OPERALD. In which category does it lie?", ['Bird', 'Wild animal', 'Fruit', 'Country'], 'Wild animal', "OPERALD rearranged gives LEOPARD, a wild animal.", "The leopard is found in northern Pakistan and Azad Kashmir.")
q("Find the odd one: Lahore, Rawalpindi, Karachi, Sindh, Quetta", ['Lahore', 'Karachi', 'Sindh', 'Quetta'], 'Sindh', "Sindh is a province; the others are cities.", "Karachi is the capital of Sindh.")
q("Cold is to ice as hot is to", ['Fire', 'Steam', 'Sun', 'Water'], 'Steam', "Very cold water becomes ice; very hot water becomes steam.", "Water boils at 100 degrees C and freezes at 0 degrees C.")
q("Which does not belong to the group: Cow, Dog, Leopard, Cat", ['Dog', 'Cow', 'Leopard', 'Cat'], 'Cow', "Dog, leopard and cat eat meat (carnivores); the cow eats grass (herbivore).", "Herbivores eat plants; carnivores eat meat.")
q("Arrange E, H, M, O, R, T into a word.", ['Mother', 'Thermo', 'Hermot', 'Mother-in-law'], 'Mother', "E, H, M, O, R, T make the word MOTHER.", "Jumbled-word questions usually make a common word.")
q("According to the dictionary, which comes first: MOUNTAIN, MARGALLA, MACHINE?", ['Mountain', 'Margalla', 'Machine', 'All same'], 'Machine', "All start with M. Second letters: A, A, O. Then third letters: C (MACHINE) comes before R (MARGALLA).", "Compare letter by letter until they differ.")
# Work and numbers
q("If 1 man writes 5 papers in 5 minutes, then 1 man will write 1 paper in", ['5 minutes', '1 minute', '2 minutes', '25 minutes'], '1 minute', "5 papers in 5 minutes = 1 paper per minute.", "Find the work done in one unit of time.")
q("There are 30 passengers in a bus and 2/3 of them are men. What is the number of women?", ['20', '10', '15', '12'], '10', "Men = 2/3 x 30 = 20. Women = 30 - 20 = 10.", "1/3 of 30 = 10.")
q("Amjad and Ahmad have 24 balls. Amjad has 3 times as many as Ahmad. How many does Ahmad have?", ['8', '6', '12', '18'], '6', "Ahmad = x, Amjad = 3x, so 4x = 24 and x = 6.", "Total parts = 1 + 3 = 4.")
q("If 5 men write 5 pages in 5 minutes, then 1 man will write 1 page in", ['1 minute', '5 minutes', '25 minutes', '10 minutes'], '5 minutes', "Each man writes 1 page in 5 minutes, because 5 men write 5 pages in 5 minutes.", "Classic trick question: the answer stays 5 minutes.")
q("10 men dig a well in 5 days. How many days will 5 men take?", ['5', '10', '2.5', '20'], '10', "Work = 10 x 5 = 50 man-days. 50 / 5 = 10 days.", "Fewer men = more days (inverse proportion).")

import random
rnd = random.Random(105)
for e in Q:
    o = e[2][:]; c = o[e[3]]
    if len(set(o)) == 4 and not any(x in ('All same', 'Cannot be found') for x in o):
        rnd.shuffle(o)
    e[2] = o; e[3] = o.index(c)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pv_final.json')
json.dump(Q, open(out, 'w'), ensure_ascii=False, indent=0)
print(len(Q), 'MCQs written to', out)
