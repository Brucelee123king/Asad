S = "Hakeem Force Academy"
QS = [
 (S, "What is a square matrix called when its transpose is equal to the matrix itself?", ["Skew-symmetric matrix", "Symmetric matrix", "Orthogonal matrix", "Identity matrix"], 1,
  "A square matrix A is symmetric when A transpose equals A, that is, a(i,j) = a(j,i) for all entries.", "In a skew-symmetric matrix the transpose equals the negative of the matrix, so all diagonal entries are zero."),
 (S, "Which mountain range joins Pakistan with China in the north?", ["Hindu Kush", "Karakoram", "Sulaiman", "Salt Range"], 1,
  "The Karakoram range lies in northern Pakistan along the border with China, and the Karakoram Highway crosses it at the Khunjerab Pass.", "K2, the second highest peak in the world, is in the Karakoram range."),
 (S, "For how many million Nanakshahi rupees was Kashmir sold to Gulab Singh by the British under the Treaty of Amritsar (1846)?", ["2.5 million", "5 million", "7.5 million", "10 million"], 2,
  "By the Treaty of Amritsar in 1846 the British sold Jammu and Kashmir to Gulab Singh for 75 lakh (7.5 million) Nanakshahi rupees.", "Gulab Singh was a Dogra ruler, and his family ruled Kashmir until 1947."),
 (S, "Justice Rana Bhagwandas, who served as a judge and acting Chief Justice of the Supreme Court of Pakistan, belonged to which religion?", ["Christianity", "Sikhism", "Hinduism", "Parsi (Zoroastrian)"], 2,
  "Rana Bhagwandas was a Hindu and was the first Hindu to serve as acting Chief Justice of Pakistan.", "He served as acting Chief Justice in 2007."),
 (S, "Who was the non-Muslim Chief Justice of Pakistan?", ["Muhammad Munir", "Alvin Robert Cornelius", "Rana Bhagwandas", "Sheikh Abdur Rashid"], 1,
  "A. R. Cornelius, a Christian, was Chief Justice of Pakistan from 1960 to 1968.", "Rana Bhagwandas was only an acting Chief Justice, and he was a Hindu."),
 (S, "In which year did Mustafa Kemal Ataturk abolish the Caliphate (Khilafat) in Turkey?", ["1919", "1922", "1924", "1928"], 2,
  "The Turkish Grand National Assembly abolished the Caliphate on 3 March 1924 under Mustafa Kemal.", "The Sultanate had already been abolished in 1922."),
 (S, "Near which place in Pakistan does the Kabul River join the Indus River?", ["Attock (Khairabad)", "Kalabagh", "Sukkur", "Taunsa"], 0,
  "The Kabul River meets the Indus near Attock at Khairabad, where the clear Kabul water and the muddy Indus water can be seen side by side.", "The Kabul River rises in Afghanistan and enters Pakistan near the Khyber area."),
 (S, "What was the relation of Hazrat Khadija (RA) with the Holy Prophet (PBUH)?", ["Mother", "Wife", "Daughter", "Aunt"], 1,
  "Hazrat Khadija (RA) was the first wife of the Holy Prophet (PBUH), and she was the first person to accept Islam.", "The Prophet (PBUH) did not marry again while she was alive."),
 (S, "At what age did the Holy Prophet (PBUH) marry Hazrat Khadija (RA)?", ["20 years", "25 years", "30 years", "40 years"], 1,
  "The Holy Prophet (PBUH) was 25 years old when he married Hazrat Khadija (RA), who was about 40.", "Hazrat Khadija (RA) passed away in the Year of Sorrow, three years before the Hijra."),
 (S, "Which thermodynamic cycle is used in a jet (gas turbine) engine?", ["Otto cycle", "Diesel cycle", "Brayton cycle", "Rankine cycle"], 2,
  "A jet engine works on the Brayton cycle: air is compressed, heated by burning fuel at constant pressure, and expanded through a turbine.", "Petrol engines use the Otto cycle and steam power plants use the Rankine cycle."),
 (S, "On what date did Pakistan become a member of the United Nations?", ["14 August 1947", "30 September 1947", "24 October 1947", "15 March 1948"], 1,
  "Pakistan was admitted to the United Nations on 30 September 1947, a few weeks after independence.", "Pakistan was the 56th member state of the UN."),
]
QS = [t + ([ids],) for t, ids in zip(QS, [2639,1159,1601,2368,4406,3392,3524,3131,3302,1614,834])]
DUPS = [(756,1098),(1736,3534),(78,1981),(578,2282),(1767,1796),(1767,390),(86,2243),(205,1099),(2349,2848),
 (1029,2682),(1029,3733),(1029,1263),(2425,3675),(1694,971),(1694,3049),(633,2247),(633,4175),(400,588),(400,3958),(400,4452),
 (1943,817),(2312,3387),(21,3412),(1045,2951),(1082,2560),(1082,523),(1573,3957),(1573,326),(1573,607),(879,1721),
 (1627,2253),(2604,3538),(152,3962),(152,4176),(1006,3124),(1006,512),(1006,3350),(1006,3360),(207,2058),(717,2071),
 (3724,2849),(468,2187),(468,484),(468,304),(1898,1406),(373,4336),(1864,4338),(1364,4360),(575,3836),(3721,2585),
 (1728,1725),(1728,736),(2298,4331),(1647,1731),(1897,4061),(3014,3571),(1773,2466),(2349,2848)]
DUPS = list(dict.fromkeys(DUPS))
