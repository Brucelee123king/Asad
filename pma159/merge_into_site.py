"""Builds site/index.html = the original 1000-MCQ site + the PMA 159 tests as a separate section.
usage: python3 merge_into_site.py <original_site.html> <output.html>"""
import json, random, re, sys, html
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
for n in range(5):
    chunk = items[n * 50:(n + 1) * 50]
    for k, it in enumerate(chunk): it["id"] = k + 1
    PMA[f"PMA-{n + 1}"] = chunk

def sub(a, b, count=1):
    global s
    assert s.count(a) == count, (s.count(a), a[:80])
    s = s.replace(a, b)

# insert data right after the ALL object
m = re.search(r'const ALL = ', s)
eol = s.index('\n', m.start())
assert s[:eol].rstrip().endswith(';')
s = s[:eol] + '\n        const PMA_DATA = ' + json.dumps(PMA, ensure_ascii=False) + ';\n        Object.assign(ALL, PMA_DATA);\n        let TEST_SECS = 1200;\n        const isPMA = k => String(k).indexOf("PMA-") === 0;' + s[eol:]

# ---- 2. second section on the selection page ----
sub('<div id="test-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>',
    '''<div id="test-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>
            <div class="bg-gradient-to-r from-emerald-700 to-teal-600 rounded-2xl text-white text-center px-6 py-8 sm:p-10 mt-10 mb-6 shadow-xl">
                <span class="inline-block bg-white/20 text-emerald-50 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider mb-3">5 Tests &bull; 250 MCQs</span>
                <h2 class="text-2xl sm:text-3xl font-bold tracking-tight mb-2">PMA 159 Long Course &ndash; Initial Test Practice</h2>
                <p class="text-emerald-50 text-sm sm:text-base">Built from PMA 159 test experiences. Questions marked (Repeated in N tests) were reported in several experiences. Every answer comes with a reason.</p>
            </div>
            <div id="pma-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>''')

# ---- 3. render both grids ----
sub("grid.innerHTML = Object.keys(ALL).map((k, i) => {",
    "grid.innerHTML = Object.keys(ALL).filter(k => !isPMA(k)).map((k, i) => {")
sub("function selectTest(k) {", '''function renderPMA() {
            const g = document.getElementById('pma-grid');
            g.innerHTML = Object.keys(ALL).filter(isPMA).map((k, i) => {
                let best = null; try { best = localStorage.getItem('mc_best_' + k); } catch (e) {}
                const secs = [...new Set(ALL[k].map(q => q.sec))].join(' &bull; ');
                return `<button type="button" onclick="selectTest('${k}')" class="text-left bg-white rounded-2xl border border-slate-200 hover:border-emerald-500 hover:shadow-lg transition p-5 flex flex-col gap-3">
                    <div class="flex items-center justify-between"><span class="bg-emerald-100 text-emerald-800 text-xs font-bold px-3 py-1 rounded-full">PMA Test ${i + 1}</span>${best !== null ? `<span class="text-xs font-bold text-emerald-600"><i class="fa-solid fa-trophy"></i> Best ${best}%</span>` : '<span class="text-xs text-slate-400">Not attempted</span>'}</div>
                    <div class="text-xl font-bold text-slate-900">PMA 159 &ndash; Part ${i + 1}</div>
                    <div class="text-xs text-slate-500">${secs}</div>
                    <div class="text-xs text-slate-500">${ALL[k].length} MCQs &bull; 10 Minutes &bull; Instant feedback</div>
                    <div class="text-sm font-semibold text-emerald-700">${best !== null ? 'Try again' : 'Start'} <i class="fa-solid fa-arrow-right ml-1"></i></div></button>`;
            }).join('');
        }
        function selectTest(k) {''')
sub("            renderSelect(); window.scrollTo(0, 0);\n        }\n\n        function bootQuizApp() {\n            renderSelect();",
    "            renderSelect(); renderPMA(); window.scrollTo(0, 0);\n        }\n\n        function bootQuizApp() {\n            renderSelect(); renderPMA();")

# ---- 4. selectTest: labels + per-test time ----
sub("const label = k.replace('-', '–');\n            document.getElementById('q-total').textContent = quizData.length;\n            document.getElementById('home-badge').textContent = '100 MCQs (Original Questions ' + label + ')';\n            document.getElementById('home-desc').textContent = 'Challenge yourself with 100 MCQs from original questions ' + label + '.';",
    """const label = k.replace('-', '–');
            TEST_SECS = isPMA(k) ? 600 : 1200;
            const nQ = quizData.length, nMin = TEST_SECS / 60;
            document.getElementById('q-total').textContent = nQ;
            document.getElementById('home-badge').textContent = isPMA(k) ? (nQ + ' MCQs (PMA 159 Long Course – Part ' + k.slice(4) + ')') : ('100 MCQs (Original Questions ' + label + ')');
            document.getElementById('home-desc').textContent = isPMA(k) ? ('Practice ' + nQ + ' MCQs from PMA 159 test experiences. Every answer shows a reason.') : ('Challenge yourself with 100 MCQs from original questions ' + label + '.');
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

# ---- 6. branding: Asadullah Notes Commission, Asad signature ----
import base64, os
sub('<title>Mission Commission Academy – MCQ Tests 1 to 1000</title>', '<title>Asadullah Notes Commission – MCQ Tests 1 to 1000</title>')
sub('tracking-tight">Mission Commission Academy</h1>', 'tracking-tight">Asadullah Notes Commission</h1>')
sub('This test belongs to <span class="text-indigo-600 font-bold">Mission Commission Academy</span>', 'This test belongs to <span class="text-indigo-600 font-bold">Asadullah Notes Commission</span>')
sub('Software Created by Admin Mubasher', 'Software Created by Admin Asadullah')
sub('<h1 class="ln">MISSION <span>COMMISSION</span></h1>', '<h1 class="ln">ASADULLAH NOTES <span>COMMISSION</span></h1>')
sub('This test is provided by Mission Commission for all of you.', 'This test is provided by Asadullah Notes Commission for all of you.')
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

open(out, 'w', encoding='utf8').write(s)
print("written", out, len(s))
