const {chromium}=require('playwright');const path=require('path');
(async()=>{const br=await chromium.launch();const p=await br.newPage();
for(const f of process.argv.slice(2)){await p.goto('file://'+path.resolve(f));const d=await p.evaluate(()=>typeof T_FIN!=='undefined'?T_FIN:DUR);console.log(f,(Math.ceil(d*30)/30).toFixed(3));}
await br.close();})();
