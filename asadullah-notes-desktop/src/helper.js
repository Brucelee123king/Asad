/* Corner study helper: Offline tab searches the built-in question bank; Online tab asks an AI model (needs internet + the user's own API key). */
(function () {
  var AI = window.__anAI;
  var tab = null, history = [], files = [], busy = false, hasKey = false, flat = null, idx = null;
  var $ = function (id) { return document.getElementById(id); };
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }

  /* ---------- offline search over the question bank ---------- */
  var STOP = {the:1,a:1,an:1,of:1,in:1,on:1,is:1,are:1,was:1,were:1,to:1,for:1,and:1,or:1,what:1,which:1,who:1,whom:1,when:1,where:1,how:1,why:1,does:1,did:1,do:1,by:1,with:1,at:1,from:1,as:1,that:1,this:1,it:1,be:1,me:1,my:1,tell:1,about:1,please:1,explain:1,mcq:1,original:1};
  function tokens(s) { return String(s || '').toLowerCase().replace(/\(\d+\)|\(repeated in \d+ tests?\)|\(original mcq #\d+\)/g, ' ').split(/[^a-z0-9؀-ۿ]+/).filter(function (w) { return w.length > 1 && !STOP[w]; }); }
  function build() {
    if (flat) return; flat = []; var seen = {};
    Object.keys(ALL).forEach(function (k) { ALL[k].forEach(function (q) {
      var key = tokens(q.question).join(' ') + '|' + q.options[q.correct]; if (seen[key]) return; seen[key] = 1;
      flat.push({ q: q, tq: tokens(q.question), ta: tokens(q.options[q.correct]), to: tokens(q.options.join(' ')), tf: tokens((q.facts || '') + ' ' + (q.rel || '')) });
    }); });
  }
  function search(query) {
    build(); var qt = tokens(query); if (!qt.length) return [];
    var out = [];
    flat.forEach(function (e) {
      var sc = 0, hit = 0;
      qt.forEach(function (w) { var h = 0;
        if (e.tq.indexOf(w) >= 0) { sc += 3; h = 1; } if (e.ta.indexOf(w) >= 0) { sc += 3; h = 1; } if (e.to.indexOf(w) >= 0) { sc += 1; h = 1; } if (e.tf.indexOf(w) >= 0) { sc += 1; h = 1; }
        hit += h; });
      if (hit >= Math.max(1, Math.ceil(qt.length * 0.6))) out.push({ e: e, sc: sc + hit * 2 });
    });
    out.sort(function (a, b) { return b.sc - a.sc; });
    return out.slice(0, 4).map(function (x) { return x.e.q; });
  }
  function hitNode(q) {
    var d = el('div', 'anHit');
    d.appendChild(el('div', 'q', String(q.question).replace(/^\(Original MCQ #\d+\)\s*/, '').replace(/\s*\(\d+\)\s*$/, '')));
    d.appendChild(el('div', 'ans', 'Answer: ' + q.options[q.correct]));
    if (q.facts) d.appendChild(el('div', 'ex', 'Explanation: ' + q.facts));
    if (q.rel) d.appendChild(el('div', 'ex', 'Related: ' + q.rel));
    return d;
  }

  /* ---------- rendering ---------- */
  function mdNode(text) {
    var box = el('div'), list = null, kind = null;
    function inline(parent, s) { s.split(/(\*\*[^*]+\*\*|`[^`]+`)/g).forEach(function (p) { if (!p) return;
      if (/^\*\*[^*]+\*\*$/.test(p)) parent.appendChild(el('b', null, p.slice(2, -2))); else if (/^`[^`]+`$/.test(p)) parent.appendChild(el('code', null, p.slice(1, -1))); else parent.appendChild(document.createTextNode(p)); }); }
    String(text).split('\n').forEach(function (line) {
      var m;
      if ((m = /^\s*[-*•]\s+(.*)/.exec(line))) { if (kind !== 'ul') { list = el('ul'); box.appendChild(list); kind = 'ul'; } var li = el('li'); inline(li, m[1]); list.appendChild(li); }
      else if ((m = /^\s*\d+[.)]\s+(.*)/.exec(line))) { if (kind !== 'ol') { list = el('ol'); box.appendChild(list); kind = 'ol'; } var li2 = el('li'); inline(li2, m[1]); list.appendChild(li2); }
      else { kind = null; if (!line.trim()) return; if ((m = /^#{1,4}\s+(.*)/.exec(line))) { var h = el('h4'); inline(h, m[1]); box.appendChild(h); } else { var p = el('p'); inline(p, line); box.appendChild(p); } }
    });
    return box;
  }
  function add(cls, node) { var m = el('div', 'anM ' + cls); if (typeof node === 'string') m.textContent = node; else m.appendChild(node); var c = $('anMsgs'); c.appendChild(m); c.scrollTop = c.scrollHeight; return m; }

  /* ---------- UI ---------- */
  function mount() {
    var btn = el('button'); btn.id = 'anHelpBtn'; btn.type = 'button'; btn.title = 'Study helper'; btn.setAttribute('aria-label', 'Study helper'); btn.innerHTML = '<i class="fa-solid fa-robot"></i>';
    var p = el('div'); p.id = 'anHelp'; p.setAttribute('role', 'dialog'); p.setAttribute('aria-label', 'Study helper');
    p.innerHTML = '<div class="anHead"><i class="fa-solid fa-robot"></i><b>Study Helper</b><button type="button" id="anClear" title="New chat" aria-label="New chat"><i class="fa-solid fa-broom"></i></button><button type="button" id="anGear" title="Settings" aria-label="Settings"><i class="fa-solid fa-gear"></i></button><button type="button" id="anClose" title="Close" aria-label="Close"><i class="fa-solid fa-xmark"></i></button></div>' +
      '<div class="anTabs"><button type="button" id="anTabOff"><i class="fa-solid fa-book"></i> Offline</button><button type="button" id="anTabOn"><i class="fa-solid fa-globe"></i> Online</button></div>' +
      '<div class="anMsgs" id="anMsgs" aria-live="polite"></div><div class="anSet" id="anSet" style="display:none"></div>' +
      '<div class="anChips" id="anChips"></div><div class="anFiles" id="anFiles"></div>' +
      '<div class="anIn" id="anIn"><button type="button" class="sec" id="anAttach" title="Attach image or file" aria-label="Attach"><i class="fa-solid fa-paperclip"></i></button><textarea id="anText" rows="1" placeholder="Ask anything…" aria-label="Your question"></textarea><button type="button" id="anSend" title="Send" aria-label="Send"><i class="fa-solid fa-paper-plane"></i></button></div>' +
      '<input type="file" id="anFile" multiple accept="image/*,.pdf,.txt,.md,.csv,.json" style="display:none">';
    document.body.appendChild(p); document.body.appendChild(btn);
    btn.onclick = toggle; $('anClose').onclick = toggle;
    $('anTabOff').onclick = function () { setTab('off'); }; $('anTabOn').onclick = function () { setTab('on'); };
    $('anClear').onclick = function () { history = []; files = []; $('anMsgs').textContent = ''; renderFiles(); intro(); };
    $('anGear').onclick = function () { showSettings(true); };
    $('anSend').onclick = send; $('anAttach').onclick = function () { $('anFile').click(); };
    $('anFile').onchange = function (e) { addFiles(Array.prototype.slice.call(e.target.files)); e.target.value = ''; };
    var ta = $('anText');
    ta.addEventListener('keydown', function (e) { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(); } else if (e.key === 'Escape') toggle(); e.stopPropagation(); });
    ta.addEventListener('keyup', function (e) { e.stopPropagation(); }); ta.addEventListener('keypress', function (e) { e.stopPropagation(); });
    ta.addEventListener('input', function () { ta.style.height = 'auto'; ta.style.height = Math.min(110, ta.scrollHeight) + 'px'; });
    ta.addEventListener('paste', function (e) { var fs = []; Array.prototype.forEach.call((e.clipboardData && e.clipboardData.files) || [], function (f) { fs.push(f); }); if (fs.length) { e.preventDefault(); addFiles(fs); } });
    window.addEventListener('online', refresh); window.addEventListener('offline', refresh);
  }
  function toggle() { var p = $('anHelp'); var o = p.classList.toggle('open'); if (o) { refresh().then(function () { if (!$('anMsgs').children.length) intro(); $('anText').focus(); }); } }
  function refresh() {
    var p = AI ? AI.hasKey() : Promise.resolve(false);
    return p.then(function (k) { hasKey = !!k; if (tab === null) tab = (navigator.onLine && hasKey) ? 'on' : 'off'; setTab(tab, true); });
  }
  function setTab(t, quiet) {
    tab = t; $('anTabOff').classList.toggle('on', t === 'off'); $('anTabOn').classList.toggle('on', t === 'on');
    $('anSet').style.display = 'none'; $('anMsgs').style.display = ''; $('anIn').style.display = '';
    $('anAttach').disabled = (t !== 'on');
    $('anText').placeholder = t === 'on' ? 'Ask anything…' : 'Search questions, e.g. Mangla Dam';
    chips();
    if (!quiet) { $('anMsgs').textContent = ''; intro(); }
    if (t === 'on' && !hasKey) showSettings(false);
  }
  function intro() {
    if (tab === 'on') add('sys', navigator.onLine ? 'Online helper: ask in English, Urdu or Roman Urdu. Attach a screenshot, PDF or text file with the paperclip (or paste with Ctrl+V). Answers use web search; please double-check important current-affairs facts.' : 'You are offline. Use the Offline tab, or connect to the internet.');
    else add('sys', 'Offline helper: searches all ' + (function () { build(); return flat.length; })() + ' questions and their explanations on this computer. No internet needed. For general or current questions, use the Online tab.');
  }
  function qBlock(q) { return 'Question: ' + q.question + '\n' + q.options.map(function (o, i) { return 'ABCDE'[i] + ') ' + o; }).join('\n') + '\nCorrect answer (from the app): ' + 'ABCDE'[q.correct] + ') ' + q.options[q.correct] + (q.facts ? '\nApp note: ' + q.facts : '') + (q.rel ? '\nRelated fact: ' + q.rel : ''); }
  function currentQ() {
    try { if (typeof quizData !== 'undefined' && quizData.length && !document.getElementById('view-quiz').classList.contains('hidden')) { var q = quizData[currentQuestionIndex]; if (userAnswers[currentQuestionIndex] === null) return { locked: true }; return { q: q }; } } catch (e) {}
    return null;
  }
  /* quick actions for the question on screen: off = offline answer, on = prompt sent to the AI */
  var ACTIONS = [
    { label: 'Explain this question', off: function (q, m) { m.appendChild(hitNode(q)); }, on: 'Explain this MCQ step by step and say why the correct option is right.' },
    { label: 'Explain in simple words', off: function (q, m) { m.appendChild(el('div', 'ex', 'In short: the answer is "' + q.options[q.correct] + '".' + (q.facts ? ' ' + q.facts : ''))); }, on: 'Explain this MCQ in very simple words, like I am a beginner.' },
    { label: 'Explain in detail', off: null, on: 'Explain this MCQ in detail: the concept, background, and everything a student should know about this topic.' },
    { label: 'Why are the others wrong?', off: function (q, m) { q.options.forEach(function (o, i) { m.appendChild(el('div', 'ex', ('ABCDE'[i]) + ') ' + o + (i === q.correct ? '  ✔ correct' : '  ✘ not the answer'))); }); if (q.facts) m.appendChild(el('div', 'ex', 'Reason: ' + q.facts)); }, on: 'Explain why each wrong option is wrong, one by one.' },
    { label: 'Memory trick', off: null, on: 'Give me an easy memory trick or mnemonic to remember this answer.' },
    { label: 'Related facts', off: function (q, m) { m.appendChild(el('div', 'ex', q.rel || q.facts || 'No extra facts are stored for this question.')); }, on: 'Give related facts and background about this topic that could be asked in the exam.' },
    { label: 'Similar questions', off: function (q, m) { var r = search(tokens(q.question).concat(tokens(q.options[q.correct])).slice(0, 8).join(' ')).filter(function (x) { return x.question !== q.question; }); if (!r.length) m.appendChild(el('div', 'ex', 'No similar questions found.')); r.forEach(function (x) { m.appendChild(hitNode(x)); }); }, on: 'Write 3 new practice MCQs on the same topic with answers and short explanations.' },
    { label: 'Urdu mein samjhao', off: null, on: 'Is MCQ ko Urdu (Roman Urdu) mein asaan alfaz mein samjhao.' }
  ];
  function runAction(a) {
    var c = currentQ();
    if (!c) { add('sys', 'Open a question during a test first, then tap this.'); return; }
    if (c.locked) { add('sys', 'Answer the question first, then ask for the explanation.'); return; }
    if (tab === 'on') { if (!hasKey) { showSettings(false); return; } $('anText').value = a.on + '\n\n' + qBlock(c.q); send(a.label); }
    else if (a.off) { add('u', a.label); var m = add('a', ''); a.off(c.q, m); }
    else add('sys', '"' + a.label + '" needs the Online tab (internet + API key).');
  }
  function chips() {
    var c = $('anChips'); c.textContent = '';
    if (currentQ()) { var t = el('div', null, 'This question:'); t.style.cssText = 'width:100%;font-size:11.5px;opacity:.7'; c.appendChild(t); ACTIONS.forEach(function (a) { var b = el('button', null, a.label); b.type = 'button'; if (tab === 'off' && !a.off) b.style.opacity = '.5'; b.onclick = function () { runAction(a); }; c.appendChild(b); }); }
    else if (tab === 'on') ['Explain in simple words', 'Give more detail', 'Give an example'].forEach(function (x) { var k = el('button', null, x); k.type = 'button'; k.onclick = function () { $('anText').value = x; send(); }; c.appendChild(k); });
  }
  function showSettings(force) {
    var s = $('anSet'); s.textContent = ''; $('anChips').textContent = ''; $('anMsgs').style.display = 'none'; $('anIn').style.display = 'none'; s.style.display = '';
    s.appendChild(el('b', null, 'Online helper settings'));
    var small = el('small'); small.appendChild(document.createTextNode('The online tab needs your own Claude API key (it is saved encrypted on this computer and used only to contact the AI service). Create one at '));
    var a = el('a', null, 'console.anthropic.com'); a.href = 'https://console.anthropic.com/'; a.target = '_blank'; small.appendChild(a); small.appendChild(document.createTextNode('. Usage is billed by the provider.'));
    s.appendChild(small);
    var inp = el('input'); inp.type = 'password'; inp.placeholder = hasKey ? 'A key is saved — paste a new one to replace it' : 'Paste API key (sk-ant-…)'; inp.autocomplete = 'off'; s.appendChild(inp);
    var msg = el('small'); s.appendChild(msg);
    var save = el('button', null, 'Save key'); save.type = 'button'; save.onclick = function () { AI.setKey(inp.value).then(function (r) { if (r.ok) { hasKey = true; setTab('on'); } else msg.textContent = r.error; }); }; s.appendChild(save);
    if (hasKey) { var del = el('button', null, 'Remove saved key'); del.type = 'button'; del.style.background = '#64748b'; del.onclick = function () { AI.clearKey().then(function () { hasKey = false; showSettings(true); }); }; s.appendChild(del); }
    var back = el('button', null, 'Back'); back.type = 'button'; back.style.background = '#e2e8f0'; back.style.color = '#334155'; back.onclick = function () { setTab(hasKey ? tab : 'off'); }; s.appendChild(back);
  }
  function renderFiles() { var f = $('anFiles'); f.textContent = ''; files.forEach(function (x, i) { var s = el('span', null, '📎 ' + x.name + ' ✕'); s.title = 'Remove'; s.onclick = function () { files.splice(i, 1); renderFiles(); }; f.appendChild(s); }); }
  function addFiles(list) {
    if (tab !== 'on') { add('sys', 'Attachments work in the Online tab only.'); return; }
    list.slice(0, 5 - files.length).forEach(function (f) {
      if (f.size > 10 * 1024 * 1024) { add('err', f.name + ' is larger than 10 MB.'); return; }
      var r = new FileReader(); r.onload = function () { files.push({ name: f.name || 'pasted-image.png', type: f.type || 'application/octet-stream', data: String(r.result).split(',')[1] || '' }); renderFiles(); }; r.readAsDataURL(f);
    });
  }
  function send(label) {
    if (busy) return; var ta = $('anText'), text = ta.value.trim(); if (!text && !files.length) return;
    ta.value = ''; ta.style.height = 'auto';
    if (tab === 'off') {
      add('u', text); var res = search(text), m;
      if (!res.length) add('a', 'No match in your question bank for that. For general or current questions, switch to the Online tab.');
      else { m = add('a', ''); res.forEach(function (q) { m.appendChild(hitNode(q)); }); }
      return;
    }
    if (!navigator.onLine) { add('err', 'No internet connection. Use the Offline tab, or reconnect.'); return; }
    if (!hasKey) { showSettings(false); return; }
    add('u', (typeof label === 'string' ? label : text) + (files.length ? '\n📎 ' + files.map(function (f) { return f.name; }).join(', ') : ''));
    history.push({ role: 'user', text: text || 'Please look at the attached file.', attachments: files }); files = []; renderFiles();
    busy = true; $('anSend').disabled = true; var wait = add('sys', 'Thinking…');
    AI.chat({ messages: history }).then(function (r) {
      wait.remove(); busy = false; $('anSend').disabled = false;
      if (!r.ok) { history.pop(); if (r.error === 'no-key') { hasKey = false; showSettings(false); } else add('err', r.error); return; }
      history[history.length - 1].attachments = [];
      history.push({ role: 'assistant', text: r.text });
      var m = add('a', mdNode(r.text));
      if (r.note) add('sys', r.note);
      if (r.sources && r.sources.length) { var s = el('span', 'src'); s.appendChild(document.createTextNode('Sources: ')); r.sources.forEach(function (x, i) { var a = el('a', null, (x.title || x.url).slice(0, 50)); a.href = x.url; a.target = '_blank'; a.rel = 'noopener'; if (i) s.appendChild(document.createTextNode(' · ')); s.appendChild(a); }); m.appendChild(s); }
    }).catch(function () { wait.remove(); busy = false; $('anSend').disabled = false; history.pop(); add('err', 'Something went wrong. Please try again.'); });
  }
  function watch() {
    var upd = function () { if ($('anHelp') && $('anHelp').classList.contains('open') && $('anSet').style.display === 'none') chips(); };
    ['question-text', 'view-quiz'].forEach(function (id) { var n = document.getElementById(id); if (n) new MutationObserver(upd).observe(n, { childList: true, characterData: true, subtree: true, attributes: true, attributeFilter: ['class'] }); });
  }
  function start() { mount(); watch(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
