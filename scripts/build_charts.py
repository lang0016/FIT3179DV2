#!/usr/bin/env python3
"""Generate readable Vega/Vega-Lite specifications from verified research extracts."""
import csv,json,math,statistics
from collections import defaultdict
from pathlib import Path
from shapely.geometry import shape,Polygon,MultiPolygon
from shapely.ops import transform
from shapely.affinity import scale,translate
from pyproj import Transformer
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/research';CHARTS=ROOT/'charts';CHARTS.mkdir(exist_ok=True)
BG='#f7f5ef';INK='#233942';BLUE='#174a67';TEAL='#216b60';VIOLET='#6e4b87';MUTED='#53656e';GRID='#d9dedc';CONTEXT='#e4e7e2'
SEQ=['#4c7189','#426780','#355b75','#294f6a','#1c425f','#113650']
SECTORS=['Sheep, beef cattle and grain','Fruit and tree nuts','Dairy cattle','Other livestock','Other crops','Mushrooms and vegetables','Nursery and floriculture','Poultry','Deer']
SHORT={'Sheep, beef cattle and grain':'Sheep, beef & grain','Fruit and tree nuts':'Fruit & tree nuts','Dairy cattle':'Dairy cattle','Other livestock':'Other livestock','Other crops':'Other crops','Mushrooms and vegetables':'Mushrooms & vegetables','Nursery and floriculture':'Nurseries & flowers','Poultry':'Poultry','Deer':'Deer'}
STATE_NAMES=['New South Wales','Victoria','Queensland','South Australia','Western Australia','Tasmania','Northern Territory','Australian Capital Territory']
ABBR=dict(zip(STATE_NAMES,['NSW','VIC','QLD','SA','WA','TAS','NT','ACT']))
POS={'New South Wales':[147,-32,153,-29.5],'Victoria':[144.5,-37,140,-38.8],'Queensland':[144,-22,148,-18.5],'South Australia':[134,-30,129,-33.8],'Western Australia':[121,-25,115,-23],'Tasmania':[147,-42,150,-44],'Northern Territory':[133,-19,133,-15],'Australian Capital Territory':[149.1,-35.5,155,-35.5]}
PROJ={'type':'albers','rotate':[-132,0,0],'parallels':[-18,-36],'center':[0,-27]}
BIZ='https://www.abs.gov.au/statistics/economy/business-indicators/counts-australian-businesses-including-entries-and-exits/jul2021-jun2025'
DA='https://www.dairyaustralia.com.au/industry-reports/australian-dairy-industry-in-focus'
LF='https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia-detailed/mar-2026'
META=[]
def rows(n):return list(csv.DictReader((DATA/n).open()))
def save(n,title,kicker,finding,note,source,period,spec,table,columns,idiom):
 slug=f'{n:02d}-'+['business-share','business-count','dairy-trend','state-change','dairy-waterfall','farmer-pyramid','state-boxplot','sector-heatmap','turnover-composition','dairy-cartogram','employment-treemap','workforce-trend'][n-1]
 spec['usermeta']={'chart':n,'title':title,'finding':finding,'source':source,'period':period,'idiom':idiom}
 spec['description']=finding+' '+note
 (CHARTS/(slug+'.json')).write_text(json.dumps(spec,indent=2)+'\n')
 META.append(dict(n=n,id='chart-'+str(n),file='charts/'+slug+'.json',title=title,kicker=kicker,finding=finding,note=note,source=source,period=period,idiom=idiom,table=table,columns=columns))
def vl(height=320):return {'$schema':'https://vega.github.io/schema/vega-lite/v5.json','width':'container','height':height,'background':BG,'padding':{'left':5,'right':12,'top':12,'bottom':6},'autosize':{'type':'fit','contains':'padding','resize':True},'config':{'font':'Arial','view':{'stroke':None},'axis':{'labelFontSize':13,'titleFontSize':13,'labelColor':INK,'titleColor':INK,'domain':False,'tickColor':GRID,'gridColor':GRID,'gridOpacity':0.7,'titleFontWeight':'normal','titlePadding':14,'labelPadding':8},'legend':{'orient':'top','labelFontSize':12,'titleFontSize':12,'labelColor':INK,'titleColor':INK,'titleFontWeight':'normal','padding':0,'offset':12},'text':{'font':'Arial','fontSize':13,'color':INK}}}
def tooltip(fields):
 titles={'abbr':'State or territory','share':'Share (%)','workers':'Estimated workers (thousands)','businesses':'Agricultural businesses','all_businesses':'All businesses','earlier':'June 2024 businesses','later':'June 2025 businesses','change':'Change in businesses','pct':'Change (%)','national_share':'Eight-state sector share (%)','relative':'Relative sector share','n':'Eligible states','farms':'Registered dairy farms'}
 return [{'field':f,'title':titles.get(f,f.replace('_',' ').capitalize()),'type':'quantitative' if t else 'nominal',**({'format':t} if t else {})} for f,t in fields]
