const {chromium}=require('playwright');const path=require('path');
(async()=>{const [file,...ts]=process.argv.slice(2);const br=await chromium.launch();const p=await br.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('PAGE ERROR',e.message));p.on('console',m=>{if(m.type()=='error')console.log('CONSOLE ERROR',m.text())});
await p.goto('file://'+path.resolve(file));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
const base=path.basename(file,'.html');
for(const t of ts){await p.evaluate(t=>seek(t),+t);await p.screenshot({path:`snap/${base}_${t}.jpg`,type:'jpeg',quality:80});}
await br.close();console.log(`snap/${base}_<t>.jpg x${ts.length}`)})();
