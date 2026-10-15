/* First-run welcome & optional personalization questions */
Screens.onboarding = (() => {
  const E = s => UI.esc(s); let step = 0; const A = { goals: [], areas: [], style: 'simple', wake: '07:00', sleep: '23:00', rem: true, remv: 'yes', track: 'habits', picks: [] };
  const GOALS = [['health', 'Be healthier'], ['fit', 'Get fit'], ['learn', 'Learn & study'], ['prod', 'Be more productive'], ['calm', 'Reduce stress'], ['sleep', 'Sleep better'], ['quit', 'Break a bad habit'], ['routine', 'Build a routine']];
  const AREAS = ['Health', 'Fitness', 'Learning', 'Productivity', 'Mindfulness', 'Relationships', 'Finances', 'Home'];
  const SUG = { health: ['Drink water', 'Eat fruit & veg'], fit: ['Workout', 'Walk 8,000 steps'], learn: ['Study', 'Read'], prod: ['Plan the day', 'Deep work block'], calm: ['Meditate', 'Gratitude'], sleep: ['Sleep by 11 PM', 'Evening wind-down'], quit: ['No phone in bed', 'No sugar'], routine: ['Morning routine', 'Wake up early'] };
  const steps = ['welcome', 'goals', 'areas', 'style', 'times', 'rem', 'track', 'picks'];
  function render() {
    const s = steps[step], foot = (next, label) => `<div class="foot"><button class="btn sec" data-act="obback">Back</button><button class="btn" data-act="${next || 'obnext'}">${label || 'Continue'}</button></div>`;
    const chips = (list, key, multi) => `<div class="chips">${list.map(x => { const v = Array.isArray(x) ? x[0] : x, l = Array.isArray(x) ? x[1] : x, on = multi ? A[key].indexOf(v) >= 0 : A[key] === v; return `<button class="chip ${on ? 'on' : ''}" style="min-height:44px" data-act="obpick" data-k="${key}" data-v="${E(v)}" data-m="${multi ? 1 : ''}">${E(l)}</button>`; }).join('')}</div>`;
    if (s === 'welcome') return `<div class="ob" style="justify-content:center;text-align:center;align-items:center"><img class="logo-img" src="icon.png" alt="HabitFlow logo"><h1 style="margin-top:20px">HabitFlow</h1><p class="muted" style="max-width:340px">Build good habits, break unwanted ones and see your progress, one day at a time.</p>
      <ul class="tl" style="text-align:left;margin:26px 0;max-width:340px">${['Track habits, routines and goals', 'Streaks, calendars and charts from your real records', 'Reminders, focus timer, journal and mood', 'Private: your data stays on this phone'].map(x => `<li>${UI.icon('check', 18)}<span>${x}</span></li>`).join('')}</ul>
      <button class="btn full" style="max-width:340px" data-act="obnext">Get started</button><button class="lnk" style="margin-top:16px" data-act="obskip">Skip setup</button>
      <p class="hint" style="margin-top:24px">By continuing you agree to the <button class="lnk xs" data-act="obdoc" data-v="terms">Terms</button> and <button class="lnk xs" data-act="obdoc" data-v="privacy">Privacy policy</button>.</p></div>`;
    let body = '', title = '', sub = '';
    if (s === 'goals') { title = 'What are your main goals?'; sub = 'Pick any. This helps suggest habits.'; body = chips(GOALS, 'goals', 1); }
    if (s === 'areas') { title = 'Which areas of life do you want to improve?'; body = chips(AREAS, 'areas', 1); }
    if (s === 'style') { title = 'How detailed do you want it?'; body = `<div class="stack">${[['simple', 'Simple tracker', 'Just check things off. Clean and quick.'], ['detailed', 'Detailed planner', 'Amounts, durations, checklists, goals and reflections.']].map(o => `<button class="card ${A.style === o[0] ? '' : 'flat'}" style="text-align:left;${A.style === o[0] ? 'border-color:var(--ac)' : ''}" data-act="obpick" data-k="style" data-v="${o[0]}"><b>${o[1]}</b><p class="small muted">${o[2]}</p></button>`).join('')}</div>`; }
    if (s === 'times') { title = 'When do you usually wake up and sleep?'; sub = 'Used to suggest reminder times.'; body = `<div class="row"><div class="fld grow"><label>Wake up</label><input class="inp" type="time" value="${A.wake}" data-change="obwake"></div><div class="fld grow"><label>Go to sleep</label><input class="inp" type="time" value="${A.sleep}" data-change="obsleep"></div></div>`; }
    if (s === 'rem') { title = 'Would you like reminders?'; body = chips([['yes', 'Yes, remind me'], ['no', 'No reminders']], 'remv'); }
    if (s === 'track') { title = 'What do you want to track?'; body = chips([['habits', 'Habits'], ['goals', 'Goals'], ['both', 'Both']], 'track'); }
    if (s === 'picks') { title = 'Start with a few habits?'; sub = 'Pick any to add now. You can change everything later.';
      const names = Array.from(new Set((A.goals.length ? A.goals : ['health', 'routine', 'learn']).reduce((a, g) => a.concat(SUG[g] || []), []))).slice(0, 8);
      body = `<div class="stack">${names.map(n => { const t = TEMPLATES.find(x => x.name === n); if (!t) return ''; const on = A.picks.indexOf(t.id) >= 0; return `<button class="hc" style="--hcol:${t.color};text-align:left" data-act="obtpl" data-v="${t.id}"><span class="hi">${t.icon}</span><span class="main"><span class="nm">${E(t.name)}</span><span class="sub">${E(t.area)}</span></span><span class="ck ${on ? 'on' : ''}">${UI.icon('check', 20)}</span></button>`; }).join('')}</div>`;
      return frame(title, sub, body, foot('obfinish', A.picks.length ? 'Add ' + A.picks.length + ' & finish' : 'Finish')); }
    return frame(title, sub, body, foot());
  }
  const frame = (title, sub, body, foot) => `<div class="ob"><div class="row"><span class="stepn grow">Step ${step} of ${steps.length - 1}</span><button class="lnk small" data-act="obskip">Skip setup</button></div><h1>${title}</h1>${sub ? `<p class="muted">${sub}</p>` : ''}<div class="body">${body}</div>${foot}</div>`;
  function finish(add) {
    const D = App.D, p = D.settings.profile; Object.assign(p, { goals: A.goals.map(g => (GOALS.find(x => x[0] === g) || [0, g])[1]), areas: A.areas, style: A.style, wake: A.wake, sleep: A.sleep, wantRem: A.rem, track: A.track });
    if (add) { const remFor = part => ({ morning: A.wake.replace(/:(\d\d)/, ':30'), afternoon: '13:00', evening: '19:00', night: (Core.pad((+A.sleep.slice(0, 2) + 23) % 24)) + A.sleep.slice(2), anytime: '12:00' })[part] || '09:00';
      A.picks.forEach((id, i) => { const t = TEMPLATES.find(x => x.id === id); D.habits.push({ id: Core.uid(), created: Date.now(), start: App.tdy(), name: t.name, icon: t.icon, color: t.color, type: t.type, goal: JSON.parse(JSON.stringify(t.goal)), sched: JSON.parse(JSON.stringify(t.sched)), part: t.part, cats: AREA_TO_CAT[t.area] ? [AREA_TO_CAT[t.area]] : [], check: (t.check || []).map((x, k) => ({ id: 'c' + k, t: x })), rem: { on: A.rem, times: [remFor(t.part)], byDay: {}, msg: '' }, order: i + 1 }); }); }
    D.settings.onboarded = true; App.save(); App.go('home');
    if (add && A.rem && A.picks.length && App.native && App.native.notifStatus && App.native.notifStatus() !== 'granted') setTimeout(async () => { if (await UI.confirm('Allow notifications?', 'HabitFlow needs permission to show your reminders.', 'Allow')) App.native.requestNotifPermission(); }, 400);
  }
  return {
    render,
    acts: {
      obnext: () => { step = Math.min(steps.length - 1, step + 1); App.render(); window.scrollTo(0, 0); }, obback: () => { step = Math.max(0, step - 1); App.render(); },
      obskip: () => finish(false), obfinish: () => finish(true),
      obdoc: t => UI.sheet(Screens.legal.render({ doc: t.dataset.v }).replace(/<div class="top">[\s\S]*?<\/div>/, '<h3>' + (t.dataset.v === 'privacy' ? 'Privacy policy' : 'Terms of use') + '</h3>')),
      obpick: t => { const k = t.dataset.k, v = t.dataset.v; if (k === 'remv') { A.remv = v; A.rem = v === 'yes'; } else if (t.dataset.m) { const i = A[k].indexOf(v); if (i >= 0) A[k].splice(i, 1); else A[k].push(v); } else A[k] = v; App.render(); },
      obtpl: t => { const i = A.picks.indexOf(t.dataset.v); if (i >= 0) A.picks.splice(i, 1); else A.picks.push(t.dataset.v); App.render(); }
    },
    changes: { obwake: t => { A.wake = t.value; }, obsleep: t => { A.sleep = t.value; } }
  };
})();
