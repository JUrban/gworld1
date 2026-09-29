#!/usr/bin/env python3
"""Serialize retained class-nine certificates to GAP literals; no research."""
import argparse,gzip,json
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument('kind',choices=['kernels','targets'])
parser.add_argument('directory',type=Path)
args=parser.parse_args();p=args.directory
def gap(v):
    if v is None:return 'fail'
    if isinstance(v,bool):return str(v).lower()
    if isinstance(v,list):return '['+','.join(map(gap,v))+']'
    if isinstance(v,dict):return 'rec('+','.join(k+':='+gap(x) for k,x in v.items())+')'
    return json.dumps(v)
halls=json.loads((p/'halls.json').read_text())
data=json.loads((p/'checks.json').read_text())
if args.kind=='kernels':
    output='N8C9KernelData := '+gap(data)+';\n'
    name='kernel-fixtures.g'
else:
    packed=p/'polynomials.json.gz'
    raw=gzip.decompress(packed.read_bytes()).decode() if packed.exists() else (p/'polynomials.json').read_text()
    output='N8C9Polynomials := '+gap(json.loads(raw))+';\n'
    name='polynomial-fixtures.g'
degrees=sorted(map(int,halls))
assert degrees==list(range(1,max(degrees)+1))
output+='N8C9Halls := '+gap([halls[str(d)] for d in degrees])+';\n'
if args.kind=='targets' and (p/'polynomials.json.gz').exists():
    (p/(name+'.gz')).write_bytes(gzip.compress(output.encode(),mtime=0))
else:(p/name).write_text(output)
print('Exported',args.kind,p)
