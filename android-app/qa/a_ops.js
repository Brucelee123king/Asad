const L=require('./lib');const fs=require('fs');
const rate=+process.argv[2]||4, lite=process.argv[3]==='lite';
(async()=>{const {b,p,cdp,errs}=await L.open({rate,lite});const R={rate,lite,sections:{},hk:{},render:{},tests:{}};
await p.evaluate(()=>authGuest());await p.waitForTimeout(1200);
R.menuNodes=await L.nodes(p);R.menuVisNodes=await L.vnodes(p);
// individual renderers
for(const f of ['renderSelect','renderPMA','renderFA','renderHK','renderLC','renderMenu','applySec','showSelect'])
  R.render[f]=await L.timeOp(p,cdp,`async()=>{${f}()}`);
// sections
for(const id of ['o','pma','fa','hk','lc']){
  const o=await L.timeOp(p,cdp,`async()=>{openSec('${id}')}`);o.vis=await L.vnodes(p);o.nodes=await L.nodes(p);R.sections[id]=o;
  await p.evaluate(()=>openSec(null));await p.waitForTimeout(400)}
await p.evaluate(()=>openSec('hk'));await p.waitForTimeout(500);
for(const s of ["'all'","'rep'","'con'","'imp'","149","157"]){const o=await L.timeOp(p,cdp,`async()=>{openHkSub(${s})}`);o.vis=await L.vnodes(p);R.hk[s]=o;await p.waitForTimeout(300)}
await p.evaluate(()=>{openHkSub(null);openSec(null)});await p.waitForTimeout(400);
// tests
const picks={'o 1-50':'1-50','PMA-1':'PMA-1','FA-1':'FA-1','HK-1':'HK-1','LC-1':'LC-1','CN-1(89)':'CN-1','IV-1(107)':'IV-1','MR biggest':null};
const keys=await p.evaluate(()=>Object.keys(ALL));
picks['MR biggest']=await p.evaluate(()=>Object.keys(ALL).filter(k=>k.startsWith('MR-')).sort((a,b)=>ALL[b].length-ALL[a].length)[0]);
for(const [name,k] of Object.entries(picks)){
  const T={key:k,n:await p.evaluate(k=>ALL[k].length,k)};
  await p.evaluate(()=>{showSelect()});await p.waitForTimeout(300);
  T.selectTest=await L.timeOp(p,cdp,`async()=>{selectTest('${k}')}`);T.homeNodes=await L.nodes(p);
  T.renderPalette=await L.timeOp(p,cdp,`async()=>{renderPalette()}`);
  const t0=Date.now();T.start=await L.timeOp(p,cdp,`async()=>{document.getElementById('start-quiz-btn').click()}`);T.quizNodes=await L.nodes(p);T.quizVis=await L.vnodes(p);
  // answer + navigate
  const nav=[];const N=Math.min(T.n-1,12);
  for(let i=0;i<N;i++){
    const a=await L.timeOp(p,cdp,`async()=>{selectOption(currentQuestionIndex,1)}`);
    const n=await L.timeOp(p,cdp,`async()=>{nextQuestion()}`);nav.push({ans:a.sync,ansPaint:a.paint,nextSync:n.sync,nextPaint:n.paint,lt:n.lt.length+a.lt.length,style:n.m.RecalcStyleDuration+a.m.RecalcStyleDuration,layout:n.m.LayoutDuration+a.m.LayoutDuration});await p.waitForTimeout(80)}
  const avg=f=>+(nav.reduce((s,x)=>s+x[f],0)/nav.length).toFixed(1);
  T.nav={ansSync:avg('ans'),ansPaint:avg('ansPaint'),nextSync:avg('nextSync'),nextPaint:avg('nextPaint'),styleMs:avg('style'),layoutMs:avg('layout'),longtasks:nav.reduce((s,x)=>s+x.lt,0)};
  T.updatePalette=await L.timeOp(p,cdp,`async()=>{updatePaletteUI()}`);
  T.loadQ=await L.timeOp(p,cdp,`async()=>{loadQuestion(currentQuestionIndex)}`);
  T.jump=await L.timeOp(p,cdp,`async()=>{jumpToQuestion(${Math.max(0,T.n-1)})}`);
  // answer all quickly then submit
  await p.evaluate(()=>{for(let i=0;i<quizData.length;i++){userAnswers[i]=i%3===0?quizData[i].correct:(quizData[i].correct+1)%quizData[i].options.length}});
  T.submit=await L.timeOp(p,cdp,`async()=>{executeSubmitQuiz()}`);T.resNodes=await L.nodes(p);T.resVis=await L.vnodes(p);
  T.reviewIncorrect=await L.timeOp(p,cdp,`async()=>{filterReview('incorrect')}`);
  T.reviewAll=await L.timeOp(p,cdp,`async()=>{filterReview('all')}`);
  T.restart=await L.timeOp(p,cdp,`async()=>{restartQuiz()}`);
  T.back=await L.timeOp(p,cdp,`async()=>{showSelect()}`);
  R.tests[name]=T;console.error(name,'done',T.selectTest.sync,T.start.sync,T.nav.nextSync)}
R.errs=errs;fs.writeFileSync(`res_ops_${rate}${lite?'_lite':''}.json`,JSON.stringify(R,null,1));
const s=(o)=>o&&`${o.sync}/${o.paint}ms lt${o.lt.length}`;
console.log('RENDER',Object.entries(R.render).map(([k,v])=>k+':'+s(v)).join(' | '));
console.log('SEC',Object.entries(R.sections).map(([k,v])=>k+':'+s(v)+' vis'+v.vis).join(' | '));
console.log('HK',Object.entries(R.hk).map(([k,v])=>k+':'+s(v)+' vis'+v.vis).join(' | '));
for(const [k,t] of Object.entries(R.tests))console.log(k,t.n,'sel',s(t.selectTest),'pal',s(t.renderPalette),'start',s(t.start),'nav',JSON.stringify(t.nav),'updPal',s(t.updatePalette),'loadQ',s(t.loadQ),'submit',s(t.submit),'revInc',s(t.reviewIncorrect),'revAll',s(t.reviewAll),'back',s(t.back),'nodes h/q/r',t.homeNodes,t.quizNodes,t.resNodes);
console.log(errs);await b.close()})()
