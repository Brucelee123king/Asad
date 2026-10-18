S = "Hakeem Force Academy"
QS = []
def add(q, opts, a, why, rel, ids):
    QS.append((S, q, opts, a, why, rel, ids))

def day(q, opts, a, why, ids):
    add(q, opts, a, why, "A week has 7 days, so the same weekday repeats every 7 days of the month.", ids)

add("What is 1/10th of 90?", ["10", "8", "9", "0.9"], 2,
    "One tenth of 90 is 90 divided by 10, which is 9.",
    "Dividing by 10 simply moves the decimal point one place to the left.", [3268])
add("What is 120 multiplied by 7?", ["820", "840", "860", "780"], 1,
    "120 x 7 = 100 x 7 + 20 x 7 = 700 + 140 = 840.",
    "Multiplying by 7 is the same as multiplying by 10 and subtracting three times the number.", [3278])
add("What is 30% of 1/10 of 120?", ["3.6", "36", "4", "3"], 0,
    "One tenth of 120 is 12. Then 30% of 12 = 0.3 x 12 = 3.6.",
    "Candidates sometimes remembered 3, but the exact answer is 3.6.", [3292])
add("In a class of 1500 students, 1200 are boys. What percentage of the students are girls?",
    ["25%", "20%", "15%", "30%"], 1,
    "Girls = 1500 - 1200 = 300. Percentage = 300 / 1500 x 100 = 20%.",
    "The percentage of boys in this class is 80%, and the two percentages always add up to 100%.", [364, 2467, 2931])
add("Out of 1500 students, 1300 are present. What percentage of the students are absent (to two decimal places)?",
    ["13.33%", "15%", "10%", "86.67%"], 0,
    "Absent = 1500 - 1300 = 200. Percentage = 200 / 1500 x 100 = 13.33%.",
    "The percentage present is 86.67%, which together with 13.33% makes 100%.", [363, 3072, 2932])
day("If Monday is the 12th day of a month, what day will be the 1st of that month?",
    ["Wednesday", "Friday", "Thursday", "Tuesday"], 2,
    "From the 1st to the 12th is 11 days, and 11 = 7 + 4. So the 1st is 4 days before Monday, which is Thursday.", [2389])
day("If the 2nd day of a month is Sunday, what days are the 12th and the 14th?",
    ["Wednesday and Friday", "Tuesday and Thursday", "Thursday and Saturday", "Wednesday and Thursday"], 0,
    "The 12th is 10 days after the 2nd, and 10 = 7 + 3, so it is Sunday + 3 = Wednesday. The 14th is 12 days after, 12 = 7 + 5, so Sunday + 5 = Friday.", [2406])
day("If the 1st day of a month is Friday, what day will be the 12th of that month?",
    ["Monday", "Sunday", "Wednesday", "Tuesday"], 3,
    "The 12th is 11 days after the 1st, and 11 = 7 + 4. Friday + 4 days = Tuesday.", [2420])
day("If the 4th day of a month is Monday, what day will be the 13th of that month?",
    ["Tuesday", "Thursday", "Wednesday", "Friday"], 2,
    "The 13th is 9 days after the 4th, and 9 = 7 + 2. Monday + 2 days = Wednesday.", [2414])
day("If the 4th day of a month is Sunday, what day will be the 13th of that month?",
    ["Monday", "Tuesday", "Wednesday", "Saturday"], 1,
    "The 13th is 9 days after the 4th, and 9 = 7 + 2. Sunday + 2 days = Tuesday.", [881])
day("If the 2nd day of a month is Monday, what day will be the 13th of that month?",
    ["Thursday", "Saturday", "Wednesday", "Friday"], 3,
    "The 13th is 11 days after the 2nd, and 11 = 7 + 4. Monday + 4 days = Friday.", [2428])
day("If the 14th day of a month is Friday, what day will be the 25th of that month?",
    ["Monday", "Wednesday", "Tuesday", "Thursday"], 2,
    "The 25th is 11 days after the 14th, and 11 = 7 + 4. Friday + 4 days = Tuesday.", [2398])
