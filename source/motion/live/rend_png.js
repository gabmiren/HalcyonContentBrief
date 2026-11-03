const {chromium}=require('playwright');const path=require('path');
(async()=>{const [file,dir,a,b]=[process.argv[2],process.argv[3],+process.argv[4],+process.argv[5]];
const br=await chromium.launch();const p=await br.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>{console.error('PAGE ERROR',e.message);process.exit(1)});
await p.goto('file://'+path.resolve(file));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
for(let f=a;f<b;f++){await p.evaluate(t=>seek(t),f/30);await p.screenshot({path:`${dir}/${String(f).padStart(5,'0')}.png`,omitBackground:true});}
await br.close()})();
