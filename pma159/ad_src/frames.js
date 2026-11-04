const {chromium}=require('playwright');const fs=require('fs');const D=process.argv[2],L=process.argv[3],T=+process.argv[4],FPS=30;
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:1080,height:1920}})).newPage();
await p.goto('file://'+D+'/'+L+'_run2.html');await p.evaluate(async()=>{try{await document.fonts.ready}catch(e){}});await p.waitForTimeout(1500);
const out=D+'/fr_'+L;fs.rmSync(out,{recursive:true,force:true});fs.mkdirSync(out);const N=Math.ceil(T*FPS);
for(let i=0;i<N;i++){await p.evaluate(t=>window.__render(t),i/FPS);await p.screenshot({path:out+'/f'+String(i).padStart(5,'0')+'.jpg',type:'jpeg',quality:90});if(i%300===0)console.log(L,i,'/',N)}
await b.close()})();
