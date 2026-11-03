// Four Halcyon backgrounds, all different from the 18th Street bokeh look. Deterministic, never static.
// Each takes (ctx, t, pulse) where pulse is 0..1 decaying after each downbeat.
function bgBase(ctx){const g=ctx.createLinearGradient(0,0,0,1920);g.addColorStop(0,'#020405');g.addColorStop(.6,'#040809');g.addColorStop(1,'#010203');ctx.fillStyle=g;ctx.fillRect(0,0,1080,1920);}
function vignette(ctx){const v=ctx.createRadialGradient(540,900,300,540,900,1250);v.addColorStop(0,'rgba(0,0,0,0)');v.addColorStop(1,'rgba(0,0,0,.65)');ctx.fillStyle=v;ctx.fillRect(0,0,1080,1920);}

// 1. GRID HORIZON: perspective trading floor, a live price line along the horizon
const CHART=[...Array(400)].map((_,i)=>{let v=0;for(let k=1;k<6;k++)v+=Math.sin(i*0.07*k+rnd(k)*6)*(14/k);return v+Math.sin(i*0.013)*30;});
function bgGrid(ctx,t,pulse){bgBase(ctx);
 const HY=1180,VX=540;
 const haze=ctx.createLinearGradient(0,HY-260,0,HY+120);haze.addColorStop(0,'rgba(0,251,244,0)');haze.addColorStop(.75,`rgba(0,200,195,${0.10+0.05*pulse})`);haze.addColorStop(1,'rgba(0,251,244,0)');ctx.fillStyle=haze;ctx.fillRect(0,HY-260,1080,380);
 ctx.lineWidth=1.5;
 for(let i=-14;i<=14;i++){const x=VX+i*95;ctx.strokeStyle=`rgba(0,251,244,${0.10*(1-Math.abs(i)/16)})`;ctx.beginPath();ctx.moveTo(VX+i*8,HY);ctx.lineTo(x*3-VX*2,1920+200);ctx.stroke();}
 const sp=(t*0.8)%1;
 for(let k=0;k<14;k++){const z=(k+sp)/14, y=HY+Math.pow(z,2.2)*900;ctx.strokeStyle=`rgba(0,251,244,${0.03+0.14*z})`;ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(1080,y);ctx.stroke();}
 for(let k=0;k<9;k++){const y=HY-110-k*120;ctx.strokeStyle=`rgba(0,251,244,${0.025*(1-k/9)})`;ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(1080,y);ctx.stroke();}
 for(let i=0;i<12;i++){const x=((i*110-t*25)%1320+1320)%1320-120;ctx.strokeStyle='rgba(0,251,244,.022)';ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,HY);ctx.stroke();}
 const off=t*70;ctx.save();ctx.shadowColor='rgba(0,251,244,.8)';ctx.shadowBlur=18;ctx.strokeStyle='rgba(0,251,244,.38)';ctx.lineWidth=3;ctx.beginPath();
 for(let x=-20;x<=1100;x+=8){const idx=Math.floor((x+off)/8)%400,v=CHART[(idx+400)%400];const y=HY-60-v;x<=-20?ctx.moveTo(x,y):ctx.lineTo(x,y);}ctx.stroke();ctx.restore();
 vignette(ctx);}

// 2. CANDLE FIELD: blurred candlesticks drifting in three depths (sprites pre-blurred once for speed)
const CANDLES=[...Array(54)].map((_,i)=>({x:rnd(i+11)*1180-50,y:rnd(i+33)*2200,h:60+rnd(i+55)*220,w:14+rnd(i+77)*20,up:rnd(i+99)>.42,d:i%3,ph:rnd(i+121)*6.28}));
let CSPR=null;
function candleSprites(){CSPR=CANDLES.map(c=>{const sc=[1.9,1.25,.8][c.d],bl=[16,7,2][c.d],al=[.10,.13,.10][c.d];const w=c.w*sc,h=c.h*sc,pad=bl*3+10;
 const cv=document.createElement('canvas');cv.width=Math.ceil(w+pad*2);cv.height=Math.ceil(h*1.7+pad*2);const x=cv.getContext('2d');x.filter=`blur(${bl}px)`;
 const a=al*(c.up?1:.55);x.fillStyle=`rgba(0,251,244,${a})`;const cx=cv.width/2,cy=cv.height/2;x.fillRect(cx-w/2,cy-h/2,w,h);x.fillRect(cx-1.5*sc,cy-h*.85,3*sc,h*1.7);return cv;});}
