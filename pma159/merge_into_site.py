"""Builds site/index.html = the original 1000-MCQ site + the PMA 159 tests as a separate section.
usage: python3 merge_into_site.py <original_site.html> <output.html>"""
import json, os, random, re, sys, html
sys.path.insert(0, '.')
from questions import Q

src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf8').read()

# ---- 1. PMA data in the site's own question format ----
items = []
for i, (sec, q, ok, wrong, why, rep) in enumerate(Q):
    o = [ok] + list(wrong)
    random.Random(i * 7919 + 13).shuffle(o)
    assert not re.search(r'[<>&]', q + ''.join(o)), q
    items.append({"id": 0, "question": q + (f" (Repeated in {rep} test{'s' if rep > 1 else ''})" if rep else ""),
                  "options": o, "correct": o.index(ok), "facts": why, "pma": True, "sec": sec})
PMA = {}
for n in range((len(items) + 49) // 50):
    chunk = items[n * 50:(n + 1) * 50]
    for k, it in enumerate(chunk): it["id"] = k + 1
    PMA[f"PMA-{n + 1}"] = chunk

import glob, runpy
FA = {}
fa_items = []
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fa_parts', 'fa_0*.py'))):
    fa_items += runpy.run_path(f)['QS']
_ov = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fa_parts', 'fa_overrides.py'))
_lab = lambda q: q.split(')', 1)[0] + ')'
_removed = [it for it in fa_items if _lab(it[1]) in _ov['REMOVE']]
assert len(_removed) == len(_ov['REMOVE']), (len(_removed), len(_ov['REMOVE']))
fa_items = [it for it in fa_items if _lab(it[1]) not in _ov['REMOVE']]
_fixed = []
for _i, (_sec, _q, _o, _a, _why, _rel) in enumerate(fa_items):
    _f = _ov['FIX'].get(_lab(_q))
    if _f:
        _a = _f.get('correct', _a); _why = _f.get('reason', _why) + _f.get('append_reason', ''); _rel = _f.get('rel', _rel)
        if 'append_reason' in _f and 'reason' not in _f: _why = fa_items[_i][4] + _f['append_reason']
        fa_items[_i] = (_sec, _q, _o, _a, _why, _rel); _fixed.append(_lab(_q))
assert sorted(_fixed) == sorted(_ov['FIX']), set(_ov['FIX']) ^ set(_fixed)
for n in range((len(fa_items) + 49) // 50):
    FA['FA-%d' % (n + 1)] = [{"id": k + 1, "question": q, "options": o, "correct": a, "facts": why, "rel": rel, "pma": True, "sec": sec}
                              for k, (sec, q, o, a, why, rel) in enumerate(fa_items[n * 50:(n + 1) * 50])]

HK = {}
hk_items = []
_hkp = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pma149', 'hk_final.json')
_hkp2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pma150', 'hk_final2.json')
if os.path.exists(_hkp2): _hkp = _hkp2
_hkp3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pma151', 'hk_final3.json')
if os.path.exists(_hkp3): _hkp = _hkp3
_hkp4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dedupe', 'hk_final_dedup.json')
if os.path.exists(_hkp4): _hkp = _hkp4
_hkp5 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dedupe', 'hk_final_dedup2.json')
if os.path.exists(_hkp5): _hkp = _hkp5
_hkp6 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pma152', 'hk_final4.json')
if os.path.exists(_hkp6): _hkp = _hkp6
_hkp7 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pma152', 'hk_final5.json')
if os.path.exists(_hkp7): _hkp = _hkp7; _hkp6 = _hkp7
_hkp8 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pma153', 'hk_final7.json')
if os.path.exists(_hkp8): _hkp = _hkp8; _hkp6 = _hkp8
if os.path.exists(_hkp):
    hk_items = json.load(open(_hkp, encoding='utf8'))
# Hakeem section is split by experience: each MCQ lives in the PMA (149/150/151/152/153) where it first appeared;
# repeats from later PMAs only raise its bracket count. Origin list: dedupe/make_origin.py
HK_META = {}
_hko = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', *(('pma153', 'hk_origin7.json') if _hkp == _hkp8 else ('pma152', 'hk_origin5.json' if _hkp == _hkp7 else 'hk_origin4.json'))) if os.path.exists(_hkp6) else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dedupe', 'hk_origin2.json')
hk_org = json.load(open(_hko)) if os.path.exists(_hko) and len(json.load(open(_hko))) == len(hk_items) else [149] * len(hk_items)
_hn = 0
for _p in (149, 150, 151, 152, 153):
    _its = [it for it, o_ in zip(hk_items, hk_org) if o_ == _p]
    for n in range((len(_its) + 49) // 50):
        _hn += 1
        HK_META['HK-%d' % _hn] = {"pma": _p, "part": n + 1}
        HK['HK-%d' % _hn] = [{"id": k + 1, "question": q + (' (%d)' % rep if rep > 1 else ''), "options": o, "correct": a, "facts": why, "rel": rel,
                              "pma": True, "sec": sec, "rep": rep}
                             for k, (sec, q, o, a, why, rel, rep) in enumerate(_its[n * 50:(n + 1) * 50])]

def sub(a, b, count=1):
    global s
    assert s.count(a) == count, (s.count(a), a[:80])
    s = s.replace(a, b)

# insert data right after the ALL object
SPLIT_JS = '''(function () {
            const NEW = {};
            Object.keys(ALL).forEach(k => {
                const a = parseInt(k.split('-')[0], 10), b = parseInt(k.split('-')[1], 10), arr = ALL[k];
                const half = arr.length / 2;
                NEW[a + '-' + (a + half - 1)] = arr.slice(0, half).map((q, i) => Object.assign({}, q, { id: i + 1 }));
                NEW[(a + half) + '-' + b] = arr.slice(half).map((q, i) => Object.assign({}, q, { id: i + 1 }));
            });
            Object.keys(ALL).forEach(k => delete ALL[k]);
            Object.assign(ALL, NEW);
        })();
        '''
m = re.search(r'const ALL = ', s)
eol = s.index('\n', m.start())
assert s[:eol].rstrip().endswith(';')
s = s[:eol] + '\n        const PMA_DATA = ' + json.dumps(PMA, ensure_ascii=False) + ';\n        ' + SPLIT_JS + 'Object.assign(ALL, PMA_DATA);\n        const FA_DATA = ' + json.dumps(FA, ensure_ascii=False) + ';\n        Object.assign(ALL, FA_DATA);\n        const HK_DATA = ' + json.dumps(HK, ensure_ascii=False) + ';\n        Object.assign(ALL, HK_DATA);\n        const HK_META = ' + json.dumps(HK_META) + ';\n        let TEST_SECS = 1200;\n        const isPMA = k => String(k).indexOf("PMA-") === 0;\n        const isFA = k => String(k).indexOf("FA-") === 0;\n        const isHK = k => String(k).indexOf("HK-") === 0;\n        const isExtra = k => isPMA(k) || isFA(k) || isHK(k);' + s[eol:]

# ---- 2. second section on the selection page ----
sub('<div id="test-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>',
    '''<div id="test-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>
            <div class="bg-gradient-to-r from-emerald-700 to-teal-600 rounded-2xl text-white text-center px-6 py-8 sm:p-10 mt-10 mb-6 shadow-xl">
                <span class="inline-block bg-white/20 text-emerald-50 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider mb-3">@@PMA_COUNT@@</span>
                <h2 class="text-2xl sm:text-3xl font-bold tracking-tight mb-2">PMA 159 Long Course &ndash; Initial Test Practice</h2>
                <p class="text-emerald-50 text-sm sm:text-base">Built from PMA 159 test experiences. Questions marked (Repeated in N tests) were reported in several experiences. Every answer comes with a reason.</p>
            </div>
            <div id="pma-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>
            <div class="bg-gradient-to-r from-amber-700 to-orange-600 rounded-2xl text-white text-center px-6 py-8 sm:p-10 mt-10 mb-6 shadow-xl">
                <span class="inline-block bg-white/20 text-amber-50 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider mb-3">@@FA_COUNT@@</span>
                <h2 class="text-2xl sm:text-3xl font-bold tracking-tight mb-2">Forces Academy Lahore &ndash; Intelligence and Academic Practice</h2>
                <p class="text-amber-50 text-sm sm:text-base">Forces Academy intelligence tests 1 to 20 (verbal) and academic questions, in blocks of 50. Every answer shows a reason and a related fact.</p>
            </div>
            <div id="fa-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>''')

s = s.replace('@@PMA_COUNT@@', '%d Tests &bull; %d MCQs' % (len(PMA), len(items)))
s = s.replace('@@FA_COUNT@@', '%d Tests &bull; %d MCQs' % (len(FA), len(fa_items)))
# ---- 3. render both grids ----
sub("grid.innerHTML = Object.keys(ALL).map((k, i) => {",
    "grid.innerHTML = Object.keys(ALL).filter(k => !isExtra(k)).map((k, i) => {")
sub("function selectTest(k) {", '''function renderPMA() {
            const g = document.getElementById('pma-grid');
            g.innerHTML = Object.keys(ALL).filter(isPMA).map((k, i) => {
                let best = null; try { best = localStorage.getItem('mc_best_' + k); } catch (e) {}
                const secs = [...new Set(ALL[k].map(q => q.sec))].join(' &bull; ');
                return `<button type="button" onclick="selectTest('${k}')" class="text-left bg-white rounded-2xl border border-slate-200 hover:border-emerald-500 hover:shadow-lg transition p-5 flex flex-col gap-3">
                    <div class="flex items-center justify-between"><span class="bg-emerald-100 text-emerald-800 text-xs font-bold px-3 py-1 rounded-full">PMA Test ${i + 1}</span>${best !== null ? `<span class="text-xs font-bold text-emerald-600"><i class="fa-solid fa-trophy"></i> Best ${best}%</span>` : '<span class="text-xs text-slate-400">Not attempted</span>'}</div>
                    <div class="text-xl font-bold text-slate-900">PMA 159 &ndash; Part ${i + 1}</div>
                    <div class="text-xs text-slate-500">${secs}</div>
                    <div class="text-xs text-slate-500">${ALL[k].length} MCQs &bull; ${Math.max(1, Math.ceil(Math.max(60, ALL[k].length * 12) / 60))} Minutes &bull; Instant feedback</div>
                    <div class="text-sm font-semibold text-emerald-700">${best !== null ? 'Try again' : 'Start'} <i class="fa-solid fa-arrow-right ml-1"></i></div></button>`;
            }).join('');
        }
        function selectTest(k) {''')
FA_RENDER = r'''function renderFA() {
            const g = document.getElementById('fa-grid');
            g.innerHTML = Object.keys(ALL).filter(isFA).map((k, i) => {
                let best = null; try { best = localStorage.getItem('mc_best_' + k); } catch (e) {}
                const secs = [...new Set(ALL[k].map(q => q.sec.replace('Forces Academy ', '')))].join(' &bull; ');
                return `<button type="button" onclick="selectTest('${k}')" class="text-left bg-white rounded-2xl border border-slate-200 hover:border-amber-500 hover:shadow-lg transition p-5 flex flex-col gap-3">
                    <div class="flex items-center justify-between"><span class="bg-amber-100 text-amber-800 text-xs font-bold px-3 py-1 rounded-full">FA Test ${i + 1}</span>${best !== null ? `<span class="text-xs font-bold text-emerald-600"><i class="fa-solid fa-trophy"></i> Best ${best}%</span>` : '<span class="text-xs text-slate-400">Not attempted</span>'}</div>
                    <div class="text-xl font-bold text-slate-900">Forces Academy &ndash; Part ${i + 1}</div>
                    <div class="text-xs text-slate-500">${secs}</div>
                    <div class="text-xs text-slate-500">${ALL[k].length} MCQs &bull; ${Math.max(1, Math.ceil(Math.max(60, ALL[k].length * 12) / 60))} Minutes &bull; Instant feedback</div>
                    <div class="text-sm font-semibold text-amber-700">${best !== null ? 'Try again' : 'Start'} <i class="fa-solid fa-arrow-right ml-1"></i></div></button>`;
            }).join('');
        }
        function selectTest(k) {'''
sub("            renderSelect(); window.scrollTo(0, 0);\n        }\n\n        function bootQuizApp() {\n            renderSelect();",
    "            renderSelect(); renderPMA(); window.scrollTo(0, 0);\n        }\n\n        function bootQuizApp() {\n            renderSelect(); renderPMA();")

# ---- 4. selectTest: labels + per-test time ----
sub("const label = k.replace('-', '–');\n            document.getElementById('q-total').textContent = quizData.length;\n            document.getElementById('home-badge').textContent = '100 MCQs (Original Questions ' + label + ')';\n            document.getElementById('home-desc').textContent = 'Challenge yourself with 100 MCQs from original questions ' + label + '.';",
    """const label = k.replace('-', '–');
            const nQ = quizData.length;
            TEST_SECS = isPMA(k) ? Math.max(60, nQ * 12) : 600;
            const nMin = Math.ceil(TEST_SECS / 60);
            document.getElementById('q-total').textContent = nQ;
            document.getElementById('home-badge').textContent = isPMA(k) ? (nQ + ' MCQs (PMA 159 Long Course – Part ' + k.slice(4) + ')') : (nQ + ' MCQs (Original Questions ' + label + ')');
            document.getElementById('home-desc').textContent = isPMA(k) ? ('Practice ' + nQ + ' MCQs from PMA 159 test experiences. Every answer shows a reason.') : ('Challenge yourself with ' + nQ + ' MCQs from original questions ' + label + '.');
            document.getElementById('info-total').textContent = nQ + ' MCQs';
            document.getElementById('info-time').textContent = nMin + ' Minutes';
            document.getElementById('info-timer-note').textContent = '• The quiz will auto-submit when the ' + nMin + '-minute timer expires.';""")
sub('<div class="text-lg font-bold text-slate-900">100 MCQs</div>', '<div id="info-total" class="text-lg font-bold text-slate-900">100 MCQs</div>')
sub('<div class="text-lg font-bold text-slate-900">20 Minutes</div>', '<div id="info-time" class="text-lg font-bold text-slate-900">20 Minutes</div>')
sub('<p>• The quiz will auto-submit when the 20-minute timer expires.</p>', '<p id="info-timer-note">• The quiz will auto-submit when the 20-minute timer expires.</p>')
sub("\n            timeRemaining = 1200;\n", "\n            timeRemaining = TEST_SECS;\n")
sub("const elapsedSeconds = 1200 - timeRemaining;", "const elapsedSeconds = TEST_SECS - timeRemaining;")

# ---- 5. feedback + reason for PMA questions ----
sub("""if (q.facts) { const ff = document.createElement('div'); ff.className = 'mt-2 p-3 rounded-xl text-xs sm:text-sm bg-slate-100 text-slate-600'; ff.innerHTML = '<b class="text-slate-700">Related facts:</b> ';""",
    """if (q.pma && !ok) { const wy = document.createElement('div'); wy.className = 'mt-2 p-3 rounded-xl text-sm bg-rose-50 text-rose-800'; wy.innerHTML = '<b>Why your choice is wrong:</b> '; wy.appendChild(document.createTextNode('You chose ' + String.fromCharCode(65 + userAnswers[index]) + ') ' + q.options[userAnswers[index]] + '. That option does not answer this question correctly.')); optionsContainer.appendChild(wy); }
                if (q.facts) { const ff = document.createElement('div'); ff.className = q.pma ? 'mt-2 p-3 rounded-xl text-sm bg-emerald-50 text-emerald-900' : 'mt-2 p-3 rounded-xl text-xs sm:text-sm bg-slate-100 text-slate-600'; ff.innerHTML = q.pma ? '<b>Why ' + String.fromCharCode(65 + q.correct) + ') ' + q.options[q.correct] + ' is correct:</b> ' : '<b class="text-slate-700">Related facts:</b> ';""")
sub("""                    <div class="space-y-1.5 pt-1">${optionsHtml}</div>
                `;""", """                    <div class="space-y-1.5 pt-1">${optionsHtml}</div>
                    ${q.pma ? '<div class="p-3 rounded-lg text-xs sm:text-sm bg-emerald-50 text-emerald-900"><b>Reason:</b> ' + q.facts + '</div>' : ''}
                `;""")

# ---- 8. 20 tests of 50 MCQs ----
sub('10 Tests &bull; 1000 MCQs', '20 Tests &bull; 1000 MCQs')
sub('Original questions 1 to 1000, in 10 tests of 100 MCQs each, all questions included.', 'Original questions 1 to 1000, in 20 tests of 50 MCQs each, all questions included.')
sub('${ALL[k].length} MCQs &bull; 20 Minutes &bull; Instant feedback</div>\n                    <div class="text-sm font-semibold text-indigo-600">', '${ALL[k].length} MCQs &bull; 10 Minutes &bull; Instant feedback</div>\n                    <div class="text-sm font-semibold text-indigo-600">')
sub('<div id="info-total" class="text-lg font-bold text-slate-900">100 MCQs</div>', '<div id="info-total" class="text-lg font-bold text-slate-900">50 MCQs</div>')
sub('<div id="info-time" class="text-lg font-bold text-slate-900">20 Minutes</div>', '<div id="info-time" class="text-lg font-bold text-slate-900">10 Minutes</div>')
sub('auto-submit when the 20-minute timer expires.</p>', 'auto-submit when the 10-minute timer expires.</p>')

# ---- 6. branding: Asadullah Notes, Asad signature ----
import base64, os
sub('<title>Mission Commission Academy – MCQ Tests 1 to 1000</title>', '<title>Asadullah Notes – MCQ Tests 1 to 1000</title>')
sub('tracking-tight">Mission Commission Academy</h1>', 'tracking-tight">Asadullah Notes</h1>')
sub('This test belongs to <span class="text-indigo-600 font-bold">Mission Commission Academy</span>', 'This test belongs to <span class="text-indigo-600 font-bold">Asadullah Notes</span>')
sub('Software Created by Admin Mubasher', 'Software Created by Admin Asadullah')
sub('<h1 class="ln">MISSION <span>COMMISSION</span></h1>', '<h1 class="ln">ASADULLAH <span>NOTES</span></h1>')
sub('This test is provided by Mission Commission for all of you.', 'This test is provided by Asadullah Notes for all of you.')
sub('Special thanks to Sir Safeer and his admins.', 'Special thanks to Asadullah and his admins.')
sig = base64.b64encode(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'asad_signature.jpg'), 'rb').read()).decode()
s, n = re.subn(r'(<div class="sig"><img alt="Signature" src=")[^"]+(")', lambda m: m.group(1) + 'data:image/jpeg;base64,' + sig + m.group(2), s)
assert n == 1
assert 'Mission Commission' not in s and 'MISSION <span>' not in s and 'Mubasher' not in s and 'Safeer' not in s
# ---- 7. splash screen: black instead of green ----
sub('radial-gradient(circle at 50% 20%,#1f3a2a 0%,#0b120f 65%)', 'radial-gradient(circle at 50% 20%,#2a2a2a 0%,#000000 65%)')
sub('background:#6f8f52;top:-60px', 'background:#555555;top:-60px')
sub('color:#91ad70;margin:12px 0 22px', 'color:#bdbdbd;margin:12px 0 22px')
sub('color:#e4ebe5;animation-delay:2s', 'color:#ececec;animation-delay:2s')
sub('background:linear-gradient(135deg,#6f8f52,#4e6b38);color:#fff;border:1px solid rgba(255,255,255,.2)', 'background:linear-gradient(135deg,#2e2e2e,#0a0a0a);color:#fff;border:1px solid rgba(197,167,90,.6)')
sub('color:#9aa8a0;background:none;border:1px solid rgba(255,255,255,.15)', 'color:#b5b5b5;background:none;border:1px solid rgba(255,255,255,.2)')

