/* Progress: overview analytics, calendar, goals, per-habit list */
Screens.progress = (() => {
  const E = s => UI.esc(s);
  function rangeFor(kind, off, t, ws) {
    if (kind === 'week') { const back = (Core.dow(t) - ws + 7) % 7, from = Core.addDays(Core.addDays(t, -back), 7 * off); return [from, Core.addDays(from, 6)]; }
    if (kind === 'month') { const p = t.split('-').map(Number), d = new Date(p[0], p[1] - 1 + off, 1); return [Core.ymd(d), Core.ymd(new Date(d.getFullYear(), d.getMonth() + 1, 0))]; }
    const y = +t.slice(0, 4) + off; return [y + '-01-01', y + '-12-31'];
  }
  function render() {
    const seg = App.ui.seg.progress || 'overview';
    return `<div class="top"><h1>Progress</h1><button class="ib" data-act="go" data-s="assistant" aria-label="Insights assistant">${UI.icon('spark')}</button></div>
      ${UI.seg('progress', [['overview', 'Overview'], ['calendar', 'Calendar'], ['goals', 'Goals'], ['habits', 'Habits']], seg)}<div class="stack mt">${seg === 'calendar' ? calendar() : seg === 'goals' ? Screens.goals.body() : seg === 'habits' ? habits() : overview()}</div>`;
  }
  function filters() {
    const D = App.D, f = App.ui.f;
    return `<div class="row"><select class="inp" data-change="pcat" aria-label="Filter by category"><option value="">All categories</option>${D.cats.map(c => `<option value="${c.id}" ${f.pcat === c.id ? 'selected' : ''}>${E(c.icon + ' ' + c.name)}</option>`).join('')}</select>
      <select class="inp" data-change="phid" aria-label="Filter by habit"><option value="">All habits</option>${D.habits.map(h => `<option value="${h.id}" ${f.phid === h.id ? 'selected' : ''}>${E(h.icon + ' ' + h.name)}${h.archived ? ' (archived)' : ''}</option>`).join('')}</select></div>`;
  }
  function overview() {
    const D = App.D, t = App.tdy(), s = D.settings, f = App.ui.f, kind = App.ui.seg.prange || 'week', off = f.poff || 0, [from, to] = rangeFor(kind, off, t, s.weekStart);
    const hs = HC.filteredHabits({ cat: f.pcat, hid: f.phid, arch: !!f.phid });
    if (!D.habits.length) return `<div class="card">${UI.empty('\u{1F4CA}', 'No data yet', 'Your statistics appear here once you start checking in habits.', '<button class="btn" data-act="go" data-s="library">Add a habit</button>')}</div>`;
    const pr = Core.periodRate(D, from, to, t, hs), per = hs.map(h => ({ h, r: Core.rate(D, h, from, to, t) })).filter(x => x.r.total);
    let skipped = 0, missed = 0; per.forEach(x => { skipped += x.r.skipped; missed += x.r.missed; });
    const avg = per.length ? Math.round(per.reduce((a, x) => a + x.r.pct, 0) / per.length) : 0;
    let cur = 0, lng = 0; hs.forEach(h => { cur = Math.max(cur, Core.currentStreak(D, h, t)); lng = Math.max(lng, Core.longestStreak(D, h, t)); });
    const label = kind === 'week' ? UI.fmtDate(from, s.dateFmt) + ' – ' + UI.fmtDate(to, s.dateFmt) : kind === 'month' ? UI.MFULL[+from.slice(5, 7) - 1] + ' ' + from.slice(0, 4) : from.slice(0, 4);
    let h = `${UI.seg('prange', [['week', 'Week'], ['month', 'Month'], ['year', 'Year']], kind)}
      <div class="row"><button class="ib" data-act="poff" data-v="-1" aria-label="Previous period">${UI.icon('left')}</button><b class="grow" style="text-align:center">${label}</b><button class="ib" data-act="poff" data-v="1" aria-label="Next period" ${off >= 0 ? 'disabled' : ''}>${UI.icon('right')}</button></div>${filters()}
      <div class="card"><div class="row" style="gap:18px">${UI.ring(pr.pct, 104, 11, `<b>${pr.pct}%</b><span>completion</span>`)}<div class="stats grow" style="grid-template-columns:repeat(2,1fr)">
      <div class="stat"><b>${pr.done}</b><span>Check-ins</span></div><div class="stat"><b>${avg}%</b><span>Avg consistency</span></div><div class="stat"><b>${skipped}</b><span>Skipped</span></div><div class="stat"><b>${missed}</b><span>Missed</span></div></div></div>
      <div class="stats mt"><div class="stat"><b>${Core.live(D).length}</b><span>Active habits</span></div><div class="stat"><b>${D.habits.filter(x => x.archived).length}</b><span>Archived</span></div><div class="stat"><b>${cur}</b><span>Best current streak</span></div><div class="stat"><b>${lng}</b><span>Longest streak</span></div></div></div>`;
    // daily / monthly chart
    let data;
    if (kind === 'year') data = UI.MN.map((mn, i) => { const a = from.slice(0, 4) + '-' + Core.pad(i + 1) + '-01', b = from.slice(0, 4) + '-' + Core.pad(i + 1) + '-' + Core.pad(Core.dim(+from.slice(0, 4), i + 1)); if (a > t) return { l: mn.slice(0, 1), v: null }; const r = Core.periodRate(D, a, b, t, hs); return { l: mn.slice(0, 1), v: r.total ? r.pct : null, t: mn + ': ' + r.pct + '% (' + r.done + '/' + r.total + ')' }; });
    else data = Core.range(from, to).map(d => { if (d > t) return { l: kind === 'week' ? UI.DN[Core.dow(d)].slice(0, 2) : +d.slice(8), v: null }; const c = Core.dayCompletion(D, d, t, hs); return { l: kind === 'week' ? UI.DN[Core.dow(d)].slice(0, 2) : +d.slice(8), v: c.total ? c.pct : null, t: UI.fmtDate(d, s.dateFmt) + ': ' + c.pct + '% (' + c.done + '/' + c.total + ')' }; });
    h += `<div class="card"><h2>${kind === 'year' ? 'Monthly' : 'Daily'} completion</h2>${UI.bars(data, { max: 100, suf: '%', label: (kind === 'year' ? 'Monthly' : 'Daily') + ' completion rate' })}<p class="hint">Share of scheduled habits completed. Skipped days are left out.</p></div>`;
    // comparisons
    const wk = [], mo = []; for (let i = 7; i >= 0; i--) { const [a, b] = rangeFor('week', -i, to > t ? t : to, s.weekStart); const r = Core.periodRate(D, a, b, t, hs); wk.push({ l: UI.fmtDate(a, s.dateFmt).slice(0, 6), v: r.total ? r.pct : null, t: 'Week of ' + UI.fmtDate(a, s.dateFmt) + ': ' + r.pct + '%' }); }
    for (let i = 5; i >= 0; i--) { const [a, b] = rangeFor('month', -i, to > t ? t : to, s.weekStart); const r = Core.periodRate(D, a, b, t, hs); mo.push(r.total ? r.pct : null); }
    const moL = []; for (let i = 5; i >= 0; i--) { const [a] = rangeFor('month', -i, to > t ? t : to, s.weekStart); moL.push(UI.MN[+a.slice(5, 7) - 1]); }
    h += `<div class="wide2 stack"><div class="card"><h2>Weekly comparison</h2>${UI.bars(wk, { max: 100, suf: '%', label: 'Completion rate for the last 8 weeks' })}</div>
      <div class="card"><h2>Monthly comparison</h2>${UI.line([{ name: 'Completion', color: 'var(--ac)', vals: mo }], moL, { max: 100, suf: '%', label: 'Completion rate for the last 6 months' })}</div></div>`;
    // categories
    const cats = D.cats.map(c => { const ch = hs.filter(x => Core.habitCats(x).indexOf(c.id) >= 0); const r = Core.periodRate(D, from, to, t, ch); return { c, r, n: ch.length }; }).filter(x => x.n && x.r.total);
    if (cats.length) h += `<div class="card"><h2>By category</h2>${cats.map(x => `<div style="margin-bottom:12px"><div class="row small"><span class="grow">${E(x.c.icon + ' ' + x.c.name)}</span><b>${x.r.pct}%</b><span class="muted">${x.r.done}/${x.r.total}</span></div>${UI.pbar(x.r.pct, x.c.color)}</div>`).join('')}</div>`;
    // heatmap
    const ws = s.weekStart, end = t, back = (Core.dow(end) - ws + 7) % 7, start = Core.addDays(Core.addDays(end, -back), -7 * 19);
    h += `<div class="card"><h2>Consistency heatmap (20 weeks)</h2>${UI.heat(Core.range(start, Core.addDays(Core.addDays(end, -back), 6)).map(d => { if (d > t) return { d, pct: null }; const c = Core.dayCompletion(D, d, t, hs); return { d, pct: c.total ? c.pct : null }; }), 'Daily completion heatmap for the last 20 weeks')}</div>`;
    // per habit
    h += `<div class="card"><h2>Habit performance</h2>${per.length ? `<div class="list">${per.sort((a, b) => b.r.pct - a.r.pct).map(x => `<button class="li" data-act="hopen" data-h="${x.h.id}"><span class="bubble">${E(x.h.icon)}</span><span class="grow"><span class="row small"><span class="grow t ell">${E(x.h.name)}</span><b>${x.r.pct}%</b></span>${UI.pbar(x.r.pct, x.h.color)}<span class="s">${x.r.done}/${x.r.total} · 🔥 ${Core.currentStreak(D, x.h, t)} · best ${Core.longestStreak(D, x.h, t)}</span></span></button>`).join('')}</div>` : '<p class="muted small">Nothing scheduled in this period.</p>'}</div>`;
    // numbers & time
    const nums = hs.filter(x => Core.goalKind(x) !== 'check').map(x => { let v = 0; Core.range(from, to > t ? t : to).forEach(d => v += (Core.getEntry(D, x, d) || {}).v || 0); return { x, v }; }).filter(o => o.v);
    const focusSecs = D.focus.filter(fs => fs.date >= from && fs.date <= to && (!f.phid || fs.hid === f.phid)).reduce((a, fs) => a + fs.secs, 0);
    const gs = Core.goalStats(D, t);
    h += `<div class="card"><h2>Amounts, time & goals</h2><ul class="tl">${nums.map(o => `<li><span>${E(o.x.icon)}</span><span class="grow">${E(o.x.name)}</span><b>${Core.goalKind(o.x) === 'time' ? UI.fmtDur(o.v * 60) : Math.round(o.v * 100) / 100 + ' ' + E(o.x.goal.unit || '')}</b></li>`).join('')}
      <li><span>⏱️</span><span class="grow">Focus time</span><b>${UI.fmtDur(focusSecs)}</b></li><li><span>\u{1F3AF}</span><span class="grow">Days a numeric goal was reached (all time)</span><b>${gs.met}/${gs.total} · ${gs.pct}%</b></li>
      <li><span>\u{1F3C1}</span><span class="grow">Goals reached</span><b>${D.goals.filter(g => Core.goalProgress(D, g, t).done).length}/${D.goals.length}</b></li></ul></div>`;
    h += `<div class="card"><h2>${UI.icon('spark', 16)} This week in words</h2>${Core.weeklyInsight(D, t).map(l => `<p class="small" style="margin-bottom:6px">${E(l)}</p>`).join('')}<p class="hint">Calculated on your device from your own records.</p></div>`;
    const ach = Core.achievements(Core.summary(D, t));
    h += `<div class="card"><h2>Achievements · ${ach.filter(a => a.ok).length}/${ach.length}</h2><div class="ach">${ach.map(a => `<div class="${a.ok ? '' : 'lock'}" title="${E(a.d)}"><span>${a.i}</span><b>${E(a.t)}</b>${E(a.d)}</div>`).join('')}</div></div>`;
    h += `<div class="card"><h2>Reports</h2><div class="chips"><button class="chip" data-act="rep" data-v="day">Daily summary</button><button class="chip" data-act="rep" data-v="week">Weekly report</button><button class="chip" data-act="rep" data-v="month">Monthly report</button><button class="chip" data-act="rep" data-v="year">Yearly summary</button><button class="chip" data-act="rep" data-v="goals">Goal report</button><button class="chip" data-act="csv">${UI.icon('share', 14)} Export CSV</button></div></div>
      <details class="card flat"><summary class="b">How these numbers are calculated</summary><ul class="small" style="margin:10px 0 0 18px;line-height:1.6"><li>Only days a habit is scheduled count. A Mon/Wed/Fri habit is never judged on other days.</li><li><b>Skipped</b> days (rest days) and <b>paused</b> days are left out: they neither count nor break a streak.</li><li>A day is <b>missed</b> only after it ends without a check-in, or when you mark it "not done". Today is never counted as missed.</li><li>"N times per week/month" habits are judged per period, once the period ends.</li><li>For habits you want to reduce or quit, a successful day must be recorded; an occurrence over the limit is a setback.</li><li>Every number comes from records saved on this device.</li></ul></details>`;
    return h;
  }
  function calendar() {
    const D = App.D, t = App.tdy(), s = D.settings, f = App.ui.f, month = f.cmonth || t.slice(0, 7), y = +month.slice(0, 4), m = +month.slice(5, 7), sel = f.cday || t, hid = f.chid || '', h1 = hid && App.habit(hid), v = App.ui.seg.cview || 'month';
    let h = `${UI.seg('cview', [['month', 'Month'], ['week', 'Week'], ['day', 'Day']], v)}<select class="inp" data-change="chid" aria-label="Habit"><option value="">All habits</option>${D.habits.map(x => `<option value="${x.id}" ${hid === x.id ? 'selected' : ''}>${E(x.icon + ' ' + x.name)}</option>`).join('')}</select>`;
    if (v === 'month') {
      h += `<div class="card"><div class="row" style="margin-bottom:10px"><button class="ib" data-act="cmon" data-v="-1" aria-label="Previous month">${UI.icon('left')}</button><b class="grow" style="text-align:center">${UI.MFULL[m - 1]} ${y}</b><button class="ib" data-act="cmon" data-v="1" aria-label="Next month">${UI.icon('right')}</button></div>`;
      const first = month + '-01', lead = (Core.dow(first) - s.weekStart + 7) % 7; h += '<div class="cal">' + [0, 1, 2, 3, 4, 5, 6].map(i => `<div class="h">${UI.DN[(i + s.weekStart) % 7].slice(0, 2)}</div>`).join(''); for (let i = 0; i < lead; i++) h += '<div></div>';
      for (let d = 1; d <= Core.dim(y, m); d++) { const ds = month + '-' + Core.pad(d); let cls = '', style = '';
        if (h1) { const st = Core.status(D, h1, ds, t); cls = st === 'off' ? 'out' : st === 'failed' ? 'st-missed' : 'st-' + st; }
        else { const c = Core.dayCompletion(D, ds, t); if (c.total && ds <= t) style = `background:color-mix(in srgb,var(--ac) ${12 + c.pct * .8}%,var(--sf2));${c.pct > 60 ? 'color:#fff' : ''}`; }
        h += `<button class="c ${cls} ${ds === t ? 'today' : ''} ${ds === sel ? 'sel' : ''}" style="${ds === sel ? '' : style}" data-act="cday" data-d="${ds}">${d}</button>`; }
      h += '</div></div>';
    } else if (v === 'week') {
      const days = HC.weekDays(sel);
      h += `<div class="row"><button class="ib" data-act="cwk" data-v="-7" aria-label="Previous week">${UI.icon('left')}</button><b class="grow" style="text-align:center">${UI.fmtDate(days[0], s.dateFmt)} – ${UI.fmtDate(days[6], s.dateFmt)}</b><button class="ib" data-act="cwk" data-v="7" aria-label="Next week">${UI.icon('right')}</button></div>
        <div class="card"><div class="list">${days.map(d => { const c = Core.dayCompletion(D, d, t, h1 ? [h1] : null); return `<button class="li" data-act="cday" data-d="${d}"><span style="width:52px" class="small b">${UI.DN[Core.dow(d)]} ${+d.slice(8)}</span><span class="grow">${c.total ? UI.pbar(d > t ? 0 : c.pct) : '<span class="muted small">Nothing scheduled</span>'}</span><span class="small muted" style="width:70px;text-align:right">${c.total ? (d > t ? c.total + ' planned' : c.done + '/' + c.total) : ''}</span></button>`; }).join('')}</div></div>`;
    }
    // selected day detail
    const list = (h1 ? [h1] : D.habits.filter(x => !x.archived)).map(x => ({ x, st: Core.status(D, x, sel, t) })).filter(o => o.st !== 'off');
    h += `<div class="card"><h2>${UI.fmtDate(sel, s.dateFmt, true)}</h2>${list.length ? `<div class="list">${list.map(o => `<button class="li" data-act="hmore" data-h="${o.x.id}" data-d="${sel}"><span class="bubble">${E(o.x.icon)}</span><span class="grow t">${E(o.x.name)}</span>${UI.badge(o.st)}</button>`).join('')}</div>${sel <= t ? '<p class="hint mt">Tap a habit to correct this day.</p>' : ''}` : '<p class="muted small">Nothing scheduled on this day.</p>'}</div>`;
    // upcoming
    const up = []; for (let i = 1; i <= 7; i++) { const d = Core.addDays(t, i), n = Core.live(D).filter(x => Core.isScheduled(x, d) && !Core.isFlex(x, d)).length; up.push(`<li><span style="width:90px">${UI.DN[Core.dow(d)]} ${+d.slice(8)}</span><span class="grow muted">${n} habit${n === 1 ? '' : 's'} scheduled</span></li>`); }
    h += `<div class="card"><h2>Upcoming week</h2><ul class="tl">${up.join('')}</ul></div>`;
    return h;
  }
  function habits() {
    const D = App.D, t = App.tdy(), f = App.ui.f; let hs = f.harch ? D.habits.filter(x => x.archived) : Core.live(D);
    if (f.hq) { const q = f.hq.toLowerCase(); hs = hs.filter(x => (x.name + ' ' + (x.desc || '')).toLowerCase().indexOf(q) >= 0); }
    if (f.hcat2) hs = hs.filter(x => Core.habitCats(x).indexOf(f.hcat2) >= 0); if (f.hpart) hs = hs.filter(x => (x.part || 'anytime') === f.hpart); if (f.hfreq) hs = hs.filter(x => (x.sched.kind === 'weekly' ? 'weekly' : x.sched.kind) === f.hfreq);
    hs = HC.sortHabits(hs, D.settings.sort);
    return `<input class="inp" type="search" placeholder="Search habits" value="${E(f.hq || '')}" data-input="hq" aria-label="Search habits"><div class="row"><select class="inp" data-change="hcat2" aria-label="Category"><option value="">All categories</option>${D.cats.map(c => `<option value="${c.id}" ${f.hcat2 === c.id ? 'selected' : ''}>${E(c.name)}</option>`).join('')}</select>
      <select class="inp" data-change="hpart" aria-label="Time of day"><option value="">Any time</option>${D.sections.map(c => `<option value="${c.id}" ${f.hpart === c.id ? 'selected' : ''}>${E(c.name)}</option>`).join('')}</select></div>
      <div class="row"><select class="inp" data-change="hfreq" aria-label="Schedule"><option value="">Any schedule</option>${[['daily', 'Every day'], ['weekly', 'Days of week'], ['interval', 'Interval'], ['times', 'Times per period'], ['monthly', 'Monthly'], ['once', 'One time']].map(o => `<option value="${o[0]}" ${f.hfreq === o[0] ? 'selected' : ''}>${o[1]}</option>`).join('')}</select>
      <select class="inp" data-change="sort" aria-label="Sort"><option value="manual">Manual order</option><option value="alpha" ${D.settings.sort === 'alpha' ? 'selected' : ''}>A–Z</option><option value="time" ${D.settings.sort === 'time' ? 'selected' : ''}>Reminder time</option></select></div>
      <div class="chips"><button class="chip ${!f.harch ? 'on' : ''}" data-act="harch" data-v="">Active (${Core.live(D).length})</button><button class="chip ${f.harch ? 'on' : ''}" data-act="harch" data-v="1">Archived (${D.habits.filter(x => x.archived).length})</button><button class="chip" data-act="go" data-s="order">${UI.icon('sort', 14)} Reorder</button></div>
      <div class="card">${hs.length ? `<div class="list">${hs.map(x => { const r = Core.rate(D, x, Core.addDays(t, -29), t, t); return `<button class="li" data-act="hopen" data-h="${x.id}"><span class="bubble" style="background:color-mix(in srgb,${x.color} 18%,transparent)">${E(x.icon)}</span><span class="grow"><span class="t">${E(x.name)}</span><span class="s" style="display:block">${E(HC.schedText(x, t))} · ${r.pct}% (30 days) · 🔥 ${Core.currentStreak(D, x, t)}${Core.isPaused(x, t) ? ' · paused' : ''}</span></span>${UI.icon('right', 18)}</button>`; }).join('')}</div>` : UI.empty('\u{1F5C2}️', f.harch ? 'No archived habits' : 'No habits match', f.harch ? 'Archived habits keep their history and appear here.' : 'Change the filters or add a habit.')}</div>`;
  }
  function report(kind) {
    const D = App.D, t = App.tdy(), s = D.settings; let from, to, title;
    if (kind === 'day') { from = to = t; title = 'Daily summary · ' + UI.fmtDate(t, s.dateFmt, true); }
    else if (kind === 'goals') { const lines = ['HabitFlow goal report · ' + UI.fmtDate(t, s.dateFmt), '']; D.goals.forEach(g => { const p = Core.goalProgress(D, g, t); lines.push((p.done ? '✓ ' : '• ') + g.name + ': ' + p.sum + '/' + p.target + ' ' + (g.unit || '') + ' (' + p.pct + '%)' + (p.done ? '' : ', ' + p.daysLeft + ' days left')); }); if (!D.goals.length) lines.push('No goals yet.'); return lines.join('\n'); }
    else { [from, to] = rangeFor(kind, 0, t, s.weekStart); title = (kind === 'week' ? 'Weekly report' : kind === 'month' ? 'Monthly report' : 'Yearly summary') + ' · ' + UI.fmtDate(from, s.dateFmt) + ' – ' + UI.fmtDate(to > t ? t : to, s.dateFmt); }
    const pr = Core.periodRate(D, from, to, t), lines = ['HabitFlow ' + title, '', 'Completion: ' + pr.pct + '% (' + pr.done + ' of ' + pr.total + ' scheduled check-ins)', ''];
    Core.live(D).forEach(h => { const r = Core.rate(D, h, from, to, t); if (!r.total) return; lines.push('• ' + h.name + ': ' + r.pct + '% (' + r.done + '/' + r.total + '), streak ' + Core.currentStreak(D, h, t)); });
    const fsec = D.focus.filter(x => x.date >= from && x.date <= to).reduce((a, x) => a + x.secs, 0); lines.push('', 'Focus time: ' + UI.fmtDur(fsec));
    if (kind === 'week') lines.push('', ...Core.weeklyInsight(D, t)); return lines.join('\n');
  }
  return {
    render, rangeFor, report,
    acts: {
      poff: t => { App.ui.f.poff = Math.min(0, (App.ui.f.poff || 0) + +t.dataset.v); App.render(); },
      seg: t => { if (t.dataset.seg === 'prange') App.ui.f.poff = 0; App.ui.seg[t.dataset.seg] = t.dataset.v; App.render(); },
      cmon: t => { const cur = App.ui.f.cmonth || App.tdy().slice(0, 7), p = cur.split('-').map(Number); App.ui.f.cmonth = Core.ymd(new Date(p[0], p[1] - 1 + +t.dataset.v, 1)).slice(0, 7); App.render(); },
      cwk: t => { App.ui.f.cday = Core.addDays(App.ui.f.cday || App.tdy(), +t.dataset.v); App.render(); },
      cday: t => { App.ui.f.cday = t.dataset.d; App.ui.f.cmonth = t.dataset.d.slice(0, 7); App.render(); },
      harch: t => { App.ui.f.harch = t.dataset.v; App.render(); },
      rep: t => { const txt = report(t.dataset.v); UI.sheet(`<h3>Report</h3><pre class="small" style="white-space:pre-wrap;font-family:inherit;background:var(--sf2);padding:12px;border-radius:12px;max-height:50vh;overflow:auto">${E(txt)}</pre><button class="btn full mt" id="rs">${UI.icon('share', 18)} Share</button>`, sh => sh.querySelector('#rs').onclick = () => App.share('HabitFlow report', txt, 'habitflow-report.txt')); },
      csv: () => App.share('HabitFlow export', Core.csv(App.D), 'habitflow-records.csv', 'text/csv'),
      cdel: t => Screens.goals.acts.cdel(t)
    },
    inputs: { hq: t => { App.ui.f.hq = t.value; clearTimeout(Screens.progress._qt); Screens.progress._qt = setTimeout(() => { App.render(); const n = document.querySelector('[data-input=hq]'); if (n) { n.focus(); n.setSelectionRange(n.value.length, n.value.length); } }, 250); } },
    changes: {
      pcat: t => { App.ui.f.pcat = t.value; App.render(); }, phid: t => { App.ui.f.phid = t.value; App.render(); }, chid: t => { App.ui.f.chid = t.value; App.render(); },
      hcat2: t => { App.ui.f.hcat2 = t.value; App.render(); }, hpart: t => { App.ui.f.hpart = t.value; App.render(); }, hfreq: t => { App.ui.f.hfreq = t.value; App.render(); },
      sort: t => App.act(() => { App.D.settings.sort = t.value; })
    }
  };
})();

