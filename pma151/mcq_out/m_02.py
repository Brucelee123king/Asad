S = "Hakeem Force Academy"
QS = []
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ORD = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 7: "7th", 8: "8th", 12: "12th", 21: "21st", 22: "22nd", 23: "23rd", 24: "24th", 25: "25th", 26: "26th", 27: "27th"}

def dayq(d1, day, d2, ids, k):
    i = DAYS.index(day)
    diff = d2 - d1
    ans = DAYS[(i + diff) % 7]
    ai = DAYS.index(ans)
    wrong = [DAYS[(ai + s) % 7] for s in (1, 3, 5)]
    opts = wrong[:]
    opts.insert(k % 4, ans)
    q = "If the " + ORD[d1] + " day of a month is " + day + ", what day will the " + ORD[d2] + " be?"
    if diff >= 0:
        r = "From the " + ORD[d1] + " to the " + ORD[d2] + " is " + str(diff) + " days. " + str(diff) + " = " + str(diff // 7) + " weeks and " + str(diff % 7) + " extra days, so count " + str(diff % 7) + " days forward from " + day + " to reach " + ans + "."
    else:
        r = "From the " + ORD[d2] + " to the " + ORD[d1] + " is " + str(-diff) + " days, which leaves " + str((-diff) % 7) + " extra days after full weeks, so go back from " + day + " to reach " + ans + "."
    QS.append((S, q, opts, k % 4, r, "Dates that are 7 days apart always fall on the same day of the week.", ids))

def dayq_rev(d1, day, d2, ids, k):
    i = DAYS.index(day)
    diff = d2 - d1
    ans = DAYS[(i + diff) % 7]
    ai = DAYS.index(ans)
    wrong = [DAYS[(ai + s) % 7] for s in (1, 3, 5)]
    opts = wrong[:]
    opts.insert(k % 4, ans)
    q = "The " + ORD[d1] + " of a month is " + day + ". What day is the " + ORD[d2] + " of the same month?"
    r = "The " + ORD[d2] + " is " + str(-diff) + " days before the " + ORD[d1] + ". " + str(-diff) + " = 3 weeks and 1 extra day, so it is one day before " + day + ", which is " + ans + "."
    QS.append((S, q, opts, k % 4, r, "Going back exactly 7 days always gives the same weekday.", ids))

k = 0
for d1, day, d2, ids in [
    (2, "Sunday", 21, [2055]), (8, "Tuesday", 21, [2071]), (1, "Friday", 21, [2074]),
    (4, "Sunday", 23, [2062]), (3, "Monday", 23, [2089]), (1, "Monday", 24, [2050]),
    (2, "Friday", 24, [719]), (3, "Monday", 24, [2058]), (1, "Sunday", 24, [2073]),
    (4, "Monday", 25, [2059]), (5, "Friday", 25, [2063]), (5, "Sunday", 25, [2066]),
    (7, "Saturday", 26, [2070]), (1, "Monday", 27, [2051]), (7, "Sunday", 25, [2068]),
    (7, "Monday", 12, [2069])]:
    dayq(d1, day, d2, ids, k)
    k += 1
dayq_rev(24, "Friday", 2, [2707], 1)

def add(q, opts, ci, r, f, ids):
    QS.append((S, q, opts, ci, r, f, ids))

add("Which country hosted the largest number of refugees in 2016?", ["Pakistan", "Turkey", "Lebanon", "Jordan"], 1,
    "According to UNHCR figures for 2016, Turkey hosted about 2.9 million refugees, mostly Syrians, which was the largest number in the world.",
    "Pakistan was the second largest host in 2016 with about 1.4 million refugees, mostly Afghans.", [4315])
add("Which country hosted the largest number of refugees in 2017?", ["Uganda", "Germany", "Iran", "Turkey"], 3,
    "UNHCR reported that Turkey hosted about 3.5 million refugees at the end of 2017, the largest number worldwide.",
    "Turkey stayed at the top of the list for several years because of the Syrian refugee crisis.", [1124])
add("According to the 2017 census, what was the population of Pakistan?", ["About 193 million", "About 220 million", "About 207.7 million", "About 241 million"], 2,
    "The 6th Population and Housing Census of 2017 counted 207,684,626 people in Pakistan.",
    "The next census, held in 2023, counted about 241.5 million people.", [181])
add("Which country hosted the 2022 FIFA World Cup?", ["Qatar", "Russia", "Brazil", "United Arab Emirates"], 0,
    "The 2022 FIFA World Cup was held in Qatar from 20 November to 18 December 2022.",
    "It was the first FIFA World Cup held in an Arab and Muslim-majority country, and Argentina won it.", [4244])
add("Which country hosted the 2018 Asian Games?", ["Indonesia", "South Korea", "China", "Japan"], 0,
    "The 2018 Asian Games were held in Indonesia, in the cities of Jakarta and Palembang.",
    "The 2022 Asian Games, held in 2023, were hosted by Hangzhou in China.", [2223])
add("On which date did the 2018 Asian Games begin?", ["18 August 2018", "8 August 2018", "2 September 2018", "1 July 2018"], 0,
    "The 18th Asian Games opened in Jakarta on 18 August 2018 and ended on 2 September 2018.",
    "Indonesia's Jakarta and Palembang shared hosting of that edition.", [4022])
add("Where were the 2018 Winter Olympic Games held?", ["Sochi, Russia", "Pyeongchang, South Korea", "Beijing, China", "Vancouver, Canada"], 1,
    "The 2018 Winter Olympics took place in Pyeongchang, South Korea, in February 2018.",
    "The 2018 Summer Olympics did not exist: the Summer Games were held in Rio in 2016 and Tokyo in 2021.", [4241])
add("Which country hosted the 2018 Asia Cup cricket tournament?", ["India", "Bangladesh", "Sri Lanka", "United Arab Emirates"], 3,
    "The 2018 Asia Cup was played in the United Arab Emirates, in Dubai and Abu Dhabi, in September 2018.",
    "India won the 2018 Asia Cup by beating Bangladesh in the final.", [4329])
add("Which country won the 2018 FIFA World Cup?", ["Croatia", "Belgium", "Brazil", "France"], 3,
    "France beat Croatia 4-2 in the final in Moscow in July 2018.",
    "Russia hosted the 2018 tournament, and Argentina won the next one in 2022.", [326])
add("Which team won the Asia Cup cricket tournament in 2022?", ["Pakistan", "Sri Lanka", "India", "Afghanistan"], 1,
    "Sri Lanka beat Pakistan by 23 runs in the final in Dubai in September 2022 to win the T20 format Asia Cup.",
    "The 2022 Asia Cup was played in the United Arab Emirates after being moved from Sri Lanka.", [60])
add("Which word is spelled by the letter positions 18, 5, 19, 20 of the English alphabet?", ["REST", "RISE", "REAL", "PEST"], 0,
    "Position 18 is R, 5 is E, 19 is S and 20 is T, so the letters spell REST.",
    "The English alphabet has 26 letters, with A as position 1 and Z as position 26.", [3844, 4501])
add("With which neighbouring country does Pakistan share a border of about 2,400 km?", ["Afghanistan", "Iran", "China", "India"], 0,
    "The Pakistan-Afghanistan border, the Durand Line, is about 2,430 km long and is commonly quoted as about 2,400 km.",
    "Pakistan's border with India is about 3,300 km, with Iran about 900 km and with China about 520 km.", [2713, 5266, 5267, 238])
add("Which is the second highest mountain in the world?", ["Mount Everest", "Kangchenjunga", "K2", "Nanga Parbat"], 2,
    "K2, at about 8,611 m, is the second highest mountain in the world after Mount Everest.",
    "K2 is the highest mountain of Pakistan and lies in the Karakoram range.", [545])
add("Which is the second highest mountain of Pakistan?", ["K2", "Nanga Parbat", "Gasherbrum I", "Rakaposhi"], 1,
    "K2 is the highest peak in Pakistan and Nanga Parbat, at about 8,126 m, is the second highest.",
    "Nanga Parbat is nicknamed the Killer Mountain and is in Gilgit-Baltistan.", [3110])
add("Who was the fourth and last Governor-General of Pakistan?", ["Khawaja Nazimuddin", "Ghulam Muhammad", "Iskander Mirza", "Ayub Khan"], 2,
    "The Governor-Generals were Jinnah, Khawaja Nazimuddin, Ghulam Muhammad and Iskander Mirza, in that order.",
    "Iskander Mirza became the first President of Pakistan when the 1956 Constitution took effect.", [1250])
add("Who was the 7th President of the United States?", ["Andrew Jackson", "John Quincy Adams", "Martin Van Buren", "James Monroe"], 0,
    "Andrew Jackson served as the 7th US President from 1829 to 1837, after John Quincy Adams.",
    "Martin Van Buren followed Jackson as the 8th President.", [1251])
add("To which city did Prophet Muhammad (PBUH) migrate in 622 AD?", ["Taif", "Madinah", "Jeddah", "Makkah"], 1,
    "In 622 AD the Prophet (PBUH) migrated from Makkah to Madinah, which was then called Yathrib.",
    "This migration, the Hijrah, marks the start of the Islamic Hijri calendar.", [2105, 2781, 2789, 4133])
add("Which is the 6th most populous country in the world?", ["Brazil", "Pakistan", "Indonesia", "Nigeria"], 3,
    "The ranking is India, China, USA, Indonesia, Pakistan and then Nigeria in sixth place.",
    "Brazil is seventh, and Pakistan is fifth.", [4420, 4421])
add("What is the value of the percentage of absent students if 300 out of 500 students are present?", ["30%", "40%", "60%", "20%"], 1,
    "Absent students = 500 - 300 = 200. Percentage absent = 200 / 500 x 100 = 40%.",
    "Percentage present plus percentage absent always equals 100%.", [2083])
add("In a class of 1500 students, 300 are present. What is the percentage of absent students?", ["20%", "75%", "85%", "80%"], 3,
    "Absent = 1500 - 300 = 1200. Percentage = 1200 / 1500 x 100 = 80%.",
    "The percentage present here is 20%.", [2119])
add("There are 1500 students in a class, 1200 are boys and 300 are girls. What is the percentage of girls?", ["25%", "20%", "30%", "15%"], 1,
    "Percentage of girls = 300 / 1500 x 100 = 20%.",
    "Boys make up the remaining 80%.", [2770])
add("Out of 1200 students, 340 are present. What is the percentage of absent students, to two decimal places?", ["28.33%", "62.33%", "71.67%", "68.00%"], 2,
    "Absent = 1200 - 340 = 860. Percentage = 860 / 1200 x 100 = 71.67%.",
    "The percentage present is 340 / 1200 x 100 = 28.33%.", [1325])
add("A helicopter flies at 340 km/h. About how much time does it take to cover 700 km?", ["About 1.5 hours", "About 2.06 hours", "About 2.5 hours", "About 3 hours"], 1,
    "Time = distance / speed = 700 / 340 = 2.06 hours, which is about 2 hours 4 minutes.",
    "Speed = distance / time is the basic formula behind such questions.", [1347])
add("If a helicopter uses 50 litres of fuel to travel 200 km, how many litres will it use to travel 350 km?", ["75 litres", "100 litres", "87.5 litres", "80 litres"], 2,
    "Fuel per km = 50 / 200 = 0.25 litre. For 350 km: 350 x 0.25 = 87.5 litres.",
    "This is a direct proportion: more distance needs proportionally more fuel.", [2006, 2007])
add("In a class of 500 students, 360 are present. How many students are absent?", ["140", "150", "160", "120"], 0,
    "Absent students = 500 - 360 = 140.",
    "As a percentage, 140 out of 500 is 28%.", [2084])
add("Out of 400 students, 360 are present. What is the percentage of present students?", ["85%", "95%", "90%", "92%"], 2,
    "Percentage present = 360 / 400 x 100 = 90%. The absent students are 40, which is 10%.",
    "Present and absent percentages add up to 100%.", [798])
add("Out of 500 students, 380 are present. What is the percentage of present students?", ["76%", "80%", "72%", "74%"], 0,
    "Percentage present = 380 / 500 x 100 = 76%.",
    "The absent percentage is 24%.", [425])
add("A plane uses 80 gallons of fuel to cover 320 miles. How many gallons will 800 miles need?", ["180", "200", "220", "160"], 1,
    "Fuel per mile = 80 / 320 = 0.25 gallon. For 800 miles: 800 x 0.25 = 200 gallons.",
    "The same method works with kilometres and litres.", [1365])
add("A car travels at 78 km/h. How far will it travel in 12 minutes?", ["15.6 km", "9.4 km", "18 km", "12 km"], 0,
    "12 minutes = 12 / 60 = 0.2 hour. Distance = 78 x 0.2 = 15.6 km.",
    "To change minutes into hours, divide by 60.", [1993])
add("How many elements are there in each row of a matrix of order 4x3?", ["4", "12", "7", "3"], 3,
    "A matrix of order 4x3 has 4 rows and 3 columns, so each row has 3 elements.",
    "The total number of elements in a 4x3 matrix is 12.", [1843])
add("A matrix is of order 4x3. How many rows does it have?", ["3", "12", "4", "7"], 2,
    "The order of a matrix is written as rows x columns, so a 4x3 matrix has 4 rows.",
    "It has 3 columns.", [2107])
add("Find the next number in the series: 55, 579, 65, 580, ?", ["581", "75", "85", "590"], 1,
    "The series is two interleaved series. The 1st, 3rd and 5th terms go 55, 65, 75 (add 10) and the 2nd and 4th terms go 579, 580, 581 (add 1). The 5th term is 75.",
    "Interleaved series are solved by reading odd and even positions separately.", [1666, 1159])

DUPS = [(724, 722), (1799, 2076), (1501, 590), (1501, 55), (1772, 1142), (1772, 557), (1920, 1185), (1920, 1186),
        (1143, 3112), (1843, 889), (1843, 4419), (210, 4242), (210, 1310), (1636, 2961), (2131, 2966), (2131, 2970),
        (731, 2111), (731, 2117), (1609, 2601), (2923, 2003)]
