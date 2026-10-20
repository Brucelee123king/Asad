# Asadullah Notes - Windows desktop app

Offline Electron app wrapping the original Asadullah Notes MCQ application (196 tests, 11,208 questions).

## Structure
- `main.js` - Electron main process (secure window, `app://` protocol, saves user data to `%APPDATA%\Asadullah Notes\user-data.json`)
- `preload.js` - mirrors `localStorage` (accounts, scores, bookmarks, mistakes, stats, theme) into that file
- `src/index.html` - original UI and logic; `src/data.js` - original question database (unchanged)
- `src/corrections.js` - corrections overlay (see `../reports/`)
- `src/vendor/` - Tailwind, Font Awesome and fonts bundled locally (no internet needed)
- `scripts/` - `build-src.js` (split original), `audit.js`, `build-reports.js`, `smoke.js` (launches the real app and clicks through a quiz)
- `build/icon.ico` - app icon

## Build on Windows
1. Install Node.js 20+ from nodejs.org.
2. `cd asadullah-notes-desktop`
3. `npm install`
4. `npm run dist` (or `npx electron-builder --win nsis portable --x64`)
5. Output in `dist/`: `AsadullahNotes-Setup.exe` (installer, per-user, Start Menu + optional desktop shortcut) and `AsadullahNotes-Portable.exe`.

Run without packaging: `npm start`. Architecture: Windows x64. Version 1.0.0.
Alternative: the GitHub Actions workflow `.github/workflows/build-windows.yml` builds both files on a Windows runner.

## Your data
Saved in `%APPDATA%\Asadullah Notes\`. The uninstaller keeps it (`deleteAppDataOnUninstall: false`).