function bgCandles(ctx,t,pulse){bgBase(ctx);if(!CSPR)candleSprites();
 const glow=ctx.createRadialGradient(540,1000,40,540,1000,1000);glow.addColorStop(0,`rgba(0,140,136,${0.16+0.06*pulse})`);glow.addColorStop(1,'rgba(0,80,78,0)');ctx.fillStyle=glow;ctx.fillRect(0,0,1080,1920);
 [2,1,0].forEach(layer=>{const sp=[70,46,26][layer];CANDLES.forEach((c,i)=>{if(c.d!==layer)return;const y=((c.y-t*sp)%2200+2200)%2200-140,x=c.x+26*Math.sin(t*.8+c.ph);const cv=CSPR[i];ctx.drawImage(cv,x-cv.width/2,y-cv.height/2);});});
 vignette(ctx);}

// 3. AURORA: slow ribbons of cyan light, deep black centre
function bgAurora(ctx,t,pulse){bgBase(ctx);
 ctx.save();ctx.globalCompositeOperation='lighter';
 const bands=[{y:380,a:90,f:.0042,s:.35,al:.11,th:220},{y:620,a:110,f:.0031,s:-.27,al:.075,th:300},{y:1420,a:100,f:.0037,s:.31,al:.10,th:260},{y:1690,a:70,f:.0050,s:-.4,al:.075,th:200}];
 bands.forEach((b,bi)=>{for(let k=0;k<26;k++){const o=(k/25-.5)*b.th;ctx.strokeStyle=`rgba(0,${200+k*2},${196+k*2},${b.al*(1-Math.abs(k/25-.5)*1.6)*(1+0.5*pulse)})`;ctx.lineWidth=5;ctx.beginPath();
  for(let x=-40;x<=1120;x+=20){const y=b.y+o+Math.sin(x*b.f+t*b.s*2+bi)*b.a+Math.sin(x*b.f*2.3-t*b.s*1.3)*b.a*.35;x<=-40?ctx.moveTo(x,y):ctx.lineTo(x,y);}ctx.stroke();}});
 ctx.restore();
 const c=ctx.createRadialGradient(540,960,100,540,960,700);c.addColorStop(0,'rgba(0,0,0,.35)');c.addColorStop(1,'rgba(0,0,0,0)');ctx.fillStyle=c;ctx.fillRect(0,0,1080,1920);
 vignette(ctx);}

// 4. PULSE MATRIX: dot grid that ripples from the centre on every downbeat, faint ticker columns
const TICK=[...Array(6)].map((_,c)=>[...Array(40)].map((_,r)=>(4800+Math.round(rnd(c*50+r)*900)).toLocaleString('en-US')+'.'+String(Math.round(rnd(c*90+r)*99)).padStart(2,'0')));
function bgPulse(ctx,t,pulse,sinceDown){bgBase(ctx);
 const sp=40,cx=540,cy=960,R=sinceDown*1300;
 for(let y=20;y<1920;y+=sp)for(let x=20;x<1080;x+=sp){const d=Math.hypot(x-cx,y-cy);const ring=Math.exp(-Math.pow((d-R)/90,2))*(1-Math.min(1,sinceDown/1.4));
  const a=0.13+0.07*Math.sin(t*1.3+x*.01+y*.007)+0.6*ring;ctx.fillStyle=`rgba(0,251,244,${a})`;const r=4+3*ring;ctx.fillRect(x-r/2,y-r/2,r,r);}
 ctx.font='500 22px Poppins';ctx.fillStyle='rgba(0,251,244,.12)';
 [40,170,880,1010].forEach((x,ci)=>{const off=(t*(30+ci*6))%(40*48);for(let r=0;r<42;r++){const y=((r*48-off)%(40*48)+40*48)%(40*48);ctx.fillText(TICK[ci][r%40],x-30,y);}});
 const g=ctx.createRadialGradient(cx,cy,10,cx,cy,800);g.addColorStop(0,`rgba(0,150,146,${0.12+0.08*pulse})`);g.addColorStop(1,'rgba(0,80,78,0)');ctx.fillStyle=g;ctx.fillRect(0,0,1080,1920);
 vignette(ctx);}
