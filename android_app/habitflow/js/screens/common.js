/* Shared screen pieces: habit card, schedule/goal text, sorting */
const HC = (() => {
  const E = s => UI.esc(s);
  function schedText(h, date) {
    const s = date ? Core.schedFor(h, date) : h.sched; const d = (s && s.days) || [];
    switch (s && s.kind) {
      case 'weekly': if (d.length === 7) return 'Every day'; if (d.join() === '1,2,3,4,5') return 'Weekdays'; if (d.slice().sort().join() === '0,6') return 'Weekends'; return d.slice().sort((a, b) => ((a + 6) % 7) - ((b + 6) % 7)).map(x => UI.DN[x]).join(', ');
      case 'monthly': return 'Monthly on day ' + s.dom;
      case 'interval': return 'Every ' + s.every + ' days';
      case 'times': return s.n + '× per ' + s.per;
      case 'once': return 'One time · ' + UI.fmtDate(h.start, App.D.settings.dateFmt);
      default: return 'Every day';
    }
  }
  function goalText(h) {
    if (h.type === 'quit') return 'Quit';
    if (h.type === 'reduce') return 'Limit ' + ((h.goal && h.goal.limit) || 0) + ' ' + E((h.goal && h.goal.unit) || 'per day');
    const k = Core.goalKind(h); if (Core.checkItems(h)) return h.check.length + ' steps';
    if (k === 'count') return h.goal.target + ' ' + E(h.goal.unit || ''); if (k === 'time') return UI.fmtDur(h.goal.target * 60);
    return 'Complete';
  }
  function remTime(h) { if (!h.rem || !h.rem.on || !h.rem.times || !h.rem.times.length) return ''; return h.rem.times.slice().sort()[0]; }
  function sortHabits(list, how) {
    const a = list.slice();
    if (how === 'alpha') a.sort((x, y) => x.name.localeCompare(y.name));
    else if (how === 'time') a.sort((x, y) => (remTime(x) || '99').localeCompare(remTime(y) || '99') || (x.order || 0) - (y.order || 0));
    else a.sort((x, y) => (x.order || 0) - (y.order || 0));
    return a;
  }
  function card(h, date) {
    const D = App.D, t = App.tdy(), st = Core.status(D, h, date, t), e = Core.getEntry(D, h, date) || {}, kind = Core.goalKind(h), neg = Core.isNegative(h), flex = Core.isFlex(h, date), items = Core.checkItems(h);
    const subs = []; let mini = null; const streak = Core.currentStreak(D, h, t);
    if (neg) { const n = e.n || 0; subs.push(h.type === 'quit' ? (n ? n + ' today' : 'Stay on track') : n + ' of ' + ((h.goal && h.goal.limit) || 0) + ' allowed'); }
    else if (flex) { const p = Core.periodProgress(D, h, date); subs.push(p.done + '/' + p.n + ' this ' + ((Core.schedFor(h, date).per) || 'week')); mini = p.done / p.n * 100; }
    else if (items) { const n = (e.chk || []).length; subs.push(n + '/' + items.length + ' steps'); mini = n / items.length * 100; }
    else if (kind !== 'check') { const v = e.v || 0; subs.push((kind === 'time' ? v + '/' + h.goal.target + ' min' : v + '/' + h.goal.target + ' ' + E(h.goal.unit || ''))); mini = v / Core.target(h) * 100; }
    else subs.push(schedText(h, date));
    if (streak > 0) subs.push('<span title="Current streak">\u{1F525} ' + streak + '</span>');
    const rt = remTime(h); if (rt) subs.push(UI.icon('bell', 12) + UI.fmtTime(rt, D.settings.timeFmt));
    if (h.stack) { const a = App.habit(h.stack); if (a) subs.push('After ' + E(a.name)); }
    if (e.note) subs.push(UI.icon('note', 12));
    if (st !== 'pending' && st !== 'done' && st !== 'open' && st !== 'partial') subs.push(UI.badge(st));
    let ctl = '';
    const ckBtn = (on, label) => `<button class="ck ${on ? 'on' : ''} ${st === 'skip' ? 'skip' : ''}" data-act="hcheck" data-h="${h.id}" data-d="${date}" aria-pressed="${on}" aria-label="${label}">${UI.icon(st === 'skip' ? 'skip' : 'check', 22)}</button>`;
    if (neg) ctl = `<button class="pill ac" data-act="hocc" data-h="${h.id}" data-d="${date}" aria-label="Record an occurrence">${UI.icon('plus', 16)}</button>` + (st === 'slip' ? '' : ckBtn(st === 'done', 'Record successful day for ' + E(h.name)));
    else {
      if (items) ctl += `<button class="pill ac" data-act="hsteps" data-h="${h.id}" data-d="${date}">${(e.chk || []).length}/${items.length}</button>`;
      else if (kind !== 'check' && st !== 'done') ctl += `<button class="pill ac" data-act="hinc" data-h="${h.id}" data-d="${date}" aria-label="Add ${kind === 'time' ? 5 : (h.goal.step || 1)} ${E(App.unitLabel(h))}">+${kind === 'time' ? 5 : (h.goal.step || 1)}</button>`;
      ctl += ckBtn(st === 'done', (st === 'done' ? 'Undo ' : 'Complete ') + E(h.name));
    }
    return `<div class="hc st-${st} ${st === 'done' ? 'done' : ''}" style="--hcol:${h.color}">
      <button class="hi" data-act="hopen" data-h="${h.id}" aria-label="Open ${E(h.name)}">${E(h.icon)}</button>
      <button class="main" data-act="hmore" data-h="${h.id}" data-d="${date}"><div class="nm">${E(h.name)}</div><div class="sub">${subs.join(' · ')}</div>${mini != null ? `<div class="mini"><i style="width:${Math.min(100, mini)}%"></i></div>` : ''}</button>
      ${ctl}<button class="more" data-act="hmore" data-h="${h.id}" data-d="${date}" aria-label="More options for ${E(h.name)}">${UI.icon('more', 20)}</button></div>`;
  }
  /* habits shown for a date, grouped by time-of-day section */
  function sections(date, opts) {
    opts = opts || {}; const D = App.D, t = App.tdy();
    let hs = Core.live(D).filter(h => Core.status(D, h, date, t) !== 'off');
    if (opts.cat) hs = hs.filter(h => Core.habitCats(h).indexOf(opts.cat) >= 0);
    if (!hs.length) return '';
    return D.sections.map(sec => { const list = sortHabits(hs.filter(h => (h.part || 'anytime') === sec.id || (sec.id === 'anytime' && !D.sections.some(s => s.id === h.part))), D.settings.sort);
      if (!list.length) return ''; const dn = list.filter(h => Core.status(D, h, date, t) === 'done').length;
      return `<section><div class="sec-t">${E(sec.icon)} ${E(sec.name)} <span class="muted">${dn}/${list.length}</span></div>${list.map(h => card(h, date)).join('')}</section>`; }).join('');
  }
  function weekDays(date) { const ws = App.D.settings.weekStart, back = (Core.dow(date) - ws + 7) % 7, from = Core.addDays(date, -back); return Core.range(from, Core.addDays(from, 6)); }
  function filteredHabits(f) {
    let hs = f && f.arch ? App.D.habits.slice() : Core.live(App.D);
    if (f && f.cat) hs = hs.filter(h => Core.habitCats(h).indexOf(f.cat) >= 0);
    if (f && f.hid) hs = hs.filter(h => h.id === f.hid);
    return hs;
  }
  return { schedText, goalText, card, sections, sortHabits, remTime, weekDays, filteredHabits };
})();
