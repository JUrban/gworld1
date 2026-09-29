#!/usr/bin/env python3
"""Finite controls and export for independent GAP pair-graph replay."""
import json
from pathlib import Path
from f38_length_envelope import length_envelope

OUT=Path('research/certificates/F38-length-envelope')
OUT.mkdir(parents=True,exist_ok=True)
assert not (OUT/'checks.json').exists(), 'Preserve old evidence'
records=[]
fixtures=[]
negative=[]
comm=(1,2,-1,-2)
lee=(1,1,2,-1,-2)
cases=[
    ('Lee-known-linear',2,(1,),lee,5,'finite',lambda k:k+4),
    ('one-way-constant',2,(1,),comm,5,'finite',lambda k:4),
    ('reverse-direction-no-envelope',2,comm,(1,),5,'negative',None),
    ('primitive-powers-gaps',2,(1,1),(1,1,1),6,'finite',lambda k:3*(k//2)),
    ('below-minimum',2,(1,1),(1,1,1),1,'empty',None),
    ('rank3-powers',3,(1,),(1,1),3,'finite',lambda k:2*k),
    ('Lee-rank3-no-envelope',3,(1,),lee,3,'negative',None),
    ('nonminimal-powers',2,(1,2,1,2),(1,2,1,2,1,2),6,'finite',lambda k:3*(k//2)),
]
for label,rank,u,v,K,kind,expected in cases:
    result=length_envelope(rank,u,v,K,max_states=15000)
    if kind=='negative':
        assert result['status']=='no_finite_global_envelope',label
        negative.append([rank,u,v,'infinite_orbit_witness',result['stabilizer_orbit']['witness'],[]])
    elif kind=='empty':
        assert result['status']=='empty_below_minimum' and all(x is None for x in result['envelope']),label
    else:
        assert result['status']=='finite_envelope_exact_prefix',label
        m=result['minimum']
        assert result['envelope']==[None if k<m else expected(k) for k in range(K+1)],label
        fixtures.append([rank,u,v,K,result['minimum'],result['minimizer'],
                         result['moves'],result['vertices'],result['adjacency'],
                         [-1 if x is None else x for x in result['envelope']],result['exponential_constant']])
    records.append(dict(label=label,result=result))
    (OUT/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
    (OUT/'fixtures.g').write_text('F38EnvelopeFixtures := '+json.dumps(fixtures)+';\n')
    (OUT/'negative-fixtures.g').write_text('F38StabilizerFixtures := '+json.dumps(negative)+';\n')
    print(label,result['status'],result.get('envelope'),len(result.get('vertices',[])),flush=True)
print('PASS F38 LENGTH ENVELOPE: exact finite prefixes; no general linear-bound decision')
