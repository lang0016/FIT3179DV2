// Render the actual application over HTTP. Optional SITE_URL tests the public site.
import {chromium} from 'playwright';
import {spawn} from 'node:child_process';
import {mkdir,writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
const root=fileURLToPath(new URL('../',import.meta.url));
const base=process.env.SITE_URL || 'http://127.0.0.1:4173/';
const output=new URL('../.browser-tests/',import.meta.url);
let server,browser;
const results=[];
try {
 if(!process.env.SITE_URL){server=spawn('python3',['-m','http.server','4173','--bind','127.0.0.1'],{cwd:root,stdio:'ignore'});}
 for(let i=0;i<100;i++){try{const r=await fetch(base);if(r.ok)break;}catch{}if(i===99)throw new Error('HTTP server did not become ready');await new Promise(r=>setTimeout(r,100));}
 browser=await chromium.launch({headless:true,args:['--no-sandbox']});
 await mkdir(output,{recursive:true});
 for(const width of [1180,1280,1366,1440]){
  const page=await browser.newPage({viewport:{width,height:1000},deviceScaleFactor:1});
  const errors=[],failed=[],warnings=[],badResponses=[],dataRequests=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('console',m=>{if(m.type()==='error')errors.push(m.text());if(m.type()==='warning')warnings.push(m.text());});
  page.on('requestfailed',r=>failed.push(r.url()));
  page.on('response',r=>{if(r.status()>=400)badResponses.push(r.url());if(/\.(json|geojson|csv)(\?|$)/.test(r.url()))dataRequests.push(r.body().then(b=>b.length));});
  await page.goto(base,{waitUntil:'networkidle'});
  await page.waitForFunction(()=>document.documentElement.dataset.ready==='true',{timeout:60000});
  const result=await page.evaluate(()=>{
   const paragraphViolations=[];
   // The student requested a full-width acknowledgement; story paragraphs stay narrow.
   document.querySelectorAll('p:not(.acknowledgement p)').forEach(p=>{
    if(!p.getClientRects().length)return;
    const lines={};const walk=document.createTreeWalker(p,NodeFilter.SHOW_TEXT);let t;
    while(t=walk.nextNode()){const re=/\S+/g;let m;while(m=re.exec(t.textContent)){const range=document.createRange();range.setStart(t,m.index);range.setEnd(t,m.index+m[0].length);const r=range.getClientRects()[0];if(!r?.width)continue;(lines[Math.round(r.top)]??=[]).push(m[0]);}}
    for(const words of Object.values(lines))if(words.length>10)paragraphViolations.push(words.join(' '));
   });
   const plots=[...document.querySelectorAll('.chart-box')];const textOutside=[],textOverlaps=[];
   for(const svg of document.querySelectorAll('.chart-box svg')){
    const bounds=svg.getBoundingClientRect();const ts=[...svg.querySelectorAll('text')].filter(t=>t.textContent.trim()&&t.getBoundingClientRect().width);
    for(const t of ts){const r=t.getBoundingClientRect();if(r.x<bounds.x-2||r.right>bounds.right+2||r.y<bounds.y-2||r.bottom>bounds.bottom+2)textOutside.push(t.textContent);}
    for(let i=0;i<ts.length;i++)for(let j=i+1;j<ts.length;j++){const a=ts[i].getBoundingClientRect(),b=ts[j].getBoundingClientRect();if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>2&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>2){if(a.x===b.x&&a.y===b.y&&ts[i].textContent===ts[j].textContent)continue;textOverlaps.push([ts[i].textContent,ts[j].textContent]);}}
   }
   return {overflow:document.documentElement.scrollWidth>innerWidth,paragraphViolations,textOutside,textOverlaps,charts:plots.length,loaded:plots.filter(p=>p.dataset.loaded==='true').length,accessible:plots.filter(p=>p.tabIndex===0&&p.querySelector('svg[role="img"][aria-label]')).length};
  });
  result.dataBytes=(await Promise.all(dataRequests)).reduce((a,b)=>a+b,0);
  if(width===1280){
   const mapData=await page.evaluate(()=>{const view=window.__farmers.views.get(10).view;return {reference:view.data('reference').map(r=>r.abbr).sort(),reported:view.data('states').length,total:view.data('states').reduce((sum,r)=>sum+r.farms,0)};});
   assert.deepEqual(mapData.reference,['ACT','NSW','NT','QLD','SA','TAS','VIC','WA']);assert.equal(mapData.reported,6);assert.equal(mapData.total,3772);
   const hierarchy=await page.evaluate(()=>{const view=window.__farmers.views.get(11).view;return {employingGroups:view.data('leaves').filter(r=>r.parent==='with-employees').length,leaves:view.data('leaves').length,total:view.data('leaves').reduce((sum,r)=>sum+r.value,0)};});
   assert.equal(hierarchy.employingGroups,4);assert.equal(hierarchy.leaves,5);assert.equal(hierarchy.total,144678);
   await page.selectOption('#sector-focus','Dairy cattle');
   await page.waitForFunction(()=>[7,8,9].every(n=>window.__farmers.views.get(n).view.signal('sectorFocus')==='Dairy cattle'));
   result.outlineHighlight=await page.locator('#chart-8 [stroke="#233942"][stroke-width="3"]').count()>0;
   result.highlight=await page.evaluate(()=>[7,8,9].every(n=>window.__farmers.views.get(n).view.signal('sectorFocus')==='Dairy cattle'));
   await page.locator('#figure-6 summary').click();result.dataTable=await page.locator('#figure-6 tbody').isVisible();
   await page.locator('#sector-focus').focus();await page.keyboard.press('Home');result.keyboardControl=await page.locator('#sector-focus').evaluate(el=>document.activeElement===el);
  }
  await page.screenshot({path:fileURLToPath(new URL(`site-${width}.png`,output)),fullPage:true});
  const row={width,...result,errors,warnings,failed,badResponses};results.push(row);
  assert.equal(result.charts,12);assert.equal(result.loaded,12);assert.equal(result.accessible,12);
  assert.deepEqual(await page.locator('.chart-counter').allTextContents(),Array.from({length:12},(_,i)=>String(i+1).padStart(2,'0')+' / 12'));
  assert.equal(result.overflow,false);assert.deepEqual(result.paragraphViolations,[]);assert.deepEqual(result.textOutside,[]);assert.deepEqual(result.textOverlaps,[]);
  assert.deepEqual(errors,[]);assert.deepEqual(warnings,[]);assert.deepEqual(failed,[]);assert.deepEqual(badResponses,[]);assert.ok(result.dataBytes<2_000_000);
  if(width===1280){assert.equal(result.highlight,true);assert.equal(result.outlineHighlight,true);assert.equal(result.dataTable,true);assert.equal(result.keyboardControl,true);}
  await page.close();
 }
 console.log(JSON.stringify(results,null,2));
} finally {
 await writeFile(new URL('results.json',output),JSON.stringify(results,null,2)+'\n');
 await browser?.close();server?.kill();
}
