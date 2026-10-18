S = "Hakeem Force Academy"
QS = []
def add(q, opts, ci, reason, fact, ids):
    QS.append((S, q, opts, ci, reason, fact, ids))

def cap(q, ans, wrongs, pos, reason, fact, ids):
    o = list(wrongs)
    o.insert(pos, ans)
    add(q, o, pos, reason, fact, ids)

cap("Accra is the capital of which country?", "Ghana", ["Nigeria", "Togo", "Senegal"], 1,
    "Accra is the capital and largest city of Ghana, on the Gulf of Guinea.",
    "Ghana was the first sub-Saharan African country to gain independence from Britain, in 1957.", [370])
cap("Lusaka is the capital of which country?", "Zambia", ["Zimbabwe", "Malawi", "Tanzania"], 2,
    "Lusaka is the capital and largest city of Zambia.",
    "Zambia was formerly called Northern Rhodesia and became independent in 1964.", [2483])
cap("Maputo is the capital of which country?", "Mozambique", ["Madagascar", "Angola", "Namibia"], 0,
    "Maputo, formerly Lourenco Marques, is the capital of Mozambique.",
    "Mozambique gained independence from Portugal in 1975.", [272, 3228])
cap("Moroni is the capital of which country?", "Comoros", ["Mauritius", "Seychelles", "Madagascar"], 3,
    "Moroni is the capital of the Union of the Comoros, an island nation in the Indian Ocean.",
    "Comoros lies between Mozambique and Madagascar.", [780])
cap("Reykjavik is the capital of which country?", "Iceland", ["Greenland", "Norway", "Ireland"], 1,
    "Reykjavik is the capital and largest city of Iceland.",
    "Reykjavik is the northernmost capital of a sovereign state in the world.", [26])
cap("Saint John's is the capital of which country?", "Antigua and Barbuda", ["Jamaica", "Barbados", "Saint Lucia"], 2,
    "Saint John's is the capital of Antigua and Barbuda, on the island of Antigua.",
    "Antigua and Barbuda became independent from Britain in 1981.", [811, 3214])
cap("San Jose is the capital of which country?", "Costa Rica", ["Panama", "Nicaragua", "Honduras"], 0,
    "San Jose is the capital and largest city of Costa Rica in Central America.",
    "Costa Rica abolished its army in 1948.", [812])
cap("Tallinn is the capital of which country?", "Estonia", ["Latvia", "Lithuania", "Finland"], 3,
    "Tallinn is the capital and largest city of Estonia, on the Gulf of Finland.",
    "Estonia, Latvia and Lithuania are the three Baltic states.", [2702, 151])
cap("What is the capital of Algeria?", "Algiers", ["Tunis", "Rabat", "Tripoli"], 1,
    "Algiers is the capital and largest city of Algeria.",
    "Algeria is the largest country in Africa by area since the split of Sudan in 2011.", [917])
cap("What is the official capital of Benin?", "Porto-Novo", ["Cotonou", "Lome", "Abuja"], 2,
    "Porto-Novo is the official capital of Benin, although the government sits in Cotonou.",
    "Cotonou is the largest city and economic centre of Benin.", [3215])
cap("What is the constitutional capital of Bolivia?", "Sucre", ["Lima", "Quito", "Asuncion"], 0,
    "Bolivia's constitution names Sucre as its capital.",
    "The government and legislature sit in La Paz, which is the seat of government.", [3216])
cap("What is the capital of Bosnia and Herzegovina?", "Sarajevo", ["Zagreb", "Belgrade", "Skopje"], 1,
    "Sarajevo is the capital and largest city of Bosnia and Herzegovina.",
    "The 1914 assassination of Archduke Franz Ferdinand in Sarajevo triggered World War I.", [3217])
cap("What is the capital of Egypt?", "Cairo", ["Alexandria", "Giza", "Khartoum"], 2,
    "Cairo is the capital and largest city of Egypt, on the River Nile.",
    "Egypt is building a New Administrative Capital east of Cairo.", [3219])
cap("What is the capital of Ethiopia?", "Addis Ababa", ["Nairobi", "Asmara", "Khartoum"], 0,
    "Addis Ababa is the capital of Ethiopia.",
    "Addis Ababa hosts the headquarters of the African Union.", [918])
cap("What is the capital of Fiji?", "Suva", ["Apia", "Port Moresby", "Nuku'alofa"], 3,
    "Suva is the capital and largest city of Fiji, on Viti Levu island.",
    "Fiji is an island country in the South Pacific.", [919])
cap("What is the capital of Finland?", "Helsinki", ["Stockholm", "Oslo", "Tallinn"], 1,
    "Helsinki is the capital and largest city of Finland.",
    "Finland joined NATO in April 2023.", [920])
cap("What is the capital of Great Britain (the United Kingdom)?", "London", ["Edinburgh", "Cardiff", "Manchester"], 2,
    "London is the capital of the United Kingdom and England.",
    "Edinburgh, Cardiff and Belfast are capitals of Scotland, Wales and Northern Ireland.", [3220])
