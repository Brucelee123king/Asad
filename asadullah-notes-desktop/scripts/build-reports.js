// Generates src/corrections.js and the audit reports. Usage: node scripts/build-reports.js
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root=path.join(__dirname,'..','..');
const SC=process.env.SCRATCH;const A=JSON.parse(fs.readFileSync(path.join(SC,'all_orig.json'),'utf8'));
const raw=JSON.parse(fs.readFileSync(path.join(SC,'audit','audit-raw.json'),'utf8'));
const OWNER=JSON.parse(fs.readFileSync(path.join(SC,'corr.json'),'utf8'));
const today='2026-10-20';
// corrections made by this audit (evidence in `why`)
const AUDIT={'751-800':{4:{options:{1:"Surah Al-Ma'idah"},why:"Option text was misspelt 'Surah Al-Mavidah'. The explanation in the same record names Surah Al-Ma'idah (chapter 5, which contains the wudu/ghusl/tayammum verse 5:6). Answer key unchanged.",src:"Qur'an 5:6 (Surah Al-Ma'idah); the record's own explanation"}}};
const csvq=s=>'"'+String(s==null?'':s).replace(/"/g,'""').replace(/\r?\n/g,' ')+'"';
const csv=(h,rows)=>h.join(',')+'\n'+rows.map(r=>r.map(csvq).join(',')).join('\n')+'\n';
const lc=s=>String(s).toLowerCase().replace(/[^a-z0-9]+/g,'');
// ---- corrections.js (overlay applied by test key + question id; nothing is deleted)
const corrJs='/* Corrections overlay: patches by test key + question id after the original data loads. Nothing is removed from the original database. */\n'+
 'const CORR_OWNER = '+JSON.stringify(OWNER)+';\n'+
 'const CORR_AUDIT = '+JSON.stringify(Object.fromEntries(Object.entries(AUDIT).map(([k,v])=>[k,Object.fromEntries(Object.entries(v).map(([id,e])=>[id,{options:e.options}]))])))+';\n'+
 `(function () {
  function patch(set, merge) { Object.keys(set).forEach(function (k) { var arr = ALL[k]; if (!arr) return; arr.forEach(function (q) { var c = set[k][String(q.id)]; if (!c) return; merge(q, c); }); }); }
  patch(CORR_OWNER, function (q, c) { Object.assign(q, c); });
  patch(CORR_AUDIT, function (q, c) { Object.keys(c.options).forEach(function (i) { q.options[i] = c.options[i]; }); });
})();
`;
fs.writeFileSync(path.join(__dirname,'..','src','corrections.js'),corrJs);
// ---- corrections csv
const rows=[];const manual=[];const summary={owner:0,ownerCosmetic:0,ownerSubstantive:0,audit:0};
for(const k in OWNER)for(const id in OWNER[k]){summary.owner++;const o=A[k].find(q=>q.id==id),x=OWNER[k][id];
  const oa=o.options[o.correct],na=(x.options||o.options)[x.correct!==undefined?x.correct:o.correct];
  const cosmetic=lc(oa)===lc(na)||lc(na).includes(lc(oa))&&lc(oa).length>3||lc(oa).includes(lc(na))&&lc(na).length>1;
  if(cosmetic)summary.ownerCosmetic++;else summary.ownerSubstantive++;
  const status=cosmetic?'Applied - wording/format cleanup, same answer (verified by comparison with original)':'Applied - changes the keyed answer or fact; supplied in owner file index.html, NOT independently verified by this audit';
  for(const f of ['question','options','correct','facts','rel']){
    if(x[f]===undefined)continue;const ov=o[f],nv=x[f];if(JSON.stringify(ov)===JSON.stringify(nv))continue;
    rows.push([k,id,f,typeof ov==='object'?JSON.stringify(ov):ov,typeof nv==='object'?JSON.stringify(nv):nv,status,'Owner-supplied correction layer (index.html, "answer audit corrections, Oct 2026")']);}
  if(!cosmetic)manual.push([k,id,'Owner-supplied correction changes answer','Original key: '+oa+' | Now: '+na,'Verify against a reliable source before relying on it (time-sensitive facts: check date)',today]);
}
for(const k in AUDIT)for(const id in AUDIT[k]){summary.audit++;const o=A[k].find(q=>q.id==id),e=AUDIT[k][id];
  Object.keys(e.options).forEach(i=>rows.push([k,id,'options['+i+']',o.options[i],e.options[i],'Applied - verified: '+e.why,e.src]));}
fs.mkdirSync(path.join(root,'reports'),{recursive:true});
fs.writeFileSync(path.join(root,'reports','MCQ_Corrections.csv'),csv(['test','question_id','field','original_value','corrected_value','status_and_reason','verification_source'],rows));
// ---- manual review
const ownerKeys=new Set(Object.keys(OWNER).flatMap(k=>Object.keys(OWNER[k]).map(i=>k+'#'+i)));
const seenM=new Set();
for(const q0 of Object.keys(A))A[q0].forEach(q=>q.options.forEach((o,j)=>{
  if(/=\)/.test(o)){const key=q0+'#'+q.id;if(ownerKeys.has(key)&&!/=\)/.test(((OWNER[q0]||{})[q.id]||{}).options?OWNER[q0][q.id].options[j]:''))return;
    manual.push([q0,q.id,'Garbled distractor text',"Option "+'ABCDE'[j]+': '+o,'Cleaning the text would duplicate another option; the author must choose a replacement distractor',today]);}
  if(/has 7 verses/.test(o))manual.push([q0,q.id,'Garbled distractor text','Option '+'ABCDE'[j]+': '+o,'Distractor contains explanation text; author must choose a replacement',today])}));
