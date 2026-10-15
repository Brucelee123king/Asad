package com.habittracker.app;

import android.Manifest;
import android.app.Activity;
import android.app.NotificationManager;
import android.content.ContentValues;
import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.provider.Settings;
import android.webkit.JavascriptInterface;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

public class MainActivity extends Activity {
    private WebView web;

    /** Methods the bundled pages can call through window.Android. Only local pages are loaded. */
    private class Bridge {
        @JavascriptInterface public void orient(final String mode) {
            runOnUiThread(() -> setRequestedOrientation("landscape".equals(mode)
                    ? ActivityInfo.SCREEN_ORIENTATION_SENSOR_LANDSCAPE : defaultOrientation()));
        }
        @JavascriptInterface public void setReminders(String json) { Reminders.replaceAll(MainActivity.this, json); }
        @JavascriptInterface public String notifStatus() {
            if (Build.VERSION.SDK_INT >= 33 && checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) return "denied";
            NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
            return nm != null && nm.areNotificationsEnabled() ? "granted" : "denied";
        }
        @JavascriptInterface public void requestNotifPermission() {
            runOnUiThread(() -> {
                if (Build.VERSION.SDK_INT >= 33 && checkSelfPermission(Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED
                        && !Reminders.prefs(MainActivity.this).getBoolean("asked_notif", false)) {
                    Reminders.prefs(MainActivity.this).edit().putBoolean("asked_notif", true).apply();
                    requestPermissions(new String[]{Manifest.permission.POST_NOTIFICATIONS}, 7);
                } else {   // already refused once: Android only allows changing it in system settings
                    Intent i = Build.VERSION.SDK_INT >= 26
                            ? new Intent(Settings.ACTION_APP_NOTIFICATION_SETTINGS).putExtra(Settings.EXTRA_APP_PACKAGE, getPackageName())
                            : new Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS, Uri.parse("package:" + getPackageName()));
                    try { startActivity(i); } catch (Exception e) { startActivity(new Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS, Uri.parse("package:" + getPackageName()))); }
                }
            });
        }
        @JavascriptInterface public void testNotification() { Reminders.show(MainActivity.this, 1, "HabitFlow test", "Reminders are working.", null, null); }
        @JavascriptInterface public void setSnooze(int minutes) { Reminders.prefs(MainActivity.this).edit().putInt("snooze", minutes).apply(); }
        @JavascriptInterface public void setTimerAlarm(double ts, String title, String text) { Reminders.setTimer(MainActivity.this, (long) ts, title, text); }
        @JavascriptInterface public void cancelTimerAlarm() { Reminders.cancelTimer(MainActivity.this); }
        @JavascriptInterface public String takeActions() { return Reminders.takeActions(MainActivity.this); }
        @JavascriptInterface public void updateWidget(String json) { Reminders.prefs(MainActivity.this).edit().putString("widget", json).apply(); HabitWidget.refresh(MainActivity.this); }
        @JavascriptInterface public String shareText(String title, String text, String filename, String mime) {
            if (text.length() < 150000) {
                Intent s = new Intent(Intent.ACTION_SEND).setType("text/plain").putExtra(Intent.EXTRA_SUBJECT, title).putExtra(Intent.EXTRA_TEXT, text);
                runOnUiThread(() -> startActivity(Intent.createChooser(s, title)));
                return "shared";
            }
            return saveToDownloads(filename == null ? "habitflow.txt" : filename, mime == null ? "text/plain" : mime, text);
        }
        @JavascriptInterface public String shareText(String title, String text) { return shareText(title, text, "habitflow.txt", "text/plain"); }
    }

    /** Phones stay in portrait; tablets and Chromebooks may rotate (HabitFlow has a wide layout). */
    private int defaultOrientation() {
        return getResources().getConfiguration().smallestScreenWidthDp >= 600
                ? ActivityInfo.SCREEN_ORIENTATION_UNSPECIFIED : ActivityInfo.SCREEN_ORIENTATION_PORTRAIT;
    }

    private String saveToDownloads(String name, String mime, String text) {
        try {
            byte[] data = text.getBytes(StandardCharsets.UTF_8);
            if (Build.VERSION.SDK_INT >= 29) {
                ContentValues v = new ContentValues();
                v.put(MediaStore.Downloads.DISPLAY_NAME, name); v.put(MediaStore.Downloads.MIME_TYPE, mime);
                v.put(MediaStore.Downloads.RELATIVE_PATH, Environment.DIRECTORY_DOWNLOADS);
                Uri uri = getContentResolver().insert(MediaStore.Downloads.EXTERNAL_CONTENT_URI, v);
                try (OutputStream o = getContentResolver().openOutputStream(uri)) { o.write(data); }
                return "saved:Downloads/" + name;
            }
            File dir = getExternalFilesDir(null); File f = new File(dir, name);
            try (FileOutputStream o = new FileOutputStream(f)) { o.write(data); }
            return "saved:" + f.getAbsolutePath();
        } catch (Exception e) { return "error:" + e.getMessage(); }
    }

    @Override protected void onCreate(Bundle b) {
        super.onCreate(b);
        setRequestedOrientation(defaultOrientation());
        Reminders.ensureChannels(this);
        web = new WebView(this);
        web.setBackgroundColor(Color.parseColor("#0D0F12"));
        setContentView(web);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setAllowFileAccess(true);
        s.setAllowContentAccess(false);
        s.setSupportZoom(true); s.setBuiltInZoomControls(true); s.setDisplayZoomControls(false);
        web.addJavascriptInterface(new Bridge(), "Android");
        web.setWebViewClient(new WebViewClient() {
            @Override public boolean shouldOverrideUrlLoading(WebView v, WebResourceRequest r) {
                Uri u = r.getUrl();
                if ("file".equals(u.getScheme()) && u.getPath() != null && u.getPath().startsWith("/android_asset/")) return false;
                try { startActivity(new Intent(Intent.ACTION_VIEW, u)); } catch (Exception ignored) { }
                return true;
            }
        });
        if (b == null) web.loadUrl(startUrl(getIntent()));
        else web.restoreState(b);
    }

    /** App shortcuts open habitflow://add, habitflow://focus or habitflow://journal */
    private String startUrl(Intent i) {
        Uri d = i == null ? null : i.getData();
        if (d != null && "habitflow".equals(d.getScheme()) && d.getHost() != null && d.getHost().matches("add|focus|journal|progress"))
            return "file:///android_asset/app.html#" + d.getHost();
        return "file:///android_asset/index.html";
    }
    @Override protected void onNewIntent(Intent i) { super.onNewIntent(i); setIntent(i); if (i.getData() != null) web.loadUrl(startUrl(i)); }
    @Override protected void onSaveInstanceState(Bundle o) { super.onSaveInstanceState(o); web.saveState(o); }
    @Override protected void onPause() { super.onPause(); web.onPause(); }
    @Override protected void onResume() { super.onResume(); web.onResume(); }
    /** Back: let HabitFlow close a sheet or go back a screen first; other pages use WebView history. */
    @Override public void onBackPressed() {
        web.evaluateJavascript("(window.App&&App.handleBack)?String(App.handleBack()):'none'", r -> {
            if ("\"true\"".equals(r)) return;
            if ("\"none\"".equals(r) && web.canGoBack()) { web.goBack(); return; }
            finish();
        });
    }
}
