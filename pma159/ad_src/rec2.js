const {chromium}=require('playwright');const D=process.argv[2],L=process.argv[3],T=+process.argv[4];
(async()=>{const b=await chromium.launch();const c=await b.newContext({viewport:{width:1080,height:1920},recordVideo:{dir:D+'/vid_'+L,size:{width:1080,height:1920}}});
const t0=Date.now();const p=await c.newPage();await p.goto('file://'+D+'/'+L+'_run.html');await p.evaluate(async()=>{try{await document.fonts.ready}catch(e){}});await p.waitForTimeout(2500);
const lead=(Date.now()-t0)/1000;await p.evaluate(()=>window.__play());await p.waitForTimeout(T*1000+800);await c.close();await b.close();require('fs').writeFileSync(D+'/lead_'+L+'.txt',String(lead))})();
