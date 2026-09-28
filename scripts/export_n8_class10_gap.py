#!/usr/bin/env python3
"""Serialize complete class-ten group records to GAP; no mathematics."""
import argparse,gzip,json
from pathlib import Path
def gap(v):
    if v is None:return 'fail'
    if isinstance(v,bool):return str(v).lower()
    if isinstance(v,list):return '['+','.join(map(gap,v))+']'
    if isinstance(v,dict):return 'rec('+','.join(k+':='+gap(x) for k,x in v.items())+')'
    return json.dumps(v)
p=argparse.ArgumentParser();p.add_argument('directory',type=Path);a=p.parse_args()
h=json.loads((a.directory/'halls.json').read_text())
for name,variable in [('polynomials','N8C9Polynomials'),('coupled','N8C10Coupled')]:
    data=json.loads(gzip.decompress((a.directory/(name+'.json.gz')).read_bytes()))
    text=variable+' := '+gap(data)+';\n'
    if name=='polynomials':text+='N8C9Halls := '+gap([h[str(i)] for i in range(1,11)])+';\n'
    target=a.directory/('polynomial-fixtures.g.gz' if name=='polynomials' else 'coupled-fixtures.g.gz')
    assert not target.exists();target.write_bytes(gzip.compress(text.encode(),mtime=0))
print('Exported',a.directory)