/* Goals & challenges */
Screens.goals = (() => {
  const E = s => UI.esc(s);
  function body() {
    const D = App.D, t = App.tdy();
    let h = `<div class="row"><button class="btn grow" data-act="go" data-s="goalForm">${UI.icon('plus', 18)} New goal</button><button class="btn sec grow" data-act="go" data-s="challengeForm">${UI.icon('flame', 18)} New challenge</button></div>`;
    if (!D.goals.length) h += `<div class="card flat">${UI.empty('\u{1F3AF}', 'No goals yet', 'Set a target like "Read 300 pages this month" and link the habits that count toward it.')}</div>`;
    else h += `<div class="card"><h2>Goals</h2><div class="list">${D.goals.map(g => { const p = Core.goalProgress(D, g, t); return `<button class="li" data-act="go" data-s="goal" data-id="${g.id}"><span class="bubble">${E(g.icon || '\u{1F3AF}')}</span><span class="grow"><span class="row small"><span class="t grow ell">${E(g.name)}</span><b>${p.pct}%</b></span>${UI.pbar(p.pct, g.color)}<span class="s">${p.sum}/${p.target} ${E(g.unit || '')} · ${p.done ? 'Reached \u{1F389}' : p.daysLeft + ' days left'} · ${E({ daily: 'Today', weekly: 'This week', monthly: 'This month', yearly: 'This year', custom: 'Until ' + UI.fmtDate(g.due || t, D.settings.dateFmt) }[g.period])}</span></span></button>`; }).join('')}</div></div>`;
    if (D.challenges.length) h += `<div class="card"><h2>Personal challenges</h2><div class="list">${D.challenges.map(c => { const p = Core.challengeProgress(D, c, t); return `<div class="li"><span class="bubble">${p.habit ? E(p.habit.icon) : '\u{1F3C1}'}</span><span class="grow"><span class="t">${E(c.name)}</span>${UI.pbar(p.pct)}<span class="s">${p.done}/${p.days} days · ${p.finished ? (p.won ? 'Completed \u{1F389}' : 'Ended') : 'until ' + UI.fmtDate(p.end, D.settings.dateFmt)}</span></span><button class="more" data-act="cdel" data-id="${c.id}" aria-label="Leave challenge">${UI.icon('x', 18)}</button></div>`; }).join('')}</div><p class="hint mt">Challenges are personal and private. Friends and public challenges need an online service that is not set up yet.</p></div>`;
    return h;
  }
  return {
    body,
    render: () => `<div class="top"><button class="ib" data-act="back" aria-label="Back">${UI.icon('left')}</button><h1 class="t2">Goals</h1></div><div class="stack">${body()}</div>`,
    acts: { cdel: async t => { if (await UI.confirm('Leave this challenge?', 'Your habit records are kept; only the challenge is removed.', 'Leave', true)) App.act(() => { App.D.challenges = App.D.challenges.filter(c => c.id !== t.dataset.id); }, 'Challenge removed.'); } }
  };
})();
Screens.goal = (() => {
  const E = s => UI.esc(s);
  return {
    render(p) {
      const D = App.D, g = D.goals.find(x => x.id === p.id), t = App.tdy(); if (!g) return UI.empty('\u{1F50E}', 'Goal not found', '');
      const pr = Core.goalProgress(D, g, t), links = (g.habitIds || []).map(id => App.habit(id)).filter(Boolean);
      const recent = Core.range(Core.addDays(t, -6), t).map(d => { let v = 0; links.forEach(h => { const e = Core.getEntry(D, h, d); if (!e) return; v += Core.goalKind(h) === 'check' ? (e.st === 'done' ? 1 : 0) : (e.v || 0); }); (g.log || []).forEach(l => { if (l.date === d) v += +l.v; }); return { l: UI.DN[Core.dow(d)].slice(0, 2), v: d >= pr.from && d <= pr.to ? v : 0 }; });
      return `<div class="top"><button class="ib" data-act="back" aria-label="Back">${UI.icon('left')}</button><h1 class="t2">${E(g.name)}</h1><button class="ib" data-act="go" data-s="goalForm" data-id="${g.id}" aria-label="Edit goal">${UI.icon('edit')}</button></div><div class="stack">
        <div class="card row" style="gap:18px">${UI.ring(pr.pct, 110, 11, `<b>${pr.pct}%</b><span>${pr.done ? 'reached' : 'complete'}</span>`, g.color)}<div class="grow"><div class="stats" style="grid-template-columns:1fr 1fr"><div class="stat"><b>${pr.sum}</b><span>of ${pr.target} ${E(g.unit || '')}</span></div><div class="stat"><b>${pr.remaining}</b><span>remaining</span></div><div class="stat"><b>${pr.daysLeft}</b><span>days left</span></div><div class="stat"><b>${UI.fmtDate(pr.to, D.settings.dateFmt).replace(/, \d{4}$/, '')}</b><span>ends</span></div></div></div></div>
        ${g.desc ? `<p class="small muted">${E(g.desc)}</p>` : ''}
        <div class="card"><h2>Last 7 days</h2>${UI.bars(recent, { color: g.color, label: 'Progress toward this goal per day' })}</div>
        <div class="card"><h2>Counts toward this goal</h2>${links.length ? `<ul class="tl">${links.map(h => `<li><span>${E(h.icon)}</span><span class="grow">${E(h.name)}</span><span class="muted small">${Core.goalKind(h) === 'check' ? 'each completed day = 1' : 'recorded ' + E(App.unitLabel(h))}</span></li>`).join('')}</ul>` : '<p class="muted small">No habits linked. Add progress manually below.</p>'}<p class="hint mt">Each habit and each day is counted once, so nothing is double-counted.</p></div>
        <div class="card"><h2>Milestones</h2>${pr.milestones.length ? `<ul class="tl">${pr.milestones.map(m => `<li><span>${m.ok ? '✅' : '⬜'}</span><span class="grow">${E(m.t)}</span><span class="muted small">at ${m.at} ${E(g.unit || '')}</span></li>`).join('')}</ul>` : '<p class="muted small">Add milestones when you edit the goal.</p>'}</div>
        <div class="card"><h2>Manual progress</h2><div class="row"><input class="inp grow" id="gv" type="number" step="any" min="0" placeholder="Amount" aria-label="Amount"><button class="btn" data-act="glog" data-id="${g.id}">Add</button></div>
        ${(g.log || []).length ? `<ul class="tl mt">${g.log.slice().reverse().slice(0, 10).map((l, i) => `<li><span class="muted small" style="width:90px">${UI.fmtDate(l.date, D.settings.dateFmt)}</span><span class="grow">+${l.v} ${E(g.unit || '')}</span><button class="lnk small" data-act="gunlog" data-id="${g.id}" data-i="${g.log.length - 1 - i}">Remove</button></li>`).join('')}</ul>` : ''}</div>
        <button class="btn danger full" data-act="gdel" data-id="${g.id}">Delete goal</button></div>`;
    },
    acts: {
      glog: t => { const v = parseFloat(document.getElementById('gv').value); if (!(v > 0)) { UI.toast('Enter an amount greater than 0.', { err: 1 }); return; } const g = App.D.goals.find(x => x.id === t.dataset.id); App.act(() => { (g.log = g.log || []).push({ date: App.tdy(), v }); }, 'Progress added.'); },
      gunlog: t => { const g = App.D.goals.find(x => x.id === t.dataset.id); App.act(() => { g.log.splice(+t.dataset.i, 1); }, 'Removed.'); },
      gdel: async t => { if (!(await UI.confirm('Delete this goal?', 'Your habit records are not affected.', 'Delete', true))) return; App.act(() => { App.D.goals = App.D.goals.filter(x => x.id !== t.dataset.id); }, 'Goal deleted.'); App.back(); }
    }
  };
})();
Screens.goalForm = (() => {
  const E = s => UI.esc(s); let G = null, key = null;
  return {
    render(p) {
      const D = App.D, t = App.tdy(); if (key !== (p.id || 'new')) { key = p.id || 'new'; const ex = p.id && D.goals.find(x => x.id === p.id); G = ex ? JSON.parse(JSON.stringify(ex)) : { id: '', name: '', desc: '', icon: '\u{1F3AF}', color: '#2f6bff', period: 'monthly', target: 10, unit: '', start: t, due: Core.addDays(t, 30), habitIds: [], ms: [], log: [] }; }
      return `<div class="top"><button class="ib" data-act="back" aria-label="Cancel">${UI.icon('x')}</button><h1 class="t2">${G.id ? 'Edit goal' : 'New goal'}</h1><button class="btn sm" data-act="save">Save</button></div><div class="stack"><div class="card">
        <div class="row"><input class="inp" style="width:64px;text-align:center;font-size:1.3rem" maxlength="4" value="${E(G.icon)}" data-input="g" data-k="icon" aria-label="Icon"><div class="grow"><input class="inp" maxlength="60" placeholder="e.g. Read 300 pages" value="${E(G.name)}" data-input="g" data-k="name" aria-label="Goal name"></div></div>
        <div class="fld mt"><label>Description (optional)</label><input class="inp" maxlength="140" value="${E(G.desc || '')}" data-input="g" data-k="desc"></div>
        <div class="fld"><label>Period</label><select class="inp" data-change="period">${[['daily', 'Every day'], ['weekly', 'Every week'], ['monthly', 'Every month'], ['yearly', 'Every year'], ['custom', 'Custom dates']].map(o => `<option value="${o[0]}" ${G.period === o[0] ? 'selected' : ''}>${o[1]}</option>`).join('')}</select></div>
        ${G.period === 'custom' ? `<div class="row"><div class="fld grow"><label>Start</label><input class="inp" type="date" value="${G.start}" data-input="g" data-k="start"></div><div class="fld grow"><label>Target date</label><input class="inp" type="date" value="${G.due}" data-input="g" data-k="due"></div></div>` : ''}
        <div class="row"><div class="fld grow"><label>Target</label><input class="inp" type="number" min="1" step="any" value="${G.target}" data-input="g" data-k="target"></div><div class="fld grow"><label>Unit</label><input class="inp" maxlength="20" value="${E(G.unit)}" placeholder="pages, workouts, min" data-input="g" data-k="unit"></div></div>
        <span class="lbl">Linked habits</span><p class="hint" style="margin:4px 0 8px">Completion habits add 1 per completed day. Amount and duration habits add what you record.</p>
        <div class="chips">${D.habits.filter(h => !h.archived).map(h => `<button class="chip ${G.habitIds.indexOf(h.id) >= 0 ? 'on' : ''}" data-act="link" data-v="${h.id}">${E(h.icon + ' ' + h.name)}</button>`).join('') || '<span class="muted small">No habits yet.</span>'}</div>
        <span class="lbl" style="display:block;margin-top:16px">Milestones</span>${G.ms.map((m, i) => `<div class="row" style="margin-top:8px"><input class="inp grow" maxlength="40" value="${E(m.t)}" data-input="ms" data-i="${i}" data-k="t" aria-label="Milestone name"><input class="inp" style="width:90px" type="number" min="1" value="${m.at}" data-input="ms" data-i="${i}" data-k="at" aria-label="Milestone amount"><button class="ib" data-act="msdel" data-i="${i}" aria-label="Remove milestone">${UI.icon('trash', 18)}</button></div>`).join('')}
        <button class="btn sec sm mt" data-act="msadd">${UI.icon('plus', 16)} Add milestone</button></div><div class="err" id="gerr"></div><button class="btn full" data-act="save">Save goal</button></div>`;
    },
    inputs: { g: t => { G[t.dataset.k] = t.value; }, ms: t => { G.ms[+t.dataset.i][t.dataset.k] = t.dataset.k === 'at' ? +t.value : t.value; } },
    changes: { period: t => { G.period = t.value; App.render(); } },
    acts: {
      link: t => { const i = G.habitIds.indexOf(t.dataset.v); if (i >= 0) G.habitIds.splice(i, 1); else G.habitIds.push(t.dataset.v); App.render(); },
      msadd: () => { G.ms.push({ id: Core.uid(), t: 'Milestone ' + (G.ms.length + 1), at: Math.round((+G.target || 10) / 2) }); App.render(); }, msdel: t => { G.ms.splice(+t.dataset.i, 1); App.render(); },
      save: () => { const er = !G.name.trim() ? 'Give your goal a name.' : !(+G.target > 0) ? 'Set a target greater than 0.' : G.period === 'custom' && (!G.due || G.due < G.start) ? 'The target date must be after the start.' : '';
        if (er) { document.getElementById('gerr').textContent = er; return; } G.target = +G.target; G.name = G.name.trim(); G.ms = G.ms.filter(m => m.t.trim() && m.at > 0).sort((a, b) => a.at - b.at);
        const D = App.D; App.act(() => { if (G.id) { const i = D.goals.findIndex(x => x.id === G.id); D.goals[i] = G; } else { G.id = Core.uid(); G.created = Date.now(); D.goals.push(G); } }, 'Goal saved.', { noUndo: 1 }); key = null; App.back(); }
    }
  };
})();
Screens.challengeForm = (() => {
  const E = s => UI.esc(s); let C = { hid: '', days: 21, name: '' };
  return {
    render() { const D = App.D, hs = Core.live(D); if (!C.hid && hs.length) C.hid = hs[0].id;
      return `<div class="top"><button class="ib" data-act="back" aria-label="Cancel">${UI.icon('x')}</button><h1 class="t2">New challenge</h1></div><div class="card">${hs.length ? `
        <div class="fld"><label>Habit</label><select class="inp" data-change="hid">${hs.map(h => `<option value="${h.id}" ${C.hid === h.id ? 'selected' : ''}>${E(h.icon + ' ' + h.name)}</option>`).join('')}</select></div>
        <span class="lbl">Length</span><div class="chips" style="margin:8px 0 14px">${[7, 21, 30, 66, 100].map(n => `<button class="chip ${C.days === n ? 'on' : ''}" data-act="len" data-v="${n}">${n} days</button>`).join('')}</div>
        <p class="hint" style="margin-bottom:14px">Starts today. Complete the habit on ${C.days} days within the next ${C.days} days to win.</p><button class="btn full" data-act="save">Start challenge</button>` : UI.empty('\u{1F3C1}', 'Add a habit first', 'A challenge is built on one of your habits.')}</div>`; },
    changes: { hid: t => { C.hid = t.value; } },
    acts: { len: t => { C.days = +t.dataset.v; App.render(); }, save: () => { const h = App.habit(C.hid); App.act(() => { App.D.challenges.push({ id: Core.uid(), name: C.days + '-day ' + h.name + ' challenge', habitId: h.id, days: C.days, start: App.tdy() }); }, 'Challenge started. You can do it!', { noUndo: 1 }); App.back(); } }
  };
})();
