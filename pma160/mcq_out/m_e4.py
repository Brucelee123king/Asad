QS = []
def q(question, correct, wrongs, reason, rel, ex=-1):
    pos = (len(QS) * 3 + 1) % 4
    opts = list(wrongs)
    opts.insert(pos, correct)
    QS.append(("Hakeem Force Academy", question, opts, pos, reason, rel, ex))

C = "1973 Constitution"
q("In which year was the First Amendment to the 1973 Constitution passed, after the separation of East Pakistan?", "1974", ["1973", "1975", "1976"],
  "The First Amendment was passed in May 1974. It redefined the territories of Pakistan after the loss of East Pakistan and allowed recognition of Bangladesh.",
  "Pakistan formally recognised Bangladesh in February 1974 at the Islamic Summit in Lahore.")
q("In which year was the Second Amendment passed, declaring Ahmadis non-Muslim?", "1974", ["1973", "1977", "1985"],
  "The Second Amendment was passed by Parliament on 7 September 1974 under Prime Minister Zulfikar Ali Bhutto.",
  "It added clause (3) to Article 260 defining a non-Muslim.")
q("The Fourth Amendment of 1975 is known for providing which new provision?", "Reserved seats for non-Muslims in the provincial assemblies", ["Abolition of the Senate", "The removal of the President's power to dissolve the Assembly", "Creation of the Federal Shariat Court"],
  "The Fourth Amendment (1975) provided reserved seats for minorities in the provincial assemblies and also restricted bail powers of High Courts.",
  "Reserved seats for minorities in the National Assembly were already part of the original 1973 text.")
q("Which amendment of 1976 raised the retirement age of the Chief Justice of the Supreme Court to 65 and of High Court judges to 62?", "Sixth Amendment", ["Fifth Amendment", "Seventh Amendment", "Fourth Amendment"],
  "The Sixth Amendment (1976) set the retirement ages at 65 for the Supreme Court Chief Justice and 62 for High Court judges.",
  "Under the present Article 179, a Supreme Court judge retires at 65 years of age.")
q("Which amendment of 1977 introduced the provision of a referendum on a vote of confidence in the Prime Minister?", "Seventh Amendment", ["Third Amendment", "Eighth Amendment", "Sixth Amendment"],
  "The Seventh Amendment (1977) inserted Article 96 allowing the Prime Minister to seek a referendum on confidence in himself. Bhutto's government was overthrown in July 1977.",
  "The 1977 elections and the PNA movement led to the coup of 5 July 1977.")
q("Which amendment, passed in 1985, gave the President the power to dissolve the National Assembly under Article 58(2)(b)?", "Eighth Amendment", ["Seventh Amendment", "Tenth Amendment", "Thirteenth Amendment"],
  "The Eighth Amendment (1985) inserted Article 58(2)(b), under which the President could dissolve the Assembly at his discretion.",
  "It also inserted Article 270A, which validated the actions of the martial law period.", -1)
q("Which Article was added by the Eighth Amendment to indemnify and validate the orders of the martial law period of 1977-85?", "Article 270A", ["Article 270AA", "Article 58", "Article 232"],
  "Article 270A, added by the Eighth Amendment in 1985, affirmed laws and orders made between 5 July 1977 and 30 December 1985.",
  "Article 270A was meant to protect the orders of the martial law period from challenge in court.")
q("Under which Article of the 1973 Constitution did General Zia ul Haq and later Presidents dissolve the National Assembly before the 13th Amendment?", "Article 58(2)(b)", ["Article 48", "Article 232", "Article 96"],
  "Article 58(2)(b), added by the Eighth Amendment, was used to dismiss the governments of Junejo (1988), Benazir (1990 and 1996) and Nawaz Sharif (1993).",
  "The 13th Amendment removed it in 1997. The 17th Amendment restored it in 2003 and the 18th removed it permanently in 2010.")
q("Martial law imposed by General Zia ul Haq on 5 July 1977 was lifted in which year?", "1985", ["1983", "1984", "1988"],
  "Martial law ended on 30 December 1985 and the 1973 Constitution was revived with amendments through the Revival of Constitutional Order.",
  "Zia ul Haq held a referendum in December 1984 and non-party elections in February 1985.")
