S = "PMA 158 Long Course"
QS = []
_n = [0]
def add(q, ans, wrong, why, rel, rep=1):
    pos = _n[0] % 4
    _n[0] += 1
    opts = list(wrong)
    opts.insert(pos, ans)
    QS.append((S, q, opts, pos, why, rel, rep))

add("Where is Mina located?", "Near Makkah (about 5 km east of it)", ["Near Madina", "Near Jeddah", "Near Taif"],
    "Mina is a valley a few kilometres east of Makkah where pilgrims stay and stone the Jamarat during Hajj.",
    "Pilgrims spend the 8th to 13th Dhul Hijjah nights in the tents of Mina.")
add("How many gates does Jannah (Paradise) have?", "8", ["7", "10", "12"],
    "Authentic Ahadith state that Jannah has eight gates, one of which is Ar-Rayyan for those who fast.",
    "Jahannam, in contrast, has seven gates.")
add("Who will blow the Trumpet (Soor) on the Day of Judgment?", "Hazrat Israfil A.S", ["Hazrat Jibrail A.S", "Hazrat Mikail A.S", "Hazrat Izrail A.S"],
    "Angel Israfil A.S has been entrusted to blow the Soor to announce Qiyamat and again for resurrection.",
    "Jibrail brings revelation, Mikail looks after rain and provision, Izrail takes souls.")
add("According to Pakistani textbooks, in which year A.D. was the Holy Prophet (PBUH) born (in Rabi-ul-Awwal, commonly given as 22nd April)?", "571 A.D", ["570 A.D", "569 A.D", "575 A.D"],
    "The year of the Elephant is taken as 571 A.D in Pakistani textbooks, with the date given as 22nd April (12 Rabi-ul-Awwal). Some historians give 570 A.D.",
    "He was born in Makkah in the Year of the Elephant.")
add("What was the name of the father of the Holy Prophet (PBUH)?", "Hazrat Abdullah", ["Hazrat Abu Talib", "Hazrat Abdul Muttalib", "Hazrat Hamza"],
    "The father of the Prophet (PBUH) was Abdullah bin Abdul Muttalib, who died before the Prophet was born.",
    "Abdullah died in Madina on a trade journey, while Amina was pregnant.")
add("What was the name of the mother of the Holy Prophet (PBUH)?", "Hazrat Amina", ["Hazrat Fatima", "Hazrat Halima", "Hazrat Khadija"],
    "The mother of the Prophet (PBUH) was Amina bint Wahb of Banu Zuhra.",
    "She died at Abwa when the Prophet was about six years old.")
add("What was the name of the maternal grandfather of the Holy Prophet (PBUH)?", "Wahb bin Abd Manaf", ["Abdul Muttalib bin Hashim", "Abu Talib bin Abdul Muttalib", "Asad bin Hashim"],
    "Amina was the daughter of Wahb bin Abd Manaf, chief of Banu Zuhra, so he was the maternal grandfather.",
    "Abdul Muttalib chose Amina for his son Abdullah.")
add("What was the name of the maternal grandmother of the Holy Prophet (PBUH), as given in the list?", "Barrah (written Batarah in the list)", ["Fatima bint Amr", "Safiyya", "Sumayyah"],
    "Amina's mother was Barrah bint Abd al-Uzza, which the list spells as Batarah.",
    "Fatima bint Amr was the paternal grandmother, the mother of Abdullah.")
add("What was the real name of Abdul Muttalib, grandfather of the Holy Prophet (PBUH)?", "Shaybah", ["Abd Manaf", "Hashim", "Qusayy"],
    "Abdul Muttalib's real name was Shaybah; he was called Abdul Muttalib because he was brought up by his uncle Muttalib.",
    "He was the chief of Quraish and the custodian of Zamzam.")
add("What was the name of the paternal grandmother of the Holy Prophet (PBUH), the mother of Abdullah?", "Fatima bint Amr", ["Amina bint Wahb", "Barrah bint Abd al-Uzza", "Safiyya bint Abdul Muttalib"],
    "Abdullah's mother was Fatima bint Amr of Banu Makhzum, so she was the Prophet's paternal grandmother.",
    "Amina was his mother, not his grandmother.")
add("At what age did the Holy Prophet (PBUH) travel to Syria with his uncle Abu Talib?", "12 years", ["9 years", "15 years", "25 years"],
    "At age 12 he went with Abu Talib on a trade caravan, where the monk Bahira recognised signs of prophethood.",
    "His second trade trip to Syria, at 25, was for Khadija R.A.")
