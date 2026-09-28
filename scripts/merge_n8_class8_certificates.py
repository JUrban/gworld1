#!/usr/bin/env python3
"""Merge disjoint saved target records; this performs no new group decision."""
import argparse,hashlib,json
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('sources',nargs='+',type=Path)
parser.add_argument('--directory',required=True,type=Path);args=parser.parse_args()
records=[];witnesses=[];steps=[];polynomials=[];halls=None;provenance=[];seen=set()
for source in args.sources:
    paths=[source/name for name in ['checks.json','polynomials.json','fixtures.g','halls.json']]
    provenance.append(dict(directory=str(source),sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}))
    checks=json.loads(paths[0].read_text());assert checks['rank']==3
    for record in checks['records']:
        key=tuple(record['word']);assert key not in seen,'overlapping target records'
        seen.add(key);records.append(record)
    polynomials+=json.loads(paths[1].read_text())
    fixtures={}
    for line in paths[2].read_text().splitlines():
        name,value=line.split(' := ',1);assert value.endswith(';')
        fixtures[name]=json.loads(value[:-1])
    witnesses+=fixtures['N8C8Witnesses'];steps+=fixtures['N8C8Steps']
    new_halls=json.loads(paths[3].read_text())
    if halls is None:halls=new_halls
    else:assert halls==new_halls
out=args.directory;out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
(out/'checks.json').write_text(json.dumps(dict(rank=3,seed=None,sources=provenance,records=records),indent=2)+'\n')
(out/'polynomials.json').write_text(json.dumps(polynomials,indent=2)+'\n')
(out/'fixtures.g').write_text('N8C8Witnesses := '+json.dumps(witnesses)+';\n'
                            +'N8C8Steps := '+json.dumps(steps)+';\n')
(out/'halls.json').write_text(json.dumps(halls)+'\n')
print('Merged saved records:',len(records),'targets;',len(witnesses),'witnesses;',len(steps),'linear steps;',len(polynomials),'polynomial branches')