q("Which amendment, passed in 1997 under Prime Minister Nawaz Sharif, removed Article 58(2)(b)?", "Thirteenth Amendment", ["Twelfth Amendment", "Fourteenth Amendment", "Fifteenth Amendment"],
  "The Thirteenth Amendment, passed in April 1997, removed the President's discretionary power to dissolve the National Assembly and the power to appoint service chiefs.",
  "It transferred the power of appointing the Governors and Chiefs of Staff back to the Prime Minister's advice.")
q("Article 63A, which disqualifies a member who defects from his party, was added by which amendment?", "Fourteenth Amendment", ["Thirteenth Amendment", "Sixteenth Amendment", "Seventeenth Amendment"],
  "The Fourteenth Amendment (1997) introduced Article 63A on defection from the parliamentary party.",
  "It was passed in July 1997, a few months after the 13th Amendment.")
q("Which amendment, passed in December 2003, restored Article 58(2)(b) and incorporated the Legal Framework Order of Musharraf?", "Seventeenth Amendment", ["Fifteenth Amendment", "Sixteenth Amendment", "Eighteenth Amendment"],
  "The Seventeenth Amendment (December 2003) gave constitutional cover to the LFO 2002 and restored the President's power to dissolve the Assembly.",
  "It also allowed Musharraf to hold both offices of President and Chief of Army Staff and created the National Security Council.")
q("The Legal Framework Order (LFO) that was later given cover by the Seventeenth Amendment was issued in which year by General Pervez Musharraf?", "2002", ["1999", "2001", "2003"],
  "Musharraf issued the Legal Framework Order in August 2002, before the October 2002 general elections.",
  "The Seventeenth Amendment was passed in December 2003 after an agreement with the MMA.")
q("In which year was the 18th Amendment passed, removing Article 58(2)(b) and giving more autonomy to the provinces?", "2010", ["2008", "2009", "2012"],
  "The National Assembly passed it on 8 April 2010 and President Zardari signed it on 19 April 2010.",
  "The committee which drafted it was headed by Senator Raza Rabbani.", 3000)
q("What happened to the Concurrent Legislative List under the 18th Amendment?", "It was abolished", ["It was doubled in size", "It was moved to the Senate only", "It was kept but given to the federal government"],
  "The 18th Amendment abolished the Concurrent Legislative List, and subjects in it were transferred mainly to the provinces.",
  "Education, health and environment are now provincial subjects, so the Federal List is the only list of the federation.")
q("Which new fundamental right to education for children aged 5 to 16 was added by the 18th Amendment?", "Article 25A", ["Article 19A", "Article 9", "Article 37"],
  "Article 25A, added by the 18th Amendment, makes free and compulsory education a right for children of five to sixteen years.",
  "Article 19A (right to information) was also added by the same amendment.")
q("Which Article gave citizens the right to access information in matters of public importance, added in 2010?", "Article 19A", ["Article 19", "Article 25A", "Article 10A"],
  "Article 19A was inserted by the 18th Amendment (2010).",
  "Article 10A (right to fair trial) was also inserted by the 18th Amendment.")
q("The Judicial Commission of Pakistan for appointing judges was created under which Article by the 18th Amendment?", "Article 175A", ["Article 175", "Article 209", "Article 191A"],
  "Article 175A, added in 2010, set up the Judicial Commission and a Parliamentary Committee for appointment of judges.",
  "The 19th Amendment (December 2010) changed its composition after a Supreme Court order.")
q("Which amendment of 2010 revised the composition of the Judicial Commission and the Parliamentary Committee for judicial appointments?", "Nineteenth Amendment", ["Seventeenth Amendment", "Twentieth Amendment", "Twenty-first Amendment"],
  "The Nineteenth Amendment (December 2010) reconstituted the Commission and Parliamentary Committee after the Supreme Court sent the 18th Amendment provision back to Parliament.",
  "It also changed the process for appointment of the Election Commissioner.")
q("The Twentieth Amendment of 2012 was related mainly to which subject?", "The appointment of the Chief Election Commissioner and a caretaker setup", ["Provincial names", "Military courts", "The merger of FATA"],
  "The Twentieth Amendment (February 2012) made the Election Commission independent and defined the process for neutral caretaker governments.",
  "It was passed to guarantee free and fair elections in 2013.")
