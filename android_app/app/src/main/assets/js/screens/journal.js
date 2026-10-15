/* Journal: daily check-in (day / week / month), notes & reflections, mood */
Screens.journal = (() => {
  const E = s => UI.esc(s);
  const MOODS = [[1, '\u{1F61E}', 'Very low'], [2, '\u{1F615}', 'Low'], [3, '\u{1F610}', 'Okay'], [4, '\u{1F642}', 'Good'], [5, '\u{1F604}', 'Great']];
  const PROMPTS = { daily: ['What went well today?', 'Which habit was easiest to complete?', 'What made a habit difficult?', 'What would I like to improve tomorrow?'],
    weekly: ['What was my biggest win this week?', 'Which habit slipped, and why?', 'What one change will I make next week?'],
    monthly: ['What am I most proud of this month?', 'Which habits stuck? Which did not?', 'What will I focus on next month?'] };
  function render() {
    const seg = App.ui.seg.journal || 'checkin';
    let h = `<div class="top"><h1>Journal</h1><button class="ib ac" data-act="go" data-s="entry" aria-label="New journal entry">${UI.icon('edit')}</button></div>
      ${UI.seg('journal', [['checkin', 'Check-in'], ['notes', 'Notes'], ['mood', 'Mood']], seg)}<div class="stack mt">`;
    h += seg === 'notes' ? notes() : seg === 'mood' ? mood() : checkin();
    return h + '</div>';
  }
  /* ---------- check-in ---------- */
  function checkin() {
    const D = App.D, t = App.tdy(), date = App.ui.date, v = App.ui.seg.jview || 'day', s = D.settings;
    let h = `<div class="row"><button class="ib" data-act="dnav" data-v="-1" aria-label="Previous">${UI.icon('left')}</button>
      <div class="grow" style="text-align:center"><b>${v === 'month' ? UI.MFULL[+date.slice(5, 7) - 1] + ' ' + date.slice(0, 4) : v === 'week' ? 'Week of ' + UI.fmtDate(HC.weekDays(date)[0], s.dateFmt) : UI.fmtDate(date, s.dateFmt, true)}</b>
      ${date !== t ? `<div><button class="lnk small" data-act="dtoday">Back to today</button></div>` : ''}</div>
      <button class="ib" data-act="dnav" data-v="1" aria-label="Next">${UI.icon('right')}</button></div>
      <div class="row">${UI.seg('jview', [['day', 'Day'], ['week', 'Week'], ['month', 'Month']], v)}
      <select class="inp" style="width:auto;min-height:42px" data-change="sort" aria-label="Sort habits"><option value="manual" ${s.sort === 'manual' || !s.sort ? 'selected' : ''}>Manual</option><option value="alpha" ${s.sort === 'alpha' ? 'selected' : ''}>A–Z</option><option value="time" ${s.sort === 'time' ? 'selected' : ''}>Reminder time</option></select></div>`;
    if (!Core.live(D).length) return h + `<div class="card">${UI.empty('\u{1F4CB}', 'No habits yet', 'Create a habit to start checking in.', '<button class="btn" data-act="go" data-s="library">Browse templates</button>')}</div>`;
    if (v === 'day') {
      const c = Core.dayCompletion(D, date, t);
      h += `<div class="card flat row">${UI.ring(c.total ? c.pct : 0, 64, 7)}<div class="grow small"><b>${c.done} of ${c.total}</b> completed<div class="muted">${c.skipped.length} skipped · ${c.missed.length} missed${c.flex.length ? ' · ' + c.flex.length + ' flexible' : ''}</div></div></div>`;
      h += HC.sections(date) || `<div class="card flat">${UI.empty('\u{1F33F}', 'Nothing scheduled', 'No habits are scheduled on this day.')}</div>`;
      const notesToday = Core.live(D).map(x => ({ x, e: Core.getEntry(D, x, date) })).filter(o => o.e && (o.e.note || (o.e.occ && o.e.occ.length)));
      if (notesToday.length) h += `<div class="card"><h2>${UI.icon('note', 16)} Notes for this day</h2><ul class="tl">${notesToday.map(o => `<li><span>${E(o.x.icon)}</span><span class="grow"><b>${E(o.x.name)}</b><br><span class="small">${E(o.e.note || '')}${o.e.occ ? o.e.occ.filter(q => q.trig).map(q => ' · trigger: ' + E(q.trig)).join('') : ''}</span></span></li>`).join('')}</ul></div>`;
    } else if (v === 'week') {
      const days = HC.weekDays(date), hs = HC.sortHabits(Core.live(D), s.sort);
      h += `<div class="card wkgrid"><table><thead><tr><th></th>${days.map(d => `<th${d === t ? ' style="color:var(--ac)"' : ''}>${UI.DN[Core.dow(d)].slice(0, 2)}<br>${+d.slice(8)}</th>`).join('')}</tr></thead><tbody>
        ${hs.map(x => `<tr><td title="${E(x.name)}">${E(x.icon)} ${E(x.name)}</td>${days.map(d => { const st = Core.status(D, x, d, t);
          return `<td>${st === 'off' ? '<span class="dot off">·</span>' : `<button class="dot ${st === 'failed' ? 'missed' : st}" data-act="wcell" data-h="${x.id}" data-d="${d}" aria-label="${E(x.name)} ${d}: ${UI.STAT[st].l}">${UI.STAT[st].i || ''}</button>`}</td>`; }).join('')}</tr>`).join('')}</tbody></table>
        <div class="legend"><span><i style="background:var(--done)"></i>Completed</span><span><i style="background:var(--part)"></i>In progress</span><span><i style="background:var(--miss)"></i>Missed / not done</span><span><i style="border:1px dashed var(--skip)"></i>Skipped</span></div></div>`;
    } else {
      h += `<div class="card">${monthCal(date, d => { const c = Core.dayCompletion(D, d, t); return c.total && d <= t ? c.pct : null; })}<p class="hint mt">Tap a day to open its check-in.</p></div>`;
    }
    return h;
  }
  function monthCal(date, valFn) {
    const D = App.D, t = App.tdy(), y = +date.slice(0, 4), m = +date.slice(5, 7), first = y + '-' + Core.pad(m) + '-01', ws = D.settings.weekStart, lead = (Core.dow(first) - ws + 7) % 7, n = Core.dim(y, m);
    let h = '<div class="cal">' + [0, 1, 2, 3, 4, 5, 6].map(i => `<div class="h">${UI.DN[(i + ws) % 7].slice(0, 2)}</div>`).join('');
    for (let i = 0; i < lead; i++) h += '<div></div>';
    for (let d = 1; d <= n; d++) { const ds = y + '-' + Core.pad(m) + '-' + Core.pad(d), v = valFn(ds);
      h += `<button class="c ${ds === t ? 'today' : ''}" data-act="calday" data-d="${ds}" style="${v == null ? '' : 'background:color-mix(in srgb,var(--ac) ' + (12 + v * .8) + '%,var(--sf2));' + (v > 60 ? 'color:#fff' : '')}" aria-label="${ds}${v == null ? '' : ': ' + v + '%'}">${d}</button>`; }
    return h + '</div>';
  }
  /* ---------- notes & reflections ---------- */
  function notes() {
    const D = App.D, f = App.ui.f, q = (f.jq || '').toLowerCase(), kind = f.jkind || 'all', per = f.jper || 'all', t = App.tdy(), tag = f.jtag || '';
    const from = per === 'week' ? Core.addDays(t, -6) : per === 'month' ? Core.addDays(t, -29) : per === 'year' ? Core.addDays(t, -364) : '0000';
    let items = [];
    if (kind !== 'habit') D.journal.forEach(j => items.push({ type: 'j', date: j.date, ts: j.ts, j }));
    if (kind === 'all' || kind === 'habit') Object.keys(D.entries).forEach(k => { const e = D.entries[k]; if (!e.note) return; const p = k.split('|'), x = App.habit(p[0]); if (x) items.push({ type: 'n', date: p[1], ts: 0, x, e }); });
    items = items.filter(it => it.date >= from && (kind === 'all' || kind === 'habit' || (it.j && it.j.kind === kind)));
    if (tag) items = items.filter(it => it.j && (it.j.tags || []).indexOf(tag) >= 0);
    if (q) items = items.filter(it => (it.j ? (it.j.text + ' ' + (it.j.tags || []).join(' ')) : (it.e.note + ' ' + it.x.name)).toLowerCase().indexOf(q) >= 0);
    items.sort((a, b) => b.date.localeCompare(a.date) || b.ts - a.ts);
    const tags = {}; D.journal.forEach(j => (j.tags || []).forEach(x => tags[x] = 1));
    let h = `<div class="row"><div class="grow" style="position:relative"><input class="inp" type="search" placeholder="Search notes" value="${E(f.jq || '')}" data-input="jq" aria-label="Search notes"></div>
      <select class="inp" style="width:auto" data-change="jper" aria-label="Date range"><option value="all">All time</option><option value="week" ${per === 'week' ? 'selected' : ''}>7 days</option><option value="month" ${per === 'month' ? 'selected' : ''}>30 days</option><option value="year" ${per === 'year' ? 'selected' : ''}>1 year</option></select></div>
      <div class="chips scroll">${[['all', 'All'], ['daily', 'Daily'], ['weekly', 'Weekly reflections'], ['monthly', 'Monthly reflections'], ['habit', 'Habit notes']].map(k => `<button class="chip ${kind === k[0] ? 'on' : ''}" data-act="jkind" data-v="${k[0]}">${k[1]}</button>`).join('')}</div>
      ${Object.keys(tags).length ? `<div class="chips scroll">${Object.keys(tags).sort().map(x => `<button class="chip ${tag === x ? 'on' : ''}" data-act="jtag" data-v="${E(x)}">#${E(x)}</button>`).join('')}</div>` : ''}
      <div class="card flat row"><span style="font-size:1.6rem">\u{1F4DD}</span><div class="grow small"><b>${Core.dow(t) === 0 || Core.dow(t) === 6 ? 'Time for a weekly reflection' : 'Reflect on your day'}</b><div class="muted">${E(PROMPTS[Core.dow(t) === 0 ? 'weekly' : 'daily'][new Date().getDate() % 3])}</div></div>
      <button class="btn sm" data-act="go" data-s="entry" data-kind="${Core.dow(t) === 0 || Core.dow(t) === 6 ? 'weekly' : 'daily'}">Write</button></div>`;
    if (!items.length) return h + `<div class="card flat">${UI.empty('\u{1F4D3}', q || tag || kind !== 'all' || per !== 'all' ? 'No matching notes' : 'Your journal is empty', q ? 'Try a different search.' : 'Write a short entry about your day. It stays private on this device.')}</div>`;
    return h + `<div class="card"><div class="list">${items.slice(0, 200).map(it => it.j
      ? `<button class="li" data-act="go" data-s="entry" data-id="${it.j.id}"><span class="bubble">${it.j.mood ? MOODS[it.j.mood - 1][1] : '\u{1F4DD}'}</span><span class="grow"><span class="t">${UI.fmtDate(it.date, App.D.settings.dateFmt)}${it.j.kind !== 'daily' ? ' · ' + (it.j.kind === 'weekly' ? 'Weekly reflection' : 'Monthly reflection') : ''}</span><span class="s ell" style="display:block">${E(it.j.text.slice(0, 120))}</span></span>${UI.icon('right', 18)}</button>`
      : `<button class="li" data-act="hmore" data-h="${it.x.id}" data-d="${it.date}"><span class="bubble">${E(it.x.icon)}</span><span class="grow"><span class="t">${E(it.x.name)} · ${UI.fmtDate(it.date, App.D.settings.dateFmt)}</span><span class="s ell" style="display:block">${E(it.e.note)}</span></span></button>`).join('')}</div></div>`;
  }
  /* ---------- mood ---------- */
  function mood() {
    const D = App.D, t = App.tdy();
    if (!D.settings.moodOn) return `<div class="card">${UI.empty('\u{1F642}', 'Mood tracking is off', 'Turn it on to log how you feel and compare it with your habits.', '<button class="btn" data-act="moodon">Turn on mood tracking</button>')}</div>`;
    const today = D.moods.find(m => m.date === t), from = Core.addDays(t, -29), days = Core.range(from, t);
    const vals = days.map(d => { const m = D.moods.filter(x => x.date === d); return m.length ? Math.round(m.reduce((a, x) => a + x.mood, 0) / m.length * 10) / 10 : null; });
    const cmp = Core.moodVsHabits(D, from, t, t);
    let h = `<div class="card"><h2>How are you feeling today?</h2><div class="row" style="justify-content:space-between">${MOODS.map(m => `<button class="bubble" style="width:54px;height:54px;font-size:1.7rem;${today && today.mood === m[0] ? 'outline:3px solid var(--ac)' : ''}" data-act="mood" data-v="${m[0]}" aria-label="${m[2]}">${m[1]}</button>`).join('')}</div>
      ${today ? `<p class="small muted mt">Logged: ${MOODS[today.mood - 1][2]}${today.note ? ' · ' + E(today.note) : ''}</p>` : ''}</div>`;
    h += `<div class="card"><h2>Last 30 days</h2>${D.moods.length ? UI.line([{ name: 'Mood', color: 'var(--ac)', vals }], days.map(d => +d.slice(8)), { max: 5, label: 'Mood over the last 30 days, scale 1 to 5' }) : '<p class="muted small">Log your mood to see a chart here.</p>'}</div>`;
    h += `<div class="card"><h2>Mood and habits</h2>${cmp.nHi + cmp.nLo >= 3 ? `<div class="stats"><div class="stat"><b>${cmp.hi == null ? '–' : cmp.hi}</b><span>Avg mood on days with 70%+ habits (${cmp.nHi})</span></div><div class="stat"><b>${cmp.lo == null ? '–' : cmp.lo}</b><span>Avg mood on other days (${cmp.nLo})</span></div></div>` : '<p class="muted small">Log your mood on a few more days to compare it with your habits.</p>'}
      <p class="hint mt">This is a personal observation from your own records, not a medical assessment, and it does not show cause and effect.</p></div>`;
    const hist = D.moods.slice().sort((a, b) => b.ts - a.ts).slice(0, 30);
    if (hist.length) h += `<div class="card"><h2>History</h2><div class="list">${hist.map(m => `<div class="li"><span class="bubble">${MOODS[m.mood - 1][1]}</span><span class="grow"><span class="t">${UI.fmtDate(m.date, D.settings.dateFmt)}</span><span class="s" style="display:block">${E(MOODS[m.mood - 1][2])}${m.note ? ' · ' + E(m.note) : ''}</span></span><button class="more" data-act="moodDel" data-id="${m.id}" aria-label="Delete mood entry">${UI.icon('trash', 18)}</button></div>`).join('')}</div></div>`;
    return h;
  }
  function moodSheet(pre) {
    const D = App.D, t = App.tdy(), ex = D.moods.find(m => m.date === t); let sel = pre || (ex && ex.mood) || 0;
    UI.sheet(`<h3>How are you feeling?</h3><div class="row" style="justify-content:space-between;margin-bottom:14px">${MOODS.map(m => `<button class="bubble" style="width:54px;height:54px;font-size:1.7rem" data-m="${m[0]}" aria-label="${m[2]}">${m[1]}</button>`).join('')}</div>
      <div class="fld"><label for="mn">Note (optional)</label><input class="inp" id="mn" maxlength="200" value="${E((ex && ex.note) || '')}" placeholder="What is affecting your mood?"></div><div class="err" id="me"></div><button class="btn full" id="ms">Save mood</button>`, sh => {
      const mark = () => sh.querySelectorAll('[data-m]').forEach(b => b.style.outline = +b.dataset.m === sel ? '3px solid var(--ac)' : ''); mark();
      sh.querySelectorAll('[data-m]').forEach(b => b.onclick = () => { sel = +b.dataset.m; mark(); });
      sh.querySelector('#ms').onclick = () => { if (!sel) { sh.querySelector('#me').textContent = 'Pick a mood first.'; return; } const note = sh.querySelector('#mn').value.trim().slice(0, 200); UI.closeSheet();
        App.act(() => { const m = D.moods.find(x => x.date === t); if (m) { m.mood = sel; m.note = note; m.ts = Date.now(); } else D.moods.push({ id: Core.uid(), date: t, ts: Date.now(), mood: sel, note }); }, 'Mood saved.'); };
    });
  }
  return {
    render, moodSheet, monthCal, MOODS, PROMPTS,
    acts: {
      dnav: t => { const v = App.ui.seg.jview || 'day', n = +t.dataset.v, d = App.ui.date;
        App.ui.date = v === 'month' ? (() => { const p = d.split('-').map(Number); const dt = new Date(p[0], p[1] - 1 + n, 1); return Core.ymd(dt); })() : Core.addDays(d, v === 'week' ? 7 * n : n); App.render(); },
      dtoday: () => { App.ui.date = App.tdy(); App.render(); },
      calday: t => { App.ui.date = t.dataset.d; App.ui.seg.jview = 'day'; App.render(); },
      wcell: t => { const h = App.habit(t.dataset.h), d = t.dataset.d; if (Core.goalKind(h) === 'check' && !Core.checkItems(h) && !Core.isNegative(h) && d <= App.tdy()) { const st = Core.status(App.D, h, d, App.tdy()); App.act(() => Core.setCheck(App.D, h, d, st !== 'done', App.tdy()), st !== 'done' ? 'Completed.' : 'Marked as not completed.'); } else App.moreSheet(h, d); },
      jkind: t => { App.ui.f.jkind = t.dataset.v; App.render(); },
      jtag: t => { App.ui.f.jtag = App.ui.f.jtag === t.dataset.v ? '' : t.dataset.v; App.render(); },
      mood: t => moodSheet(+t.dataset.v),
      moodon: () => App.act(() => { App.D.settings.moodOn = true; }, 'Mood tracking is on.', { noUndo: 1 }),
      moodDel: async t => { if (await UI.confirm('Delete this mood entry?', 'This cannot be undone.', 'Delete', true)) App.act(() => { App.D.moods = App.D.moods.filter(m => m.id !== t.dataset.id); }, 'Mood entry deleted.'); }
    },
    inputs: { jq: (t) => { App.ui.f.jq = t.value; clearTimeout(Screens.journal._qt); Screens.journal._qt = setTimeout(() => { const pos = t.selectionStart; App.render(); const n = document.querySelector('[data-input=jq]'); if (n) { n.focus(); try { n.setSelectionRange(pos, pos); } catch (e) { } } }, 250); } },
    changes: { sort: t => App.act(() => { App.D.settings.sort = t.value; }), jper: t => { App.ui.f.jper = t.value; App.render(); } }
  };
})();