# ---- 9. Forces Academy section ----
sub("function selectTest(k) {", FA_RENDER)
sub("renderSelect(); renderPMA(); window.scrollTo(0, 0);", "renderSelect(); renderPMA(); renderFA(); window.scrollTo(0, 0);")
sub("function bootQuizApp() {\n            renderSelect(); renderPMA();", "function bootQuizApp() {\n            renderSelect(); renderPMA(); renderFA();")
sub("TEST_SECS = isPMA(k) ? Math.max(60, nQ * 12) : 600;", "TEST_SECS = isExtra(k) ? Math.max(60, nQ * 12) : 600;")
sub("isPMA(k) ? (nQ + ' MCQs (PMA 159 Long Course – Part ' + k.slice(4) + ')')", "isExtra(k) ? (nQ + (isFA(k) ? ' MCQs (Forces Academy Lahore – Part ' + k.slice(3) + ')' : ' MCQs (PMA 159 Long Course – Part ' + k.slice(4) + ')'))")
sub("isPMA(k) ? ('Practice ' + nQ + ' MCQs from PMA 159 test experiences. Every answer shows a reason.')", "isExtra(k) ? ('Practice ' + nQ + (isFA(k) ? ' MCQs from Forces Academy Lahore tests and academic lists. Every answer shows a reason and a related fact.' : ' MCQs from PMA 159 test experiences. Every answer shows a reason.'))")
sub("optionsContainer.appendChild(ff); }", "optionsContainer.appendChild(ff); }\n                if (q.rel) { const rf = document.createElement('div'); rf.className = 'mt-2 p-3 rounded-xl text-xs sm:text-sm bg-slate-100 text-slate-700'; rf.innerHTML = '<b>Related fact:</b> '; rf.appendChild(document.createTextNode(q.rel)); optionsContainer.appendChild(rf); }")
sub("<b>Reason:</b> ' + q.facts + '</div>' : ''}", "<b>Reason:</b> ' + q.facts + '</div>' : ''}\n                    ${q.rel ? '<div class=\"p-3 rounded-lg text-xs sm:text-sm bg-slate-100 text-slate-700\"><b>Related fact:</b> ' + q.rel + '</div>' : ''}")

