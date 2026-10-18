S = "Hakeem Force Academy"
QS = [
 (S, "What is 90% of 60?", ["56", "54", "6", "5.4"], 1,
  "90% of 60 = 90/100 x 60 = 54. The same value results from 60% of 90, since percentages are commutative.",
  "A quick way: 10% of 60 is 6, so 90% is 60 minus 6 = 54.", [60]),
 (S, "What is 90% of 91?", ["81.9", "82.9", "81", "8.19"], 0,
  "90% of 91 = 0.9 x 91 = 81.9. Equivalently, 10% of 91 is 9.1, and 91 minus 9.1 = 81.9.",
  "Taking 90% of a number is the same as subtracting 10% of it.", [3309]),
 (S, "What is 90% of 99?", ["90.1", "88.1", "89.1", "9.9"], 2,
  "90% of 99 = 0.9 x 99 = 89.1. Equivalently, 10% of 99 is 9.9, and 99 minus 9.9 = 89.1.",
  "90% of 100 is 90, so 90% of 99 is 0.9 less than 90.", [3310]),
 (S, "What is 90 divided by 90 (90/90)?", ["0", "81", "1", "90"], 2,
  "Any non-zero number divided by itself equals 1, so 90/90 = 1.",
  "Division of zero by a non-zero number gives 0, but division by zero is undefined.", [565]),
 (S, "In set theory, what is n(A-B) equal to?", ["n(A) - n(A intersection B)", "n(A) - n(B)", "n(A) + n(B) - n(A intersection B)", "n(B) - n(A intersection B)"], 0,
  "A-B contains the elements of A that are not in B. These are all elements of A except those common to both, so n(A-B) = n(A) - n(A intersection B).",
  "The union formula is n(A union B) = n(A) + n(B) - n(A intersection B).", [3396]),
]
DUPS = [(0, 0), (819, 156), (1021, 275), (301, 4346)]
