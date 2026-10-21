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

## Phase 8: PMA 152 (6033-page PDF) added
Pipeline in `pma152/` (same as 151): chunks c_01..40 -> extract -> cluster152.py/match152.py (existing = dedupe/hk_final_dedup2.json) -> mcq_in/b_01..46 -> writers mcq_out/m_NN.py -> `python3 pma152/build152.py` (hk_final4.json + hk_origin4.json; overrides in hk152_overrides.json) -> blind check (verify/, cmp152.py; 7 disagreements reviewed) -> `python3 pma152/apply_dups.py` merges 41 paraphrased repeat pairs (dup_pairs_text.json) -> hk_final5.json + hk_origin5.json. merge_into_site.py prefers hk_final5/hk_origin5.
Result: Hakeem section 4798 MCQs: PMA 149 1517, PMA 150 1441, PMA 151 1042, PMA 152 798 (16 blocks). Questions already on the site only got their repeat counts raised. Hakeem colour is now rose/pink (seccolor_block, SECS grad). Time-sensitive facts web-checked (Bangladesh President, GB Governor, KP governor's rule since 11 Oct 2026, etc).

## Phase 9: PMA 153 (8337-page PDF; its text layer is broken: word fragments, lost spaces) added
Pipeline in `pma153/` (same as 152): chunks c_01..49 -> extract (agents rebuilt questions from garbled text, ok=false when unsure) -> cluster153.py/match153.py (existing = pma152/hk_final5.json) -> mcq_in/b_01..49 -> writers mcq_out -> `python3 pma153/build153.py` (hk_final6.json/hk_origin6.json; overrides in hk153_overrides.json: 7 removals + fixes of the existing "342-member National Assembly" MCQ -> 336/169) -> blind check (cmp153.py, 11 disagreements reviewed) -> `python3 pma153/apply_dups.py` merges 29 paraphrased repeats -> hk_final7.json + hk_origin7.json (preferred by merge_into_site.py).
Result: Hakeem section 5720 MCQs: PMA 149 1517, 150 1441, 151 1042, 152 797, 153 923. Hakeem colour is now ocean blue (sky/cyan). Time-sensitive answers web-checked.

## Phase 10 - PMA 154 (done)
- Hakeem now has PMA 154 (5 tests, 222 new MCQs). Total Hakeem 5942.
- FINAL RULE from user: an MCQ in PMA 154 that already exists in PMA 149-153 is NOT written in 154; it stays in the earlier PMA and its repeat count is raised by the 154 repeats (940 earlier MCQs got higher counts). Only genuinely new MCQs are in 154. (An earlier version copied them into 154; user rejected that.)
- Pipeline in pma154/: extract -> cluster154/match154 -> writers -> build154.py -> blind check (233 new, 0 disagreements) -> paraphrase merge (dup_pairs_text.json, 14 pairs; apply_dups.py never merges two earlier-PMA MCQs) -> hk_final7/hk_origin7.json. Build: `python3 pma159/merge_into_site.py pma159/base_original_site.html site/index.html`.
- Weak spots: writers skipped vague/garbled questions; blind check was quick.

## Phase 11 - PMA 155 (done)
- PDF "PMA 155 long course important MCQs" = list of short Q + answer (not experiences). Pipeline in pma155/ (same as 154, apply_dups.py uses N0=5942). Rule: repeats of earlier-PMA MCQs raise the earlier MCQ's count (394 MCQs), only new MCQs (148) are in PMA 155 (3 blocks). Total Hakeem 6090.
- Blind check: 154 new, 5 disagreements; removed 2 ambiguous (first institution of Islam, Zardak Peak). Candidate answers in the PDF are often outdated; our answers are current (Oct 2026).
- merge_into_site.py now supports 155 (card, HK_META, texts).

## Phase 12 - PMA 156 (done)
- PMA 156 PDF (919 pages, experiences format) done with same pipeline (pma156/, existing = pma155/hk_final7.json, apply_dups N0=6090). Rule unchanged: repeats raise earlier PMA's count; only new MCQs (177) in PMA 156 (4 blocks). Total Hakeem 6267. merge_into_site.py supports 156.
- Blind check 193 new: 0 disagreements (checkers mostly did not use web); 3 current-affairs facts verified by web search (AO 2026 final, ISI DG, Bangladesh PM).

## Phase 13 - PMA 157 (done)
- PMA 157 PDF (337 pages, experiences format) via pma157/ pipeline (existing = pma156/hk_final7.json, apply_dups N0=6267). Same rule: repeats raise earlier PMA's count (314 MCQs); only new MCQs (156) in PMA 157 (4 blocks). Total Hakeem 6423. merge_into_site.py supports 157.
- Blind check 162 new (with web search): 2 disagreements, both ambiguous (national dish, martial law count) -> removed.

## Phase 14 - Hakeem menu: All Experiences + Most Repeated (done)
- PMA 158 PDF was byte-identical in text to PMA 155 (checked); not added.
- Hakeem Force Academy now opens a landing page with 2 cards: "PMA All Experiences" (the PMA 149-157 cards, unchanged) and "Most Repeated MCQs".
- Most Repeated: tests are repeat-count BANDS, no MCQ in two tests: 500+, 450-499 (empty, skipped), 400-449, 350-399, 300-349, 250-299, 200-249, 150-199, 100-149, 50-99, 40-49, 30-39, 20-29, 10-19 (14 tests incl. 5-9 band, 2274 MCQs). Keys `MR-<lower>`; HK_META has pma:'rep', thr, hi. Time = 30 s per MCQ (nQ*30). MCQs are copies; the PMA tests are untouched.
- hkSub states: null (landing), 'all', 'rep', number (PMA). Back: number->'all'->null->menu. merge_into_site.py (MR_THR, isMR, renderHK), seccolor/backnav blocks updated.
- Added band 5-9 (MR-5, 835 MCQs, ~418 min).

## Phase 15 - Timer pace (done)
- All tests (1000 MCQs, PMA 159, Forces Academy, Hakeem PMA tests, Most Repeated) now use SEC_PER_MCQ = 30 seconds per MCQ (50 MCQs = 25 min). Real PMA initial test (unofficial prep sites): verbal ~84 MCQs/30 min (~21 s), non-verbal ~64/30 min (~28 s), academic ~50/30-40 min (36-48 s); whole paper ~27 s average. Change SEC_PER_MCQ in merge_into_site.py to adjust.

## Phase 16 - Constitution of Pakistan (done)
- PDF "constitution of Pakistan 1956,1962,1973" has 96 MCQs with the author's answers (some wrong). pma160/src_mcqs.json = parsed list; agents (m_s1, m_s2) fixed wording/answers with web search -> 89 MCQs kept (7 dropped as unverifiable/duplicate). User said: NO MCQs of our own. Extra MCQs written by agents (m_e1..e4, 336 MCQs, con_all.json) are NOT used (kept in repo only).
- Hakeem landing now has a 3rd card "Constitution of Pakistan" -> ONE test CN-1 (89 MCQs, 30 s each = 45 min). If the same MCQ exists in Hakeem sets, its repeat count (hk_final7 rep) is shown in brackets (18 MCQs); the existing Hakeem MCQs are untouched. Data: pma160/constitution_final.json; site code in merge_into_site.py (CN, isCN, hkSub 'con').

## Phase 17 - 100 Most Repeated Questions (done)
- PDF MOST_IMPORTANT_VERBEL_QUESTIONS (100 verbal statements, several wrong) -> pma161/ (src_text.txt, m_v1/m_v2 writer outputs, verbal_final.json = 107 MCQs; multi-part items split, 4 items skipped as ambiguous/missing). Wrong printed answers corrected (items 25, 28, 31, 34, 37, 43, 51, 53, 73, 89, 98).
- Hakeem landing now has a 4th card "100 Most Repeated Questions" -> ONE test IV-1 (107 MCQs, 30 s each = 54 min). Bracket = repeat count of the same MCQ in the earlier Hakeem tests (81 MCQs); earlier tests untouched. Site code: IV/isIV/hkSub 'imp' in merge_into_site.py.

## Phase 18 - New PMA 159 file (Vision Force Academy) merged into PMA 159 section (done)
- File "PMA 159 Experience vision force academy" (74 MCQs) -> pma162/ (src_items.json, m_p1.py, m_p2.py with MATCH/NEW). 32 items matched existing PMA 159 MCQs: their repeat count (rep) +1 each, MCQ not rewritten. 39 new MCQs appended to the PMA 159 list (items 42 and 52 removed after review) -> 308 MCQs, 7 parts (part 6 filled to 50, part 7 has 8). Done in merge_into_site.py right after `from questions import Q` (questions.py untouched). Old 269 MCQs verified unchanged (question+answer).
- Writers did not use web search for this file (facts are stable); item 13 author answer Tuesday was wrong (Monday used).

## Phase 19 - Light Forces Academy experiences added to PMA 159 section (done)
- Narrative file (10 write-ups, ~48 remembered questions without answers) -> pma163/ (clean.txt, m_q1.py MATCH/NEW; existing list = current 308-MCQ PMA 159 list). 6 matched existing (rep +1), 26 NEW written with web-verified answers, 2 duplicates merged (items 31->7, 42->20, rep+1) -> 24 added; PMA 159 now 332 MCQs, 7 parts (part 7 has 32). 15 items skipped as unclear/disputed (age at Hijrat, atomic site, CPEC HQ, etc.).
- merge_into_site.py applies pma162 then pma163 right after `from questions import Q`.

## Phase 20 - PMA 158 Long Course section (done)
- New 5th category on the home menu (after Hakeem Force Academy): "PMA 158 Long Course MCQs" (violet). Source "Pma_158_LC_15-_students_experience" (226 numbered items, many answers wrong/missing) -> pma164/ (clean.txt, m_a1..a3.py, pma158_all.json, pma158_final.json = 205 MCQs, 5 tests LC-1..LC-5 of 50, last has 5). 30 s per MCQ. Items skipped as vague/disputed (Iran operation name, Hero's Medal, India dam river, plateau/peak of Balochistan, 1937 seats, Quaid-e-Azam title year, first CJ, first naval chief, King of Khan, Usman Quran copies etc.). Blind check: 2 disagreements: #72 area of Pakistan removed (881,913 vs 796,096 disputed); Shaikh-ul-Anbiya = Nuh kept.
- merge_into_site.py: LC dict, isLC, renderLC, lc-grid, SECS entry id 'lc', seccolor 'lc'.

## Phase 21 - Pro Genius "Solved Academic Experience" PDF added to PMA 159 section (done)
- PDF is page images (no text): pages rendered to pma165/pg/p-NN.png and read visually by agents (m_r1..r3.py MATCH/NEW; list of existing = 332 MCQs). 58 items seen: 47 matched existing PMA 159 MCQs (rep +1 each; Q46 read twice, counted once), 7 NEW (appended, part 7 now 39), 4 skipped (Gwadar price, Hajj year, two unclear maths, Balochistan plateau). PMA 159 = 339 MCQs, 7 parts. merge_into_site.py applies pma162, pma163, pma165 in order after `from questions import Q`.


## Phase 22 - Android APK + full MCQ answer audit
- Android project: `android-app/` (package com.asadullahnotes.mcq, v1.0.0, minSdk 24, target 35). Signed APK: `android-app/release/AsadullahNotes-1.0.0.apk`. Keystore is OUTSIDE the repo (`/home/user/keystore/asadullah-notes.jks`, user was sent a copy) - never commit it. Read `android-app/README.md` and `android-app/docs/FIXES_AND_LIMITS.md`.
- Web bundle for the app is built by `android-app/tools/build_web.py` from `android-app/source/index.html` (= `site/index.html`); offline, performance and layout fixes live only in that script (and tools/android_head.html), not in the Netlify site.
- Audit: all 8,931 unique MCQs blind-checked (batches in `android-app/verify_all/`), 360 flagged items re-judged, 70 MCQs patched via `pma159/corrections.json` (applied at runtime inside the page by `merge_into_site.py`, matched by test key + id). 22 unresolved items listed in `verify_all/final_lists.json`. Web search budget ran out, so many current-affairs answers are NOT web-verified.
- Not tested on a real device or emulator.

- v1.0.1 (versionCode 2): smoothness fix in `android-app/tools/build_web.py` + `tools/android_head.html` (always 'lite': no backdrop-filter/blur/animations; JSON.parse data). Netlify site unchanged. APK: `android-app/release/AsadullahNotes-1.0.1.apk`.
- v1.0.2 (versionCode 3): login parallax off, instant scroll on Next, in-place option update (`answerInPlace` patched in build_web.py), :hover rules stripped, decorative layers hidden in app. APK: `android-app/release/AsadullahNotes-1.0.2.apk`. User's phone: Samsung Galaxy A07 (budget).
- v1.0.3 (versionCode 4): filter-free coloured background (FLAT block in build_web.py). APK: android-app/release/AsadullahNotes-v103.apk
- v1.0.4 (versionCode 5): status bar colour follows page (MainActivity.kt 'top:#rrggbb' bridge + tools/android_head.html). Nothing else changed. APK: android-app/release/AsadullahNotes-v104.apk
- v1.0.5/1.0.6: fixed selector-split bug in hover-strip script (coloured block behind quiz), removed page-entry animations, rounded instructions box, native app-styled confirm dialog (showAppDialog in MainActivity.kt). APK: android-app/release/AsadullahNotes-v106.apk
- v1.0.7/1.0.8: 7 more MCQ fixes (161,686,749,852,911,3923,1349) in pma159/corrections.json; smooth theme-switch fade in tools/android_head.html. APK: android-app/release/AsadullahNotes-v108.apk
- v1.0.9: theme switch now uses document.startViewTransition cross-fade (no blank screen); v1.0.8 overlay-fade removed. APK: android-app/release/AsadullahNotes-v109.apk
- v1.0.10: page drawn behind status bar (MainActivity.kt topInsetPx/applyInsetToPage + --sat CSS in tools/android_head.html). APK: android-app/release/AsadullahNotes-v1010.apk
- v1.0.11: press feedback (:active scale/opacity) in tools/build_web.py PRESS block. APK: android-app/release/AsadullahNotes-v1011.apk
- v1.0.12: themeBtn/brand/side selectors given higher specificity (html body ...) so --sat offset wins over page rules; header 97% opaque. APK: android-app/release/AsadullahNotes-v1012.apk

## Phase 23 - 11 friends' PMA 159 experiences (Oct 2026) added
- Raw text pma166/raw.txt, de-duplicated items pma166/items.json (108, with count), 12 slices m_s01..12.py (MATCH raises rep by count, NEW appended), pma166/drop.json (dropped NEW item ids), blind check in pma166/blind/ (55/55 agree). merge_into_site.py applies pma166 after pma165. PMA 159 = 394 MCQs, 8 parts. APK v1.0.13: android-app/release/AsadullahNotes-v1013.apk

## v1.0.14 (versionCode 15)
- Custom Range Test (From/To total-ask range, block size, 30 s per MCQ, "Start ALL").
- PMA 159 now 394 MCQs (8 tests). 5 wrong MATCH counts fixed. 2 broken MCQs fixed (1-50 id 23, 451-500 id 31).
- Native fixes: dialog leak, render-crash loop, saved bar colours, onJsBeforeUnload.
- CSS: themeBtn z-index 40, review scroll margin, header title/avatar hidden <=380px.
- Known: 28 MCQs in 1000 MCQs (51-100, 951-1000, 1-50) have no reason text in data. Not tested on a real phone.

## v1.0.15 (versionCode 16)
- AI Helper: round button bottom-right (pma159/ai_block.html). Offline = keyword search over all MCQs; Online = POST to Netlify function netlify/functions/ask.js (Gemini, key in env GEMINI_API_KEY; setup in netlify/SETUP_AI_ONLINE.md). Quick-action chips for the current question. Image/PDF/text attach (online).
- APK now has INTERNET permission (Online mode only) and a file chooser; server address set via gear box.
- Known: some original 1-50/51-100 MCQs have wrong or missing reason text (e.g. 1-50 Q1 shows FIFA text). Not edited (data rule).

## v1.0.16 (versionCode 17)
- Reason text fixed for 109 original MCQs (28 had none, 81 had unrelated text) via corrections.json (facts only; no question/option/answer changed). Written by 5 agents mostly from knowledge (only slice 4 and part of slice 2 used web search). 901-950 id 31 (Noah's ark 6 months) is tradition-based and noted as such in the text.

## v1.0.17 (versionCode 18)
- New main category "Pro Genius Academy MCQs" (PG-n tests, 299 MCQs in 6 tests of 50, from progenius/*.pdf: PMA 159 experience + PMA Important MCQs). Source PDFs had no options, so 3 wrong options per MCQ were generated by agents; answers blind-checked by 3 more agents (7 disagreements: 5 ambiguous MCQs dropped, 1 reworded, 1 kept with note). 7 repeats merged with (2). Data: progenius/pg_final.json. "Famous 1000 MCQs" (PF-n, progenius/pf_final.json) shows "Coming soon": the 35 MB PDF is not uploaded yet.
- Pro Genius is NOT counted in Range "All sections"; Custom Range Test now has a Category chooser (All / 1000 MCQs / PMA 159 / Hakeem / Forces Academy / PMA 158 / Pro Genius); counts only inside the chosen category.

## v1.0.18 (versionCode 19)
- Pro Genius "Famous 1000 MCQs" (PF-n): 818 unique MCQs in 17 tests (sum of repeat counts 1102; 1110 entries read from the scanned PDF progenius/Al Famous Thousand...pdf, 132 pages, read by 11 vision agents; 6 dedupe agents; 6 blind-check agents; 7 ambiguous items dropped, 3 fixed). Data: progenius/pf_final.json (raw: pf_final_raw.json, work2/).
- Range test "All sections" now ALSO counts Pro Genius (user request); Pro Genius is also its own category chip.

## v1.0.19 (versionCode 20)
- Currency check of all 1117 Pro Genius MCQs (7 agents, ~87 verified by web search, the rest static). 3 dropped (KP CM, Pak-Afghan border length, first Pakistani woman on K2: sources disagree), ~23 got an updated explanation with 'As of Oct 2026' notes (27th Amendment, hydel share, KP governor's rule 11 Oct 2026, etc.), PG158 and PF39 explanations/question fixed. PF now 815 MCQs (17 tests), PG 299 (6 tests).

## v1.0.20 (versionCode 21)
- "Non Verbal PMA Test" (NV-1) as 3rd option inside Pro Genius Academy: picture MCQs redrawn as SVG by agents from progenius/nv/Non_Verbal_04.pdf (22 puzzles). The PDF has no answer key: each puzzle was solved by 2 independent blind solvers; only the 13 where both agreed shipped (PDF Q3,4,5,6,8,9,11,12,13,14,20,21,22); 9 disagreed and were dropped (Q1,2,7,10,15,16,17,18,19) - waiting for the user's answer key. Q3, Q8, Q9 carry a "check with your key" note. Each question has a Solution and a Trick text. Code: pma159/nv_block.html, data progenius/nv_final.json (build: progenius/nv/build_nv.py with DROP env).
- Fixed: short tests could never PASS (needed 25 correct); now >= 50%.

## v1.0.21 (versionCode 22)
- Non Verbal PMA Test moved OUT of Pro Genius into its own main category (7th card, id 'nv'). 19 puzzles (PDF Q1-6,8-14,17-22). Votes (first solver + second blind solver + 3 solvers on the original PDF) for the 9 disputed ones: Q1,2,10,17,18,19 got a clear majority and were added (Q2,10,17,19 carry a 'please check with your key' note); Q7, Q15, Q16 stayed ambiguous (no option is a true mirror in Q7; Q15 has two mirror images; Q16 has two near-identical figures) and are left out until the user supplies an answer key. Build: DROP=7,15,16 python3 progenius/nv/build_nv.py.

## v1.0.22 (versionCode 23)
- User supplied the true answers for two Non Verbal puzzles: PDF Q2 = option 5, PDF Q17 = option 3 (both were wrong in the agents' solutions, so the other agent-solved puzzles are still unverified against a real key: Q1,3,4,5,6,8,9,10,11,12,13,14,18,19,20,21,22). Asked the user for the full key (also for Q7, Q15, Q16 which are not shipped).

## v1.0.23 (versionCode 24)
- Hakeem Force Academy: the "Most Repeated MCQs" card (MR-n tests) removed at the user's request; Hakeem now has 3 cards: PMA All Experiences, Constitution of Pakistan, 100 Most Repeated Questions. (MR data still in the file but not shown; the Custom Range Test category chips cover it.)

## v1.0.24 (versionCode 25)
- AI Helper (round robot button) REMOVED at the user's request: pma159/ai_block.html and the netlify/ folder deleted (still in git history), INTERNET permission removed again (app has no permissions). The unused file-chooser code in MainActivity.kt stays (harmless).