day("If the 1st day of a month is Monday, what day will be the 14th of that month?",
    ["Saturday", "Monday", "Sunday", "Tuesday"], 2,
    "The 14th is 13 days after the 1st, and 13 = 7 + 6. Monday + 6 days = Sunday.", [884])
day("If the 15th day of a month is Friday, what day was the 4th of that month?",
    ["Monday", "Tuesday", "Friday", "Sunday"], 0,
    "From the 4th to the 15th is 11 days, and 11 = 7 + 4. So the 4th is 4 days before Friday, which is Monday.", [2399])
day("If the 15th day of a month is Monday, what day will be the 1st of that month?",
    ["Sunday", "Tuesday", "Saturday", "Monday"], 3,
    "From the 1st to the 15th is 14 days, exactly two weeks, so both fall on the same weekday, Monday.", [2400])
day("If the 1st day of a month is Friday, what day will be the 15th of that month?",
    ["Friday", "Saturday", "Thursday", "Monday"], 0,
    "The 15th is 14 days after the 1st, which is exactly two weeks, so it is also a Friday.", [2423])
day("If the 1st day of a month is Monday, what day will be the 15th of that month?",
    ["Sunday", "Tuesday", "Monday", "Wednesday"], 2,
    "The 15th is 14 days after the 1st, which is exactly two weeks, so it is also a Monday.", [886])
add("Which term comes next in the series: 3z, 6y, 9x, 15w, ?", ["21v", "24v", "30v", "24u"], 1,
    "The numbers 3, 6, 9, 15 follow the rule that each is the sum of the two before it (3+6=9, 6+9=15), so the next is 9+15=24. The letters go backwards from z, y, x, w to v.",
    "A series where each term is the sum of the previous two is called a Fibonacci-type series.", [4461, 4464])
add("What is the square root of 1600?", ["30", "50", "40", "160"], 2,
    "40 x 40 = 1600, so the square root of 1600 is 40.",
    "The square root of 16 is 4, so the square root of 1600 is 4 x 10 = 40.", [1172])
add("What is the value of sin 180 degrees?", ["1", "-1", "0.5", "0"], 3,
    "On the unit circle, 180 degrees is the point (-1, 0), and sine is the y-coordinate, which is 0.",
    "Also cos 180 degrees = -1 and sin 90 degrees = 1.", [576])
add("What is sin(180 - x) equal to?", ["sin x", "-sin x", "cos x", "-cos x"], 0,
    "Angles 180 - x and x lie on the same horizontal level of the unit circle, so they have the same sine: sin(180 - x) = sin x.",
    "In the same way, cos(180 - x) = -cos x.", [3434])
add("What is the value of cos 180 degrees?", ["0", "1", "-1", "180"], 2,
    "On the unit circle, 180 degrees is the point (-1, 0), and cosine is the x-coordinate, which is -1.",
    "cos 0 degrees = 1, cos 90 degrees = 0 and cos 180 degrees = -1.", [478])
add("What did the British call the War of 1857 that Muslims and Hindus of the subcontinent called the War of Independence?",
    ["Sepoy Mutiny", "War of Liberation", "Quit India Movement", "Boxer Rebellion"], 0,
    "The British described the uprising of 1857 as a mutiny of their Indian soldiers (sepoys), calling it the Sepoy Mutiny or Indian Mutiny.",
    "Indian and Pakistani historians call it the War of Independence; the last Mughal emperor Bahadur Shah Zafar was exiled to Rangoon afterwards.", [1687, 3193, 4104, 4179])
add("Who announced the partition of Bengal in 1905?", ["Lord Mayo", "Lord Ripon", "Lord Curzon", "Lord Minto"], 2,
    "Lord Curzon, the Viceroy of India, announced the partition of Bengal on 19 July 1905 and it took effect on 16 October 1905, creating a Muslim-majority eastern province.",
    "The partition was annulled in 1911, and the All India Muslim League was formed in 1906 partly in reaction to these events.", [3054, 5271])
