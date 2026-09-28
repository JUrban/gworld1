#!/usr/bin/env python3
"""Export the completion-kernel probe records to the existing GAP replay."""
import argparse,json
from pathlib import Path

def gap(v):
    if v is None:return 'fail'
    if isinstance(v,bool):return str(v).lower()
    if isinstance(v,list):return '['+','.join(map(gap,v))+']'
    if isinstance(v,dict):return 'rec('+','.join(k+':='+gap(x) for k,x in v.items())+')'
    return json.dumps(v)

p=argparse.ArgumentParser();p.add_argument('directory',type=Path);a=p.parse_args()
data=json.loads((a.directory/'checks.json').read_text())
for row in data['records']:
    row['j']=row['offset']
    if 'direction' in row:row['predicted_direction']=row['direction']
data['obstructions']=[]
halls=json.loads((a.directory/'halls.json').read_text())
target=a.directory/'kernel-fixtures.g';assert not target.exists()
target.write_text('N8C9KernelData := '+gap(data)+';\nN8C9Halls := '
                  +gap([halls[str(i)] for i in range(1,10)])+';\n')
print('Exported',target)
