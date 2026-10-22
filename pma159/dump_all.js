// usage: node dump_all.js <plain.html> <out.json>   (dumps ALL without custom tests)
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage();
await p.goto('file://'+require('path').resolve(process.argv[2]));await p.waitForTimeout(1500);
const d=await p.evaluate(()=>{const o={};Object.keys(ALL).forEach(k=>{if(k.indexOf('CUS-')===0)return;o[k]=ALL[k]});return o});
fs.writeFileSync(process.argv[3],JSON.stringify(d));console.log(Object.keys(d).length,'tests');await b.close()})();
