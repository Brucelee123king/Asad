/* Focus: countdown timer, stopwatch, Pomodoro. Time is derived from wall-clock timestamps,
   so it stays correct when the app is in the background or the screen is off. */
Screens.focus = (() => {
  const E = s => UI.esc(s), KEY = (window.__u || 'guest::') + 'habitflow.focus';
  let S = { mode: 'timer', running: false, startAt: 0, acc: 0, dur: 25 * 60, phase: 'focus', round: 1, label: '', hid: '', sound: 'none', vol: .35, pomo: { f: 25, s: 5, l: 15, r: 4 } };
  try { const x = JSON.parse(localStorage.getItem(KEY)); if (x) S = Object.assign(S, x); } catch (e) { }
  const persist = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { } };
  const elapsed = () => S.acc + (S.running ? (Date.now() - S.startAt) / 1000 : 0);
  const remaining = () => Math.max(0, S.dur - elapsed());
  const isCount = () => S.mode !== 'stopwatch';
  const phaseLen = ph => (ph === 'focus' ? S.pomo.f : ph === 'short' ? S.pomo.s : S.pomo.l) * 60;
  /* ---------- sound ---------- */
  let ac = null, src = null, gain = null;
  function startSound() {
    stopSound(); if (S.sound === 'none') return;
    try { ac = ac || new (window.AudioContext || window.webkitAudioContext)(); if (ac.state === 'suspended') ac.resume();
      const len = ac.sampleRate * 4, buf = ac.createBuffer(1, len, ac.sampleRate), d = buf.getChannelData(0); let last = 0;
      for (let i = 0; i < len; i++) { const w = Math.random() * 2 - 1; if (S.sound === 'white') d[i] = w * .5; else { last = (last + .02 * w) / 1.02; d[i] = last * 3.5; } }
      src = ac.createBufferSource(); src.buffer = buf; src.loop = true; gain = ac.createGain(); gain.gain.value = S.vol;
      let node = src; if (S.sound === 'rain') { const f = ac.createBiquadFilter(); f.type = 'highpass'; f.frequency.value = 400; src.connect(f); node = f; }
      node.connect(gain); gain.connect(ac.destination); src.start();
    } catch (e) { UI.toast('Sound is not available on this device.', { err: 1 }); }
  }
  function stopSound() { try { if (src) src.stop(); } catch (e) { } src = null; }
  function chime() { try { ac = ac || new (window.AudioContext || window.webkitAudioContext)(); [0, .25, .5].forEach((t, i) => { const o = ac.createOscillator(), g = ac.createGain(); o.frequency.value = [660, 880, 990][i]; g.gain.setValueAtTime(.0001, ac.currentTime + t); g.gain.exponentialRampToValueAtTime(.25, ac.currentTime + t + .02); g.gain.exponentialRampToValueAtTime(.0001, ac.currentTime + t + .4); o.connect(g); g.connect(ac.destination); o.start(ac.currentTime + t); o.stop(ac.currentTime + t + .45); }); } catch (e) { } try { navigator.vibrate && navigator.vibrate([200, 100, 200]); } catch (e) { } }
  /* ---------- native completion alarm ---------- */
  function armAlarm() { const N = App.native; if (!N || !N.setTimerAlarm || !isCount()) return; try { N.setTimerAlarm(Date.now() + remaining() * 1000, S.mode === 'pomo' ? (S.phase === 'focus' ? 'Focus session complete' : 'Break is over') : 'Timer finished', S.label || 'Open HabitFlow to continue.'); } catch (e) { } }
  function cancelAlarm() { const N = App.native; if (N && N.cancelTimerAlarm) try { N.cancelTimerAlarm(); } catch (e) { } }
  /* ---------- controls ---------- */
  function start() { if (isCount() && remaining() <= 0) return; S.running = true; S.startAt = Date.now(); persist(); armAlarm(); startSound(); App.render(); }
  function pause() { S.acc = elapsed(); S.running = false; persist(); cancelAlarm(); stopSound(); App.render(); }
  function reset() { S.running = false; S.acc = 0; if (S.mode === 'pomo') S.dur = phaseLen(S.phase); persist(); cancelAlarm(); stopSound(); App.render(); }
  function record(secs, mode) {
    const D = App.D, t = App.tdy(), sess = { id: Core.uid(), ts: Date.now(), date: t, secs: Math.round(secs), mode, label: S.label.trim().slice(0, 60), hid: S.hid || null }; let msg = 'Session saved: ' + UI.fmtDur(secs) + '.';
    App.act(() => {
      D.focus.push(sess); const h = S.hid && App.habit(S.hid);
      if (h) { try { if (Core.goalKind(h) === 'time') { Core.addValue(D, h, t, Math.round(secs / 60), t); msg += ' Added ' + Math.round(secs / 60) + ' min to ' + h.name + '.'; } else if (!Core.isNegative(h) && Core.status(D, h, t, t) !== 'done') { Core.setCheck(D, h, t, true, t); msg += ' ' + h.name + ' marked complete.'; } }
        catch (e) { msg += ' (' + h.name + ': ' + e.message + ')'; } }
    }, null); UI.toast(msg, { ms: 4500 });
  }
  function complete() {
    const secs = S.dur; S.running = false; S.acc = 0; stopSound(); chime();
    if (S.mode === 'timer') { record(secs, 'timer'); }
    else if (S.mode === 'pomo') {
      if (S.phase === 'focus') { record(secs, 'pomodoro'); S.phase = S.round % S.pomo.r === 0 ? 'long' : 'short'; }
      else { S.phase = 'focus'; S.round++; UI.toast('Break over. Ready for the next focus round?'); }
      S.dur = phaseLen(S.phase);
    }
    persist(); App.render();
  }
  function stopwatchSave() { const secs = elapsed(); S.running = false; S.acc = 0; stopSound(); persist(); if (secs < 60) { UI.toast('Sessions under 1 minute are not saved.'); App.render(); return; } record(secs, 'stopwatch'); App.render(); }
  function tick() {
    if (S.running && isCount() && remaining() <= 0) { complete(); return; }
    const el = document.getElementById('ftm'); if (!el) return;
    const v = isCount() ? remaining() : elapsed(); el.textContent = UI.clock(v);
    const arc = document.querySelector('#fring .ring-arc'); if (arc && isCount()) { const r = +arc.getAttribute('r'), C = 2 * Math.PI * r; arc.setAttribute('stroke-dasharray', ((1 - remaining() / S.dur) * C) + ' ' + C); }
  }
  /* ---------- view ---------- */
  function render() {
    const D = App.D, t = App.tdy(), hs = Core.live(D);
    const today = D.focus.filter(f => f.date === t), wkFrom = Core.addDays(t, -6), week = D.focus.filter(f => f.date >= wkFrom), all = D.focus.reduce((a, f) => a + f.secs, 0);
    const v = isCount() ? remaining() : elapsed(), pct = isCount() ? (1 - v / S.dur) * 100 : 0, idle = !S.running && S.acc === 0;
    let h = `<div class="top"><h1>Focus</h1></div><div class="stack">${UI.seg('fmode', [['timer', 'Timer'], ['stopwatch', 'Stopwatch'], ['pomo', 'Pomodoro']], S.mode)}
      <div class="card"><div class="timer"><div id="fring">${UI.ring(pct, 230, 14, `<div class="tm" id="ftm">${UI.clock(v)}</div><span>${S.mode === 'pomo' ? (S.phase === 'focus' ? 'Focus · round ' + S.round : S.phase === 'short' ? 'Short break' : 'Long break') : S.mode === 'timer' ? 'Countdown' : 'Stopwatch'}${S.running ? '' : S.acc ? ' · paused' : ''}</span>`)}</div>
      <div class="ctrls">${S.running ? `<button class="btn sec" data-act="fpause">${UI.icon('pause', 18)} Pause</button>` : `<button class="btn" data-act="fstart">${UI.icon('play', 18)} ${S.acc ? 'Resume' : 'Start'}</button>`}
      ${S.mode === 'stopwatch' ? `<button class="btn ghost" data-act="fsave" ${elapsed() > 0 ? '' : 'disabled'}>${UI.icon('stop', 18)} Finish</button>` : `<button class="btn ghost" data-act="freset" ${idle ? 'disabled' : ''}>${UI.icon('reset', 18)} Reset</button>`}</div>
      ${S.mode === 'pomo' && S.phase !== 'focus' && !S.running ? `<button class="lnk small" data-act="fskipbreak">Skip break</button>` : ''}</div></div>`;
    if (S.mode === 'timer') h += `<div class="card"><h2>Duration</h2><div class="chips">${[5, 10, 15, 25, 45, 60, 90].map(m => `<button class="chip ${S.dur === m * 60 ? 'on' : ''}" data-act="fdur" data-v="${m}" ${idle ? '' : 'disabled'}>${m} min</button>`).join('')}</div>
      <div class="row mt"><input class="inp grow" type="number" min="1" max="600" placeholder="Custom minutes" id="fcm" ${idle ? '' : 'disabled'} aria-label="Custom minutes"><button class="btn sec sm" data-act="fcustom" ${idle ? '' : 'disabled'}>Set</button></div></div>`;
    if (S.mode === 'pomo') h += `<div class="card"><h2>Pomodoro settings</h2><div class="row">${[['f', 'Focus'], ['s', 'Short break'], ['l', 'Long break'], ['r', 'Rounds']].map(k => `<div class="fld grow"><label class="xs">${k[1]}</label><input class="inp" type="number" min="1" max="${k[0] === 'r' ? 12 : 180}" value="${S.pomo[k[0]]}" data-change="fpomo" data-k="${k[0]}" ${idle ? '' : 'disabled'}></div>`).join('')}</div><p class="hint">Minutes. A long break comes after every ${S.pomo.r} focus rounds. Only finished focus rounds are saved.</p></div>`;
    h += `<div class="card"><h2>Session</h2><div class="fld"><label for="flab">Label (optional)</label><input class="inp" id="flab" maxlength="60" value="${E(S.label)}" data-input="flabel" placeholder="e.g. Chapter 4, essay draft"></div>
      <div class="fld"><label for="fh">Count toward a habit</label><select class="inp" id="fh" data-change="fhabit"><option value="">None</option>${hs.filter(x => !Core.isNegative(x)).map(x => `<option value="${x.id}" ${S.hid === x.id ? 'selected' : ''}>${E(x.icon + ' ' + x.name)}${Core.goalKind(x) === 'time' ? ' (adds minutes)' : ' (marks complete)'}</option>`).join('')}</select></div>
      <div class="row"><div class="fld grow"><label for="fs">Background sound</label><select class="inp" id="fs" data-change="fsound">${[['none', 'None'], ['white', 'White noise'], ['brown', 'Brown noise'], ['rain', 'Soft rain']].map(o => `<option value="${o[0]}" ${S.sound === o[0] ? 'selected' : ''}>${o[1]}</option>`).join('')}</select></div>
      <div class="fld grow"><label for="fv">Volume</label><input id="fv" type="range" min="0.05" max="1" step="0.05" value="${S.vol}" data-input="fvol" style="width:100%;min-height:46px"></div></div>
      ${App.native ? '<p class="hint">You get a notification when the timer ends, even if HabitFlow is in the background.</p>' : '<p class="hint">The timer keeps correct time in the background. Keep the app open in a browser to hear the end chime.</p>'}</div>`;
    const days = Core.range(Core.addDays(t, -6), t).map(d => ({ l: UI.DN[Core.dow(d)].slice(0, 2), v: Math.round(D.focus.filter(f => f.date === d).reduce((a, f) => a + f.secs, 0) / 60) }));
    h += `<div class="card"><h2>Focus history</h2><div class="stats"><div class="stat"><b>${UI.fmtDur(today.reduce((a, f) => a + f.secs, 0))}</b><span>Today</span></div><div class="stat"><b>${UI.fmtDur(week.reduce((a, f) => a + f.secs, 0))}</b><span>Last 7 days</span></div><div class="stat"><b>${UI.fmtDur(all)}</b><span>All time · ${D.focus.length} sessions</span></div></div>
      <div class="mt">${UI.bars(days, { suf: 'm', label: 'Focus minutes per day, last 7 days' })}</div>
      ${D.focus.length ? `<div class="list mt">${D.focus.slice().sort((a, b) => b.ts - a.ts).slice(0, 15).map(f => { const hb = f.hid && App.habit(f.hid); return `<div class="li"><span class="bubble">${hb ? E(hb.icon) : '⏱️'}</span><span class="grow"><span class="t">${UI.fmtDur(f.secs)} · ${f.mode === 'pomodoro' ? 'Pomodoro' : f.mode === 'stopwatch' ? 'Stopwatch' : 'Timer'}</span><span class="s" style="display:block">${UI.fmtDate(f.date, D.settings.dateFmt)}, ${new Date(f.ts).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit', hour12: D.settings.timeFmt !== '24' })}${f.label ? ' · ' + E(f.label) : ''}${hb ? ' · ' + E(hb.name) : ''}</span></span><button class="more" data-act="fdel" data-id="${f.id}" aria-label="Delete session">${UI.icon('trash', 18)}</button></div>`; }).join('')}</div>` : '<p class="muted small mt">Finished sessions appear here.</p>'}</div></div>`;
    return h;
  }
  return {
    render, tick,
    acts: {
      seg: t => { if (t.dataset.seg !== 'fmode') return; if (S.running || S.acc) { UI.toast('Finish or reset the current session first.'); return; } S.mode = t.dataset.v; S.phase = 'focus'; S.round = 1; S.acc = 0; S.dur = S.mode === 'pomo' ? phaseLen('focus') : S.mode === 'timer' ? (S.dur || 1500) : 0; persist(); App.render(); },
      fstart: start, fpause: pause, freset: reset, fsave: stopwatchSave,
      fskipbreak: () => { S.phase = 'focus'; S.round++; S.dur = phaseLen('focus'); S.acc = 0; persist(); App.render(); },
      fdur: t => { S.dur = +t.dataset.v * 60; S.acc = 0; persist(); App.render(); },
      fcustom: () => { const m = parseInt(document.getElementById('fcm').value); if (!(m >= 1 && m <= 600)) { UI.toast('Enter 1 to 600 minutes.', { err: 1 }); return; } S.dur = m * 60; S.acc = 0; persist(); App.render(); },
      fdel: async t => { if (await UI.confirm('Delete this session?', 'Minutes already added to a habit stay recorded on that habit.', 'Delete', true)) App.act(() => { App.D.focus = App.D.focus.filter(f => f.id !== t.dataset.id); }, 'Session deleted.'); }
    },
    inputs: { flabel: t => { S.label = t.value; persist(); }, fvol: t => { S.vol = +t.value; if (gain) gain.gain.value = S.vol; persist(); } },
    changes: {
      fhabit: t => { S.hid = t.value; persist(); }, fsound: t => { S.sound = t.value; persist(); if (S.running) startSound(); },
      fpomo: t => { const v = parseInt(t.value), k = t.dataset.k; if (!(v >= 1)) return; S.pomo[k] = Math.min(k === 'r' ? 12 : 180, v); S.dur = phaseLen(S.phase); persist(); App.render(); }
    }
  };
})();