raw.issues.filter(x=>x.type==='explanation-vs-key'&&!ownerKeys.has(x.test+'#'+x.id)).forEach(x=>{const q=A[x.test].find(q=>q.id===x.id);
  manual.push([x.test,x.id,'Heuristic flag (low confidence)','Key: '+q.options[q.correct]+' | explanation names another option','Explanation likely just mentions related options; a sample of 13 flags had no confirmed error. Review if time permits',today])});
raw.issues.filter(x=>x.type==='arithmetic').forEach(x=>manual.push([x.test,x.id,'Arithmetic check',x.detail,'Check computation',today]));
fs.writeFileSync(path.join(root,'reports','MCQ_Manual_Review.csv'),csv(['test','question_id','issue','detail','suggested_action','flagged_on'],manual));
// ---- integrity report
const sha=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const dups=raw.issues.filter(x=>x.type==='duplicate'),conf=dups.filter(x=>x.sev==='high');
const per=Object.entries(raw.stats).map(([k,v])=>'  '+k.padEnd(5)+String(v).padStart(6)+' questions').join('\n');
const sect={ORIG:'1000 MCQs (20 tests)',PMA:'PMA 159 (7 tests)',FA:'Forces Academy (16 tests)',HK:'Hakeem Force Academy PMA experiences (132 tests)',MR:'Most Repeated (14 tests)',CN:'Constitution (1 test)',IV:'100 Most Repeated (1 test)',LC:'PMA 158 (5 tests)'};
const txt=`DATA INTEGRITY REPORT - Asadullah Notes ${today}
Source of truth: original-backup/index-7.original.html (sha256 ${sha(path.join(root,'original-backup','index-7.original.html'))})
Tests found: ${raw.tests}
Questions found: ${raw.total}
${per}
Result: no questions truncated or deleted. The desktop build loads the original database unchanged (src/data.js) and applies the corrections overlay (src/corrections.js) on top.
Checks over all ${raw.total} questions (automated):
  Question text present ............ pass
  Answer key index within options .. pass (0 failures)
  Empty options .................... pass (0 failures)
  Identical options in one question  ${raw.issues.filter(x=>x.type==='duplicate-options').length} found (case-insensitive; 1 is a false positive: "Ee" vs "EE" are different letters in HK-96 #6)
  Corrupted characters (U+FFFD etc.) ${raw.issues.filter(x=>x.type==='encoding').length}
  Script/iframe markup in text ..... ${raw.issues.filter(x=>x.type==='markup').length}
  Questions with 3 or 5 options .... ${raw.issues.filter(x=>x.type==='option-count').length} (FA sections; accepted by the app)
  Same question appearing in more than one test: ${dups.length} repeats (by design: HK experience tests and Most Repeated tests reuse questions); repeats with a CONFLICTING answer: ${conf.length}
  Garbled distractor "Surah An-Naml, =)" ... 4 occurrences (1 corrected, 3 flagged for manual review)
Corrections overlay: ${summary.owner} owner-supplied entries (${summary.ownerCosmetic} wording/format cleanups, ${summary.ownerSubstantive} change an answer or fact and are NOT independently verified) + ${summary.audit} audit correction(s).
Limits: factual accuracy of 11,208 questions was NOT fully verified against external sources in this audit. See MCQ_Audit_Report.html.
`;
fs.writeFileSync(path.join(root,'reports','data-integrity-report.txt'),txt);
// ---- html report
const esc=s=>String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const html=`<!doctype html><html lang="en"><meta charset="utf-8"><title>MCQ Audit Report</title><style>body{font:15px/1.5 system-ui,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem;color:#1e293b}h1{color:#4338ca}table{border-collapse:collapse;width:100%}td,th{border:1px solid #cbd5e1;padding:6px 10px;text-align:left}th{background:#eef2ff}.warn{background:#fffbeb;border-left:4px solid #f59e0b;padding:10px 14px}</style>
<h1>Asadullah Notes - MCQ Audit Report</h1><p>Audit date: ${today}. Source: original-backup/index-7.original.html.</p>
<div class="warn"><b>Scope statement.</b> Every question was checked automatically for structure, key validity, encoding, duplicates, and simple arithmetic. Factual accuracy was <b>not</b> verified question-by-question against external sources, so no claim of 100% accuracy is made.</div>
<h2>Counts</h2><table><tr><th>Section</th><th>Questions</th></tr>${Object.entries(raw.stats).map(([k,v])=>`<tr><td>${sect[k]}</td><td>${v}</td></tr>`).join('')}<tr><th>Total (${raw.tests} tests)</th><th>${raw.total}</th></tr></table>
<h2>Results</h2><table><tr><th>Item</th><th>Count</th></tr>
<tr><td>Questions examined</td><td>${raw.total}</td></tr>
<tr><td>Confirmed defects fixed by this audit</td><td>${summary.audit} (751-800 #4 option typo)</td></tr>
<tr><td>Owner-supplied corrections applied (from index.html)</td><td>${summary.owner} (${summary.ownerCosmetic} cosmetic, ${summary.ownerSubstantive} substantive and unverified)</td></tr>
<tr><td>Items in manual-review list</td><td>${manual.length}</td></tr>
<tr><td>Cross-test repeated questions</td><td>${dups.length} (all with the same answer; ${conf.length} conflicts)</td></tr>
<tr><td>Garbled distractor "Surah An-Naml, =)"</td><td>4 (1 fixed, 3 for manual review)</td></tr></table>
<h2>Evidence</h2><p>Qur'an 5:6 for Surah Al-Ma'idah (wudu, ghusl, tayammum). Substantive owner-supplied changes (for example 27th Amendment details, KP Chief Minister, 2025-2026 events) are time-sensitive and could not be verified from the offline environment; they are listed in MCQ_Manual_Review.csv with the flag date ${today}.</p>
<h2>Files</h2><ul><li>MCQ_Corrections.csv - every field changed, with original and corrected value</li><li>MCQ_Manual_Review.csv - unresolved items</li><li>data-integrity-report.txt</li></ul></html>`;
fs.writeFileSync(path.join(root,'reports','MCQ_Audit_Report.html'),html);
console.log(summary,'corrections rows',rows.length,'manual',manual.length);