cap("What is the capital of Greenland?", "Nuuk", ["Reykjavik", "Oslo", "Copenhagen"], 0,
    "Nuuk is the capital and largest city of Greenland.",
    "Greenland is an autonomous territory of the Kingdom of Denmark.", [360])
cap("What is the capital of Kazakhstan?", "Astana", ["Almaty", "Tashkent", "Bishkek"], 2,
    "Astana is the capital of Kazakhstan; it replaced Almaty as capital in 1997.",
    "Astana was renamed Nur-Sultan in 2019 and returned to the name Astana in 2022.", [5])
cap("What is the capital of Kenya?", "Nairobi", ["Mombasa", "Kampala", "Dodoma"], 1,
    "Nairobi is the capital and largest city of Kenya.",
    "Nairobi hosts a major United Nations office, UNEP headquarters.", [922])
cap("What is the capital of Latvia?", "Riga", ["Vilnius", "Tallinn", "Minsk"], 0,
    "Riga is the capital and largest city of Latvia.",
    "Latvia is one of the three Baltic states.", [28])
cap("What is the capital of Liberia?", "Monrovia", ["Freetown", "Accra", "Conakry"], 3,
    "Monrovia is the capital of Liberia and is named after US President James Monroe.",
    "Liberia was founded by freed African American slaves.", [3222])
cap("What is the capital of Madagascar?", "Antananarivo", ["Maputo", "Moroni", "Port Louis"], 1,
    "Antananarivo is the capital and largest city of Madagascar.",
    "Madagascar is the fourth largest island in the world.", [3223])
cap("What is the capital of Mongolia?", "Ulaanbaatar", ["Beijing", "Astana", "Hohhot"], 2,
    "Ulaanbaatar (Ulan Bator) is the capital of Mongolia.",
    "Ulaanbaatar is one of the coldest capital cities in the world.", [3225])
cap("What is the capital of Morocco?", "Rabat", ["Casablanca", "Marrakesh", "Tunis"], 0,
    "Rabat is the capital of Morocco.",
    "Casablanca is the largest city of Morocco.", [3227])
cap("What is the capital of Norway?", "Oslo", ["Bergen", "Stockholm", "Copenhagen"], 0,
    "Oslo is the capital and largest city of Norway.",
    "Norway is not a member of the European Union.", [474])
cap("What is the capital of Turkmenistan?", "Ashgabat", ["Tashkent", "Dushanbe", "Bishkek"], 3,
    "Ashgabat is the capital of Turkmenistan.",
    "Turkmenistan is a Central Asian country bordering Iran and Afghanistan.", [3236])
cap("What is the capital of Uzbekistan?", "Tashkent", ["Samarkand", "Bukhara", "Astana"], 1,
    "Tashkent is the capital and largest city of Uzbekistan.",
    "The 1966 Tashkent Declaration between Pakistan and India was signed in this city.", [3238])
cap("What is the capital of Vietnam?", "Hanoi", ["Ho Chi Minh City", "Bangkok", "Vientiane"], 2,
    "Hanoi is the capital of Vietnam.",
    "Ho Chi Minh City (formerly Saigon) is the largest city of Vietnam.", [3239])
cap("What is the capital of Zimbabwe?", "Harare", ["Bulawayo", "Lusaka", "Gaborone"], 0,
    "Harare is the capital and largest city of Zimbabwe.",
    "Harare was formerly called Salisbury.", [294])

add("In which years were the Olympic Games cancelled because of World War II?",
    ["1940 and 1944", "1938 and 1942", "1942 and 1946", "1936 and 1940"], 0,
    "The 1940 Games (Tokyo/Helsinki) and the 1944 Games (London) were cancelled due to the war.",
    "The Olympics were also cancelled in 1916 because of World War I.", [762, 2427])
add("In which years was the FIFA World Cup not held because of World War II?",
    ["1938 and 1942", "1942 and 1946", "1940 and 1944", "1946 and 1950"], 1,
    "The World Cup was held in 1938 and then next in 1950, so the 1942 and 1946 tournaments were cancelled.",
    "Brazil hosted the 1950 World Cup, the first after the war.", [2430])
add("What is the currency of Canada?",
    ["Canadian dollar", "Canadian pound", "US dollar", "Canadian franc"], 0,
    "Canada uses the Canadian dollar (CAD).",
    "The Canadian one dollar coin is nicknamed the loonie.", [3312])
add("Which dam in Pakistan was built with the help of Canada under the Colombo Plan?",
    ["Warsak Dam", "Mangla Dam", "Tarbela Dam", "Diamer-Bhasha Dam"], 0,
    "Warsak Dam on the Kabul River near Peshawar was built in the 1950s with Canadian aid under the Colombo Plan.",
    "Mangla Dam was built on the Jhelum River and Tarbela Dam on the Indus River.", [4358])
add("Who is the captain of the Pakistan women's cricket team in 2026?",
    ["Bismah Maroof", "Nida Dar", "Fatima Sana", "Muneeba Ali"], 2,
    "Fatima Sana leads Pakistan women's team, including at the 2026 Women's T20 World Cup.",
    "Before Fatima Sana, Nida Dar and Bismah Maroof had captained the side.", [3562])