# ---- 10. Hakeem Force Academy section ----
sub('<div id="fa-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>', '''<div id="fa-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>
            <div class="bg-gradient-to-r from-sky-700 to-cyan-500 rounded-2xl text-white text-center px-6 py-8 sm:p-10 mt-10 mb-6 shadow-xl">
                <span class="inline-block bg-white/20 text-sky-50 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider mb-3">@@HK_COUNT@@</span>
                <h2 class="text-2xl sm:text-3xl font-bold tracking-tight mb-2">Hakeem Force Academy</h2>
                <p class="text-sky-50 text-sm sm:text-base">Choose PMA 149, 150, 151, 152 or 153 experience. Every question is written only once. The number in brackets shows how many times that question was repeated. The most repeated questions come first. Every answer has a reason and a related fact, and current-affairs answers are updated to today.</p>
            </div>
            <div id="hk-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>''')
s = s.replace('@@HK_COUNT@@', '%d Tests &bull; %d MCQs' % (len(HK), len(hk_items)))
sub("function selectTest(k) {", """let hkSub = null;
        function openHkSub(p) { hkSub = p; renderHK(); window.scrollTo(0, 0); }
        function renderHK() {
            const g = document.getElementById('hk-grid');
            const ks = Object.keys(ALL).filter(isHK);
            if (hkSub === null) {
                g.innerHTML = [149, 150, 151, 152, 153].map(p => {
                    const pk = ks.filter(k => HK_META[k].pma === p), n = pk.reduce((t, k) => t + ALL[k].length, 0);
                    return `<button type="button" onclick="openHkSub(${p})" class="text-left bg-white rounded-2xl border border-slate-200 hover:border-sky-500 hover:shadow-lg transition p-6 flex flex-col gap-3">
                        <div class="flex items-center gap-3"><i class="fa-solid fa-medal text-2xl text-sky-600"></i><span class="text-xl font-bold text-slate-900">PMA ${p} Experience</span></div>
                        <div class="text-xs text-slate-500">${pk.length} Tests &bull; ${n} MCQs</div>
                        <div class="text-sm font-semibold text-sky-700">Open <i class="fa-solid fa-arrow-right ml-1"></i></div></button>`;
                }).join('');
                return;
            }
            const bar = '<div class="col-span-full"><button type="button" onclick="openHkSub(null)" class="inline-flex items-center gap-2 bg-white border border-slate-200 hover:border-sky-400 text-slate-700 text-sm font-semibold px-4 py-2 rounded-full shadow-sm"><i class="fa-solid fa-arrow-left"></i> Hakeem Force Academy</button><div class="text-lg font-bold text-slate-900 mt-3">PMA ' + hkSub + ' Experience</div></div>';
            g.innerHTML = bar + ks.filter(k => HK_META[k].pma === hkSub).map(k => {
                let best = null; try { best = localStorage.getItem('mc_best_' + k); } catch (e) {}
                const part = HK_META[k].part;
                const reps = ALL[k].map(q => q.rep || 1), hi = Math.max.apply(null, reps), lo = Math.min.apply(null, reps);
                const rtxt = hi > 1 ? ('Repeated ' + hi + (lo !== hi ? ' to ' + lo : '') + ' times') : 'Asked once each';
                return `<button type="button" onclick="selectTest('${k}')" class="text-left bg-white rounded-2xl border border-slate-200 hover:border-sky-500 hover:shadow-lg transition p-5 flex flex-col gap-3">
                    <div class="flex items-center justify-between"><span class="bg-sky-100 text-sky-800 text-xs font-bold px-3 py-1 rounded-full">PMA ${hkSub} &bull; Test ${part}</span>${best !== null ? `<span class="text-xs font-bold text-emerald-600"><i class="fa-solid fa-trophy"></i> Best ${best}%</span>` : '<span class="text-xs text-slate-400">Not attempted</span>'}</div>
                    <div class="text-xl font-bold text-slate-900">PMA ${hkSub} Experience &ndash; Part ${part}</div>
                    <div class="text-xs text-slate-500">${rtxt}</div>
                    <div class="text-xs text-slate-500">${ALL[k].length} MCQs &bull; ${Math.max(1, Math.ceil(Math.max(60, ALL[k].length * 12) / 60))} Minutes &bull; Instant feedback</div>
                    <div class="text-sm font-semibold text-sky-700">${best !== null ? 'Try again' : 'Start'} <i class="fa-solid fa-arrow-right ml-1"></i></div></button>`;
            }).join('');
        }
        function selectTest(k) {""")