add("At what age did the Holy Prophet (PBUH) marry Hazrat Khadija R.A?", "25 years", ["20 years", "30 years", "40 years"],
    "He married Khadija R.A at age 25, while she was about 40.",
    "Khadija R.A was his first wife and all his children except Ibrahim were from her.")
add("Who was the first woman to accept Islam?", "Hazrat Khadija R.A", ["Hazrat Ayesha R.A", "Hazrat Fatima R.A", "Hazrat Sumayyah R.A"],
    "Khadija R.A believed in the Prophet (PBUH) immediately after the first revelation, so she was the first woman and the first person to accept Islam.",
    "Sumayyah R.A was the first martyr of Islam.")
add("Among adult free men, who was the first to accept Islam?", "Hazrat Abu Bakr R.A", ["Hazrat Umar R.A", "Hazrat Usman R.A", "Hazrat Ali R.A"],
    "Abu Bakr Siddiq R.A was the first adult free man to accept Islam.",
    "He is titled Siddiq and was the first Caliph.")
add("Who was the first among children to accept Islam?", "Hazrat Ali R.A", ["Hazrat Zubair R.A", "Hazrat Zaid bin Haritha R.A", "Hazrat Talha R.A"],
    "Ali R.A, then about ten years old and living in the Prophet's house, was the first child to accept Islam.",
    "Zaid bin Haritha R.A is counted as the first freed slave among the early Muslims.")
add("After the first revelation, which relative of Hazrat Khadija R.A confirmed that the Prophet (PBUH) was the awaited Prophet?", "Waraqa bin Naufal", ["Abu Talib", "Abu Lahab", "Uthman bin Talha"],
    "Khadija R.A took the Prophet (PBUH) to her cousin Waraqa bin Naufal, a Christian scholar, who confirmed his prophethood.",
    "Waraqa died soon afterwards and the revelation paused for a time (Fatrat-ul-Wahy).")
add("How many children did the Holy Prophet (PBUH) have, according to the common Seerah account?", "7 (3 sons and 4 daughters)", ["4 (1 son and 3 daughters)", "5 (2 sons and 3 daughters)", "9 (4 sons and 5 daughters)"],
    "The common account gives 3 sons (Qasim, Abdullah, Ibrahim) and 4 daughters (Zainab, Ruqayyah, Umm Kulthum, Fatima).",
    "Ibrahim was the only child not born to Khadija R.A; his mother was Maria Qibtiyya.")
add("At what age did the Holy Prophet (PBUH) receive the first revelation (Wahy)?", "40 years", ["25 years", "35 years", "45 years"],
    "The first revelation came in the cave of Hira when he was 40 years old.",
    "The first verses were from Surah Al-Alaq, beginning with Iqra.")
add("Who was the second wife of the Holy Prophet (PBUH)?", "Hazrat Sawda bint Zam'a R.A", ["Hazrat Ayesha R.A", "Hazrat Hafsa R.A", "Hazrat Zainab bint Jahsh R.A"],
    "After Khadija R.A passed away, the Prophet (PBUH) married Sawda R.A, so she is his second wife. The name Zubaida in the list is not correct.",
    "Ayesha R.A, daughter of Abu Bakr, married him soon after, in Makkah.")
add("In which year A.D. did the Holy Prophet (PBUH) migrate to Madina?", "622 A.D", ["610 A.D", "615 A.D", "630 A.D"],
    "The Hijrah took place in 622 A.D, which is the start of the Islamic calendar.",
    "The Hijri calendar was started in the time of Hazrat Umar R.A.")
add("Which pair were among the foster mothers (wet nurses) of the Holy Prophet (PBUH)?", "Hazrat Halima Sa'diyah and Thuwaybah", ["Hazrat Khadija and Hazrat Sawda", "Hazrat Ayesha and Hazrat Hafsa", "Hazrat Fatima and Hazrat Zainab"],
    "Thuwaybah (the freed slave of Abu Lahab) and Halima Sa'diyah both nursed the Prophet (PBUH). The list's Sobia is Thuwaybah.",
    "Halima belonged to the tribe of Banu Sa'd.")
