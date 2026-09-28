#!/usr/bin/env python3
"""Bounded exact tests of the proved all-rank class-seven kernel classification."""
import json,random
from pathlib import Path
from itertools import combinations
from sympy import Matrix
from n8_central import Magnus,add,bracket

SEED=9282622
rng=random.Random(SEED)
out=Path('research/certificates/N8-class7-all-rank')
out.mkdir(parents=True,exist_ok=True)
assert not (out/'kernels.json').exists()
records=[]

def nullspace(columns):
    words=sorted(set().union(*(set(v) for v in columns)))
    return Matrix([[v.get(w,0) for v in columns] for w in words]).nullspace()

def save(row):
    records.append(row)
    (out/'kernels.json').write_text(json.dumps(dict(seed=SEED,records=records),indent=2)+'\n')
    print(json.dumps(row),flush=True)

for rank in (2,3):
    m=Magnus(rank,6)
    basis={d:[m.layer(h['value'],d) for h in m.bydegree[d]] for d in range(1,7)}
    c33=[bracket(m,a,b) for a,b in combinations(basis[3],2)]
    c24=[bracket(m,a,b) for a in basis[2] for b in basis[4]]
    k33,k24,kall=map(lambda c:len(nullspace(c)),(c33,c24,c33+c24))
    assert k33==0 and kall==k33+k24
    save(dict(test='degree6_direct_sum',rank=rank,columns33=len(c33),
              columns24=len(c24),kernel24=k24,intersection=0))
    for case in range(5):
        z=add(basis[1][0],basis[1][-1],rng.choice((-2,-1,1,2)))
        tt={}
        for b in basis[2]:tt=add(tt,b,rng.choice((-2,-1,1,2)))
        dt=bracket(m,z,tt);d=bracket(m,z,dt)
        vv=add({},bracket(m,tt,dt),-1)
        assert add(bracket(m,tt,d),bracket(m,z,vv))=={}
        columns=[bracket(m,u,d) for u in basis[2]]+[bracket(m,z,v) for v in basis[5]]
        kernel=nullspace(columns)
        assert len(kernel)==1
        predicted=m.coordinates(tt,2)+m.coordinates(vv,5)
        pivot=next(i for i,v in enumerate(predicted) if v)
        ratio=kernel[0][pivot]/predicted[pivot]
        assert list(kernel[0])==[ratio*v for v in predicted]
        save(dict(test='classified_nonzero_kernel',rank=rank,case=case,
                  z=m.coordinates(z,1),T=m.coordinates(tt,2),D=m.coordinates(d,4),
                  kernel_dimension=1,predicted=predicted))
        if rank>2:
            perturb=bracket(m,basis[2][0],basis[2][-1])
            for label,other in [('derived_perturbation',add(d,perturb)),('pure_derived',perturb)]:
                cols=[bracket(m,u,other) for u in basis[2]]+[bracket(m,z,v) for v in basis[5]]
                assert not nullspace(cols)
                save(dict(test=label,rank=rank,case=case,kernel_dimension=0))
        # (2,3) first correction: the entire kernel is the Nielsen line.
        c=tt;d3=dt
        cols=[bracket(m,u,d3) for u in basis[3]]+[bracket(m,c,v) for v in basis[4]]
        ker=nullspace(cols);assert len(ker)==1
        predicted=m.coordinates(d3,3)+[0]*len(basis[4])
        pivot=next(i for i,v in enumerate(predicted) if v)
        ratio=ker[0][pivot]/predicted[pivot]
        assert list(ker[0])==[ratio*v for v in predicted]
        save(dict(test='type23_Nielsen_kernel',rank=rank,case=case,kernel_dimension=1))
print('PASS all-rank class7 kernel checks:',len(records))
