# Islamiat MCQs PMA (from the user's 3 note pages: notes_p1.jpg, notes_p2.jpg, notes_p3.jpg)

Write MCQs ONLY from the facts in the notes (one MCQ per fact; a line with several facts can give 2-3 MCQs).
Where the notes are wrong, use the CORRECT fact (list below) and say so in "note". Skip facts that are doubtful
(listed under SKIP) - do not invent extra topics.

Output JSON list, each item:
{"question": str, "options": [4 strings], "correct": 0-3, "why": str, "rel": str, "topic": str, "note": str}
- 4 options, one clearly right; wrong options must be plausible but clearly wrong (no "all of these"/"none of these").
- Put the correct option at a random position (spread A/B/C/D evenly).
- "why": simple English, 2-5 short sentences: why the answer is right AND why each other option is wrong
  (e.g. "A) 7 is wrong: ... C) ...").  Use letters A) B) C) D) for the options order.
- "rel": 1-2 related, similar facts that help to remember (from the same notes or common knowledge, correct only).
- Use PBUH after the Holy Prophet's name and (AS) for prophets, (RA) for companions.
- No "<" or ">" characters. Plain text. Valid JSON (UTF-8). Validate with python3 before finishing.

## CORRECTIONS (the notes are wrong here - use the correct fact)
- Hazrat Saleh (AS): nation Samood; miracle she-camel; punishment was a mighty blast/earthquake (NOT rain of stones; rain of stones was on the nation of Hazrat Lut (AS)).
- Ghazwa Tabuk (9 AH) was against the Romans (Byzantine Empire), NOT the Egyptians.
- Sahifas: 100 Sahifas in total (Hazrat Sheeth 50, Hazrat Idrees 30, Hazrat Ibrahim 10, Hazrat Adam 10) and 4 books. "30 Sahifas" were given to Hazrat Idrees (AS).
- Nisab of Zakat on animals: 5 camels, 40 goats, 30 cows/buffaloes (NOT 3).
- Ushr: 1/10 on land watered by rain, 1/20 on land watered by irrigation (wells/tubewells); Khums 1/5.
- Farz of Hajj (3): Ihram, Wuquf-e-Arafat (9 Zil Hajj), Tawaf-e-Ziarat.
- Ghazwa Mutah was in 8 AH (NOT 7 AH). Letters to kings: end of 6 AH / 7 AH (use 7 AH).
- Hazrat Khalid bin Waleed (RA) accepted Islam in 8 AH (NOT 6 AH); in options do not put 7 AH.
- First Ghazwa: Ghazwa Waddan (Abwa), Safar 2 AH (the notes say 1 AH). Use 2 AH, and do not put 1 AH as an option.
- The word "Islam" occurs 6 times in the Quran (do NOT make an MCQ on how many times the word "Quran" occurs).
- Prophet Adam (AS): height 60 cubits (about 90 feet) - Sahih Bukhari. Hazrat Sheeth (AS) was his son (do not say "youngest").

## SKIP (doubtful - no MCQ)
- number of Rukus, "12 Ghazwat mentioned", Yousaf (AS) "well at age 15", Meesaq-e-Madina "54/57" articles,
  alcohol haram year, veil order year, Ismail born when Ibrahim was 86, Kaaba "4000 years ago",
  Nooh (AS) prophethood at 40.
