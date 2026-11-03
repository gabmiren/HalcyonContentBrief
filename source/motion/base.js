// Halcyon motion helpers. Pages are 1080x1920 and driven by window.seek(t) (seconds).
const $=id=>document.getElementById(id);
const C=x=>Math.max(0,Math.min(1,x)), P=(t,a,d)=>C((t-a)/d), L=(a,b,x)=>a+(b-a)*x;
const E=x=>x>=1?1:1-Math.pow(2,-10*x);
const Q=x=>1-Math.pow(1-x,3);
const IN=x=>x*x*x;
const IO=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const B=x=>{const c1=1.70158,c3=c1+1;return x<=0?0:1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
const rnd=i=>{const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x)};
// Halcyon brand (onboarding form): cyan #00FBF4, grey #AFAFAF, black #000000, white #FFFFFF. Font: Poppins.
const COL={cy:'#00FBF4',cyd:'#0A6E6B',grey:'#AFAFAF',ink:'#FFFFFF',unlit:'#3B4445',lab:'#7E8787'};
// Facts from halcyontraderfunding.com/dynamic-* pages, read 3 Nov 2026. Re-check before posting.
const EVAL=[['Account size','$50K'],['Profit target','$3,000'],['Drawdown','$2,000'],['Minimum days','1']];
const SIZES=['50K','75K','100K','150K'];
const DD={'50K':'$2,000','75K':'$2,500','100K':'$3,000','150K':'$4,000'};
const DISC='Halcyon offers simulated educational accounts. Results not guaranteed. T&C apply.';
// Beat grid: 120 BPM placeholder (no track chosen yet). Drop at 2.0s, downbeats every 2.0s.
const BT0=0, BP=0.5, BD=4, BEAT=n=>BT0+BP*n, DOWN=k=>BEAT(BD+4*k);
function words(el){if(el.dataset.split)return;el.dataset.split=1;const parts=el.innerHTML.split(/(<[^>]+>[^<]*<\/[^>]+>|\s+)/).filter(s=>s&&!/^\s+$/.test(s));el.innerHTML=parts.map(w=>`<span class="w" style="display:inline-block;white-space:pre">${w}</span>`).join(' ');}
function show(id,on){$(id).style.visibility=on?'visible':'hidden';}
function fadeIn(el,t,s,d=.45,dy=30,blur=8){const a=E(P(t,s,d));el.style.opacity=a;el.style.transform=`translateY(${(1-a)*dy}px)`;el.style.filter=blur?`blur(${(1-a)*blur}px)`:'none';return a;}
// Living background: black-to-charcoal, one breathing cyan glow, slow sweep, bokeh, motes. Never static.
const MOTES=[...Array(70)].map((_,i)=>({x:rnd(i)*1080,y:rnd(i+70)*1920,r:1.1+rnd(i+140)*2.4,v:30+rnd(i+210)*40,a:.16+rnd(i+280)*.28,ph:rnd(i+350)*6.28}));
const BOKEH=[...Array(12)].map((_,i)=>({x:rnd(i+500)*1080,y:rnd(i+520)*1920,r:90+rnd(i+540)*150,v:46+rnd(i+560)*44,a:.045+rnd(i+580)*.05,ph:rnd(i+600)*6.28}));
function drawBG(ctx,t,cx=540,cy=860,k=1){
 const g=ctx.createLinearGradient(0,0,0,1920);g.addColorStop(0,'#05080A');g.addColorStop(.55,'#081012');g.addColorStop(1,'#040607');ctx.fillStyle=g;ctx.fillRect(0,0,1080,1920);
 const br=(0.8+0.12*Math.sin(t*1.7)+0.08*Math.sin(t*2.9+1))*k, gx=cx+200*Math.sin(t*0.7), gy=cy+110*Math.sin(t*0.53);
 const r=ctx.createRadialGradient(gx,gy,10,gx,gy,880);r.addColorStop(0,`rgba(0,170,166,${0.24*br})`);r.addColorStop(.45,`rgba(0,120,118,${0.09*br})`);r.addColorStop(1,'rgba(0,90,90,0)');ctx.fillStyle=r;ctx.fillRect(0,0,1080,1920);
 const sx=((t*170)%2400)-600, sh=ctx.createLinearGradient(sx,0,sx+600,520);sh.addColorStop(0,'rgba(0,251,244,0)');sh.addColorStop(.5,'rgba(0,251,244,0.035)');sh.addColorStop(1,'rgba(0,251,244,0)');ctx.fillStyle=sh;ctx.fillRect(0,0,1080,1920);
 BOKEH.forEach(p=>{const y=((p.y-p.v*t)%2400+2400)%2400-240,x=p.x+50*Math.sin(t*0.7+p.ph);const g2=ctx.createRadialGradient(x,y,0,x,y,p.r);g2.addColorStop(0,`rgba(0,251,244,${p.a})`);g2.addColorStop(.7,`rgba(0,251,244,${p.a*.4})`);g2.addColorStop(1,'rgba(0,251,244,0)');ctx.fillStyle=g2;ctx.beginPath();ctx.arc(x,y,p.r,0,6.283);ctx.fill();});
 MOTES.forEach(m=>{const y=((m.y-m.v*t)%1920+1920)%1920,x=m.x+18*Math.sin(t*.8+m.ph),a=m.a*(0.6+0.4*Math.sin(t*2+m.ph));ctx.fillStyle=`rgba(150,255,250,${a})`;ctx.beginPath();ctx.arc(x,y,m.r,0,6.283);ctx.fill();});
}

// slow camera drift on the whole stage so no stretch is ever still
function drift(t){$('st').style.transform=`scale(${1.018+0.014*Math.sin(t*1.1)}) translate(${6*Math.sin(t*0.7)}px,${8*Math.sin(t*0.9)}px)`;}
