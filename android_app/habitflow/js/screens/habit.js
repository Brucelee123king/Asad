/* Habit creation & editing, template library, habit details */
const COLORS = ['#2f6bff', '#0a84ff', '#64d2ff', '#30d158', '#2fbf4f', '#ffd60a', '#ff9f0a', '#ff6b35', '#ff453a', '#ff375f', '#bf5af2', '#5e5ce6', '#ac8e68', '#8e8e93'];
const EMOJI = ['\u{1F4A7}', '\u{1F3C3}', '\u{1F4DA}', '\u{1F9D8}', '\u{1F4AA}', '\u{1F34E}', '\u{1F634}', '✍️', '\u{1F3AF}', '\u{1F4C5}', '\u{1F4BB}', '\u{1F3B8}', '\u{1F3A8}', '\u{1F331}', '☀️', '\u{1F319}', '\u{1F48A}', '\u{1F957}', '\u{1F6AD}', '\u{1F4F5}', '☕', '\u{1F4B0}', '\u{1F9F9}', '❤️'];
Screens.habitForm = (() => {
  const E = s => UI.esc(s); let F = null, key = null;
  function fromHabit(h) {
    const s = h.sched || { kind: 'daily' }; let freq = s.kind;
    if (s.kind === 'weekly') { const d = (s.days || []).slice().sort().join(); freq = d === '1,2,3,4,5' ? 'weekdays' : d === '0,6' ? 'weekends' : d === '0,1,2,3,4,5,6' ? 'daily' : 'days'; }
    return { id: h.id, name: h.name, desc: h.desc || '', icon: h.icon, color: h.color, type: h.type || 'build', track: Core.checkItems(h) ? 'steps' : Core.goalKind(h),
      target: (h.goal && h.goal.target) || 1, unit: (h.goal && h.goal.unit) || '', limit: (h.goal && h.goal.limit) || 0, step: (h.goal && h.goal.step) || 1,
      cats: Core.habitCats(h).slice(), part: h.part || 'anytime', freq, days: (s.days || [1, 3, 5]).slice(), every: s.every || 2, n: s.n || 3, per: s.per || 'week', dom: s.dom || 1,
      start: h.start, end: h.end || '', check: (h.check || []).map(c => Object.assign({}, c)), remOn: !!(h.rem && h.rem.on), times: (h.rem && h.rem.times && h.rem.times.slice()) || ['08:00'],
      byDayOn: !!(h.rem && h.rem.byDay && Object.keys(h.rem.byDay).length), byDay: Object.assign({}, (h.rem && h.rem.byDay) || {}), msg: (h.rem && h.rem.msg) || '', stack: h.stack || '', priority: !!h.priority, notes: h.notes || '' };
  }
  function blank(tpl) {
    const t = App.tdy(), base = { id: '', name: '', desc: '', icon: '⭐', color: '#2f6bff', type: 'build', track: 'check', target: 1, unit: '', limit: 1, step: 1, cats: [], part: 'anytime', freq: 'daily', days: [1, 3, 5], every: 2, n: 3, per: 'week', dom: +t.slice(8),
      start: t, end: '', check: [], remOn: false, times: [App.D.settings.remDefaults ? '08:00' : '08:00'], byDayOn: false, byDay: {}, msg: '', stack: '', priority: false, notes: '' };
    if (!tpl) return base;
    const f = fromHabit({ id: '', name: tpl.name, icon: tpl.icon, color: tpl.color, type: tpl.type, goal: tpl.goal, sched: tpl.sched, part: tpl.part, start: t, check: (tpl.check || []).map((x, i) => ({ id: 'c' + i, t: x })), cats: AREA_TO_CAT[tpl.area] ? [AREA_TO_CAT[tpl.area]] : [] });
    f.dom = +t.slice(8); return f;
  }
  function render(p) {
    const k = (p.id || '') + '|' + (p.tpl || '') + '|' + (p.k || ''); const D = App.D;
    if (key !== k || !F) { key = k; F = p.id ? fromHabit(App.habit(p.id)) : blank(p.tpl && TEMPLATES.find(x => x.id === p.tpl)); }
    const sel = (v, o) => o.map(x => `<option value="${x[0]}" ${String(v) === String(x[0]) ? 'selected' : ''}>${x[1]}</option>`).join('');
    const chip = (k2, v, label, on) => `<button class="chip ${on ? 'on' : ''}" data-act="set" data-k="${k2}" data-v="${E(v)}">${label}</button>`;
    let h = `<div class="top"><button class="ib" data-act="back" aria-label="Cancel">${UI.icon('x')}</button><h1 class="t2">${F.id ? 'Edit habit' : 'New habit'}</h1><button class="btn sm" data-act="save">Save</button></div><div class="stack">`;
    if (!F.id) h += `<button class="card flat row" data-act="go" data-s="library" style="text-align:left"><span style="font-size:1.6rem">\u{1F4DA}</span><span class="grow"><b>Start from a template</b><span class="small muted" style="display:block">${TEMPLATES.length} ready-made habits you can customise</span></span>${UI.icon('right')}</button>`;
    h += `<div class="card"><div class="row" style="margin-bottom:14px"><button class="bubble" style="width:58px;height:58px;font-size:1.8rem;background:color-mix(in srgb,${F.color} 18%,transparent)" data-act="emoji" aria-label="Change icon">${E(F.icon)}</button>
      <div class="grow"><label class="lbl" for="hn">Name</label><input class="inp" id="hn" maxlength="60" placeholder="e.g. Read, Drink water" value="${E(F.name)}" data-input="f" data-k="name" ${F.id ? '' : 'autofocus'}></div></div>
      <div class="fld"><label for="hd">Description (optional)</label><input class="inp" id="hd" maxlength="140" value="${E(F.desc)}" data-input="f" data-k="desc" placeholder="Why does this habit matter to you?"></div>
      <span class="lbl">Color</span><div class="swatches" style="margin:8px 0 4px">${COLORS.map(c => `<button class="swatch ${F.color === c ? 'on' : ''}" style="background:${c}" data-act="set" data-k="color" data-v="${c}" aria-label="Color ${c}"></button>`).join('')}</div></div>`;
    // type & goal
    h += `<div class="card"><h2>Habit type</h2>${UI.seg('htype', [['build', 'Build'], ['reduce', 'Reduce'], ['quit', 'Quit']], F.type)}<p class="hint" style="margin:8px 0 14px">${F.type === 'build' ? 'A habit you want to do more of.' : F.type === 'reduce' ? 'Something you want to do less. Set a daily limit; days within it count as successful.' : 'Something you want to stop. Record successful days and any occurrences.'}</p>`;
    if (F.type === 'build') {
      h += `<span class="lbl">What to track</span><div class="chips" style="margin:8px 0 14px">${chip('track', 'check', 'Completion', F.track === 'check')}${chip('track', 'count', 'Amount / reps', F.track === 'count')}${chip('track', 'time', 'Duration', F.track === 'time')}${chip('track', 'steps', 'Checklist', F.track === 'steps')}</div>`;
      if (F.track === 'count') h += `<div class="row"><div class="fld grow"><label for="ht">Goal per day</label><input class="inp" id="ht" type="number" min="1" step="any" value="${F.target}" data-input="f" data-k="target"></div><div class="fld grow"><label for="hu">Unit</label><input class="inp" id="hu" maxlength="20" value="${E(F.unit)}" placeholder="pages, km, reps" data-input="f" data-k="unit"></div><div class="fld" style="width:90px"><label for="hs">Step (+)</label><input class="inp" id="hs" type="number" min="0.1" step="any" value="${F.step}" data-input="f" data-k="step"></div></div>`;
      if (F.track === 'time') h += `<div class="fld"><label for="ht">Minutes per day</label><input class="inp" id="ht" type="number" min="1" max="1440" value="${F.target}" data-input="f" data-k="target"></div>`;
      if (F.track === 'steps') h += `<span class="lbl">Checklist steps</span><p class="hint" style="margin:4px 0 8px">The habit counts as complete when every step is done. Steps reset on each scheduled day; history is kept.</p>
        ${F.check.map((c, i) => `<div class="row" style="margin-bottom:8px"><input class="inp grow" maxlength="80" value="${E(c.t)}" data-input="step" data-i="${i}" aria-label="Step ${i + 1}">
          <button class="ib" data-act="sup" data-i="${i}" aria-label="Move up" ${i ? '' : 'disabled'}>${UI.icon('up', 18)}</button><button class="ib" data-act="sdel" data-i="${i}" aria-label="Delete step">${UI.icon('trash', 18)}</button></div>`).join('')}
        <button class="btn sec sm" data-act="sadd">${UI.icon('plus', 16)} Add step</button>`;
    } else if (F.type === 'reduce') h += `<div class="row"><div class="fld grow"><label for="hl">Daily limit</label><input class="inp" id="hl" type="number" min="0" value="${F.limit}" data-input="f" data-k="limit"></div><div class="fld grow"><label for="hu">Unit</label><input class="inp" id="hu" maxlength="20" value="${E(F.unit)}" placeholder="cups, sessions" data-input="f" data-k="unit"></div></div>`;
    h += '</div>';
    // schedule
    const FREQ = [['daily', 'Every day'], ['weekdays', 'Weekdays (Mon–Fri)'], ['weekends', 'Weekends'], ['days', 'Specific days of the week'], ['interval', 'Every few days'], ['times', 'A number of times per week / month / year'], ['monthly', 'A day of the month'], ['once', 'One time only']];
    h += `<div class="card"><h2>Schedule</h2><div class="fld"><label for="hf">Repeat</label><select class="inp" id="hf" data-change="freq">${sel(F.freq, FREQ)}</select></div>`;
    if (F.freq === 'days') h += `<div class="chips" style="margin-bottom:14px">${[1, 2, 3, 4, 5, 6, 0].map(d => `<button class="chip ${F.days.indexOf(d) >= 0 ? 'on' : ''}" data-act="day" data-v="${d}">${UI.DN[d]}</button>`).join('')}</div>`;
    if (F.freq === 'interval') h += `<div class="fld"><label for="he">Every how many days?</label><input class="inp" id="he" type="number" min="2" max="365" value="${F.every}" data-input="f" data-k="every"></div>`;
    if (F.freq === 'times') h += `<div class="row"><div class="fld grow"><label for="hnn">Times</label><input class="inp" id="hnn" type="number" min="1" max="366" value="${F.n}" data-input="f" data-k="n"></div><div class="fld grow"><label for="hp">Per</label><select class="inp" id="hp" data-change="per">${sel(F.per, [['week', 'Week'], ['month', 'Month'], ['year', 'Year']])}</select></div></div><p class="hint" style="margin:-6px 0 12px">Log it on any day. Success is judged once the ${F.per} ends, so it is never marked missed early.</p>`;
    if (F.freq === 'monthly') h += `<div class="fld"><label for="hdm">Day of month</label><input class="inp" id="hdm" type="number" min="1" max="31" value="${F.dom}" data-input="f" data-k="dom"><span class="hint">In shorter months it falls on the last day.</span></div>`;
    h += `<div class="row"><div class="fld grow"><label for="hst">${F.freq === 'once' ? 'Date' : 'Start date'}</label><input class="inp" id="hst" type="date" value="${F.start}" data-input="f" data-k="start"></div>${F.freq === 'once' ? '' : `<div class="fld grow"><label for="hen">End date (optional)</label><input class="inp" id="hen" type="date" value="${F.end}" min="${F.start}" data-input="f" data-k="end"></div>`}</div>
      ${F.id ? '<p class="hint">Schedule changes apply from today. Past days keep the schedule they had, so your history stays accurate.</p>' : ''}</div>`;
    // organize
    h += `<div class="card"><h2>Organize</h2><span class="lbl">Time of day</span><div class="chips" style="margin:8px 0 14px">${D.sections.map(s => chip('part', s.id, E(s.icon + ' ' + s.name), F.part === s.id)).join('')}</div>
      <span class="lbl">Categories (pick any)</span><div class="chips" style="margin:8px 0 6px">${D.cats.map(c => `<button class="chip ${F.cats.indexOf(c.id) >= 0 ? 'on' : ''}" data-act="cat" data-v="${c.id}">${E(c.icon)} ${E(c.name)}</button>`).join('')}<button class="chip" data-act="newcat">${UI.icon('plus', 14)} New</button></div>
      <div class="row" style="margin-top:12px"><div class="grow"><b class="small">Daily priority</b><div class="hint">Show it in "Today's priorities" on Home.</div></div>${UI.sw('', F.priority, 'prio', 'Daily priority')}</div></div>`;
    // reminders
    const others = D.habits.filter(x => !x.archived && x.id !== F.id);
    h += `<div class="card"><h2>Reminders</h2><div class="row"><b class="grow small">Remind me</b>${UI.sw('', F.remOn, 'remOn', 'Reminders on')}</div>`;
    if (F.remOn) {
      h += `<div class="mt">${F.times.map((t, i) => `<div class="row" style="margin-bottom:8px"><input class="inp grow" type="time" value="${t}" data-input="time" data-i="${i}" aria-label="Reminder time ${i + 1}">${F.times.length > 1 ? `<button class="ib" data-act="tdel" data-i="${i}" aria-label="Remove time">${UI.icon('trash', 18)}</button>` : ''}</div>`).join('')}
        ${F.times.length < 5 ? `<button class="btn sec sm" data-act="tadd">${UI.icon('plus', 16)} Add another time</button>` : ''}</div>
        <div class="row mt"><div class="grow"><b class="small">Different time on some days</b><div class="hint">Leave a day empty to use the times above.</div></div>${UI.sw('', F.byDayOn, 'byDayOn', 'Different time per day')}</div>
        ${F.byDayOn ? `<div class="mt">${[1, 2, 3, 4, 5, 6, 0].map(d => `<div class="row" style="margin-bottom:6px"><span style="width:44px" class="small b">${UI.DN[d]}</span><input class="inp grow" type="time" value="${(F.byDay[d] && F.byDay[d][0]) || ''}" data-input="bday" data-d="${d}" aria-label="${UI.DFULL[d]} reminder"></div>`).join('')}</div>` : ''}
        <div class="fld mt"><label for="hm">Custom message (optional)</label><input class="inp" id="hm" maxlength="120" value="${E(F.msg)}" data-input="f" data-k="msg" placeholder="e.g. Five minutes is enough to start."></div>`;
      if (!App.native) h += `<div class="banner info small">${UI.icon('bell', 18)}<span>Notifications are delivered by the Android app. In a web browser, reminders only show inside the app.</span></div>`;
    }
    h += `<div class="fld mt"><label for="hsk">Habit stacking: do this after…</label><select class="inp" id="hsk" data-change="stack"><option value="">No link</option>${others.map(x => `<option value="${x.id}" ${F.stack === x.id ? 'selected' : ''}>${E(x.icon + ' ' + x.name)}</option>`).join('')}</select><span class="hint">When you complete that habit, HabitFlow suggests this one next.</span></div></div>`;
    h += `<div class="card"><div class="fld" style="margin:0"><label for="hno">Notes (optional)</label><textarea class="inp" id="hno" maxlength="1000" data-input="f" data-k="notes" placeholder="Tips, motivation or details for this habit">${E(F.notes)}</textarea></div></div>
      <div class="err" id="ferr" role="alert"></div><button class="btn full" data-act="save">${F.id ? 'Save changes' : 'Create habit'}</button><div style="height:12px"></div></div>`;
    return h;
  }
  function keep(fn) { const y = window.scrollY; fn(); App.render(); window.scrollTo(0, y); }
  function buildSched() {
    switch (F.freq) {
      case 'weekdays': return { kind: 'weekly', days: [1, 2, 3, 4, 5] }; case 'weekends': return { kind: 'weekly', days: [0, 6] };
      case 'days': return { kind: 'weekly', days: F.days.slice().sort() }; case 'interval': return { kind: 'interval', every: +F.every };
      case 'times': return { kind: 'times', n: +F.n, per: F.per }; case 'monthly': return { kind: 'monthly', dom: +F.dom }; case 'once': return { kind: 'once' };
      default: return { kind: 'daily' };
    }
  }
  function validate() {
    if (!F.name.trim()) return 'Give your habit a name.';
    if (F.type === 'build' && (F.track === 'count' || F.track === 'time') && !(+F.target > 0)) return 'Set a goal greater than 0.';
    if (F.track === 'time' && +F.target > 1440) return 'A day has 1,440 minutes. Pick a smaller goal.';
    if (F.type === 'build' && F.track === 'steps' && !F.check.some(c => c.t.trim())) return 'Add at least one checklist step.';
    if (F.type === 'reduce' && !(+F.limit >= 0)) return 'Set a daily limit of 0 or more.';
    if (F.freq === 'days' && !F.days.length) return 'Pick at least one day of the week.';
    if (F.freq === 'interval' && !(+F.every >= 2 && +F.every <= 365)) return 'Repeat every 2 to 365 days.';
    if (F.freq === 'times') { const mx = F.per === 'week' ? 7 : F.per === 'month' ? 31 : 366; if (!(+F.n >= 1 && +F.n <= mx)) return 'Pick 1 to ' + mx + ' times per ' + F.per + '.'; }
    if (F.freq === 'monthly' && !(+F.dom >= 1 && +F.dom <= 31)) return 'Pick a day between 1 and 31.';
    if (!/^\d{4}-\d{2}-\d{2}$/.test(F.start)) return 'Pick a start date.';
    if (F.end && F.end < F.start) return 'The end date must be after the start date.';
    if (F.remOn && !F.times.every(t => /^\d{2}:\d{2}$/.test(t))) return 'Check the reminder times.';
    if (F.stack && F.stack === F.id) return 'A habit cannot follow itself.';
    return '';
  }
  async function save() {
    const err = validate(); if (err) { document.getElementById('ferr').textContent = err; UI.toast(err, { err: 1 }); return; }
    const D = App.D, t = App.tdy(), sched = buildSched();
    const goal = F.type === 'reduce' ? { kind: 'check', limit: +F.limit, unit: F.unit.trim() } : F.type === 'quit' ? { kind: 'check' } :
      F.track === 'count' ? { kind: 'count', target: +F.target, unit: F.unit.trim(), step: +F.step > 0 ? +F.step : 1 } : F.track === 'time' ? { kind: 'time', target: Math.round(+F.target), unit: 'min' } : { kind: 'check' };
    const byDay = {}; if (F.byDayOn) Object.keys(F.byDay).forEach(d => { if (F.byDay[d] && F.byDay[d][0]) byDay[d] = F.byDay[d].slice(0, 1); });
    const fields = { name: F.name.trim().slice(0, 60), desc: F.desc.trim(), icon: F.icon || '⭐', color: F.color, type: F.type, goal, cats: F.cats.slice(), part: F.part, end: F.freq === 'once' ? F.start : (F.end || null),
      check: F.type === 'build' && F.track === 'steps' ? F.check.filter(c => c.t.trim()).map(c => ({ id: c.id, t: c.t.trim() })) : [],
      rem: { on: F.remOn, times: Array.from(new Set(F.times)).sort(), byDay, msg: F.msg.trim() }, stack: F.stack || null, priority: F.priority, notes: F.notes.trim() };
    let id = F.id;
    const ok = App.act(() => {
      if (F.id) { const h = App.habit(F.id); if (F.start !== h.start) { h.start = F.start; if (h.schedHist && h.schedHist.length) h.schedHist[0].from = F.start; } Core.changeSchedule(h, sched, t); Object.assign(h, fields); }
      else { id = Core.uid(); D.habits.push(Object.assign({ id, created: Date.now(), start: F.start, sched, order: D.habits.reduce((m, x) => Math.max(m, x.order || 0), 0) + 1 }, fields)); }
    }, F.id ? 'Habit updated.' : 'Habit created.', { noUndo: !F.id });
    if (!ok) return;
    const wasNew = !F.id; F = null; key = null;
    App.ui.stack = App.ui.stack.filter(s => s.s !== 'habitForm' && s.s !== 'library'); App.render();
    if (wasNew && fields.rem.on && App.native && App.native.notifStatus && App.native.notifStatus() !== 'granted') {
      if (await UI.confirm('Allow notifications?', 'HabitFlow needs notification permission to send your reminders. You can change this later in Android settings.', 'Allow')) App.native.requestNotifPermission();
    }
  }
  return {
    render, reset: () => { F = null; key = null; },
    inputs: {
      f: t => { F[t.dataset.k] = t.value; },
      step: t => { F.check[+t.dataset.i].t = t.value; },
      time: t => { F.times[+t.dataset.i] = t.value; },
      bday: t => { if (t.value) F.byDay[t.dataset.d] = [t.value]; else delete F.byDay[t.dataset.d]; }
    },
    changes: {
      freq: t => keep(() => { F.freq = t.value; }), per: t => keep(() => { F.per = t.value; }), stack: t => { F.stack = t.value; },
      remOn: t => keep(() => { F.remOn = t.checked; }), byDayOn: t => keep(() => { F.byDayOn = t.checked; }), prio: t => { F.priority = t.checked; }
    },
    acts: {
      save, set: t => keep(() => { F[t.dataset.k] = t.dataset.v; }),
      seg: t => { if (t.dataset.seg === 'htype') keep(() => { F.type = t.dataset.v; }); },
      day: t => keep(() => { const d = +t.dataset.v, i = F.days.indexOf(d); if (i >= 0) F.days.splice(i, 1); else F.days.push(d); }),
      cat: t => keep(() => { const i = F.cats.indexOf(t.dataset.v); if (i >= 0) F.cats.splice(i, 1); else F.cats.push(t.dataset.v); }),
      sadd: () => keep(() => { F.check.push({ id: Core.uid(), t: '' }); }), sdel: t => keep(() => { F.check.splice(+t.dataset.i, 1); }),
      sup: t => keep(() => { const i = +t.dataset.i; if (i > 0) { const x = F.check[i]; F.check[i] = F.check[i - 1]; F.check[i - 1] = x; } }),
      tadd: () => keep(() => { F.times.push('20:00'); }), tdel: t => keep(() => { F.times.splice(+t.dataset.i, 1); }),
      emoji: () => UI.sheet(`<h3>Choose an icon</h3><div class="emo">${EMOJI.map(e => `<button data-e="${e}" class="${F.icon === e ? 'on' : ''}">${e}</button>`).join('')}</div>
        <div class="fld mt"><label for="ce">Or type any emoji</label><input class="inp" id="ce" maxlength="4" value="${E(F.icon)}"></div><button class="btn full" id="ceok">Use this icon</button>`, sh => {
        sh.querySelectorAll('[data-e]').forEach(b => b.onclick = () => { UI.closeSheet(); keep(() => { F.icon = b.dataset.e; }); });
        sh.querySelector('#ceok').onclick = () => { const v = sh.querySelector('#ce').value.trim(); UI.closeSheet(); if (v) keep(() => { F.icon = v; }); }; }),
      newcat: () => UI.sheet(`<h3>New category</h3><div class="fld"><label for="cn">Name</label><input class="inp" id="cn" maxlength="30" autofocus></div><div class="err" id="cerr"></div><button class="btn full" id="cok">Add category</button>`, sh => {
        sh.querySelector('#cok').onclick = () => { const n = sh.querySelector('#cn').value.trim(); if (!n) { sh.querySelector('#cerr').textContent = 'Enter a name.'; return; }
          const id = 'c' + Core.uid(); UI.closeSheet(); App.D.cats.push({ id, name: n, color: '#8e8e93', icon: '\u{1F3F7}️' }); App.save(); keep(() => { F.cats.push(id); }); }; })
    }
  };
})();

