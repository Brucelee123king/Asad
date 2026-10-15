/* End-to-end checks in a phone-sized Chromium.
   Run:  cd android_app && python3 build_assets.py && NODE_PATH=$(npm root -g) node habitflow/tests/e2e.test.js
   Needs the Playwright package and a Chromium (PW_CHROMIUM=/path/to/chrome to override). */
const { chromium } = require('playwright');
const path = require('path');
const A = 'file://' + path.resolve(__dirname, '../../app/src/main/assets') + '/';
let pass = 0, fail = 0; const errs = [];
const ok = (c, name, extra) => { if (c) { pass++; console.log('ok   -', name); } else { fail++; console.log('FAIL -', name, extra || ''); } };

(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_CHROMIUM || '/opt/pw-browsers/chromium' });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
  const p = await ctx.newPage();
  p.on('pageerror', e => errs.push(e.message));
  p.on('console', m => { if (m.type() === 'error' && !/vibrate/.test(m.text())) errs.push(m.text()); });
  const wait = ms => p.waitForTimeout(ms || 120);
  const ev = (f, a) => p.evaluate(f, a);

  /* ---- account ---- */
  await p.goto(A + 'index.html');
  await p.click('#mode'); await p.fill('#user', 'tester'); await p.fill('#pass', 'abc'); await p.click('#go');
  ok(/8 characters/.test(await p.textContent('#msg')), 'weak password rejected');
  await p.fill('#pass', 'secure123'); await p.click('#go'); await wait(300);
  const code = (await p.textContent('.code')).trim();
  ok(/^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$/.test(code), 'recovery code shown');
  await p.click('#cont'); await p.waitForURL('**/app.html');
  ok(await p.locator('[data-act=obnext]').count() > 0, 'onboarding shown to new user');
  await p.click('[data-act=obskip]'); await wait(200);
  ok(/Welcome to HabitFlow/.test(await p.textContent('main')), 'empty state for new user');

  /* ---- seed one habit of every kind through the real API ---- */
  await ev(() => {
    const t = App.tdy(), D = App.D, mk = (o, i) => Object.assign({ id: 'h' + i, created: Date.now(), start: Core.addDays(t, -20), icon: '⭐', color: '#2f6bff', type: 'build', goal: { kind: 'check' }, sched: { kind: 'daily' }, part: 'morning', cats: ['health'], check: [], rem: { on: true, times: ['23:59'], byDay: {}, msg: '' }, order: i }, o);
    [{ name: 'Check' }, { name: 'Water', goal: { kind: 'count', target: 8, unit: 'glasses', step: 1 } }, { name: 'Study', goal: { kind: 'time', target: 30, unit: 'min' }, part: 'evening' },
     { name: 'Routine', check: [{ id: 'a', t: 'One' }, { id: 'b', t: 'Two' }] }, { name: 'Gym', sched: { kind: 'times', n: 3, per: 'week' } }, { name: 'Smoking', type: 'quit' },
     { name: 'Coffee', type: 'reduce', goal: { kind: 'check', limit: 2, unit: 'cups' } }, { name: 'Run', sched: { kind: 'weekly', days: [1, 3, 5] } }].forEach((o, i) => D.habits.push(mk(o, i)));
    Core.range(Core.addDays(t, -20), Core.addDays(t, -1)).forEach((d, k) => { if (k % 4) Core.setCheck(D, D.habits[0], d, true, t); });
    D.goals.push({ id: 'g1', name: 'Hydrate', period: 'weekly', target: 40, unit: 'glasses', start: t, due: t, habitIds: ['h1'], ms: [{ id: 'm', t: 'Half', at: 20 }], log: [] });
    D.challenges.push({ id: 'c1', name: '7-day Check', habitId: 'h0', days: 7, start: Core.addDays(t, -3) });
    D.journal.push({ id: 'j1', date: t, kind: 'daily', text: 'Hello #world', tags: ['world'], ts: Date.now(), mood: 4 });
    D.moods.push({ id: 'm1', date: t, ts: Date.now(), mood: 4, note: '' });
    D.focus.push({ id: 'f1', ts: Date.now(), date: t, secs: 1500, mode: 'timer', label: '', hid: 'h2' });
    App.save(); App.go('home');
  });

  /* ---- streak / progress numbers shown match core ---- */
  const streak = await ev(() => Core.currentStreak(App.D, App.D.habits[0], App.tdy()));
  ok(streak === 3, 'streak calc (every 4th day missing → 3)', streak);

  /* ---- tap every control on every screen ---- */
  const routes = [['tab', 'home'], ['tab', 'journal'], ['tab', 'progress'], ['tab', 'focus'], ['tab', 'settings'],
    ['seg', 'journal', 'notes'], ['seg', 'journal', 'mood'], ['seg', 'jview', 'week'], ['seg', 'jview', 'month'],
    ['seg', 'progress', 'calendar'], ['seg', 'progress', 'goals'], ['seg', 'progress', 'habits'],
    ['push', 'habitForm'], ['push', 'library'], ['push', 'habit', { id: 'h3' }], ['push', 'habit', { id: 'h5' }], ['push', 'habit', { id: 'h4' }],
    ['push', 'goal', { id: 'g1' }], ['push', 'goalForm'], ['push', 'challengeForm'], ['push', 'entry', { id: 'j1' }], ['push', 'assistant'],
    ['push', 'appearance'], ['push', 'profile'], ['push', 'notifs'], ['push', 'cats'], ['push', 'sections'], ['push', 'order'], ['push', 'archived'],
    ['push', 'data'], ['push', 'integrations'], ['push', 'plans'], ['push', 'help'], ['push', 'legal', { doc: 'privacy' }], ['push', 'classic']];
  const SKIP = /^(signout|delall|delacct|del|gdel|cdel|fdel|moodDel|restore)$/;
  let tapped = 0, broken = [];
  const open = r => ev(r => { UI.closeSheet(); App.D.settings.onboarded = true; App.ui.date = App.tdy(); App.ui.f = {}; App.ui.stack = []; App.ui.seg = {}; if (r[0] === 'tab') App.go(r[1]); else if (r[0] === 'seg') { const tab = { journal: 'journal', jview: 'journal', progress: 'progress' }[r[1]]; if (r[1] === 'jview') App.ui.seg.journal = 'checkin'; App.ui.seg[r[1]] = r[2]; App.go(tab); } else { App.go('home'); App.push(r[1], r[2] || {}); } }, r);
  for (const r of routes) {
    await open(r); await wait(60);
    const n = await p.locator('main [data-act]').count();
    for (let i = 0; i < n; i++) {
      await open(r); await wait(30);
      const el = p.locator('main [data-act]').nth(i);
      if (!(await el.count())) continue;
      const act = await el.getAttribute('data-act');
      if (SKIP.test(act) || act === 'tab' || !(await el.isVisible()) || await el.isDisabled()) continue;
      const before = errs.length;
      try { await el.click({ timeout: 1500 }); } catch (e) { continue; }
      await wait(60); tapped++;
      const txt = await p.textContent('body');
      if (errs.length > before || /Something went wrong|Screen not found/.test(txt)) broken.push(r.join(':') + ' → ' + act + ' ' + errs.slice(before).join(' | '));
      await ev(() => UI.closeSheet());
    }
  }
  ok(broken.length === 0, 'tapped ' + tapped + ' controls on ' + routes.length + ' screens without errors', '\n  ' + broken.join('\n  '));

  /* ---- check-in, undo, add/set ---- */
  await ev(() => { const t = App.tdy(); Object.keys(App.D.entries).forEach(k => { if (k.endsWith('|' + t)) delete App.D.entries[k]; }); App.save(); });
  await open(['tab', 'home']);
  const done0 = await ev(() => Core.dayCompletion(App.D, App.tdy(), App.tdy()).done);
  await p.locator('.ck[data-h=h0]').click(); await wait();
  ok(await ev(() => Core.status(App.D, App.habit('h0'), App.tdy(), App.tdy())) === 'done', 'one-tap complete');
  await p.click('.toast button'); await wait();
  ok(await ev(() => Core.dayCompletion(App.D, App.tdy(), App.tdy()).done) === done0, 'undo restores state');
  await ev(() => App.logSheet(App.habit('h1'), App.tdy())); await p.fill('#lv', '2'); await p.click('#ladd'); await wait();
  await ev(() => App.logSheet(App.habit('h1'), App.tdy())); await p.fill('#lv', '3'); await p.click('#ladd'); await wait();
  ok(await ev(() => Core.getEntry(App.D, App.habit('h1'), App.tdy()).v) === 5, 'Add 2 then Add 3 = 5');
  await ev(() => App.logSheet(App.habit('h1'), App.tdy())); await p.fill('#lv', '3'); await p.click('#lset'); await wait();
  ok(await ev(() => Core.getEntry(App.D, App.habit('h1'), App.tdy()).v) === 3, 'Set 3 = 3');

  /* ---- create, edit, archive, delete through the UI ---- */
  await ev(() => { App.go('home'); App.push('habitForm'); });
  await p.click('[data-act=save]'); ok(/name/.test(await p.textContent('#ferr')), 'empty name blocked');
  await p.fill('#hn', 'Stretch'); await p.click('[data-act=save]'); await wait(200);
  const sid = await ev(() => (App.D.habits.find(h => h.name === 'Stretch') || {}).id);
  ok(!!sid, 'habit created via form');
  await ev(id => App.push('habitForm', { id }), sid); await p.fill('#hn', 'Stretch daily'); await p.click('[data-act=save]'); await wait(200);
  ok(await ev(id => App.habit(id).name, sid) === 'Stretch daily', 'habit edited');
  await ev(id => App.push('habit', { id }), sid); await p.click('[data-act=arch]'); await wait();
  ok(await ev(id => App.habit(id).archived, sid) === true, 'habit archived (history kept)');
  await p.click('[data-act=del]'); await wait(); await p.click('#cOk'); await wait(200);
  ok(await ev(id => !App.habit(id), sid), 'habit deleted after confirmation');

  /* ---- back navigation ---- */
  await ev(() => { App.go('home'); App.push('habit', { id: 'h0' }); App.push('habitForm', { id: 'h0' }); });
  ok(await ev(() => App.handleBack()) === true && await ev(() => App.ui.stack.length) <= 2, 'back pops a screen'); await wait(150);
  await ev(() => App.moreSheet(App.habit('h0'), App.tdy()));
  ok(await ev(() => App.handleBack()) === true && await p.locator('.scrim').count() === 0, 'back closes an open sheet first');
  await ev(() => { App.ui.stack = []; App.go('progress'); });
  ok(await ev(() => App.handleBack()) === true && await ev(() => App.ui.tab) === 'home', 'back from another tab goes Home');
  ok(await ev(() => App.handleBack()) === false, 'back on Home leaves the app');

  /* ---- theme, persistence ---- */
  await ev(() => { App.push('appearance'); }); await p.click('[data-seg=theme][data-v=dark]'); await wait();
  ok(await ev(() => document.documentElement.dataset.theme) === 'dark', 'dark theme applies');
  const snap = await ev(() => JSON.stringify(App.D));
  await p.reload(); await wait(400);
  ok(await ev(() => JSON.stringify(App.D)) === snap, 'all data identical after restart');
  ok(await ev(() => document.documentElement.dataset.theme) === 'dark', 'theme persists after restart');

  /* ---- backup round trip ---- */
  const backup = await ev(() => JSON.stringify(App.D));
  await ev(() => { App.D = Core.newData(); App.D.settings.onboarded = true; App.save(); });
  await ev(b => { App.D = Core.validateImport(JSON.parse(b)); App.save(); }, backup);
  ok(await ev(() => App.D.habits.length) === JSON.parse(backup).habits.length, 'backup restore round trip');

  /* ---- sign out / login / reset ---- */
  await ev(() => { localStorage.removeItem('ht.session'); }); await p.goto(A + 'index.html');
  await p.fill('#user', 'tester'); await p.fill('#pass', 'wrong999'); await p.click('#go');
  ok(/Wrong password/.test(await p.textContent('#msg')), 'wrong password rejected');
  await p.click('#forgot'); await p.fill('#fu', 'tester'); await p.fill('#fc', code); await p.fill('#fp', 'newpass99'); await p.click('#fgo');
  ok(/updated/.test(await p.textContent('#msg')), 'password reset with recovery code');
  await p.fill('#user', 'TESTER'); await p.fill('#pass', 'newpass99'); await p.click('#go'); await p.waitForURL('**/app.html'); await wait(300);
  ok(await ev(() => App.D.habits.length) > 0, 'login restores the same data');
  ok(errs.length === 0, 'no JavaScript errors during the run', errs.join(' | '));
  console.log('\n' + pass + ' passed, ' + fail + ' failed');
  await b.close(); process.exitCode = fail ? 1 : 0;
})();
