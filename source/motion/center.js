const {chromium}=require('playwright');const path=require('path');
(async()=>{const [file,...ts]=process.argv.slice(2);const br=await chromium.launch();const p=await br.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.resolve(file));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
const seen=new Map();
for(const t of ts){await p.evaluate(t=>seek(+t),t);
 const r=await p.evaluate(()=>{const out=[];
  const vis=e=>{let x=e;while(x&&x!==document.body){const s=getComputedStyle(x);if(s.visibility==='hidden'||s.display==='none'||+s.opacity<0.6)return false;x=x.parentElement}return true};
  for(const e of document.querySelectorAll('body *')){
   if(e.tagName==='svg'||e.closest('svg'))continue;const s=getComputedStyle(e);
   const hasBox=(parseFloat(s.borderTopWidth)>0&&s.borderTopStyle!=='none'&&!/rgba\(.*, 0\)/.test(s.borderTopColor))||(s.backgroundColor!=='rgba(0, 0, 0, 0)'&&s.backgroundColor!=='transparent')||s.backgroundImage!=='none';
   if(!hasBox)continue;const txt=(e.innerText||'').trim();if(!txt||txt.length>60)continue;
   const b=e.getBoundingClientRect();if(b.width<40||b.height<24||b.height>260||b.width>1000)continue;
   if(b.right<0||b.left>1080||b.bottom<0||b.top>1920||!vis(e))continue;
   const tv=[e,...e.querySelectorAll('*')].filter(c=>[...c.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()));
   if(tv.length&&tv.every(c=>+getComputedStyle(c).opacity<0.6))continue;
   const rg=document.createRange();rg.selectNodeContents(e);const rs=[...rg.getClientRects()].filter(q=>q.width>0&&q.height>0);
   let L=1e9,R=-1e9,T=1e9,B=-1e9;for(const q of rs){L=Math.min(L,q.left);R=Math.max(R,q.right);T=Math.min(T,q.top);B=Math.max(B,q.bottom)}
   for(const c of e.querySelectorAll('*')){const cb=c.getBoundingClientRect();if(cb.width>0&&cb.height>0&&cb.width<b.width*0.9){L=Math.min(L,cb.left);R=Math.max(R,cb.right);T=Math.min(T,cb.top);B=Math.max(B,cb.bottom)}}
   if(L>R)continue;
   const bl=parseFloat(s.borderLeftWidth)||0,brr=parseFloat(s.borderRightWidth)||0,bt=parseFloat(s.borderTopWidth)||0,bb=parseFloat(s.borderBottomWidth)||0;
   const ix=b.left+bl,iw=b.width-bl-brr,iy=b.top+bt,ih=b.height-bt-bb;
   const dx=((L+R)/2)-(ix+iw/2),dy=((T+B)/2)-(iy+ih/2),padL=L-ix,padR=(ix+iw)-R;
   const clipped=L<ix-1||R>ix+iw+1||T<iy-1||B>iy+ih+1;
   out.push({id:e.id||'',txt:txt.slice(0,40).replace(/\n/g,' | '),dx:Math.round(dx),dy:Math.round(dy),padL:Math.round(padL),padR:Math.round(padR),w:Math.round(b.width),h:Math.round(b.height),clipped});}
  return out});
 for(const o of r){const k=o.txt+'|'+o.id;const bad=o.clipped||Math.abs(o.dy)>3||(Math.abs(o.dx)>3&&Math.abs(o.padL-o.padR)>6);
  if(bad&&!seen.has(k)){seen.set(k,1);console.log(`t=${t} ${o.clipped?'CLIPPED ':''}"${o.txt}" id=${o.id} box ${o.w}x${o.h} dx=${o.dx} dy=${o.dy} padL=${o.padL} padR=${o.padR}`)}}}
console.log(seen.size?`${seen.size} box(es) to review`:'all boxed text centred');await br.close()})();
