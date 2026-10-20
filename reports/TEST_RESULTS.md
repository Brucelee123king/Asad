# Test results - Asadullah Notes desktop 1.0.0 (2026-10-20)

Environment: Linux container. Windows was NOT available, so the .exe files were cross-built (Electron 33 + electron-builder + wine) and never run on Windows.

## Passed (automated, real Electron app run under Xvfb on Linux, `scripts/smoke.js`)
- App opens in its own window; title "Asadullah Notes"
- All 196 tests / 11,208 questions load (counts match the original)
- Guest login, open section, select test, Start, answer, Next, submit, results screen (score 1/50 for the scripted answers)
- Corrections overlay applied (e.g. 1-50 #30 key reads "Muhammad Sohail Afridi")
- Fully offline: 0 requests outside the app, Tailwind, Font Awesome and fonts all load from the bundle
- 0 JavaScript console errors
- History/accounts/scores saved to user-data.json and restored after browser storage was wiped (counter 1 -> 2 -> 3 over three launches)
- Installer and portable files exist (~83 MB each); version info embedded; asar contains all app files
- Data integrity checks over all questions (see data-integrity-report.txt)

## Not performed / could not be performed (needs real Windows)
- Running Setup.exe, Start Menu / desktop shortcut creation, Installed Apps entry, uninstall, upgrade-keeps-data
- Running the Portable.exe
- Icon display in taskbar/Start Menu/installer on Windows
- Windows display-scaling and window maximize/restore checks
- Timer expiry auto-submit, retake, review filters, question palette: logic is unchanged original code, but not individually exercised in this run
- Performance profiling on a modest PC; memory-leak testing
- Code signing: the installer is unsigned, so Windows SmartScreen will show a warning ("More info" > "Run anyway")

## Known limitations
- Factual accuracy of all 11,208 questions was not externally verified; see MCQ_Audit_Report.html and MCQ_Manual_Review.csv
- 37 owner-supplied corrections change answers/facts and are unverified (review list)
- Resume-after-closing for an active test was not implemented (optional in the brief)
- The original in-app login is local to the device; Google/Facebook sign-in buttons were already non-functional in the original
