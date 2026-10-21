MATCH = [(276, 295), (300, 11)]
NEW = [
(277, "Islamiat", "On which night was the five daily prayers (Salah) made obligatory for Muslims?", "Night of Miraj (Shab-e-Miraj)", ["Laylat-ul-Qadr", "Shab-e-Barat", "Night of Hijrat"], "The five daily prayers were prescribed during the Isra and Miraj journey of the Prophet (PBUH), when 50 prayers were reduced to five.", 0),
(278, "Pakistan Studies", "Who was the head of state under the 1962 Constitution of Pakistan?", "The President", ["The Prime Minister", "The Governor General", "The Chief Justice"], "The 1962 Constitution gave Pakistan a presidential system in which the President was both head of state and head of government; the post of Prime Minister was abolished.", 0),
(281, "General Knowledge", "What is the currency of Russia?", "Ruble", ["Rupee", "Dinar", "Lira"], "The official currency of Russia is the Russian ruble (code RUB), issued by the Central Bank of Russia.", 0),
(285, "Pakistan Studies", "In which year was the One Unit scheme implemented in Pakistan?", "1955", ["1947", "1956", "1962"], "The One Unit scheme merged the western provinces into West Pakistan in 1955 (Act passed 30 September 1955, in force 14 October 1955) and was ended in 1970.", 0),
(286, "Current Affairs", "On which date is the International Day to Combat Islamophobia observed?", "15 March", ["5 February", "5 August", "14 August"], "The UN General Assembly declared 15 March as the International Day to Combat Islamophobia in 2022, on a resolution moved by Pakistan and the OIC.", 0),
(289, "Current Affairs", "Who is the Prime Minister of France (as of October 2026)?", "Sebastien Lecornu", ["Francois Bayrou", "Gabriel Attal", "Michel Barnier"], "Sebastien Lecornu has been Prime Minister of France since 9 September 2025 and was still in office in October 2026.", 0),
(290, "Verbal: Maths & Reasoning", "If the 5th day of a month is Friday, what day will the 28th be?", "Sunday", ["Saturday", "Friday", "Monday"], "From the 5th to the 28th is 23 days; 23 = 3 weeks + 2 days, so Friday + 2 = Sunday.", 0),
(291, "Pakistan Studies", "In 2020, Kashmir Highway in Islamabad was renamed as:", "Srinagar Highway", ["Muzaffarabad Highway", "Jinnah Avenue", "Kargil Highway"], "In August 2020 Kashmir Highway was renamed Srinagar Highway to show solidarity with Kashmiris on the first Youm-e-Istehsal.", 0),
(292, "Verbal: Maths & Reasoning", "If the 1st day of a month is Monday, what day will the 15th be?", "Monday", ["Sunday", "Tuesday", "Saturday"], "From the 1st to the 15th is 14 days, exactly two weeks, so the day is the same: Monday.", 0),
(293, "Pakistan Studies", "In which district of Punjab is Rohtas Fort located?", "Jhelum", ["Rawalpindi", "Lahore", "Attock"], "Rohtas Fort was built by Sher Shah Suri near Dina in Jhelum district and is a UNESCO World Heritage Site since 1997.", 0),
(295, "Pakistan Studies", "Who signed the Indus Waters Treaty (1960) on behalf of Pakistan?", "Field Marshal Ayub Khan", ["Liaquat Ali Khan", "Zulfikar Ali Bhutto", "Iskander Mirza"], "The treaty was signed in Karachi on 19 September 1960 by President Ayub Khan of Pakistan and Prime Minister Nehru of India, with the World Bank also signing.", 0),
(296, "Pakistan Studies", "In which city is the Pakistan Navy Headquarters (Naval Headquarters) located?", "Islamabad", ["Karachi", "Lahore", "Gwadar"], "Naval Headquarters was shifted from Karachi to Islamabad in 1975 and is in Sector E-9, Islamabad.", 0),
(298, "Verbal: Maths & Reasoning", "What is 40% of 60?", "24", ["20", "22", "26"], "40% of 60 = 40/100 x 60 = 24.", 0),
]
SKIPPED = {
279: "context not given (President elected by whom/which constitution)",
280: "vague, no concrete question (subcontinent called what)",
282: "ambiguous: Islamabad and Dhaka are both capitals, Dubai is not",
283: "ambiguous: who had the Munafiq title not specific",
284: "ambiguous: several cities (Karachi, Gwadar, Pasni, Ormara) lie on the coast",
287: "numbers 8, 12, 15 given but the proportion question is not clear",
288: "ambiguous first governor of Sindh (British era vs after 1947), sources unclear",
294: "ambiguous which percentage (provincial vs central seats), sources differ",
297: "x is not given, cannot form a question",
299: "x is not given, cannot form a question",
}
