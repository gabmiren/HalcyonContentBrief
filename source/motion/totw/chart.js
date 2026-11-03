// Halcyon Trade of the Week: example trade (illustration only). Bearish FVG, 50% entry, 20 EMA trail, exit on close above.
function mkChart(seed,K,TGT){
 let s=seed;const R=()=>{s=(s*1664525+1013904223)>>>0;return s/4294967296};const N2=()=>(R()+R()+R()-1.5)/1.5;
 const S=70,E=S+11,X=E+33,N=X+1,A=2/21;
 const o=[],c=[],h=[],l=[];
 let p=21412;
 for(let i=0;i<S;i++){const tgt=21412+120*(i/(S-1))+8*Math.sin(i*0.37)+5*Math.sin(i*1.1+2);
  o[i]=p;c[i]=tgt+N2()*4;if(Math.abs(c[i]-o[i])<1.5)c[i]=o[i]+(R()<.5?-2:2);p=c[i];}
 const seq=[-28,-74,-18];
 for(let k=0;k<3;k++){const i=S+k;o[i]=p;c[i]=p+seq[k];p=c[i];}
 const pb=[-6,8,-5,11,12,-4,13,6];
 for(let k=0;k<8;k++){const i=S+3+k;o[i]=p;c[i]=p+pb[k];p=c[i];}
 o[E]=p;c[E]=p-14;p=c[E];
 for(let k=1;k<33;k++){const i=E+k;o[i]=p;
  let d=K*(-5.6*Math.exp(-k/17)-1.2)+N2()*4.2+(k%6==3?6.5:0)+(k%6==4?-5.5:0);
  if(k>=26)d=2.0+N2()*2.4;
  c[i]=p+d;p=c[i];}
 o[X]=p;c[X]=p+24;
 for(let i=0;i<N;i++){const top=Math.max(o[i],c[i]),bot=Math.min(o[i],c[i]);h[i]=top+1+R()*5;l[i]=bot-1-R()*5;}
 h[S]=o[S]+3;l[S]=c[S]-5;h[S+1]=o[S+1]+1.5;l[S+1]=c[S+1]-6;h[S+2]=o[S+2]+9;l[S+2]=c[S+2]-4;
 const gapTop=l[S],gapBot=h[S+2],MID=(gapTop+gapBot)/2;
 const ema=[];const TOUCH=[E+5,E+12,E+19,E+29];
 for(let i=0;i<N;i++){
  if(i>0&&i!==S&&i!==S+1&&i!==S+2)o[i]=c[i-1];
  const prev=i?ema[i-1]:c[0];
  if(i>=S+3&&i<E){c[i]=Math.min(c[i],prev-5,MID-8);h[i]=Math.min(Math.max(o[i],c[i])+1+((i*7)%5),MID-3);l[i]=Math.min(l[i],Math.min(o[i],c[i])-1);}
  if(i==E){h[E]=MID;c[E]=Math.min(c[E],prev-6);l[E]=Math.min(o[E],c[E])-3;}
  if(i>E&&i<X){c[i]=Math.min(c[i],prev-3.5);h[i]=Math.max(o[i],c[i])+1+((i*13)%6)*0.8;l[i]=Math.min(o[i],c[i])-1-((i*11)%7)*0.7;
   if(h[i]>prev-1)h[i]=prev-1;
   if(TOUCH.includes(i)){c[i]=Math.min(prev-7,Math.max(c[i],o[i]+12));h[i]=prev+0.5;}}
  if(i==X){c[X]=prev+14;h[X]=c[X]+3;l[X]=o[X]-2;}
  if(i>0){h[i]=Math.max(h[i],o[i],c[i]);l[i]=Math.min(l[i],o[i],c[i]);}
  ema[i]=i?prev+A*(c[i]-prev):c[0];
 }
 if(TGT){c[X]=MID-TGT;h[X]=Math.max(h[X],c[X]+3);l[X]=Math.min(o[X],c[X])-2;ema[X]=ema[X-1]+A*(c[X]-ema[X-1]);}
 return {S,E,X,N,A,o,c,h,l,ema,gapTop,gapBot,MID,TOUCH,PTS:MID-c[X]};
}
if(typeof module!=='undefined')module.exports=mkChart;
