S = "Hakeem Force Academy"
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def ordn(n):
    if 10 <= n % 100 <= 20:
        suf = "th"
    else:
        suf = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return str(n) + suf

def dayq(a, aday, b, ids, k):
    d = b - a
    i = DAYS.index(aday)
    ans = DAYS[(i + d) % 7]
    others = [x for x in DAYS if x != ans]
    off = (a + b) % 4
    wrong = [others[(off + j) % 6] for j in range(3)]
    opts = wrong[:]
    pos = k % 4
    opts.insert(pos, ans)
    q = "If the %s day of a month is %s, what day will the %s be?" % (ordn(a), aday, ordn(b))
    if d >= 0:
        why = "From the %s to the %s is %d days. %d days is %d full weeks plus %d day(s), so the day is %d day(s) after %s, which is %s." % (ordn(a), ordn(b), d, d, d // 7, d % 7, d % 7, aday, ans)
    else:
        why = "From the %s back to the %s is %d days. %d days is %d full weeks plus %d day(s), so the day is %d day(s) before %s, which is %s." % (ordn(b), ordn(a), -d, -d, (-d) // 7, (-d) % 7, (-d) % 7, aday, ans)
    rel = "Dates that are 7 days apart always fall on the same weekday, so only the remainder after dividing the gap by 7 matters."
    return (S, q, opts, pos, why, rel, ids)

QS = []
for k, (a, ad, b, ids) in enumerate([
    (1, "Monday", 19, [2401]), (2, "Friday", 19, [878]), (3, "Sunday", 19, [880]),
    (4, "Friday", 19, [143]), (2, "Sunday", 19, [2431]), (2, "Monday", 20, [362]),
    (4, "Friday", 20, [2425]), (1, "Sunday", 21, [2402]), (5, "Monday", 21, [2417]),
    (3, "Friday", 23, [2411]), (4, "Friday", 23, [2424]), (2, "Friday", 23, [2429]),
    (24, "Tuesday", 3, [876]), (12, "Friday", 26, [2397]), (4, "Tuesday", 26, [169, 2426]),
    (4, "Monday", 27, [2415]), (5, "Friday", 27, [2416]), (3, "Monday", 28, [2412]),
    (4, "Friday", 28, [2413]), (29, "Tuesday", 4, [2404]), (3, "Friday", 29, [2410]),
    (6, "Monday", 29, [2418]),
]):
    QS.append(dayq(a, ad, b, ids, k))

QS += [
(S, "For how many days was the 1965 Pakistan-India war fought?", ["14 days", "21 days", "17 days", "6 days"], 2,
 "The war began in early September 1965 and the ceasefire came on 23 September 1965, a total of 17 days. It is remembered as the 17-day war.",
 "Pakistan celebrates 6 September as Defence Day in memory of the 1965 war.", [345]),
(S, "Which form of government was in force in Pakistan during the 1971 war?", ["Parliamentary democracy", "Martial law (military government under Yahya Khan)", "Presidential system under Ayub Khan", "Islamic caliphate"], 1,
 "General Yahya Khan had taken over in March 1969 and imposed martial law, so Pakistan was under military rule in 1971. Power passed to Zulfikar Ali Bhutto in December 1971.",
 "Ayub Khan, who ruled before Yahya Khan, had resigned in March 1969.", [4084]),
(S, "Which constitution was enforced in Pakistan in April 1972 after the separation of East Pakistan?", ["Interim Constitution of 1972", "Constitution of 1956", "Constitution of 1962", "Constitution of 1985"], 0,
 "After 1971 a temporary Interim Constitution was adopted in April 1972, which ended martial law and ran until the permanent constitution of 1973.",
 "The permanent Constitution of Pakistan was passed in April 1973 and enforced on 14 August 1973.", [1081]),
(S, "What was the official name of Pakistan under the 1973 Constitution?", ["Islamic Republic of Pakistan", "Republic of Pakistan", "Dominion of Pakistan", "Islamic State of Pakistan"], 0,
 "Article 1 of the 1973 Constitution names the country the Islamic Republic of Pakistan.",
 "The 1956 Constitution also used the name Islamic Republic of Pakistan, while the 1962 Constitution used Republic of Pakistan.", [1211]),
(S, "Under whose government was the 1973 Constitution of Pakistan framed and passed?", ["Zulfikar Ali Bhutto", "Ayub Khan", "Zia ul Haq", "Liaquat Ali Khan"], 0,
 "The 1973 Constitution was drafted by a parliamentary committee and passed by the National Assembly during the premiership of Zulfikar Ali Bhutto. It was adopted in April 1973.",
 "Abdul Hafeez Pirzada, the law minister, played a leading role in drafting it.", [1431]),
(S, "How many seats are reserved for non-Muslim minorities in the National Assembly of Pakistan under the 1973 Constitution?", ["5", "10", "20", "15"], 1,
 "Article 51 of the Constitution reserves ten seats in the National Assembly for non-Muslims.",
 "Minority members are chosen on reserved seats in proportion to the seats won by each party.", [2247]),
(S, "In which year was the Mangla Dam completed?", ["1974", "1977", "1967", "1958"], 2,
 "Construction of Mangla Dam on the Jhelum River began in the early 1960s and it was completed in 1967. Sources differ slightly on the start year but agree on 1967.",
 "Tarbela Dam on the Indus was completed later, in 1974.", [2727]),
(S, "A village had 1600 people in 2000, and its population doubles every five years. What was its population in 1980?", ["50", "100", "200", "400"], 1,
 "From 1980 to 2000 is 20 years, which is 4 doublings, so the population in 2000 is 16 times that of 1980. Hence 1600 divided by 16 gives 100.",
 "Going back in time with doubling growth means halving the number once for every period.", [2490]),
(S, "How many nuclear tests did Pakistan conduct in total in May 1998?", ["Five", "Six", "Seven", "Two"], 1,
 "Pakistan conducted five tests on 28 May 1998 (Chagai-I) and one more on 30 May 1998 (Chagai-II), a total of six. Some sources mention only the five of 28 May.",
 "Pakistan became the seventh nuclear-weapon state and the first in the Muslim world.", [2113]),
(S, "Which war took place between Pakistan and India in 1999?", ["Kargil War", "Rann of Kutch War", "Siachen War", "Tashkent War"], 0,
 "The Kargil War was fought in the Kargil sector of Kashmir between May and July 1999.",
 "The Lahore Declaration had been signed earlier in 1999 between Nawaz Sharif and Atal Bihari Vajpayee.", [4953]),
(S, "Who is generally listed as the first Governor-General of India (of Bengal, 1774)?", ["Lord Cornwallis", "Lord Dalhousie", "Warren Hastings", "Lord Canning"], 2,
 "Warren Hastings became Governor-General of Bengal in 1774 and is commonly called the first Governor-General of India in textbooks.",
 "Sources differ: Lord William Bentinck was the first Governor-General of all India in 1833, and Lord Mountbatten was the first of independent India.", [1451, 1452]),
(S, "In a class of 1500 students, 200 are absent. What percentage of students is present?", ["86.67 percent", "85 percent", "88 percent", "90 percent"], 0,
 "Present students are 1500 minus 200, which is 1300. Then 1300 divided by 1500 times 100 gives 86.67 percent.",
 "Percentage equals part divided by whole times 100.", [2388]),
(S, "Where were the FIFA World Cup matches of 2022 played?", ["Russia", "Brazil", "Qatar", "Germany"], 2,
 "The 2022 FIFA World Cup was hosted by Qatar from November to December 2022. Argentina won it.",
 "It was the first FIFA World Cup held in an Arab and Muslim-majority country.", [4361, 1275]),
(S, "Which country hosted the 2022 Winter Olympics?", ["Qatar", "China", "Japan", "South Korea"], 1,
 "The 2022 Winter Olympics were held in Beijing, China, in February 2022. There was no Summer Olympics in 2022.",
 "The 2020 Summer Olympics were held in Tokyo in 2021, and the 2024 Summer Games in Paris.", [2584, 4517, 4403]),
(S, "Which country hosted the largest number of refugees in 2019?", ["Germany", "Pakistan", "Turkey", "Jordan"], 2,
 "According to UNHCR, Turkey hosted about 3.6 million refugees in 2019, mostly Syrians, which was the highest in the world.",
 "In 2023 and 2024 Iran overtook Turkey as the largest refugee-hosting country.", [4507]),
(S, "Which number comes next in the series 115, 55, 170, 65, 225, ?", ["70", "75", "280", "85"], 1,
 "There are two series mixed together. The odd places 115, 170, 225 rise by 55 each time, and the even places 55, 65, next rise by 10, so the next term is 75.",
 "Alternating series are solved by separating the odd and even positions.", [4743]),
(S, "Who abrogated the 1962 Constitution, Pakistan's second constitution, in 1969?", ["Zulfikar Ali Bhutto", "Yahya Khan", "Zia ul Haq", "Iskander Mirza"], 1,
 "General Yahya Khan took over from Ayub Khan in March 1969, imposed martial law and abrogated the 1962 Constitution.",
 "Iskander Mirza abrogated the first constitution (1956) in October 1958.", [5323]),
(S, "Which is the second longest river in the world according to common textbooks?", ["Nile", "Yangtze", "Mississippi", "Amazon"], 3,
 "The Nile is usually named first at about 6650 km and the Amazon, flowing mainly through Brazil, second at about 6400 km.",
 "Sources differ: some recent measurements make the Amazon longer than the Nile, though the Amazon is the largest river by volume.", [4617]),
(S, "Which battle of the Muslims, fought in 3 AH, is counted as the second major battle after Badr?", ["Khandaq", "Uhud", "Khyber", "Hunayn"], 1,
 "The major battles in order are Badr (2 AH), Uhud (3 AH) and Khandaq (5 AH), so Uhud is the second.",
 "Sources differ: early chronologies also list small expeditions such as Abwa and Buwat before Badr.", [1147, 4955, 1375]),
(S, "Which is counted as the third major Ghazwa of the Holy Prophet (PBUH), after Badr and Uhud?", ["Ghazwa Khandaq (Ahzab)", "Ghazwa Tabuk", "Ghazwa Hunayn", "Fath Makkah"], 0,
 "The major battles in order are Badr, Uhud and Khandaq (Ahzab), fought in 5 AH. The Muslims dug a trench on the advice of Salman Farsi.",
 "Sources differ: early chronologies also list small expeditions such as Abwa and Buwat before Badr.", [4956, 4957, 1376]),
(S, "What is 2 x 2 divided by 2?", ["1", "2", "3", "4"], 1,
 "Work left to right: 2 x 2 is 4, and 4 divided by 2 is 2.",
 "Multiplication and division have equal priority and are done left to right.", [1054]),
(S, "What is 4 x 3 + 2 x 3?", ["18", "30", "24", "15"], 0,
 "Multiply first: 4 x 3 is 12 and 2 x 3 is 6. Then 12 plus 6 gives 18.",
 "In BODMAS, multiplication is done before addition.", [3298]),
(S, "In a class of 1200 students, 300 are absent. What percentage of students is present?", ["70 percent", "80 percent", "65 percent", "75 percent"], 3,
 "Present students are 1200 minus 300, which is 900. Then 900 divided by 1200 times 100 gives 75 percent.",
 "Absent percentage here is 25, and present plus absent always make 100 percent.", [2466]),
(S, "In a class of 500 students, 320 are present. What percentage of students is absent?", ["32 percent", "36 percent", "64 percent", "34 percent"], 1,
 "Absent students are 500 minus 320, which is 180. Then 180 divided by 500 times 100 gives 36 percent.",
 "Present students here are 64 percent.", [2436]),
(S, "In a class of 500 students, 340 are male. What percentage of the students is male?", ["34 percent", "66 percent", "70 percent", "68 percent"], 3,
 "340 divided by 500 times 100 gives 68 percent.",
 "The remaining 32 percent are female.", [734]),
(S, "In a school of 500 students, 340 are male. What percentage of the students is female?", ["32 percent", "34 percent", "36 percent", "68 percent"], 0,
 "Females are 500 minus 340, which is 160. Then 160 divided by 500 times 100 gives 32 percent.",
 "Males make up 68 percent.", [903]),
(S, "Out of 500 students, 360 are present. What percentage of students is absent?", ["32 percent", "26 percent", "28 percent", "72 percent"], 2,
 "Absent students are 500 minus 360, which is 140. Then 140 divided by 500 times 100 gives 28 percent.",
 "Present students here are 72 percent.", [2933]),
(S, "In a class there are 500 students and 340 are present. What percentage of the students is present?", ["68 percent", "34 percent", "32 percent", "66 percent"], 0,
 "340 divided by 500 times 100 gives 68 percent.",
 "The absent students are 32 percent.", [2480]),
(S, "In a class of 1500 students, 360 are boys. What percentage of the students is girls?", ["24 percent", "72 percent", "76 percent", "74 percent"], 2,
 "Girls are 1500 minus 360, which is 1140. Then 1140 divided by 1500 times 100 gives 76 percent.",
 "Boys here are 24 percent.", [2468]),
(S, "In a class of 400 students, 360 are boys. What percentage of the students is girls?", ["10 percent", "9 percent", "90 percent", "40 percent"], 0,
 "Girls are 400 minus 360, which is 40. Then 40 divided by 400 times 100 gives 10 percent.",
 "Boys here are 90 percent.", [2476]),
(S, "In a class of 500 students, 360 are boys. What percentage of the students is girls?", ["72 percent", "36 percent", "28 percent", "30 percent"], 2,
 "Girls are 500 minus 360, which is 140. Then 140 divided by 500 times 100 gives 28 percent.",
 "Boys here are 72 percent.", [2478]),
(S, "Which is the third largest city of Pakistan by population?", ["Rawalpindi", "Faisalabad", "Multan", "Peshawar"], 1,
 "By population Karachi is first, Lahore second and Faisalabad third, in both the 2017 and 2023 censuses.",
 "Faisalabad was formerly called Lyallpur.", [218]),
(S, "Who was the third Governor-General of Pakistan?", ["Ghulam Muhammad", "Khawaja Nazimuddin", "Iskander Mirza", "Liaquat Ali Khan"], 0,
 "The Governors-General were Quaid-e-Azam, Khawaja Nazimuddin, Ghulam Muhammad (1951-55) and then Iskander Mirza.",
 "Iskander Mirza became the first President of Pakistan in 1956.", [693]),
]

DUPS = [
(808, 4405), (808, 4406), (1503, 5327), (470, 336), (856, 4571), (1197, 657), (1415, 1331),
(1203, 705), (1203, 1489), (1138, 1324), (1501, 692), (1501, 111), (1502, 5316),
(1638, 3290), (4, 2470), (10, 867), (394, 527), (141, 3273), (1583, 2408),
]
