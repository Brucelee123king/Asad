const L=require('./lib');
async function run(name,keysFn,n,finish){const {b,p,cdp}=await L.open({rate:1});await p.evaluate(()=>authGuest());await p.waitForTimeout(1200);
const el=async()=>{const r=await cdp.send('Runtime.evaluate',{expression:`(()=>{let t=0;const o={};for(const [n,x] of [['document',document],['window',window],['body',document.body]]){const l=getEventListeners(x);o[n]=Object.values(l).reduce((s,a)=>s+a.length,0);}let all=0;document.querySelectorAll('*').forEach(e=>{const l=getEventListeners(e);for(const k in l)all+=l[k].length});o.elements=all;return JSON.stringify(o)})()`,includeCommandLineAPI:true});return r.result.value};
const snap=async()=>({...(await L.counters(cdp)),el:await el(),activeIntervals:await p.evaluate(()=>__t.siActive.size),intervalsCreated:await p.evaluate(()=>__t.si),hist:await p.evaluate(()=>history.length),addL:await p.evaluate(()=>__t.al),remL:await p.evaluate(()=>__t.rl)});
const keys=await p.evaluate(keysFn);
for(let i=0;i<3;i++){await p.evaluate(k=>{showSelect();selectTest(k);document.getElementById('start-quiz-btn').click()},keys[0]);} // warm-up
const s0=await snap();
for(let i=0;i<n;i++){const k=keys[i%keys.length];
 await p.evaluate(k=>{showSelect();openSec(k.startsWith('MR')?'hk':k.startsWith('HK')?'hk':'o');selectTest(k);document.getElementById('start-quiz-btn').click();nextQuestion();selectOption(currentQuestionIndex,1);nextQuestion()},k);
 if(finish)await p.evaluate(()=>{executeSubmitQuiz()});
 await p.evaluate(()=>showSelect());await p.waitForTimeout(40)}
const s1=await snap();console.log(name,'\nbefore',JSON.stringify(s0),'\nafter ',JSON.stringify(s1));await b.close()}
(async()=>{
await run('30 tests (orig 1000 section), leave via Back',()=>Object.keys(ALL).filter(k=>/^\d/.test(k)),30,false);
await run('30 tests, finish then leave',()=>Object.keys(ALL).filter(k=>/^\d/.test(k)),30,true);
await run('30 HK tests, finish then leave',()=>Object.keys(ALL).filter(k=>/^HK-/.test(k)).slice(0,30),30,true);
await run('10x biggest MR (835), finish then leave',()=>[Object.keys(ALL).filter(k=>k.startsWith('MR-')).sort((a,b)=>ALL[b].length-ALL[a].length)[0]],10,true);
})()
