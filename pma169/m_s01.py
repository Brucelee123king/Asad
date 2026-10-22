V = "Verbal: Maths & Reasoning"
E = "Verbal: English"
MATCH = [(1,55),(2,48),(3,52),(8,33),(9,53),(10,0),(11,364),(14,37),(19,273),(22,517),(26,377),(27,138),(28,522),(31,95),(35,385)]
NEW = [
(4, V, "Ali is 9 years old and Hareem is twice his age. How old will Hareem be when Ali is 13?", "22 years", ["26 years", "18 years", "20 years"], "Hareem is now 18. Ali needs 4 more years to reach 13, so Hareem will be 18 + 4 = 22.", 0),
(5, V, "Ali is 5 years old and his sister is four times his age. How old will the sister be when Ali is 10?", "25 years", ["40 years", "20 years", "30 years"], "Sister is now 4 x 5 = 20. Ali needs 5 more years, so she will be 20 + 5 = 25.", 0),
(6, V, "If yesterday was Saturday, what day will it be the day after tomorrow?", "Tuesday", ["Monday", "Wednesday", "Sunday"], "Yesterday Saturday means today is Sunday. Tomorrow is Monday and the day after tomorrow is Tuesday.", 0),
(7, V, "If the 14th day of a month is Sunday, what day is the 26th of the same month?", "Friday", ["Thursday", "Saturday", "Sunday"], "26 - 14 = 12 days later. 12 = 7 + 5, so move 5 days after Sunday, which is Friday.", 0),
(13, V, "Ali walks towards the north, turns left and walks 5 m, then turns left again. In which direction is he facing now?", "South", ["North", "East", "West"], "Facing north, a left turn gives west. Another left turn from west gives south.", 0),
(17, V, "Akbar was born in 1980 and Aslam in 1987. Bilal is elder than Aslam but younger than Akbar. What is the order from eldest to youngest?", "Akbar, Bilal, Aslam", ["Aslam, Bilal, Akbar", "Bilal, Akbar, Aslam", "Akbar, Aslam, Bilal"], "Akbar (1980) is eldest and Aslam (1987) is youngest. Bilal is younger than Akbar and elder than Aslam, so he is in the middle.", 0),
(20, E, "Choose the synonym of BRAVE.", "Courageous", ["Timid", "Weak", "Lazy"], "Brave means ready to face danger without fear, which is the meaning of courageous.", 0),
(21, E, "Choose the word closest in meaning to DISTURB.", "Bother", ["Calm", "Soothe", "Assist"], "To disturb is to interrupt or trouble someone, which is the meaning of bother.", 0),
(29, E, "Choose the synonym of NIBBLE.", "Bite gently", ["Swallow whole", "Throw away", "Shout"], "To nibble is to take small gentle bites, as dictionary.com defines it.", 0),
(30, E, "Choose the synonym of MEDIATE.", "Arbitrate", ["Ignore", "Quarrel", "Refuse"], "To mediate is to step in between two sides to settle a dispute. Dictionary.com lists arbitrate as its synonym.", 0),
(32, "Islamiat", "Which pillar of Islam was made obligatory for the Muslims on the night of Miraj?", "Salat (five daily prayers)", ["Zakat", "Sawm (fasting)", "Hajj"], "The five daily prayers were prescribed during the Isra and Miraj journey, the Prophet PBUH brought them back for his Ummah.", 0),
(33, "General Knowledge", "In which sport is the word 'love' used for a score of zero?", "Tennis", ["Cricket", "Hockey", "Football"], "In tennis a score of zero is called love, probably from the French l'oeuf (egg).", 0),
(34, "General Knowledge", "24 January is observed every year as the International Day of:", "Education", ["Women", "Peace", "Literacy"], "The UN General Assembly proclaimed 24 January International Day of Education in December 2018, first observed in 2019.", 0),
(36, "Pakistan Studies", "Who was the President of Pakistan during the 1965 war with India?", "Field Marshal Muhammad Ayub Khan", ["General Yahya Khan", "Iskander Mirza", "Zulfikar Ali Bhutto"], "Ayub Khan was President from 1958 to 1969 and led Pakistan in the August to September 1965 war.", 0),
(37, V, "What is the product of two negative integers?", "A positive integer", ["A negative integer", "Zero", "Cannot be determined"], "A negative times a negative is positive, for example (-3) x (-4) = 12.", 0),
]
SKIPPED = {
12: "Unclear question (quarter of 1/10 of 90 gives 2.25 but write-up garbled with 10, 12)",
15: "Options unknown, odd-one-out sets unclear",
16: "Mirror image of 2 and 5 depends on mirror axis, unclear",
18: "Words not remembered",
23: "Unclear which tense is intended (past perfect vs past continuous), sources not definitive",
24: "Unclear what rearranging BEAUTY should produce",
25: "Sources could not confirm Liaquat Ali Khan first foreign visit (Moscow invitation vs USA 1950)",
}