q("Military courts for terrorism cases were first established through which amendment?", "Twenty-first Amendment", ["Eighteenth Amendment", "Nineteenth Amendment", "Twenty-second Amendment"],
  "The 21st Amendment (January 2015) was passed after the attack on the Army Public School Peshawar in December 2014, with a sunset period of two years.",
  "It was accompanied by the Pakistan Army Act amendment of 2015.")
q("For how long were military courts first allowed under the Twenty-first Amendment of 2015?", "Two years", ["One year", "Three years", "Five years"],
  "The 21st Amendment included a sunset clause of two years, ending in January 2017.",
  "The 23rd Amendment of March 2017 extended them for another two years.")
q("Which amendment of 2017 revived military courts for a further two years?", "Twenty-third Amendment", ["Twenty-second Amendment", "Twenty-fourth Amendment", "Twenty-fifth Amendment"],
  "The 23rd Amendment extended the military courts' mandate after their term had lapsed in January 2017.",
  "The courts ended in 2019 when the extension lapsed.")
q("Which amendment of 2016 was about the qualifications of the Election Commission members, such as allowing technocrats?", "Twenty-second Amendment", ["Twenty-first Amendment", "Twentieth Amendment", "Twenty-third Amendment"],
  "The 22nd Amendment (2016) changed the qualifications of the Chief Election Commissioner and ECP members, allowing technocrats and retired civil servants.",
  "The Election Commission has a Chief Election Commissioner and four members, one from each province.")
q("The Twenty-fourth Amendment of 2017 was passed to fix what issue?", "Redistribution of National Assembly seats based on the 2017 census", ["Merger of FATA", "Military courts", "Appointment of judges"],
  "The 24th Amendment (December 2017) allowed delimitation of constituencies using the provisional results of the 2017 census, in time for the 2018 elections.",
  "The 2017 census was the first since 1998.")
q("In which year was the Twenty-fifth Amendment passed, merging FATA into Khyber Pakhtunkhwa?", "2018", ["2016", "2017", "2019"],
  "The 25th Amendment was passed in May 2018, and the first provincial elections in the merged districts were held in July 2019.",
  "FATA included seven tribal agencies and six Frontier Regions.")
q("After the Twenty-fifth Amendment, how many total seats does the National Assembly have?", "336", ["342", "272", "326"],
  "Before the merger, the Assembly had 342 seats. After FATA's 12 seats were removed, the number came down to 336, effective from the 2018 elections.",
  "The Senate seats of FATA (8) were also removed, and the Senate had 96 seats after the transition.")
q("Which provision of Pakistan's Constitution was amended by the 25th Amendment to extend the High Court and the Supreme Court jurisdiction to FATA?", "Article 247", ["Article 246", "Article 248", "Article 260"],
  "Article 247, which governed the administration of tribal areas, was omitted by the 25th Amendment, extending the jurisdiction of the superior courts and of Parliament.",
  "Article 246 defined the Tribal Areas and was also removed.")
q("Through which amendment was the name of NWFP changed to Khyber Pakhtunkhwa?", "Eighteenth Amendment", ["Seventeenth Amendment", "Nineteenth Amendment", "Twenty-fifth Amendment"],
  "The change was made in Article 1 by the 18th Amendment in 2010 after the demand of the ANP.",
  "The renaming ended the use of the name North-West Frontier Province, used since 1901.", 6144)
q("In which year was the 26th Amendment to the Constitution passed?", "2024", ["2022", "2023", "2025"],
  "The Parliament passed the 26th Amendment in October 2024, changing the way the Chief Justice is appointed.",
  "It was passed when Qazi Faez Isa's term was about to end.")
q("Under the 26th Amendment, the Chief Justice of Pakistan is appointed from how many most senior judges of the Supreme Court?", "Three", ["Two", "Four", "Five"],
  "A special parliamentary committee recommends one name out of the three most senior Supreme Court judges to the Prime Minister, who advises the President.",
  "Justice Yahya Afridi became Chief Justice under this new method in October 2024.")
q("What was the term of the Chief Justice of Pakistan fixed by the 26th Amendment?", "Three years", ["Two years", "Four years", "Five years"],
  "The 26th Amendment set a fixed term of three years for the Chief Justice, subject to age 65.",
  "Yahya Afridi was appointed on 26 October 2024.")
