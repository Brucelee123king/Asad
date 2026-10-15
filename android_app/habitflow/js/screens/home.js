/* Home dashboard */
Screens.home = (() => {
  const E = s => UI.esc(s);
  const MOTIV = {
    none: ['Small steps add up. Pick one habit and start.', 'Every streak starts with day one.'],
    low: ['A good start. Keep the momentum going.', 'Progress, not perfection.'],
    mid: ['Over halfway there. You are doing great.', 'Nice rhythm today. Keep it up.'],
    high: ['Almost done. Finish strong!', 'So close to a perfect day.'],
    done: ['Every habit done today. Take a moment to enjoy it.', 'Perfect day. Rest well and come back tomorrow.']
  };
  function greet() { const h = new Date().getHours(); return h < 5 ? 'Good night' : h < 12 ? 'Good morning' : h < 17 ? 'Good afternoon' : 'Good evening'; }
  function render() {
    const D = App.D, t = App.tdy(), date = App.ui.date, s = D.settings, hc = s.homeCards, c = Core.dayCompletion(D, date, t), name = s.name ? ', ' + E(s.name) : '';
    const any = Core.live(D).length;
    let h = `<div class="top"><h1><small>${UI.fmtDate(t, s.dateFmt, true)}</small>${greet()}${name}</h1>
      ${s.aiOn ? `<button class="ib" data-act="go" data-s="assistant" aria-label="Assistant">${UI.icon('spark')}</button>` : ''}
      <button class="ib ac" data-act="go" data-s="habitForm" aria-label="Add habit">${UI.icon('plus')}</button></div><div class="stack">`;
    if (hc.week) h += `<div class="week">${HC.weekDays(date).map(d => { const cc = Core.dayCompletion(D, d, t);
      return `<button class="wd ${d === date ? 'on' : ''}" data-act="day" data-d="${d}" aria-label="${UI.fmtDate(d, s.dateFmt, true)}, ${cc.pct}%">${UI.DN[Core.dow(d)].slice(0, 3)}${UI.ring(cc.total ? cc.pct : 0, 34, 4, `<b style="font-size:.78rem">${+d.slice(8)}</b>`, d > t ? 'var(--ln)' : null)}</button>`; }).join('')}</div>`;
    if (!any) {
      h += `<div class="card">${UI.empty('\u{1F331}', 'Welcome to HabitFlow', 'Add your first habit to start tracking. Pick a ready-made template or create your own.',
        '<div class="row" style="justify-content:center;flex-wrap:wrap"><button class="btn" data-act="go" data-s="library">Browse templates</button><button class="btn sec" data-act="go" data-s="habitForm">Create from scratch</button></div>')}</div></div>`;
      return h;
    }
    const pctTxt = c.total ? c.pct : 0;
    h += `<div class="card"><div class="row" style="gap:18px">${UI.ring(pctTxt, 108, 11, `<b>${pctTxt}%</b><span>${date === t ? 'today' : UI.fmtDate(date, s.dateFmt).replace(/, \d{4}$/, '')}</span>`)}
      <div class="grow"><div class="b" style="font-size:1.05rem">${c.done} of ${c.total} done</div><div class="small muted" style="margin-bottom:10px">${c.total ? (c.done === c.total ? 'Everything is done for today.' : (c.total - c.done - c.missed.length) + ' still to do') : 'Nothing scheduled'}${c.flex.length ? ' · ' + c.flex.length + ' flexible' : ''}</div>
      <div class="stats" style="grid-template-columns:repeat(3,1fr);gap:6px"><div class="stat"><b>${c.total - c.done - c.missed.length}</b><span>Left</span></div><div class="stat"><b>${c.skipped.length}</b><span>Skipped</span></div><div class="stat"><b>${c.missed.length}</b><span>Missed</span></div></div></div></div>
      ${hc.motivation ? `<p class="small muted" style="margin-top:12px">${motiv(c)}</p>` : ''}</div>`;
    h += `<div class="chips scroll"><button class="chip" data-act="go" data-s="habitForm">${UI.icon('plus', 16)}Habit</button><button class="chip" data-act="tab" data-v="focus">${UI.icon('focus', 16)}Focus</button>
      <button class="chip" data-act="go" data-s="entry">${UI.icon('note', 16)}Journal</button>${s.moodOn ? `<button class="chip" data-act="mood">${UI.icon('mood', 16)}Mood</button>` : ''}<button class="chip" data-act="go" data-s="goals">${UI.icon('target', 16)}Goals</button></div>`;
    const usedCats = D.cats.filter(ct => Core.live(D).some(x => Core.habitCats(x).indexOf(ct.id) >= 0));
    if (usedCats.length > 1) h += `<div class="chips scroll"><button class="chip ${!App.ui.f.homeCat ? 'on' : ''}" data-act="hcat" data-v="">All</button>${usedCats.map(ct => `<button class="chip ${App.ui.f.homeCat === ct.id ? 'on' : ''}" data-act="hcat" data-v="${ct.id}">${E(ct.icon)} ${E(ct.name)}</button>`).join('')}</div>`;
    const secs = HC.sections(date, { cat: App.ui.f.homeCat });
    h += secs || `<div class="card flat">${UI.empty('\u{1F33F}', 'Nothing scheduled', date > t ? 'No habits are scheduled for this day.' : 'No habits are scheduled for this day. Enjoy the rest or add a habit.', '')}</div>`;
    // priorities
    const pri = c.remaining.filter(x => x.priority);
    if (date === t && (pri.length || c.remaining.length)) { const list = (pri.length ? pri : c.remaining).slice(0, 3);
      h += `<div class="card"><h2>${UI.icon('star', 16)} Today's priorities</h2><ul class="tl">${list.map(x => `<li><span>${E(x.icon)}</span><span class="grow">${E(x.name)}</span><span class="muted small">${E(HC.goalText(x))}</span></li>`).join('')}</ul></div>`; }
    let wide = '';
    if (hc.streaks) { const st = Core.live(D).map(x => ({ x, n: Core.currentStreak(D, x, t) })).filter(o => o.n > 0).sort((a, b) => b.n - a.n).slice(0, 3);
      wide += `<div class="card"><h2>${UI.icon('flame', 16)} Streaks</h2>${st.length ? `<ul class="tl">${st.map(o => `<li><span>${E(o.x.icon)}</span><span class="grow">${E(o.x.name)}</span><b>${o.n}</b><span class="muted small">${Core.isFlex(o.x, t) ? Core.schedFor(o.x, t).per + (o.n === 1 ? '' : 's') : (o.n === 1 ? 'day' : 'days')}</span></li>`).join('')}</ul>` : '<p class="muted small">Complete a habit to start a streak.</p>'}</div>`; }
    if (hc.reminders) { const now = new Date(), rem = Core.upcomingReminders(D, now, 1, 4);
      wide += `<div class="card"><h2>${UI.icon('bell', 16)} Upcoming reminders</h2>${rem.length ? `<ul class="tl">${rem.map(r => `<li><span>${UI.fmtTime(r.time, s.timeFmt)}</span><span class="grow ell">${E(r.title)}</span></li>`).join('')}</ul>` : '<p class="muted small">No more reminders today.' + (s.notif ? '' : ' Reminders are turned off in Settings.') + '</p>'}</div>`; }
    const goals = D.goals.filter(g => !g.archived).slice(0, 3);
    if (goals.length) wide += `<div class="card"><h2>${UI.icon('target', 16)} Goals <button class="lnk" data-act="go" data-s="goals">All</button></h2>${goals.map(g => { const p = Core.goalProgress(D, g, t);
      return `<button class="li" data-act="go" data-s="goal" data-id="${g.id}"><span class="bubble">${E(g.icon || '\u{1F3AF}')}</span><span class="grow"><span class="t">${E(g.name)}</span><span class="s" style="display:block">${p.sum}/${p.target} ${E(g.unit || '')} · ${p.pct}%</span>${UI.pbar(p.pct, g.color)}</span></button>`; }).join('')}</div>`;
    if (hc.recent) { const rec = c.finished.map(x => ({ x, at: (Core.getEntry(D, x, date) || {}).at || 0 })).sort((a, b) => b.at - a.at).slice(0, 4);
      if (rec.length) wide += `<div class="card"><h2>${UI.icon('check', 16)} Recently completed</h2><ul class="tl">${rec.map(o => `<li><span>${E(o.x.icon)}</span><span class="grow">${E(o.x.name)}</span><span class="muted small">${o.at ? new Date(o.at).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit', hour12: s.timeFmt !== '24' }) : ''}</span></li>`).join('')}</ul></div>`; }
    h += `<div class="wide2 stack">${wide}</div>`;
    h += `<div class="card flat"><h2>${UI.icon('focus', 16)} Focus</h2><div class="row"><p class="small muted grow">Start a timer for deep work, study or meditation and link it to a habit.</p><button class="btn sm" data-act="tab" data-v="focus">Start</button></div></div>`;
    return h + '</div>';
  }
  function motiv(c) { const k = !c.total ? 'none' : c.done === c.total ? 'done' : c.pct >= 75 ? 'high' : c.pct >= 40 ? 'mid' : c.done ? 'low' : 'none'; const l = MOTIV[k]; return l[new Date().getDate() % l.length]; }
  return {
    render,
    acts: {
      day: t => { App.ui.date = t.dataset.d; App.render(); },
      hcat: t => { App.ui.f.homeCat = t.dataset.v; App.render(); },
      mood: () => Screens.journal.moodSheet()
    }
  };
})();