add("Besides Hazrat Halima, whom did the Holy Prophet (PBUH) call his mother?", "Umm Ayman (Barakah) R.A", ["Hazrat Safiyya R.A", "Hazrat Asma bint Abu Bakr R.A", "Hazrat Umm Salama R.A"],
    "The Prophet (PBUH) called Umm Ayman, who raised him after Amina's death, 'my mother after my mother'.",
    "Her son was Usama bin Zaid R.A.")
add("How many years after the birth of the Holy Prophet (PBUH) did his mother Hazrat Amina die?", "6 years", ["2 years", "4 years", "8 years"],
    "Amina died at Abwa while returning from Madina when the Prophet was about six years old.",
    "After her, his grandfather Abdul Muttalib took care of him until he died when the Prophet was 8.")
add("What was the name of the foster sister of the Holy Prophet (PBUH)?", "Shaima", ["Safiyya", "Umm Hani", "Barakah"],
    "Shaima (Hudhafa bint Harith), daughter of Halima, used to carry and care for the Prophet (PBUH) as a child.",
    "She was captured in the battle of Hunain and treated with great respect by the Prophet.")
add("Which of these was a foster brother of the Holy Prophet (PBUH), a son of Hazrat Halima?", "Abdullah bin Harith", ["Abdullah bin Ubayy", "Abdullah bin Masood", "Abdullah bin Abbas"],
    "Abdullah bin Harith, son of Halima and Harith, was nursed with the Prophet (PBUH) and is known as his foster brother.",
    "The list gives the name as Abdullah bin Abu Sheema.")
add("For how long, according to the common account, did Hazrat Halima look after the Holy Prophet (PBUH)?", "About 4 years", ["1 year", "7 years", "10 years"],
    "The common Seerah account says the Prophet stayed with Halima in the desert for around four years (some say five).",
    "Desert upbringing gave him pure Arabic and strong health.")
add("How old was the Holy Prophet (PBUH) at the time of the Hajr-e-Aswad (Black Stone) incident?", "35 years", ["25 years", "30 years", "40 years"],
    "When the Kaaba was rebuilt, the Prophet (PBUH), then 35, settled the dispute by placing the stone on a sheet carried by all tribal leaders.",
    "He was called Al-Amin (the Trustworthy) before prophethood.")
add("Who used to spread thorns in the way of the Holy Prophet (PBUH)?", "Umm Jamil, wife of Abu Lahab", ["Hind bint Utba", "Umm Salama", "Sumayyah"],
    "Umm Jamil bint Harb, wife of Abu Lahab, used to put thorns on the Prophet's path; Surah Al-Lahab mentions her as the carrier of firewood.",
    "She was the sister of Abu Sufyan.")
add("Whose house was used as the centre of secret preaching by the Holy Prophet (PBUH)?", "Hazrat Arqam bin Abi Arqam R.A", ["Hazrat Abu Bakr R.A", "Hazrat Khadija R.A", "Hazrat Usman R.A"],
    "The house of Arqam on Mount Safa was Dar-e-Arqam, the first centre of Islamic teaching in Makkah.",
    "Umar R.A accepted Islam and the Muslims then began to preach openly.")
add("In which year of Prophethood did the boycott of Banu Hashim begin?", "7th Nabvi", ["3rd Nabvi", "5th Nabvi", "10th Nabvi"],
    "Quraish boycotted Banu Hashim and Banu Muttalib from the 7th year of prophethood and they stayed in Shib Abi Talib for about three years.",
    "The boycott ended in the 10th Nabvi, the year of grief.")
add("Which Prophet did the Holy Prophet (PBUH) meet on the first heaven during Miraj?", "Hazrat Adam A.S", ["Hazrat Isa A.S", "Hazrat Musa A.S", "Hazrat Ibrahim A.S"],
    "Authentic Ahadith of Bukhari and Muslim say he met Adam A.S in the first heaven.",
    "Ibrahim A.S was met in the seventh heaven.")
add("Which Prophets did the Holy Prophet (PBUH) meet on the second heaven during Miraj?", "Hazrat Isa A.S and Hazrat Yahya A.S", ["Hazrat Yusuf A.S", "Hazrat Idris A.S", "Hazrat Musa A.S and Hazrat Haroon A.S"],
    "In the second heaven he met the cousins Isa A.S and Yahya A.S.",
    "Isa and Yahya were maternal cousins.")
