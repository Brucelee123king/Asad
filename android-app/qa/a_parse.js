const L=require('./lib');const fs=require('fs');
const html=fs.readFileSync('../app/src/main/assets/www/index.html','utf8');
(async()=>{
const sizes={};for(const m of html.matchAll(/const (\w+_DATA|ALL|HK_META) = (\{[\s\S]*?\});?\n/g))sizes[m[1]]=m[2].length;console.log('data bytes',JSON.stringify(sizes));
for(const rate of [1,4,6]){const {b,p}=await L.open({rate});
const r=await p.evaluate(()=>{const s=JSON.stringify(ALL);const t=[];for(let i=0;i<5;i++){let a=performance.now();JSON.parse(s);const j=performance.now()-a;a=performance.now();new Function('return '+s)();t.push([j,performance.now()-a])}
 const q={};let tot=0,dup=0;for(const k in ALL)ALL[k].forEach(x=>{tot++;if(q[x.question])dup++;q[x.question]=1});
 return {len:s.length,jsonParse:t.map(x=>+x[0].toFixed(1)),literal:t.map(x=>+x[1].toFixed(1)),tot,dup}});
console.log('rate',rate,JSON.stringify(r));await b.close()}})()
