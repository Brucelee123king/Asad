S = "Hakeem Force Academy"
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def ordn(n):
    if 10 <= n % 100 <= 20:
        return str(n) + "th"
    return str(n) + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

def dayq(ids, known, d1, d2, pos):
    k = DAYS.index(known)
    diff = d2 - d1
    ans = DAYS[(k + diff) % 7]
    ai = DAYS.index(ans)
    wrong = [DAYS[(ai + s) % 7] for s in (1, 2, 3)]
    opts = wrong[:]
    opts.insert(pos, ans)
    step = "%d days later" % diff if diff >= 0 else "%d days earlier" % (-diff)
    r = "From the %s to the %s is %s. %d divided by 7 leaves remainder %d, so move %d day(s) %s from %s to reach %s." % (
        ordn(d1), ordn(d2), step, abs(diff), abs(diff) % 7, abs(diff) % 7,
        "forward" if diff >= 0 else "backward", known, ans)
    q = "If the %s day of a month is %s, what day will the %s of that month be?" % (ordn(d1), known, ordn(d2))
    return (S, q, opts, pos, r, "A week has 7 days, so the same weekday repeats every 7 days of the month.", ids)

QS = [
 (S, "Who was the Speaker (President) of the Constituent Assembly of Pakistan from 1948, after Quaid-e-Azam?",
  ["Maulvi Tamizuddin Khan", "Liaquat Ali Khan", "Khawaja Nazimuddin", "Chaudhry Muhammad Ali"], 0,
  "Maulvi Tamizuddin Khan became President (Speaker) of the Constituent Assembly of Pakistan in 1948 and held the post until 1954.",
  "In 1954 Tamizuddin Khan challenged the dissolution of the Assembly by Governor General Ghulam Muhammad in court.", [517]),
 (S, "Which constitution of Pakistan was made in 1956?",
  ["The first constitution of Pakistan", "The second constitution of Pakistan", "The third constitution of Pakistan", "The Interim Constitution"], 0,
  "The Constituent Assembly passed the first constitution of Pakistan in 1956, which made the country an Islamic Republic.",
  "It was abrogated by President Iskander Mirza in October 1958.", [3918]),
 (S, "Which constitution of Pakistan was enforced in 1962?",
  ["The second constitution, with a presidential system", "The first constitution, with a parliamentary system", "The third constitution, with a parliamentary system", "The Government of India Act 1935"], 0,
  "The 1962 constitution was the second constitution of Pakistan and gave a presidential system with strong powers to the President.",
  "It was given by President Ayub Khan and ended in 1969 when Yahya Khan imposed martial law.", [292, 718]),
 (S, "Who was the President of Pakistan under the 1962 constitution in 1962?",
  ["Iskander Mirza", "Yahya Khan", "Ayub Khan", "Ghulam Muhammad"], 2,
  "Field Marshal Ayub Khan was President of Pakistan from 1958 to 1969, and he introduced the 1962 constitution.",
  "Ayub Khan was the first Pakistani Commander-in-Chief of the Pakistan Army.", [779, 2086]),
 (S, "Who was the President of Pakistan during the 1971 war with India?",
  ["Zulfikar Ali Bhutto", "Yahya Khan", "Ayub Khan", "Zia ul Haq"], 1,
  "General Yahya Khan was President from March 1969 until 20 December 1971, so he was President during the December 1971 war.",
  "Zulfikar Ali Bhutto took over as President and Chief Martial Law Administrator on 20 December 1971.", [4744, 4749, 780]),
 (S, "Who was the Prime Minister of Pakistan during the December 1971 war?",
  ["Zulfikar Ali Bhutto", "Nurul Amin", "Liaquat Ali Khan", "Muhammad Khan Junejo"], 1,
  "Nurul Amin was appointed Prime Minister on 7 December 1971 and held office during the war, which ended on 16 December.",
  "He later served as Vice President of Pakistan under Zulfikar Ali Bhutto.", [4743, 1380]),
 (S, "In which city was the second Islamic Summit Conference of the OIC held in 1974?",
  ["Rabat", "Cairo", "Lahore", "Islamabad"], 2,
  "The second OIC Islamic Summit took place in Lahore in February 1974 and was hosted by Prime Minister Zulfikar Ali Bhutto.",
  "The first Islamic Summit was held in Rabat, Morocco, in 1969.", [278, 3844, 3843]),
 (S, "Which country won the 1974 FIFA World Cup?",
  ["Netherlands", "Brazil", "West Germany", "Argentina"], 2,
  "West Germany beat the Netherlands 2-1 in the final in Munich to win the 1974 FIFA World Cup.",
  "West Germany had also won the World Cup in 1954.", [378]),
 (S, "What was the first amendment to the 1973 Constitution of Pakistan about?",
  ["Recognition of Bangladesh by changing the definition of the territories of Pakistan", "Declaring Ahmadis non-Muslims", "Allowing the President to dissolve the Assembly", "Changing the name of the country"], 0,
  "The First Amendment of 1974 changed Article 1 so that the territories of Pakistan no longer included East Pakistan, after Bangladesh was recognized.",
  "The Second Amendment of 1974 declared Ahmadis non-Muslims for the purposes of the Constitution.", [3503]),
 (S, "Who was the Prime Minister of Pakistan during the 1999 Kargil conflict?",
  ["Benazir Bhutto", "Pervez Musharraf", "Nawaz Sharif", "Zafarullah Khan Jamali"], 2,
  "Nawaz Sharif was Prime Minister from 1997 until October 1999, so he was in office during the Kargil conflict.",
  "General Pervez Musharraf removed him in a coup on 12 October 1999.", [4754]),
 (S, "On which date was the first Cricket World Cup final played in 1975?",
  ["7 June 1975", "21 June 1975", "14 June 1975", "1 June 1975"], 1,
  "The first Cricket World Cup was played in England in June 1975 and its final was held at Lord's on 21 June 1975.",
  "West Indies won that final by beating Australia.", [2482]),
 (S, "If a car covers 200 km in one hour, how many km will it cover in one minute?",
  ["2 km", "3.33 km", "4 km", "2.5 km"], 1,
  "One hour has 60 minutes, so distance in one minute is 200 divided by 60 = 3.33 km (10/3 km).",
  "Speed is distance divided by time.", [888]),
 (S, "A plane uses 60 gallons of fuel to cover 90 km. How many gallons are needed to cover 200 km?",
  ["120 gallons", "150 gallons", "133.33 gallons", "180 gallons"], 2,
  "Fuel per km is 60/90 = 2/3 gallon. For 200 km: 200 x 2/3 = 133.33 gallons.",
  "Fuel needed is directly proportional to the distance covered.", [1957]),
 (S, "Who won the 2014 ICC World Twenty20 (T20 World Cup)?",
  ["India", "Sri Lanka", "West Indies", "Pakistan"], 1,
  "Sri Lanka beat India by six wickets in the final at Dhaka in April 2014.",
  "Pakistan's only T20 World Cup win was in 2009.", [4779]),
 (S, "Who won the 2023 ICC Men's Cricket World Cup?",
  ["India", "Australia", "England", "New Zealand"], 1,
  "Australia beat hosts India by six wickets in the final at Ahmedabad on 19 November 2023.",
  "It was Australia's sixth World Cup title.", [4780]),
 (S, "Who was the Chief Justice of Pakistan in 2018?",
  ["Mian Saqib Nisar", "Asif Saeed Khosa", "Iftikhar Muhammad Chaudhry", "Gulzar Ahmed"], 0,
  "Mian Saqib Nisar was Chief Justice of Pakistan from December 2016 until January 2019, which covers all of 2018.",
  "Asif Saeed Khosa succeeded him in January 2019.", [4661, 4662]),
 (S, "What is the value of 2 + 2 x 3?",
  ["12", "8", "10", "6"], 1,
  "By BODMAS, multiplication comes first: 2 x 3 = 6. Then 2 + 6 = 8.",
  "Brackets, orders, division and multiplication, then addition and subtraction is the correct order of operations.", [2819]),
 (S, "In a class of 500 students, 340 are boys. What percentage of the students are girls?",
  ["68%", "30%", "34%", "32%"], 3,
  "Girls = 500 - 340 = 160. Percentage = 160/500 x 100 = 32%.",
  "The percentage of boys here is 68%, and the two percentages add up to 100%.", [137]),
 (S, "In a class of 500 students, 340 are present. What percentage of the students are present?",
  ["68%", "70%", "66%", "80%"], 0,
  "Percentage present = 340/500 x 100 = 68%.",
  "Percentage = (part / whole) x 100.", [2030]),
 dayq([902], "Sunday", 4, 19, 1),
 dayq([1991], "Monday", 2, 19, 2),
 dayq([1985], "Monday", 4, 20, 0),
 dayq([1993], "Friday", 2, 20, 3),
 dayq([2001, 2003], "Monday", 4, 22, 1),
 dayq([1997], "Monday", 31, 25, 2),
 dayq([903], "Thursday", 3, 25, 0),
 dayq([1995, 2022], "Friday", 2, 27, 3),
 dayq([1989], "Monday", 12, 29, 1),
 dayq([904], "Monday", 4, 29, 2),
 dayq([1998], "Monday", 31, 20, 0),
 dayq([1999], "Monday", 31, 2, 3),
]

DUPS = [
 (59 if False else 1750, 771),
 (3423, 310), (3423, 3071),
 (1658, 4741),
 (815, 1616),
 (446, 255), (446, 1026),
 (1718, 4753),
 (1680, 4597), (1680, 4598),
 (104, 794), (104, 946),
 (475, 991), (475, 1096),
 (353, 486),
 (871, 136),
 (1218, 3072),
 (937, 4223),
 (1104, 806),
 (172, 519), (172, 2321), (172, 4329),
 (1628, 1145), (1628, 3445),
 (3105, 4049),
 (2247, 2023), (678, 907), (1435, 2021), (4108, 908), (2253, 2696), (3400, 2010),
]
