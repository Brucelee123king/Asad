/* On-device assistant: rule-based (no AI model, no network). Every change needs a tap to confirm. */
Screens.assistant = (() => {
  const E = s => UI.esc(s); let msgs = [], pend = {};
  try { msgs = JSON.parse(sessionStorage.getItem('hf.asst') || '[]'); } catch (e) { }
  const keep = () => { try { sessionStorage.setItem('hf.asst', JSON.stringify(msgs.slice(-40))); } catch (e) { } };
  const bot = (text, acts) => { msgs.push({ me: 0, text, acts: acts || [] }); keep(); };
  const DAYS = { sun: 0, mon: 1, tue: 2, wed: 3, thu: 4, fri: 5, sat: 6 };
  function propose(label, summary, fn) { const id = Core.uid(); pend[id] = fn; return { id, label, summary }; }
  function newHabit(o) { return Object.assign({ id: Core.uid(), created: Date.now(), start: App.tdy(), icon: '⭐', color: '#2f6bff', type: 'build', goal: { kind: 'check' }, sched: { kind: 'daily' }, part: 'anytime', cats: [], check: [], rem: { on: false, times: ['08:00'], byDay: {}, msg: '' }, order: App.D.habits.reduce((m, x) => Math.max(m, x.order || 0), 0) + 1 }, o); }
  function parseHabit(text) {
    let s = text.replace(/^(please\s+)?(add|create|start|track|make)\s+(a\s+)?(new\s+)?(habit\s+)?(to\s+|for\s+)?/i, '').trim(); if (!s) return null;
    const o = { name: '', goal: { kind: 'check' }, sched: { kind: 'daily' }, rem: { on: false, times: ['08:00'], byDay: {}, msg: '' } }, low = s.toLowerCase();
    const tm = low.match(/\bat\s+(\d{1,2})(?::(\d{2}))?\s*(am|pm)?/); if (tm) { let h = +tm[1]; if (tm[3] === 'pm' && h < 12) h += 12; if (tm[3] === 'am' && h === 12) h = 0; if (h < 24) { o.rem = { on: true, times: [Core.pad(h) + ':' + (tm[2] || '00')], byDay: {}, msg: '' }; o.part = h < 12 ? 'morning' : h < 17 ? 'afternoon' : h < 21 ? 'evening' : 'night'; } }
    const q = low.match(/(\d+(?:\.\d+)?)\s*(pages?|km|kilometers?|miles?|glasses?|cups?|reps?|push-?ups?|steps?|words?|minutes?|mins?|min|hours?|hrs?)\b/);
    if (q) { const n = +q[1], u = q[2]; if (/^(minutes?|mins?|min)$/.test(u)) o.goal = { kind: 'time', target: n, unit: 'min' }; else if (/^(hours?|hrs?)$/.test(u)) o.goal = { kind: 'time', target: n * 60, unit: 'min' }; else o.goal = { kind: 'count', target: n, unit: u, step: 1 }; }
    const tw = low.match(/(\d+)\s*(?:times|x)\s*(?:a|per)\s*(week|month|year)/);
    if (tw) o.sched = { kind: 'times', n: +tw[1], per: tw[2] };
    else if (/weekdays/.test(low)) o.sched = { kind: 'weekly', days: [1, 2, 3, 4, 5] };
    else if (/weekends?/.test(low)) o.sched = { kind: 'weekly', days: [0, 6] };
    else { const ds = []; Object.keys(DAYS).forEach(k => { if (new RegExp('\\b' + k + '(day|s)?\\b').test(low)) ds.push(DAYS[k]); }); if (ds.length) o.sched = { kind: 'weekly', days: ds.sort() }; else { const ev = low.match(/every\s+(\d+)\s+days/); if (ev) o.sched = { kind: 'interval', every: Math.max(2, +ev[1]) }; } }
    if (/\b(quit|stop|no more)\b/.test(low)) o.type = 'quit';
    o.name = s.replace(/\bat\s+\d{1,2}(:\d{2})?\s*(am|pm)?/i, '').replace(/(\d+(\.\d+)?)\s*(times|x)\s*(a|per)\s*(week|month|year)/i, '').replace(/\b(every\s*day|daily|each day|on|every\s+\d+\s+days|weekdays|weekends?)\b/gi, '').replace(/\b(sun|mon|tue|wed|thu|fri|sat)(day|s)?\b,?/gi, '').replace(/\s{2,}/g, ' ').replace(/[ ,.]+$/, '').trim();
    if (!o.name) return null; o.name = o.name.charAt(0).toUpperCase() + o.name.slice(1, 60);
    const tp = TEMPLATES.find(t => o.name.toLowerCase().indexOf(t.name.toLowerCase().split(' ')[0]) >= 0); if (tp) { o.icon = tp.icon; o.color = tp.color; if (!o.part) o.part = tp.part; }
    return o;
  }
  function describe(o) { return `${o.icon || '⭐'} ${o.name} · ${HC.goalText(o)} · ${HC.schedText(Object.assign({ start: App.tdy() }, o))}${o.rem.on ? ' · reminder ' + UI.fmtTime(o.rem.times[0], App.D.settings.timeFmt) : ''}`; }
  function reply(text) {
    const D = App.D, t = App.tdy(), low = text.toLowerCase().trim(), find = n => D.habits.filter(h => !h.archived).find(h => low.indexOf(h.name.toLowerCase()) >= 0);
    if (/(summar|progress|how am i|how did i|this week|report)/.test(low)) { const c = Core.dayCompletion(D, t, t); bot(['Today: ' + c.done + ' of ' + c.total + ' done (' + c.pct + '%).', ...Core.weeklyInsight(D, t)].join('\n')); return; }
    if (/(consistent|best|worst|rank|strongest|weakest)/.test(low)) { const r = Core.live(D).map(h => ({ h, p: Core.rate(D, h, Core.addDays(t, -29), t, t) })).filter(x => x.p.total).sort((a, b) => b.p.pct - a.p.pct);
      bot(r.length ? 'Most consistent over the last 30 days:\n' + r.slice(0, 5).map((x, i) => (i + 1) + '. ' + x.h.name + ' – ' + x.p.pct + '% (' + x.p.done + '/' + x.p.total + ')').join('\n') + (r.length > 5 ? '\n\nNeeds attention: ' + r.slice(-2).map(x => x.h.name + ' (' + x.p.pct + '%)').join(', ') : '') : 'There are no check-ins in the last 30 days yet, so there is nothing to rank.'); return; }
    if (/streak/.test(low)) { const s = Core.live(D).map(h => ({ h, n: Core.currentStreak(D, h, t), b: Core.longestStreak(D, h, t) })).sort((a, b) => b.n - a.n); bot(s.length ? s.slice(0, 6).map(x => x.h.name + ': ' + x.n + ' now, best ' + x.b).join('\n') : 'No habits yet.'); return; }
    if (/morning routine|evening routine|wind.?down|bedtime routine/.test(low)) { const ev = /evening|wind|bed/.test(low), tp = TEMPLATES.find(x => x.name === (ev ? 'Evening wind-down' : 'Morning routine')), w = D.settings.profile, tm = ev ? (w.sleep || '23:00').replace(/^(\d\d)/, m => Core.pad((+m + 23) % 24)) : (w.wake || '07:00');
      const o = newHabit({ name: tp.name, icon: tp.icon, color: tp.color, part: tp.part, check: tp.check.map((x, i) => ({ id: 'c' + i, t: x })), rem: { on: true, times: [tm], byDay: {}, msg: '' } });
      bot('Here is a ' + (ev ? 'wind-down' : 'morning') + ' routine as a checklist habit with a reminder at ' + UI.fmtTime(tm, D.settings.timeFmt) + ':\n' + tp.check.map((x, i) => (i + 1) + '. ' + x).join('\n') + '\n\nYou can edit the steps after adding it.', [propose('Add this routine', o.name, () => App.D.habits.push(o))]); return; }
    if (/study/.test(low) && /(plan|help|session|schedule)/.test(low)) { const o = newHabit({ name: 'Study session', icon: '\u{1F4D6}', color: '#5e5ce6', goal: { kind: 'time', target: 45, unit: 'min' }, sched: { kind: 'weekly', days: [1, 2, 3, 4, 5] }, part: 'afternoon', cats: ['learn'], rem: { on: true, times: ['16:00'], byDay: {}, msg: 'One focused session. Start with 25 minutes if that feels easier.' } });
      bot('A realistic start: 45 minutes on weekdays at 4 PM. Use the Focus tab\'s Pomodoro timer and link it to this habit so the minutes are logged automatically.', [propose('Add study habit', describe(o), () => App.D.habits.push(o))]); return; }
    if (/(change|set|make)\s+.+\s+to\s+\d+\s*(days|times)/.test(low)) { const h = find(low), n = +(low.match(/to\s+(\d+)\s*(days|times)/) || [])[1], per = /month/.test(low) ? 'month' : 'week';
      if (!h) { bot("I couldn't tell which habit you mean. Include its exact name, e.g. \"Change Workout to 3 days per week\"."); return; }
      if (!(n >= 1 && n <= (per === 'week' ? 7 : 31))) { bot('Pick between 1 and ' + (per === 'week' ? 7 : 31) + ' per ' + per + '.'); return; }
      bot('Change "' + h.name + '" from "' + HC.schedText(h, t) + '" to ' + n + '× per ' + per + '? It applies from today; past days keep their old schedule.', [propose('Apply change', h.name, () => Core.changeSchedule(h, { kind: 'times', n, per }, App.tdy()))]); return; }
    if (/(adjust|too hard|lower|easier|realistic|struggl)/.test(low)) { const low30 = Core.live(D).filter(h => Core.goalKind(h) !== 'check' && !Core.isNegative(h)).map(h => ({ h, p: Core.rate(D, h, Core.addDays(t, -29), t, t) })).filter(x => x.p.total >= 5 && x.p.pct < 50);
      if (!low30.length) { bot('None of your amount or duration goals look too hard right now (all are at 50% or more over the last 30 days, or have too little data). Nice work.'); return; }
      bot('These goals were reached on fewer than half of their days. A smaller target you hit often builds the habit faster:', low30.map(x => { const nt = Math.max(1, Math.round(x.h.goal.target * .7)); return propose('Lower ' + x.h.name + ' to ' + nt + ' ' + App.unitLabel(x.h), x.p.pct + '% of days', () => { x.h.goal.target = nt; }); })); return; }
    if (/(suggest|recommend|ideas?|what habit|new habits)/.test(low)) { const have = D.habits.map(h => h.name.toLowerCase()), areas = (D.settings.profile.areas || []).concat(D.settings.profile.goals || []).join(' ').toLowerCase();
      const pool = TEMPLATES.filter(x => have.indexOf(x.name.toLowerCase()) < 0).sort((a, b) => (areas.indexOf(b.area.toLowerCase().split(' ')[0]) >= 0) - (areas.indexOf(a.area.toLowerCase().split(' ')[0]) >= 0)).slice(0, 4);
      bot('Some ideas' + (areas ? ' based on what you told me' : '') + '. Tap one to customise it before adding:', pool.map(x => ({ id: 'tpl:' + x.id, label: x.icon + ' ' + x.name, summary: x.area }))); return; }
    if (/^(add|create|start|track|make)\b/.test(low)) { const o = parseHabit(text); if (!o) { bot('Tell me what to track, for example: "Add read 20 pages every day at 9pm" or "Track run 3 km on mon wed fri".'); return; } const h = newHabit(o);
      bot('I understood this habit:\n' + describe(h) + '\n\nAdd it, or open it in the editor to adjust.', [propose('Add habit', h.name, () => App.D.habits.push(h)), { id: 'edit:' + Core.uid(), label: 'Edit first', summary: '', hab: h }]); return; }
    if (/(export|backup|restore)/.test(low)) { bot('Go to Settings > Data, backup & privacy. You can export a full JSON backup, a CSV of your records, your journal, or restore a backup.'); return; }
    if (/(reminder|notification)/.test(low)) { bot('Edit a habit and turn on "Remind me". You can add several times, a different time on some weekdays, and a custom message. Quiet hours and snooze length are in Settings > Notifications.'); return; }
    if (/(skip|rest day|missed|not done)/.test(low)) { bot('Skip = planned rest day, keeps your streak. Not done = you record that it did not happen. Missed = a scheduled day ended with no check-in. Open a habit\'s ⋯ menu to choose.'); return; }
    bot('I can help with:\n• "Summarize my week"\n• "Which habits am I most consistent with?"\n• "Help me create a morning routine"\n• "Help me plan my study sessions"\n• "Add read 20 pages every day at 9pm"\n• "Change Workout to 3 days per week"\n• "Suggest new habits"\n• "Adjust my goals"');
  }
  function render() {
    if (!App.D.settings.aiOn) return `<div class="top"><button class="ib" data-act="back" aria-label="Back">${UI.icon('left')}</button><h1 class="t2">Assistant</h1></div><div class="card">${UI.empty('\u{1F916}', 'The assistant is off', 'Turn it on in Settings > Data, backup & privacy.', '<button class="btn" data-act="on">Turn on</button>')}</div>`;
    if (!msgs.length) bot('Hi! I can summarize your progress, rank your habits, build routines and create or adjust habits for you. Nothing changes until you tap to confirm.');
    return `<div class="top"><button class="ib" data-act="back" aria-label="Back">${UI.icon('left')}</button><h1 class="t2">Assistant</h1><button class="ib" data-act="clear" aria-label="Clear conversation">${UI.icon('reset')}</button></div>
      <div class="banner info small" style="margin-bottom:12px">${UI.icon('lock', 18)}<span>On-device helper using simple rules, not an AI model. It reads only your HabitFlow data on this phone and sends nothing anywhere. Suggestions are not medical advice. A cloud AI assistant would need an AI API key and a server, which are not set up.</span></div>
      <div class="chat" id="chat">${msgs.map(m => `<div class="msg ${m.me ? 'me' : 'bot'}">${E(m.text)}${(m.acts || []).length ? `<div class="chips" style="margin-top:10px">${m.acts.map(a => `<button class="chip" data-act="do" data-id="${E(a.id)}" ${a.done ? 'disabled' : ''}>${a.done ? '✓ ' : ''}${E(a.label)}</button>`).join('')}</div>` : ''}</div>`).join('')}</div>
      <div class="chips scroll mt">${['Summarize my week', 'Most consistent habits', 'Create a morning routine', 'Plan my study sessions', 'Suggest new habits', 'Adjust my goals'].map(q => `<button class="chip" data-act="ask" data-v="${q}">${q}</button>`).join('')}</div>
      <form class="row mt" data-act="noop" onsubmit="return false"><input class="inp grow" id="aq" maxlength="200" placeholder="Ask or tell me what to add" aria-label="Message"><button class="btn" data-act="send">Send</button></form>`;
  }
  function send(text) { text = (text || '').trim(); if (!text) return; msgs.push({ me: 1, text }); try { reply(text); } catch (e) { bot('Sorry, something went wrong working that out. Your data was not changed.'); } keep(); App.render(); setTimeout(() => { window.scrollTo(0, document.body.scrollHeight); const i = document.getElementById('aq'); if (i) i.focus(); }, 30); }
  return {
    render,
    mount: el => { const i = el.querySelector('#aq'); if (i) i.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); send(i.value); } }); },
    acts: {
      send: () => send(document.getElementById('aq').value), ask: t => send(t.dataset.v), clear: () => { msgs = []; pend = {}; keep(); App.render(); },
      on: () => App.act(() => { App.D.settings.aiOn = true; }),
      do: t => { const id = t.dataset.id;
        if (id.indexOf('tpl:') === 0) { Screens.habitForm.reset(); App.push('habitForm', { tpl: id.slice(4) }); return; }
        const m = msgs.find(x => (x.acts || []).some(a => a.id === id)), a = m && m.acts.find(x => x.id === id);
        if (id.indexOf('edit:') === 0 && a && a.hab) { const h = a.hab; m.acts.forEach(x => x.done = true); keep(); App.act(() => App.D.habits.push(h), null); Screens.habitForm.reset(); App.push('habitForm', { id: h.id }); UI.toast('Added. Adjust it and tap Save.'); return; }
        const fn = pend[id]; if (!fn) { UI.toast('This suggestion has expired. Ask again.'); return; }
        if (App.act(fn, 'Done.')) { delete pend[id]; if (a) { if (m.acts.some(x => x.id.indexOf('edit:') === 0)) m.acts.forEach(x => x.done = true); else a.done = true; } bot('Done. You can undo from the message at the bottom of the screen.'); App.render(); } }
    }
  };
})();
