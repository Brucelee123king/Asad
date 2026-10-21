MATCH = [
    (58, 452), (60, 546), (63, 537), (64, 291), (65, 188), (66, 100),
    (69, 529), (70, 359), (71, 217), (72, 259), (74, 106), (75, 377),
]
NEW = [
    (59, "Pakistan Studies", "The Morley-Minto Reforms (Indian Councils Act), which introduced separate electorates for Muslims, were passed in:", "1909",
     ["1905", "1919", "1935"],
     "The Indian Councils Act of 1909 is known as the Morley-Minto Reforms, after Secretary of State John Morley and Viceroy Lord Minto. It gave Muslims separate electorates.", 0),
    (61, "Pakistan Studies", "In which year did Allama Iqbal deliver his Allahabad Address, presenting the idea of a separate Muslim state in north-western India?", "1930",
     ["1906", "1940", "1947"],
     "Iqbal gave the Allahabad Address on 29 December 1930 at the annual session of the All-India Muslim League.", 0),
    (62, "Current Affairs", "Who is the current President of Pakistan (as of October 2026)?", "Asif Ali Zardari",
     ["Shehbaz Sharif", "Arif Alvi", "Mamnoon Hussain"],
     "Asif Ali Zardari is the 14th President of Pakistan, in office since 10 March 2024. Shehbaz Sharif is the Prime Minister.", 0),
    (67, "Verbal: Maths & Reasoning", "Which letter comes immediately after M in the English alphabet?", "N",
     ["L", "O", "P"],
     "The alphabet runs ... K, L, M, N, O ... so N follows M.", 0),
]
SKIPPED = {
    68: "ambiguous: write-up says 10% or 20% of 1/3 of 90 (answers 3 or 6); numbers not clear",
    73: "ambiguous: 'when was Sindh conquered' - 711 or 712 AD depending on source, and an existing MCQ covers who conquered it",
    76: "ambiguous: expression and options not clear (log x value 0, 1, -1 or 1/2)",
}