add("Which Prophet did the Holy Prophet (PBUH) meet on the third heaven during Miraj?", "Hazrat Yusuf A.S", ["Hazrat Yaqub A.S", "Hazrat Idris A.S", "Hazrat Haroon A.S"],
    "Authentic Hadith says he met Yusuf A.S in the third heaven. The list's answer Yaqub is not correct.",
    "Yusuf A.S was given half of all beauty.")
add("Which Prophet did the Holy Prophet (PBUH) meet on the fourth heaven during Miraj?", "Hazrat Idris A.S", ["Hazrat Yusuf A.S", "Hazrat Haroon A.S", "Hazrat Adam A.S"],
    "He met Idris A.S in the fourth heaven.",
    "Idris A.S is mentioned in the Quran as a truthful Prophet raised to a high place.")
add("Which Prophet did the Holy Prophet (PBUH) meet on the fifth heaven during Miraj?", "Hazrat Haroon A.S", ["Hazrat Musa A.S", "Hazrat Yahya A.S", "Hazrat Ibrahim A.S"],
    "He met Haroon A.S in the fifth heaven.",
    "Haroon A.S was the elder brother of Musa A.S.")
add("Which Prophet did the Holy Prophet (PBUH) meet on the sixth heaven during Miraj?", "Hazrat Musa A.S", ["Hazrat Haroon A.S", "Hazrat Isa A.S", "Hazrat Idris A.S"],
    "He met Musa A.S in the sixth heaven; Musa advised him to ask Allah to reduce the number of prayers.",
    "The prayers were reduced from fifty to five.")
add("Which Prophet did the Holy Prophet (PBUH) meet on the seventh heaven during Miraj?", "Hazrat Ibrahim A.S", ["Hazrat Musa A.S", "Hazrat Nuh A.S", "Hazrat Adam A.S"],
    "He met Ibrahim A.S in the seventh heaven, leaning against Bait-ul-Mamoor.",
    "Bait-ul-Mamoor is visited daily by seventy thousand angels.")
add("What was the name of the camel on which the Holy Prophet (PBUH) traveled during the Hijrah?", "Al-Qaswa", ["Al-Adba", "Al-Jada", "Duldul"],
    "The Prophet's well-known she-camel was Al-Qaswa, and he rode her to Madina.",
    "Duldul was his white mule.")
add("From whom did the Holy Prophet (PBUH) purchase the land for the mosque in Madina (Masjid-e-Nabawi)?", "Two orphans (Sahl and Suhail)", ["Hazrat Abu Ayyub Ansari R.A", "Abdullah bin Ubayy", "Banu Qurayza"],
    "The land of Masjid-e-Nabawi belonged to two orphans, Sahl and Suhail, and the Prophet (PBUH) bought it from them.",
    "The Prophet first stayed at the house of Abu Ayyub Ansari R.A.")
add("In which Hijri year was the Charter of Madina (Meesaq-e-Madina) issued?", "1 A.H", ["2 A.H", "5 A.H", "8 A.H"],
    "The Charter of Madina was made soon after the Hijrah, in 1 A.H, between Muslims, Jews and others of Madina.",
    "It is often called the first written constitution of an Islamic state. The number of its articles differs in sources, so that part is not asked.")
add("In which Hijri year was the change of Qibla (from Baitul Maqdis to Kaaba) ordered?", "2nd A.H", ["1st A.H", "4th A.H", "6th A.H"],
    "The order to turn towards the Kaaba came in the 2nd year after Hijrah, during prayer at Masjid-e-Qiblatain.",
    "The Battle of Badr took place in the same year.")
add("According to the common Seerah count, how many Ghazwat (expeditions led by the Prophet PBUH himself) are there?", "27", ["19", "56", "313"],
    "Seerah books commonly count 27 Ghazwat, in which the Prophet (PBUH) took part himself; he actually fought in about nine of them.",
    "Expeditions he did not lead are called Saraya, commonly counted as 56.")
add("Which was the first Ghazwa of Islam?", "Ghazwa Abwa (Waddan)", ["Ghazwa Badr", "Ghazwa Uhud", "Ghazwa Khandaq"],
    "The first Ghazwa led by the Prophet (PBUH) was Abwa, also called Waddan, in 2 A.H, and no fighting took place.",
    "The first major battle of Islam was Badr.")
