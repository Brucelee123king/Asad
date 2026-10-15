/* HabitFlow reusable UI components (string templates + small DOM helpers) */
const UI = (() => {
  const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const P = {
    home: '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20h14V9.5"/><path d="M10 20v-5h4v5"/>',
    journal: '<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h11"/><path d="M9 8h6"/>',
    progress: '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    focus: '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 2h6"/>',
    settings: '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
    plus: '<path d="M12 5v14M5 12h14"/>', minus: '<path d="M5 12h14"/>', check: '<path d="m5 12.5 4.5 4.5L19 7.5"/>', x: '<path d="M6 6l12 12M18 6 6 18"/>',
    left: '<path d="m15 18-6-6 6-6"/>', right: '<path d="m9 18 6-6-6-6"/>', down: '<path d="m6 9 6 6 6-6"/>', up: '<path d="m18 15-6-6-6 6"/>',
    more: '<circle cx="12" cy="5" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="12" cy="19" r="1.4"/>',
    bell: '<path d="M18 8a6 6 0 1 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/>',
    flame: '<path d="M12 22c4 0 7-3 7-7 0-4-3-6-4-9-1 2-2 3-3.5 3.5C11 6 10 4 9 2 7 6 5 9 5 15c0 4 3 7 7 7z"/>',
    cal: '<rect x="3" y="4.5" width="18" height="17" rx="3"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4"/>',
    edit: '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>', trash: '<path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/>',
    archive: '<rect x="3" y="4" width="18" height="5" rx="1.5"/><path d="M5 9v10h14V9M10 13h4"/>', pause: '<path d="M8 5v14M16 5v14"/>', play: '<path d="M7 4.5v15l12-7.5z"/>',
    copy: '<rect x="8" y="8" width="13" height="13" rx="3"/><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"/>', search: '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    star: '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9z"/>', target: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
    spark: '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>', cloud: '<path d="M7 18a5 5 0 1 1 .9-9.9A6 6 0 0 1 19 10a4 4 0 0 1-1 8z"/>',
    lock: '<rect x="4" y="10" width="16" height="11" rx="3"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>', share: '<path d="M12 3v12M7 8l5-5 5 5M5 14v6h14v-6"/>',
    skip: '<path d="M5 12h11M12 7l5 5-5 5M20 5v14"/>', note: '<path d="M5 3h10l4 4v14H5z"/><path d="M14 3v5h5M8 13h8M8 17h5"/>', undo: '<path d="M9 14 4 9l5-5"/><path d="M4 9h11a5 5 0 0 1 0 10h-3"/>',
    user: '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-6.5 8-6.5s8 2.5 8 6.5"/>', moon: '<path d="M20 14.5A8.5 8.5 0 0 1 9.5 4 8.5 8.5 0 1 0 20 14.5z"/>',
    palette: '<circle cx="12" cy="12" r="9"/><circle cx="8" cy="10" r="1.3"/><circle cx="12" cy="7.5" r="1.3"/><circle cx="16" cy="10" r="1.3"/><path d="M12 21a2 2 0 0 1 0-4h2a3 3 0 0 0 3-3"/>',
    grid: '<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/>',
    help: '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14M12 17.5v.01"/>', plug: '<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0zM12 18v4"/>',
    crown: '<path d="m3 8 4.5 4L12 5l4.5 7L21 8l-2 11H5z"/>', data: '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    out: '<path d="M15 4h4v16h-4M10 17l5-5-5-5M15 12H3"/>', tag: '<path d="M3 12V3h9l9 9-9 9z"/><circle cx="7.5" cy="7.5" r="1.5"/>', mood: '<circle cx="12" cy="12" r="9"/><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9.5h.01M15 9.5h.01"/>',
    sort: '<path d="M7 4v16M3 16l4 4 4-4M17 20V4M13 8l4-4 4 4"/>', filter: '<path d="M3 5h18l-7 8v6l-4 2v-8z"/>', drag: '<path d="M9 6h.01M15 6h.01M9 12h.01M15 12h.01M9 18h.01M15 18h.01"/>',
    stop: '<rect x="6" y="6" width="12" height="12" rx="2"/>', reset: '<path d="M4 4v6h6"/><path d="M5.5 15a7.5 7.5 0 1 0 1.8-7.8L4 10"/>', sound: '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16 9a4 4 0 0 1 0 6M19 6a8 8 0 0 1 0 12"/>'
  };
  const icon = (n, s) => `<svg class="ic" width="${s || 22}" height="${s || 22}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${P[n] || ''}</svg>`;

  function ring(pct, size, sw, inner, color) {
    size = size || 120; sw = sw || 12; const r = (size - sw) / 2, C = 2 * Math.PI * r, v = Math.max(0, Math.min(100, pct || 0));
    return `<div class="ringw" style="width:${size}px;height:${size}px" role="img" aria-label="${Math.round(v)} percent">
      <svg width="${size}" height="${size}" style="transform:rotate(-90deg)"><circle cx="${size / 2}" cy="${size / 2}" r="${r}" fill="none" stroke="var(--sf2)" stroke-width="${sw}"/>
      <circle class="ring-arc" cx="${size / 2}" cy="${size / 2}" r="${r}" fill="none" stroke="${color || 'var(--ac)'}" stroke-width="${sw}" stroke-linecap="round" stroke-dasharray="${v / 100 * C} ${C}"/></svg>
      <div class="lab">${inner == null ? `<b>${Math.round(v)}%</b>` : inner}</div></div>`;
  }
  const pbar = (pct, color) => `<div class="pbar" role="progressbar" aria-valuenow="${Math.round(pct)}" aria-valuemin="0" aria-valuemax="100"><i style="width:${Math.max(0, Math.min(100, pct))}%;${color ? 'background:' + color : ''}"></i></div>`;

  /* bar chart: data [{l:label, v:value, t:tooltip}] */
  function bars(data, o) {
    o = o || {}; const W = 340, H = o.h || 150, L = 30, B = 22, T = 10, pw = W - L - 6, ph = H - B - T, max = o.max || Math.max(1, ...data.map(d => d.v || 0));
    const sharp = document.documentElement.dataset.chart === 'sharp';
    let s = ''; [0, .5, 1].forEach(k => { const y = T + ph * (1 - k); s += `<line class="grid" x1="${L}" x2="${W - 4}" y1="${y}" y2="${y}"/><text x="${L - 5}" y="${y + 3}" text-anchor="end">${Math.round(max * k)}${o.suf || ''}</text>`; });
    const n = data.length, slot = pw / Math.max(1, n), bw = Math.max(3, Math.min(26, slot * .62)), every = Math.ceil(n / 12);
    data.forEach((d, i) => { const v = Math.max(0, d.v || 0), bh = d.v == null ? 0 : Math.max(v > 0 ? 2 : 0, ph * Math.min(v, max) / max), x = L + slot * i + (slot - bw) / 2;
      s += `<rect x="${x.toFixed(1)}" y="${(T + ph - bh).toFixed(1)}" width="${bw.toFixed(1)}" height="${bh.toFixed(1)}" rx="${sharp ? 1 : Math.min(5, bw / 2)}" fill="${d.c || o.color || 'var(--ac)'}" opacity="${d.v == null ? 0 : 1}"><title>${esc(d.t || (d.l + ': ' + v + (o.suf || '')))}</title></rect>`;
      if (i % every === 0) s += `<text x="${(x + bw / 2).toFixed(1)}" y="${H - 6}" text-anchor="middle">${esc(d.l)}</text>`; });
    return `<svg class="chart" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(o.label || 'Bar chart')}">${s}</svg>`;
  }
  /* line chart: series [{name,color,vals:[...]}], labels */
  function line(series, labels, o) {
    o = o || {}; const W = 340, H = o.h || 150, L = 30, B = 22, T = 10, pw = W - L - 10, ph = H - B - T, max = o.max || 100, n = labels.length, every = Math.ceil(n / 10);
    let s = ''; [0, .5, 1].forEach(k => { const y = T + ph * (1 - k); s += `<line class="grid" x1="${L}" x2="${W - 4}" y1="${y}" y2="${y}"/><text x="${L - 5}" y="${y + 3}" text-anchor="end">${Math.round(max * k)}${o.suf || ''}</text>`; });
    labels.forEach((l, i) => { if (i % every === 0) s += `<text x="${(L + (n > 1 ? pw * i / (n - 1) : pw / 2)).toFixed(1)}" y="${H - 6}" text-anchor="middle">${esc(l)}</text>`; });
    series.forEach(se => { const pts = []; se.vals.forEach((v, i) => { if (v == null) return; pts.push([L + (n > 1 ? pw * i / (n - 1) : pw / 2), T + ph * (1 - Math.min(v, max) / max), v, labels[i]]); });
      if (!pts.length) return;
      s += `<path d="${pts.map((p, i) => (i ? 'L' : 'M') + p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join(' ')}" fill="none" stroke="${se.color}" stroke-width="2.2" stroke-linejoin="round" ${se.dash ? 'stroke-dasharray="4 4"' : ''}/>`;
      pts.forEach(p => s += `<circle cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="3" fill="${se.color}"><title>${esc(se.name + ' · ' + p[3] + ': ' + p[2] + (o.suf || ''))}</title></circle>`); });
    return `<svg class="chart" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(o.label || 'Line chart')}">${s}</svg>`;
  }
  /* heatmap: cells [{d, pct|null}] in date order starting on a week-start day */
  function heat(cells, label) {
    return `<div class="heat" role="img" aria-label="${esc(label || 'Heatmap')}">${cells.map(c => `<i title="${c.d}: ${c.pct == null ? 'nothing scheduled' : c.pct + '%'}" style="${c.pct == null ? '' : 'background:color-mix(in srgb,var(--ac) ' + (15 + c.pct * .85) + '%,var(--sf2))'}"></i>`).join('')}</div>
      <div class="legend"><span><i style="background:var(--sf2)"></i>None</span><span><i style="background:color-mix(in srgb,var(--ac) 40%,var(--sf2))"></i>Some</span><span><i style="background:var(--ac)"></i>All done</span></div>`;
  }
  const seg = (name, opts, val) => `<div class="seg" role="tablist">${opts.map(o => `<button role="tab" aria-selected="${o[0] === val}" class="${o[0] === val ? 'on' : ''}" data-act="seg" data-seg="${name}" data-v="${o[0]}">${o[1]}</button>`).join('')}</div>`;
  const empty = (art, title, text, btn) => `<div class="empty"><div class="art">${art}</div><h3>${esc(title)}</h3><p>${esc(text)}</p>${btn || ''}</div>`;
  const sw = (id, on, act, label) => `<label class="sw"><input type="checkbox" ${on ? 'checked' : ''} data-change="${act}" ${id ? 'id="' + id + '"' : ''} aria-label="${esc(label || '')}"><i></i></label>`;
  const STAT = {
    done: { l: 'Completed', i: '\u2713' }, skip: { l: 'Skipped', i: '\u21B7' }, missed: { l: 'Missed', i: '!' }, failed: { l: 'Not done', i: '\u2715' }, slip: { l: 'Setback', i: '!' },
    partial: { l: 'In progress', i: '\u25D0' }, open: { l: 'Open', i: '\u25D0' }, pending: { l: 'Not started', i: '' }, off: { l: 'Not scheduled', i: '' }
  };
  const badge = st => `<span class="badge ${st === 'failed' ? 'missed' : st}">${STAT[st] ? (STAT[st].i ? STAT[st].i + ' ' : '') + STAT[st].l : st}</span>`;

  /* formatting */
  function fmtTime(t, fmt) { if (!t) return ''; const p = t.split(':').map(Number); if (fmt === '24') return t; const h = p[0] % 12 || 12; return h + ':' + (p[1] < 10 ? '0' : '') + p[1] + (p[0] < 12 ? ' AM' : ' PM'); }
  const MN = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], MFULL = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  const DN = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], DFULL = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function fmtDate(d, fmt, long) {
    const p = d.split('-').map(Number), wd = Core.dow(d);
    if (long) return DFULL[wd] + ', ' + (fmt === 'DMY' ? p[2] + ' ' + MFULL[p[1] - 1] : fmt === 'YMD' ? MFULL[p[1] - 1] + ' ' + p[2] : MFULL[p[1] - 1] + ' ' + p[2]);
    if (fmt === 'DMY') return p[2] + ' ' + MN[p[1] - 1] + ' ' + p[0]; if (fmt === 'YMD') return d; return MN[p[1] - 1] + ' ' + p[2] + ', ' + p[0];
  }
  const fmtDur = secs => { secs = Math.max(0, Math.round(secs)); const h = Math.floor(secs / 3600), m = Math.floor(secs % 3600 / 60); return h ? h + 'h ' + m + 'm' : m + 'm'; };
  const clock = secs => { secs = Math.max(0, Math.round(secs)); const h = Math.floor(secs / 3600), m = Math.floor(secs % 3600 / 60), s = secs % 60, z = n => (n < 10 ? '0' : '') + n; return (h ? h + ':' + z(m) : z(m)) + ':' + z(s); };

  /* overlays */
  let sheetClose = null;
  function sheet(html, onMount) {
    closeSheet(); const scrim = document.createElement('div'); scrim.className = 'scrim';
    scrim.innerHTML = `<div class="sheet" role="dialog" aria-modal="true"><div class="grab"></div>${html}</div>`;
    scrim.addEventListener('click', e => { if (e.target === scrim) closeSheet(); });
    document.body.appendChild(scrim); const sh = scrim.firstChild;
    sheetClose = () => { scrim.remove(); sheetClose = null; };
    if (onMount) onMount(sh); const f = sh.querySelector('[autofocus]'); if (f) setTimeout(() => f.focus(), 60);
    return sh;
  }
  function closeSheet() { if (sheetClose) sheetClose(); }
  let toastT = null;
  function toast(msg, o) {
    o = o || {}; const old = document.querySelector('.toast'); if (old) old.remove(); clearTimeout(toastT);
    const el = document.createElement('div'); el.className = 'toast' + (o.err ? ' err' : ''); el.setAttribute('role', 'status');
    el.innerHTML = `<span>${esc(msg)}</span>${o.action ? `<button>${esc(o.action)}</button>` : ''}`;
    if (o.action) el.querySelector('button').onclick = () => { el.remove(); o.onAction(); };
    document.body.appendChild(el); toastT = setTimeout(() => el.remove(), o.ms || (o.action ? 5000 : 2600));
  }
  function confirm(title, text, okLabel, danger) {
    return new Promise(res => {
      let done = false; const fin = v => { if (done) return; done = true; closeSheet(); res(v); };
      sheet(`<h3>${esc(title)}</h3><p class="muted" style="margin-bottom:18px">${esc(text)}</p><div class="row"><button class="btn sec grow" id="cNo">Cancel</button><button class="btn grow ${danger ? 'danger' : ''}" id="cOk">${esc(okLabel || 'OK')}</button></div>`,
        sh => { sh.querySelector('#cNo').onclick = () => fin(false); sh.querySelector('#cOk').onclick = () => fin(true); });
    });
  }
  return { esc, icon, ring, pbar, bars, line, heat, seg, empty, sw, badge, STAT, fmtTime, fmtDate, fmtDur, clock, MN, MFULL, DN, DFULL, sheet, closeSheet, toast, confirm };
})();
