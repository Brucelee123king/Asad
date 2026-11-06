const L=require('./lib');const fs=require('fs');
const html=fs.readFileSync('../app/src/main/assets/www/index.html','utf8');
const styles=[...html.matchAll(/<style[^>]*>[\s\S]*?<\/style>/g)].map(m=>[m.index,m[0].length]);
const variants={base:h=>h,
 noAuthCss:h=>h.replace(/<style[^>]*>\s*#auth\{--tx[\s\S]*?<\/style>/,''),
 noGlass:h=>h.replace(/<style[^>]*>\s*\/\* ======== LIQUID GLASS[\s\S]*?<\/style>/,''),
 no3d:h=>h.replace(/<style[^>]*>\s*\/\* ======== 3D MIX[\s\S]*?<\/style>/,''),
 noPolish:h=>h.replace(/<style[^>]*>\s*\/\* -+ premium[\s\S]*?<\/style>/,''),
 noTailwind:h=>h.replace('<link rel="stylesheet" href="css/tailwind.css">',''),
 noFA:h=>h.replace('<link rel="stylesheet" href="css/fontawesome.css">',''),
 noAllInlineCss:h=>h.replace(/<style[^>]*>[\s\S]*?<\/style>/g,''),
 noObj3d:h=>h.replace(/<div id="obj3d"[\s\S]*?<\/div>\s*(?=<script|<style|<\/body)/,''),
};
(async()=>{for(const [n,f] of Object.entries(variants)){const r=[];
 for(let i=0;i<3;i++){const {b,p,cdp}=await L.open({rate:4,noWait:true});
  await p.route('**/index.html',route=>route.fulfill({body:f(html),contentType:'text/html'}));
  await p.goto(L.URL,{waitUntil:'load'});await p.waitForTimeout(1200);const m=await L.metrics(cdp);
  r.push([+(m.RecalcStyleDuration*1000).toFixed(0),m.RecalcStyleCount,+(m.LayoutDuration*1000).toFixed(0),+(m.TaskDuration*1000).toFixed(0)]);await b.close()}
 r.sort((a,b)=>a[0]-b[0]);console.log(n,'median style ms/count/layout/task',JSON.stringify(r[1]),await 0)}})()
