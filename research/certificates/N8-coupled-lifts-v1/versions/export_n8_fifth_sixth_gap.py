#!/usr/bin/env python3
"""Serialize retained audit records for an independent GAP replay."""
import argparse,gzip,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('directory',type=Path);a=p.parse_args();out=a.directory
assert not (out/'polynomial-fixtures.g.gz').exists()
def gap(v):
 if v is None:return 'fail'
 if isinstance(v,bool):return str(v).lower()
 if isinstance(v,list):return '['+','.join(map(gap,v))+']'
 if isinstance(v,dict):return 'rec('+','.join(k+':='+gap(x) for k,x in v.items())+')'
 return json.dumps(v)
audit=json.loads(gzip.decompress((out/'audit.json.gz').read_bytes()))
data=json.loads((out/'checks.json').read_text());h=json.loads((out/'halls.json').read_text())
steps=[[r['rank'],r['degree'],r['word'],r['x'],r['y'],r['axes'],r['soluble']]
       for r in audit if r['kind'] in ('layer','tail')]
witnesses=json.loads((out/'witnesses.json').read_text())
(out/'fixtures.g').write_text('N8C9Witnesses := '+gap(witnesses)+';\nN8C9Steps := '+gap(steps)+';\n')
text='N8C9Halls := '+gap([h[str(i)] for i in range(1,data['degree']+1)])+';\n'
for variable,kinds in [('N8C9Polynomials',('polynomial','polynomial_late')),
                       ('N8NewCoupled',('coupled',)),('N8NewNielsen',('nielsen',)),
                       ('N8NewNullities',('nullity',))]:
 text+=variable+' := '+gap([r for r in audit if r['kind'] in kinds])+';\n'
(out/'polynomial-fixtures.g.gz').write_bytes(gzip.compress(text.encode(),mtime=0))
driver='N8C9Directory := '+gap(str(out))+';;\nRead("scripts/check_n8_fifth_sixth_gap_core.g");\n'
(out/'check.g').write_text(driver)
for name in ['export_n8_fifth_sixth_gap.py','check_n8_fifth_sixth_gap_core.g',
             'n8_gap_hall_cache.g','n8_gap_integer_components.g']:
 src=Path('scripts')/name;(out/'versions'/name).write_bytes(src.read_bytes())
print('Exported',out,len(witnesses),'witnesses;',len(steps),'linear steps')