sub("renderSelect(); renderPMA(); renderFA(); window.scrollTo(0, 0);", "renderSelect(); renderPMA(); renderFA(); renderHK(); window.scrollTo(0, 0);")
sub("function bootQuizApp() {\n            renderSelect(); renderPMA(); renderFA();", "function bootQuizApp() {\n            renderSelect(); renderPMA(); renderFA(); renderHK();")
sub("(isFA(k) ? ' MCQs (Forces Academy Lahore – Part ' + k.slice(3) + ')' : ' MCQs (PMA 159 Long Course – Part ' + k.slice(4) + ')')", "(isHK(k) ? ' MCQs (Hakeem Force Academy – PMA ' + HK_META[k].pma + ' Part ' + HK_META[k].part + ')' : isFA(k) ? ' MCQs (Forces Academy Lahore – Part ' + k.slice(3) + ')' : ' MCQs (PMA 159 Long Course – Part ' + k.slice(4) + ')')")
sub("(isFA(k) ? ' MCQs from Forces Academy Lahore tests and academic lists. Every answer shows a reason and a related fact.' : ' MCQs from PMA 159 test experiences. Every answer shows a reason.')", "(isHK(k) ? ' MCQs from PMA ' + HK_META[k].pma + ' test experiences. The number in brackets is how many times the question was repeated. Every answer shows a reason and a related fact.' : isFA(k) ? ' MCQs from Forces Academy Lahore tests and academic lists. Every answer shows a reason and a related fact.' : ' MCQs from PMA 159 test experiences. Every answer shows a reason.')")

