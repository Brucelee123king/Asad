# Fixes, optimisations, tests, limits

## MCQ audit (all 8,931 unique MCQs = 11,208 entries in 196 tests)
- Every unique MCQ was solved blind (marked answer hidden) by an independent agent: 8,931 of 8,931 answered.
- Matches marked answer with high/medium confidence: 8,678. Low-confidence match: 84. Disagree: 48. Flawed/unclear (X): 121.
- 360 flagged or time-sensitive items were re-judged (7 answer changes, 78 rewrites suggested, rest KEEP).
- Applied: 79 MCQs fixed (84 occurrences; the last 9 after a second web-verification round): 30 answers changed, 49 same answer but option/question/reason text repaired (duplicate or junk options, wrong wording, outdated counts such as constitution amendments, KP governor's rule 11 Oct 2026). Plus 4 formatting fixes (Surah An-Naml x2, Ionian Sea x2).
- No MCQ was deleted. Test count (196) and entry count (11,208) are unchanged; 88 entries differ from the original site.
- Second round (19 agents, web search): 187 items re-checked; 135 confirmed, 34 could not be verified because search was refused, 9 clearly supported fixes applied (e.g. Liaquat's 1950 USA visit, Rawalpindi interim capital 1959, a junk-option cleanup). Unapplied suggestions (low confidence or disputed) include: largest city (Jakarta vs Tokyo), KP district count, 'Hero's Award', salah count.
- NOT resolved (left exactly as they were): about 22 MCQs plus the 34 unverifiable ones (see verify_all/final_lists.json): ambiguous or unverifiable (e.g. number of OIC countries in Asia, Fatima Jinnah joining year, "What is Pakistaniat", KP district count, largest city by population).
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

## v1.0.1 - smoothness update (after a real-phone report of lag)
- Cause found: the glass styles put a heavy blur (backdrop-filter) on the header, every card and hundreds of list buttons; the app also ran decorative animations on phones with 6-8 cores.
- Fix (app only): blur/backdrop/drop-shadow filters and continuous animations are always off in the app; pointer tracking skipped on touch; data tables loaded with JSON.parse. Look is almost identical.
- Measured (Chromium, CPU slowed 6x, software drawing): idle 8 fps -> 60 fps, scroll frame time 197 ms -> 29 ms, start-up a little faster. Question data identical (11,208 entries). Still NOT measured on a real phone.

## v1.0.2 - login drag, Next button and tap-blink fixes (reported on a Samsung Galaxy A07)
- Login page: touch / gyro / mouse parallax rewrote CSS variables on every move (3D card re-transformed while dragging) -> parallax removed, page is static.
- Next / Previous: long smooth-scroll animation (1-2 s) replaced by an instant scroll; question palette no longer rewrites unchanged classes.
- Option tap: the 4 option cards are now updated in place (no full rebuild); result checked identical to the old behaviour on 36 taps in 6 test types.
- Tap blink: sticky :hover styles removed (0 hover rules left), two full-screen decorative layers (blurred blobs, 3D icons) hidden, tap highlight / text selection flash disabled.
- Full walk-through (201 steps: login, theme, search, 5 sections, 7 Hakeem pages, 8 quiz types incl. 835-question test: start, answer, next, jump, submit, review, retake, back) with CPU slowed 4x: 0 errors; only theme toggle (about 0.3 s) and result screens (0.15-0.25 s) show a short pause.
- Still not measured on the phone itself.

## v1.0.3 - look fix after a real-phone screenshot
- The "goo" SVG filter on the coloured background blobs rendered as solid purple blocks on the phone GPU. Replaced with filter-free soft radial gradients (same colours), study icons kept (static), page colour #eef2f8, cards slightly see-through, corners clipped. No blur, no animation.
- Measured (CPU slowed 6x): scroll frame 172 ms -> 16 ms, idle 10 -> 60 fps. 201-step walk-through: 0 errors.

## v1.0.4 - status bar follows the page
- The bar at the very top (time / battery) was always indigo. The page now tells the app the colour at its top (login: lavender, app screens: white by day / deep indigo at night); the app paints the status bar with it and switches the icons dark/light. Nothing else changed.

## v1.0.5 / v1.0.6 - section-colour box, corners, styled dialog
- Bug found and fixed: my "no hover" script split selector lists inside `:is(...)`, which turned one rule into `#view-quiz{background:<section colour>}` - this painted a solid orange / sky-blue / purple / green block behind every test page (day and dark mode). Fixed (selectors are now split only on top-level commas).
- Page-entry animations (blur + 3D) removed in the app; "Important Instructions" box has all four corners rounded again.
- The "Leave this test? Your progress will be lost." box (and log-out / alerts) is now an app-styled dialog: rounded card, icon, "Stay" / "Leave" buttons, follows day/night. Compiled and packaged but NOT seen on a device (no emulator here).

## v1.0.7 / v1.0.8 - answer updates after the web re-check, smooth theme switch
- 7 more MCQs fixed (8 entries): 161 (Chief Justice selection, now 27th Amendment rule), 686 (largest city: Jakarta, UN 2025), 749 + 852 (Fatima Jinnah, 1934), 911 (squash: 14 World Open titles), 3923 (namaz made obligatory on the night of Mi'raj), 1349 (snake crawls). 88 + 8 = 96 changed entries in total; still 196 tests / 11,208 entries; nothing deleted.
- Still unresolved (left as they were): about 11 items, see verify_all/final_check_report.md section C.
- Day / night switch (v1.0.8 used a black-out fade and was removed): v1.0.9 uses the browser's View Transitions, which keep a picture of the old screen and cross-fade it into the new theme in about 0.3 s - the screen never goes blank. On a very old WebView it simply switches at once.

## v1.0.10 - status bar matches the page exactly
- Android 15+: the page is now drawn behind the status bar, so the page's own background (login gradient, header white / indigo, day or night) reaches the very top - no separate coloured strip. The app passes the bar height to the page as CSS `--sat`; header, theme button, login brand/card and search box start below it. Status-bar icons switch light/dark with the page colour.
- Older Android (14 and below): the bar is still painted with the page's top colour (previous behaviour).
- Checked in a desktop browser with a 28 px bar; native part compiled, not seen on a phone.

## v1.0.11 - tap feedback back
- Every tappable thing (buttons, option cards, test cards, category tiles, palette numbers, login buttons) gives a light press effect: shrinks slightly (2.5% for big cards, 5% for buttons) and dims a little for 0.12 s while pressed. Transform/opacity only, so it stays smooth. Checked in a desktop browser on 7 element types.

## v1.0.12 - day/night button position, solid header
- The day/night (moon/sun) button had slipped up into the status bar (the page's own rule overrode the new position). It now sits below the status bar, in line with the avatar / logo (checked with a 34 px bar).
- Header is nearly solid (97%), so page text no longer shows through it.

## v1.0.13 - PMA 159 section extended with 11 friends' experiences (Oct 2026)
- 108 remembered questions (cleaned, de-duplicated) were processed by 12 agents with web checks: 46 repeated MCQs already in PMA 159 got their repeat count raised (written once, count in brackets); 55 new MCQs were appended (all 55 solved blind by 3 other agents, 0 disagreements); the rest were skipped as vague / disputed (e.g. sons of Prophet SAW, sons of Hazrat Ibrahim, direction of China, KP Chief Minister during Governor's rule, Hajj faraiz, Highest plateau of Balochistan, number of Government houses). 1 new MCQ (Hajj faraiz) dropped as disputed.
- PMA 159: 339 -> 394 MCQs, 8 tests of 50 (last has 44). Other sections unchanged. Source files: pma166/.
