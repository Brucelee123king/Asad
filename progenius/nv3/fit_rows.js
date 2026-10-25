// Trim the whole-row / whole-grid stem pictures (noq) to their drawn content, so they show large in the app.
// usage: node fit_rows.js <nv_final.json>
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const f=process.argv[2];const d=JSON.parse(fs.readFileSync(f,'utf8'));
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage();await p.setContent('<div id="h"></div>');let n=0;
 for(const q of d){if(!q.noq)continue;for(const g of q.stem)for(let i=0;i<g.length;i++){
   const out=await p.evaluate(s=>{const h=document.getElementById('h');h.innerHTML=s;const svg=h.querySelector('svg');svg.setAttribute('width','400');svg.setAttribute('height','400');
     const bg=svg.children[0]&&svg.children[0].tagName==='rect'?svg.children[0]:null;if(bg)bg.remove();let x0,y0,x1,y1;try{const bb=svg.getBBox();x0=bb.x;y0=bb.y;x1=bb.x+bb.width;y1=bb.y+bb.height}catch(e){return s}if(bg)svg.insertBefore(bg,svg.firstChild);
     if(x1<=x0||y1<=y0)return s;const pad=3;x0-=pad;y0-=pad;x1+=pad;y1+=pad;const w=x1-x0,hh=y1-y0;
     svg.setAttribute('viewBox',[x0,y0,w,hh].map(v=>+v.toFixed(2)).join(' '));svg.removeAttribute('width');svg.removeAttribute('height');
     const r=svg.querySelector('rect');if(r&&svg.children[0]===r){r.setAttribute('x',x0.toFixed(2));r.setAttribute('y',y0.toFixed(2));r.setAttribute('width',w.toFixed(2));r.setAttribute('height',hh.toFixed(2))}
     return svg.outerHTML},g[i]);
   if(out!==g[i]){g[i]=out;n++}}}
 fs.writeFileSync(f,JSON.stringify(d));console.log('fitted',n);await b.close()})();