MENU_JS = """let curSec = null, menuReady = false;
        const SECS = [
            {id: 'o', name: '1000 MCQs', sub: 'Original questions 1 to 1000', grad: 'from-indigo-600 to-violet-600', icon: 'fa-book', test: k => !isExtra(k)},
            {id: 'pma', name: 'PMA 159 MCQs', sub: 'PMA 159 Long Course test experiences', grad: 'from-emerald-700 to-teal-600', icon: 'fa-shield-halved', test: k => isPMA(k)},
            {id: 'fa', name: 'Forces Academy Lahore MCQs', sub: 'Intelligence tests and academic practice', grad: 'from-amber-700 to-orange-600', icon: 'fa-brain', test: k => isFA(k)},
            {id: 'hk', name: 'Hakeem Force Academy MCQs', sub: 'PMA 149, 150, 151, 152 and 153 initial experiences', grad: 'from-sky-700 to-cyan-500', icon: 'fa-medal', test: k => isHK(k)}
        ];
        function initMenu() {
            if (menuReady) return; menuReady = true;
            const v = document.getElementById('view-select');
            const kids = Array.from(v.children);
            SECS.forEach((sc, i) => {
                const a = kids[2 * i], b = kids[2 * i + 1];
                a.dataset.sec = sc.id; b.dataset.sec = sc.id;
                const bar = document.createElement('div');
                bar.dataset.sec = sc.id; bar.className = 'mb-4';
                bar.innerHTML = '<button type="button" onclick="openSec(null)" class="inline-flex items-center gap-2 bg-white border border-slate-200 hover:border-indigo-400 text-slate-700 text-sm font-semibold px-4 py-2 rounded-full shadow-sm"><i class="fa-solid fa-arrow-left"></i> All categories</button>';
                v.insertBefore(bar, a);
                a.classList.remove('mt-10');
            });
            const m = document.createElement('div'); m.id = 'sec-menu'; v.insertBefore(m, v.firstChild);
        }
        function renderMenu() {
            const keys = Object.keys(ALL);
            document.getElementById('sec-menu').innerHTML = '<div class="text-center mb-6"><h2 class="text-2xl sm:text-3xl font-bold tracking-tight text-slate-900">Choose a Category</h2><p class="text-slate-500 text-sm mt-1">Tap a category to see its tests</p></div><div class="grid grid-cols-1 sm:grid-cols-2 gap-4">' + SECS.map(sc => {
                const ks = keys.filter(sc.test), n = ks.reduce((t, k) => t + ALL[k].length, 0);
                return `<button type="button" onclick="openSec('${sc.id}')" class="text-left bg-gradient-to-r ${sc.grad} text-white rounded-2xl shadow-xl hover:shadow-2xl hover:scale-[1.01] transition p-6 flex flex-col gap-2">
                    <div class="flex items-center gap-3"><i class="fa-solid ${sc.icon} text-2xl"></i><span class="text-xl sm:text-2xl font-bold">${sc.name}</span></div>
                    <div class="text-white/90 text-sm">${sc.sub}</div>
                    <div class="text-white/80 text-xs font-semibold">${ks.length} Tests &bull; ${n} MCQs</div>
                    <div class="text-sm font-bold mt-1">Open <i class="fa-solid fa-arrow-right ml-1"></i></div></button>`;
            }).join('') + '</div>';
        }
        function applySec() {
            initMenu(); renderMenu();
            const v = document.getElementById('view-select');
            Array.from(v.children).forEach(e => {
                if (e.id === 'sec-menu') e.classList.toggle('hidden', curSec !== null);
                else e.classList.toggle('hidden', e.dataset.sec !== curSec);
            });
        }
        function openSec(id) { curSec = id; applySec(); window.scrollTo(0, 0); }
        function bootQuizApp() {"""