/* Template library */
Screens.library = (() => {
  const E = s => UI.esc(s);
  return {
    render() {
      const q = (App.ui.f.lq || '').toLowerCase(), area = App.ui.f.larea || '', areas = Array.from(new Set(TEMPLATES.map(t => t.area)));
      const list = TEMPLATES.filter(t => (!area || t.area === area) && (!q || (t.name + ' ' + t.area).toLowerCase().indexOf(q) >= 0));
      return `<div class="top"><button class="ib" data-act="back" aria-label="Back">${UI.icon('left')}</button><h1 class="t2">Habit library</h1></div><div class="stack">
        <input class="inp" type="search" placeholder="Search templates" value="${E(App.ui.f.lq || '')}" data-input="lq" aria-label="Search templates">
        <div class="chips scroll"><button class="chip ${!area ? 'on' : ''}" data-act="larea" data-v="">All</button>${areas.map(a => `<button class="chip ${area === a ? 'on' : ''}" data-act="larea" data-v="${E(a)}">${E(a)}</button>`).join('')}</div>
        <div class="card">${list.length ? `<div class="list">${list.map(t => `<button class="li" data-act="pick" data-id="${t.id}"><span class="bubble" style="background:color-mix(in srgb,${t.color} 18%,transparent)">${t.icon}</span><span class="grow"><span class="t">${E(t.name)}</span><span class="s" style="display:block">${E(t.area)} · ${t.type === 'quit' ? 'Quit' : t.type === 'reduce' ? 'Reduce' : HC.goalText(Object.assign({ goal: t.goal, check: (t.check || []).map(x => ({ t: x })) }, t))} · ${HC.schedText({ sched: t.sched, start: App.tdy() })}</span></span>${UI.icon('plus', 20)}</button>`).join('')}</div>` : UI.empty('\u{1F50E}', 'No templates found', 'Try another search, or create your own habit.', '<button class="btn" data-act="own">Create from scratch</button>')}</div></div>`;
    },
    acts: { larea: t => { App.ui.f.larea = t.dataset.v; App.render(); }, pick: t => { Screens.habitForm.reset(); App.replaceTop('habitForm', { tpl: t.dataset.id }); }, own: () => { Screens.habitForm.reset(); App.replaceTop('habitForm', {}); } },
    inputs: { lq: t => { App.ui.f.lq = t.value; clearTimeout(Screens.library._qt); Screens.library._qt = setTimeout(() => { App.render(); const n = document.querySelector('[data-input=lq]'); if (n) { n.focus(); n.setSelectionRange(n.value.length, n.value.length); } }, 250); } }
  };
})();

