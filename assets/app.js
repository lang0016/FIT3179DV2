'use strict';
(() => {
  const views = new Map();
  let metadata = [];
  let geometryPromise;
  async function sharedGeometry() {
    geometryPromise ??= fetch('data/states.geojson').then(r=>{if(!r.ok)throw new Error('Boundary data could not load');return r.json();});
    return (await geometryPromise).features;
  }
  const sectorNames = ['Sheep, beef cattle and grain','Fruit and tree nuts','Dairy cattle','Other livestock','Other crops','Mushrooms and vegetables','Nursery and floriculture','Poultry','Deer'];
  const node = (tag, className, text) => {
    const el = document.createElement(tag);
    if (className) el.className = className;
    if (text !== undefined) el.textContent = text;
    return el;
  };
  function tableValue(value) {
    if (value === null || value === undefined) return 'Not reported';
    if (typeof value === 'number') return new Intl.NumberFormat('en-AU', {maximumFractionDigits: 1}).format(value);
    return String(value);
  }
  function makeCard(meta) {
    const card = node('article','chart-card'); card.id = 'figure-' + meta.n;
    const header = node('header');
    const top = node('div','chart-topline');
    top.append(node('span','chart-counter',String(meta.n).padStart(2,'0') + ' / 12'),node('span','chart-kicker',meta.kicker));
    const title = node('h3','',meta.title); title.id = meta.id + '-title';
    header.append(top,title,node('span','chart-period',meta.period));
    const plot = node('div','chart-box'); plot.id = meta.id; plot.tabIndex = 0;
    plot.setAttribute('role','group'); plot.setAttribute('aria-labelledby',title.id); plot.setAttribute('aria-describedby',meta.id + '-finding');
    plot.append(node('span','loading','Loading the visualisation…'));
    if (meta.n === 6) {const key=node('div','mini-key');key.append(node('span','','Males · left'),node('span','female','Females · right'));header.append(key);}
    if (meta.n === 4) {const key=node('div','mini-key');key.append(node('span','','◆ June 2025 change'),node('span','context','○ June 2024 baseline'));header.append(key);}
    const caption = node('div','chart-caption');
    const finding=node('p','finding',meta.finding);finding.id=meta.id+'-finding';
    caption.append(finding,node('p','chart-note',meta.note));
    const source=node('div','card-source');
    const sourceLink=node('a','',meta.source.includes('dairyaustralia')?'Source: Dairy Australia ↗':'Source: ABS ↗');sourceLink.href=meta.source;sourceLink.target='_blank';sourceLink.rel='noopener';
    const spec=node('a','','Chart specification ↗');spec.href=meta.file;spec.target='_blank';spec.rel='noopener';source.append(sourceLink,spec);
    const details=node('details');details.append(node('summary','','Read the data'));
    const scroll=node('div','data-scroll');scroll.tabIndex=0;scroll.setAttribute('aria-label',meta.title+' data table');
    const table=node('table');table.append(node('caption','',meta.period+' · '+meta.idiom));
    const head=node('thead');const hr=node('tr');meta.columns.forEach(c=>{const th=node('th','',c[1]);th.scope='col';hr.append(th);});head.append(hr);table.append(head);
    const tbody=node('tbody');meta.table.forEach(row=>{const tr=node('tr');meta.columns.forEach(c=>tr.append(node('td','',tableValue(row[c[0]]))));tbody.append(tr);});table.append(tbody);scroll.append(table);details.append(scroll);
    card.append(header,plot,caption,source,details);return card;
  }
  function plotHeight(meta, width) {
    if (meta.n === 8 || meta.n === 9) return 410;
    if (meta.n === 10) return Math.max(255, width * 470 / 760);
    return 370;
  }
  async function render(meta) {
    const el=document.getElementById(meta.id);
    try {
      const response=await fetch(meta.file);if (!response.ok) throw new Error('Specification request failed: '+response.status);
      const spec=await response.json();
      if(meta.n===1 || meta.n===2) {
        const features=await sharedGeometry();
        const replaceGeometry=value=>{if(!value || typeof value!=='object')return;if(value.data?.url==='data/states.geojson')value.data={values:features};for(const child of Object.values(value)){if(Array.isArray(child)){for(const item of child)replaceGeometry(item);}else if(child&&typeof child==='object')replaceGeometry(child);}};
        replaceGeometry(spec);
      }
      const width=Math.floor(el.clientWidth);const height=plotHeight(meta,width);
      if (meta.n === 8 && width < 480) {spec.layer[0].encoding.color.legend.columns=1;spec.layer[0].encoding.color.legend.title='Relative mix (×)';}
      if (meta.n === 9 && width < 480) {spec.layer[0].encoding.color.legend.columns=1;spec.layer[0].encoding.color.legend.title='Turnover (AUD)';}
      if (spec.params) spec.params.forEach(p=>{if(p.name==='sectorFocus')p.value=document.getElementById('sector-focus').value;});
      el.style.height=(height+18)+'px';el.replaceChildren();
      const result=await vegaEmbed(el,spec,{renderer:'svg',actions:false,width,height,tooltip:{theme:'light'}});
      const svg=el.querySelector('svg');
      if (svg) {svg.setAttribute('role','img');svg.setAttribute('aria-label',meta.title+'. '+meta.finding);}
      views.set(meta.n,{view:result.view,el,meta,width});
      el.dataset.loaded='true';
    } catch (error) {
      console.error('Chart '+meta.n,error);el.replaceChildren(node('p','plot-error','This chart could not load. The data table and source link below are still available.'));el.dataset.error='true';
    }
  }
  async function init() {
    const response=await fetch('assets/charts.json');if (!response.ok) throw new Error('Chart register could not load');metadata=await response.json();
    document.querySelectorAll('[data-charts]').forEach(grid=>grid.dataset.charts.split(',').forEach(n=>grid.append(makeCard(metadata.find(x=>x.n===Number(n))))));
    const select=document.getElementById('sector-focus');sectorNames.forEach(name=>select.append(new Option(name,name)));
    select.addEventListener('change',async()=>{
      for (const n of [7,8,9]) {const entry=views.get(n);if(entry) await entry.view.signal('sectorFocus',select.value).runAsync();}
    });
    await Promise.all(metadata.map(render));
    let timer;
    window.addEventListener('resize',()=>{clearTimeout(timer);timer=setTimeout(async()=>{
      for (const entry of views.values()) {
        const width=Math.floor(entry.el.clientWidth);if(width===entry.width) continue;
        if([8,9].includes(entry.meta.n) && (width < 480) !== (entry.width < 480)) {await render(entry.meta);continue;}
        const height=plotHeight(entry.meta,width);entry.el.style.height=(height+18)+'px';entry.width=width;
        await entry.view.width(width).height(height).resize().runAsync();
      }
    },160);});
    window.__farmers={views,metadata};document.documentElement.dataset.ready='true';
  }
  init().catch(error=>{console.error(error);document.getElementById('main').append(node('p','plot-error','The chart register could not load. Please reload, or open the research register below.'));});
})();
