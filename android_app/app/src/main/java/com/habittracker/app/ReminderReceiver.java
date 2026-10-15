package com.habittracker.app;

import android.app.AlarmManager;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Build;

public class ReminderReceiver extends BroadcastReceiver {
    @Override public void onReceive(Context c, Intent i) {
        String a = i.getAction(); if (a == null) return;
        int id = i.getIntExtra("id", 0);
        NotificationManager nm = (NotificationManager) c.getSystemService(Context.NOTIFICATION_SERVICE);
        switch (a) {
            case Reminders.A_REMIND:
                Reminders.show(c, id, i.getStringExtra("title"), i.getStringExtra("text"), i.getStringExtra("hid"), i.getStringExtra("date"));
                break;
            case Reminders.A_DONE:
                Reminders.queueDone(c, i.getStringExtra("hid"), i.getStringExtra("date"));
                if (nm != null) nm.cancel(id);
                break;
            case Reminders.A_SNOOZE: {
                if (nm != null) nm.cancel(id);
                long at = System.currentTimeMillis() + Reminders.prefs(c).getInt("snooze", 10) * 60000L;
                Intent again = new Intent(c, ReminderReceiver.class).setAction(Reminders.A_REMIND).putExtras(i);
                PendingIntent p = PendingIntent.getBroadcast(c, id, again, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);
                ((AlarmManager) c.getSystemService(Context.ALARM_SERVICE)).setAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, at, p);
                break;
            }
            case Reminders.A_TIMER: {
                Reminders.ensureChannels(c);
                if (nm == null || !nm.areNotificationsEnabled()) return;
                Intent open = new Intent(c, MainActivity.class).setData(android.net.Uri.parse("habitflow://focus")).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                Notification.Builder b = Build.VERSION.SDK_INT >= 26 ? new Notification.Builder(c, Reminders.CH_FOCUS) : new Notification.Builder(c);
                b.setSmallIcon(R.drawable.ic_stat).setContentTitle(i.getStringExtra("title")).setContentText(i.getStringExtra("text")).setColor(0xFF2F6BFF).setAutoCancel(true)
                        .setContentIntent(PendingIntent.getActivity(c, Reminders.TIMER_ID, open, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE));
                nm.notify(Reminders.TIMER_ID, b.build());
                break;
            }
            default:   // boot completed, app updated, time or time zone changed
                Reminders.rescheduleSaved(c);
                HabitWidget.refresh(c);
        }
    }
}
