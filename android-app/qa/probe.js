const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:393,height:800}});
const errs=[];p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});p.on('pageerror',e=>errs.push('PE '+e.message));
await p.goto('http://127.0.0.1:8765/index.html');await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{const o={};Object.keys(ALL).forEach(k=>{const pre=k.split('-')[0];o[pre]=o[pre]||[];o[pre].push(ALL[k].length)});
 const s={};for(const k in o)s[k]={n:o[k].length,min:Math.min(...o[k]),max:Math.max(...o[k])};
 return {s,hc:navigator.hardwareConcurrency,dm:navigator.deviceMemory,lite:document.documentElement.classList.contains('lite'),keys:Object.keys(ALL).length, mem:performance.memory&&performance.memory.usedJSHeapSize}});
console.log(JSON.stringify(r),errs);await b.close()})()
