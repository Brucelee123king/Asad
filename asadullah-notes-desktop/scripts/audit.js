// Structural + automated checks over every question. Usage: node scripts/audit.js <all.json> <outdir>
const fs=require('fs'),path=require('path');
const ALL=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));const out=process.argv[3];
const issues=[];const add=(t,i,sev,type,detail)=>issues.push({test:t,id:i,sev,type,detail});
const norm=s=>String(s).toLowerCase().replace(/\(\d+\)|\(repeated in \d+ tests?\)|\(original mcq #\d+\)/g,'').replace(/[^a-z0-9]+/g,' ').trim();
const seen=new Map();let total=0,tests=0;const stats={};
for(const [k,arr] of Object.entries(ALL)){tests++;
  arr.forEach((q,ix)=>{total++;const id=q.id;
    const P=k.replace(/[-\d]+$/,'')||'ORIG';stats[P]=(stats[P]||0)+1;
    if(typeof q.question!=='string'||!q.question.trim())add(k,id,'high','missing-question','empty question');
    if(!Array.isArray(q.options)||q.options.length<2)add(k,id,'high','missing-options','fewer than 2 options');
    else{
      if(q.options.length!==4)add(k,id,'low','option-count',q.options.length+' options');
      const ns=q.options.map(o=>String(o).toLowerCase().replace(/\s+/g,' ').trim());
      if(new Set(ns).size!==ns.length)add(k,id,'high','duplicate-options','two options are identical: '+JSON.stringify(q.options));
      q.options.forEach((o,j)=>{if(typeof o!=='string'||!o.trim())add(k,id,'high','empty-option','option '+j+' empty')});
    }
    if(!Number.isInteger(q.correct)||q.correct<0||!q.options||q.correct>=q.options.length)add(k,id,'high','bad-answer-key','correct='+q.correct);
    const txt=[q.question,...(q.options||[]),q.facts||'',q.rel||''].join(' ');
    if(/�|â€|Ã[\u0080-¿]|\?\?\?\?/.test(txt))add(k,id,'high','encoding','corrupted characters');
    if(/<\/?(script|iframe)/i.test(txt))add(k,id,'high','markup','script/iframe in text');
    if(q.pma&&!q.facts)add(k,id,'med','missing-explanation','no explanation on a question that expects one');
    // explanation mentions a different option as the answer
    if(q.facts&&Array.isArray(q.options)&&Number.isInteger(q.correct)&&q.options[q.correct]!=null){
      const f=norm(q.facts),c=norm(q.options[q.correct]);
      const others=q.options.map(norm).filter((o,j)=>j!==q.correct&&o.length>3&&f.includes(o)&&!c.includes(o)&&!o.includes(c));
      if(others.length&&!(c.length>2&&f.includes(c)))add(k,id,'med','explanation-vs-key','explanation names a different option but not the keyed one (review)');
    }
    // simple arithmetic: "What is X% of Y?"
    let m=/what is (\d+(?:\.\d+)?)% of (\d+(?:\.\d+)?)\??/i.exec(q.question);
    if(m&&Array.isArray(q.options)){const v=+m[1]*+m[2]/100;const ok=q.options.findIndex(o=>Math.abs(parseFloat(String(o).replace(/,/g,''))-v)<1e-9);
      if(ok>=0&&ok!==q.correct)add(k,id,'high','arithmetic','computed '+v+' is option '+ok+' but key is '+q.correct);
      if(ok<0)add(k,id,'med','arithmetic','computed '+v+' not among options');}
    const key=norm(q.question)+'|'+(q.options||[]).map(norm).sort().join('|');
    const keyQ=norm(q.question);
    if(seen.has(key)){const p=seen.get(key);const pa=ALL[p.t].find(x=>x.id===p.i);
      const a=(q.options||[])[q.correct],b=(pa.options||[])[pa.correct];
      add(k,id,norm(a)===norm(b)?'info':'high','duplicate',(norm(a)===norm(b)?'same':'CONFLICTING answer vs ')+' '+p.t+'#'+p.i+' ('+JSON.stringify(a)+' vs '+JSON.stringify(b)+')');}
    else seen.set(key,{t:k,i:id});
  });}
fs.mkdirSync(out,{recursive:true});
fs.writeFileSync(path.join(out,'audit-raw.json'),JSON.stringify({tests,total,stats,issues}));
const by={};issues.forEach(x=>{const kk=x.type+'/'+x.sev;by[kk]=(by[kk]||0)+1});
console.log({tests,total,stats,by});