q("Which Article of the Constitution, inserted by the 26th Amendment, created constitutional benches in the Supreme Court?", "Article 191A", ["Article 175A", "Article 184", "Article 199"],
  "Article 191A provided for Constitutional Benches of the Supreme Court to hear constitutional matters.",
  "A similar bench in each High Court was provided by Article 202A.")
q("In which year was the 27th Amendment to the Constitution passed?", "2025", ["2024", "2026", "2023"],
  "Parliament passed the 27th Amendment in November 2025, and President Zardari signed it on 13 November 2025.",
  "It was passed after the 26th Amendment of October 2024.")
q("Which new court was created by the 27th Amendment?", "Federal Constitutional Court", ["Federal Shariat Court", "Supreme Appellate Court", "Constitutional Bench of the Supreme Court"],
  "The 27th Amendment created a Federal Constitutional Court to hear constitutional matters and disputes between the federation and provinces.",
  "Justice Aminuddin Khan took oath as its first Chief Justice on 14 November 2025.")
q("Who was the first Chief Justice of the Federal Constitutional Court of Pakistan?", "Justice Aminuddin Khan", ["Justice Yahya Afridi", "Justice Mansoor Ali Shah", "Justice Aamer Farooq"],
  "Justice Aminuddin Khan, earlier head of the Supreme Court's constitutional bench, was sworn in on 14 November 2025.",
  "The Federal Constitutional Court was established under the 27th Amendment.")
q("Which new military post was created by the 27th Amendment in Article 243?", "Chief of Defence Forces", ["Chairman Joint Chiefs of Staff Committee", "Chief of Joint Staff", "Supreme Commander"],
  "The amendment created the post of Chief of Defence Forces, held by the Chief of Army Staff, over the army, navy and air force.",
  "The post of Chairman Joint Chiefs of Staff Committee was abolished.")
q("Which post was abolished by the 27th Amendment?", "Chairman Joint Chiefs of Staff Committee", ["Chief of Army Staff", "Chief of Naval Staff", "Chief of Air Staff"],
  "The 27th Amendment ended the post of CJCSC, whose term expired on 27 November 2025.",
  "The post had been created in 1976 as a coordinating post among the three services.")
q("Under which Article of the 1973 Constitution are the Armed Forces' command and the Chief of Staff appointments provided?", "Article 243", ["Article 244", "Article 245", "Article 190"],
  "Article 243 deals with the command of the armed forces, and has been amended by the 27th Amendment.",
  "Article 245 deals with the functions of the armed forces, and Article 244 with their oath.")
q("Which Article of the 1973 Constitution provides the procedure for amending the Constitution?", "Article 239", ["Article 238", "Article 240", "Article 237"],
  "Article 238 permits amendment and Article 239 sets the procedure, requiring a two-thirds majority of the total membership of each House.",
  "A bill to amend the Constitution cannot be challenged in any court under Article 239(5).")
q("What majority is needed in each House of Parliament to amend the 1973 Constitution?", "Two-thirds of its total membership", ["Simple majority of members present", "Three-fourths of total membership", "Two-thirds of members present"],
  "Article 239(4) requires a bill to be passed by two-thirds of the total membership of each House.",
  "A bill affecting a province's boundaries also requires the consent of that Provincial Assembly (Article 239(4)).")
q("In which year was the first martial law imposed in Pakistan, abrogating the 1956 Constitution?", "1958", ["1953", "1956", "1962"],
  "President Iskander Mirza abrogated the 1956 Constitution on 7 October 1958 and appointed General Ayub Khan as Chief Martial Law Administrator.",
  "Ayub Khan removed Mirza after twenty days, on 27 October 1958.", -1)
q("Which President abrogated the 1956 Constitution of Pakistan?", "Iskander Mirza", ["Ghulam Muhammad", "Ayub Khan", "Yahya Khan"],
  "Iskander Mirza announced martial law and the abrogation of the 1956 Constitution on 7 October 1958.",
  "He had become the first President in 1956 under that Constitution.")
q("Which Chief Justice delivered the judgment that validated Iskander Mirza's action in 1958 by using the doctrine of necessity?", "Justice Muhammad Munir", ["Justice Cornelius", "Justice Hamoodur Rahman", "Justice Anwarul Haq"],
  "In the Dosso case (1958), the Federal Court under Chief Justice Muhammad Munir validated the abrogation based on Kelsen's theory of revolutionary legality.",
  "The Dosso judgment was declared wrong in the Asma Jilani case (1972).")
