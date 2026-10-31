MATCH = [(307, 318), (317, 107), (325, 2)]
NEW = [
(301, "Verbal: Maths & Reasoning", "If the 3rd day of a month is Sunday, what day will the 15th day of that month be?", "Friday", ["Thursday", "Saturday", "Sunday"], "From the 3rd to the 15th is 12 days; 12 = 1 week + 5 days, so Sunday + 5 days = Friday.", 0),
(302, "Verbal: Maths & Reasoning", "Complete the series: 1A, 2D, 3H, ?", "4M", ["4L", "4N", "5M"], "Numbers go 1, 2, 3, 4. Letters A, D, H, M move forward by 3, 4, 5, so the next letter is M.", 0),
(304, "Verbal: Maths & Reasoning", "Cow is to milk as dog is to ?", "Bark", ["Fur", "Tail", "Bone"], "A cow gives milk and a dog gives a bark, the thing it produces.", 0),
(306, "Verbal: Maths & Reasoning", "Train A runs at 60 km/h and train B is twice as fast. How many km does train B cover in 30 minutes?", "60 km", ["30 km", "120 km", "90 km"], "Speed of B = 120 km/h. In 30 minutes (half an hour) it covers 120 x 1/2 = 60 km.", 0),
(308, "Islamiat", "In which city did the Quraish tribe live?", "Makkah", ["Madinah", "Taif", "Jeddah"], "The Quraish were the ruling tribe of Makkah and guardians of the Kaaba.", 0),
(309, "Pakistan Studies", "In which year was the first Round Table Conference held in London?", "1930", ["1929", "1931", "1932"], "The first Round Table Conference began on 12 November 1930 in London. The Congress did not attend.", 0),
(310, "Pakistan Studies", "Who started the Faraizi movement in Bengal?", "Haji Shariatullah", ["Syed Ahmad Barelvi", "Titu Mir", "Sir Syed Ahmad Khan"], "Haji Shariatullah founded the Faraizi movement in 1818 to make Bengali Muslims follow the obligatory duties (faraiz) of Islam. His son Dudu Miyan later led it.", 0),
(312, "Islamiat", "Which companion served the Prophet Muhammad (PBUH) for ten years?", "Hazrat Anas bin Malik (R.A.)", ["Hazrat Abu Hurairah (R.A.)", "Hazrat Bilal (R.A.)", "Hazrat Zaid bin Thabit (R.A.)"], "Hazrat Anas bin Malik (R.A.) served the Prophet (PBUH) for ten years in Madinah, starting as a boy.", 0),
(313, "Pakistan Studies", "Iran, Turkey and Pakistan formed which organization in 1964?", "Regional Cooperation for Development (RCD)", ["Economic Cooperation Organization (ECO)", "SEATO", "Baghdad Pact"], "RCD was founded in July 1964 by Iran, Pakistan and Turkey for economic and social development. It was replaced by ECO in 1985.", 0),
(314, "General Knowledge", "In which year did the UN General Assembly adopt the Universal Declaration of Human Rights?", "1948", ["1945", "1950", "1956"], "The Declaration was adopted on 10 December 1948 as resolution 217 A (III) in Paris.", 0),
(315, "General Knowledge", "Which is the national bird of Pakistan?", "Chukar (Chakor)", ["Peacock", "Sparrow", "Shaheen"], "The chukar partridge (chakor) is the national bird of Pakistan.", 0),
(318, "Verbal: English", "Choose the synonym of JUBILANT.", "Joyful", ["Sorrowful", "Angry", "Fearful"], "Jubilant means feeling or showing great joy, so joyful is the closest meaning.", 0),
(319, "Verbal: English", "Choose the antonym of GLORY.", "Disgrace", ["Honour", "Fame", "Triumph"], "Glory means great honour and fame; its opposite is disgrace or shame.", 0),
(321, "Pakistan Studies", "In which year did Quaid-e-Azam Muhammad Ali Jinnah leave the Indian National Congress?", "1920", ["1913", "1916", "1928"], "Jinnah resigned from the Congress at its Nagpur session in December 1920 because he opposed Gandhi's non-cooperation movement.", 0),
(323, "Verbal: Maths & Reasoning", "Find the next letter in the series: A, C, F, ?", "J", ["I", "K", "H"], "Positions are 1, 3, 6, 10: gaps of 2, 3, 4. Next is 10, which is J.", 0),
(324, "Verbal: Maths & Reasoning", "What is 90% of 80?", "72", ["70", "76", "8"], "90% of 80 = 0.9 x 80 = 72.", 0),
]
SKIPPED = {
303: "Number series 1/22, 22/3, 5/33, 33/7 is garbled in write-ups; pattern unclear",
305: "Only a topic (miles per hour to minutes), no numbers given",
311: "Age of Hazrat Ali at martyrdom: sources differ (62/63/64), disputed",
316: "Pakistan's biggest award ambiguous (Nishan-e-Pakistan vs Nishan-e-Haider)",
320: "Article not specified, no concrete question",
322: "Year Fatima Jinnah joined Muslim League not clearly established, sources differ",
}
