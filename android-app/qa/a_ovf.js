const L=require('./lib');
(async()=>{for(const w of [320,360]){const {b,p}=await L.open({w,h:w===320?640:740});await p.evaluate(()=>authGuest());await p.waitForTimeout(1500);
const f=async n=>console.log(w,n,JSON.stringify(await p.evaluate(()=>{const vw=innerWidth,o=[];document.querySelectorAll('body *').forEach(e=>{if(e.closest('#auth,#liquidBg,#obj3d,#srchModal'))return;const r=e.getBoundingClientRect();if(r.width&&r.right>vw+1&&getComputedStyle(e).position!=='fixed')o.push(e.tagName+'#'+e.id+'.'+String(e.className).slice(0,40)+' w'+Math.round(r.width)+' R'+Math.round(r.right))});return {doc:document.documentElement.scrollWidth-vw,o:o.slice(0,8)}})));
await f('home');
await p.evaluate(()=>{showSelect();selectTest('1-50');document.getElementById('start-quiz-btn').click()});await p.waitForTimeout(800);await f('quiz');
await p.evaluate(()=>{executeSubmitQuiz()});await p.waitForTimeout(800);await f('results');await b.close()}})()