/* Journal entry editor */
Screens.entry = (() => {
  const E = s => UI.esc(s); let draft = null, forId = null;
  function render(p) {
    const D = App.D, ex = p.id && D.journal.find(j => j.id === p.id);
    if (forId !== (p.id || 'new:' + (p.kind || ''))) { forId = p.id || 'new:' + (p.kind || ''); draft = ex ? JSON.parse(JSON.stringify(ex)) : { id: '', date: App.tdy(), kind: p.kind || 'daily', mood: 0, text: '', tags: [] }; }
    const prompts = Screens.journal.PROMPTS[draft.kind] || [];
    return `<div class="top"><button class="ib" data-act="back" aria-label="Back">${UI.icon('left')}</button><h1 class="t2">${ex ? 'Edit entry' : 'New entry'}</h1>${ex ? `<button class="ib" data-act="del" aria-label="Delete entry">${UI.icon('trash')}</button>` : ''}</div>
      <div class="card"><div class="row"><div class="fld grow"><label for="jd">Date</label><input class="inp" id="jd" type="date" max="${App.tdy()}" value="${draft.date}" data-input="f" data-k="date"></div>
      <div class="fld grow"><label for="jk">Type</label><select class="inp" id="jk" data-change="kind"><option value="daily">Daily entry</option><option value="weekly" ${draft.kind === 'weekly' ? 'selected' : ''}>Weekly reflection</option><option value="monthly" ${draft.kind === 'monthly' ? 'selected' : ''}>Monthly reflection</option></select></div></div>
      ${D.settings.moodOn ? `<div class="fld"><span class="lbl">Mood (optional)</span><div class="row" style="justify-content:space-between">${Screens.journal.MOODS.map(m => `<button class="bubble" style="width:48px;height:48px;font-size:1.5rem;${draft.mood === m[0] ? 'outline:3px solid var(--ac)' : ''}" data-act="jm" data-v="${m[0]}" aria-label="${m[2]}">${m[1]}</button>`).join('')}</div></div>` : ''}
      <div class="fld"><span class="lbl">Prompts</span><div class="chips">${prompts.map(q => `<button class="chip" data-act="prompt" data-v="${E(q)}">${E(q)}</button>`).join('')}</div></div>
      <div class="fld"><label for="jt">Entry</label><textarea class="inp" id="jt" style="min-height:200px" maxlength="10000" data-input="f" data-k="text" placeholder="Write freely. This stays private on this device.">${E(draft.text)}</textarea></div>
      <div class="fld"><label for="jg">Tags (comma separated)</label><input class="inp" id="jg" data-input="f" data-k="tags" value="${E((draft.tags || []).join(', '))}" placeholder="e.g. work, gratitude"></div>
      <div class="err" id="je"></div><button class="btn full" data-act="save">Save entry</button></div>`;
  }
  return {
    render,
    inputs: { f: t => { const k = t.dataset.k; draft[k] = k === 'tags' ? t.value.split(',').map(x => x.trim().toLowerCase().replace(/^#/, '')).filter(Boolean).slice(0, 10) : t.value; } },
    changes: { kind: t => { draft.kind = t.value; App.render(); } },
    acts: {
      jm: t => { draft.mood = draft.mood === +t.dataset.v ? 0 : +t.dataset.v; App.render(); },
      prompt: t => { draft.text = (draft.text ? draft.text.replace(/\s+$/, '') + '\n\n' : '') + t.dataset.v + '\n'; App.render(); const ta = document.getElementById('jt'); if (ta) { ta.focus(); ta.selectionStart = ta.value.length; } },
      save: () => { if (!draft.text.trim()) { document.getElementById('je').textContent = 'Write something before saving.'; return; } if (!draft.date || draft.date > App.tdy()) { document.getElementById('je').textContent = 'Pick a date that is today or earlier.'; return; }
        const D = App.D; App.act(() => { if (draft.id) { const i = D.journal.findIndex(j => j.id === draft.id); D.journal[i] = Object.assign({}, draft, { edited: Date.now() }); } else { draft.id = Core.uid(); draft.ts = Date.now(); D.journal.push(JSON.parse(JSON.stringify(draft))); }
          if (draft.mood && D.settings.moodOn && !D.moods.some(m => m.date === draft.date)) D.moods.push({ id: Core.uid(), date: draft.date, ts: Date.now(), mood: draft.mood, note: '' }); }, 'Entry saved.', { noUndo: 1 });
        forId = null; App.back(); },
      del: async () => { if (!(await UI.confirm('Delete this entry?', 'It will be removed permanently from this device.', 'Delete', true))) return; const id = draft.id; App.act(() => { App.D.journal = App.D.journal.filter(j => j.id !== id); }, 'Entry deleted.'); forId = null; App.back(); }
    }
  };
})();
