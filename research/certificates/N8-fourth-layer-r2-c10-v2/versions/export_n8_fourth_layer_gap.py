#!/usr/bin/env python3
"""Export retained records and extra independent checks; no new decisions."""
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
data=json.loads((out/'checks.json').read_text());c=data['degree'];rank=data['rank']
halls=json.loads((out/'halls.json').read_text())
polys=json.loads(gzip.decompress((out/'polynomials.json.gz').read_bytes()))
text='N8C9Polynomials := '+gap(polys)+';\nN8C9Halls := '+gap([halls[str(i)] for i in range(1,c+1)])+';\n'
(out/'polynomial-fixtures.g.gz').write_bytes(gzip.compress(text.encode(),mtime=0))
raw=(out/'fixtures.g').read_text();steps=json.loads(raw.split('N8C9Steps := ',1)[1].rsplit(';',1)[0])
firsts=[row for row in steps if row[1]==c-2 and row[6]]
expected=[(rec['word'],branch['first_kernel_dimension']) for rec in data['records']
          for branch in rec['result']['trace'] if branch['first_soluble']]
assert len(firsts)==len(expected)
first_maps=[]
for row,(word,dim) in zip(firsts,expected):
 assert row[2]==word
 first_maps.append([rank,c-2,row[3],row[4],row[5],dim])
scope=[]
(out/'extra-fixtures.g').write_text('N8Type1FirstMaps := '+gap(first_maps)+';\nN8Type1Scopes := '+gap(scope)+';\n')
(out/'nielsen-fixtures.g').write_text('N8NielsenLines := '+gap(json.loads((out/'nielsen.json').read_text()))+';\n')
print('Exported',len(first_maps),'first maps;',len(scope),'higher-type scope checks;',len(polys),'polynomials')
