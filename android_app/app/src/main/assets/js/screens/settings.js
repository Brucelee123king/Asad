/* Settings and its sub-screens */
const ACCENTS = ['#2f6bff', '#0a84ff', '#2fbf4f', '#30d158', '#ff9f0a', '#ff453a', '#ff375f', '#bf5af2', '#5e5ce6', '#00a5a5'];
const VERSION = '2.1.0';
const back = t => `<div class="top"><button class="ib" data-act="back" aria-label="Back">${UI.icon('left')}</button><h1 class="t2">${t}</h1></div>`;
const setS = (fn, msg) => App.act(fn, msg || null, { noUndo: 1 });
Screens.settings = (() => {
  const E = s => UI.esc(s);
  const row = (s, ic, t, sub, extra) => `<button class="li" data-act="go" data-s="${s}"${extra || ''}><span class="bubble">${UI.icon(ic, 20)}</span><span class="grow"><span class="t">${t}</span>${sub ? `<span class="s" style="display:block">${sub}</span>` : ''}</span>${UI.icon('right', 18)}</button>`;
  return {
    render() {
      const D = App.D, s = D.settings, ss = App.sess || {};
      return `<div class="top"><h1>Settings</h1></div><div class="stack">
        <button class="card row" data-act="go" data-s="profile" style="text-align:left">${s.photo ? `<img class="avatar" src="${s.photo}" alt="">` : `<span class="avatar">${E((s.name || ss.user || 'G').slice(0, 1).toUpperCase())}</span>`}<span class="grow"><b>${E(s.name || (ss.guest ? 'Guest' : ss.user))}</b><span class="small muted" style="display:block">${ss.guest ? 'Guest · data on this device only' : E(ss.user) + ' · local account'}</span></span>${UI.icon('right', 18)}</button>
        <div class="card"><h2>Preferences</h2><div class="list">${row('appearance', 'palette', 'Appearance', 'Theme, accent color, text size, layout')}${row('notifs', 'bell', 'Notifications & reminders', s.notif ? 'On' + (s.quiet.on ? ' · quiet ' + s.quiet.from + '–' + s.quiet.to : '') : 'Off')}${row('profile', 'user', 'Profile, date & time', 'Name, week start, formats, goals')}</div></div>
        <div class="card"><h2>Organize</h2><div class="list">${row('cats', 'tag', 'Categories', D.cats.length + ' categories')}${row('sections', 'grid', 'Time-of-day sections', D.sections.map(x => x.name).join(', '))}${row('order', 'sort', 'Reorder habits', 'Manual order used on Home')}${row('archived', 'archive', 'Archived habits', D.habits.filter(h => h.archived).length + ' archived')}</div></div>
        <div class="card"><h2>Tools</h2><div class="list">${row('assistant', 'spark', 'Assistant', s.aiOn ? 'On-device helper (no AI model)' : 'Off')}${row('integrations', 'plug', 'Integrations', 'What can connect and what needs setup')}${row('classic', 'grid', 'Classic dashboards', 'Your earlier tracker boards')}${row('plans', 'crown', 'Plans & subscription', 'Free preview · billing not set up')}</div></div>
        <div class="card"><h2>Privacy & data</h2><div class="list">${row('data', 'data', 'Data, backup & privacy', 'Export, restore, delete')}${row('help', 'help', 'Help & feedback', 'How things work, FAQ')}${row('legal', 'lock', 'Privacy policy', '', ' data-doc="privacy"')}${row('legal', 'note', 'Terms of use', '', ' data-doc="terms"')}</div></div>
        <button class="btn sec full" data-act="signout">${UI.icon('out', 18)} Sign out</button><p class="hint" style="text-align:center">HabitFlow ${VERSION} · data stored on this device</p></div>`;
    },
    acts: { signout: async () => { if (!(await UI.confirm('Sign out?', App.sess && App.sess.guest ? 'As a guest your data stays on this device and you can come back to it with "Use as a Guest".' : 'Your data stays on this device. Sign in again to see it.', 'Sign out'))) return;
      try { localStorage.removeItem('ht.session'); sessionStorage.removeItem('ht.session'); window.Android && Android.setReminders && Android.setReminders('[]'); } catch (e) { } location.replace('index.html'); } }
  };
})();
Screens.appearance = {
  render() { const s = App.D.settings, hc = s.homeCards;
    return back('Appearance') + `<div class="stack"><div class="card"><h2>Theme</h2>${UI.seg('theme', [['system', 'System'], ['light', 'Light'], ['dark', 'Dark']], s.theme)}</div>
      <div class="card"><h2>Accent color</h2><div class="swatches">${ACCENTS.map(c => `<button class="swatch ${s.accent === c ? 'on' : ''}" style="background:${c}" data-act="acc" data-v="${c}" aria-label="Accent ${c}"></button>`).join('')}</div></div>
      <div class="card"><h2>Text size</h2>${UI.seg('ts', [['0.9', 'Small'], ['1', 'Default'], ['1.12', 'Large'], ['1.25', 'Larger']], String(s.textScale))}<p class="hint mt">The app also follows your Android font size.</p></div>
      <div class="card"><h2>Layout density</h2>${UI.seg('dens', [['comfortable', 'Comfortable'], ['compact', 'Compact']], s.density)}</div>
      <div class="card"><h2>Charts</h2>${UI.seg('chart', [['rounded', 'Rounded bars'], ['sharp', 'Square bars']], s.chartStyle || 'rounded')}</div>
      <div class="card"><h2>Home dashboard</h2>${[['week', 'Week strip'], ['motivation', 'Motivational message'], ['streaks', 'Streak highlights'], ['reminders', 'Upcoming reminders'], ['recent', 'Recently completed']].map(k => `<div class="row" style="min-height:48px"><span class="grow">${k[1]}</span>${UI.sw('', hc[k[0]], 'hcard', k[1]).replace('data-change="hcard"', 'data-change="hcard" data-k="' + k[0] + '"')}</div>`).join('')}</div>
      <div class="card flat"><h2>App icon</h2><p class="small muted">Android does not let apps change their own launcher icon here, so the HabitFlow icon stays the same.</p></div></div>`; },
  acts: { seg: t => { const k = t.dataset.seg, v = t.dataset.v; setS(() => { const s = App.D.settings; if (k === 'theme') s.theme = v; if (k === 'ts') s.textScale = +v; if (k === 'dens') s.density = v; if (k === 'chart') s.chartStyle = v; }); },
    acc: t => setS(() => { App.D.settings.accent = t.dataset.v; }) },
  changes: { hcard: t => setS(() => { App.D.settings.homeCards[t.dataset.k] = t.checked; }) }
};
Screens.profile = {
  render() { const s = App.D.settings, p = s.profile, E = UI.esc, tz = (Intl.DateTimeFormat().resolvedOptions().timeZone || 'device time zone');
    return back('Profile') + `<div class="stack"><div class="card"><div class="row" style="margin-bottom:14px">${s.photo ? `<img class="avatar" src="${s.photo}" alt="Profile picture">` : `<span class="avatar">${UI.icon('user')}</span>`}<div class="grow"><label class="btn sec sm" style="cursor:pointer">Choose photo<input type="file" accept="image/*" data-change="photo" hidden></label> ${s.photo ? '<button class="lnk small" data-act="nophoto">Remove</button>' : ''}<div class="hint">Optional. Stored only on this device.</div></div></div>
      <div class="fld"><label for="pn">Display name</label><input class="inp" id="pn" maxlength="40" value="${E(s.name)}" data-change="name"></div></div>
      <div class="card"><h2>Date & time</h2><div class="fld"><label>Time zone</label><div class="inp" style="display:flex;align-items:center">${E(tz)}</div><span class="hint">HabitFlow follows your phone's time zone. Days are recorded in local time.</span></div>
      <div class="fld"><label>Week starts on</label>${UI.seg('ws', [['1', 'Monday'], ['0', 'Sunday'], ['6', 'Saturday']], String(s.weekStart))}</div>
      <div class="fld"><label>Date format</label>${UI.seg('df', [['MDY', 'Mar 5, 2026'], ['DMY', '5 Mar 2026'], ['YMD', '2026-03-05']], s.dateFmt)}</div>
      <div class="fld"><label>Time format</label>${UI.seg('tf', [['12', '12-hour'], ['24', '24-hour']], s.timeFmt)}</div>
      <div class="fld" style="margin:0"><label>Language</label><div class="inp" style="display:flex;align-items:center">English</div><span class="hint">More languages are not available yet.</span></div></div>
      <div class="card"><h2>Personal goals & routine</h2><div class="fld"><label for="pg">What do you want to achieve?</label><textarea class="inp" id="pg" maxlength="400" data-change="pgoals" style="min-height:80px">${E((p.goals || []).join(', '))}</textarea></div>
      <div class="row"><div class="fld grow"><label>Usual wake-up</label><input class="inp" type="time" value="${p.wake}" data-change="wake"></div><div class="fld grow"><label>Usual bedtime</label><input class="inp" type="time" value="${p.sleep}" data-change="sleep"></div></div>
      <button class="btn sec sm" data-act="reob">Run the setup questions again</button></div></div>`; },
  acts: { seg: t => setS(() => { const s = App.D.settings, v = t.dataset.v; if (t.dataset.seg === 'ws') s.weekStart = +v; if (t.dataset.seg === 'df') s.dateFmt = v; if (t.dataset.seg === 'tf') s.timeFmt = v; }),
    nophoto: () => setS(() => { delete App.D.settings.photo; }), reob: () => setS(() => { App.D.settings.onboarded = false; }) },
  changes: { name: t => setS(() => { App.D.settings.name = t.value.trim().slice(0, 40); }, 'Saved.'), pgoals: t => setS(() => { App.D.settings.profile.goals = t.value.split(',').map(x => x.trim()).filter(Boolean).slice(0, 10); }, 'Saved.'),
    wake: t => setS(() => { App.D.settings.profile.wake = t.value; }), sleep: t => setS(() => { App.D.settings.profile.sleep = t.value; }),
    photo: t => { const f = t.files && t.files[0]; if (!f) return; if (!/^image\//.test(f.type)) { UI.toast('Pick an image file.', { err: 1 }); return; }
      const img = new Image(), url = URL.createObjectURL(f); img.onload = () => { const c = document.createElement('canvas'), s = 160, r = Math.max(s / img.width, s / img.height); c.width = c.height = s; const x = c.getContext('2d'); x.drawImage(img, (s - img.width * r) / 2, (s - img.height * r) / 2, img.width * r, img.height * r); URL.revokeObjectURL(url); setS(() => { App.D.settings.photo = c.toDataURL('image/jpeg', .82); }, 'Photo updated.'); };
      img.onerror = () => UI.toast('That image could not be read.', { err: 1 }); img.src = url; } }
};
Screens.notifs = {
  render() { const D = App.D, s = D.settings, N = App.native, st = N && N.notifStatus ? N.notifStatus() : null, E = UI.esc;
    const withRem = D.habits.filter(h => !h.archived && h.rem && h.rem.on);
    return back('Notifications') + `<div class="stack">
      <div class="card">${!N ? `<div class="banner info small">${UI.icon('bell', 18)}<span>Reminder notifications are delivered by the HabitFlow Android app. In a browser you will see reminders on the Home screen only.</span></div>` :
        st === 'granted' ? `<div class="banner small">${UI.icon('check', 18)}<span>Notifications are allowed for HabitFlow.</span></div>` : `<div class="banner warn small">${UI.icon('bell', 18)}<span class="grow">Notifications are blocked, so reminders cannot be shown.</span><button class="btn sm" data-act="perm">Allow</button></div>`}
      <div class="row mt" style="min-height:48px"><span class="grow"><b>Habit reminders</b><span class="hint" style="display:block">Turn all reminder notifications on or off.</span></span>${UI.sw('', s.notif, 'notif', 'Habit reminders')}</div>
      ${N ? `<button class="btn sec sm mt" data-act="test">Send a test notification</button>` : ''}</div>
      <div class="card"><h2>Quiet hours</h2><div class="row" style="min-height:48px"><span class="grow">No reminders during quiet hours</span>${UI.sw('', s.quiet.on, 'qon', 'Quiet hours')}</div>
      ${s.quiet.on ? `<div class="row"><div class="fld grow"><label>From</label><input class="inp" type="time" value="${s.quiet.from}" data-change="qfrom"></div><div class="fld grow"><label>To</label><input class="inp" type="time" value="${s.quiet.to}" data-change="qto"></div></div>` : ''}</div>
      <div class="card"><h2>Snooze</h2><p class="small muted" style="margin-bottom:10px">Length of the "Snooze" button on reminder notifications.</p>${UI.seg('snz', [['5', '5 min'], ['10', '10 min'], ['15', '15 min'], ['30', '30 min']], String(s.snooze || 10))}</div>
      <div class="card"><h2>Reminders (${withRem.length})</h2>${withRem.length ? `<div class="list">${withRem.map(h => `<div class="li"><span class="bubble">${E(h.icon)}</span><span class="grow"><span class="t">${E(h.name)}</span><span class="s" style="display:block">${h.rem.times.map(x => UI.fmtTime(x, s.timeFmt)).join(', ')}${h.rem.byDay && Object.keys(h.rem.byDay).length ? ' · custom days' : ''}</span></span><button class="ib" data-act="go" data-s="habitForm" data-id="${h.id}" aria-label="Edit reminder">${UI.icon('edit', 18)}</button><button class="ib" data-act="remoff" data-id="${h.id}" aria-label="Delete reminder">${UI.icon('trash', 18)}</button></div>`).join('')}</div>` : '<p class="muted small">Add reminders when you create or edit a habit.</p>'}</div>
      <div class="card flat small muted"><b>Good to know:</b> HabitFlow schedules the next 14 days of reminders each time you open it. Some phones stop background apps to save battery; if reminders arrive late, allow HabitFlow to run in the background in your phone's battery settings. Location-based reminders are not available.</div></div>`; },
  acts: { perm: () => { try { App.native.requestNotifPermission(); setTimeout(App.render, 1500); } catch (e) { } }, test: () => { try { App.native.testNotification(); UI.toast('Test notification sent.'); } catch (e) { UI.toast('Could not send a test notification.', { err: 1 }); } },
    seg: t => setS(() => { App.D.settings.snooze = +t.dataset.v; try { App.native && App.native.setSnooze && App.native.setSnooze(+t.dataset.v); } catch (e) { } }),
    remoff: async t => { const h = App.habit(t.dataset.id); if (await UI.confirm('Delete this reminder?', 'The habit stays; only its reminder is turned off.', 'Delete', true)) App.act(() => { h.rem.on = false; }, 'Reminder deleted.'); } },
  changes: { notif: t => setS(() => { App.D.settings.notif = t.checked; }, t.checked ? 'Reminders on.' : 'Reminders off.'), qon: t => setS(() => { App.D.settings.quiet.on = t.checked; }),
    qfrom: t => setS(() => { App.D.settings.quiet.from = t.value; }), qto: t => setS(() => { App.D.settings.quiet.to = t.value; }) }
};
Screens.cats = {
  render() { const D = App.D, E = UI.esc;
    return back('Categories') + `<div class="stack"><div class="card"><div class="list">${D.cats.map((c, i) => `<div class="li"><button class="bubble" data-act="cedit" data-id="${c.id}" style="background:color-mix(in srgb,${c.color} 22%,transparent)">${E(c.icon)}</button><button class="grow" data-act="cedit" data-id="${c.id}" style="text-align:left"><span class="t">${E(c.name)}</span><span class="s" style="display:block">${D.habits.filter(h => Core.habitCats(h).indexOf(c.id) >= 0).length} habits</span></button>
      <button class="ib" data-act="cup" data-i="${i}" aria-label="Move up" ${i ? '' : 'disabled'}>${UI.icon('up', 18)}</button><button class="ib" data-act="cdel" data-id="${c.id}" aria-label="Delete category">${UI.icon('trash', 18)}</button></div>`).join('')}</div>
      <button class="btn sec full mt" data-act="cedit">${UI.icon('plus', 18)} Add category</button></div><p class="hint">To move a habit to another category, edit the habit. A habit can be in several categories.</p></div>`; },
  acts: {
    cup: t => setS(() => { const a = App.D.cats, i = +t.dataset.i; [a[i - 1], a[i]] = [a[i], a[i - 1]]; }),
    cdel: async t => { const c = App.cat(t.dataset.id); if (!(await UI.confirm('Delete "' + c.name + '"?', 'Habits in it are kept; they just lose this category.', 'Delete', true))) return; App.act(() => { App.D.cats = App.D.cats.filter(x => x.id !== c.id); App.D.habits.forEach(h => { h.cats = Core.habitCats(h).filter(x => x !== c.id); delete h.cat; }); }, 'Category deleted.'); },
    cedit: t => { const c = t.dataset.id ? App.cat(t.dataset.id) : null, E = UI.esc; let col = c ? c.color : COLORS[0];
      UI.sheet(`<h3>${c ? 'Edit' : 'New'} category</h3><div class="row"><input class="inp" id="ci" style="width:64px;text-align:center;font-size:1.3rem" maxlength="4" value="${E(c ? c.icon : '\u{1F3F7}️')}" aria-label="Icon"><input class="inp grow" id="cn" maxlength="30" value="${E(c ? c.name : '')}" placeholder="Name" autofocus></div>
        <div class="swatches mt">${COLORS.map(x => `<button class="swatch" style="background:${x}" data-c="${x}" aria-label="${x}"></button>`).join('')}</div><div class="err" id="ce"></div><button class="btn full mt" id="cs">Save</button>`, sh => {
        const mark = () => sh.querySelectorAll('[data-c]').forEach(b => b.classList.toggle('on', b.dataset.c === col)); mark(); sh.querySelectorAll('[data-c]').forEach(b => b.onclick = () => { col = b.dataset.c; mark(); });
        sh.querySelector('#cs').onclick = () => { const n = sh.querySelector('#cn').value.trim(), ic = sh.querySelector('#ci').value.trim() || '\u{1F3F7}️'; if (!n) { sh.querySelector('#ce').textContent = 'Enter a name.'; return; } UI.closeSheet();
          setS(() => { if (c) Object.assign(c, { name: n, icon: ic, color: col }); else App.D.cats.push({ id: 'c' + Core.uid(), name: n, icon: ic, color: col }); }, 'Category saved.'); }; }); }
  }
};
Screens.sections = {
  render() { const D = App.D, E = UI.esc, builtin = ['morning', 'afternoon', 'evening', 'night', 'anytime'];
    return back('Time-of-day sections') + `<div class="stack"><div class="card"><p class="small muted" style="margin-bottom:8px">Sections group your habits on Home in this order.</p><div class="list">${D.sections.map((c, i) => `<div class="li"><span class="bubble">${E(c.icon)}</span><input class="inp grow" maxlength="20" value="${E(c.name)}" data-change="sname" data-id="${c.id}" aria-label="Section name">
      <button class="ib" data-act="sup" data-i="${i}" aria-label="Move up" ${i ? '' : 'disabled'}>${UI.icon('up', 18)}</button>${builtin.indexOf(c.id) < 0 ? `<button class="ib" data-act="sdel" data-id="${c.id}" aria-label="Delete section">${UI.icon('trash', 18)}</button>` : ''}</div>`).join('')}</div>
      <div class="row mt"><input class="inp grow" id="nsn" maxlength="20" placeholder="New section, e.g. Lunch break" aria-label="New section name"><button class="btn sec" data-act="sadd">Add</button></div></div></div>`; },
  acts: { sup: t => setS(() => { const a = App.D.sections, i = +t.dataset.i; [a[i - 1], a[i]] = [a[i], a[i - 1]]; }),
    sadd: () => { const n = document.getElementById('nsn').value.trim(); if (!n) return; setS(() => { App.D.sections.splice(App.D.sections.length - 1, 0, { id: 's' + Core.uid(), name: n, icon: '\u{1F552}' }); }, 'Section added.'); },
    sdel: async t => { if (!(await UI.confirm('Delete this section?', 'Its habits move to "Anytime".', 'Delete', true))) return; App.act(() => { App.D.sections = App.D.sections.filter(s => s.id !== t.dataset.id); App.D.habits.forEach(h => { if (h.part === t.dataset.id) h.part = 'anytime'; }); }, 'Section deleted.'); } },
  changes: { sname: t => setS(() => { const s = App.D.sections.find(x => x.id === t.dataset.id); s.name = t.value.trim() || s.name; }, 'Saved.') }
};
Screens.order = {
  render() { const D = App.D, E = UI.esc, hs = Core.live(D).slice().sort((a, b) => (a.order || 0) - (b.order || 0));
    return back('Reorder habits') + `<div class="stack"><p class="small muted">This manual order is used when sorting is set to "Manual".</p><div class="card">${hs.length ? `<div class="list">${hs.map((h, i) => `<div class="li"><span class="bubble">${E(h.icon)}</span><span class="grow t ell">${E(h.name)}</span><button class="ib" data-act="mv" data-i="${i}" data-v="-1" aria-label="Move up" ${i ? '' : 'disabled'}>${UI.icon('up', 18)}</button><button class="ib" data-act="mv" data-i="${i}" data-v="1" aria-label="Move down" ${i < hs.length - 1 ? '' : 'disabled'}>${UI.icon('down', 18)}</button></div>`).join('')}</div>` : UI.empty('\u{1F5C2}️', 'No habits', 'Add habits first.')}</div>
      <div class="chips"><button class="chip" data-act="az">Sort A–Z now</button></div></div>`; },
  acts: { mv: t => setS(() => { const hs = Core.live(App.D).slice().sort((a, b) => (a.order || 0) - (b.order || 0)), i = +t.dataset.i, j = i + +t.dataset.v; [hs[i], hs[j]] = [hs[j], hs[i]]; hs.forEach((h, k) => h.order = k + 1); App.D.settings.sort = 'manual'; }),
    az: () => App.act(() => { Core.live(App.D).slice().sort((a, b) => a.name.localeCompare(b.name)).forEach((h, k) => h.order = k + 1); App.D.settings.sort = 'manual'; }, 'Sorted A–Z.') }
};
Screens.archived = {
  render() { const D = App.D, E = UI.esc, hs = D.habits.filter(h => h.archived);
    return back('Archived habits') + `<div class="card">${hs.length ? `<div class="list">${hs.map(h => `<div class="li"><span class="bubble">${E(h.icon)}</span><button class="grow" style="text-align:left" data-act="hopen" data-h="${h.id}"><span class="t">${E(h.name)}</span><span class="s" style="display:block">${Core.totalDone(D, h, App.tdy())} completions kept</span></button><button class="btn sm sec" data-act="restore" data-id="${h.id}">Restore</button></div>`).join('')}</div>` : UI.empty('\u{1F4E6}', 'Nothing archived', 'Archived habits keep their history and show up here.')}</div>`; },
  acts: { restore: t => App.act(() => { App.habit(t.dataset.id).archived = false; }, 'Restored.') }
};
Screens.classic = {
  render() { return back('Classic dashboards') + `<div class="stack"><p class="small muted">Your earlier tracker boards. They keep their own data, separate from HabitFlow habits.</p><div class="card"><div class="list">
    ${[['ultimate.html', '\u{1F3AF}', 'Ultimate Habit Tracker', 'Monthly board · opens in landscape'], ['digital.html', '⚡', 'Digital Habit Tracker', '12-week neon board'], ['task.html', '✅', 'Task Tracker Dashboard', 'Monthly grid with analysis'], ['custom.html', '\u{1F9E9}', 'My custom boards', 'Boards you built yourself']].map(x => `<a class="li" href="${x[0]}" style="color:inherit;text-decoration:none"><span class="bubble">${x[1]}</span><span class="grow"><span class="t">${x[2]}</span><span class="s" style="display:block">${x[3]}</span></span>${UI.icon('right', 18)}</a>`).join('')}</div></div></div>`; }
};
Screens.data = {
  render() { const s = App.D.settings, ss = App.sess || {};
    return back('Data, backup & privacy') + `<div class="stack">
      <div class="card"><h2>Where your data lives</h2><ul class="small" style="margin-left:18px;line-height:1.6"><li>Everything (habits, check-ins, journal, mood, focus sessions) is stored <b>only on this device</b>, inside the app.</li><li>Nothing is sent to a server. There is no cloud sync yet, so uninstalling the app or clearing its storage deletes your data. Make regular backups.</li><li>Reminders are scheduled with Android's alarm system on this device.</li><li>No analytics, ads or third-party services receive your data.</li></ul></div>
      <div class="card"><h2>Backup & export</h2><div class="list">
        <button class="li" data-act="exp">${UI.icon('share')}<span class="grow"><span class="t">Full backup (JSON)</span><span class="s" style="display:block">Everything, for restoring later or on another phone</span></span></button>
        <button class="li" data-act="csv">${UI.icon('share')}<span class="grow"><span class="t">Habit records (CSV)</span><span class="s" style="display:block">Opens in Excel or Google Sheets</span></span></button>
        <button class="li" data-act="jexp">${UI.icon('share')}<span class="grow"><span class="t">Journal & mood (text)</span><span class="s" style="display:block">Your private entries as plain text</span></span></button>
        <button class="li" data-act="ics">${UI.icon('cal')}<span class="grow"><span class="t">Calendar file (.ics)</span><span class="s" style="display:block">Add habit reminders to Google Calendar or Outlook</span></span></button>
        <button class="li" data-act="imp">${UI.icon('undo')}<span class="grow"><span class="t">Restore from backup</span><span class="s" style="display:block">Replace current data with a JSON backup</span></span></button></div></div>
      <div class="card"><h2>Privacy controls</h2><div class="row" style="min-height:48px"><span class="grow">Mood tracking</span>${UI.sw('', s.moodOn, 'moodOn', 'Mood tracking')}</div><div class="row" style="min-height:48px"><span class="grow">Assistant</span>${UI.sw('', s.aiOn, 'aiOn', 'Assistant')}</div></div>
      <div class="card"><h2>Delete</h2><div class="list"><button class="li" data-act="deljournal" style="color:var(--miss)">${UI.icon('trash')}<span class="grow t">Delete journal & mood data</span></button><button class="li" data-act="delall" style="color:var(--miss)">${UI.icon('trash')}<span class="grow t">Delete all my data</span></button>
        ${ss.guest ? '' : `<button class="li" data-act="delacct" style="color:var(--miss)">${UI.icon('user')}<span class="grow"><span class="t">Delete account</span><span class="s" style="display:block">Removes your login and all its data from this device</span></span></button>`}</div></div></div>`; },
  acts: {
    exp: () => App.share('HabitFlow backup', JSON.stringify(Object.assign({ app: 'HabitFlow', exported: new Date().toISOString() }, App.D), null, 1), 'habitflow-backup-' + App.tdy() + '.json', 'application/json'),
    csv: () => App.share('HabitFlow records', Core.csv(App.D), 'habitflow-records.csv', 'text/csv'),
    jexp: () => { const D = App.D, L = []; D.journal.slice().sort((a, b) => a.date.localeCompare(b.date)).forEach(j => L.push('## ' + j.date + (j.kind !== 'daily' ? ' (' + j.kind + ' reflection)' : '') + (j.tags && j.tags.length ? '  #' + j.tags.join(' #') : ''), j.text, '')); if (D.moods.length) { L.push('## Mood log'); D.moods.slice().sort((a, b) => a.date.localeCompare(b.date)).forEach(m => L.push(m.date + ': ' + m.mood + '/5' + (m.note ? ' – ' + m.note : ''))); } App.share('HabitFlow journal', L.join('\n') || 'No journal entries yet.', 'habitflow-journal.txt'); },
    ics: () => { const D = App.D, L = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//HabitFlow//EN']; const dn = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA'];
      Core.live(D).forEach(h => { if (!h.rem || !h.rem.on) return; const s = h.sched; let rr = 'FREQ=DAILY'; if (s.kind === 'weekly') rr = 'FREQ=WEEKLY;BYDAY=' + s.days.map(d => dn[d]).join(','); else if (s.kind === 'interval') rr = 'FREQ=DAILY;INTERVAL=' + s.every; else if (s.kind === 'monthly') rr = 'FREQ=MONTHLY;BYMONTHDAY=' + s.dom; else if (s.kind === 'once') rr = ''; else if (s.kind === 'times') rr = 'FREQ=DAILY';
        if (h.end && rr) rr += ';UNTIL=' + h.end.replace(/-/g, '') + 'T235959';
        h.rem.times.forEach((t, i) => { const st = h.start.replace(/-/g, '') + 'T' + t.replace(':', '') + '00'; L.push('BEGIN:VEVENT', 'UID:' + h.id + '-' + i + '@habitflow', 'DTSTAMP:' + new Date().toISOString().replace(/[-:]/g, '').slice(0, 15) + 'Z', 'DTSTART:' + st, 'DURATION:PT15M', 'SUMMARY:' + (h.icon + ' ' + h.name).replace(/[,;]/g, ' ')); if (rr) L.push('RRULE:' + rr); L.push('END:VEVENT'); }); });
      L.push('END:VCALENDAR'); if (L.length === 4) { UI.toast('Turn on reminders for a habit first; their times become calendar events.'); return; } App.share('HabitFlow calendar', L.join('\r\n'), 'habitflow.ics', 'text/calendar'); },
    imp: () => UI.sheet(`<h3>Restore from backup</h3><p class="small muted" style="margin-bottom:12px">This replaces all current HabitFlow data on this device. Make a backup of your current data first if you need it.</p>
      <label class="btn sec full" style="cursor:pointer;margin-bottom:10px">Choose backup file<input type="file" accept=".json,application/json,text/plain" id="impf" hidden></label><div class="fld"><label for="impt">…or paste the backup text</label><textarea class="inp" id="impt" placeholder='{"app":"HabitFlow", ...}'></textarea></div><div class="err" id="impe"></div><button class="btn full" id="impok">Restore</button>`, sh => {
      sh.querySelector('#impf').onchange = e => { const f = e.target.files[0]; if (!f) return; const r = new FileReader(); r.onload = () => { sh.querySelector('#impt').value = r.result; }; r.readAsText(f); };
      sh.querySelector('#impok').onclick = async () => { let d; try { d = Core.validateImport(JSON.parse(sh.querySelector('#impt').value)); } catch (e) { sh.querySelector('#impe').textContent = e instanceof SyntaxError ? 'That is not valid backup text.' : e.message; return; }
        UI.closeSheet(); if (!(await UI.confirm('Replace your data?', 'Your current data will be replaced by the backup (' + d.habits.length + ' habits, ' + Object.keys(d.entries).length + ' records).', 'Restore', true))) return;
        App.act(() => { delete d.app; delete d.exported; App.D = d; }, 'Backup restored.', { noUndo: 1 }); }; }),
    deljournal: async () => { if (await UI.confirm('Delete journal & mood data?', 'All journal entries and mood records will be permanently deleted from this device.', 'Delete', true)) App.act(() => { App.D.journal = []; App.D.moods = []; }, 'Journal and mood data deleted.', { noUndo: 1 }); },
    delall: async () => { if (!(await UI.confirm('Delete all data?', 'Every habit, record, journal entry and setting will be permanently deleted from this device. This cannot be undone.', 'Delete everything', true))) return; App.act(() => { App.D = Core.newData(); App.D.settings.onboarded = true; }, 'All data deleted.', { noUndo: 1 }); App.go('home'); },
    delacct: async () => { const ss = App.sess; if (!(await UI.confirm('Delete your account?', 'Your login and all of its data will be removed from this device. This cannot be undone.', 'Delete account', true))) return;
      try { const U = JSON.parse(localStorage.getItem('ht.users') || '{}'); delete U[ss.user.toLowerCase()]; localStorage.setItem('ht.users', JSON.stringify(U)); const pre = window.__u || ''; Object.keys(localStorage).forEach(k => { if (pre && k.indexOf(pre) === 0) localStorage.removeItem(k); }); localStorage.removeItem('ht.session'); sessionStorage.removeItem('ht.session'); window.Android && Android.setReminders && Android.setReminders('[]'); } catch (e) { }
      location.replace('index.html'); }
  },
  changes: { moodOn: t => setS(() => { App.D.settings.moodOn = t.checked; }), aiOn: t => setS(() => { App.D.settings.aiOn = t.checked; }) }
};
Screens.integrations = {
  render() { const it = (ic, n, st, d) => `<div class="li"><span class="bubble">${ic}</span><span class="grow"><span class="t">${n}</span><span class="s" style="display:block">${d}</span></span><span class="badge ${st === 'Available' ? 'done' : 'pending'}">${st}</span></div>`;
    return back('Integrations') + `<div class="stack"><div class="banner info small">${UI.icon('plug', 18)}<span>HabitFlow only lists an integration as available when it actually works in this version. Nothing is connected unless you set it up here.</span></div>
      <div class="card"><h2>Works now</h2><div class="list">${it('\u{1F4C5}', 'Calendar file export', 'Available', 'Export reminders as an .ics file for Google Calendar, Outlook or Apple Calendar (Settings > Data).')}${it('\u{1F4C4}', 'CSV / JSON export', 'Available', 'Use your records in spreadsheets or other tools.')}${it('\u{1F514}', 'Android notifications', 'Available', 'Reminders with Done and Snooze buttons.')}${it('\u{1F4F1}', 'Home-screen widget', 'Available', "Shows today's progress. Long-press your home screen > Widgets > HabitFlow.")}</div></div>
      <div class="card"><h2>Needs extra setup (not available yet)</h2><div class="list">
      ${it('❤️', 'Android Health Connect', 'Not set up', 'Needs the Health Connect SDK and permission review by Google Play.')}
      ${it('\u{1F34E}', 'Apple Health', 'Not possible', 'Only available to iPhone apps.')}
      ${it('\u{1F3C3}', 'Fitbit / Strava / Google Fit', 'Not set up', 'Needs a developer account, API keys and a server for secure sign-in.')}
      ${it('\u{1F4C6}', 'Live Google / Outlook Calendar sync', 'Not set up', 'Needs OAuth credentials and a server.')}
      ${it('⏳', 'Screen time / RescueTime', 'Not set up', 'Needs the Usage Access permission (a sensitive permission that also triggers Play Protect warnings) or a RescueTime API key.')}
      ${it('\u{1F3F7}️', 'NFC tags', 'Not set up', 'Needs NFC support code; planned.')}
      ${it('⚡', 'Zapier / IFTTT / webhooks', 'Not set up', 'Needs a server to receive and send events.')}
      ${it('\u{1F465}', 'Friends, shared challenges & leaderboards', 'Not set up', 'Needs an online account service. No fake users are shown.')}</div></div></div>`; }
};
Screens.plans = {
  render() { const plan = (n, f, cur) => `<div class="card ${cur ? '' : 'flat'}" ${cur ? 'style="border-color:var(--ac)"' : ''}><h2>${n}${cur ? ' <span class="badge done">Your plan</span>' : ''}</h2><ul class="small" style="margin-left:18px;line-height:1.7">${f.map(x => `<li>${x}</li>`).join('')}</ul></div>`;
    return back('Plans & subscription') + `<div class="stack"><div class="banner small">${UI.icon('crown', 18)}<span><b>Free preview: every feature is unlocked.</b> No payment method is set up in this version, so nothing can be charged and there is nothing to buy or restore.</span></div>
      ${plan('Preview (current)', ['Unlimited habits, reminders and checklists', 'All analytics, focus tools, journal and mood', 'Free while billing is not set up'], true)}
      ${plan('Free (planned)', ['Up to 5 active habits', 'Basic check-ins, streaks and progress', 'Essential reminders'])}
      ${plan('Plus (planned)', ['Unlimited habits', 'More reminder options and custom areas', 'Extra personalization'])}
      ${plan('Pro (planned)', ['Advanced checklists and routines', 'Detailed analytics and reports', 'Integrations and automation when available'])}
      <p class="hint">Prices, renewal terms and Google Play billing will be shown here once the paid plans launch. You will always confirm a purchase before you are charged, and you can cancel in Google Play.</p></div>`; }
};
Screens.help = {
  render() { const q = (t, a) => `<details class="card flat"><summary class="b">${t}</summary><p class="small" style="margin-top:8px;line-height:1.55">${a}</p></details>`;
    return back('Help & feedback') + `<div class="stack">
      ${q('How do streaks work?', 'A streak counts scheduled days completed in a row. Days the habit is not scheduled are ignored, skipped (rest) and paused days do not break it, and today never breaks it until the day is over. "N times per week" habits count weeks in a row where the target was met.')}
      ${q('What is the difference between Skip, Not done and Missed?', '<b>Skip</b> is a planned rest day: it keeps your streak. <b>Not done</b> is something you record yourself. <b>Missed</b> is set automatically when a scheduled day ends without a check-in. Not done and missed both count as unsuccessful.')}
      ${q('How do I log an amount?', 'Tap the +1 / +5 button on a habit, or open the ⋯ menu and choose "Add or set progress". <b>Add</b> adds to what you recorded (2 km + 3 km = 5 km); <b>Set</b> replaces it.')}
      ${q('How do habits I want to quit work?', 'Record a successful day with the check button. If it happens, tap + to record an occurrence and, if you like, what triggered it. For "reduce" habits, days within your limit can still be successful.')}
      ${q('Can I fix an old entry?', 'Yes. Open the habit, tap a day in its calendar (or use Journal > Check-in and go back in time) and change the record. Future days cannot be recorded.')}
      ${q('Will changing a schedule change my history?', 'No. A new schedule applies from today. Earlier days keep the schedule they had.')}
      ${q('My reminders arrive late or not at all', 'Check that notifications are allowed (Settings > Notifications). Some phones stop apps in the background to save battery: allow HabitFlow to run in the background in your phone settings. Opening the app refreshes the next 14 days of reminders.')}
      ${q('Where is my data stored? Is there sync?', 'Only on this device. There is no cloud sync yet, so use Settings > Data to back up and restore.')}
      <div class="card"><h2>Feedback</h2><p class="small">Found a bug or have an idea? Email <b style="user-select:all">home@entalogics.com</b> and include your app version (${VERSION}).</p></div></div>`; }
};
Screens.legal = {
  render(p) { const priv = p.doc === 'privacy';
    return back(priv ? 'Privacy policy' : 'Terms of use') + `<div class="card small" style="line-height:1.6">${priv ? `<p><b>Summary:</b> HabitFlow keeps your data on your device and does not collect it.</p><br><p><b>What is stored.</b> Your account name, a salted hash of your password (never the password itself), your habits, check-ins, notes, journal, mood and focus sessions, and your settings. All of it stays in the app's storage on this device.</p><br><p><b>What is shared.</b> Nothing is sent to us or to third parties. There are no ads or analytics. Data leaves your device only when you export or share it yourself.</p><br><p><b>Permissions.</b> Notifications (for reminders), alarms and starting after reboot (to keep reminders scheduled), and vibration. Nothing else.</p><br><p><b>Your control.</b> You can export everything, delete journal and mood data, delete all data or delete your account at any time in Settings > Data.</p><br><p><b>Health information.</b> Mood and habit charts are personal observations, not medical advice.</p>` :
      `<p>HabitFlow is provided as is, free of charge, during this preview. You are responsible for backing up your data; because it is stored only on your device, uninstalling the app or clearing its storage deletes it.</p><br><p>Statistics, insights and assistant suggestions are for personal motivation only and are not medical, psychological or professional advice.</p><br><p>Paid plans are not on sale. If they are introduced, prices and terms will be shown before any purchase and payments will go through Google Play.</p>`}</div>`; }
};