def sector_params(s):s['params']=[{'name':'sectorFocus','value':'All sectors'}];return s
def opacity():return {'value':1}
def main():
 g=rows('business_groups_employment.csv');dairy=rows('dairy_registered_farms.csv');states=[]
 totals={r['state']:int(r['businesses']) for r in rows('all_businesses_by_state.csv')}
 sums=defaultdict(int);by=defaultdict(int)
 for r in g:
  sums[(r['year'],r['state'])]+=int(r['total'])
  by[(r['year'],r['state'],r['sector'])]+=int(r['total'])
 for i,name in enumerate(STATE_NAMES,1):
  count=sums[('2025',name)];lon,lat,llon,llat=POS[name]
  states.append(dict(code=str(i),state=name,abbr=ABBR[name],businesses=count,all_businesses=totals[name],share=count/totals[name]*100,previous=sums[('2024',name)],lon=lon,lat=lat,label_lon=llon,label_lat=llat,label=(f'{ABBR[name]} · {count:,}' if name in ['New South Wales','Tasmania'] else ABBR[name])))
 # 1: normalised map.
 s=vl(365);s['projection']=PROJ;s['data']={'url':'data/states.geojson','format':{'type':'json','property':'features'}}
 s['transform']=[{'lookup':'properties.code','from':{'data':{'values':states},'key':'code','fields':['state','abbr','businesses','all_businesses','share']}}]
 s['mark']={'type':'geoshape','stroke':BG,'strokeWidth':1.5}
 s['encoding']={'color':{'field':'share','type':'quantitative','scale':{'domain':[0,10],'range':SEQ},'legend':{'title':'Agriculture / all businesses (%)','gradientLength':190,'format':'.0f'}},'tooltip':tooltip([('state',None),('share','.1f'),('businesses',',.0f'),('all_businesses',',.0f')])}
 s['layer']=[{'mark':s.pop('mark'),'encoding':s.pop('encoding')},{'data':{'values':[r for r in states if r['abbr'] not in ['ACT','TAS']]},'transform':[],'mark':{'type':'text','fontSize':12,'fontWeight':600,'color':BG},'encoding':{'longitude':{'field':'lon'},'latitude':{'field':'lat'},'text':{'field':'abbr'}}}]
 s['layer'].append({'data':{'values':[{'lon':150,'lat':-43.2}]},'transform':[],'mark':{'type':'text','fontSize':12,'fontWeight':600,'color':INK},'encoding':{'longitude':{'field':'lon'},'latitude':{'field':'lat'},'text':{'value':'TAS'}}})
 save(1,'Small state, strong farming presence','THE BUSINESS LANDSCAPE','Agriculture makes up 9.1% of Tasmania’s businesses, versus 4.9% in NSW.','Colour shows a share of actively trading businesses, not land area or employment. Main-state allocation; class-cell sums are approximate.',BIZ,'June 2025',s,states,[['state','State'],['share','Agriculture share (%)'],['businesses','Agriculture businesses'],['all_businesses','All businesses']],'Choropleth map')
 # 2: proportional symbols with leaders.
 s=vl(365);s['projection']=PROJ
 links=[]
 for r in states:
  for order,(lon,lat) in enumerate([(r['lon'],r['lat']),(r['label_lon'],r['label_lat'])]):links.append(dict(state=r['state'],lon=lon,lat=lat,order=order))
 s['layer']=[{'data':{'url':'data/states.geojson','format':{'type':'json','property':'features'}},'mark':{'type':'geoshape','fill':CONTEXT,'stroke':BG,'strokeWidth':1.3}}, {'data':{'values':links},'mark':{'type':'line','color':MUTED,'strokeWidth':0.7},'encoding':{'longitude':{'field':'lon'},'latitude':{'field':'lat'},'detail':{'field':'state'},'order':{'field':'order'}}},{'data':{'values':states},'mark':{'type':'circle','color':BLUE,'opacity':1,'stroke':BG,'strokeWidth':1.5},'encoding':{'longitude':{'field':'lon'},'latitude':{'field':'lat'},'size':{'field':'businesses','type':'quantitative','scale':{'domain':[0,50000],'range':[0,2500]},'legend':None},'tooltip':tooltip([('state',None),('businesses',',.0f')])}},{'data':{'values':states},'mark':{'type':'text','fontSize':12,'fontWeight':600,'stroke':BG,'strokeWidth':3,'strokeJoin':'round'},'encoding':{'longitude':{'field':'label_lon'},'latitude':{'field':'label_lat'},'text':{'field':'label'}}},{'data':{'values':states},'mark':{'type':'text','fontSize':12,'fontWeight':600,'fill':INK},'encoding':{'longitude':{'field':'label_lon'},'latitude':{'field':'label_lat'},'text':{'field':'label'}}}]
 save(2,'New South Wales has the most businesses','COUNT, NOT COVERAGE','New South Wales has 45,163 agricultural businesses; Tasmania has 4,015.','Smaller circles reduce crowding; their area remains proportional to business count. Points represent state totals, not farm locations. Unknown/other geography is excluded from maps.',BIZ,'June 2025',s,states,[['state','State'],['businesses','Agriculture businesses']],'Proportional-symbol map')
 # 3: dairy time series.
 dt=[dict(year=int(r['financial_year'][:4])+1,season=r['financial_year'],farms=int(r['registered_farms']),provisional=r['provisional']=='True') for r in dairy if r['state']=='Australia']
 s=vl(300);s['data']={'values':dt};s['encoding']={'x':{'field':'year','type':'quantitative','axis':{'title':'Financial year ending June','format':'d','tickCount':5},'scale':{'zero':False}},'y':{'field':'farms','type':'quantitative','axis':{'title':'Registered dairy farms'},'scale':{'domain':[0,7400]}},'tooltip':tooltip([('season',None),('farms',',.0f'),('provisional',None)])}
 s['layer']=[{'mark':{'type':'line','color':VIOLET,'strokeWidth':3,'point':{'filled':True,'size':28}}},{'transform':[{'filter':'datum.year === 2012 || datum.year === 2025'}],'mark':{'type':'text','dy':{'expr':"datum.year === 2025 ? -32 : -15"},'dx':{'expr':"datum.year === 2012 ? 24 : -23"},'fontWeight':600,'color':VIOLET},'encoding':{'text':{'field':'farms','format':','}}}]
 save(3,'Fewer registered dairy farms','THIRTEEN YEARS OF CHANGE','Registered dairy farms fell 44.3%, from 6,770 to 3,772.','This is a dairy-only series, not a count of all farms. The financial year runs July–June; 2024–25 is provisional.',DA,'2011–12 to 2024–25',s,dt,[['season','Financial year'],['farms','Registered farms'],['provisional','Provisional']],'Line chart')
 # 4: indexed dumbbell; a shared 2024 baseline makes small state changes visible.
 change=[dict(state=r['state'],abbr=r['abbr'],earlier=r['previous'],later=r['businesses'],change=r['businesses']-r['previous'],pct=(r['businesses']/r['previous']-1)*100,baseline=0) for r in states]
 order=[r['abbr'] for r in sorted(change,key=lambda r:r['pct'])]
 s=vl(300);s['data']={'values':change};s['encoding']={'y':{'field':'abbr','type':'nominal','sort':order,'axis':{'title':None,'labelPadding':14}},'tooltip':tooltip([('state',None),('earlier',',.0f'),('later',',.0f'),('change','+,.0f'),('pct','+.1f')])}
 xaxis={'title':'Change in businesses (%)','values':[-3,-2,-1,0],'labelExpr':"format(datum.value, '.0f') + '%'",'grid':False}
 s['layer']=[{'mark':{'type':'rule','color':BLUE,'strokeWidth':2.5},'encoding':{'x':{'field':'pct','type':'quantitative','scale':{'domain':[-3.8,0.45],'nice':False},'axis':xaxis},'x2':{'field':'baseline'}}},{'mark':{'type':'point','filled':True,'shape':'diamond','color':BLUE,'size':110},'encoding':{'x':{'field':'pct','type':'quantitative'}}},{'mark':{'type':'point','filled':True,'fill':BG,'stroke':MUTED,'strokeWidth':1.5,'size':55},'encoding':{'x':{'field':'baseline','type':'quantitative'}}},{'mark':{'type':'text','align':'right','dx':-13,'fontSize':13,'fontWeight':600,'color':BLUE},'encoding':{'x':{'field':'pct','type':'quantitative'},'text':{'field':'pct','format':'+.1f'}}}]
 save(4,'Every state has fewer farming businesses','BUSINESS COUNTS · PERCENTAGE CHANGE','South Australia fell 2.3%; Queensland was almost unchanged (−0.1%).','Open circles are the June 2024 baseline (0%). Diamonds show the change to June 2025. Original counts remain in the tooltips and table. Small differences, especially in territories, may reflect confidentiality adjustments.',BIZ,'June 2024 → June 2025',s,change,[['state','State'],['earlier','June 2024'],['later','June 2025'],['change','Count change'],['pct','Change (%)']],'Dumbbell chart')
 # 5: exact state contributions to dairy decline.
 dlookup={(r['financial_year'],r['state']):int(r['registered_farms']) for r in dairy};start=dlookup[('2021-22','Australia')];end=dlookup[('2024-25','Australia')];running=start;wf=[dict(label='2021–22',bottom=0,top=start,value=start,kind='Total',display=f'{start:,}')]
 for state in ['Victoria','New South Wales','Tasmania','Queensland','Western Australia','South Australia']:
  delta=dlookup[('2024-25',state)]-dlookup[('2021-22',state)];nxt=running+delta;wf.append(dict(label=ABBR[state],bottom=min(running,nxt),top=max(running,nxt),value=delta,kind='Change',display=f'{delta:+,}'));running=nxt
 assert running==end
 wf.append(dict(label='2024–25',bottom=0,top=end,value=end,kind='Total',display=f'{end:,}'))
 s=vl(310);s['data']={'values':wf};s['encoding']={'x':{'field':'label','type':'nominal','sort':[x['label'] for x in wf],'axis':{'title':None,'labelAngle':0}},'y':{'field':'top','type':'quantitative','axis':{'title':'Registered dairy farms'},'scale':{'domain':[0,4900]}},'tooltip':tooltip([('label',None),('value','+,.0f')])};s['layer']=[{'mark':{'type':'bar','size':{'expr':'max(12, width / 14)'}},'encoding':{'y2':{'field':'bottom'},'color':{'value':VIOLET}}},{'mark':{'type':'text','dy':-12,'fontWeight':600},'encoding':{'text':{'field':'display'}}}]
 save(5,'Victoria accounts for most of the decline','ONE NATIONAL CHANGE, SIX CONTRIBUTIONS','Victoria accounts for 508 of the 648 fewer registered dairy farms.','Floating bars subtract each state’s contribution. This is an accounting comparison, not an explanation of why farms left. End year provisional.',DA,'2021–22 → 2024–25',s,wf,[['label','State / total'],['value','Contribution or total']],'Waterfall chart')
 # 6: occupation pyramid.
 age=rows('farmers_age_sex_latest.csv');ages=['65 years and over','55-64 years','45-54 years','35-44 years','25-34 years','15-24 years'];ar=[]
 for r in age:ar.append(dict(age=r['age_band'],sex=r['sex'],workers=float(r['total_thousands']),signed=float(r['total_thousands'])*(-1 if r['sex']=='Males' else 1)))
 s=vl(320);s['data']={'values':ar};s['mark']={'type':'bar','cornerRadiusEnd':2};s['encoding']={'y':{'field':'age','type':'ordinal','sort':ages,'axis':{'title':None,'labelExpr':"replace(replace(datum.label, ' years and over', '+'), ' years', '')"}},'x':{'field':'signed','type':'quantitative','stack':None,'scale':{'domain':[-36,36]},'axis':{'title':'Workers (thousands)','labelExpr':'abs(datum.value)','values':[-30,-15,0,15,30]}},'color':{'field':'sex','type':'nominal','scale':{'domain':['Males','Females'],'range':[TEAL,'#926039']},'legend':None},'tooltip':tooltip([('age',None),('sex',None),('workers','.1f')])}
 s['layer']=[{'mark':s.pop('mark'),'encoding':s.pop('encoding')},{'data':{'values':[{}]},'mark':{'type':'rule','color':INK,'strokeWidth':2},'encoding':{'x':{'datum':0,'type':'quantitative'}}}]
 save(6,'Farmers are concentrated in older age groups','THE PEOPLE BEHIND THE FARMS','An estimated 59% of Farmers and Farm Managers are aged 55+.','Teal males on the left; ochre females on the right. The centre line marks zero. Values are survey estimates in thousands. “Farmer” is an occupation, not everyone working in agriculture. Source sex categories are retained.',LF,'February 2026',s,ar,[['age','Age band'],['sex','Source sex category'],['workers','Estimated workers (thousands)']],'Population pyramid')
 # 7: state distributions of non-employing business share.
 obs=[];counts=defaultdict(int)
 for r in g:
  if r['year']=='2025' and r['state'] in STATE_NAMES and int(r['total'])>=100:counts[r['sector']]+=1
 for r in g:
  if r['year']=='2025' and r['state'] in STATE_NAMES and int(r['total'])>=100 and counts[r['sector']]>=5:
   obs.append(dict(state=r['state'],sector=r['sector'],short=SHORT[r['sector']],share=int(r['non_employing'])/int(r['total'])*100,n=counts[r['sector']]))
 s=sector_params(vl(410));s['data']={'values':obs};s['encoding']={'y': {'field': 'short', 'type': 'nominal', 'sort': ['Sheep, beef & grain', 'Fruit & tree nuts', 'Dairy cattle', 'Other livestock', 'Other crops', 'Mushrooms & vegetables', 'Nurseries & flowers', 'Poultry'], 'axis': {'title': None, 'labelLimit': 190}}, 'x': {'field': 'share', 'type': 'quantitative', 'scale': {'domain': [0, 100]}, 'axis': {'title': 'Non-employing (%)', 'tickCount': 6}}};s['layer']=[{'mark': {'type': 'boxplot', 'extent': 'min-max', 'size': 16, 'median': {'color': '#174a67', 'strokeWidth': 2}, 'outliers': False, 'box': {'fill': '#dce8f0', 'stroke': '#174a67', 'strokeWidth': 1.3}, 'rule': {'color': '#174a67', 'strokeWidth': 1.2}}, 'encoding': {}}, {'mark': {'type': 'point', 'filled': True, 'size': 80, 'color': '#174a67', 'stroke': '#ffffff', 'strokeWidth': 1.5, 'yOffset': {'expr': 'datum.pointOffset'}}, 'encoding': {'opacity': {'value': 1}, 'stroke': {'condition': {'test': "sectorFocus !== 'All sectors' && datum.sector === sectorFocus", 'value': '#233942'}, 'value': '#ffffff'}, 'strokeWidth': {'condition': {'test': "sectorFocus !== 'All sectors' && datum.sector === sectorFocus", 'value': 2.5}, 'value': 1.5}, 'tooltip': [{'field': 'state', 'title': 'State', 'type': 'nominal'}, {'field': 'sector', 'title': 'Sector', 'type': 'nominal'}, {'field': 'share', 'title': 'Share (%)', 'type': 'quantitative', 'format': '.1f'}, {'field': 'n', 'title': 'Eligible states', 'type': 'quantitative', 'format': ',.0f'}]}, 'transform': [{'window': [{'op': 'row_number', 'as': 'pointRank'}], 'groupby': ['sector'], 'sort': [{'field': 'share', 'order': 'ascending'}, {'field': 'state', 'order': 'ascending'}]}, {'calculate': '((datum.pointRank - 1) % (width < 300 ? 5 : 3) - (width < 300 ? 2 : 1)) * 11', 'as': 'pointOffset'}]}]
 save(7,'Business staffing differs between states','EACH DOT IS A STATE','Dairy’s non-employing share spans about 48–78% across eligible states.','Pale boxes hold the middle half of state shares; the dark line is the median. Larger dots show individual states, offset vertically for visibility; only horizontal position represents percentage. Each state counts equally. Include ≥100 businesses and ≥5 eligible states per sector. Owners and family may still work.',BIZ,'June 2025',s,obs,[['state','State'],['sector','Sector'],['share','Non-employing (%)'],['n','Eligible states']],'Box plot')
 # 8: composition heatmap.
 heat=[]
 for name in STATE_NAMES:
  for sector in SECTORS:heat.append(dict(state=name,abbr=ABBR[name],sector=sector,short=SHORT[sector],businesses=by[('2025',name,sector)],share=by[('2025',name,sector)]/sums[('2025',name)]*100))
 national={sector:sum(r['businesses'] for r in heat if r['sector']==sector) for sector in SECTORS}
 national_total=sum(national.values())
 bands=['< 0.5×','0.5–<0.8×','0.8–<1.25×','1.25–<2×','2× or more']
 for r in heat:
  r['national_share']=national[r['sector']]/national_total*100
  r['relative']=r['share']/r['national_share']
  r['share_band']=bands[sum(r['relative']>=v for v in [0.5,0.8,1.25,2])]
  r['relative_label']=f"{r['relative']:.1f}×"
 s=sector_params(vl(350));s['data']={'values':heat};s['mark']={'type':'rect','strokeWidth':0};s['encoding']={'x':{'field':'abbr','type':'nominal','sort':[ABBR[x] for x in STATE_NAMES],'axis':{'title':None,'labelAngle':0,'orient':'top'}},'y':{'field':'short','type':'nominal','sort':[SHORT[x] for x in SECTORS],'axis':{'title':None,'labelLimit':190}},'color':{'field':'share_band','type':'ordinal','sort':bands,'scale':{'domain':bands,'range':['#e3edf3','#b4cddd','#7da7c2','#417491','#174a67']},'legend':{'title':'Relative concentration (×)','type':'symbol','columns':3,'symbolType':'square','labelFontSize':12}},'opacity':opacity(),'tooltip':tooltip([('state',None),('sector',None),('businesses',',.0f'),('share','.1f'),('national_share','.1f'),('relative','.2f')])}
 s['layer']=[{'mark':s.pop('mark'),'encoding':s.pop('encoding')},{'transform':[{'filter':"sectorFocus === 'All sectors' ? datum.sector === 'Dairy cattle' && (datum.abbr === 'VIC' || datum.abbr === 'TAS') : datum.sector === sectorFocus"}],'mark':{'type':'text','color':BG,'fontSize':14,'fontWeight':600},'encoding':{'x':{'field':'abbr','type':'nominal','sort':[ABBR[x] for x in STATE_NAMES],'axis':{'title':None,'labelAngle':0,'orient':'top'}},'y':{'field':'short','type':'nominal','sort':[SHORT[x] for x in SECTORS],'axis':{'title':None}},'text':{'field':'relative_label'},'color':{'condition':{'test':'datum.relative >= 1.25','value':BG},'value':INK},'tooltip':tooltip([('state',None),('sector',None),('businesses',',.0f'),('share','.1f')])}}]
 save(8,'Where each sector stands out','REGIONAL SPECIALISATION · 1× = REFERENCE MIX','Dairy makes up a larger business share in Victoria and Tasmania than across the eight states combined.','Each cell divides a sector’s share within that state by its share across all eight states. Darker blue means greater concentration. Below 1× is under-represented; above 1× is over-represented. This compares business mix, not productivity or absolute counts. Labels highlight dairy in Victoria and Tasmania; choose a sector for its labels. Exact values are in tooltips and the table. Small territory counts can produce volatile ratios.',BIZ,'June 2025',s,heat,[['state','State'],['sector','Sector'],['businesses','Businesses'],['share','Within-state share (%)'],['national_share','Eight-state share (%)'],['relative','Relative concentration (×)']],'Heatmap')
 # 9: turnover compositions.
 turns=rows('business_turnover.csv');ta=defaultdict(int);labels=[]
 for r in turns:
  if r['year']=='2025':
   ta[(r['sector'],r['turnover_class'])]+=int(r['businesses'])
   if r['turnover_class'] not in labels:labels.append(r['turnover_class'])
 tr=[]
 short_labels=['< $50k','$50–200k','$200k–2m','$2–5m','$5–10m','$10m+']
 for sector in SECTORS:
  denom=sum(ta[(sector,x)] for x in labels)
  for i,label in enumerate(labels):tr.append(dict(sector=sector,short=SHORT[sector],turnover=short_labels[i],rank=i,businesses=ta[(sector,label)],share=ta[(sector,label)]/denom*100))
 # Combine published bins into three interpretable sales bands.
 grouped=[]
 for sector in SECTORS:
  for j,(label,ranks) in enumerate([('Under 200,000',[0,1]),('200,000–under 2 million',[2]),('2 million or more',[3,4,5])]):
   cells=[r for r in tr if r['sector']==sector and r['rank'] in ranks]
   grouped.append(dict(sector=sector,short=SHORT[sector],turnover=label,rank=j,businesses=sum(r['businesses'] for r in cells),share=sum(r['share'] for r in cells)))
 tr=grouped;short_labels=['Under 200,000','200,000–under 2 million','2 million or more']
 turnover_order=[SHORT[r['sector']] for r in sorted([r for r in tr if r['rank']==2],key=lambda r:-r['share'])]
 offsets=defaultdict(float)
 for row in tr:
  row['midpoint']=offsets[row['sector']]+row['share']/2
  row['label']=f"{row['share']:.0f}%"
  offsets[row['sector']]+=row['share']
 extra_sectors=['Other crops','Fruit and tree nuts','Sheep, beef cattle and grain','Other livestock']
 for row in tr:row['requested_label']=row['rank']==2 and row['sector'] in extra_sectors
 s=sector_params(vl(350));s['padding']['right']=46;s['data']={'values':tr};s['mark']={'type':'bar','stroke':BG,'strokeWidth':1};s['encoding']={'y':{'field':'short','type':'nominal','sort':turnover_order,'axis':{'title':None,'labelLimit':190}},'x':{'field':'share','type':'quantitative','stack':'zero','scale':{'domain':[0,100]},'axis':{'title':'Share of businesses (%)','values':[0,20,40,60,80,100]}},'order':{'field':'rank'},'color':{'field':'turnover','type':'ordinal','sort':short_labels,'scale':{'domain':short_labels,'range':['#53656e','#356c82','#123c52']},'legend':{'title':'Annual sales (Australian dollars)','columns':3,'symbolType':'square','labelLimit':260}},'opacity':opacity(),'stroke':{'condition':{'test':"sectorFocus !== 'All sectors' && datum.sector === sectorFocus",'value':INK},'value':BG},'strokeWidth':{'condition':{'test':"sectorFocus !== 'All sectors' && datum.sector === sectorFocus",'value':3},'value':1},'tooltip':tooltip([('sector',None),('turnover',None),('businesses',',.0f'),('share','.1f')])}
 s['layer']=[{'mark':s.pop('mark'),'encoding':s.pop('encoding')},{'transform':[{'filter':"(datum.share >= 9 || datum.requested_label) && datum.share * width / 100 >= 30"}],'mark':{'type':'text','color':BG,'fontSize':13,'fontWeight':600},'encoding':{'x':{'field':'midpoint','type':'quantitative','scale':{'domain':[0,100]},'axis':{'title':'Share of businesses (%)','values':[0,20,40,60,80,100]}},'y':{'field':'short','type':'nominal','sort':turnover_order,'axis':{'title':None}},'text':{'field':'label'}}}]
 s['layer'].extend([{'transform':[{'filter':'datum.requested_label && datum.share * width / 100 < 30'}],'mark':{'type':'rule','color':INK,'strokeWidth':0.8},'encoding':{'x':{'datum':100,'type':'quantitative'},'x2':{'datum':103},'y':{'field':'short','type':'nominal','sort':turnover_order,'axis':{'title':None}}}},{'transform':[{'filter':'datum.requested_label && datum.share * width / 100 < 30'}],'mark':{'type':'text','align':'left','dx':8,'color':INK,'fontSize':12,'fontWeight':600},'encoding':{'x':{'datum':103,'type':'quantitative'},'y':{'field':'short','type':'nominal','sort':turnover_order,'axis':{'title':None}},'text':{'field':'label'}}}])
 poultry_high=sum(x['share'] for x in tr if x['sector']=='Poultry' and x['rank']>=1)
 save(9,'Business size depends on the sector','SALES BEFORE EXPENSES',f'About {poultry_high:.0f}% of poultry businesses report annual turnover of at least AUD 200,000.','Each bar totals 100%. Rows rank the share with annual sales of at least 2 million Australian dollars. Sales are not profit. Labels include the smaller high-sales shares; narrow segments use outside labels. Three bands combine six published bins; confidentiality adjustments can affect totals.',BIZ,'June 2025',s,tr,[['sector','Sector'],['turnover','Annual turnover (AUD)'],['businesses','Businesses'],['share','Share (%)']],'100% stacked bars')
 # 10: geographic reference beside a count-proportional non-contiguous cartogram.
 features=json.loads((ROOT/'data/states.geojson').read_text())['features'];project=Transformer.from_crs('EPSG:7844','EPSG:3577',always_xy=True).transform
 geos={f['properties']['name']:transform(project,shape(f['geometry'])) for f in features}
 def path_for(geo):
  parts=[]
  for p in ([geo] if isinstance(geo,Polygon) else geo.geoms):
   for ring in [p.exterior,*p.interiors]:parts.append('M'+'L'.join(f'{x:.2f},{y:.2f}' for x,y in ring.coords)+'Z')
  return ''.join(parts)
 xmin=min(g.bounds[0] for g in geos.values());xmax=max(g.bounds[2] for g in geos.values());ymin=min(g.bounds[1] for g in geos.values());ymax=max(g.bounds[3] for g in geos.values())
 reference_factor=min(300/(xmax-xmin),330/(ymax-ymin));reference=[]
 for name,geo in geos.items():
  ref=scale(geo,xfact=reference_factor,yfact=-reference_factor,origin=(0,0));ref=translate(ref,xoff=15-xmin*reference_factor,yoff=100+ymax*reference_factor)
  point=ref.representative_point()
  reference.append(dict(state=name,abbr=ABBR[name],path=path_for(ref),x=point.x,y=point.y,reported=dlookup.get(('2024-25',name)) is not None))
 reported=[name for name in ['Western Australia','South Australia','Tasmania','Queensland','New South Wales','Victoria']]
 # A common area-per-farm factor fits every silhouette in its cell, preserving exact area ratios.
 area_per_farm=min(min(170/(geos[n].bounds[2]-geos[n].bounds[0]),150/(geos[n].bounds[3]-geos[n].bounds[1]))**2*geos[n].area/dlookup[('2024-25',n)] for n in reported)
 cart=[];cart_geometries=[]
 for i,name in enumerate(reported):
  geo=geos[name];value=dlookup[('2024-25',name)];x=435+(i%3)*205;y=145+(i//3)*235
  factor=math.sqrt(value*area_per_farm/geo.area)
  resized=scale(geo,xfact=factor,yfact=-factor,origin=geo.centroid);resized=translate(resized,xoff=x-resized.centroid.x,yoff=y-resized.centroid.y)
  assert all(resized.intersection(other).area<0.01 for other in cart_geometries),'Cartogram states overlap'
  cart_geometries.append(resized)
  cart.append(dict(state=name,abbr=ABBR[name],farms=value,path=path_for(resized),x=x,label_y=y+100,label=f'{ABBR[name]} · {value:,}'))
 s={'$schema':'https://vega.github.io/schema/vega/v5.json','width':1000,'height':560,'padding':0,'background':BG,'autosize':{'type':'fit','contains':'padding','resize':True},'signals':[{'name':'factor','update':'width / 1000'}],'data':[{'name':'reference','values':reference},{'name':'states','values':cart}],'marks':[
  {'type':'path','from':{'data':'reference'},'encode':{'update':{'path':{'field':'path'},'scaleX':{'signal':'factor'},'scaleY':{'signal':'factor'},'fill':{'value':CONTEXT},'stroke':{'value':MUTED},'strokeWidth':{'value':0.7},'tooltip':{'signal':"datum.state + (datum.reported ? '' : ': dairy count not reported')"}}}},
  {'type':'text','from':{'data':'reference'},'encode':{'update':{'x':{'signal':'datum.x * factor'},'y':{'signal':'datum.y * factor'},'text':{'field':'abbr'},'align':{'value':'center'},'fill':{'value':INK},'fontSize':{'value':11},'opacity':{'signal':"width >= 650 && datum.abbr !== 'ACT' ? 1 : 0"}}}},
  {'type':'rule','encode':{'update':{'x':{'signal':'330 * factor'},'y':{'signal':'65 * factor'},'y2':{'signal':'510 * factor'},'stroke':{'value':GRID}}}},
  {'type':'path','from':{'data':'states'},'encode':{'update':{'path':{'field':'path'},'scaleX':{'signal':'factor'},'scaleY':{'signal':'factor'},'fill':{'value':VIOLET},'stroke':{'value':BG},'strokeWidth':{'value':1},'tooltip':{'signal':"datum.state + ': ' + format(datum.farms, ',') + ' registered farms'"}}}},
  {'type':'text','from':{'data':'states'},'encode':{'update':{'x':{'signal':'datum.x * factor'},'y':{'signal':'datum.label_y * factor'},'text':{'field':'label'},'align':{'value':'center'},'fill':{'value':INK},'fontSize':{'signal':'width < 600 ? 9 : 13'},'fontWeight':{'value':600}}}},
  {'type':'text','encode':{'update':{'x':{'signal':'165 * factor'},'y':{'signal':'30 * factor'},'text':{'value':'Geographic reference'},'align':{'value':'center'},'fill':{'value':INK},'fontSize':{'signal':'width < 600 ? 9 : 13'}}}},
  {'type':'text','encode':{'update':{'x':{'signal':'640 * factor'},'y':{'signal':'30 * factor'},'text':{'value':'Area = registered dairy farms'},'align':{'value':'center'},'fill':{'value':INK},'fontSize':{'signal':'width < 600 ? 9 : 13'}}}},
  {'type':'text','encode':{'update':{'x':{'signal':'165 * factor'},'y':{'signal':'490 * factor'},'text':{'value':'NT / ACT: counts not reported'},'align':{'value':'center'},'fill':{'value':INK},'fontSize':{'signal':'width < 600 ? 8 : 11'}}}}
 ]}
 save(10,'Victoria is the centre of dairy farming','GEOGRAPHY AND FARM COUNTS, SIDE BY SIDE','Victoria holds 65.6% of Australia’s registered dairy farms.','Left: complete geographic reference, including NT and ACT. Right: six reported state silhouettes, resized with a common area-per-farm scale and arranged in rows for comparison. Shape area represents farms, not land. NT and ACT counts are not reported; they are not zeros.',DA,'2024–25 · provisional',s,[{'state':name,'farms':dlookup.get(('2024-25',name))} for name in STATE_NAMES],[['state','State'],['farms','Registered farms']],'Non-contiguous cartogram')
 # 11: hierarchical treemap with contrasting employment status and direct callouts.
 national=[r for r in g if r['year']=='2025' and r['state']=='Australia (published class total)'];fields=['non_employing','employees_1_4','employees_5_19','employees_20_199','employees_200_plus'];emp_labels=['No employees','1–4 employees','5–19 employees','20–199 employees','200 or more employees'];emp=[{'id':'root','parent':None,'label':'Agriculture','value':0}]
 for i,(field,label) in enumerate(zip(fields,emp_labels)):emp.append({'id':str(i),'parent':'root','label':label,'value':sum(int(r[field]) for r in national)})
 totalbins=sum(r['value'] for r in emp);published=sum(int(r['total']) for r in national)
 for r in emp[2:]:r['parent']='with-employees'
 emp.append({'id':'with-employees','parent':'root','label':'With employees','value':0})
 s={'$schema':'https://vega.github.io/schema/vega/v5.json','width':1000,'height':400,'padding':0,'background':BG,'autosize':{'type':'fit','contains':'padding','resize':True},
  'data':[{'name':'tree','values':emp,'transform':[{'type':'stratify','key':'id','parentKey':'parent'},{'type':'treemap','field':'value','sort':{'field':'value','order':'descending'},'method':'slicedice','size':[{'signal':'width * 0.53'},{'signal':'height - 12'}],'paddingInner':0,'paddingTop':28,'round':False}]},
   {'name':'groups','source':'tree','transform':[{'type':'filter','expr':"datum.id === 'with-employees'"}]},
   {'name':'leaves','source':'tree','transform':[{'type':'filter','expr':'!datum.children'}]},
   {'name':'employing','source':'leaves','transform':[{'type':'filter','expr':"datum.parent === 'with-employees'"},{'type':'formula','expr':'(datum.y0+datum.y1)/2','as':'source_y'},{'type':'formula','expr':'width * 0.62','as':'label_x'},{'type':'formula','expr':'70 + (toNumber(datum.id)-1)*(height-120)/3','as':'label_y'},{'type':'linkpath','shape':'diagonal','orient':'horizontal','sourceX':'x1','sourceY':'source_y','targetX':'label_x','targetY':'label_y','as':'leader'}]}],
  'marks':[
   {'type':'rect','from':{'data':'groups'},'encode':{'update':{'x':{'field':'x0'},'y':{'field':'y0'},'x2':{'field':'x1'},'y2':{'field':'y1'},'fill':{'value':'#ece0cc'}}}},
   {'type':'rect','from':{'data':'leaves'},'encode':{'update':{'x':{'field':'x0'},'y':{'field':'y0'},'x2':{'field':'x1'},'y2':{'field':'y1'},'fill':{'signal':"datum.id === '0' ? '#174a67' : '#d6b47b'"},'stroke':{'signal':"datum.id === '0' ? '#f7f5ef' : '#233942'"},'strokeWidth':{'signal':"datum.id === '0' ? 1.5 : datum.y1-datum.y0 > 3 ? 1 : 0"},'tooltip':{'signal':"datum.label + ': ' + format(datum.value, ',') + ' businesses'"}}}},
   {'type':'rect','from':{'data':'groups'},'encode':{'update':{'x':{'signal':'datum.x0-1.5'},'y':{'signal':'datum.y0-1.5'},'x2':{'signal':'datum.x1+1.5'},'y2':{'signal':'datum.y1+1.5'},'fillOpacity':{'value':0},'stroke':{'value':INK},'strokeWidth':{'value':2}}}},
   {'type':'text','encode':{'update':{'x':{'value':5},'y':{'value':17},'text':{'value':'Agricultural businesses'},'fill':{'value':INK},'fontSize':{'signal':'width < 600 ? 11 : 13'}}}},
   {'type':'text','from':{'data':'groups'},'encode':{'update':{'x':{'signal':'(datum.x0+datum.x1)/2'},'y':{'signal':'datum.y0+11'},'text':{'signal':"width >= 600 ? ['With','employees'] : ''"},'lineHeight':{'value':12},'align':{'value':'center'},'fill':{'value':INK},'fontSize':{'value':12}}}},
   {'type':'text','from':{'data':'leaves'},'encode':{'update':{'x':{'signal':'(datum.x0+datum.x1)/2'},'y':{'signal':'(datum.y0+datum.y1)/2 - 8'},'text':{'signal':"datum.id === '0' ? 'No employees' : ''"},'align':{'value':'center'},'fill':{'value':BG},'fontSize':{'signal':'width < 600 ? 12 : 16'}}}},
   {'type':'text','from':{'data':'leaves'},'encode':{'update':{'x':{'signal':'(datum.x0+datum.x1)/2'},'y':{'signal':'(datum.y0+datum.y1)/2 + 17'},'text':{'signal':"datum.id === '0' ? format(datum.value, ',') : ''"},'align':{'value':'center'},'fill':{'value':BG},'fontSize':{'value':18},'fontWeight':{'value':600}}}},
   {'type':'text','encode':{'update':{'x':{'signal':'width*0.62'},'y':{'value':28},'text':{'value':'With employees'},'fill':{'value':INK},'fontSize':{'signal':'width < 600 ? 12 : 15'},'fontWeight':{'value':600}}}},
   {'type':'path','from':{'data':'employing'},'encode':{'update':{'path':{'field':'leader'},'stroke':{'value':MUTED},'strokeWidth':{'value':1},'fillOpacity':{'value':0}}}},
   {'type':'symbol','from':{'data':'employing'},'encode':{'update':{'x':{'field':'x1'},'y':{'field':'source_y'},'size':{'value':15},'fill':{'value':INK}}}},
   {'type':'text','from':{'data':'employing'},'encode':{'update':{'x':{'signal':'datum.label_x+7'},'y':{'signal':'datum.label_y-5'},'text':{'signal':"width < 600 && datum.id === '4' ? ['200 or more','employees'] : datum.label"},'lineHeight':{'value':14},'fill':{'value':INK},'fontSize':{'signal':'width < 600 ? 12 : 14'}}}},
   {'type':'text','from':{'data':'employing'},'encode':{'update':{'x':{'signal':'datum.label_x+7'},'y':{'signal':"datum.label_y + (width < 600 && datum.id === '4' ? 38 : 16)"},'text':{'signal':"format(datum.value, ',') + ' businesses'"},'fill':{'value':INK},'fontSize':{'signal':'width < 600 ? 12 : 15'},'fontWeight':{'value':600}}}}
  ]}

 save(11,'Most businesses have no employees','SMALL TEAMS, MANY OWNERS',f'About {emp[1]["value"]/published*100:.1f}% of the derived agriculture-business total is non-employing.','The outlined group contains businesses with employees, divided by staff count. Area counts businesses, not workers. Owners and family may still work without employees. Blue shows businesses without employees; gold shows businesses with employees. Leader lines name all four staff-size groups, including the smallest. Bin sum '+f'{totalbins:,}'+', versus published-class total sum '+f'{published:,}'+': the difference reflects confidentiality adjustments.',BIZ,'June 2025',s,[r for r in emp[1:] if r['id']!='with-employees'],[['label','Employment-size class'],['value','Businesses']],'Treemap')
 # 12: annual averages only; keep the latest quarterly estimate explicitly in the note.
 er=[]
 for r in rows('agriculture_employment.csv'):
  desc=r['description'].replace('>','').strip()
  if desc=='Agriculture ;  Employed total ;  Persons ;':er.append(dict(date=r['date'],workers=float(r['workers_thousands']),year=int(r['date'][:4])))
 annual=defaultdict(list)
 for r in er:annual[r['year']].append(r['workers'])
 av=[dict(year=y,workers=statistics.mean(v)) for y,v in sorted(annual.items()) if len(v)==4]
 for r in av:r['label']=f"{r['workers']:.0f},000"
 s=vl(300);s['data']={'values':av};s['encoding']={'x':{'field':'year','type':'quantitative','scale':{'domain':[1999,2026],'nice':False,'zero':False},'axis':{'title':None,'values':[2000,2005,2010,2015,2020,2025],'format':'d','grid':False}},'y':{'field':'workers','type':'quantitative','scale':{'domain':[0,400],'zero':True,'nice':False},'axis':{'title':'Workers (thousands)','values':[0,100,200,300,400],'grid':True}},'tooltip':tooltip([('year','d'),('workers','.1f')])}
 s['layer']=[{'mark':{'type':'line','color':TEAL,'strokeWidth':3.5,'strokeCap':'round'}},{'transform':[{'filter':'datum.year === 2000 || datum.year === 2025'}],'mark':{'type':'point','filled':True,'color':TEAL,'size':75,'stroke':BG,'strokeWidth':2}},{'transform':[{'filter':'datum.year === 2000 || datum.year === 2025'}],'mark':{'type':'text','fontSize':14,'fontWeight':600,'color':TEAL,'align':{'expr':"datum.year === 2000 ? 'left' : 'right'"},'dx':{'expr':"datum.year === 2000 ? 12 : -12"},'dy':{'expr':"datum.year === 2000 ? -18 : 22"}},'encoding':{'text':{'field':'label'}}}]
 save(12,'A smaller agricultural workforce','THE LONG VIEW · ANNUAL AVERAGES',f'The annual average fell from {av[0]["workers"]:.0f},000 in {av[0]["year"]} to {av[-1]["workers"]:.0f},000 in {av[-1]["year"]}.','One point per complete year; the vertical axis starts at zero. The latest quarter is separate: about 245,900 workers in February 2026. This counts the agriculture industry, not just the farmer occupation.',LF,'2000–2025 · complete-year averages',s,av,[['year','Complete year'],['workers','Annual average workers (thousands)']],'Time-series line chart')
 (ROOT/'assets/charts.json').write_text(json.dumps(META,indent=2)+'\n')
 print('Generated 12 specifications, metadata and accessible data tables.')
if __name__=='__main__':main()