sub("function bootQuizApp() {", MENU_JS)
sub("renderSelect(); renderPMA(); renderFA(); renderHK(); window.scrollTo(0, 0);", "renderSelect(); renderPMA(); renderFA(); renderHK(); applySec(); window.scrollTo(0, 0);")
sub("function bootQuizApp() {\n            renderSelect(); renderPMA(); renderFA(); renderHK();", "function bootQuizApp() {\n            renderSelect(); renderPMA(); renderFA(); renderHK(); applySec();")

# login screen (glassy sign in / create account / continue as guest) and day-night mode
_d = os.path.dirname(os.path.abspath(__file__))
_blk = open(os.path.join(_d, 'theme_block.html'), encoding='utf8').read() + open(os.path.join(_d, 'auth_block.html'), encoding='utf8').read() + open(os.path.join(_d, 'seccolor_block.html'), encoding='utf8').read() + open(os.path.join(_d, 'polish_block.html'), encoding='utf8').read() + open(os.path.join(_d, 'backnav_block.html'), encoding='utf8').read() + open(os.path.join(_d, 'features_block.html'), encoding='utf8').read() + open(os.path.join(_d, 'glass_block.html'), encoding='utf8').read() + open(os.path.join(_d, 'd3_block.html'), encoding='utf8').read()
import json as _j
_imgs=_j.load(open(os.path.join(_d,'space_imgs.json')))
for _k,_v in _imgs.items(): _blk=_blk.replace('{{IMG_'+_k+'}}','data:image/webp;base64,'+_v)
assert s.count('<div id="splash"') == 1
s = s.replace('<div id="splash"', _blk + '\n<div id="splash"')

