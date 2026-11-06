const L=require('./lib');const fs=require('fs');
const V={
 base:{},
 lite:{cls:'lite'},
 noBackdrop:{css:'*,*::before,*::after{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}'},
 noAnim:{css:'*,*::before,*::after{animation:none!important}'},
 noFilter:{css:'*,*::before,*::after{filter:none!important}'},
 noDecor:{css:'#liquidBg,#obj3d{display:none!important}'},
 noRafLoop:{reduced:true},
 allOff:{cls:'lite',css:'*,*::before,*::after{animation:none!important;backdrop-filter:none!important;-webkit-backdrop-filter:none!important;filter:none!important}#liquidBg,#obj3d{display:none!important}',reduced:true},
};
const med=a=>a.slice().sort((x,y)=>x-y)[Math.floor(a.length/2)];
(async()=>{const out={};
for(const [n,v] of Object.entries(V)){
 const {b,p,cdp}=await L.open({rate:4,reduced:!!v.reduced});
 await p.evaluate(()=>authGuest());await p.waitForTimeout(1200);
 if(v.cls)await p.evaluate(c=>document.documentElement.classList.add(c),v.cls);
 if(v.css)await p.addStyleTag({content:v.css});await p.waitForTimeout(500);
 const R={};
 const idle=async()=>{const m0=await L.metrics(cdp);const fr=await p.evaluate(()=>new Promise(r=>{let c=0,t0=performance.now(),d=[];let l=t0;const f=t=>{c++;d.push(t-l);l=t;if(t-t0<3000)requestAnimationFrame(f);else r({c,avgFrame:(t-t0)/c,max:Math.max(...d)})};requestAnimationFrame(f)}));const m1=await L.metrics(cdp);return {fps:+(fr.c/3).toFixed(1),avgFrameMs:+fr.avgFrame.toFixed(1),maxFrame:+fr.max.toFixed(0),busyPct:+(((m1.TaskDuration-m0.TaskDuration)/3)*100).toFixed(0),styleMs:+((m1.RecalcStyleDuration-m0.RecalcStyleDuration)*1000/3).toFixed(0),layoutMs:+((m1.LayoutDuration-m0.LayoutDuration)*1000/3).toFixed(0),scriptMs:+((m1.ScriptDuration-m0.ScriptDuration)*1000/3).toFixed(0)}};
 R.idleMenu=await idle();
 await p.evaluate(()=>openSec('hk'));await p.waitForTimeout(600);
 // scroll jank in HK list: wheel scroll
 await p.evaluate(()=>{window.__fr=[];let l=performance.now();const f=t=>{__fr.push(t-l);l=t;requestAnimationFrame(f)};requestAnimationFrame(f)});
 const cx=196;for(let i=0;i<10;i++){await p.mouse.wheel(0,300);await p.waitForTimeout(60)}await p.waitForTimeout(300);
 R.scroll=await p.evaluate(()=>{const a=__fr.slice(-30);return {frames:a.length,avg:+(a.reduce((s,x)=>s+x,0)/a.length).toFixed(1),max:Math.round(Math.max(...a))}});
 await p.evaluate(()=>{openSec(null);showSelect();selectTest('1-50');document.getElementById('start-quiz-btn').click()});await p.waitForTimeout(1000);
 R.idleQuiz=await idle();
 const nav=[];for(let i=0;i<8;i++){const a=await L.timeOp(p,cdp,`async()=>{selectOption(currentQuestionIndex,1);nextQuestion()}`);nav.push(a.paint);await p.waitForTimeout(100)}
 R.answerNextPaintMs=med(nav);
 out[n]=R;console.log(n.padEnd(11),JSON.stringify(R));await b.close()}
fs.writeFileSync('res_attr.json',JSON.stringify(out,null,1))})()