add("Who was the first to compile Ahadith (Hadith) officially, on the order of Hazrat Umar bin Abdul Aziz?", "Imam Zuhri (Ibn Shihab Zuhri)", ["Imam Bukhari", "Imam Muslim", "Imam Malik"],
    "Imam Ibn Shihab Zuhri is widely regarded as the first to compile Ahadith formally, at the order of Umar bin Abdul Aziz.",
    "Imam Bukhari's Sahih Bukhari is the most authentic collection.")
add("How many Ahadith are reported from Hazrat Abu Hurairah R.A?", "5374", ["1540", "2210", "3000"],
    "Hazrat Abu Hurairah R.A is credited with 5374 narrations, the highest among the Sahaba, according to Baqi bin Makhlad.",
    "Abdullah bin Umar R.A and Anas bin Malik R.A follow him in the number of narrations.")
add("Which Prophet is known as Shaikh-ul-Anbiya?", "Hazrat Nuh A.S", ["Hazrat Ibrahim A.S", "Hazrat Adam A.S", "Hazrat Musa A.S"],
    "Hazrat Nuh A.S is called Shaikh-ul-Anbiya (Elder of the Prophets) because of his very long life of preaching.",
    "Ibrahim A.S is called Khalilullah and Abul Anbiya.")
add("Who was given the title Ameen-ul-Ummat?", "Hazrat Abu Ubaidah bin Jarrah R.A", ["Hazrat Abu Bakr R.A", "Hazrat Khalid bin Walid R.A", "Hazrat Saad bin Abi Waqqas R.A"],
    "The Prophet (PBUH) gave Abu Ubaidah bin Jarrah R.A the title Ameen-ul-Ummat (Trustworthy of the Ummah).",
    "He was one of the ten Sahaba given the good news of Jannah.")
add("What is the dome over the sacred grave of the Holy Prophet (PBUH) known as?", "Gumbad-e-Khizra (Green Dome)", ["Gumbad-e-Sakhra", "Gumbad-e-Zarrin", "Gumbad-e-Baida"],
    "The dome over the Prophet's tomb in Masjid-e-Nabawi is known as the Green Dome (Gumbad-e-Khizra).",
    "Gumbad-e-Sakhra is the Dome of the Rock in Jerusalem.")
add("Where is Bait-ul-Mamoor located?", "In the seventh heaven", ["In the first heaven", "In Makkah near the Kaaba", "In Jerusalem"],
    "Bait-ul-Mamoor is a house of worship of the angels in the seventh heaven, directly above the Kaaba.",
    "The Prophet (PBUH) saw it during Miraj.")
add("Which mosque was demolished on the order of the Holy Prophet (PBUH)?", "Masjid-e-Dirar (Mosque of Zarar)", ["Masjid-e-Quba", "Masjid-e-Qiblatain", "Masjid-e-Aqsa"],
    "The hypocrites built Masjid-e-Dirar to harm Muslims, and the Prophet (PBUH) had it destroyed after Surah At-Tawbah revealed its purpose.",
    "Masjid-e-Quba was the first mosque built in Islam.")
add("Who conquered the fort of Qamus during the Battle of Khyber?", "Hazrat Ali R.A", ["Hazrat Umar R.A", "Hazrat Khalid bin Walid R.A", "Hazrat Hamza R.A"],
    "Hazrat Ali R.A, given the flag by the Prophet (PBUH), conquered the fort of Qamus and killed its champion Marhab.",
    "Ali R.A is known by the title Asadullah (Lion of Allah).")
add("Which woman tried to poison the Holy Prophet (PBUH) at Khyber?", "Zainab bint Harith", ["Hind bint Utba", "Umm Jamil", "Sumayyah"],
    "A Jewish woman, Zainab bint Harith, served poisoned roasted goat meat to the Prophet (PBUH) after the conquest of Khyber.",
    "Bishr bin Bara R.A died from eating it.")
add("Which Surah did the Holy Prophet (PBUH) recite at the conquest of Makkah?", "Surah Al-Fath", ["Surah Al-Baqarah", "Surah Yaseen", "Surah Al-Kahf"],
    "On entering Makkah, the Prophet (PBUH) was reciting Surah Al-Fath while riding his camel.",
    "Surah Al-Fath was revealed after the Treaty of Hudaybiyyah.")
add("In which year of Prophethood did the first migration to Abyssinia (Habshah) take place?", "5th Nabvi (615 A.D)", ["2nd Nabvi (612 A.D)", "8th Nabvi (618 A.D)", "10th Nabvi (620 A.D)"],
    "In Rajab of the 5th year of Prophethood (615 A.D), a small group went to Abyssinia to escape persecution.",
    "They were protected by the Christian king Najashi (Negus).")
