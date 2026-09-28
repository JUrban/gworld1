#!/usr/bin/env python3
"""Compare direct tail columns with full group commutators in bounded cases."""
import json,random
from pathlib import Path
from n8_multigraded_magnus import Magnus
from n8_class7 import tail_axes,tail_columns as old_columns,apply_tail
from n8_class9_tail import tail_columns
from n8_ia_orbits import add,ONE

seed=9282647;rng=random.Random(seed);records=[]
for rank,degree in [(2,9),(3,8)]:
    m=Magnus(rank,degree)
    for p,q,start in [(1,2,4),(1,3,3),(2,2,3),(2,3,3),(1,4,3),(1,5,2),(2,4,2),(3,3,2),(1,6,2),(2,5,2),(3,4,2)]:
        if p+q+start>degree or p==q==2 and rank==2:continue
        x=m.bydegree[p][0]['value'];y=m.bydegree[q][-1]['value']
        if p+1<=degree:x=m.mul(x,m.bydegree[p+1][0]['value'])
        if q+1<=degree:y=m.mul(y,m.bydegree[q+1][-1]['value'])
        axes=tail_axes(m,p,q,start)
        sampled=rng.sample(axes,min(6,len(axes)))
        direct=tail_columns(m,x,y,sampled,p,q)
        old=old_columns(m,x,y,sampled)
        assert direct==old,(rank,degree,p,q,start)
        vector=[rng.choice([-2,-1,0,1,2]) for _ in sampled]
        changed=apply_tail(m,x,y,sampled,vector)
        residual=add(m.mul(m.inv(m.comm(x,y)),m.comm(*changed)),ONE,-1)
        expected={}
        for n,col in zip(vector,direct):expected=add(expected,col,n)
        assert residual==expected
        records.append(dict(rank=rank,degree=degree,p=p,q=q,start=start,
                            columns=len(sampled),vector=vector))
out=Path('research/certificates/N8-class9')
assert not (out/'tail-check.json').exists()
(out/'tail-check.json').write_text(json.dumps(dict(seed=seed,records=records),indent=2)+'\n')
print('PASS N8 class9 direct tails:',len(records),'fixtures')
