# Hand-over: MCQ site for Asadullah Notes (branch ccr-c452b4f4-v2803x)

## What exists
- `site/index.html` is the FINAL site file the user uploads to Netlify (also in repo root as older copies). It contains:
  1. 1000 original MCQs in 20 tests of 50 (unchanged content, black "Asadullah Notes" splash, Asad signature)
  2. PMA 159 section (6 blocks, 269 MCQs, repeat counts as "(Repeated in N tests)")
  3. Forces Academy Lahore section (16 blocks, 771 MCQs: intelligence tests 1-17, 20, academic lists)
  4. Hakeem Force Academy section (34 blocks, 1678 MCQs from the 456-page PDF "PMA 149 ALL ASRC INITIAL ACADEMIC EXPERIENCE WRITTEN BY HAKEEM KHAN.pdf"; repeat count in brackets only, e.g. "(156)", most repeated first)
- Rebuild command (from repo root): `python3 pma159/merge_into_site.py pma159/base_original_site.html site/index.html`
  (base_original_site.html is the original 1000-MCQ site; the script adds all three extra sections from the data files below.)

## Data files
- PMA 159: `pma159/questions.py`
- Forces Academy: `pma159/fa_parts/fa_0*.py`, fixes in `pma159/fa_parts/fa_overrides.py`
- Hakeem (PMA 149): `pma149/hk_final.json` (built by `python3 pma149/build_hk.py` from `pma149/hk_merged_stage1.json`; manual fixes go in `pma149/hk_overrides.json` as {"remove":[question prefixes], "fix":{question prefix:{"correct":idx,"options":[...],"reason":"...","rel":"...","question":"..."}}})
- Raw: `pma149/chunks`, `pma149/extract/ex_*.jsonl` (all questions extracted), `pma149/clusters.json`, `pma149/mcq_in`, `pma149/mcq_out`

## Rules the user set
- Everything in English. Wrong answer must show why it is wrong, the correct answer, the reason and a related fact.
- Answers must be correct today (October 2026): update outdated current-affairs answers (e.g. Punjab CM is Maryam Nawaz) and check doubtful facts by web search.
- Existing sections (1000 MCQs, PMA 159, Forces Academy) must NOT be changed. Only add/fix the Hakeem section.
- Blocks of 50 MCQs, 12 seconds per MCQ (10 minutes per 50).

## Open task when this note was written
The Hakeem MCQs (1678) were being independently re-solved by 8 blind checkers: inputs `pma149/verify_hk/blind_1..8.txt`, outputs `pma149/verify_hk/answers_1..8.txt` (lines: `<n>: <letter> | <high/medium/low> | <note>`; n = position in `pma149/hk_final.json`, 1-based, letters A-E = option order).
Next steps:
1. For each n where the checker letter differs from the answer in hk_final.json, decide who is right (use web search for facts/current affairs, solve maths), then add a fix or removal to `pma149/hk_overrides.json`.
2. Also web-check these time-sensitive items that helpers wrote from single sources: UK Prime Minister, KPK Chief Minister (governor's rule claim from Oct 2026 is unverified), Naval chief, Balochistan CM, Speaker, Defence Minister.
3. `python3 pma149/build_hk.py`, rebuild the site (command above), run a quick browser/JS check, commit, push, and send `site/index.html` to the user.

## Phase 2 (PMA 150 PDF) - started
User uploaded `pma 150 initial experience.pdf` (4038 pages, 1.35 MB text) to the repo. It goes INTO the Hakeem section:
- A question already in `pma149/hk_final.json` -> do NOT write it again; add the new repeat count to the bracket number of the existing MCQ (keep existing order, update only the count).
- A new question -> new MCQ appended after the existing ones, continuing the blocks of 50.
- Same quality rules (English only, reason + related fact, answers current for Oct 2026, web-check doubtful facts, blind check).
Work dir: `pma150/` (chunks `chunks/c_01..34.txt` = text with Urdu lines removed; `SPEC_extract.md`; extraction output `extract/ex_NN.jsonl`, exp ids = chunk*1000+seq).
Plan: extract (34 agents) -> cluster -> match to hk_final (Jaccard+numbers) -> add counts -> write MCQs for unmatched clusters (repeat>=2 first, then singles) -> blind check -> build -> merge into site.
Tell the user: "Continue the task from HANDOFF.md ... Phase 2 PMA 150". 
