// Shared Trade of the Week core for Halcyon: timing, captions, chart story, chart drawing.
const W=(l,i)=>WD[l][i][1], We=(l,i)=>WD[l][i][2];
const D=mkChart(733,0.6,64); D.dir='short'; window.CH=D;
const S=D.S,iE=D.E,X=D.X,N=D.N;
// caption groups per line: [firstWord,lastWord,text]
const CAPG=[
 [[0,3,'Trade of the week']],
 [[0,2,'64 points'],[3,5,'on the Nasdaq']],
 [[0,3,'During the US session'],[4,6,'this trader spotted'],[7,10,'a clean bearish setup'],[11,15,'on the 5-minute chart']],
 [[0,1,'Price left'],[2,5,'a fair value gap'],[6,9,'Instead of chasing it'],[10,11,'he waited'],[12,14,'for a pullback'],[15,19,'to the 50% level'],[20,22,'of that gap'],[23,25,'then went short']],
 [[0,1,'From there'],[2,4,'the 20 EMA'],[5,7,'acted as resistance'],[8,10,'and he rode'],[11,13,'the move down']],
 [[0,2,'No early exit'],[3,6,'He held the trade'],[7,9,'until a candle'],[10,12,'closed back above'],[13,15,'the 20 EMA']],
 [[0,5,'2 hours 45 minutes'],[6,9,'from plan to profit']],
 [[0,2,'Do you use'],[3,5,'the 20 EMA'],[6,9,'to trail your trades?'],[10,11,'Tell us'],[12,14,'in the Discord']]];
