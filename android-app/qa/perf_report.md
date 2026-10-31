# Performance and mobile layout audit: www/index.html (offline bundle)

Method: Playwright + /opt/pw-browsers/chromium, local http.server, 393x800 mobile (DPR 2.75, touch), CDP CPU throttling 1x/4x/6x. Default run forces "non-lite" (the page adds `html.lite` when cores<=4 or RAM<=3GB, and this sandbox reports 4 cores). The lite class is also tested. Scripts and raw JSON are in this folder (`a_*.js`, `lib.js`, `res_*.json`). No repo files were edited.
Caveat: headless Chromium uses software rasterisation. Absolute paint/backdrop-filter numbers are pessimistic against a real phone GPU. Relative comparisons are valid.

## 1. Headline: the slowness is not JS or data, it is the per-frame style recalc caused by the parallax loop

JS time is tiny: `selectTest` 2-13 ms, `loadQuestion` about 2 ms, and `startQuiz` 2-30 ms at 4x. But every action takes 200-400 ms to reach the screen at 4x, and idle FPS is 6-7.

Cause: the d3 block (`loop()` using `requestAnimationFrame`) writes `--gx`, `--gy` and `--sy` on `document.documentElement` every frame, forever. Custom properties inherit, so each frame invalidates style for the whole document (about 2300-4000 nodes).

Measured at 4x (non-lite, idle menu, 3 s):

| Variant | FPS | main thread busy | style recalc per second | answer+next paint |
|---|---|---|---|---|
| base | 6-7 | 85% | 750-780 ms | 298-317 ms |
| rAF loop killed (nothing else changed) | 17 | 22% | 68 ms | 92 ms |
| prefers-reduced-motion (loop and CSS motion off) | 60 | 13% | 15 ms | 79 ms |
| everything off (animations, filters, backdrop, decor, loop) | 60 | 4-5% | 0 | 31 ms |

Other single-feature removals gave only modest gains:
- `backdrop-filter: none`: 6 to 7.3 fps.
- `animation: none`: 6 to 8.7 fps.
- `filter: none`: 6 to 10 fps.
- Hide `#liquidBg` and `#obj3d`: 6 to 11.7 fps.

They only help once the root-variable loop is gone. `html.lite` alone does not fix it, because the loop still runs: 7.3 fps, 95% busy.

Idle cost, scroll and quiz paint:
- Idle quiz: 7.3 fps base, 60 fps with everything off.
- Scrolling the HK list: avg frame 166 ms base, 16.7 ms with everything off.
- Every question tap or next costs a full 250-300 ms frame at 4x. At 1x it is fine.

### Fix 1 (minimal, no visual change)
Do not write the vars on `:root`.
- Write `--gx/--gy/--sy` only on `#obj3d` and `#liquidBg` (the only consumers), and add `contain: layout style` on them. The style invalidation then touches a few dozen nodes instead of the whole tree.
- Stop the loop when it is invisible: no `requestAnimationFrame(loop)` while `#auth` is shown, while a quiz is active, or when `document.hidden` is true.
- Also skip the loop when `html.lite` is set.

Expected: idle 6 fps to about 17 fps or better, and per-tap paint 300 ms to about 90 ms at 4x.

### Fix 2 (secondary)
Give `#liquidBg` and `#obj3d` `will-change: transform` or `contain: strict`, and pause their CSS animations during a quiz:
`body.quizing .lb, body.quizing .st, body.quizing .si { animation-play-state: paused }`.
Removing them gained a further 6 to 12 fps.

## 2. Load (3 runs each, median, throttle 1x / 4x / 6x)

| | 1x | 4x | 6x |
|---|---|---|---|
| domInteractive | 392 ms | 1928 ms | 2718 ms |
| DOMContentLoaded | 414 ms | 2004 ms | 2804 ms |
| load | 513 ms | 2428 ms | 3310 ms |
| first paint (FCP) | 144 ms | 428 ms | 576 ms |
| LCP | 184 ms | 1516 ms | 2108 ms |

- Long tasks: 4 at 1x (largest 132 ms). At 4x there are 14 (largest 920 ms at about 1.1 s). At 6x there are 16 (largest 666 ms).
- JS heap after load: 4.6 MB. DOM at load: 2280 nodes, 112 listeners.
- Lite mode is not faster at load: DCL 1474 ms at 4x, with style recalc 1.5 s.
- 4.7 MB HTML is 4.33 MB of data. HK_DATA is 2.66 MB, MR_DATA 0.96 MB, FA 0.33 MB, ALL 0.34 MB. 2312 of 11208 questions have a duplicate question text (MR repeats HK).
- Other resources: fontawesome.css 100 KB, fa-solid woff2 150 KB, tailwind.css 29 KB, 9 font files about 13-25 KB each.
- Parse cost of the data literal (in page, 4x): the first cold evaluation of the object literal is about 450 ms. `JSON.parse` of the same text is about 147 ms. At 6x it is about 500 ms vs about 117 ms.