add("In which year did Quaid-e-Azam Muhammad Ali Jinnah receive the title of Quaid-e-Azam (Great Leader), as most Pakistani textbooks state?",
    ["1936", "1938", "1940", "1934"], 1,
    "Most Pakistani textbooks say that Maulana Mazharuddin Shaheed gave the title Quaid-e-Azam to Jinnah in 1938.",
    "Sources differ on the exact year, and some mention 1936 or other dates.", [2705, 4230])
add("Who was the Prime Minister of the United Kingdom at the outbreak of the Second World War in 1939?",
    ["Winston Churchill", "Stanley Baldwin", "Clement Attlee", "Neville Chamberlain"], 3,
    "Neville Chamberlain was Prime Minister from 1937 to May 1940 and declared war on Germany on 3 September 1939.",
    "The UK has no president; Winston Churchill replaced Chamberlain in May 1940, and Boris Johnson (named by a candidate) was PM only in 2019 to 2022.", [5393])
add("Which party formed the government in the North-West Frontier Province (now KPK) at the time of independence in 1947?",
    ["Muslim League", "Awami National Party", "Indian National Congress", "Unionist Party"], 2,
    "The ministry of Dr Khan Sahib, which belonged to the Indian National Congress (backed by the Khudai Khidmatgars), was in power in the province in August 1947.",
    "The Governor dismissed the Khan Sahib ministry on 22 August 1947, and Abdul Qayyum Khan of the Muslim League then became Chief Minister.", [4966, 5444])
add("According to the 1956 Constitution, what was the minimum age to become President of Pakistan?",
    ["35 years", "40 years", "45 years", "30 years"], 1,
    "The 1956 Constitution required the President to be a Muslim of not less than 40 years of age.",
    "Some candidates remembered 45, but 40 is the age given in the Constitution of 1956.", [163, 1673])
add("Who abrogated the 1956 Constitution of Pakistan in October 1958?",
    ["Ayub Khan", "Yahya Khan", "Ghulam Muhammad", "Iskander Mirza"], 3,
    "President Iskander Mirza abrogated the 1956 Constitution on 7 October 1958, dissolved the assemblies and imposed martial law.",
    "Iskander Mirza himself was removed by General Ayub Khan only 20 days later.", [4990, 1389])
add("Under which Prime Minister was the 1956 Constitution of Pakistan framed and enforced?",
    ["Chaudhry Muhammad Ali", "Liaquat Ali Khan", "Huseyn Shaheed Suhrawardy", "Feroz Khan Noon"], 0,
    "Chaudhry Muhammad Ali was Prime Minister when the Constituent Assembly passed the constitution in 1956, and it came into force on 23 March 1956.",
    "23 March is the day later celebrated as Republic Day, and Iskander Mirza became the first President under it.", [5244])
add("Who dismissed (abrogated) the 1962 Constitution of Pakistan?",
    ["Zulfikar Ali Bhutto", "Yahya Khan", "Zia ul Haq", "Ayub Khan"], 1,
    "General Yahya Khan took over from Ayub Khan in March 1969, imposed martial law and abrogated the 1962 Constitution.",
    "The 1962 Constitution had lasted about seven years.", [5039])
add("Which President introduced the 1962 Constitution of Pakistan?",
    ["Iskander Mirza", "Yahya Khan", "Ayub Khan", "Ghulam Ishaq Khan"], 2,
    "Field Marshal Ayub Khan was President and enforced the 1962 Constitution on 8 June 1962, framed by a commission headed by Justice Shahabuddin.",
    "It introduced a presidential system with the President elected through Basic Democrats.", [686, 5392])

DUPS = [(942, 2156), (30, 1048), (30, 121), (430, 3403), (268, 3270), (429, 1049), (195, 3272),
        (9, 3274), (9, 331), (30, 3276), (1631, 2435), (1629, 2469), (717, 2422), (1596, 885),
        (646, 1067), (1564, 137), (1669, 1904), (1668, 1598), (290, 5455), (769, 3590),
        (272, 905), (272, 223), (272, 1221), (273, 4145), (463, 749), (870, 1832), (1067, 5470),
        (104, 4087), (104, 4136), (107, 1994)]
