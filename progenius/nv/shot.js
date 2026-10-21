const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:760,height:360}});
for(let n=1;n<=22;n++){await p.goto('file:///home/user/Asad/progenius/nv/prev/q'+n+'.html');await p.screenshot({path:'/home/user/Asad/progenius/nv/prev/q'+n+'.png'})}
await b.close()})();
