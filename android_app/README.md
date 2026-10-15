# HabitFlow (Android)

HabitFlow is an offline-first habit tracker. The interface is an HTML/CSS/JS app (`habitflow/`) bundled inside a small native Android shell (`app/`). The native shell adds reminders, notification actions, a home-screen widget, app shortcuts and file export. Everything runs on the device, with no server, API keys or accounts in the cloud.

## Build

Requirements: JDK 17+, Android SDK (platform 35, build-tools 35), Gradle 8.7+.

```bash
cd android_app
python3 build_assets.py                 # copies habitflow/ + login/classic pages into app/src/main/assets
cp keystore.properties.template keystore.properties   # fill in your release keystore (never commit it)
gradle assembleDebug assembleRelease bundleRelease     # debug APK (signed with the same key), APK: app/build/outputs/apk/release, AAB (Play Store): app/build/outputs/bundle/release
```

Without `keystore.properties`, `assembleDebug` still works but produces a debug-signed APK. **Keep the release keystore and its password safe.** Every future update must be signed with the same key, or users have to uninstall first.

## Tests

```bash
node android_app/habitflow/tests/core.test.js                       # 30 unit tests: schedules, streaks, goals, reminders…
for tz in UTC America/New_York Asia/Kolkata Pacific/Auckland; do TZ=$tz node android_app/habitflow/tests/core.test.js; done
```

End-to-end tests (Playwright, Chromium, 390×844), 27 checks, including tapping every control on 35 screens:

```bash
cd android_app && python3 build_assets.py && NODE_PATH=$(npm root -g) node habitflow/tests/e2e.test.js
```

They cover:

- sign-up, login, password reset and onboarding
- Android back-button behaviour (sheet → screen → Home → exit)
- habit creation, check-ins with undo, and Add/Set for amounts
- journal, mood, goals, the focus timer and the assistant
- every settings screen, theme changes, and persistence after reload

Native features (notifications, widget, shortcuts, boot rescheduling) compile and are wired up, but have **not** been tested on a physical device or emulator.

## Architecture

| Path | Purpose |
|---|---|
| `habitflow/js/core.js` | Pure logic, no DOM: schedules (incl. history-preserving schedule changes), check-in rules, streaks, rates, goals, challenges, mood, achievements, reminder planning, CSV, backup validation/migration |
| `habitflow/js/ui.js` | Reusable components: icons, progress ring/bar, bar & line charts, heatmap, segmented control, switch, badges, bottom sheet, toast with Undo, confirm dialog, formatters |
| `habitflow/js/app.js` | Storage, routing (with Android back button), undo-able mutations, global habit actions, native bridge sync |
| `habitflow/js/screens/*.js` | Home, Journal (check-in/notes/mood), Progress (overview/calendar/goals/habits), Focus, Settings and sub-screens, habit form/library/details, goals, assistant, onboarding |
| `pages/login.html` | Welcome/login, local accounts, recovery code |
| `app/src/main/java/...` | `MainActivity` (WebView + JS bridge), `Reminders` (alarms, notifications, action queue), `ReminderReceiver` (alarms, Done/Snooze, boot/time-zone changes), `HabitWidget` |

## Data model (stored per user in the WebView's localStorage, JSON, versioned with migrations)

- **habits**: `id, name, desc, icon, color, type (build|reduce|quit), goal {kind: check|count|time, target, unit, step, limit}, sched {kind: daily|weekly(days)|interval(every)|monthly(dom)|times(n, per week|month|year)|once}, schedHist [{from, sched}], start, end, pauses [{from,to}], part (section), cats [], check [{id,t}] (checklist), rem {on, times[], byDay{weekday:[time]}, msg}, stack (habit id), priority, notes, archived, order, created`
- **entries**: keyed `habitId|YYYY-MM-DD` (one record per habit per day, so duplicates are impossible): `st (done|skip|fail), v (amount/minutes), chk [step ids], n (occurrences), occ [{ts, trig}], note, at (completion time)`
- **journal** `[{id, date, kind daily|weekly|monthly, text, mood, tags[], ts}]`, **moods** `[{id, date, mood 1-5, note, ts}]`, **focus** `[{id, ts, date, secs, mode, label, hid}]`
- **goals** `[{id, name, period, target, unit, start, due, habitIds[], ms[{t,at}], log[{date,v}]}]`, **challenges** `[{id, habitId, days, start}]`
- **cats** `[{id, name, color, icon}]`, **sections** `[{id, name, icon}]`, **settings** (theme, accent, density, text size, week start, formats, quiet hours, notifications, profile, home cards…)
- **Accounts**: `ht.users` stores a salted SHA-256 hash stretched 4,000 rounds plus a hashed recovery code. Passwords are never stored.

## Feature status

**Implemented & working (tested in browser):**

- Accounts: welcome screen, local accounts, guest mode, recovery-code password reset, sign out, account deletion
- Onboarding questions, which can be skipped
- Home: greeting, date, progress ring, stats, week strip, sections, priorities, streaks, reminders, goals, recently completed
- Habit types and tracking:
  - build / reduce / quit habits
  - completion, amount, duration and checklist tracking
  - every schedule type: daily, selected days, weekdays/weekends, every N days, N times per week/month/year, day of month, one-time
  - start/end dates, pause/resume, archive/restore, duplicate, delete with confirmation
- Schedule changes never rewrite history
- Check-ins: complete, partial amounts (Add/Set), skip (rest day), not done, notes, occurrences with triggers, undo, correcting past days, timestamps
- Journal: day/week/month check-in, notes with search, filters, tags, weekly and monthly reflections, mood tracking with charts (can be switched off)
- Progress: filters, daily/weekly/monthly/yearly charts, comparisons, category breakdown, heatmap, per-habit analytics, achievements, reports, CSV export
- Calendar: month/week/day views, per-habit view
- Goals with linked habits (no double counting), milestones, manual progress; personal challenges
- Focus: timer, stopwatch and Pomodoro (timestamp-based, so accurate in the background), sounds, habit linking, history
- Categories (multiple per habit, colours, reorder), custom sections, manual/A–Z/reminder-time sorting
- Appearance: theme, accent colour, text size, density, chart style, home cards
- Data: full backup and restore, journal export, .ics calendar export
- On-device rule-based assistant, which can create and adjust habits after confirmation

**Implemented natively, compiled but not device-tested:** reminder notifications with Done/Snooze, per-weekday times, quiet hours, rescheduling after reboot or time-zone change, timer-finished notification, home-screen widget, app shortcuts, saving large exports to Downloads.

**Not implemented: needs services, keys or platform approval**

- Cloud accounts, email verification, cross-device sync and online password reset: need a backend (e.g. Firebase/Supabase) and its credentials.
- Google, Discord and Facebook sign-in: need OAuth client IDs and a backend.
- AI assistant (LLM): needs an AI API key and a server to keep the key secret.
- Subscriptions and payments: need a Google Play Console account and Play Billing products. This version is a free preview and charges nothing.
- Health Connect, Fitbit, Strava, live calendar sync, RescueTime, Zapier/IFTTT, webhooks: need SDKs, API keys or servers.
- Screen-time tracking: needs the Usage Access permission, which also increases Play Protect warnings.
- NFC tags, location-based reminders, image attachments, multiple languages: not built yet.
- Friends, shared challenges and leaderboards: need a backend. No fake users are shown.

See `RELEASE_CHECKLIST.md` for the Google Play steps.