# user request: 20 minutes for every 50-MCQ test (24 seconds per MCQ)
s = s.replace("TEST_SECS = isExtra(k) ? Math.max(60, nQ * 12) : 600;", "TEST_SECS = isExtra(k) ? Math.max(60, nQ * 24) : 1200;")
s = s.replace("ALL[k].length * 12) / 60))} Minutes", "ALL[k].length * 24) / 60))} Minutes")
s = s.replace("${ALL[k].length} MCQs &bull; 10 Minutes &bull;", "${ALL[k].length} MCQs &bull; 20 Minutes &bull;")
s = s.replace('<div id="info-time" class="text-lg font-bold text-slate-900">10 Minutes</div>', '<div id="info-time" class="text-lg font-bold text-slate-900">20 Minutes</div>')
s = s.replace("auto-submit when the 10-minute timer expires.", "auto-submit when the 20-minute timer expires.")
assert "nQ * 24" in s and "* 12) / 60" not in s and "10 Minutes" not in s

# user request: remove the front "ASADULLAH NOTES presents" splash page completely
import re as _re
_a = s.index('<div id="splash"'); _b = s.index('</script>', s.index('setTimeout(closeSplash', _a)) + len('</script>')
s = s[:_a] + '<script>function closeSplash(){}</script>' + s[_b:]
s = _re.sub(r'[ \t]*#splash[^\n]*\n', '', s)
assert 'id="splash"' not in s

open(out, 'w', encoding='utf8').write(s)
print("written", out, len(s))
