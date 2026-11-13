const L=require('./lib');
(async()=>{for(const v of ['base','killLoop']){const {b,p,cdp}=await L.open({rate:4,noWait:true});
if(v==='killLoop')await p.addInitScript(()=>{const r=window.requestAnimationFrame;window.requestAnimationFrame=function(f){if(String(f).includes('--gx'))return 0;return r.call(window,f)}});
await p.goto(L.URL);await p.waitForTimeout(800);await p.evaluate(()=>authGuest());await p.waitForTimeout(1200);
const m0=await L.metrics(cdp);const fr=await p.evaluate(()=>new Promise(r=>{let c=0,t0=performance.now();const f=t=>{c++;if(t-t0<3000)requestAnimationFrame(f);else r(c/3)};requestAnimationFrame(f)}));const m1=await L.metrics(cdp);
const nav=[];await p.evaluate(()=>{selectTest('1-50');document.getElementById('start-quiz-btn').click()});await p.waitForTimeout(800);
for(let i=0;i<8;i++){const a=await L.timeOp(p,cdp,`async()=>{selectOption(currentQuestionIndex,1);nextQuestion()}`);nav.push(a.paint);await p.waitForTimeout(100)}
console.log(v,'menu fps',fr.toFixed(1),'busy%',((m1.TaskDuration-m0.TaskDuration)/3*100).toFixed(0),'style ms/s',((m1.RecalcStyleDuration-m0.RecalcStyleDuration)*1000/3).toFixed(0),'ans+next paint',nav.sort((a,b)=>a-b)[4]);await b.close()}})()