add("How many people took part in the first migration to Abyssinia, according to Ibn Ishaq?", "15 (11 men and 4 women)", ["83", "101", "313"],
    "Ibn Ishaq's account gives 11 men and 4 women, in total 15.",
    "Hazrat Usman R.A and his wife Ruqayyah R.A were among them.")
add("In which year A.D. did the second migration to Abyssinia take place, according to the common account?", "616 A.D", ["610 A.D", "622 A.D", "630 A.D"],
    "The second, bigger migration took place about a year after the first, around 616 A.D.",
    "Hazrat Jafar bin Abi Talib R.A led the second group.")
add("How many people in total took part in the second migration to Abyssinia?", "101 (including 18 women)", ["15", "313", "40"],
    "The second migration had 83 men and 18 women, in total 101 people.",
    "Hazrat Jafar R.A recited Surah Maryam before King Najashi.")
add("What does Harb-e-Fijar mean?", "A war fought in the prohibited (sacred) months", ["A war fought for water", "A war fought against Romans", "A war for the Kaaba key"],
    "Harb-e-Fijar was fought between Quraish and Banu Qais in the sacred months, in which fighting was forbidden, so it was called the sinful war.",
    "The young Prophet (PBUH) took part in it by handing arrows to his uncles.")
add("Which year is called Aam-ul-Huzn (Year of Grief)?", "10th Nabvi", ["5th Nabvi", "7th Nabvi", "1st Hijri"],
    "In the 10th year of Prophethood, Hazrat Khadija R.A and Abu Talib both passed away, so it is called the Year of Grief.",
    "Soon after, the Prophet (PBUH) went to Taif.")
add("What was the original name of Abu Jahl?", "Amr bin Hisham", ["Abdullah bin Ubayy", "Walid bin Mughira", "Abu Sufyan bin Harb"],
    "Abu Jahl was Amr bin Hisham, called Abul Hakam by Quraish; the Prophet (PBUH) called him Abu Jahl (father of ignorance). The list writes Omar bin Hisham.",
    "He was killed in the Battle of Badr.")
add("In which Hijri year did the conquest of Makkah take place?", "8th Hijri", ["6th Hijri", "7th Hijri", "10th Hijri"],
    "Makkah was conquered peacefully in Ramadan of 8 A.H (630 A.D).",
    "The Prophet (PBUH) forgave the people of Makkah.")
add("In which Hijri year did the Holy Prophet (PBUH) perform his (Farewell) Hajj?", "10th Hijri", ["6th Hijri", "8th Hijri", "11th Hijri"],
    "He performed the only Hajj of his life, the Farewell Hajj, in 10 A.H and delivered the Last Sermon at Arafat.",
    "He passed away about three months later.")
add("Where was the Holy Prophet (PBUH) buried?", "In the room (Hujra) of Hazrat Ayesha R.A", ["In Jannat-ul-Baqi", "Near the Kaaba in Makkah", "At Quba"],
    "He passed away in the room of Ayesha R.A and was buried at the same spot, as Prophets are buried where they die.",
    "Abu Bakr R.A and Umar R.A were later buried beside him.")
add("Which king tore up the letter of the Holy Prophet (PBUH) inviting him to Islam?", "Khusro Parvez, King of Persia (Iran)", ["Heraclius, Emperor of Rome", "Najashi, King of Abyssinia", "Muqawqis, ruler of Egypt"],
    "The Persian king Khusro Parvez tore the letter, and the Prophet (PBUH) said his kingdom would also be torn apart.",
    "Heraclius received the letter politely and Muqawqis sent gifts.")
add("Who was the Byzantine (Roman) emperor in the 7th Hijri year, when the Prophet PBUH sent him a letter?", "Heraclius (Hercules)", ["Khusro Parvez", "Najashi", "Constantine"],
    "Heraclius ruled the Byzantine Empire from 610 to 641 A.D and received the Prophet's letter in 7 A.H.",
    "Abu Sufyan was questioned by Heraclius about the Prophet.")
add("At what age did the Holy Prophet (PBUH) pass away?", "63 years", ["60 years", "65 years", "70 years"],
    "He passed away on 12 Rabi-ul-Awwal 11 A.H at the age of 63 years.",
    "Abu Bakr R.A, Umar R.A and Ali R.A also died at 63 years.")