q("In which year was the second martial law imposed, when Ayub Khan handed over power to the army chief?", "1969", ["1965", "1968", "1971"],
  "General Yahya Khan imposed martial law on 25 March 1969, abrogating the 1962 Constitution.",
  "The Legal Framework Order of March 1970 prepared the first general elections held in December 1970.")
q("Which Supreme Court case of 1972 declared Yahya Khan a usurper and overruled the Dosso case?", "Asma Jilani case", ["Nusrat Bhutto case", "Zafar Ali Shah case", "Tikka Khan case"],
  "In the case of Asma Jilani v. Government of Punjab (1972), the Court held that Yahya Khan's martial law was illegal.",
  "The Court was headed by Chief Justice Hamoodur Rahman.")
q("The Supreme Court validated Zia's coup of 1977 in which case?", "Nusrat Bhutto case", ["Asma Jilani case", "Dosso case", "Sharaf Faridi case"],
  "In Begum Nusrat Bhutto v. Chief of Army Staff (1977), the Supreme Court used the doctrine of necessity to validate the coup.",
  "Chief Justice Anwarul Haq headed the bench.")
q("What was the name of the military operation by which General Zia ul Haq took power on 5 July 1977?", "Operation Fair Play", ["Operation Gibraltar", "Operation Midnight Jackal", "Operation Searchlight"],
  "Operation Fair Play removed Prime Minister Z. A. Bhutto and put the Constitution in abeyance.",
  "Operation Midnight Jackal refers to the 1995 coup plot.")
q("Which instrument was used to put the 1973 Constitution in abeyance after the coup of October 1999?", "Provisional Constitution Order", ["Legal Framework Order", "Revival of Constitutional Order", "Eighth Amendment"],
  "General Musharraf issued Provisional Constitution Order No. 1 of 1999 on 14 October 1999 and became Chief Executive.",
  "He did not impose martial law formally.")
q("On which date did General Pervez Musharraf take over power by removing Nawaz Sharif?", "12 October 1999", ["5 July 1999", "12 October 1998", "14 August 1999"],
  "The coup took place on 12 October 1999 after Nawaz Sharif tried to remove Musharraf as army chief.",
  "Musharraf took the title Chief Executive and not Chief Martial Law Administrator.")
q("Which case of 2000 validated Musharraf's coup and allowed him three years to hold elections?", "Zafar Ali Shah case", ["Nusrat Bhutto case", "Asma Jilani case", "Dosso case"],
  "In Syed Zafar Ali Shah v. Pervez Musharraf (May 2000) the Supreme Court validated the coup on the doctrine of necessity and set a three year limit.",
  "The Court under Chief Justice Irshad Hasan Khan also allowed him to amend the Constitution to a limited extent.")
q("The Revival of Constitutional Order (RCO) of 1985 was issued by which ruler?", "General Zia ul Haq", ["General Yahya Khan", "General Pervez Musharraf", "General Ayub Khan"],
  "Zia issued the Revival of the Constitution of 1973 Order (RCO) in March 1985 to restore the 1973 Constitution with large changes.",
  "The Eighth Amendment later gave the changes constitutional cover.")
q("On which date did President Musharraf proclaim a state of emergency and issue a Provisional Constitution Order, removing the Chief Justice?", "3 November 2007", ["12 October 2007", "9 March 2007", "15 December 2007"],
  "On 3 November 2007 Musharraf, as Chief of Army Staff, suspended the Constitution, issued PCO No. 1 of 2007 and removed Chief Justice Iftikhar Chaudhry.",
  "The emergency was lifted on 15 December 2007.")
q("Which Chief Justice of Pakistan was removed by the emergency of 3 November 2007?", "Iftikhar Muhammad Chaudhry", ["Abdul Hameed Dogar", "Saeed uz Zaman Siddiqui", "Nasir ul Mulk"],
  "He was removed and put under house arrest, and Justice Abdul Hameed Dogar took oath under the PCO.",
  "He had earlier been suspended in March 2007 and was reinstated in July 2007.")
