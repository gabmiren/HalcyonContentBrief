// Shared moves for the Halcyon promos
function sweepAt(el,t,at,d=.7){const k=P(t,at,d);el.style.opacity=k>0&&k<1?Math.sin(Math.PI*k):0;el.style.transform=`translateX(${L(-230,230,IO(k))}%) skewX(-18deg)`;}
function flareAt(el,t,at,d=.55){const k=P(t,at-.08,d);el.style.opacity=k<=0||k>=1?0:Math.pow(Math.sin(Math.PI*k),1.5)*.9;el.style.transform=`scale(${0.5+0.9*E(k)})`;}
// segmented control: steps = [[time, index], ...]; first step sets the start index
function segAt(cont,t,steps){const ch=[...cont.querySelectorAll('.sg')],ind=cont.querySelector('.segi');let pos=steps[0][1];
 steps.slice(1).forEach(([at,i])=>{pos=L(pos,i,E(P(t,at,.32)));});
 const a=Math.floor(pos),b=Math.min(ch.length-1,a+1),f=pos-a,x=L(ch[a].offsetLeft,ch[b].offsetLeft,f),w=L(ch[a].offsetWidth,ch[b].offsetWidth,f);
 ind.style.left=x+'px';ind.style.width=w+'px';ch.forEach((c,j)=>c.classList.toggle('on',Math.abs(pos-j)<0.5));return Math.round(pos);}
function growPill(pill,txt,t,at,pad=90){const g=E(P(t,at,.45)),full=txt.offsetWidth+pad;pill.style.width=Math.max(pill.offsetHeight||92,full*g)+'px';pill.style.opacity=C(P(t,at,.1));txt.style.opacity=C((g-.6)/.4);}
function bgPulseAt(t,downs){let last=-99;downs.forEach(d=>{if(t>=d)last=d;});return Math.exp(-3*(t-last));}