/* Habit details: statistics & history */
Screens.habit = (() => {
  const E = s => UI.esc(s);
  function render(p) {
    const D = App.D, h = App.habit(p.id), t = App.tdy(), s = D.settings; if (!h) return `<div class="top"><button class="ib" data-act="back">${UI.icon('left')}</button></div>` + UI.empty('\u{1F50E}', 'Habit not found', 'It may have been deleted.');
    const month = App.ui.f['hm' + h.id] || t.slice(0, 7), y = +month.slice(0, 4), m = +month.slice(5, 7), mFrom = month + '-01', mTo = month + '-' + Core.pad(Core.dim(y, m));
    const r30 = Core.rate(D, h, Core.addDays(t, -29), t, t), all = Core.rate(D, h, h.start, t, t), kind = Core.goalKind(h), flex = Core.isFlex(h, t), neg = Core.isNegative(h), unit = flex ? (Core.schedFor(h, t).per + 's') : 'days';
    let total = 0, timeFromFocus = 0, occ = 0; Object.keys(D.entries).forEach(k => { if (k.indexOf(h.id + '|') === 0) { total += D.entries[k].v || 0; occ += D.entries[k].n || 0; } });
    D.focus.forEach(f => { if (f.hid === h.id) timeFromFocus += f.secs; });
    const gs = !flex && kind !== 'check' ? (() => { let met = 0, n = 0; Core.range(h.start, t).forEach(d => { const st = Core.status(D, h, d, t); if (st === 'off' || st === 'skip' || (d === t && st !== 'done')) return; n++; if (st === 'done') met++; }); return n ? Math.round(met / n * 100) : 0; })() : null;
    const paused = Core.isPaused(h, t);
    let out = `<div class="top"><button class="ib" data-act="back" aria-label="Back">${UI.icon('left')}</button><h1 class="t2">${E(h.name)}</h1><button class="ib" data-act="go" data-s="habitForm" data-id="${h.id}" aria-label="Edit">${UI.icon('edit')}</button></div><div class="stack">
      <div class="card row"><span class="bubble" style="width:56px;height:56px;font-size:1.7rem;background:color-mix(in srgb,${h.color} 18%,transparent)">${E(h.icon)}</span><div class="grow"><b>${E(h.name)}</b><div class="small muted">${E(HC.goalText(h))} · ${E(HC.schedText(h, t))}</div>
      <div class="chips" style="margin-top:6px">${h.archived ? '<span class="badge paused">Archived</span>' : ''}${paused ? '<span class="badge paused">Paused</span>' : ''}${neg ? `<span class="badge partial">${h.type === 'quit' ? 'Quit' : 'Reduce'}</span>` : ''}${Core.habitCats(h).map(c => App.cat(c)).filter(Boolean).map(c => `<span class="badge pending">${E(c.icon + ' ' + c.name)}</span>`).join('')}</div>${h.desc ? `<p class="small mt">${E(h.desc)}</p>` : ''}</div></div>
      <div class="stats"><div class="stat"><b>${Core.currentStreak(D, h, t)}</b><span>Current streak (${unit})</span></div><div class="stat"><b>${Core.longestStreak(D, h, t)}</b><span>Longest streak</span></div>
      <div class="stat"><b>${flex ? all.done : Core.totalDone(D, h, t)}</b><span>${flex ? 'Periods met' : neg ? 'Successful days' : 'Completions'}</span></div><div class="stat"><b>${r30.pct}%</b><span>Last 30 days</span></div>
      <div class="stat"><b>${all.missed}</b><span>${neg ? 'Setbacks / unrecorded' : 'Missed / not done'}</span></div><div class="stat"><b>${all.skipped}</b><span>Skipped</span></div>
      ${gs != null ? `<div class="stat"><b>${gs}%</b><span>Days goal reached</span></div><div class="stat"><b>${kind === 'time' ? UI.fmtDur(total * 60) : Math.round(total * 100) / 100 + ' ' + E(h.goal.unit || '')}</b><span>Total recorded</span></div>` : ''}
      ${neg ? `<div class="stat"><b>${occ}</b><span>Occurrences recorded</span></div>` : ''}${timeFromFocus ? `<div class="stat"><b>${UI.fmtDur(timeFromFocus)}</b><span>Focus time</span></div>` : ''}</div>`;
    // calendar
    out += `<div class="card"><div class="row" style="margin-bottom:10px"><button class="ib" data-act="hmon" data-v="-1" data-id="${h.id}" aria-label="Previous month">${UI.icon('left')}</button><b class="grow" style="text-align:center">${UI.MFULL[m - 1]} ${y}</b><button class="ib" data-act="hmon" data-v="1" data-id="${h.id}" aria-label="Next month">${UI.icon('right')}</button></div>${habitCal(h, y, m)}
      <div class="legend"><span><i style="background:var(--done)"></i>Done</span><span><i style="background:color-mix(in srgb,var(--part) 40%,transparent)"></i>Partial</span><span><i style="background:color-mix(in srgb,var(--miss) 30%,transparent)"></i>Missed</span><span><i style="background:color-mix(in srgb,var(--skip) 40%,transparent)"></i>Skipped</span></div><p class="hint mt">Tap a past day to correct its record.</p></div>`;
    // patterns
    const from84 = Core.addDays(t, -83), wd = [0, 1, 2, 3, 4, 5, 6].map(d => { let dn = 0, tot = 0; Core.range(from84 < h.start ? h.start : from84, t).forEach(x => { if (Core.dow(x) !== d) return; const st = Core.status(D, h, x, t); if (st === 'off' || st === 'skip' || st === 'open' || (x === t && st !== 'done')) return; tot++; if (st === 'done') dn++; }); return tot ? Math.round(dn / tot * 100) : null; });
    const ws = s.weekStart, wdOrd = [0, 1, 2, 3, 4, 5, 6].map(i => (i + ws) % 7);
    if (!flex) out += `<div class="card"><h2>Weekly pattern (last 12 weeks)</h2>${UI.bars(wdOrd.map(d => ({ l: UI.DN[d].slice(0, 2), v: wd[d], t: UI.DFULL[d] + ': ' + (wd[d] == null ? 'not scheduled' : wd[d] + '%') })), { max: 100, suf: '%', color: h.color, label: 'Completion rate by weekday' })}</div>`;
    const months = []; for (let i = 5; i >= 0; i--) { const dt = new Date(+t.slice(0, 4), +t.slice(5, 7) - 1 - i, 1), a = Core.ymd(dt), b = Core.ymd(new Date(dt.getFullYear(), dt.getMonth() + 1, 0)); months.push({ l: UI.MN[dt.getMonth()], v: b < h.start ? null : Core.rate(D, h, a, b, t).pct }); }
    out += `<div class="card"><h2>Monthly pattern</h2>${UI.bars(months, { max: 100, suf: '%', color: h.color, label: 'Completion rate for the last 6 months' })}</div>`;
    if (kind !== 'check' && !neg) { const days = Core.range(Core.addDays(t, -13), t); out += `<div class="card"><h2>Recorded ${kind === 'time' ? 'minutes' : E(h.goal.unit || 'amount')} (14 days)</h2>${UI.bars(days.map(d => ({ l: +d.slice(8), v: (Core.getEntry(D, h, d) || {}).v || 0 })), { color: h.color, label: 'Recorded amount per day' })}</div>`; }
    if (neg) {
      const wk = []; for (let i = 7; i >= 0; i--) { const a = Core.addDays(t, -7 * i - 6), b = Core.addDays(t, -7 * i); let n = 0; Core.range(a, b).forEach(d => n += (Core.getEntry(D, h, d) || {}).n || 0); wk.push({ l: UI.fmtDate(a, s.dateFmt).slice(0, 6), v: n }); }
      const trig = {}; Object.keys(D.entries).forEach(k => { if (k.indexOf(h.id + '|') !== 0) return; (D.entries[k].occ || []).forEach(o => { const x = (o.trig || '').trim().toLowerCase(); if (x) trig[x] = (trig[x] || 0) + 1; }); });
      const tl = Object.keys(trig).sort((a, b) => trig[b] - trig[a]).slice(0, 5);
      out += `<div class="card"><h2>Occurrences per week</h2>${UI.bars(wk, { color: 'var(--miss)', label: 'Occurrences per week, last 8 weeks' })}<p class="hint mt">Fewer bars over time means progress. Setbacks are normal; look for what triggers them.</p></div>
        <div class="card"><h2>Common triggers</h2>${tl.length ? `<ul class="tl">${tl.map(x => `<li><span class="grow">${E(x)}</span><b>${trig[x]}×</b></li>`).join('')}</ul>` : '<p class="muted small">Add a note about what was going on when you record an occurrence to see patterns here.</p>'}</div>`;
    }
    if (flex) { const per = []; let d = t; for (let i = 0; i < 8; i++) { const pr = Core.periodRange(D, h, d); if (pr.to < h.start) break; per.unshift({ l: UI.fmtDate(pr.from, s.dateFmt).slice(0, 6), v: Core.periodProgress(D, h, pr.from).done }); d = Core.addDays(pr.from, -1); }
      out += `<div class="card"><h2>Per ${E(Core.schedFor(h, t).per)} (goal ${Core.flexTarget(h, t)})</h2>${UI.bars(per, { color: h.color, label: 'Completions per period' })}</div>`; }
    const notes = Object.keys(D.entries).filter(k => k.indexOf(h.id + '|') === 0 && D.entries[k].note).sort().reverse().slice(0, 10);
    out += `<div class="card"><h2>Notes</h2>${notes.length ? `<ul class="tl">${notes.map(k => `<li><span class="muted small" style="width:84px;flex:none">${UI.fmtDate(k.split('|')[1], s.dateFmt)}</span><span class="grow small">${E(D.entries[k].note)}</span></li>`).join('')}</ul>` : '<p class="muted small">Notes you add to check-ins appear here.</p>'}${h.notes ? `<p class="small mt"><b>Habit notes:</b> ${E(h.notes)}</p>` : ''}</div>`;
    out += `<div class="card"><h2>Manage</h2><div class="list">
      <button class="li" data-act="dup" data-id="${h.id}">${UI.icon('copy')}<span class="grow t">Duplicate</span></button>
      ${h.archived ? '' : `<button class="li" data-act="pause" data-id="${h.id}">${UI.icon(paused ? 'play' : 'pause')}<span class="grow"><span class="t">${paused ? 'Resume' : 'Pause'}</span><span class="s" style="display:block">${paused ? 'Start scheduling it again from today.' : 'Stop scheduling it for now. Paused days never count as missed.'}</span></span></button>`}
      <button class="li" data-act="arch" data-id="${h.id}">${UI.icon('archive')}<span class="grow"><span class="t">${h.archived ? 'Restore' : 'Archive'}</span><span class="s" style="display:block">${h.archived ? 'Bring it back to your active habits.' : 'Hide it. All history is kept and you can restore it any time.'}</span></span></button>
      <button class="li" data-act="del" data-id="${h.id}" style="color:var(--miss)">${UI.icon('trash')}<span class="grow t">Delete permanently</span></button></div></div></div>`;
    return out;
  }
  function habitCal(h, y, m) {
    const D = App.D, t = App.tdy(), first = y + '-' + Core.pad(m) + '-01', ws = D.settings.weekStart, lead = (Core.dow(first) - ws + 7) % 7, n = Core.dim(y, m);
    let s = '<div class="cal">' + [0, 1, 2, 3, 4, 5, 6].map(i => `<div class="h">${UI.DN[(i + ws) % 7].slice(0, 2)}</div>`).join(''); for (let i = 0; i < lead; i++) s += '<div></div>';
    for (let d = 1; d <= n; d++) { const ds = y + '-' + Core.pad(m) + '-' + Core.pad(d), st = Core.status(D, h, ds, t), cls = st === 'off' ? 'out' : st === 'failed' ? 'st-missed' : 'st-' + st;
      s += `<button class="c ${cls} ${ds === t ? 'today' : ''}" ${st === 'off' || ds > t ? 'disabled' : `data-act="hmore" data-h="${h.id}" data-d="${ds}"`} aria-label="${ds}: ${UI.STAT[st] ? UI.STAT[st].l : st}">${d}</button>`; }
    return s + '</div>';
  }
  return {
    render,
    acts: {
      hmon: t => { const k = 'hm' + t.dataset.id, cur = App.ui.f[k] || App.tdy().slice(0, 7), p = cur.split('-').map(Number), dt = new Date(p[0], p[1] - 1 + +t.dataset.v, 1); App.ui.f[k] = Core.ymd(dt).slice(0, 7); App.render(); },
      dup: t => { const h = App.habit(t.dataset.id); App.act(() => { const c = JSON.parse(JSON.stringify(h)); c.id = Core.uid(); c.name = (h.name + ' (copy)').slice(0, 60); c.start = App.tdy(); c.created = Date.now(); delete c.schedHist; delete c.pauses; c.archived = false; c.order = (h.order || 0) + .5; App.D.habits.push(c); }, 'Duplicated. History is not copied.'); },
      pause: t => { const h = App.habit(t.dataset.id), p = Core.isPaused(h, App.tdy()); App.act(() => { if (p) Core.resumeHabit(h, App.tdy()); else Core.pauseHabit(h, App.tdy()); }, p ? 'Resumed.' : 'Paused. Your history and streak are kept.'); },
      arch: t => { const h = App.habit(t.dataset.id); App.act(() => { h.archived = !h.archived; }, h.archived ? 'Archived. Find it in Settings > Archived habits.' : 'Restored.'); },
      del: async t => { const h = App.habit(t.dataset.id); if (!(await UI.confirm('Delete "' + h.name + '"?', 'This permanently removes the habit and all of its history. Archive it instead if you might want it back.', 'Delete forever', true))) return;
        App.act(() => { App.D.habits = App.D.habits.filter(x => x.id !== h.id); Object.keys(App.D.entries).forEach(k => { if (k.indexOf(h.id + '|') === 0) delete App.D.entries[k]; }); App.D.habits.forEach(x => { if (x.stack === h.id) x.stack = null; }); App.D.goals.forEach(g => g.habitIds = (g.habitIds || []).filter(i => i !== h.id)); }, 'Habit deleted.');
        App.ui.stack = App.ui.stack.filter(s => !(s.s === 'habit' && s.p.id === h.id)); App.render(); }
    }
  };
})();
