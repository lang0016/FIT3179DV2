#!/usr/bin/env python3
"""Prepare official ABS state geometry for the page. Originals stay outside Git."""
import argparse,hashlib,json,urllib.request,zipfile
from pathlib import Path
import shapefile
from shapely.geometry import shape,mapping,box,Polygon,MultiPolygon
from shapely.geometry.polygon import orient
from shapely.ops import transform
from shapely.affinity import scale,translate
from pyproj import Transformer
ROOT=Path(__file__).resolve().parents[1]
URL='https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs/edition-3-july-2021-june-2026/access-and-downloads/digital-boundary-files/STE_2021_AUST_SHP_GDA2020.zip'
SHA='d9b7f735de6085b37414faf011f796dda3c7f768c55e9dce01f96e790f399a21'
# Expected hash is persisted in data/map_sources.json by the first verified build.
def main():
 p=argparse.ArgumentParser();p.add_argument('--source-dir',type=Path,required=True);a=p.parse_args();a.source_dir.mkdir(parents=True,exist_ok=True)
 archive=a.source_dir/'states2021.zip';manifest=ROOT/'data/map_sources.json'
 expected=json.loads(manifest.read_text())['sha256'] if manifest.exists() else SHA
 if not archive.exists():archive.write_bytes(urllib.request.urlopen(URL,timeout=90).read())
 raw=archive.read_bytes();digest=hashlib.sha256(raw).hexdigest()
 if expected and digest!=expected:raise ValueError('Boundary source changed; investigate checksum mismatch')
 dest=a.source_dir/'states2021';dest.mkdir(exist_ok=True)
 with zipfile.ZipFile(archive) as z:
  for n in z.namelist():
   if n.endswith(('.shp','.shx','.dbf','.prj')):(dest/Path(n).name).write_bytes(z.read(n))
 r=shapefile.Reader(str(next(dest.glob('*.shp'))));features=[]
 for sr in r.iterShapeRecords():
  props=sr.record.as_dict();code=str(props['STE_CODE21'])
  if code not in list('12345678'):continue
  geom=shape(sr.shape.__geo_interface__).intersection(box(112,-44.2,154.5,-9)).simplify(0.025,preserve_topology=True)
  if isinstance(geom,Polygon):geom=orient(geom,sign=-1)
  elif isinstance(geom,MultiPolygon):geom=MultiPolygon([orient(g,sign=-1) for g in geom.geoms])
  assert geom.is_valid and not geom.is_empty
  coords=json.loads(json.dumps(mapping(geom)),parse_float=lambda x:round(float(x),4))
  features.append({'type':'Feature','properties':{'code':code,'name':props['STE_NAME21']},'geometry':coords})
 assert len(features)==8
 (ROOT/'data/states.geojson').write_text(json.dumps({'type':'FeatureCollection','features':features},separators=(',',':'))+'\n')
 manifest.write_text(json.dumps({'publisher':'Australian Bureau of Statistics','title':'ASGS 2021 States and Territories, GDA2020','url':URL,'sha256':digest,'original_bytes':len(raw),'licence':'CC BY 4.0, subject to ABS exceptions','preparation':'Keep states/territories 1–8; clip display to 112–154.5 E, 44.2–9 S; simplify 0.025 degrees preserving topology; round coordinates to four decimals. Excludes Other Territories and remote islands outside the display extent. Statistical state totals remain unchanged.','projection':'Australia Albers equal-area; cartogram geometry first projected to EPSG:3577 then resized with area proportional to registered dairy farms and relocated for legibility.'},indent=2)+'\n')
 print('Prepared eight valid official state polygons:',(ROOT/'data/states.geojson').stat().st_size,'bytes')
if __name__=='__main__':main()
