const {chromium}=require('playwright');
const URL='http://127.0.0.1:8765/index.html';
const INIT=`(()=>{
 const lite=${'__LITE__'};
 try{Object.defineProperty(navigator,'hardwareConcurrency',{get:()=>lite?4:8});Object.defineProperty(navigator,'deviceMemory',{get:()=>lite?2:6});}catch(e){}
 window.__t={si:0,sc:0,siActive:new Set(),st:0,al:0,rl:0,raf:0};
 const _si=window.setInterval,_ci=window.clearInterval;
 window.setInterval=function(f,t){const id=_si.apply(this,arguments);__t.si++;__t.siActive.add(id);return id};
 window.clearInterval=function(id){__t.siActive.delete(id);return _ci.apply(this,arguments)};
 const _st=window.setTimeout;window.setTimeout=function(){__t.st++;return _st.apply(this,arguments)};
 const _ae=EventTarget.prototype.addEventListener,_re=EventTarget.prototype.removeEventListener;
 EventTarget.prototype.addEventListener=function(){__t.al++;return _ae.apply(this,arguments)};
 EventTarget.prototype.removeEventListener=function(){__t.rl++;return _re.apply(this,arguments)};
 const _raf=window.requestAnimationFrame;window.requestAnimationFrame=function(){__t.raf++;return _raf.apply(this,arguments)};
 window.__lt=[];try{new PerformanceObserver(l=>{for(const e of l.getEntries())__lt.push([Math.round(e.startTime),Math.round(e.duration)])}).observe({type:'longtask',buffered:true})}catch(e){}
 window.__lcp=0;try{new PerformanceObserver(l=>{for(const e of l.getEntries())__lcp=e.startTime}).observe({type:'largest-contentful-paint',buffered:true})}catch(e){}
})();`;
async function open({w=393,h=800,rate=1,lite=false,noWait=false,reduced=false}={}){
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--enable-precise-memory-info','--js-flags=--expose-gc']});
  const ctx=await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2.75,isMobile:true,hasTouch:true,reducedMotion:reduced?'reduce':'no-preference'});
  const p=await ctx.newPage();
  const errs=[];p.on('console',m=>{if(m.type()==='error'||m.type()==='warning')errs.push(m.type()+': '+m.text()+' @'+(m.location().url||'').split('/').pop())});
  p.on('pageerror',e=>errs.push('PAGEERROR '+e.message));
  p.on('requestfailed',r=>errs.push('REQFAIL '+r.url()));
  p.on('response',r=>{if(r.status()>=400)errs.push('HTTP'+r.status()+' '+r.url())});
  p.on('dialog',d=>d.accept());
  await p.addInitScript(INIT.replace('__LITE__',String(lite)));
  const cdp=await ctx.newCDPSession(p);
  await cdp.send('Performance.enable');
  if(rate>1)await cdp.send('Emulation.setCPUThrottlingRate',{rate});
  if(!noWait){await p.goto(URL,{waitUntil:'load'});await p.waitForTimeout(800)}
  return {b,ctx,p,cdp,errs};
}
async function metrics(cdp){const m=(await cdp.send('Performance.getMetrics')).metrics;const o={};m.forEach(x=>o[x.name]=x.value);return o}
function diff(a,b){const o={};for(const k of['TaskDuration','ScriptDuration','LayoutDuration','RecalcStyleDuration','LayoutCount','RecalcStyleCount'])o[k]=+((b[k]-a[k])*(/Duration/.test(k)?1000:1)).toFixed(1);return o}
// time an in-page op: sync time + time to next painted frame (rAF+rAF)
async function timeOp(p,cdp,fnSrc,arg){
  const m0=await metrics(cdp);
  const r=await p.evaluate(async([src,arg])=>{const f=eval('('+src+')');const t0=performance.now();const lt0=__lt.length;await f(arg);const t1=performance.now();
    await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));const t2=performance.now();return {sync:t1-t0,paint:t2-t0,lt:__lt.slice(lt0)}},[fnSrc,arg]);
  const m1=await metrics(cdp);r.m=diff(m0,m1);r.sync=+r.sync.toFixed(1);r.paint=+r.paint.toFixed(1);return r}
async function counters(cdp){await cdp.send('HeapProfiler.collectGarbage');await cdp.send('HeapProfiler.collectGarbage');const c=await cdp.send('Memory.getDOMCounters');const m=await metrics(cdp);return {nodes:c.nodes,listeners:c.jsEventListeners,docs:c.documents,heapMB:+(m.JSHeapUsedSize/1048576).toFixed(2),heapTotMB:+(m.JSHeapTotalSize/1048576).toFixed(2)}}
const nodes=p=>p.evaluate(()=>document.getElementsByTagName('*').length);
const vnodes=p=>p.evaluate(()=>{let n=0;document.querySelectorAll('body *').forEach(e=>{if(e.offsetParent!==null||getComputedStyle(e).position==='fixed')n++});return n});
module.exports={open,metrics,diff,timeOp,counters,nodes,vnodes,URL};
