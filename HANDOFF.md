# START HERE (read this first in a new chat)

**User:** Asadullah, admin of an MCQ-practice Netlify site. He types Hindi/Urdu by voice. **Always reply in simple English.** He uploads `site/index.html` to Netlify himself (same link each time). Never change/mix MCQ data unless he asks.

**Deliverable:** `site/index.html` (single file). Rebuild with:
`python3 pma159/merge_into_site.py pma159/base_original_site.html site/index.html` (run from repo root). Never hand-edit site/index.html; edit the source blocks and rebuild.

**Sections / data (do not change unless asked):** 1000 MCQs (20 tests x 50), PMA 159, Forces Academy Lahore, Hakeem Force Academy (PMA 149+150+151, 4033 MCQs, repeat count in brackets). Each 50-MCQ test has a 20-minute timer. Hakeem data priority: dedupe/hk_final_dedup.json > pma151/hk_final3.json > pma150/hk_final2.json > pma149/hk_final.json.

**UI blocks (all in pma159/, injected in this order by merge_into_site.py `_blk`):**
theme_block (day/night) > auth_block (Student Login page: glossy graduation cap + scroll hero, liquid-glass shiny card, pastel blobs, floating study icons, Continue as Guest; sign-up pane too) > seccolor_block (section colours inside tests) > polish_block (premium look) > backnav_block (Back button + phone back) > features_block (dashboard, streak, Daily Challenge, Saved, Mistakes, Search, Share score, keyboard shortcuts) > glass_block (liquid glass, goo blobs, droplets) > d3_block (floating 3D study icons: book/pencil/cap/bulb/clock instead of cubes/balls, tilt cards, clay buttons, very slow parallax).
Splash screen is permanently removed. Accounts/streaks/saved are device-local (localStorage); Google/Facebook buttons are cosmetic.

**Workflow:** edit block -> rebuild -> `node --check` inline scripts -> playwright test in /opt/pw-browsers/chromium (light+dark, 400px and desktop) -> commit with trailers -> push branch `ccr-c452b4f4-v2803x` -> SendUserFile site/index.html -> tell him to upload to Netlify.

**Ideas not done yet:** check ~235 time-sensitive Hakeem answers on the web; real Google login would need a server.

---
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

### Phase 2 status
- Extraction done (34 chunks). `pma150/cluster150.py 0.75` -> clusters.json (duplicate write-ups merged); `pma150/match150.py 0.6` -> hk_add.json (lexical matches to existing MCQs) + unmatched.json; `make_batches.py 100` -> mcq_in/b_01..56.jsonl.
- MCQ writers (spec `pma150/SPEC_mcq150.md`, check `check150.py`) write mcq_out/m_NN.py (QS 7-tuples with input ids as last field, DUPS = (existing index, input id)). A batch is done when its m_NN.py exists and passes check150.py.
- Build: `python3 pma150/build150.py` -> pma150/hk_final2.json (existing order kept, counts raised; new MCQs appended, sorted by repeat). merge_into_site.py uses hk_final2.json automatically. Fixes: pma150/hk150_overrides.json (same format as pma149/hk_overrides.json).
- Then blind-check the new MCQs, rebuild site, test, send.

### Phase 2 DONE (Oct 2026)
- 56 MCQ batches written, near-duplicates merged, blind check of all 1531 new MCQs done (18 disagreements reviewed; fixes/removals in pma150/hk150_overrides.json), key current-affairs answers web-checked.
- Final Hakeem section: 3201 MCQs, 65 blocks (1676 PMA 149 MCQs with raised repeat counts + 1525 new PMA 150 MCQs). site/index.html rebuilt and sent.
- Optional follow-up: pma150/verify/ts_00..02.txt list 235 time-sensitive MCQs for a further web check (spec SPEC_timesens.md) - the agents for it hit the usage limit.

## Phase 3 (PMA 151 PDF, 8197 pages) - in progress
- Timer: all 50-MCQ tests now 20 minutes (patch at end of pma159/merge_into_site.py). Done and sent.
- Same pipeline in `pma151/`: chunks c_01..40 extracted; cluster151.py, match151.py (existing = pma150/hk_final2.json, 3201 MCQs), make_batches -> mcq_in/b_01..53.
- MCQ writers: spec SPEC_mcq151.md, check151.py, output mcq_out/m_NN.py. A batch is done when m_NN.py exists.
- Then: `python3 pma151/build151.py` -> pma151/hk_final3.json (merge script picks it up automatically), make_blind.py 160 -> verify/blind_*, blind checkers (SPEC_blind.md) -> verify/answers_*, cmp151.py, fixes in pma151/hk151_overrides.json, rebuild site, test, send.

### Phase 3 DONE
- PMA 151 added: 53 batches, blind check of 1105 new MCQs (12 disagreements reviewed, fixes in pma151/hk151_overrides.json), key current affairs web-checked. Hakeem section now 4304 MCQs, 87 blocks. Timer 20 min for all tests. site/index.html rebuilt and sent.

### Phase 4 (design)
- Hakeem dedupe: dedupe/ (pairs reviewed, apply.py -> dedupe/hk_final_dedup.json, 4033 MCQs). merge script uses it automatically.
- Added blocks injected by merge_into_site.py: pma159/theme_block.html (day/night mode), pma159/auth_block.html (glassy Sign In / Create Account / Continue as Guest, accounts stored in the browser's localStorage only), pma159/seccolor_block.html (each section keeps its colour inside tests incl. Submit button), pma159/polish_block.html (premium look, header avatar, desktop bug fix: hidden views stay hidden).

## Phase 5: ilampoint-style features
pma159/features_block.html (dashboard, streak, Daily Challenge, Saved/bookmarks, Mistakes bank, Search, Share score, keyboard shortcuts) is appended to _blk in merge_into_site.py. Question data unchanged. Rebuild: python3 pma159/merge_into_site.py pma159/base_original_site.html site/index.html

## User preference (standing)
Asadullah's messages may arrive in Hindi/Urdu script (voice typing). Always reply in simple English (Roman Urdu is fine). He asked that this be remembered every session.

## Phase 6: sign-in redesign + liquid glass + 3D
auth_block.html (planet photo scene from space_imgs.json, placeholders {{IMG_scene}} replaced in merge script), glass_block.html (liquid glass, goo blobs, droplets), d3_block.html (3D cubes/orbs/ring, tilt cards, clay buttons). All appended to _blk in merge_into_site.py.

## Phase 7: Hakeem section split by experience
Hakeem Force Academy card -> 3 cards (PMA 149 / 150 / 151 Experience) -> blocks of 50 for that PMA. Each MCQ is written once, in the PMA where it first appeared (repeats from later PMAs only raise the bracket count). Origin list: `python3 dedupe/make_origin.py` -> dedupe/hk_origin.json (parallel to hk_final_dedup.json; 1533 / 1450 / 1050 MCQs, total 4033). merge_into_site.py builds HK_META and renderHK/openHkSub; backnav_block handles Back. Other sections untouched (verified identical).
Second duplicate pass (paraphrased repeats): dedupe/r2_same.txt (33 pairs, reviewed) -> `python3 dedupe/apply2.py` -> hk_final_dedup2.json + hk_origin2.json (4000 MCQs: 1517/1441/1042). merge_into_site.py prefers these. Earlier-placed MCQ kept, counts added.
