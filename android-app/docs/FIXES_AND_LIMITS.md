# Fixes, optimisations, tests, limits

## MCQ audit (all 8,931 unique MCQs = 11,208 entries in 196 tests)
- Every unique MCQ was solved blind (marked answer hidden) by an independent agent: 8,931 of 8,931 answered.
- Matches marked answer with high/medium confidence: 8,678. Low-confidence match: 84. Disagree: 48. Flawed/unclear (X): 121.
- 360 flagged or time-sensitive items were re-judged (7 answer changes, 78 rewrites suggested, rest KEEP).
- Applied: 70 MCQs fixed (75 occurrences): 29 answers changed, 41 same answer but option/question/reason text repaired (duplicate or junk options, wrong wording, outdated counts such as constitution amendments, KP governor's rule 11 Oct 2026). Plus 4 formatting fixes (Surah An-Naml x2, Ionian Sea x2).
- No MCQ was deleted. Test count (196) and entry count (11,208) are unchanged; exactly 79 entries differ from the earlier site.
- NOT resolved (left exactly as they were): 22 MCQs (see verify_all/final_lists.json): ambiguous or unverifiable (e.g. number of OIC countries in Asia, Fatima Jinnah joining year, "What is Pakistaniat", KP district count, largest city by population).
- Limits: the shared web-search budget ran out during the check, so many time-sensitive items (office holders, rankings, 2025-26 events) were answered from model knowledge and are NOT web-verified. About 360 such items were re-judged but mostly also without search. Please spot-check current-affairs MCQs.
- Garbled OCR text in the "reason" of the first 1000 MCQs (about 400 flagged) and small option typos were reported but not mass-edited (only 4 certain fixes applied) to avoid damaging content.

## App fixes and optimisations
- Offline: Tailwind precompiled, fonts and icons bundled, Netlify HUD script removed, no network needed.
- Parallax animation wrote CSS variables on <html> every frame (whole-page style recalc, 6-7 fps at 4x CPU throttle): now written only on the two decorative layers, paused when the app is in the background, and off on low-end phones ("lite" mode: no animations/blur).
- Layout fixes: dashboard tiles no longer overflow on 320/360 px wide screens; quiz header fits at 320 px; long review lists render only visible cards.
- Native shell: no external browser, safe WebView settings, no SSL bypass, back button confirmation during a quiz, error screen with "Try again", system bar colours follow day/night theme, zoom disabled, portrait.

## Tests actually run
See the end of this file for the final table.

### Quiz bug found and fixed in the app
- If the timer reached 0 while the "Submit?" popup was open, the popup stayed on top of the results and blocked the next test. Fixed in the app bundle (not in the Netlify site file).

## Test results (all run in desktop Chromium via Playwright with phone-size screens, the real bundled files, internet blocked)
| Area | Result |
|---|---|
| Quiz flow on 8 test types (1-50, PMA, FA, HK, MR, CN, IV, LC): timer 1s/s, single timer, question order, Prev/Next, answer record, palette colours, jump, submit popup, score, pass/fail, best score saved, review and filters, retake, Back confirmation | 243 checks pass |
| Auto-submit at 0 (3 test types), popup closed after fix | pass |
| Answer cannot be changed after the first click | by design in the site (instant feedback mode); not changed |
| Data: 196 tests, 11,208 entries; APK file data = source file data | identical |
| 8 MR tests, CN-1, IV-1 are not listed as separate cards on the home menu | by design, they open from the Hakeem sub-pages |
| Layout 393 / 360 / 320 px wide | no sideways overflow after fix (was 62 px / 22 px) |
| JS errors / console errors | none |
| Speed (CPU slowed 4x, software drawing): idle frame rate | 6-7 fps before, 12-15 fps (full effects) / 60 fps (low-end "lite" mode) after |
| Leaks: 30 open/close cycles | no timer/listener leak, memory about flat |
| APK: builds, signed (v2 + v3), package/version/permissions (none), same index.html inside APK as source | pass |

## NOT tested
- No Android emulator or real phone was available (no hardware virtualisation here): install, launch, WebView behaviour, hardware back button, rotation, system bar colours, real-device speed and the native error screen were NOT run on a device. Native code compiled and the APK signed, nothing more.
- Lint was not completed (Maven returned "too many requests" for lint's own libraries).
- Dark theme and landscape were not tested.
- Review of 835-question results can still take several seconds on slow phones (only partly improved).
- Data saved by the Netlify site (best scores, login) does not carry into the app (different origin).
- The quiz-QA helper agent never wrote its own report; the results above come from running its script myself.
