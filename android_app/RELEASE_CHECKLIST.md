# Google Play release checklist: HabitFlow 2.1.0

Status as of this build. ✅ = done and verified, ⚠️ = done but needs your check, ❌ = still required.

## Build & identity
- ✅ Package ID: `com.habittracker.app`. It **cannot change after the first Play upload**. If you want e.g. `com.yourname.habitflow`, change `applicationId` in `app/build.gradle` *before* uploading. Changing it makes it a new app on phones too.
- ✅ Version: `versionName 2.1.0`, `versionCode 4`. Increase `versionCode` for every upload.
- ✅ Target SDK 35 (Android 15), min SDK 24 (Android 7.0). Google Play currently requires a recent target SDK. Check the current requirement in Play Console when you upload.
- ✅ Signed release build: `app/build/outputs/bundle/release/app-release.aab` (upload this to Play) and `app-release.apk`. Both are signed with the HabitFlow key (SHA-256 `2d:e5:68:5c:…:3a:ba:83`).
- ❌ **Back up the signing key.** It lives only in this build environment. Without it you cannot ship updates to people who installed this APK. With Play App Signing, Google holds the app-signing key and this becomes your upload key.
- ✅ Launcher icon: adaptive icon with a themed (monochrome) layer, plus a 512×512 store icon (`store_icon_512.png`).
- ⚠️ Lint: 0 errors. 10 warnings, all reviewed: attributes ignored on older Android versions, JavaScript required for the bundled UI, and orientation (phones are portrait, tablets rotate).

## Permissions (all justified, nothing sensitive)
- `POST_NOTIFICATIONS`: habit reminders and timer alerts. Asked only when the user turns on a reminder.
- `RECEIVE_BOOT_COMPLETED`: re-schedule reminders after a restart.
- `VIBRATE`: completion feedback and the timer chime.
- `INTERNET`: only the classic boards load a Google Font. HabitFlow itself works fully offline. You could remove this permission if you drop the web font.

## Store listing (Play Console)
- ❌ Google Play developer account ($25 one-time) and identity verification.
- ❌ **Privacy policy URL.** Play requires a public web page. The in-app text (Settings › Privacy policy) can be published as-is, for example on GitHub Pages.
- ❌ **Data safety form.** Truthful answers for this version: no data collected or shared, data stored on device, users can delete data in the app.
- ❌ Content rating questionnaire (expected: Everyone), target audience, ads declaration (no ads).
- ❌ Screenshots (at least 2 phone screenshots; the test screenshots can be a starting point), feature graphic 1024×500, short and full description.
- ❌ Testing track. New personal developer accounts must run a closed test (currently at least 12 testers for 14 days) before production. Check current rules in Play Console.

## Before you call it production-ready
- ❌ **Test on real phones.** Notifications (Done/Snooze), boot rescheduling, the widget and shortcuts compile and are wired up, but have not been run on a device. Test on at least one Android 13+ phone and one older phone.
- ❌ Battery-optimisation behaviour on Samsung, Xiaomi and similar phones (reminders may be delayed when the app is restricted).
- ⚠️ Paid plans are not on sale. The app says so. Do not advertise subscriptions in the listing until Play Billing is implemented.
- ⚠️ Accounts are local to the phone (no cloud sync). Say this clearly in the description.
