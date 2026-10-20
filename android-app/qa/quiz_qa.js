const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs');
const PORT = 8765;
const WWW = '/home/user/Asad/android-app/app/src/main/assets/www';
const results = [];
function rec(name, ok, ev) { results.push({ name, ok: !!ok, ev: String(ev === undefined ? '' : ev) }); console.log((ok ? 'PASS ' : 'FAIL ') + name + ' | ' + (ev === undefined ? '' : ev)); }
const secOf = k => /^PMA-/.test(k) ? 'pma' : /^FA-/.test(k) ? 'fa' : /^HK-/.test(k) ? 'hk' : /^LC-/.test(k) ? 'lc' : /^(MR|CN|IV)-/.test(k) ? 'hk' : 'o';
(async () => {
  const srv = spawn('python3', ['-m', 'http.server', String(PORT), '--bind', '127.0.0.1'], { cwd: WWW, stdio: 'ignore' });
  await new Promise(r => setTimeout(r, 800));
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const ctx = await browser.newContext({ viewport: { width: 393, height: 800 }, isMobile: true, hasTouch: false });
  const blocked = [], consoleErrs = [], failedReq = [], pageErrs = [], dialogs = [];
  await ctx.route('**/*', route => { const u = route.request().url(); if (/^https?:\/\/127\.0\.0\.1[:/]/.test(u) || u.startsWith('data:') || u.startsWith('blob:')) route.continue(); else { blocked.push(u); route.abort(); } });
  const page = await ctx.newPage();
  let dialogMode = 'accept';
  page.on('dialog', d => { dialogs.push(d.type() + ':' + d.message()); dialogMode === 'accept' ? d.accept() : d.dismiss(); });
  page.on('console', m => { if (m.type() === 'error') consoleErrs.push(m.text()); });
  page.on('pageerror', e => pageErrs.push(e.message));
  page.on('requestfailed', r => { if (!r.url().startsWith('http://127.0.0.1') || true) failedReq.push(r.url() + ' ' + (r.failure() || {}).errorText); });
  await page.addInitScript(() => {
    const si = window.setInterval.bind(window), ci = window.clearInterval.bind(window);
    window.__iv = new Set();
    window.setInterval = (f, d, ...a) => { const id = si(f, d, ...a); if (d === 1000) window.__iv.add(id); return id; };
    window.clearInterval = id => { window.__iv.delete(id); return ci(id); };
  });
  await page.clock.install({ time: new Date('2026-01-01T10:00:00') });
  const boot = async () => { await page.goto(`http://127.0.0.1:${PORT}/index.html`); await page.waitForTimeout(500); await page.getByText('Continue as Guest').first().click(); await page.clock.runFor(1500); };
  await boot();
  const ivCount = () => page.evaluate(() => window.__iv.size);
  const vis = id => page.evaluate(i => !document.getElementById(i).classList.contains('hidden'), id);
  const timer = () => page.evaluate(() => document.getElementById('timer-display').textContent);
  const secs = s => { const [m, x] = s.split(':').map(Number); return m * 60 + x; };

  // ---- data counts
  const data = await page.evaluate(() => { const o = {}; Object.keys(ALL).forEach(k => o[k] = ALL[k].length); return o; });
  const bySec = {}; const keys = Object.keys(data);
  keys.forEach(k => { const s = ['o'].concat([]); });
  const secKeys = { o: [], pma: [], fa: [], hk: [], lc: [] };
  await page.evaluate(() => { }); 
  const secKeysRaw = await page.evaluate(() => { const r = {}; SECS.forEach(s => r[s.id] = Object.keys(ALL).filter(s.test)); r.unassigned = Object.keys(ALL).filter(k => !SECS.some(s => s.test(k))); return r; });
  const menu = {};
  await page.evaluate(() => openSec(null));
  const menuTxt = await page.evaluate(() => Array.from(document.querySelectorAll('#sec-menu button')).map(b => b.innerText.replace(/\s+/g, ' ')));
  const total = keys.reduce((t, k) => t + data[k], 0);
  rec('DATA total keys/questions', true, `${keys.length} tests, ${total} questions; per-section: ` + Object.entries(secKeysRaw).map(([s, ks]) => `${s}=${ks.length} tests/${ks.reduce((t, k) => t + data[k], 0)} Q`).join(', '));
  rec('DATA every test belongs to a section card', secKeysRaw.unassigned.length === 0, 'tests not matched by any SECS.test (invisible from menu cards): ' + JSON.stringify(secKeysRaw.unassigned) + ' (they may be reachable via HK sub-pages, checked below)');
  for (const sc of ['o', 'pma', 'fa', 'hk', 'lc']) {
    const ks = secKeysRaw[sc], n = ks.reduce((t, k) => t + data[k], 0);
    const line = menuTxt.find(t => t.includes(`${ks.length} Tests`) && t.includes(`${n} MCQs`));
    rec(`MENU count matches data: section ${sc}`, !!line, `expected "${ks.length} Tests • ${n} MCQs"; menu: ${JSON.stringify(menuTxt.map(t => (t.match(/\d+ Tests • \d+ MCQs/) || [''])[0]))}`);
  }
  // data integrity
  const integ = await page.evaluate(() => { const bad = []; Object.keys(ALL).forEach(k => ALL[k].forEach((q, i) => { if (!q.question || !Array.isArray(q.options) || q.options.length < 2 || q.options.length > 6 || !Number.isInteger(q.correct) || q.correct < 0 || q.correct >= q.options.length || q.options.some(o => o === '' || o == null) || new Set(q.options).size !== q.options.length) bad.push(k + '#' + (i + 1)); })); return bad; });
  rec('DATA integrity (question text, 2-6 distinct non-empty options, valid correct index) for all tests', integ.length === 0, integ.length ? integ.length + ' bad e.g. ' + integ.slice(0, 15).join(',') : 'all ok');
  const optCounts = await page.evaluate(() => { const c = {}; Object.keys(ALL).forEach(k => ALL[k].forEach(q => c[q.options.length] = (c[q.options.length] || 0) + 1)); return c; });
  rec('DATA option-count distribution (info)', true, JSON.stringify(optCounts));
  // original sections: 20 tests x 50
  rec('DATA original section = 40 tests x 50 (1000 MCQs split in halves)', secKeysRaw.o.length === 40 && secKeysRaw.o.every(k => data[k] === 50), `${secKeysRaw.o.length} tests, sizes ${[...new Set(secKeysRaw.o.map(k => data[k]))]}  keys first/last ${secKeysRaw.o[0]} ${secKeysRaw.o.at(-1)}`);

  // ---- per-test flow
  const TESTS = ['1-50', 'PMA-1', 'FA-1', 'HK-1', 'MR-500', 'CN-1', 'IV-1', 'LC-1'];
  for (const k of TESTS) {
    if (!data[k]) { rec(`[${k}] exists in ALL`, false, 'missing'); continue; }
    const N = data[k]; const Q = await page.evaluate(k => ALL[k], k);
    const P = n => `[${k}] ${n}`;
    // open via UI
    await page.evaluate(() => { if (document.getElementById('view-select').classList.contains('hidden')) showSelect(); });
    await page.evaluate(s => openSec(s), secOf(k));
    let uiCard = await page.evaluate(k => { const b = Array.from(document.querySelectorAll('#view-select button[onclick]')).find(b => b.getAttribute('onclick') === `selectTest('${k}')`); if (!b) return false; return !!(b.offsetParent); }, k);
    if (!uiCard && (secOf(k) === 'hk')) { await page.evaluate(() => { if (typeof openHkSub === 'function') openHkSub('all'); }); uiCard = await page.evaluate(k => { const b = Array.from(document.querySelectorAll('#view-select button[onclick]')).find(b => b.getAttribute('onclick') === `selectTest('${k}')`); return !!(b && b.offsetParent); }, k); }
    rec(P('selection card visible & clickable in UI'), uiCard, uiCard ? 'card found' : 'no visible card calling selectTest');
    if (uiCard) await page.locator(`#view-select button[onclick="selectTest('${k}')"]`).first().click(); else await page.evaluate(k => selectTest(k), k);
    const homeOk = await vis('view-home');
    const qTotal = await page.textContent('#q-total'); const infoTotal = await page.textContent('#info-total'); const infoTime = await page.textContent('#info-time');
    const expMin = Math.ceil(Math.max(60, N * 30) / 60);
    rec(P('test opens (intro screen: count and minutes)'), homeOk && +qTotal === N && infoTotal.includes(String(N)) && infoTime.includes(String(expMin)), `home visible=${homeOk}, q-total=${qTotal}, info=${infoTotal}/${infoTime}, expected ${N}/${expMin} min`);
    const ivBase = await ivCount();
    await page.click('#start-quiz-btn');
    rec(P('quiz view shown, quizActive'), (await vis('view-quiz')) && await page.evaluate(() => quizActive), '');
    rec(P('timer starts at N*30s (min 60s)'), secs(await timer()) === Math.max(60, N * 30), `display ${await timer()} expected ${Math.floor(Math.max(60, N * 30) / 60)}:${String(Math.max(60, N * 30) % 60).padStart(2, '0')}`);
    // timer countdown & single interval
    const t0 = secs(await timer()); await page.clock.runFor(5000); const t1 = secs(await timer());
    rec(P('timer counts down 1s/s (5s elapsed -> -5)'), t0 - t1 === 5, `${t0} -> ${t1}; sidebar=${await page.textContent('#sidebar-timer')}`);
    rec(P('exactly one new 1s interval running'), (await ivCount()) - ivBase === 1, `active 1000ms intervals base=${ivBase} now=${await ivCount()}`);

    // order & options for each question, via Next
    let orderBad = [];
    const nCheck = Math.min(N, 12);
    for (let i = 0; i < N; i++) {
      if (i < nCheck || i === N - 1) {
        const st = await page.evaluate(() => ({ n: document.getElementById('current-q-num').textContent, q: document.getElementById('question-text').textContent, o: Array.from(document.querySelectorAll('#options-container [role=button]')).map(e => e.children[1].textContent) }));
        if (+st.n !== i + 1 || st.q !== Q[i].question || JSON.stringify(st.o) !== JSON.stringify(Q[i].options)) orderBad.push(i + 1);
      }
      if (i < N - 1) { if (i < nCheck) await page.click('#btn-next'); else await page.evaluate(() => nextQuestion()); }
    }
    // full DOM verification for ALL questions (fast, via functions)
    const fullBad = await page.evaluate(() => { const bad = []; for (let i = 0; i < quizData.length; i++) { jumpToQuestion(i); const o = Array.from(document.querySelectorAll('#options-container [role=button]')).map(e => e.children[1].textContent); if (document.getElementById('question-text').textContent !== quizData[i].question || o.length !== quizData[i].options.length || o.some((t, j) => t !== quizData[i].options[j]) || +document.getElementById('current-q-num').textContent !== i + 1) bad.push(i + 1); } return bad; });
    rec(P('questions appear in order with all options (real Next clicks for first 12 + last; all N via DOM)'), orderBad.length === 0 && fullBad.length === 0, `click-walk bad=${JSON.stringify(orderBad)} full-scan bad=${JSON.stringify(fullBad.slice(0, 10))}`);
    // last-question label
    const lastLbl = await page.textContent('#btn-next-text');
    rec(P('last question shows "Finish & Submit"'), lastLbl.trim() === 'Finish & Submit', lastLbl);
    // Prev/Next
    await page.evaluate(() => jumpToQuestion(0));
    const prevDis0 = await page.evaluate(() => document.getElementById('btn-prev').disabled);
    await page.click('#btn-next'); await page.click('#btn-next'); await page.click('#btn-prev');
    const qn = await page.textContent('#current-q-num');
    rec(P('Previous/Next navigation (Prev disabled at Q1; next,next,prev -> Q2)'), prevDis0 && qn === '2', `prevDisabledAtQ1=${prevDis0}, qnum=${qn}`);
    // answering pattern: i%3==0 correct, 1 wrong, 2 skip
    const exp = Q.map((q, i) => i % 3 === 2 ? null : (i % 3 === 0 ? q.correct : (q.correct + 1) % q.options.length));
    // real clicks for Q1..Q3, DOM clicks rest
    await page.evaluate(() => jumpToQuestion(0));
    for (let i = 0; i < N; i++) {
      if (i > 0) { if (i < 3) await page.click('#btn-next'); else await page.evaluate(i => jumpToQuestion(i), i); }
      if (exp[i] !== null) { if (i < 3) await page.locator('#options-container [role=button]').nth(exp[i]).click(); else await page.evaluate(o => document.querySelectorAll('#options-container [role=button]')[o].click(), exp[i]); }
    }
    const ua = await page.evaluate(() => userAnswers.slice());
    rec(P('selecting an answer records it (pattern correct/wrong/skip over all Qs)'), JSON.stringify(ua) === JSON.stringify(exp), `mismatches=${ua.filter((v, i) => v !== exp[i]).length}`);
    // change answer attempt on Q1 (index 0)
    await page.evaluate(() => jumpToQuestion(0));
    const before = await page.evaluate(() => userAnswers[0]);
    const other = (before + 1) % Q[0].options.length;
    await page.locator('#options-container [role=button]').nth(other).click();
    const after = await page.evaluate(() => userAnswers[0]);
    const fb = await page.evaluate(() => Array.from(document.querySelectorAll('#options-container > div')).pop().textContent);
    rec(P('changing an answer (second click on other option)'), after === other, `answer ${before} -> ${after}; app LOCKS first answer by design ("answer locked after first click"); instant feedback: "${fb.slice(0, 40)}"`);
    // palette colours
    const pal = await page.evaluate(() => quizData.map((q, i) => { const c = document.getElementById('palette-btn-' + i).className; const cur = i === currentQuestionIndex; return { i, c, cur }; }));
    const palBad = pal.filter(p => { const a = ua[p.i]; if (a === null) return !/bg-slate-100|bg-indigo-50/.test(p.c) || /emerald|rose/.test(p.c); return a === Q[p.i].correct ? !/bg-emerald-600/.test(p.c) : !/bg-rose-600/.test(p.c); });
    rec(P('palette colours: unanswered=slate/indigo-50(current), correct=green, wrong=red'), palBad.length === 0, `bad=${JSON.stringify(palBad.slice(0, 3).map(p => p.i + 1))}`);
    // palette jump
    const jt = [Math.floor(N / 2), N - 1, 0];
    let jb = [];
    for (const j of jt) { await page.locator('#palette-grid button').nth(j).scrollIntoViewIfNeeded(); await page.locator('#palette-grid button').nth(j).click(); const n = await page.textContent('#current-q-num'); const qt = await page.textContent('#question-text'); if (+n !== j + 1 || qt !== Q[j].question) jb.push(j + 1); }
    rec(P('palette click jumps to that question'), jb.length === 0, `tested Q${jt.map(x => x + 1)} bad=${jb}`);
    // manual submit with confirmation
    await page.evaluate(() => jumpToQuestion(quizData.length - 1));
    const answered = exp.filter(x => x !== null).length + 0;
    await page.click('#btn-next');
    const modalVis = await vis('modal-submit-confirm') ; const msg = await page.textContent('#submit-confirm-msg');
    rec(P('submit shows confirmation with answered count'), modalVis && msg.includes(`answered ${answered} out of ${N}`), msg);
    await page.click('#modal-submit-confirm >> text=Continue Quiz');
    rec(P('"Continue Quiz" cancels submit (still in quiz, timer alive)'), !(await vis('view-results')) && (await vis('view-quiz')) && await page.evaluate(() => quizActive), '');
    const tBefore = secs(await timer());
    await page.click('#btn-next'); await page.click('#modal-submit-confirm >> text=Yes, Submit');
    // results
    const correctN = Q.reduce((c, q, i) => c + (exp[i] === q.correct ? 1 : 0), 0); const pct = Math.round(correctN / N * 100);
    const r = await page.evaluate(() => ({ s: document.getElementById('result-score-text').textContent, p: document.getElementById('result-percentage-text').textContent, c: document.getElementById('stat-correct').textContent, w: document.getElementById('stat-incorrect').textContent, ps: document.getElementById('result-pass-status').textContent, tm: document.getElementById('stat-time').textContent, rv: !document.getElementById('view-results').classList.contains('hidden'), tv: document.getElementById('header-timer-container').classList.contains('hidden') }));
    rec(P('manual submit: results screen, timer hidden, no running timer'), r.rv && r.tv && (await ivCount()) === ivBase && !(await page.evaluate(() => quizActive)), `results=${r.rv} timerHidden=${r.tv} intervals ${await ivCount()} (base ${ivBase})`);
    rec(P('score / percentage / correct / incorrect match own computation'), r.s === `${correctN} / ${N}` && r.p === pct + '%' && +r.c === correctN && +r.w === N - correctN, `app: ${r.s} ${r.p} correct=${r.c} incorrect=${r.w}; expected ${correctN}/${N} ${pct}% incorrect=${N - correctN}`);
    const elapsedExp = Math.max(60, N * 30) - tBefore + 0;
    rec(P('time-taken stat sane (>= elapsed fast-forward 5s)'), secs(r.tm) >= 5 , `stat-time=${r.tm}`);
    const passExp = correctN >= 25;
    rec(P(`PASS/FAIL badge is consistent with ${N}-question test (app rule: correct>=25)`), r.ps === (passExp ? 'PASS' : 'FAIL'), `badge=${r.ps} correct=${correctN}/${N} (${pct}%); 50% of ${N} = ${N / 2}${N < 50 ? ' -> fixed threshold 25 is above 50% for this size' : N > 50 ? ' -> fixed threshold 25 is below 50% for this size' : ''}`);
    // best persistence
    const best = await page.evaluate(k => localStorage.getItem('mc_best_' + k), k);
    rec(P('best score saved to localStorage (mc_best_*)'), best === String(pct), `stored=${best} expected=${pct}`);
    // review
    const rv = await page.evaluate(() => ({ n: document.querySelectorAll('#review-list-container > div').length, cor: Array.from(document.querySelectorAll('#review-list-container > div')).filter(d => /Correct/.test(d.textContent) && !/Incorrect/.test(d.textContent.slice(0, 80))).length }));
    const cards = await page.evaluate(() => Array.from(document.querySelectorAll('#review-list-container > div')).map(d => d.children[0].children[1].textContent.trim()));
    const expLbl = Q.map((q, i) => exp[i] === null ? 'Unanswered' : exp[i] === q.correct ? 'Correct' : 'Incorrect');
    rec(P('answer review lists all Qs with right Correct/Incorrect/Unanswered labels'), JSON.stringify(cards) === JSON.stringify(expLbl), `cards=${cards.length}/${N}`);
    await page.click('#rev-filter-incorrect');
    const inc = await page.evaluate(() => Array.from(document.querySelectorAll('#review-list-container > div')).map(d => d.children[0].children[0].textContent.trim() + '|' + d.children[0].children[1].textContent.trim()));
    const expInc = expLbl.map((l, i) => l === 'Correct' ? null : `Q${i + 1}|${l}`).filter(Boolean);
    rec(P('review "Incorrect Only" filter (incorrect + unanswered, none correct)'), JSON.stringify(inc) === JSON.stringify(expInc), `shown ${inc.length}, expected ${expInc.length} (incorrect=${N - correctN - exp.filter(x => x === null).length}, unanswered=${exp.filter(x => x === null).length}); note: filter treats unanswered as incorrect`);
    await page.click('#rev-filter-all');
    const allN = await page.evaluate(() => document.querySelectorAll('#review-list-container > div').length);
    rec(P('review "All" filter restores full list'), allN === N, `${allN}`);
    // retake
    await page.evaluate(() => { const b = Array.from(document.querySelectorAll('#view-results button')).find(b => /Retake/.test(b.textContent)); b.click(); });
    const rs = await page.evaluate(() => ({ ua: userAnswers.every(x => x === null) && userAnswers.length === quizData.length, home: !document.getElementById('view-home').classList.contains('hidden'), res: document.getElementById('view-results').classList.contains('hidden'), active: quizActive }));
    rec(P('retake resets answers and returns to intro'), rs.ua && rs.home && rs.res && !rs.active, JSON.stringify(rs));
    await page.click('#start-quiz-btn');
    const rs2 = await page.evaluate(() => ({ q: document.getElementById('current-q-num').textContent, t: document.getElementById('timer-display').textContent, pal: Array.from(document.querySelectorAll('#palette-grid button')).filter(b => /emerald|rose/.test(b.className)).length, opts: document.querySelectorAll('#options-container > div').length, nBtn: document.querySelectorAll('#palette-grid button').length }));
    rec(P('retake: Q1, full timer, palette all unanswered, only options (no stale feedback), single interval'), rs2.q === '1' && secs(rs2.t) === Math.max(60, N * 30) && rs2.pal === 0 && rs2.opts === Q[0].options.length && (await ivCount()) - ivBase === 1, JSON.stringify(rs2) + ` intervals=${(await ivCount()) - ivBase}`);
    // back with confirm: dismiss then accept
    dialogMode = 'dismiss'; dialogs.length = 0;
    await page.click('#backBtn'); await page.waitForTimeout(200);
    const stillQ = (await vis('view-quiz')) && await page.evaluate(() => quizActive);
    const tA = secs(await timer()); await page.clock.runFor(3000); const tB = secs(await timer());
    rec(P('Back button during quiz asks confirmation; Cancel keeps quiz + timer running'), dialogs.length >= 1 && stillQ && tA - tB === 3, `dialogs=${JSON.stringify(dialogs)} stillInQuiz=${stillQ} timer ${tA}->${tB}`);
    // history/phone-back cancel
    dialogs.length = 0; await page.goBack().catch(() => { }); await page.waitForTimeout(200);
    const url = page.url();
    dialogMode = 'accept'; dialogs.length = 0;
    await page.evaluate(() => { document.getElementById('backBtn').click(); }); await page.waitForTimeout(300);
    const sel = await vis('view-select') ; 
    const stillRunning = await ivCount();
    const tx = await timer(); await page.clock.runFor(5000); const ty = await timer();
    rec(P('Back + OK: returns to selection, quiz stopped, no running timer'), sel && !(await page.evaluate(() => quizActive)) && stillRunning === ivBase && tx === ty, `selectVisible=${sel} intervals=${stillRunning}(base ${ivBase}) display ${tx}->${ty} dialogs=${JSON.stringify(dialogs)}`);
  }
  // ---- auto submit at 0 (3 tests), run once, no double timer after restart
  for (const k of ['1-50', 'PMA-1', 'IV-1']) {
    const N = data[k], Q = await page.evaluate(k => ALL[k], k), P = n => `[${k}] ${n}`;
    await page.evaluate(() => { if (document.getElementById('view-select').classList.contains('hidden')) { quizActive = false; showSelect(); } });
    await page.evaluate(k => selectTest(k), k);
    const ivBase = await ivCount();
    await page.click('#start-quiz-btn');
    // answer first 4 correctly, 1 wrong
    await page.evaluate(() => { const c = i => { jumpToQuestion(i); document.querySelectorAll('#options-container [role=button]')[quizData[i].correct].click(); }; c(0); c(1); c(2); c(3); jumpToQuestion(4); document.querySelectorAll('#options-container [role=button]')[(quizData[4].correct + 1) % quizData[4].options.length].click(); });
    // open the confirm modal and leave it open to see auto-submit behaviour
    await page.evaluate(() => confirmSubmitQuiz());
    const total = Math.max(60, N * 30);
    await page.clock.runFor((total - 3) * 1000);
    const near = await timer();
    const notYet = !(await vis('view-results'));
    await page.clock.runFor(2000);
    const stillNo = !(await vis('view-results')) && secs(await timer()) === 1;
    await page.clock.runFor(1000);
    const res = await page.evaluate(() => ({ rv: !document.getElementById('view-results').classList.contains('hidden'), s: document.getElementById('result-score-text').textContent, modal: !document.getElementById('modal-submit-confirm').classList.contains('hidden'), tv: document.getElementById('header-timer-container').classList.contains('hidden'), tm: document.getElementById('stat-time').textContent, active: quizActive, disp: document.getElementById('timer-display').textContent }));
    rec(P('auto-submit exactly when timer hits 0 (not before)'), notYet && stillNo && res.rv, `at T-3s display=${near}; results shown at 0: ${res.rv}`);
    rec(P('auto-submit score = own computation (4 correct, 1 wrong, rest unanswered)'), res.s === `4 / ${N}`, res.s);
    rec(P('auto-submit: timer stops (no interval, no negative display) and quizActive=false'), (await ivCount()) === ivBase && !res.active && res.disp === '00:00', `intervals ${await ivCount()}/${ivBase}, display ${res.disp}, stat-time=${res.tm} (expected ${Math.floor(total / 60)}:${String(total % 60).padStart(2, '0')})`);
    rec(P('auto-submit while confirm modal open: modal is closed'), !res.modal, `modal still visible over results = ${res.modal}`);
    await page.clock.runFor(10000);
    const bestK = await page.evaluate(k => localStorage.getItem('mc_best_' + k), k);
    rec(P('after auto-submit, 10s later nothing changes (ran once)'), (await vis('view-results')), `best stored=${bestK}`);
    // restart quickly: no double timer
    await page.evaluate(() => { Array.from(document.querySelectorAll('#view-results button')).find(b => /Retake/.test(b.textContent)).click(); });
    await page.click('#start-quiz-btn'); const a = secs(await timer()); await page.clock.runFor(10000); const b = secs(await timer());
    rec(P('timer after retake counts 1s/s (no duplicated timer)'), a - b === 10 && (await ivCount()) - ivBase === 1, `${a}->${b}, intervals ${(await ivCount()) - ivBase}`);
    // start again via leave without finishing -> reselect -> start
    await page.evaluate(() => { quizActive = false; showSelect(); });
    rec(P('showSelect() clears timer'), (await ivCount()) === ivBase, `intervals ${await ivCount()}`);
  }
  // ---- double start protection: call startQuiz twice quickly
  await page.evaluate(() => { selectTest('1-50'); });
  const b0 = await ivCount(); await page.click('#start-quiz-btn'); await page.evaluate(() => startQuiz()); await page.evaluate(() => startQuiz());
  rec('startQuiz() called repeatedly creates only one timer', (await ivCount()) - b0 === 1, `new intervals ${(await ivCount()) - b0}`);
  dialogMode = 'accept'; await page.evaluate(() => showSelect());
  // ---- persistence after reload
  const bestBefore = await page.evaluate(() => { const o = {}; for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (k.startsWith('mc_best_')) o[k] = localStorage.getItem(k); } return o; });
  await page.reload(); await page.waitForTimeout(500);
  const guestBtn = await page.getByText('Continue as Guest').first().isVisible().catch(() => false);
  if (guestBtn) await page.getByText('Continue as Guest').first().click();
  await page.clock.runFor(1500);
  const bestAfter = await page.evaluate(() => { const o = {}; for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (k.startsWith('mc_best_')) o[k] = localStorage.getItem(k); } return o; });
  rec('best scores persist in localStorage after reload', JSON.stringify(bestBefore) === JSON.stringify(bestAfter) && Object.keys(bestAfter).length >= 6, `before=${JSON.stringify(bestBefore)}`);
  // displayed on cards
  await page.evaluate(() => { if (document.getElementById('view-select').classList.contains('hidden')) showSelect(); openSec('o'); });
  const badge = await page.evaluate(() => { const b = Array.from(document.querySelectorAll('#test-grid button')).find(b => b.getAttribute('onclick') === "selectTest('1-50')"); return b ? b.innerText.replace(/\s+/g, ' ') : null; });
  const exp150 = bestAfter['mc_best_1-50'];
  rec('best score shown on the test card after reload', badge && badge.includes(`Best ${exp150}%`), badge);
  // best only goes up: finish 1-50 with 0 answers and see best unchanged
  await page.evaluate(() => selectTest('1-50')); await page.click('#start-quiz-btn'); await page.evaluate(() => executeSubmitQuiz());
  const best2 = await page.evaluate(() => localStorage.getItem('mc_best_1-50'));
  rec('best score never decreases (0% retry keeps old best)', best2 === exp150, `before ${exp150}, after ${best2}`);
  // reload during quiz? skip. finally offline & errors
  rec('offline: no request outside 127.0.0.1 was attempted', blocked.length === 0, blocked.length ? 'blocked: ' + [...new Set(blocked)].slice(0, 10).join(', ') : 'none attempted');
  rec('no failed requests', failedReq.length === 0, failedReq.slice(0, 5).join(' ; ') || 'none');
  rec('no JS page errors', pageErrs.length === 0, pageErrs.slice(0, 5).join(' ; ') || 'none');
  rec('no console errors', consoleErrs.length === 0, consoleErrs.slice(0, 5).join(' ; ') || 'none');
  fs.writeFileSync('/home/user/Asad/android-app/qa/quiz_qa_results.json', JSON.stringify(results, null, 1));
  await browser.close(); srv.kill();
})().catch(e => { console.error('SCRIPT ERROR', e); process.exit(1); });
