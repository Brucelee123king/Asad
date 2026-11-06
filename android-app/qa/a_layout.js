const L=require('./lib');const fs=require('fs');
const SCAN=`()=>{const vw=innerWidth;const de=document.documentElement;
 const vis=e=>{const r=e.getBoundingClientRect();if(r.width===0||r.height===0)return false;const cs=getComputedStyle(e);if(cs.visibility==='hidden'||cs.display==='none')return false;let a=e;while(a&&a!==document.body){const s=getComputedStyle(a);if(s.display==='none'||s.visibility==='hidden'||+s.opacity===0)return false;a=a.parentElement}return true};
 const sel=e=>e.tagName.toLowerCase()+(e.id?'#'+e.id:'')+(e.className&&typeof e.className==='string'?'.'+e.className.trim().split(/\\s+/).slice(0,3).join('.'):'');
 const off=[];document.querySelectorAll('body *').forEach(e=>{if(!vis(e))return;if(e.closest('#liquidBg,#obj3d,[aria-hidden=true]'))return;const r=e.getBoundingClientRect();if(r.right>vw+1||r.left<-1)off.push(sel(e)+' L'+Math.round(r.left)+' R'+Math.round(r.right))});
 const tt=[];document.querySelectorAll('button,a[href],input,select,textarea,[role=button],[onclick]').forEach(e=>{if(!vis(e))return;if(e.closest('[aria-hidden=true]'))return;const r=e.getBoundingClientRect();if(Math.min(r.width,r.height)<44)tt.push([sel(e),Math.round(r.width),Math.round(r.height),(e.textContent||e.getAttribute('aria-label')||'').trim().slice(0,18)])});
 return {docOverflow:de.scrollWidth-vw,bodyOverflow:document.body.scrollWidth-vw,offCount:off.length,off:off.slice(0,6),tt:tt}}`;
(async()=>{const out={};
for(const w of [393,320,360]){const h=w===393?800:w===320?640:740;
 const {b,p,cdp,errs}=await L.open({w,h});
 const scr={};const scan=async n=>{scr[n]=await p.evaluate(eval(SCAN))};
 await p.waitForTimeout(500);await scan('login');
 await p.evaluate(()=>{const i=document.getElementById('paneUp');});
 await p.evaluate(()=>authSwitch('up'));await p.waitForTimeout(1500);await scan('signup');
 await p.evaluate(()=>authGuest());await p.waitForTimeout(1000);await scan('home');
 for(const id of ['o','pma','fa','hk','lc']){await p.evaluate(id=>openSec(id),id);await p.waitForTimeout(700);await scan('sec_'+id)}
 await p.evaluate(()=>openHkSub('all'));await p.waitForTimeout(600);await scan('hk_all');
 await p.evaluate(()=>{openHkSub(149)});await p.waitForTimeout(600);await scan('hk_149');
 await p.evaluate(()=>{openHkSub('rep')});await p.waitForTimeout(600);await scan('hk_rep');
 await p.evaluate(()=>{openHkSub(null);openSec(null)});
 // longest content
 const lk=await p.evaluate(()=>{let best=null,bl=0;for(const k in ALL)ALL[k].forEach((q,i)=>{const l=q.question.length+q.options.join('').length+(q.facts||'').length+(q.rel||'').length;if(l>bl){bl=l;best=[k,i]}});return best});
 const lw=await p.evaluate(()=>{let best=null,bl=0;for(const k in ALL)ALL[k].forEach((q,i)=>{const l=Math.max(...(q.question+' '+q.options.join(' ')).split(' ').map(s=>s.length));if(l>bl){bl=l;best=[k,i,l]}});return best});
 out.longest=lk;out.longestWord=lw;
 await p.evaluate(()=>{showSelect();selectTest('1-50')});await p.waitForTimeout(700);await scan('test_home');
 await p.evaluate(()=>{document.getElementById('start-quiz-btn').click()});await p.waitForTimeout(700);await scan('quiz');
 await p.evaluate(()=>selectOption(0,1));await p.waitForTimeout(300);await scan('quiz_answered');
 await p.evaluate(()=>confirmSubmitQuiz());await p.waitForTimeout(400);await scan('submit_modal');await p.evaluate(()=>closeSubmitModal());
 // worst-case content questions
 for(const [tag,kk] of [['quiz_longest',lk],['quiz_longestword',lw]]){
   await p.evaluate(([k,i])=>{showSelect();selectTest(k);document.getElementById('start-quiz-btn').click();quizActive=true;jumpToQuestion(i);selectOption(i,0)},[kk[0],kk[1]]);await p.waitForTimeout(600);await scan(tag);}
 await p.evaluate(()=>{executeSubmitQuiz()});await p.waitForTimeout(700);await scan('results');
 await p.evaluate(()=>{document.getElementById('review-section').scrollIntoView()});await p.waitForTimeout(500);await scan('review');
 await p.evaluate(()=>{showSelect();openSearch()});await p.waitForTimeout(500);await scan('search');
 out[w]={scr,errs};await b.close()}
fs.writeFileSync('res_layout.json',JSON.stringify(out,null,1));
for(const w of [393,320,360]){console.log('== width',w,out[w].errs.slice(0,3));for(const [n,s] of Object.entries(out[w].scr)){const sm=s.tt.length?Math.min(...s.tt.map(t=>Math.min(t[1],t[2]))):'-';console.log(n.padEnd(18),'docOvf',s.docOverflow,'bodyOvf',s.bodyOverflow,'offEls',s.offCount,s.off.slice(0,2).join(';'),'| small targets',s.tt.length,'min',sm)}}
console.log(out.longest,out.longestWord)})()