q("Who was the Chief Martial Law Administrator who imposed the first martial law of 1958 and later became President in October 1958?", "General Muhammad Ayub Khan", ["General Yahya Khan", "General Ziaul Haq", "General Musa Khan"],
  "Ayub Khan was appointed CMLA on 7 October 1958 and became President on 27 October 1958.",
  "He introduced the Constitution of 1962 after martial law was lifted in June 1962.")
q("Which Article of the 1973 Constitution defines the act of high treason as abrogating or subverting the Constitution?", "Article 6", ["Article 5", "Article 7", "Article 8"],
  "Article 6 makes subverting or abrogating the Constitution by force high treason, punishable by death or life imprisonment.",
  "The 18th Amendment added the clause that no court may validate such acts.")
q("Which Article of the 1973 Constitution covers a Proclamation of Emergency on grounds of war or internal disturbance?", "Article 232", ["Article 233", "Article 234", "Article 235"],
  "Article 232 deals with emergency on account of war or internal disturbance. Article 233 deals with suspension of fundamental rights.",
  "Article 234 is about the failure of constitutional machinery in a province and Article 235 about a financial emergency.")
q("Which Article of the 1973 Constitution deals with the failure of the constitutional machinery in a province, known as Governor's rule?", "Article 234", ["Article 232", "Article 235", "Article 236"],
  "Article 234 provides for a Proclamation if the government of a province cannot be carried on in accordance with the Constitution.",
  "Article 235 is the provision for a financial emergency.")
q("In which year was the 1973 Constitution first suspended?", "1977", ["1973", "1975", "1985"],
  "The Constitution was held in abeyance by General Zia ul Haq's coup of 5 July 1977 and was revived in 1985.",
  "It was adopted on 10 April 1973 and enforced from 14 August 1973.")
q("Which Prime Minister was dismissed by President Zia ul Haq under Article 58(2)(b) in May 1988?", "Muhammad Khan Junejo", ["Benazir Bhutto", "Nawaz Sharif", "Zulfikar Ali Bhutto"],
  "President Zia dismissed the Junejo government on 29 May 1988 using Article 58(2)(b).",
  "Zia died in an air crash on 17 August 1988.")
q("How many Articles of the Constitution were changed by the 18th Amendment, roughly?", "About 100", ["About 20", "About 50", "About 200"],
  "The 18th Amendment altered, substituted or deleted around 102 Articles, making it the largest amendment.",
  "Parliament's committee had 27 members and it was headed by Raza Rabbani.")
q("Which amendment removed the bar on a person becoming Prime Minister for more than two terms, a restriction added by the 17th Amendment?", "Eighteenth Amendment", ["Thirteenth Amendment", "Nineteenth Amendment", "Twentieth Amendment"],
  "The 18th Amendment removed the two-term limit on the Prime Minister and Chief Minister (Article 91 clause 6 and Article 130).",
  "The two-term bar was inserted into the Constitution by Musharraf's LFO.")
q("On which date was the 1973 Constitution adopted by the National Assembly?", "10 April 1973", ["14 August 1973", "23 March 1973", "12 April 1973"],
  "The Assembly adopted it on 10 April 1973, and it came into force on 14 August 1973.",
  "Z. A. Bhutto was the Prime Minister and the first Speaker was Fazal Elahi Chaudhry.")
q("What is the present number of amendments passed to the 1973 Constitution, after the 27th Amendment of 2025?", "27", ["26", "28", "25"],
  "Twenty-seven amendments have been made, the latest being the 27th in November 2025.",
  "Not all numbered amendment bills were passed: for example, the 9th and 11th were not enacted.", 871)
q("The Twelfth Amendment of 1991 provided for which special courts?", "Special courts for speedy trial of heinous offences", ["Military courts", "Shariat courts", "Banking courts"],
  "The Twelfth Amendment (1991) inserted Article 212A for speedy trials, for a limited period of three years.",
  "The Nawaz Sharif government passed it.")
q("The Shariat Court of Pakistan was established in which year, by a Presidential Order of Zia ul Haq?", "1980", ["1977", "1979", "1985"],
  "The Federal Shariat Court was established in May 1980 by Presidential Order No. 1 of 1980, adding Chapter 3A to the Constitution.",
  "It examines whether laws are in accordance with the Injunctions of Islam under Article 203D.")
