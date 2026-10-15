/* HabitFlow app shell: storage, routing, global actions, native bridge */
const Screens = window.Screens || (window.Screens = {});
const App = (() => {
  const $ = (s, r) => (r || document).querySelector(s);
  /* ---------- session & storage ---------- */
  let sess = null;
  try { sess = JSON.parse(localStorage.getItem('ht.session') || sessionStorage.getItem('ht.session') || 'null'); } catch (e) { }
  if (!sess) { location.replace('index.html'); }
  const KEY = (window.__u || 'guest::') + 'habitflow.v2';
  let D;
  (function load() {
    let raw = null; try { raw = localStorage.getItem(KEY); } catch (e) { }
    if (!raw) { D = Core.newData(); return; }
    try { D = Core.migrate(JSON.parse(raw)); }
    catch (e) { // never silently discard: keep the unreadable copy and start fresh
      try { localStorage.setItem(KEY + '.unreadable.' + Date.now(), raw); } catch (x) { }
      D = Core.newData(); setTimeout(() => UI.toast('Saved data could not be read. A copy was kept; you can export it from Settings > Data.', { err: 1, ms: 7000 }), 600);
    }
  })();
  let syncT = null;
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(D)); }
    catch (e) { UI.toast('Could not save: device storage is full. Export a backup and free up space.', { err: 1, ms: 7000 }); return false; }
    clearTimeout(syncT); syncT = setTimeout(syncNative, 700); return true;
  }
  const tdy = () => Core.todayStr();

  /* ---------- UI state & routing ---------- */
  const ui = { tab: 'home', stack: [], date: tdy(), seg: {}, f: {} };
  try { const t = sessionStorage.getItem('hf.tab'); if (t) ui.tab = t; } catch (e) { }
  const cur = () => !D.settings.onboarded ? { s: 'onboarding', p: {} } : ui.stack.length ? ui.stack[ui.stack.length - 1] : { s: ui.tab, p: {} };
  function go(tab) { ui.tab = tab; ui.stack = []; try { sessionStorage.setItem('hf.tab', tab); } catch (e) { } render(); window.scrollTo(0, 0); }
  function push(s, p) { ui.stack.push({ s, p: p || {} }); if (!window.Android) try { history.pushState({ n: ui.stack.length }, ''); } catch (e) { } render(); window.scrollTo(0, 0); }
  function back() { if (document.querySelector('.scrim')) { UI.closeSheet(); return; } if (!ui.stack.length) return; if (window.Android) handleBack(); else history.back(); }
  window.addEventListener('popstate', () => { if (document.querySelector('.scrim')) UI.closeSheet(); if (ui.stack.length) { ui.stack.pop(); render(); } });
  /* Android back button: sheet → screen → Home tab → leave the app (returns false) */
  function handleBack() {
    if (document.querySelector('.scrim')) { UI.closeSheet(); return true; }
    if (!D.settings.onboarded) return false;
    if (ui.stack.length) { ui.stack.pop(); render(); window.scrollTo(0, 0); return true; }
    if (ui.tab !== 'home') { go('home'); return true; }
    return false;
  }
  function replaceTop(s, p) { ui.stack[ui.stack.length - 1] = { s, p: p || {} }; render(); }

  /* ---------- theme ---------- */
  const mq = window.matchMedia ? matchMedia('(prefers-color-scheme: dark)') : null;
  function applyTheme() {
    const s = D.settings, r = document.documentElement;
    r.dataset.theme = s.theme === 'system' ? (mq && mq.matches ? 'dark' : 'light') : s.theme;
    r.style.setProperty('--ac', s.accent); r.style.setProperty('--ts', s.textScale || 1);
    const hex = s.accent.replace('#', ''), lum = (parseInt(hex.substr(0, 2), 16) * 299 + parseInt(hex.substr(2, 2), 16) * 587 + parseInt(hex.substr(4, 2), 16) * 114) / 1000;
    r.style.setProperty('--ac-tx', lum > 170 ? '#111' : '#fff');
    r.classList.toggle('compact', s.density === 'compact'); r.dataset.chart = s.chartStyle || 'rounded';
  }
  if (mq && mq.addEventListener) mq.addEventListener('change', () => render());

  /* ---------- render ---------- */
  const NAV = [['home', 'Home', 'home'], ['journal', 'Journal', 'journal'], ['progress', 'Progress', 'progress'], ['focus', 'Focus', 'focus'], ['settings', 'Settings', 'settings']];
  function render() {
    applyTheme();
    const main = $('#main'), nav = $('#nav');
    if (!D.settings.onboarded) { nav.hidden = true; main.innerHTML = Screens.onboarding.render(); Screens.onboarding.mount && Screens.onboarding.mount(main); return; }
    nav.hidden = false;
    nav.innerHTML = `<div class="brand"><img src="icon.png" alt="">HabitFlow</div>` + NAV.map(n => `<button data-act="tab" data-v="${n[0]}" class="${!ui.stack.length && ui.tab === n[0] ? 'on' : ''}" aria-current="${ui.tab === n[0]}">${UI.icon(n[2], 22)}<span>${n[1]}</span></button>`).join('');
    const c = cur(), S = Screens[c.s];
    if (!S) { main.innerHTML = UI.empty('\u{1F9ED}', 'Screen not found', 'Go back and try again.'); return; }
    try { main.innerHTML = S.render(c.p); if (S.mount) S.mount(main, c.p); }
    catch (e) { console.error(e); main.innerHTML = `<div class="card">${UI.empty('⚠️', 'Something went wrong', 'This screen could not be shown. Your data is safe.', '<button class="btn" data-act="tab" data-v="home">Go home</button>')}</div>`; }
  }

  /* ---------- mutations with undo ---------- */
  function act(fn, msg, o) {
    o = o || {}; const snap = JSON.stringify(D); let r;
    try { r = fn(); } catch (e) { UI.toast(e.message || 'Something went wrong.', { err: 1 }); return false; }
    if (!save()) { D = Core.migrate(JSON.parse(snap)); return false; }
    render();
    if (msg) UI.toast(msg, o.noUndo ? {} : { action: 'Undo', onAction: () => { D = Core.migrate(JSON.parse(snap)); save(); render(); UI.toast('Undone'); } });
    return r === undefined ? true : r;
  }
  const habit = id => D.habits.find(h => h.id === id);
  const cat = id => D.cats.find(c => c.id === id);

  /* ---------- habit actions (used by Home, Journal, details) ---------- */
  function nextStacked(h, date) {
    const nx = D.habits.find(x => !x.archived && x.stack === h.id && Core.status(D, x, date, tdy()) === 'pending');
    return nx ? ' Next up: ' + nx.name : '';
  }
  function unitLabel(h) { return Core.goalKind(h) === 'time' ? 'min' : (h.goal.unit || ''); }
  function logSheet(h, date) {
    const e = Core.getEntry(D, h, date), curV = (e && e.v) || 0;
    UI.sheet(`<h3>${UI.esc(h.icon + ' ' + h.name)}</h3><p class="muted small" style="margin-bottom:12px">${UI.fmtDate(date, D.settings.dateFmt, true)} · recorded <b>${curV}</b> of ${Core.target(h)} ${UI.esc(unitLabel(h))}</p>
      <div class="fld"><label for="lv">Amount (${UI.esc(unitLabel(h))})</label><input class="inp" id="lv" type="number" inputmode="decimal" min="0" step="any" autofocus></div>
      <div class="err" id="le"></div><div class="row"><button class="btn sec grow" id="lset">Set to this</button><button class="btn grow" id="ladd">Add</button></div>
      <p class="hint" style="margin-top:10px">Add puts the amount on top of what you recorded (2 + 3 = 5). Set replaces it (Set 3 = 3).</p>`, sh => {
      const val = () => { const v = parseFloat(sh.querySelector('#lv').value); if (isNaN(v) || v < 0) { sh.querySelector('#le').textContent = 'Enter a number of 0 or more.'; return null; } return v; };
      sh.querySelector('#ladd').onclick = () => { const v = val(); if (v == null) return; UI.closeSheet(); act(() => Core.addValue(D, h, date, v, tdy()), 'Added ' + v + ' ' + unitLabel(h) + '.' + nextStacked(h, date)); };
      sh.querySelector('#lset').onclick = () => { const v = val(); if (v == null) return; UI.closeSheet(); act(() => Core.setValue(D, h, date, v, tdy()), 'Set to ' + v + ' ' + unitLabel(h) + '.'); };
    });
  }
  function stepsSheet(h, date) {
    const draw = sh => { const e = Core.getEntry(D, h, date), chk = (e && e.chk) || [];
      sh.innerHTML = `<div class="grab"></div><h3>${UI.esc(h.icon + ' ' + h.name)}</h3><p class="muted small" style="margin-bottom:8px">${chk.length} of ${h.check.length} steps done</p>${UI.pbar(chk.length / h.check.length * 100, h.color)}
        <div class="list" style="margin-top:8px">${h.check.map(c => `<button class="li" data-step="${c.id}"><span class="ck ${chk.indexOf(c.id) >= 0 ? 'on' : ''}" style="--hcol:${h.color}">${UI.icon('check', 20)}</span><span class="grow t">${UI.esc(c.t)}</span></button>`).join('')}</div>
        <button class="btn full mt" id="sdone">Done</button>`;
      sh.querySelectorAll('[data-step]').forEach(b => b.onclick = () => { const id = b.dataset.step, on = !((Core.getEntry(D, h, date) || {}).chk || []).includes(id);
        try { Core.setItem(D, h, date, id, on, tdy()); save(); render(); draw(sh); } catch (er) { UI.toast(er.message, { err: 1 }); } });
      sh.querySelector('#sdone').onclick = UI.closeSheet; };
    UI.sheet('', draw);
  }
  function noteSheet(h, date) {
    const e = Core.getEntry(D, h, date);
    UI.sheet(`<h3>Note · ${UI.esc(h.name)}</h3><p class="muted small" style="margin-bottom:10px">${UI.fmtDate(date, D.settings.dateFmt, true)}</p><textarea class="inp" id="nt" maxlength="500" placeholder="How did it go? What helped or got in the way?" autofocus>${UI.esc((e && e.note) || '')}</textarea><button class="btn full mt" id="ns">Save note</button>`,
      sh => sh.querySelector('#ns').onclick = () => { const v = sh.querySelector('#nt').value; UI.closeSheet(); act(() => Core.setNote(D, h, date, v), v.trim() ? 'Note saved.' : 'Note removed.'); });
  }
  function occSheet(h, date) {
    UI.sheet(`<h3>Record an occurrence</h3><p class="muted small" style="margin-bottom:12px">Setbacks are part of change. Noting what led to it helps you spot patterns.</p>
      <div class="fld"><label for="ot">What was going on? (optional)</label><input class="inp" id="ot" maxlength="200" placeholder="e.g. stressed, bored, with friends" autofocus></div>
      <div class="chips" style="margin-bottom:14px">${['Stress', 'Boredom', 'Tired', 'Social', 'Habit cue', 'Craving'].map(x => `<button class="chip" data-tr="${x}">${x}</button>`).join('')}</div>
      <button class="btn full" id="os">Record</button>`, sh => {
      sh.querySelectorAll('[data-tr]').forEach(b => b.onclick = () => { sh.querySelector('#ot').value = b.dataset.tr; });
      sh.querySelector('#os').onclick = () => { const v = sh.querySelector('#ot').value; UI.closeSheet(); act(() => Core.addOccurrence(D, h, date, v, tdy()), 'Recorded. Be kind to yourself; tomorrow is a fresh start.'); };
    });
  }
  function moreSheet(h, date) {
    const st = Core.status(D, h, date, tdy()), neg = Core.isNegative(h), kind = Core.goalKind(h), e = Core.getEntry(D, h, date), future = date > tdy();
    const o = (id, ic, label, cls) => `<button class="opt ${cls || ''}" data-o="${id}">${UI.icon(ic)}<span>${label}</span></button>`;
    let h2 = `<h3>${UI.esc(h.icon + ' ' + h.name)}</h3><p class="muted small" style="margin-bottom:6px">${UI.fmtDate(date, D.settings.dateFmt, true)} · ${UI.badge(st)}${e && e.at ? ' · at ' + new Date(e.at).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' }) : ''}</p>`;
    if (!future && st !== 'off') {
      if (neg) { h2 += o('clean', 'check', st === 'done' ? 'Undo successful day' : 'Record successful day') + o('occ', 'plus', 'Record an occurrence'); if (e && e.n) h2 += o('unocc', 'minus', 'Remove last occurrence (' + e.n + ')'); }
      else {
        h2 += o('done', 'check', st === 'done' ? 'Mark as not completed' : 'Mark complete');
        if (kind !== 'check') h2 += o('log', 'plus', 'Add or set progress');
        if (Core.checkItems(h)) h2 += o('steps', 'grid', 'Checklist steps');
        if (!Core.isFlex(h, date)) h2 += o('fail', 'x', st === 'failed' ? 'Clear "not done"' : 'Mark as not done today');
      }
      if (!Core.isFlex(h, date)) h2 += o('skip', 'skip', st === 'skip' ? 'Remove skip' : 'Skip (rest day, keeps streak)');
      h2 += o('note', 'note', e && e.note ? 'Edit note' : 'Add note');
    } else if (future) h2 += `<p class="hint" style="margin:6px 0 10px">Future days can be viewed but not recorded.</p>`;
    h2 += o('detail', 'progress', 'Statistics & history') + o('edit', 'edit', 'Edit habit');
    UI.sheet(h2, sh => sh.querySelectorAll('[data-o]').forEach(b => b.onclick = () => {
      const k = b.dataset.o; UI.closeSheet();
      if (k === 'done') act(() => Core.setCheck(D, h, date, st !== 'done', tdy()), st !== 'done' ? 'Completed!' + nextStacked(h, date) : 'Marked as not completed.');
      if (k === 'clean') act(() => Core.setClean(D, h, date, st !== 'done', tdy()), st !== 'done' ? 'Successful day recorded. Well done.' : 'Cleared.');
      if (k === 'occ') occSheet(h, date);
      if (k === 'unocc') act(() => Core.removeOccurrence(D, h, date), 'Occurrence removed.');
      if (k === 'log') logSheet(h, date);
      if (k === 'steps') stepsSheet(h, date);
      if (k === 'fail') act(() => Core.setFail(D, h, date, st !== 'failed', tdy()), st !== 'failed' ? 'Recorded. Tomorrow is a new chance.' : 'Cleared.');
      if (k === 'skip') act(() => Core.setSkip(D, h, date, st !== 'skip', tdy()), st !== 'skip' ? 'Skipped. Your streak is safe.' : 'Skip removed.');
      if (k === 'note') noteSheet(h, date);
      if (k === 'detail') push('habit', { id: h.id });
      if (k === 'edit') push('habitForm', { id: h.id });
    }));
  }

  /* ---------- global click / change / input delegation ---------- */
  const G = {
    tab: t => go(t.dataset.v), back: () => back(),
    go: t => { const p = Object.assign({}, t.dataset); delete p.act; delete p.s; push(t.dataset.s, p); },
    seg: t => { ui.seg[t.dataset.seg] = t.dataset.v; render(); },
    hcheck: t => { const h = habit(t.dataset.h), date = t.dataset.d || tdy(); if (!h) return;
      if (date > tdy()) { UI.toast('Future days can be viewed but not recorded.'); return; }
      const st = Core.status(D, h, date, tdy());
      if (Core.isNegative(h)) { if (st === 'slip') { UI.toast('An occurrence is recorded today. Open ⋯ to change it.'); return; } act(() => Core.setClean(D, h, date, st !== 'done', tdy()), st !== 'done' ? 'Successful day recorded. Well done.' : 'Cleared.'); return; }
      if (st === 'skip') { act(() => Core.setSkip(D, h, date, false, tdy()), 'Skip removed.'); return; }
      act(() => Core.setCheck(D, h, date, st !== 'done', tdy()), st !== 'done' ? 'Completed!' + nextStacked(h, date) : 'Marked as not completed.');
      if (st !== 'done' && navigator.vibrate) try { navigator.vibrate(12); } catch (e) { } },
    hinc: t => { const h = habit(t.dataset.h), date = t.dataset.d || tdy(); if (!h) return; const step = Core.goalKind(h) === 'time' ? 5 : (h.goal.step || 1);
      act(() => Core.addValue(D, h, date, step, tdy()), '+' + step + ' ' + unitLabel(h) + (Core.status(D, h, date, tdy()) === 'done' ? ' · Goal reached!' + nextStacked(h, date) : '')); },
    hlog: t => logSheet(habit(t.dataset.h), t.dataset.d || tdy()),
    hsteps: t => stepsSheet(habit(t.dataset.h), t.dataset.d || tdy()),
    hocc: t => { const d = t.dataset.d || tdy(); if (d > tdy()) { UI.toast('Future days can be viewed but not recorded.'); return; } occSheet(habit(t.dataset.h), d); },
    hmore: t => moreSheet(habit(t.dataset.h), t.dataset.d || tdy()),
    hopen: t => push('habit', { id: t.dataset.h })
  };
  document.addEventListener('click', e => {
    const t = e.target.closest('[data-act]'); if (!t || t.disabled) return;
    const n = t.dataset.act, S = Screens[cur().s] || {}, f = (S.acts && S.acts[n]) || G[n];
    if (f) { e.preventDefault(); f(t, e); }
  });
  ['change', 'input'].forEach(type => document.addEventListener(type, e => {
    const t = e.target.closest('[data-' + type + ']'); if (!t) return;
    const n = t.dataset[type], S = Screens[cur().s] || {}, f = (S[type + 's'] && S[type + 's'][n]) || (type === 'change' && G[n]);
    if (f) f(t, e);
  }));

  /* ---------- native bridge (Android) ---------- */
  const N = window.Android || null;
  function syncNative() {
    if (!N) return;
    try { if (N.setReminders) N.setReminders(JSON.stringify(D.settings.notif ? Core.upcomingReminders(D, new Date(), 14, 60) : [])); } catch (e) { }
    try { if (N.updateWidget) { const c = Core.dayCompletion(D, tdy(), tdy()); let best = 0; Core.live(D).forEach(h => best = Math.max(best, Core.currentStreak(D, h, tdy())));
      N.updateWidget(JSON.stringify({ date: tdy(), pct: c.pct, done: c.done, total: c.total, next: c.remaining.slice(0, 3).map(h => h.icon + ' ' + h.name), streak: best })); } } catch (e) { }
  }
  function takeNativeActions() {
    if (!N || !N.takeActions) return; let list = []; try { list = JSON.parse(N.takeActions() || '[]'); } catch (e) { return; }
    let n = 0; list.forEach(a => { const h = habit(a.hid); if (!h) return; try { if (Core.isNegative(h)) Core.setClean(D, h, a.date, true, tdy()); else Core.setCheck(D, h, a.date, true, tdy()); n++; } catch (e) { } });
    if (n) { save(); render(); UI.toast(n + (n === 1 ? ' habit' : ' habits') + ' marked done from a notification.'); }
  }
  function share(title, text, filename, mime) {
    if (N && N.shareText) { try { const r = String(N.shareText(title, text, filename || 'habitflow.txt', mime || 'text/plain'));
      if (r.indexOf('saved:') === 0) UI.toast('Saved to ' + r.slice(6), { ms: 5000 }); else if (r.indexOf('error:') === 0) UI.toast('Could not export: ' + r.slice(6), { err: 1 }); return; } catch (e) { } }
    try { const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([text], { type: mime || 'text/plain' })); a.download = filename || 'habitflow.txt'; document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500); UI.toast('Downloaded ' + (filename || 'file') + '.'); }
    catch (e) { if (navigator.clipboard) navigator.clipboard.writeText(text).then(() => UI.toast('Copied to clipboard.'), () => UI.toast('Could not export on this device.', { err: 1 })); }
  }

  /* ---------- boot ---------- */
  let lastDay = tdy();
  function boot() {
    try { window.Android && Android.orient('portrait'); } catch (e) { }
    if (!D.settings.name && sess && !sess.guest) D.settings.name = sess.user.split('@')[0];
    const sc = (location.hash || '').slice(1); if (sc) { try { history.replaceState(null, '', location.pathname); } catch (e) { } }
    if (D.settings.onboarded) { if (sc === 'focus' || sc === 'progress') ui.tab = sc; if (sc === 'add') ui.stack = [{ s: 'habitForm', p: {} }]; if (sc === 'journal') ui.stack = [{ s: 'entry', p: {} }]; }
    render(); takeNativeActions(); syncNative();
    setInterval(() => { const t = tdy(); if (t !== lastDay) { if (ui.date === lastDay) ui.date = t; lastDay = t; render(); syncNative(); } if (Screens.focus && Screens.focus.tick) Screens.focus.tick(); }, 1000);
    document.addEventListener('visibilitychange', () => { if (!document.hidden) { takeNativeActions(); render(); syncNative(); } });
  }
  return { get D() { return D; }, set D(v) { D = v; }, ui, sess, tdy, save, render, go, push, back, handleBack, replaceTop, act, habit, cat, share, native: N, syncNative, boot, applyTheme, KEY,
    logSheet, stepsSheet, noteSheet, occSheet, moreSheet, unitLabel };
})();
