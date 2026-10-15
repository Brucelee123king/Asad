// Run: node android_app/habitflow/tests/core.test.js   (set TZ=... to test other time zones)
const C = require('../js/core.js');
const assert = require('assert');
let n = 0; const t = (name, fn) => { try { fn(); n++; console.log('ok  -', name); } catch (e) { console.error('FAIL -', name, '\n', e.message); process.exitCode = 1; } };
const H = (o) => Object.assign({ id: 'h1', name: 'Read', start: '2026-03-01', sched: { kind: 'daily' }, goal: { kind: 'check' } }, o);
const D = () => C.newData();

t('addDays/diffDays are stable across DST changes', () => {
  assert.strictEqual(C.addDays('2026-03-07', 1), '2026-03-08'); assert.strictEqual(C.addDays('2026-03-08', 1), '2026-03-09');
  assert.strictEqual(C.addDays('2026-11-01', 1), '2026-11-02'); assert.strictEqual(C.addDays('2026-12-31', 1), '2027-01-01');
  assert.strictEqual(C.diffDays('2026-03-01', '2026-04-01'), 31); assert.strictEqual(C.diffDays('2026-01-01', '2027-01-01'), 365);
  assert.strictEqual(C.range('2026-03-07', '2026-03-10').length, 4);
});
t('weekly schedule only on chosen weekdays', () => {
  const h = H({ sched: { kind: 'weekly', days: [1, 3] } }); // Mon, Wed
  assert.ok(C.isScheduled(h, '2026-03-02')); assert.ok(!C.isScheduled(h, '2026-03-03')); assert.ok(C.isScheduled(h, '2026-03-04'));
});
t('monthly schedule clamps to the last day of short months', () => {
  const h = H({ start: '2026-01-01', sched: { kind: 'monthly', dom: 31 } });
  assert.ok(C.isScheduled(h, '2026-01-31')); assert.ok(C.isScheduled(h, '2026-02-28')); assert.ok(!C.isScheduled(h, '2026-02-27')); assert.ok(C.isScheduled(h, '2026-04-30'));
});
t('interval schedule counts from the start date', () => {
  const h = H({ start: '2026-03-01', sched: { kind: 'interval', every: 3 } });
  assert.ok(C.isScheduled(h, '2026-03-01')); assert.ok(!C.isScheduled(h, '2026-03-02')); assert.ok(C.isScheduled(h, '2026-03-04')); assert.ok(C.isScheduled(h, '2026-03-31'));
});
t('start and end dates limit scheduling', () => {
  const h = H({ start: '2026-03-05', end: '2026-03-10' });
  assert.ok(!C.isScheduled(h, '2026-03-04')); assert.ok(C.isScheduled(h, '2026-03-10')); assert.ok(!C.isScheduled(h, '2026-03-11'));
});
t('check-ins are unique per habit and day (no duplicates)', () => {
  const d = D(), h = H(); d.habits.push(h);
  C.setCheck(d, h, '2026-03-05', true, '2026-03-05'); C.setCheck(d, h, '2026-03-05', true, '2026-03-05');
  assert.strictEqual(Object.keys(d.entries).length, 1);
  C.setCheck(d, h, '2026-03-05', false, '2026-03-05'); assert.strictEqual(Object.keys(d.entries).length, 0);
});
t('future days, pre-start days and unscheduled days are rejected', () => {
  const d = D(), h = H({ sched: { kind: 'weekly', days: [1] } });
  assert.throws(() => C.setCheck(d, h, '2026-03-10', true, '2026-03-05'), /future/);
  assert.throws(() => C.setCheck(d, h, '2026-02-23', true, '2026-03-05'), /before/);
  assert.throws(() => C.setCheck(d, h, '2026-03-03', true, '2026-03-05'), /not scheduled/);
});
t('count goals: partial progress is not done until the target is reached', () => {
  const d = D(), h = H({ goal: { kind: 'count', target: 8, unit: 'glasses' } });
  C.setValue(d, h, '2026-03-05', 3, '2026-03-05'); assert.strictEqual(C.status(d, h, '2026-03-05', '2026-03-05'), 'partial');
  C.addValue(d, h, '2026-03-05', 5, '2026-03-05'); assert.strictEqual(C.status(d, h, '2026-03-05', '2026-03-05'), 'done');
  C.setValue(d, h, '2026-03-05', 2, '2026-03-05'); assert.strictEqual(C.status(d, h, '2026-03-05', '2026-03-05'), 'partial');
  C.setValue(d, h, '2026-03-05', -4, '2026-03-05'); assert.strictEqual(C.getEntry(d, h, '2026-03-05'), null);
});
t('streak: counts consecutive done days; today still open does not break it', () => {
  const d = D(), h = H(); d.habits.push(h);
  ['2026-03-02', '2026-03-03', '2026-03-04'].forEach(x => C.setCheck(d, h, x, true, '2026-03-05'));
  assert.strictEqual(C.currentStreak(d, h, '2026-03-05'), 3);
  C.setCheck(d, h, '2026-03-05', true, '2026-03-05'); assert.strictEqual(C.currentStreak(d, h, '2026-03-05'), 4);
});
t('streak: a missed past day breaks it, a rest day does not', () => {
  const d = D(), h = H(); d.habits.push(h);
  C.setCheck(d, h, '2026-03-01', true, '2026-03-06'); C.setCheck(d, h, '2026-03-02', true, '2026-03-06');
  C.setSkip(d, h, '2026-03-03', true, '2026-03-06'); C.setCheck(d, h, '2026-03-04', true, '2026-03-06'); C.setCheck(d, h, '2026-03-05', true, '2026-03-06');
  assert.strictEqual(C.currentStreak(d, h, '2026-03-06'), 4); assert.strictEqual(C.longestStreak(d, h, '2026-03-06'), 4);
  C.setCheck(d, h, '2026-03-04', false, '2026-03-06'); assert.strictEqual(C.currentStreak(d, h, '2026-03-06'), 1); assert.strictEqual(C.longestStreak(d, h, '2026-03-06'), 2);
});
t('streak only looks at scheduled days (weekly habit)', () => {
  const d = D(), h = H({ start: '2026-03-01', sched: { kind: 'weekly', days: [1, 4] } }); d.habits.push(h); // Mon & Thu
  ['2026-03-02', '2026-03-05', '2026-03-09'].forEach(x => C.setCheck(d, h, x, true, '2026-03-10'));
  assert.strictEqual(C.currentStreak(d, h, '2026-03-10'), 3);
});
t('rate ignores rest days and unscheduled days', () => {
  const d = D(), h = H(); d.habits.push(h);
  C.setCheck(d, h, '2026-03-01', true, '2026-03-04'); C.setSkip(d, h, '2026-03-02', true, '2026-03-04'); // 3rd, 4th: missed / pending-today
  const r = C.rate(d, h, '2026-03-01', '2026-03-04', '2026-03-04');
  assert.deepStrictEqual([r.done, r.total, r.skipped, r.missed, r.pct], [1, 3, 1, 1, 33]);
});
t('day completion lists remaining habits', () => {
  const d = D(), a = H({ id: 'a' }), b = H({ id: 'b', name: 'Run' }); d.habits.push(a, b);
  C.setCheck(d, a, '2026-03-05', true, '2026-03-05'); const c = C.dayCompletion(d, '2026-03-05', '2026-03-05');
  assert.strictEqual(c.pct, 50); assert.strictEqual(c.remaining[0].id, 'b');
});
t('achievements unlock from real data', () => {
  const d = D(), h = H(); d.habits.push(h);
  C.range('2026-03-01', '2026-03-07').forEach(x => C.setCheck(d, h, x, true, '2026-03-07'));
  const a = C.achievements(C.summary(d, '2026-03-07')); const ok = id => a.find(x => x.id === id).ok;
  assert.ok(ok('first') && ok('s7') && ok('t10') === false);
});
t('reminders: respect schedule, quiet hours, done status and time', () => {
  const d = D(), h = H({ rem: { on: true, times: ['08:00', '23:00'] } }); d.habits.push(h);
  d.settings.quiet = { on: true, from: '22:00', to: '07:00' };
  const now = new Date(2026, 2, 5, 9, 0, 0); // 5 Mar 2026 09:00 local
  const r = C.upcomingReminders(d, now, 2); // today (08:00 already passed, 23:00 quiet) + tomorrow 08:00
  assert.strictEqual(r.length, 1); assert.strictEqual(new Date(r[0].ts).getDate(), 6); assert.strictEqual(new Date(r[0].ts).getHours(), 8);
  C.setCheck(d, h, '2026-03-05', true, '2026-03-05'); d.settings.quiet.on = false;
  assert.ok(C.upcomingReminders(d, new Date(2026, 2, 5, 6, 0), 1).length === 0); // done today -> no reminder
});
t('reminder times follow the device time zone (wall-clock time)', () => {
  const d = D(), h = H({ rem: { on: true, times: ['07:30'] } }); d.habits.push(h);
  const r = C.upcomingReminders(d, new Date(2026, 2, 7, 12, 0), 3); // spans a DST change in some zones
  r.forEach(x => { const dt = new Date(x.ts); assert.strictEqual(dt.getHours() + ':' + dt.getMinutes(), '7:30'); });
});
t('quiet hours across midnight', () => {
  const q = { on: true, from: '22:00', to: '07:00' };
  assert.ok(C.inQuiet('23:30', q)); assert.ok(C.inQuiet('03:00', q)); assert.ok(!C.inQuiet('07:00', q)); assert.ok(!C.inQuiet('12:00', q));
});
t('backup import validates structure', () => {
  assert.throws(() => C.validateImport({ nope: 1 }), /not a HabitFlow/);
  const d = C.validateImport({ habits: [], entries: {} }); assert.ok(d.settings && d.cats);
});
t('paused days are not scheduled and do not break streaks; history is kept', () => {
  const d = D(), h = H(); d.habits.push(h);
  C.setCheck(d, h, '2026-03-01', true, '2026-03-06'); C.setCheck(d, h, '2026-03-02', true, '2026-03-06');
  C.pauseHabit(h, '2026-03-03'); C.resumeHabit(h, '2026-03-05'); // paused 3rd-4th
  assert.ok(!C.isScheduled(h, '2026-03-03') && !C.isScheduled(h, '2026-03-04') && C.isScheduled(h, '2026-03-05'));
  C.setCheck(d, h, '2026-03-05', true, '2026-03-06'); assert.strictEqual(C.currentStreak(d, h, '2026-03-06'), 3);
  assert.ok(C.getEntry(d, h, '2026-03-01'));
});
t('one-time activity is scheduled only on its date', () => {
  const h = H({ start: '2026-03-04', sched: { kind: 'once' } }); assert.ok(C.isScheduled(h, '2026-03-04') && !C.isScheduled(h, '2026-03-05'));
});
t('N times per week: judged per week, never "missed" per day', () => {
  const d = D(), h = H({ start: '2026-03-02', sched: { kind: 'times', n: 3, per: 'week' } }); d.habits.push(h); // weeks start Monday
  ['2026-03-02', '2026-03-04', '2026-03-06', '2026-03-09', '2026-03-10', '2026-03-12'].forEach(x => C.setCheck(d, h, x, true, '2026-03-17'));
  assert.strictEqual(C.status(d, h, '2026-03-03', '2026-03-17'), 'open');
  assert.strictEqual(C.currentStreak(d, h, '2026-03-17'), 2);   // current week (16-22) still in progress
  const r = C.rate(d, h, '2026-03-02', '2026-03-17', '2026-03-17'); assert.deepStrictEqual([r.done, r.total], [2, 2]);
  assert.deepStrictEqual(C.periodProgress(d, h, '2026-03-17').done, 0);
});
t('week start setting changes weekly periods', () => {
  const d = D(); d.settings.weekStart = 0; const h = H({ sched: { kind: 'times', n: 1, per: 'week' } });
  assert.strictEqual(C.periodRange(d, h, '2026-03-04').from, '2026-03-01');
});
t('checklist habit is done only when every step is done', () => {
  const d = D(), h = H({ check: [{ id: 'a', t: 'Wake' }, { id: 'b', t: 'Bed' }] }); d.habits.push(h);
  C.setItem(d, h, '2026-03-05', 'a', true, '2026-03-05'); assert.strictEqual(C.status(d, h, '2026-03-05', '2026-03-05'), 'partial');
  C.setItem(d, h, '2026-03-05', 'b', true, '2026-03-05'); assert.strictEqual(C.status(d, h, '2026-03-05', '2026-03-05'), 'done');
  C.setItem(d, h, '2026-03-05', 'a', false, '2026-03-05'); assert.strictEqual(C.status(d, h, '2026-03-05', '2026-03-05'), 'partial');
  assert.strictEqual(C.status(d, h, '2026-03-06', '2026-03-06'), 'pending'); // resets next day
});
t('quit habit: occurrence is a setback, successful day must be recorded', () => {
  const d = D(), h = H({ type: 'quit' }); d.habits.push(h);
  C.setClean(d, h, '2026-03-01', true, '2026-03-03'); C.addOccurrence(d, h, '2026-03-02', 'stress', '2026-03-03');
  assert.strictEqual(C.status(d, h, '2026-03-02', '2026-03-03'), 'slip');
  assert.throws(() => C.setClean(d, h, '2026-03-02', true, '2026-03-03'), /occurrence/);
  C.removeOccurrence(d, h, '2026-03-02'); C.setClean(d, h, '2026-03-02', true, '2026-03-03');
  assert.strictEqual(C.currentStreak(d, h, '2026-03-03'), 2);
});
t('reduce habit: within the daily limit can still be a successful day', () => {
  const d = D(), h = H({ type: 'reduce', goal: { kind: 'check', limit: 2 } }); d.habits.push(h);
  C.addOccurrence(d, h, '2026-03-02', '', '2026-03-03'); C.setClean(d, h, '2026-03-02', true, '2026-03-03');
  assert.strictEqual(C.status(d, h, '2026-03-02', '2026-03-03'), 'done');
  C.addOccurrence(d, h, '2026-03-02', '', '2026-03-03'); C.addOccurrence(d, h, '2026-03-02', '', '2026-03-03');
  assert.strictEqual(C.status(d, h, '2026-03-02', '2026-03-03'), 'slip');
});
t('goal progress counts each habit and each day once', () => {
  const d = D(), h = H({ goal: { kind: 'count', target: 10, unit: 'pages' } }); d.habits.push(h);
  C.setValue(d, h, '2026-03-02', 12, '2026-03-04'); C.setValue(d, h, '2026-03-03', 8, '2026-03-04');
  const g = { id: 'g', period: 'custom', start: '2026-03-01', due: '2026-03-31', target: 100, habitIds: ['h1', 'h1'], log: [{ date: '2026-03-03', v: 5 }], ms: [{ id: 'm', t: 'Quarter', at: 25 }] };
  const p = C.goalProgress(d, g, '2026-03-04'); assert.deepStrictEqual([p.sum, p.pct, p.remaining, p.milestones[0].ok], [25, 25, 75, true]);
});
t('migration upgrades old data without losing records', () => {
  const old = { habits: [{ id: 'x', name: 'Old', start: '2026-01-01' }], entries: { 'x|2026-01-02': { st: 'done' } }, cats: ['Health'] };
  const m = C.migrate(old); assert.strictEqual(m.cats[0].name, 'Health'); assert.strictEqual(m.habits[0].sched.kind, 'daily'); assert.ok(m.entries['x|2026-01-02']);
});
t('changing a schedule does not rewrite past days', () => {
  const d = D(), h = H({ start: '2026-03-01' }); d.habits.push(h);
  C.setCheck(d, h, '2026-03-02', true, '2026-03-10'); // Monday under the old daily schedule
  C.changeSchedule(h, { kind: 'weekly', days: [5] }, '2026-03-10'); // Fridays only from 10 Mar
  assert.ok(C.isScheduled(h, '2026-03-03'));            // old Tuesday still scheduled (and missed)
  assert.ok(!C.isScheduled(h, '2026-03-11') && C.isScheduled(h, '2026-03-13'));
  assert.strictEqual(C.status(d, h, '2026-03-02', '2026-03-10'), 'done');
});
t('explicit failed status counts as missed and breaks the streak', () => {
  const d = D(), h = H(); d.habits.push(h);
  C.setCheck(d, h, '2026-03-01', true, '2026-03-03'); C.setFail(d, h, '2026-03-02', true, '2026-03-03');
  assert.strictEqual(C.status(d, h, '2026-03-02', '2026-03-03'), 'failed'); assert.strictEqual(C.currentStreak(d, h, '2026-03-03'), 0);
  C.setFail(d, h, '2026-03-03', true, '2026-03-03'); assert.strictEqual(C.dayCompletion(d, '2026-03-03', '2026-03-03').missed.length, 1);
});
t('reminders can differ by weekday and use a custom message', () => {
  const d = D(), h = H({ rem: { on: true, times: ['08:00'], byDay: { 6: ['10:00'], 0: ['10:00'] }, msg: 'Go!' } }); d.habits.push(h);
  const r = C.upcomingReminders(d, new Date(2026, 2, 6, 9, 0), 3); // Fri 9:00 -> Sat 10:00, Sun 10:00
  assert.deepStrictEqual(r.map(x => new Date(x.ts).getHours()), [10, 10]); assert.strictEqual(r[0].text, 'Go!');
});
console.log('\n' + n + ' tests passed' + (process.exitCode ? ' (with failures)' : ''));
