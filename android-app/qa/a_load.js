const L=require('./lib');const fs=require('fs');
(async()=>{const out=[];
for(const lite of [false,true])for(const rate of [1,4,6])for(let run=0;run<3;run++){
  const {b,p,cdp,errs}=await L.open({rate,lite,noWait:true});
  const t0=Date.now();await p.goto(L.URL,{waitUntil:'load'});await p.waitForTimeout(1500);
  const r=await p.evaluate(()=>{const n=performance.getEntriesByType('navigation')[0];const fcp=(performance.getEntriesByName('first-contentful-paint')[0]||{}).startTime;
    return {responseEnd:n.responseEnd,domInteractive:n.domInteractive,dcl:n.domContentLoadedEventEnd,load:n.loadEventEnd,fcp,lcp:__lcp,lt:__lt.slice(),timers:{si:__t.si,st:__t.st,al:__t.al,raf:__t.raf},transfer:performance.getEntriesByType('resource').map(e=>[e.name.split('/').slice(-2).join('/'),e.transferSize||e.encodedBodySize])}});
  const c=await L.counters(cdp);const m=await L.metrics(cdp);
  out.push({lite,rate,run,...r,...c,script:+(m.ScriptDuration*1000).toFixed(0),layout:+(m.LayoutDuration*1000).toFixed(0),style:+(m.RecalcStyleDuration*1000).toFixed(0),errs:errs.slice(0,6)});
  await b.close();}
fs.writeFileSync('res_load.json',JSON.stringify(out,null,1));
const med=a=>a.sort((x,y)=>x-y)[Math.floor(a.length/2)];
for(const lite of [false,true])for(const rate of [1,4,6]){const g=out.filter(o=>o.lite===lite&&o.rate===rate);
 console.log('lite',lite,'rate',rate,'domInt',med(g.map(o=>o.domInteractive|0)),'DCL',med(g.map(o=>o.dcl|0)),'load',med(g.map(o=>o.load|0)),'FCP',med(g.map(o=>o.fcp|0)),'LCP',med(g.map(o=>o.lcp|0)),'heap',med(g.map(o=>o.heapMB)),'nodes',g[0].nodes,'lis',g[0].listeners,'script',med(g.map(o=>o.script)),'layout',med(g.map(o=>o.layout)),'style',med(g.map(o=>o.style)),'LT',JSON.stringify(g[1].lt))}
console.log(JSON.stringify(out[0].transfer),out[0].errs, out[0].timers)})()
