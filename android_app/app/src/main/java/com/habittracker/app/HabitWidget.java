package com.habittracker.app;

import android.app.PendingIntent;
import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.widget.RemoteViews;

import org.json.JSONArray;
import org.json.JSONObject;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

/** Home-screen widget showing today's progress, using the summary the app saves on every change. */
public class HabitWidget extends AppWidgetProvider {
    @Override public void onUpdate(Context c, AppWidgetManager m, int[] ids) { for (int id : ids) m.updateAppWidget(id, views(c)); }

    static void refresh(Context c) {
        AppWidgetManager m = AppWidgetManager.getInstance(c);
        int[] ids = m.getAppWidgetIds(new ComponentName(c, HabitWidget.class));
        for (int id : ids) m.updateAppWidget(id, views(c));
    }

    static RemoteViews views(Context c) {
        RemoteViews v = new RemoteViews(c.getPackageName(), R.layout.widget);
        String today = new SimpleDateFormat("yyyy-MM-dd", Locale.US).format(new Date());
        try {
            JSONObject o = new JSONObject(Reminders.prefs(c).getString("widget", "{}"));
            if (!today.equals(o.optString("date"))) {
                v.setTextViewText(R.id.w_pct, "–"); v.setTextViewText(R.id.w_sub, "Open HabitFlow to update today's progress"); v.setTextViewText(R.id.w_next, "");
            } else {
                int total = o.optInt("total"), done = o.optInt("done");
                v.setTextViewText(R.id.w_pct, total == 0 ? "–" : o.optInt("pct") + "%");
                v.setTextViewText(R.id.w_sub, total == 0 ? "Nothing scheduled today" : done + " of " + total + " done" + (o.optInt("streak") > 0 ? " · best streak " + o.optInt("streak") : ""));
                JSONArray n = o.optJSONArray("next"); StringBuilder sb = new StringBuilder();
                if (n != null) for (int i = 0; i < n.length(); i++) sb.append(i == 0 ? "Next: " : "\n").append(n.optString(i));
                v.setTextViewText(R.id.w_next, done == total && total > 0 ? "All done today!" : sb.toString());
            }
        } catch (Exception e) { v.setTextViewText(R.id.w_sub, "Open HabitFlow"); }
        Intent open = new Intent(c, MainActivity.class).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        v.setOnClickPendingIntent(R.id.w_root, PendingIntent.getActivity(c, 9, open, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE));
        return v;
    }
}
