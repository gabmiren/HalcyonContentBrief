// node rend.js stills t1,t2,...   |  node rend.js video out.mp4 DUR
const { chromium } = require('playwright');const { spawn } = require('child_process');const fs=require('fs');const path=require('path');
(async()=>{const mode=process.argv[2];const br=await chromium.launch();const p=await br.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>{console.error('PAGE ERROR',e.message);process.exit(1)});
await p.goto('file://'+path.join(__dirname,'payout_call.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
if(mode==='stills'){for(const t of process.argv[3].split(',').map(Number)){await p.evaluate(t=>seek(t),t);await p.screenshot({path:path.join(__dirname,`s_${t}.jpg`),type:'jpeg',quality:85});}}
else{const out=process.argv[3],dur=+process.argv[4],N=Math.round(dur*30),tmp=out.replace(/\.mp4$/,'.part.mp4');
 const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',tmp],{stdio:['pipe','inherit','inherit']});
 for(let f=0;f<N;f++){await p.evaluate(t=>seek(t),f/30);const b=await p.screenshot({type:'jpeg',quality:92});if(!ff.stdin.write(b))await new Promise(r=>ff.stdin.once('drain',r));if(f%150===0)console.log('frame',f,'/',N);}
 ff.stdin.end();const code=await new Promise(r=>ff.on('close',r));if(code===0)fs.renameSync(tmp,out);else{console.error('ffmpeg failed');process.exit(1);}}
await br.close();})();