### Fix 3 (data parse, zero data change)
Emit each `const X_DATA = JSON.parse('...')` (or a `<script type="application/json">` block read with `JSON.parse(textContent)`) in the build script instead of an object literal. This saves roughly 300 ms of the first-load script block at 4x. Optionally, build MR/CN/IV by referencing HK objects, which would cut about 1 MB. This is a data restructuring, so only do it if you want it.

### Fix 4 (tiny)
`/favicon.ico` returns 404, and it is the only console error found. Add `<link rel="icon" href="data:,">`.

## 3. Time per screen (4x, sync JS / time to painted frame)

- Home to section: `openSec` 0.6-17 ms sync, 250-320 ms painted. This is the frame cost from section 1.
- HK sub-lists (all, rep, con, imp, 149): 4-9 ms sync, 187-369 ms painted. 149 is the heaviest at 566 visible nodes.
- `showSelect` (Back): 22 ms sync, 293 ms painted. It calls renderSelect, renderPMA, renderFA, renderHK, renderLC and renderMenu/applySec every time, including hidden sections. That is wasted but small (under 25 ms total sync).
- `selectTest`: 1.6-13 ms sync (the 835-question test is the slowest at 13 ms). It calls `renderPalette()` for N buttons, and `startQuiz` calls it again.
- `startQuiz`: 2.3-7 ms for 50-107 questions. The 835-question test takes 30 ms sync and 348 ms painted.
- Per-question nav (answer + next), 4x:
  - 50 questions: sync 10-17 ms, painted 240-330 ms.
  - 107 questions: 17 ms sync, 396 ms painted.
  - 835 questions: 21 ms sync, 479 ms painted.
  - `updatePaletteUI` rewrites `className` on all N buttons on every question, which is why larger tests are slower. For 835 buttons it is 1.4 ms sync here, but it forces N style invalidations.
- Submit to results, review list (4x), the real data-driven hotspot:

| Test size | Submit | `filterReview('all')` | DOM nodes on results |
|---|---|---|---|
| 50 q | 430-800 ms painted | 380-710 ms | about 2.1-2.4k |
| 89-107 q | 1.1-1.5 s | about 0.6-0.8 s | 3.3-3.7k |
| 835 q (Most Repeated MR) | 65 ms sync, 5.6 s painted | 288 ms sync, 6.9 s painted | 21,692 |
| 835 q, filter incorrect | 229 ms sync, 4.0 s painted | | |

### Fix 5
In `renderReviewList`, make the review cards cheap to lay out and paint:
- Add `.review-card { content-visibility: auto; contain-intrinsic-size: 1px 220px }` on the card `div`.
- Optionally render in chunks of about 40 cards via `requestIdleCallback` / `setTimeout`.
- Optionally show only the first 50 cards plus a "Show more" button.

Also clear `#review-list-container.innerHTML` and `#palette-grid` in `showSelect()`. Otherwise up to about 22k hidden nodes stay in the DOM after leaving a big test.

### Fix 6
`updatePaletteUI`: only update the previous and current button plus the one just answered, instead of looping over all N and rewriting `className`. Also drop `transition` from the palette buttons (class `transition` on 835 buttons).

## 4. DOM counts

- Menu: 2280 nodes in total, about 443 visible nodes at the start of "o".
- Sections: 311-566 visible nodes each. HK sub 149 has 566.
- Quiz screen: about 1.1k to 3.3k nodes total. This includes the hidden lists, because all five section lists are always built (renderSelect, renderPMA, renderFA, renderHK, renderLC).
- Results: 2.1-2.4k nodes for 50-question tests, 3.3-3.7k for CN/IV, 21.7k for the 835-question MR test.

## 5. Leaks (30 open/close cycles, 1x)

