/* HabitFlow core: dates, schedules, tracking rules, streaks, stats, reminders.
   Pure functions on a plain data object `D` (no DOM) so they can be unit-tested in Node. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory(); else root.Core = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';
  const pad = n => (n < 10 ? '0' : '') + n;
  const ymd = d => d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());   // local calendar date
  const parse = s => { const p = s.split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); };
  const todayStr = now => ymd(now || new Date());
  const addDays = (s, n) => { const d = parse(s); d.setDate(d.getDate() + n); return ymd(d); };
  const diffDays = (a, b) => { const x = a.split('-').map(Number), y = b.split('-').map(Number); return Math.round((Date.UTC(y[0], y[1] - 1, y[2]) - Date.UTC(x[0], x[1] - 1, x[2])) / 864e5); };
  const dow = s => parse(s).getDay();
  const dim = (y, m) => new Date(y, m, 0).getDate();
  const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
  function range(from, to, cap) { const out = []; let d = from, n = 0; while (d <= to && n++ < (cap || 4000)) { out.push(d); d = addDays(d, 1); } return out; }

  const DEFAULT_CATS = [
    { id: 'health', name: 'Health', color: '#34c759', icon: '\u2764\uFE0F' }, { id: 'fitness', name: 'Fitness', color: '#ff9f0a', icon: '\u{1F4AA}' },
    { id: 'mind', name: 'Mindfulness', color: '#5e5ce6', icon: '\u{1F9E0}' }, { id: 'learn', name: 'Learning', color: '#0a84ff', icon: '\u{1F4DA}' },
    { id: 'work', name: 'Productivity', color: '#64d2ff', icon: '\u{1F4BC}' }, { id: 'home', name: 'Home', color: '#ac8e68', icon: '\u{1F3E0}' }];
  const DEFAULT_SECTIONS = [
    { id: 'morning', name: 'Morning', icon: '\u{1F305}' }, { id: 'afternoon', name: 'Afternoon', icon: '\u2600\uFE0F' },
    { id: 'evening', name: 'Evening', icon: '\u{1F307}' }, { id: 'night', name: 'Night', icon: '\u{1F319}' }, { id: 'anytime', name: 'Anytime', icon: '\u23F0' }];
  function newSettings() {
    return { theme: 'system', accent: '#2f6bff', density: 'comfortable', textScale: 1, quiet: { on: false, from: '22:00', to: '07:00' }, notif: true,
      weekStart: 1, name: '', timeFmt: '12', dateFmt: 'MDY', moodOn: true, aiOn: true, onboarded: false, plan: 'pro',
      profile: { goals: [], areas: [], style: 'simple', wake: '07:00', sleep: '23:00', wantRem: true, track: 'habits' },
      homeCards: { week: true, streaks: true, reminders: true, motivation: true, recent: true }, wellbeingLimit: 0 };
  }
  function newData() {
    return { v: 2, habits: [], entries: {}, journal: [], moods: [], focus: [], goals: [], challenges: [], integrations: {},
      cats: JSON.parse(JSON.stringify(DEFAULT_CATS)), sections: JSON.parse(JSON.stringify(DEFAULT_SECTIONS)), settings: newSettings() };
  }
  function migrate(d) {
    const n = newData(); d = d || {};
    Object.keys(n).forEach(k => { if (d[k] === undefined) d[k] = n[k]; });
    d.settings = Object.assign(newSettings(), d.settings || {});
    d.settings.profile = Object.assign(newSettings().profile, d.settings.profile || {});
    d.settings.homeCards = Object.assign(newSettings().homeCards, d.settings.homeCards || {});
    d.settings.quiet = Object.assign(newSettings().quiet, d.settings.quiet || {});
    d.cats = (d.cats || []).map((c, i) => typeof c === 'string' ? { id: 'c' + i + c.toLowerCase().replace(/\W/g, ''), name: c, color: '#8e8e93', icon: '\u2B50' } : c);
    d.habits.forEach(h => { if (!h.cats) h.cats = h.cat ? [h.cat] : []; if (h.part === undefined) h.part = 'anytime'; if (!h.sched) h.sched = { kind: 'daily' }; if (!h.goal) h.goal = { kind: 'check' }; if (h.type === undefined) h.type = 'build'; });
    d.v = 2; return d;
  }

  /* ---------- schedules ---------- */
  const isPaused = (h, date) => (h.pauses || []).some(p => date >= p.from && (!p.to || date <= p.to));
  function pauseHabit(h, date) { if (!isPaused(h, date)) (h.pauses = h.pauses || []).push({ from: date, to: null }); }
  function resumeHabit(h, date) {
    const p = (h.pauses || []).find(x => !x.to || x.to >= date); if (!p) return;
    if (p.from >= date) h.pauses.splice(h.pauses.indexOf(p), 1); else p.to = addDays(date, -1);
  }
  const isFlex = (h, date) => { const s = date ? schedFor(h, date) : h.sched; return !!s && s.kind === 'times'; };
  const isNegative = h => h.type === 'reduce' || h.type === 'quit';
  function isActive(h, date) { return date >= h.start && (!h.end || date <= h.end) && !isPaused(h, date); }
  /* h.schedHist = [{from, sched}] keeps earlier schedules so editing a schedule never rewrites history */
  function schedFor(h, date) {
    let s = h.sched || { kind: 'daily' };
    if (h.schedHist && h.schedHist.length) { for (let i = h.schedHist.length - 1; i >= 0; i--) { if (date >= h.schedHist[i].from) return h.schedHist[i].sched; } return h.schedHist[0].sched; }
    return s;
  }
  function changeSchedule(h, sched, tdy) {   // new schedule applies from today; earlier days keep the old one
    if (JSON.stringify(sched) === JSON.stringify(h.sched)) return;
    if (!h.schedHist || !h.schedHist.length) h.schedHist = [{ from: h.start, sched: h.sched || { kind: 'daily' } }];
    const from = tdy < h.start ? h.start : tdy;
    h.schedHist = h.schedHist.filter(x => x.from < from); h.schedHist.push({ from, sched }); h.sched = sched;
  }
  function isScheduled(h, date) {
    if (!isActive(h, date)) return false;
    const s = schedFor(h, date);
    switch (s.kind) {
      case 'weekly': return (s.days && s.days.length ? s.days : [0, 1, 2, 3, 4, 5, 6]).indexOf(dow(date)) >= 0;
      case 'monthly': { const p = date.split('-').map(Number); return p[2] === Math.min(s.dom || 1, dim(p[0], p[1])); }
      case 'interval': return diffDays(h.start, date) % Math.max(1, s.every || 1) === 0;
      case 'once': return date === h.start;
      default: return true; // daily and "times per period" (flexible) habits can be logged on any active day
    }
  }
  /* "N times per week / month / year" habits are judged per period, not per day */
  function periodRange(D, h, date) {
    const sc = h.start ? schedFor(h, date) : h.sched, per = (sc && sc.per) || 'week';
    if (per === 'month') { const p = date.split('-').map(Number); return { from: p[0] + '-' + pad(p[1]) + '-01', to: p[0] + '-' + pad(p[1]) + '-' + pad(dim(p[0], p[1])) }; }
    if (per === 'year') { const y = date.slice(0, 4); return { from: y + '-01-01', to: y + '-12-31' }; }
    const ws = D.settings.weekStart, back = (dow(date) - ws + 7) % 7, from = addDays(date, -back); return { from, to: addDays(from, 6) };
  }
  function periodDone(D, h, from, to) { let n = 0; range(from, to, 400).forEach(d => { const e = D.entries[ek(h.id, d)]; if (e && e.st === 'done') n++; }); return n; }
  const flexTarget = (h, date) => { const s = date && h.start ? schedFor(h, date) : h.sched; return Math.max(1, (s && s.n) || 1); };
  function periodProgress(D, h, date) { const r = periodRange(D, h, date); return { from: r.from, to: r.to, done: periodDone(D, h, r.from, r.to), n: flexTarget(h, date) }; }

  /* ---------- entries ---------- */
  const ek = (id, date) => id + '|' + date;
  const goalKind = h => (h.goal && h.goal.kind) || 'check';
  const target = h => goalKind(h) === 'check' ? 1 : Math.max(1, +h.goal.target || 1);
  function getEntry(D, h, date) { return D.entries[ek(h.id, date)] || null; }
  const checkItems = h => (h.check && h.check.length) ? h.check : null;
  function status(D, h, date, tdy) {
    if (!isScheduled(h, date)) return 'off';
    const e = D.entries[ek(h.id, date)];
    if (isNegative(h)) {
      const n = (e && e.n) || 0, lim = h.type === 'reduce' ? Math.max(0, (h.goal && h.goal.limit) || 0) : 0;
      if (e && e.st === 'skip') return 'skip';
      if (e && e.st === 'fail') return 'failed';
      if (n > lim) return 'slip';
      if (e && e.st === 'done') return 'done';
      return date < tdy ? 'missed' : 'pending';
    }
    if (e) {
      if (e.st === 'skip') return 'skip'; if (e.st === 'done') return 'done'; if (e.st === 'fail') return 'failed';
      if ((e.v || 0) > 0 || (e.chk && e.chk.length)) return isFlex(h, date) ? 'open' : (date < tdy ? 'missed' : 'partial');
    }
    if (isFlex(h, date)) return date > tdy ? 'pending' : 'open';
    return date < tdy ? 'missed' : 'pending';
  }
  function guard(h, date, tdy) {
    if (date > tdy) throw new Error('You cannot record a future day.');
    if (date < h.start) throw new Error('That day is before this habit started.');
    if (!isScheduled(h, date)) throw new Error('This habit is not scheduled on that day.');
  }
  function tidy(D, k) { const e = D.entries[k]; if (e && !e.st && !(e.v > 0) && !e.note && !(e.chk && e.chk.length) && !(e.n > 0)) delete D.entries[k]; }
  function setCheck(D, h, date, on, tdy) {
    guard(h, date, tdy); const k = ek(h.id, date); const e = D.entries[k] || (D.entries[k] = {});
    if (on) { e.st = 'done'; delete e.auto; if (goalKind(h) !== 'check') e.v = Math.max(e.v || 0, target(h)); if (checkItems(h)) e.chk = h.check.map(c => c.id); if (e.at === undefined) e.at = Date.now(); }
    else { delete e.st; delete e.auto; delete e.at; e.v = 0; if (checkItems(h)) e.chk = []; }
    tidy(D, k); return D.entries[k] || null;
  }
  function setValue(D, h, date, v, tdy) {
    guard(h, date, tdy); v = Math.max(0, Math.round((+v || 0) * 100) / 100);
    const k = ek(h.id, date); const e = D.entries[k] || (D.entries[k] = {});
    e.v = v; if (v >= target(h)) e.st = 'done'; else if (e.st === 'done') delete e.st;
    tidy(D, k); return D.entries[k] || null;
  }
  function addValue(D, h, date, delta, tdy) { const e = getEntry(D, h, date); return setValue(D, h, date, ((e && e.v) || 0) + delta, tdy); }
  function setItem(D, h, date, itemId, on, tdy) {
    guard(h, date, tdy); const items = checkItems(h); if (!items) throw new Error('This habit has no checklist.');
    const k = ek(h.id, date), e = D.entries[k] || (D.entries[k] = {}); let chk = (e.chk || []).filter(x => items.some(c => c.id === x));
    chk = on ? (chk.indexOf(itemId) < 0 ? chk.concat(itemId) : chk) : chk.filter(x => x !== itemId); e.chk = chk;
    if (chk.length === items.length) { e.st = 'done'; e.auto = true; if (e.at === undefined) e.at = Date.now(); }
    else if (e.st === 'done' && e.auto) { delete e.st; delete e.auto; delete e.at; }
    tidy(D, k); return D.entries[k] || null;
  }
  function addOccurrence(D, h, date, trigger, tdy) {   // negative habits: record that it happened
    guard(h, date, tdy); const k = ek(h.id, date), e = D.entries[k] || (D.entries[k] = {});
    e.n = (e.n || 0) + 1; (e.occ = e.occ || []).push({ ts: Date.now(), trig: (trigger || '').trim().slice(0, 200) });
    if (e.st === 'done' && e.n > (h.type === 'reduce' ? ((h.goal && h.goal.limit) || 0) : 0)) delete e.st; return e;
  }
  function removeOccurrence(D, h, date) { const k = ek(h.id, date), e = D.entries[k]; if (!e || !e.n) return; e.n--; if (e.occ) e.occ.pop(); tidy(D, k); }
  function setClean(D, h, date, on, tdy) {            // negative habits: record a successful day
    guard(h, date, tdy); const k = ek(h.id, date), e = D.entries[k] || (D.entries[k] = {});
    if (on) { const lim = h.type === 'reduce' ? ((h.goal && h.goal.limit) || 0) : 0; if ((e.n || 0) > lim) throw new Error(h.type === 'quit' ? 'An occurrence is recorded for this day. Remove it first if it was a mistake.' : 'You are over your limit for this day.'); e.st = 'done'; e.at = e.at || Date.now(); }
    else delete e.st; tidy(D, k); return D.entries[k] || null;
  }
  function setFail(D, h, date, on, tdy) {   // user explicitly records "not done today"
    guard(h, date, tdy); const k = ek(h.id, date), e = D.entries[k] || (D.entries[k] = {});
    if (on) { e.st = 'fail'; delete e.auto; } else if (e.st === 'fail') delete e.st; tidy(D, k); return D.entries[k] || null;
  }
  function setSkip(D, h, date, on, tdy) {
    guard(h, date, tdy); const k = ek(h.id, date); const e = D.entries[k] || (D.entries[k] = {});
    if (on) e.st = 'skip'; else if (e.st === 'skip') delete e.st;
    tidy(D, k); return D.entries[k] || null;
  }
  function setNote(D, h, date, text) {
    const k = ek(h.id, date); const e = D.entries[k] || (D.entries[k] = {});
    text = (text || '').trim().slice(0, 500); if (text) e.note = text; else delete e.note; tidy(D, k);
  }

  /* ---------- streaks & rates ---------- */
  function flexStreaks(D, h, tdy) {
    const n = flexTarget(h); let cur = 0, run = 0, best = 0;
    let d = h.start; while (d <= tdy) { const pr = periodRange(D, h, d); const ended = pr.to < tdy; const met = periodDone(D, h, pr.from, pr.to) >= n;
      if (met) { run++; if (run > best) best = run; } else if (ended) run = 0; d = addDays(pr.to, 1); }
    let p = periodRange(D, h, tdy); if (periodDone(D, h, p.from, p.to) >= n) cur++;
    d = addDays(p.from, -1); while (d >= h.start) { p = periodRange(D, h, d); if (periodDone(D, h, p.from, p.to) >= n) cur++; else break; d = addDays(p.from, -1); }
    return { cur, best };
  }
  function currentStreak(D, h, tdy) {
    if (isFlex(h, tdy)) return flexStreaks(D, h, tdy).cur;
    let cur = 0, d = tdy, guardN = 0;
    while (d >= h.start && guardN++ < 4000) {
      if (isScheduled(h, d)) {
        const st = status(D, h, d, tdy);
        if (st === 'done') cur++;
        else if (st === 'skip') { /* rest day: neither counts nor breaks */ }
        else if (d === tdy && st !== 'slip' && st !== 'failed') { /* today still open */ }
        else break;
      }
      d = addDays(d, -1);
    }
    return cur;
  }
  function longestStreak(D, h, tdy) {
    if (isFlex(h, tdy)) return flexStreaks(D, h, tdy).best;
    let run = 0, best = 0;
    range(h.start, tdy).forEach(d => {
      if (!isScheduled(h, d)) return;
      const st = status(D, h, d, tdy);
      if (st === 'done') { run++; if (run > best) best = run; }
      else if (st === 'skip' || (d === tdy && st !== 'slip' && st !== 'failed')) { /* neutral */ }
      else run = 0;
    });
    return best;
  }
  function totalDone(D, h, tdy) { let n = 0; range(h.start, tdy).forEach(d => { if (status(D, h, d, tdy) === 'done') n++; }); return n; }
  function flexRate(D, h, from, to, tdy) {
    const n = flexTarget(h), end = to > tdy ? tdy : to; let met = 0, total = 0, d = from < h.start ? h.start : from;
    while (d <= end) { const pr = periodRange(D, h, d), ok = periodDone(D, h, pr.from, pr.to) >= n; if (pr.to <= tdy || ok) { total++; if (ok) met++; } d = addDays(pr.to, 1); }
    return { done: met, total, skipped: 0, missed: total - met, pct: total ? Math.round(met / total * 100) : 0 };
  }
  function rate(D, h, from, to, tdy) {
    if (isFlex(h, tdy)) return flexRate(D, h, from, to, tdy);
    let done = 0, total = 0, skipped = 0, missed = 0;
    const end = to > tdy ? tdy : to, start = from < h.start ? h.start : from;
    range(start, end).forEach(d => {
      const st = status(D, h, d, tdy); if (st === 'off') return;
      if (st === 'skip') { skipped++; return; }
      total++; if (st === 'done') done++; else if (st === 'missed' || st === 'slip' || st === 'failed') missed++;
    });
    return { done, total, skipped, missed, pct: total ? Math.round(done / total * 100) : 0 };
  }
  const live = D => D.habits.filter(h => !h.archived);
  const habitCats = h => h.cats && h.cats.length ? h.cats : (h.cat ? [h.cat] : []);
  function dayCompletion(D, date, tdy, habits) {
    let done = 0, total = 0; const remaining = [], finished = [], skipped = [], missed = [], flex = [];
    (habits || live(D)).forEach(h => {
      const st = status(D, h, date, tdy); if (st === 'off') return;
      if (isFlex(h, date)) { flex.push({ h, st, p: periodProgress(D, h, date) }); return; }
      if (st === 'skip') { skipped.push(h); return; }
      if (st === 'missed' || st === 'slip' || st === 'failed') missed.push(h);
      total++; if (st === 'done') { done++; finished.push(h); } else remaining.push(h);
    });
    return { done, total, pct: total ? Math.round(done / total * 100) : 0, remaining, finished, skipped, missed, flex };
  }
  function periodRate(D, from, to, tdy, habits) {
    let done = 0, total = 0;
    (habits || live(D)).forEach(h => { const r = rate(D, h, from, to, tdy); done += r.done; total += r.total; });
    return { done, total, pct: total ? Math.round(done / total * 100) : 0 };
  }
  function goalStats(D, tdy) { // for count/time goals: days the target was reached
    let met = 0, total = 0;
    live(D).forEach(h => { if (goalKind(h) === 'check' || isFlex(h, tdy)) return; range(h.start, tdy).forEach(d => { const st = status(D, h, d, tdy); if (st === 'off' || st === 'skip' || (st === 'pending' && d === tdy)) return; total++; if (st === 'done') met++; }); });
    return { met, total, pct: total ? Math.round(met / total * 100) : 0 };
  }

  /* ---------- goals & challenges ---------- */
  function goalWindow(D, g, tdy) {
    switch (g.period) {
      case 'daily': return [tdy, tdy];
      case 'weekly': { const r = periodRange(D, { sched: { per: 'week' } }, tdy); return [r.from, r.to]; }
      case 'monthly': { const r = periodRange(D, { sched: { per: 'month' } }, tdy); return [r.from, r.to]; }
      case 'yearly': { const r = periodRange(D, { sched: { per: 'year' } }, tdy); return [r.from, r.to]; }
      default: return [g.start || tdy, g.due || tdy];
    }
  }
  function goalProgress(D, g, tdy) {   // every habit is counted once, every day-entry is counted once
    const w = goalWindow(D, g, tdy), from = w[0], to = w[1] > tdy ? tdy : w[1]; let sum = 0; const seen = {};
    (g.habitIds || []).forEach(id => { if (seen[id]) return; seen[id] = 1; const h = D.habits.find(x => x.id === id); if (!h) return;
      range(from, to, 800).forEach(d => { const e = D.entries[ek(id, d)]; if (!e) return; if (goalKind(h) === 'check') { if (e.st === 'done') sum++; } else sum += e.v || 0; }); });
    (g.log || []).forEach(l => { if (l.date >= from && l.date <= to) sum += +l.v || 0; });
    const tg = Math.max(1, +g.target || 1), pct = Math.min(100, Math.round(sum / tg * 100));
    return { sum: Math.round(sum * 100) / 100, target: tg, pct, remaining: Math.max(0, Math.round((tg - sum) * 100) / 100), from: w[0], to: w[1], daysLeft: Math.max(0, diffDays(tdy, w[1])), done: sum >= tg,
      milestones: (g.ms || []).map(m => ({ id: m.id, t: m.t, at: m.at, ok: sum >= m.at })) };
  }
  function challengeProgress(D, c, tdy) {
    const h = D.habits.find(x => x.id === c.habitId); const end = addDays(c.start, c.days - 1), to = end > tdy ? tdy : end; let done = 0;
    if (h) range(c.start, to).forEach(d => { if (status(D, h, d, tdy) === 'done') done++; });
    return { done, days: c.days, pct: Math.round(done / c.days * 100), end, finished: tdy > end, won: done >= c.days, habit: h };
  }
  function moodAverage(D, from, to) { const m = D.moods.filter(x => x.date >= from && x.date <= to); return m.length ? Math.round(m.reduce((a, x) => a + x.mood, 0) / m.length * 10) / 10 : null; }
  function moodVsHabits(D, from, to, tdy) {   // personal observation only: average mood on days with high vs low completion
    const hi = [], lo = [];
    D.moods.forEach(m => { if (m.date < from || m.date > to) return; const c = dayCompletion(D, m.date, tdy); if (!c.total) return; (c.pct >= 70 ? hi : lo).push(m.mood); });
    const avg = a => a.length ? Math.round(a.reduce((x, y) => x + y, 0) / a.length * 10) / 10 : null;
    return { hi: avg(hi), lo: avg(lo), nHi: hi.length, nLo: lo.length };
  }

  /* ---------- summary & achievements ---------- */
  function summary(D, tdy) {
    let total = 0, longest = 0, perfect = 0, earliest = tdy;
    D.habits.forEach(h => { total += totalDone(D, h, tdy); longest = Math.max(longest, longestStreak(D, h, tdy)); if (h.start < earliest) earliest = h.start; });
    const hs = live(D);
    if (hs.length) range(earliest, tdy, 800).forEach(d => { const c = dayCompletion(D, d, tdy, hs); if (c.total >= 3 && c.done === c.total) perfect++; });
    const focusMin = Math.round(D.focus.reduce((a, s) => a + s.secs, 0) / 60);
    return { total, longest, perfect, focusSessions: D.focus.length, focusMin, journal: D.journal.length, goals: D.goals.filter(g => goalProgress(D, g, tdy).done).length };
  }
  const ACH = [
    { id: 'first', t: 'First Step', d: 'Complete a habit for the first time', f: s => s.total >= 1, i: '\u{1F331}' },
    { id: 't10', t: 'Getting Going', d: '10 completions', f: s => s.total >= 10, i: '\u{1F33F}' },
    { id: 't50', t: 'Building Momentum', d: '50 completions', f: s => s.total >= 50, i: '\u{1F333}' },
    { id: 't100', t: 'Century', d: '100 completions', f: s => s.total >= 100, i: '\u{1F4AF}' },
    { id: 't500', t: 'Unstoppable', d: '500 completions', f: s => s.total >= 500, i: '\u{1F3C6}' },
    { id: 's3', t: '3-Day Streak', d: 'Keep one habit going 3 days', f: s => s.longest >= 3, i: '\u{1F525}' },
    { id: 's7', t: 'One Full Week', d: '7-day streak', f: s => s.longest >= 7, i: '\u{1F4C5}' },
    { id: 's30', t: 'Habit Formed', d: '30-day streak', f: s => s.longest >= 30, i: '\u{1F31F}' },
    { id: 's100', t: 'Legend', d: '100-day streak', f: s => s.longest >= 100, i: '\u{1F451}' },
    { id: 'perfect', t: 'Perfect Day', d: 'Finish every habit in a day (3+ habits)', f: s => s.perfect >= 1, i: '✨' },
    { id: 'focus5', t: 'Deep Focus', d: 'Finish 5 focus sessions', f: s => s.focusSessions >= 5, i: '\u{1F3AF}' },
    { id: 'focus10h', t: 'Ten Hours', d: '10 hours of focus time', f: s => s.focusMin >= 600, i: '⏱️' },
    { id: 'goal1', t: 'Goal Getter', d: 'Reach a personal goal', f: s => s.goals >= 1, i: '\u{1F3C1}' },
    { id: 'journal7', t: 'Reflective', d: 'Write 7 journal entries', f: s => s.journal >= 7, i: '\u{1F4D3}' }
  ];
  const achievements = s => ACH.map(a => ({ id: a.id, t: a.t, d: a.d, i: a.i, ok: !!a.f(s) }));

  /* ---------- reminders ---------- */
  function inQuiet(t, q) { if (!q || !q.on) return false; return q.from <= q.to ? (t >= q.from && t < q.to) : (t >= q.from || t < q.to); }
  function hashId(str) { let h = 5381; for (let i = 0; i < str.length; i++) h = ((h << 5) + h + str.charCodeAt(i)) | 0; return Math.abs(h) % 2000000000 + 1; }
  function upcomingReminders(D, now, days, max) {
    const out = [], tdy = todayStr(now), q = D.settings.quiet;
    live(D).forEach(h => {
      if (!h.rem || !h.rem.on || !h.rem.times) return;
      for (let o = 0; o < (days || 14); o++) {
        const date = addDays(tdy, o); if (!isScheduled(h, date)) continue;
        if (o === 0) { const st = status(D, h, date, tdy); if (st === 'done' || st === 'skip') continue; }
        if (isFlex(h, date) && periodProgress(D, h, date).done >= flexTarget(h, date)) continue;
        const wd = dow(date), times = (h.rem.byDay && h.rem.byDay[wd] && h.rem.byDay[wd].length) ? h.rem.byDay[wd] : h.rem.times;
        times.forEach(t => {
          if (inQuiet(t, q)) return;
          const p = date.split('-').map(Number), hm = t.split(':').map(Number);
          const ts = new Date(p[0], p[1] - 1, p[2], hm[0], hm[1], 0, 0).getTime();
          if (ts <= now.getTime() + 30000) return;
          const after = h.stack && D.habits.find(x => x.id === h.stack);
          out.push({ id: hashId(h.id + date + t), ts, hid: h.id, date, time: t,
            title: (h.icon || '') + ' ' + h.name,
            text: h.rem.msg ? h.rem.msg : h.type === 'quit' ? 'Stay strong today. You can do this.' : (after ? 'After "' + after.name + '": time for this habit.' : 'Time for your habit. A small step counts.') });
        });
      }
    });
    out.sort((a, b) => a.ts - b.ts); return out.slice(0, max || 60);
  }

  /* ---------- text reports ---------- */
  function weeklyInsight(D, tdy) {
    const from = addDays(tdy, -6), prevFrom = addDays(tdy, -13), prevTo = addDays(tdy, -7);
    const cur = periodRate(D, from, tdy, tdy), prev = periodRate(D, prevFrom, prevTo, tdy);
    const per = live(D).map(h => ({ h, r: rate(D, h, from, tdy, tdy) })).filter(x => x.r.total);
    per.sort((a, b) => b.r.pct - a.r.pct);
    const lines = [];
    if (!cur.total) return ['Add a habit and check it off to see your weekly insights here.'];
    lines.push('You completed ' + cur.done + ' of ' + cur.total + ' scheduled habits this week (' + cur.pct + '%).');
    if (prev.total) { const d = cur.pct - prev.pct; lines.push(d > 0 ? 'That is ' + d + ' points better than last week. Nice progress.' : d < 0 ? 'That is ' + (-d) + ' points lower than last week. A fresh start is always one check-in away.' : 'Same as last week. Steady and consistent.'); }
    if (per.length) { lines.push('Strongest habit: ' + per[0].h.name + ' (' + per[0].r.pct + '%).'); if (per.length > 1 && per[per.length - 1].r.pct < per[0].r.pct) lines.push('Most room to grow: ' + per[per.length - 1].h.name + ' (' + per[per.length - 1].r.pct + '%). Try a smaller goal or an earlier time.'); }
    return lines;
  }
  function csv(D) {
    const esc = v => '"' + String(v == null ? '' : v).replace(/"/g, '""') + '"';
    const rows = [['habit', 'date', 'status', 'value', 'note'].join(',')];
    Object.keys(D.entries).sort().forEach(k => { const [id, date] = k.split('|'), h = D.habits.find(x => x.id === id), e = D.entries[k]; if (!h) return;
      rows.push([esc(h.name), date, e.st || (e.n ? 'occurrence' : e.v ? 'partial' : 'note'), e.v || e.n || 0, esc(e.note || '')].join(',')); });
    return rows.join('\n');
  }
  function validateImport(obj) {
    if (!obj || typeof obj !== 'object' || !Array.isArray(obj.habits) || typeof obj.entries !== 'object') throw new Error('This is not a HabitFlow backup.');
    return migrate(JSON.parse(JSON.stringify(obj)));
  }

  return { schedFor, changeSchedule, setFail, habitCats, DEFAULT_CATS, DEFAULT_SECTIONS, newSettings, migrate, isPaused, pauseHabit, resumeHabit, isFlex, isNegative, periodRange, periodProgress, flexTarget, checkItems, setItem, addOccurrence, removeOccurrence, setClean, goalWindow, goalProgress, challengeProgress, moodAverage, moodVsHabits, pad, ymd, parse, todayStr, addDays, diffDays, dow, dim, uid, range, newData, isActive, isScheduled, ek, goalKind, target, getEntry, status,
    setCheck, setValue, addValue, setSkip, setNote, currentStreak, longestStreak, totalDone, rate, live, dayCompletion, periodRate, goalStats,
    summary, achievements, inQuiet, hashId, upcomingReminders, weeklyInsight, csv, validateImport };
});