add("In which year did the US-led invasion of Afghanistan begin?",
    ["1999", "2001", "2003", "2005"], 1,
    "After the attacks of 11 September 2001, the US-led forces invaded Afghanistan in October 2001.",
    "US and NATO forces withdrew from Afghanistan in August 2021 and the Taliban returned to power.", [3992])
add("Change the narration: The captain said to his men, \"Stand at ease.\"",
    ["The captain told his men that they stood at ease.", "The captain commanded his men to stand at ease.",
     "The captain asked his men if they stood at ease.", "The captain said to his men that stand at ease."], 1,
    "The quoted sentence is an order, so the reporting verb becomes commanded and the order is turned into an infinitive.",
    "Imperative sentences in indirect speech use words such as ordered, commanded, requested or advised.", [1596])
add("What are the members of a Cartesian plane called?",
    ["Ordered pairs", "Vectors", "Sets", "Matrices"], 0,
    "Every point of a Cartesian plane is written as an ordered pair (x, y) of coordinates.",
    "The Cartesian plane is named after the French mathematician Rene Descartes.", [835])
add("Choose the part of speech of the word 'but' in: I ran fast to catch the train but I was late.",
    ["Preposition", "Conjunction", "Adverb", "Interjection"], 1,
    "Here 'but' joins two clauses showing contrast, so it is a coordinating conjunction.",
    "The coordinating conjunctions are for, and, nor, but, or, yet and so.", [1607])
add("Change into passive voice: Dogs always chase the cats.",
    ["The cats are always chased by dogs.", "The cats were always chased by dogs.",
     "The cats are always being chased by dogs.", "The cats always chase the dogs."], 0,
    "The sentence is present simple, so the passive is 'am/is/are + past participle': the cats are always chased by dogs.",
    "The 'being' form is used only for the present continuous passive.", [643])
add("Change the voice: Dogs always chased cats.",
    ["Cats are always chased by dogs.", "Cats have always been chased by dogs.",
     "Cats were always chased by dogs.", "Cats were always being chased by dogs."], 2,
    "The sentence is past simple, so the passive uses 'was/were + past participle': cats were always chased by dogs.",
    "In passive voice the object of the active sentence becomes the subject.", [1601])
add("What causes earthquakes, including those under the ocean?",
    ["Movement of tectonic plates", "Strong ocean winds", "Heavy rainfall", "Lunar eclipses"], 0,
    "Earthquakes occur when tectonic plates slip or collide and release energy along faults, on land or the sea floor.",
    "A big undersea earthquake can cause a tsunami.", [2859, 2860])
add("In which city is the World Trade Center located?",
    ["Washington D.C.", "Chicago", "Los Angeles", "New York City"], 3,
    "The World Trade Center complex is in Lower Manhattan, New York City.",
    "The original Twin Towers were destroyed in the attacks of 11 September 2001.", [4223])
add("What was the name of the camel of Prophet Muhammad (PBUH)?",
    ["Qaswa", "Duldul", "Buraq", "Adba"], 0,
    "The Prophet's well-known camel was named Qaswa, which he rode during the Hijrat.",
    "Sources also mention the name Adba for his camel, and Duldul was his mule.", [3920])
add("In which year did Pakistan join CENTO (the Baghdad Pact)?",
    ["1952", "1954", "1955", "1959"], 2,
    "Pakistan joined the Baghdad Pact in 1955, which was renamed CENTO in 1959.",
    "Pakistan left CENTO in 1979 after Iran withdrew.", [4013])
add("What is the center of a circle called?",
    ["Origin of the circumference", "Focus", "Vertex", "Point from which all boundary points are equidistant"], 3,
    "The center is the fixed point inside a circle that is at the same distance from every point on the circle.",
    "The fixed distance is called the radius.", [610])
add("In a circle, what is the distance from the center to any point on the circle called?",
    ["Diameter", "Radius", "Chord", "Circumference"], 1,
    "The distance from the center to a point on the circle is the radius.",
    "The diameter is twice the radius.", [402])
add("On a farm, the cows are 5, the camels are three times the cows and the goats are three times the camels. How many animals are there in total?",
    ["55", "60", "65", "75"], 2,
    "Cows = 5, camels = 3 x 5 = 15, goats = 3 x 15 = 45. Total = 5 + 15 + 45 = 65.",
    "Always compute each group step by step before adding.", [2539])

DUPS = [(602,167),(1532,2802),(2184,2880),(3183,2106),(1927,4885),(866,1955),(866,1957),
 (274,2128),(274,4068),(2193,728),(1040,3210),(573,3587),(1304,1688),(116,2477),(1164,269),
 (1078,2776),(1078,2778),(2037,2001),(1643,3245),(2776,2861),(2776,2862),(1064,4797),(1064,4900),
 (612,3893),(506,2719),(990,2261),(2216,4056),(2194,2366),(482,4553),(2625,4028)]
