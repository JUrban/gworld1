#!/usr/bin/env python3
"""Export recorded JSON certificates as GAP literals; no math calculation."""
import argparse,json
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('--rank',type=int,required=True)
parser.add_argument('--directory',type=Path)
args=parser.parse_args();p=args.directory or Path(f'research/certificates/N8-class8-rank{args.rank}')
def gap(v):
    if v is None:return 'fail'
    if isinstance(v,bool):return str(v).lower()
    if isinstance(v,list):return '['+','.join(map(gap,v))+']'
    if isinstance(v,dict):return 'rec('+','.join(k+':='+gap(x) for k,x in v.items())+')'
    return json.dumps(v)
polys=json.loads((p/'polynomials.json').read_text())
halls=json.loads((p/'halls.json').read_text())
(p/'polynomial-fixtures.g').write_text('N8C8Polynomials := '+gap(polys)+';\n'
                                    +'N8C8Halls := '+gap([halls[str(d)] for d in range(1,9)])+';\n')
print('Exported',len(polys),'polynomial group certificates for rank',args.rank)
