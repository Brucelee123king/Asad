# Asadullah Notes - Android app (WebView, fully offline)

- Package ID: `com.asadullahnotes.mcq`   Version: `1.0.0` (versionCode 1)
- minSdk 24 (Android 7.0), targetSdk / compileSdk 35, portrait only
- Permissions: none (no INTERNET). No ads, no trackers.
- The whole site (all MCQs, all sections, timers, palette, scoring, review, retake, footer credit) is bundled in `app/src/main/assets/www/`.
- Tailwind is pre-compiled; Inter, Plus Jakarta Sans and Font Awesome are bundled. Nothing is loaded from the internet.

## Install (phone)
1. Copy `release/AsadullahNotes-1.0.0.apk` to the phone.
2. Open it. If Android asks, allow "Install unknown apps" for the app you opened it from.
3. Tap Install, then open "Asadullah Notes".

## Rebuild
Needs JDK 17+, Android SDK (platform 35, build-tools 35), Node 18+ (only for the web bundle).
```
cd tools && npm install            # tailwindcss 3.4.17, fontawesome 6.4.0, fontsource fonts
python3 tools/build_web.py tools   # builds app/src/main/assets/www from source/index.html
./gradlew assembleRelease          # app/build/outputs/apk/release/app-release.apk
```
Signing: create `keystore.properties` next to `gradlew` (never commit it):
```
storeFile=/path/to/asadullah-notes.jks
storePassword=...
keyAlias=asadullah
keyPassword=...
```
Without it the release APK is built unsigned. KEEP THE KEYSTORE: every future update must be signed with the same key.

## Folders
- `source/index.html` - corrected site file used for the app (the same file as `site/index.html`).
- `original/index.html` - untouched backup of the file before this work.
- `tools/` - web bundle build (`build_web.py`), icon generator, error page.
- `verify_all/` - the MCQ audit (inputs, agent answers, adjudication, patches). `corrections.json` = applied fixes.
- `qa/` - format scan, performance and quiz test scripts and reports.
- `docs/` - fixes list, test results, limitations.