- Timers: 0 active `setInterval` after leaving. Every `startQuiz` creates one interval (33 created in total over the run) and it is cleared each time. No timer leak.
- Listeners: flat. Memory.getDOMCounters shows 170 to 170. `getEventListeners` over document, window and every element is unchanged: document 6, window 6, elements 158 to 158 (or 160 after finishing tests). No listener leak.
- Heap after GC: 4.67 to 4.82-4.85 MB, about +0.15 MB over 30 cycles. No meaningful growth. 10 cycles of the 835-question test: 4.72 to 4.95 MB, about +0.23 MB.
- Detached/hidden DOM: nodes grow from 2400 to 5234-5652 after 30 finished tests, because the review list stays in the DOM. After 10 finished 835-question tests the counter showed 58k nodes, so this scales with test size (see Fix 5).
- History: `history.length` grows by about 1.5 entries per open/close cycle, from 5 to 50 over 30 cycles. `selectTest` and `openSec` push entries and the Back button navigates away from them with `history.back()` only once per press. This is a mild UX issue (many Back presses), not a memory leak.
  Fix: use `history.replaceState` when the current state is already `{n:1}`, or push only when entering a new level.

## 6. Layout overflow (393 / 360 / 320)

- 393x800: no document-level horizontal overflow on any screen: login, sign-up, home, five section lists, HK sub-lists, test home, quiz (including the longest question and the longest word, HK-66 with a 29-char word), submit modal, results, review, search.
- 320x640: home overflows by 62 px, and the search modal by 62 px (the dashboard is behind it). The quiz screen overflows by 15 px (header: `#hdrUser` avatar ends at 335 > 320). Results overflows by 8 px in the first run and 0 px in a re-check, so treat it as intermittent.
- 360x740: home overflows by 22 px (the same dashboard cause). The quiz, results and review screens were clean in the re-check. The first run showed results and search at 43 and 39 px, but those came from the same `.dash` overflow behind them.
- Login screen: only decorative `.lyr` and blob elements extend past the edge (aria-hidden, clipped). No real overflow.

Root cause of the home overflow: a CSS class collision. The 3D block defines a global `.st{width:84px;height:84px;filter:drop-shadow(...);animation:bob 26s ...}` for the floating study icons. The dashboard stat tiles `.dash .st` also match it. Four 84 px tiles plus gaps give a minimum width of 366 px, which overflows any viewport narrower than about 398 px. The `.dash .st` tiles also get a drop-shadow filter and a perpetual `bob` animation they should not have.

### Fix 7
Scope the icon rule to `#obj3d .st{...}`, or add `.dash .st{width:auto;height:auto;filter:none;animation:none}`. The dashboard grid (`repeat(4,1fr)`) then fits at 320 px, and 4 animated filter layers disappear.

### Fix 8
Quiz header at 320: reduce `header>div{padding-right:64px!important}` to about 12 px at `max-width: 360px`, or allow the timer and avatar to shrink (`min-width:0`; hide the timer label text).

## 7. Touch targets (393 wide, elements under 44 px)

- Login: show-password eye 23x23, remember-me checkbox 16x16, "Forgot password?" link 116x20, "Sign up" link 50x18.
- Home and section lists: theme button 40x40, Back 40x40, "All categories" 146x38. Test cards are large.
- Quiz: palette buttons 54x36 (min 36), star 38x38, Previous/Next 42 px tall, Submit Quiz 38 px. Option cards are fine.
- Results: review filter buttons 44 px tall but "All" is 36 px wide. Search close button 40x40.
- Nothing is below 36 px except the login eye, checkbox and links. Suggested minimal fix: pad the login links and checkbox (`padding:10px; margin:-10px`) and make the eye 40x40. This changes appearance very little.

## 8. Console errors

Only one: `GET /favicon.ico 404` (see Fix 4). No JS errors or exceptions in any flow, including quiz, submit, review, search and 30-cycle runs.

## 9. Priority order

1. Fix 1 (stop writing vars on `:root`): biggest win, 3x FPS and 3x faster taps.
2. Fix 7 and Fix 8 (layout at 320 and 360): CSS only.
3. Fix 5 and Fix 6 (large-test review and palette): needed for the 835-question MR test, which takes 5-7 s to show results at 4x.
4. Fix 3 (JSON.parse for data): about 300 ms off startup at 4x.
5. Fix 2, Fix 4, history fix.

## 10. Not tested

- Real device GPU, real WebView, and thermal throttling. CDP CPU throttling only slows the main thread, and rasterisation is software here.
- Real touch scrolling and gesture jank. Scroll was simulated with mouse wheel.
- Dark theme (day mode only), desktop widths, and landscape.
- The login form's functional flows beyond showing the screen, and the Android native shell (`AsadApp` bridge).
- Memory growth over longer than 30 cycles, and low-RAM eviction behaviour.
- Fix proposals were not applied or re-measured, except that Fix 1 was confirmed by killing the loop at runtime (6.7 to 17 fps) and the "everything off" variants.
