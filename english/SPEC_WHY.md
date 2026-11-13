# Add detailed reasons + related facts to English MCQs

Input: english/out/<X>.json (list of MCQ objects). Output: english/out2/<X>.json — the SAME list, SAME order, SAME length,
every existing field unchanged, plus two NEW fields on every item (also on skipped items, can be "" for skip:true):

- "why": simple English for a Pakistani student (2-5 short sentences). Must say:
  1) WHY the correct option is right (the rule / meaning), and
  2) why EACH other option is wrong, one short part per option, e.g. "A) 'goed' is wrong: 'go' is irregular. C) ..."
  Use the letters A) B) C) D) matching the options order. For passage questions, point to the line in the passage.
- "rel": 1-2 related, similar facts that help remember, e.g. other synonyms/antonyms of the word, similar idioms,
  the same grammar rule with another example, similar commonly confused words. One or two short sentences.

Rules:
- Do NOT change "question", "options", "correct", "skip". If you are SURE the key is wrong, do not change it; write the
  problem in "note" starting with "KEYCHECK:".
- No "<" or ">" characters anywhere in the text. Plain text only, no markdown.
- Keep it accurate. Write valid JSON (UTF-8). Validate with: python3 -c "import json;d=json.load(open('PATH'));print(len(d))"
  and check every item has non-empty "why" and "rel" (unless skip).
