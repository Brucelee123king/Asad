package com.habittracker.app;

import android.app.AlarmManager;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Build;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.Calendar;

/** Schedules reminder alarms handed over by the app, shows notifications and handles their buttons. */
public final class Reminders {
    static final String CH_REM = "reminders", CH_FOCUS = "focus";
    static final String A_REMIND = "com.habittracker.app.REMIND", A_DONE = "com.habittracker.app.DONE",
            A_SNOOZE = "com.habittracker.app.SNOOZE", A_TIMER = "com.habittracker.app.TIMER";
    static final int TIMER_ID = 424242;
    private Reminders() { }

    static SharedPreferences prefs(Context c) { return c.getSharedPreferences("habitflow", Context.MODE_PRIVATE); }

    static void ensureChannels(Context c) {
        if (Build.VERSION.SDK_INT < 26) return;
        NotificationManager nm = c.getSystemService(NotificationManager.class);
        NotificationChannel r = new NotificationChannel(CH_REM, "Habit reminders", NotificationManager.IMPORTANCE_HIGH);
        r.setDescription("Reminders for your habits");
        NotificationChannel f = new NotificationChannel(CH_FOCUS, "Focus timer", NotificationManager.IMPORTANCE_HIGH);
        f.setDescription("Tells you when a focus session or break ends");
        nm.createNotificationChannel(r); nm.createNotificationChannel(f);
    }

    private static PendingIntent pi(Context c, int code, Intent i) {
        return PendingIntent.getBroadcast(c, code, i, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);
    }

    /** Wall-clock time in the current time zone, so reminders follow time-zone changes. */
    static long wallClock(JSONObject o) {
        try {
            String[] d = o.getString("date").split("-"), t = o.getString("time").split(":");
            Calendar cal = Calendar.getInstance();
            cal.set(Integer.parseInt(d[0]), Integer.parseInt(d[1]) - 1, Integer.parseInt(d[2]), Integer.parseInt(t[0]), Integer.parseInt(t[1]), 0);
            cal.set(Calendar.MILLISECOND, 0);
            return cal.getTimeInMillis();
        } catch (Exception e) { return o.optLong("ts", 0); }
    }

    static synchronized void replaceAll(Context c, String json) {
        AlarmManager am = (AlarmManager) c.getSystemService(Context.ALARM_SERVICE);
        SharedPreferences p = prefs(c);
        try {
            JSONArray old = new JSONArray(p.getString("rem", "[]"));
            for (int i = 0; i < old.length(); i++) am.cancel(pi(c, old.getJSONObject(i).getInt("id"), new Intent(c, ReminderReceiver.class).setAction(A_REMIND)));
            JSONArray arr = new JSONArray(json == null ? "[]" : json);
            long now = System.currentTimeMillis();
            for (int i = 0; i < arr.length(); i++) {
                JSONObject o = arr.getJSONObject(i);
                long ts = wallClock(o);
                if (ts <= now) continue;
                Intent it = new Intent(c, ReminderReceiver.class).setAction(A_REMIND)
                        .putExtra("id", o.getInt("id")).putExtra("title", o.optString("title")).putExtra("text", o.optString("text"))
                        .putExtra("hid", o.optString("hid")).putExtra("date", o.optString("date"));
                am.setAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, ts, pi(c, o.getInt("id"), it));
            }
            p.edit().putString("rem", arr.toString()).apply();
        } catch (Exception ignored) { }
    }

    static void rescheduleSaved(Context c) { replaceAll(c, prefs(c).getString("rem", "[]")); }

    static void show(Context c, int id, String title, String text, String hid, String date) {
        ensureChannels(c);
        NotificationManager nm = (NotificationManager) c.getSystemService(Context.NOTIFICATION_SERVICE);
        if (nm == null || !nm.areNotificationsEnabled()) return;
        Intent open = new Intent(c, MainActivity.class).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP);
        PendingIntent content = PendingIntent.getActivity(c, id, open, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);
        Notification.Builder b = Build.VERSION.SDK_INT >= 26 ? new Notification.Builder(c, CH_REM) : new Notification.Builder(c);
        b.setSmallIcon(R.drawable.ic_stat).setContentTitle(title).setContentText(text).setStyle(new Notification.BigTextStyle().bigText(text))
                .setColor(0xFF2F6BFF).setAutoCancel(true).setContentIntent(content).setCategory(Notification.CATEGORY_REMINDER);
        if (hid != null && !hid.isEmpty()) {
            Intent done = new Intent(c, ReminderReceiver.class).setAction(A_DONE).putExtra("id", id).putExtra("hid", hid).putExtra("date", date);
            Intent snooze = new Intent(c, ReminderReceiver.class).setAction(A_SNOOZE).putExtra("id", id).putExtra("hid", hid).putExtra("date", date)
                    .putExtra("title", title).putExtra("text", text);
            b.addAction(new Notification.Action.Builder(null, "Done", pi(c, id + 1, done)).build());
            b.addAction(new Notification.Action.Builder(null, "Snooze " + prefs(c).getInt("snooze", 10) + " min", pi(c, id + 2, snooze)).build());
        }
        nm.notify(id, b.build());
    }

    static void setTimer(Context c, long ts, String title, String text) {
        AlarmManager am = (AlarmManager) c.getSystemService(Context.ALARM_SERVICE);
        Intent i = new Intent(c, ReminderReceiver.class).setAction(A_TIMER).putExtra("title", title).putExtra("text", text);
        am.setAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, ts, pi(c, TIMER_ID, i));
    }
    static void cancelTimer(Context c) {
        AlarmManager am = (AlarmManager) c.getSystemService(Context.ALARM_SERVICE);
        am.cancel(pi(c, TIMER_ID, new Intent(c, ReminderReceiver.class).setAction(A_TIMER)));
    }

    /** "Done" taps from notifications are queued here and applied by the app the next time it opens. */
    static synchronized void queueDone(Context c, String hid, String date) {
        try {
            JSONArray a = new JSONArray(prefs(c).getString("actions", "[]"));
            a.put(new JSONObject().put("hid", hid).put("date", date).put("a", "done"));
            prefs(c).edit().putString("actions", a.toString()).apply();
        } catch (Exception ignored) { }
    }
    static synchronized String takeActions(Context c) {
        String s = prefs(c).getString("actions", "[]");
        prefs(c).edit().putString("actions", "[]").apply();
        return s;
    }
}