const CAPS=[];CAPG.forEach((g,l)=>g.forEach(([a,b,txt])=>CAPS.push({l,a,b,txt,t0:W(l,a),last:We(l,b)})));
CAPS.forEach((c,i)=>{const nx=CAPS[i+1];c.t1=Math.min(nx?nx.t0:1e9,c.last+0.55);});
function capAt(t){for(const c of CAPS)if(t>=c.t0&&t<c.t1)return c;return null;}
// word-level brightness inside a caption group (for the glow style)
function capWords(c,t){const ws=c.txt.split(' ');const n=c.b-c.a+1;return ws.map((w,k)=>{const wi=c.a+Math.min(n-1,Math.floor(k*n/ws.length));return [w,t>=W(c.l,wi)];});}
// chart story
const ST={L2:W(2,0),gap0:W(3,0),fvg:W(3,3),pb0:W(3,6),pb1:We(3,14),half:W(3,17),ent0:W(3,23),short:W(3,25),ema:W(4,3),trend0:W(4,9),trend1:W(5,9),exit0:W(5,10),exit:We(5,12)};
const KF=[[ST.L2-0.2,30],[We(2,15),S],[ST.gap0,S],[We(3,2),S+3],[ST.pb0,S+3],[ST.pb1,iE],[ST.ent0,iE],[ST.short,iE+1],[ST.trend0,iE+1],[ST.trend1,X],[ST.exit0,X],[ST.exit,X+1]];
function rev(t){if(t<=KF[0][0])return KF[0][1];for(let i=1;i<KF.length;i++){const [a,va]=KF[i-1],[b,vb]=KF[i];if(t<=b)return b===a?vb:va+(vb-va)*(t-a)/(b-a);}return X+1;}
function holdMins(t){const r=rev(t);return Math.max(0,Math.min(165,(r-(iE+1))/(X-iE)*165));}
const PMIN=Math.min(...D.l),PMAX=Math.max(...D.h);
// draw the chart. R = target rect, V = {i0,i1,p0,p1}
function drawChart(ctx,t,R,V,o={}){
 const r=rev(t),full=Math.floor(r),f=r-full;
 const xs=i=>R.x+(i-V.i0+0.5)*R.w/(V.i1-V.i0), ys=p=>R.y+R.h*(1-(p-V.p0)/(V.p1-V.p0));
 const cw=Math.max(2,R.w/(V.i1-V.i0)*0.62);
 ctx.save();ctx.beginPath();ctx.rect(R.x,R.y,R.w,R.h);ctx.clip();
 if(o.grid!==false){ctx.strokeStyle='rgba(0,251,244,0.06)';ctx.lineWidth=1.5;for(let k=1;k<6;k++){const y=R.y+R.h*k/6;ctx.beginPath();ctx.moveTo(R.x,y);ctx.lineTo(R.x+R.w,y);ctx.stroke();}}
 // FVG box
 const ga=o.gapA!=null?o.gapA:Math.min(1,Math.max(0,(t-ST.fvg)/0.45));
 if(ga>0){const x0=xs(S)-cw/2,x1=x0+(xs(Math.min(iE+3,N))-x0)*Math.min(1,ga*1.4);ctx.fillStyle=`rgba(0,251,244,${0.13*ga})`;ctx.fillRect(x0,ys(D.gapTop),x1-x0,ys(D.gapBot)-ys(D.gapTop));
  ctx.strokeStyle=`rgba(0,251,244,${0.65*ga})`;ctx.lineWidth=2;ctx.strokeRect(x0,ys(D.gapTop),x1-x0,ys(D.gapBot)-ys(D.gapTop));}
 // 50% line
 const ha=Math.min(1,Math.max(0,(t-ST.half)/0.5));
 if(ha>0){const x0=xs(S)-cw/2,x1=x0+(R.x+R.w-x0)*ha;ctx.setLineDash([12,10]);ctx.strokeStyle='rgba(255,255,255,0.8)';ctx.lineWidth=2.5;ctx.beginPath();ctx.moveTo(x0,ys(D.MID));ctx.lineTo(x1,ys(D.MID));ctx.stroke();ctx.setLineDash([]);}
 // candles
 for(let i=Math.max(0,Math.floor(V.i0)-1);i<=Math.min(N-1,full);i++){
  let op=D.o[i],cl=D.c[i],hi=D.h[i],lo=D.l[i];
  if(i===full){if(f<=0.02)break;const k=f;cl=op+(cl-op)*k;hi=Math.max(op,cl)+(hi-Math.max(D.o[i],D.c[i]))*k;lo=Math.min(op,cl)-(Math.min(D.o[i],D.c[i])-lo)*k;}
  const up=cl>=op,x=xs(i);
  ctx.strokeStyle=up?'#00FBF4':'#AFAFAF';ctx.lineWidth=Math.max(1.5,cw*0.16);ctx.beginPath();ctx.moveTo(x,ys(hi));ctx.lineTo(x,ys(lo));ctx.stroke();
  const yt=ys(Math.max(op,cl)),yb=ys(Math.min(op,cl));ctx.fillStyle=up?'#0B5E5B':'#C9CDCD';ctx.fillRect(x-cw/2,yt,cw,Math.max(2,yb-yt));
  if(up){ctx.strokeStyle='#00FBF4';ctx.lineWidth=1.5;ctx.strokeRect(x-cw/2,yt,cw,Math.max(2,yb-yt));}
 }
 // EMA
 const ea=Math.min(1,Math.max(0,(t-ST.ema)/0.8));
 if(ea>0){const iEnd=Math.min(r,N-0.001),i0=Math.max(0,Math.floor(V.i0)-1),iDraw=i0+(iEnd-i0)*ea;
  ctx.save();ctx.shadowColor='rgba(0,251,244,0.9)';ctx.shadowBlur=18;ctx.strokeStyle='#5FFFF9';ctx.lineWidth=o.emaW||4;ctx.lineJoin='round';ctx.beginPath();
  for(let i=i0;i<=Math.floor(iDraw);i++){const x=xs(i),y=ys(D.ema[i]);i===i0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
  const fi=Math.floor(iDraw),fr=iDraw-fi;if(fi+1<N&&fr>0)ctx.lineTo(xs(fi)+(xs(fi+1)-xs(fi))*fr,ys(D.ema[fi]+(D.ema[fi+1]-D.ema[fi])*fr));
  ctx.stroke();ctx.restore();}
 ctx.restore();
 return {xs,ys,cw};
}
// pill helper: position a DOM pill centred on (x,y) with a pop
function popAt(el,t,at,x,y,on=true){const k=t>=at?Math.min(1,(t-at)/0.32):0;const s=k<=0?0:B(k);el.style.left=x+'px';el.style.top=y+'px';el.style.opacity=on?Math.min(1,k*3):0;el.style.transform=`translate(-50%,-50%) scale(${s})`;el.style.visibility=k>0&&on?'visible':'hidden';}
