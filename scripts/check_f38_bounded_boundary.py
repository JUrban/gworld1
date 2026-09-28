#!/usr/bin/env python3
"""Bounded convention checks for a prior F38(c) example and scope boundary.

The universal rank-two bound is imported from Lee, not proved by this sample.
"""
import json,random
from pathlib import Path
from f38_polynomial_identity import word_reduce,cyclic_reduce,substitute

out=Path('research/certificates/F38-bounded-boundary')
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
u=(1,);v=(1,1,2,-1,-2)
seed=9282638;rng=random.Random(seed);records=[]
def inv(w):return tuple(-x for x in reversed(w))
for test in range(96):
    images=[(1,),(2,)]
    for _ in range(test%13):
        a=rng.randrange(2);b=1-a;choice=rng.randrange(5)
        if choice==0:images[a]=inv(images[a])
        elif choice==1:images[0],images[1]=images[1],images[0]
        else:
            other=images[b] if choice<4 else inv(images[b])
            images[a]=tuple(word_reduce(images[a]+other if choice%2 else other+images[a]))
    lengths=[len(cyclic_reduce(substitute(w,images))) for w in [u,v]]
    assert lengths[1]==lengths[0]+4,(images,lengths)
    records.append(dict(kind='rank2_automorphism',images=images,lengths=lengths))
for n in [1,2,3,5,10,25]:
    images=[(1,),(2,)*n]
    lengths=[len(cyclic_reduce(substitute(w,images))) for w in [u,v]]
    assert lengths==[1,2*n+3]
    records.append(dict(kind='rank2_injection',n=n,determinant=n,images=images,lengths=lengths))
    images=[(1,),(2,)+(3,)*n,(3,)]
    lengths=[len(cyclic_reduce(substitute(w,images))) for w in [u,v]]
    assert lengths==[1,2*n+5]
    records.append(dict(kind='rank3_automorphism',n=n,images=images,lengths=lengths))
(out/'checks.json').write_text(json.dumps(dict(seed=seed,u=u,v=v,records=records),indent=2)+'\n')
(out/'fixtures.g').write_text('F38BoundaryU := '+json.dumps(u)+';\n'
    +'F38BoundaryV := '+json.dumps(v)+';\n'
    +'F38BoundaryRows := '+json.dumps([[r['images'],r['lengths']] for r in records])+';\n')
print('PASS F38 bounded scope:',len(records),'word records; rank-two universality is prior')
