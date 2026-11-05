// Measures how long every block of on-screen text stays readable. usage: node dwell.js page.html duration
const {chromium}=require('playwright');const path=require('path');
(async()=>{const [file,q]=[process.argv[2],process.argv[3]||''];const step=0.05;
const br=await chromium.launch();const p=await br.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.resolve(file)+(q?'?'+q:''));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
const dur=await p.evaluate(()=>typeof T_FIN!=='undefined'?T_FIN:(typeof DUR!=='undefined'?DUR:20));const seen={};
for(let t=0;t<=dur;t+=step){
 await p.evaluate(t=>seek(t),t);
 const vis=await p.evaluate(()=>{const out=[];const BLK=/^(DIV|P|H1|H2|H3|LI|SECTION|BODY)$/;
  for(const el of document.querySelectorAll('div,p,h1,h2,span')){
   if(el.tagName==='SPAN'&&el.parentElement&&![...el.parentElement.children].some(c=>BLK.test(c.tagName))&&el.parentElement.innerText.trim()) continue; // spans inside a text block
   if([...el.children].some(c=>BLK.test(c.tagName))) continue;
   const tx=el.innerText.replace(/\s+/g,' ').trim(); if(!tx||tx.length<2) continue;
   let o=1,n=el,ok=true;while(n&&n.nodeType===1){const cs=getComputedStyle(n);if(cs.visibility==='hidden'||cs.display==='none'){ok=false;break;}o*=+cs.opacity;n=n.parentElement;}
   if(!ok||o<0.6) continue; const r=el.getBoundingClientRect(); if(r.width<4||r.bottom<0||r.top>1920||r.right<0||r.left>1080) continue;
   // dim words (unlit #3B4445) are not readable yet
   const cs=getComputedStyle(el); if(cs.color==='rgb(59, 68, 69)') continue;
   out.push(tx);} return [...new Set(out)];});
 for(const tx of vis){(seen[tx]=seen[tx]||[]).push(+t.toFixed(2));}
}
await br.close();
const rows=[];for(const [tx,ts] of Object.entries(seen)){
 // longest continuous run
 let best=0,cur=0,start=ts[0],bs=ts[0];for(let i=0;i<ts.length;i++){if(i&&ts[i]-ts[i-1]>step*1.5){cur=0;start=ts[i];}cur=ts[i]-start+step;if(cur>best){best=cur;bs=start;}}
 const words=tx.split(' ').length;const need=Math.max(1.0,0.5+words*0.3);rows.push({tx,words,dwell:+best.toFixed(2),from:bs,need:+need.toFixed(2),ok:best>=need});}
rows.sort((a,b)=>a.from-b.from);
console.log(JSON.stringify({dur,rows}));})();
