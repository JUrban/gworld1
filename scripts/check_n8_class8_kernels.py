#!/usr/bin/env python3
"""Exact bounded checks of the six proposed class-eight kernel lemmas."""
import json, random
from pathlib import Path
from flint import fmpz_mat
from sympy import symbols, binomial, expand_func, simplify
from n8_fast_magnus import Magnus
from n8_central import bracket
from n8_ia_orbits import add

SEED=9282627
rng=random.Random(SEED)
out=Path('research/certificates/N8-class8')
out.mkdir(parents=True,exist_ok=True)
assert not (out/'kernels.json').exists()
records=[];halls={}

r=symbols('r',integer=True,positive=True)
e=(r*r-r)/2;b=(r**3-r)/3;w=(r**4-r*r)/4-e*(e-1)/2
mu6=r*binomial(r+4,5)-binomial(r+5,6)
assert simplify(expand_func((r**6-r**3-r*r+r)/6-mu6
                           -(e*w+b*(b-1)/2+(e**3-e)/3)))==0

def save():
    (out/'kernels.json').write_text(json.dumps(dict(seed=SEED,records=records),indent=2)+'\n')
    (out/'kernel-halls.json').write_text(json.dumps(halls)+'\n')

for rank in [2,3]:
    m=Magnus(rank,7)
    basis={d:[m.layer(h['value'],d) for h in m.bydegree[d]] for d in range(1,8)}
    halls[str(rank)]={str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,8)}
    def combo(d):
        z={}
        for h in rng.sample(basis[d],min(3,len(basis[d]))):
            z=add(z,h,rng.choice([-2,-1,1,2]))
        return z
    def check(label,c,d,p,q,j,expected):
        cols=[bracket(m,u,d) for u in basis[p+j]]+[bracket(m,c,v) for v in basis[q+j]]
        degree=p+q+j
        coordinates=[m.coordinates(x,degree) for x in cols]
        nullity=len(cols)-fmpz_mat(coordinates).rank()
        row=dict(test=label,rank=rank,p=p,q=q,j=j,C=m.coordinates(c,p),
                 D=m.coordinates(d,q),columns=len(cols),nullity=nullity,expected=expected)
        records.append(row);save();print(json.dumps(row),flush=True)
        assert nullity==expected
        if expected==1:
            predicted=m.coordinates(d,p+j)+[0]*len(basis[q+j])
            assert all(sum(v*col[k] for v,col in zip(predicted,coordinates))==0
                       for k in range(len(coordinates[0])))
    for case in range(3):
        z=combo(1)
        check('type13_second',z,combo(3),1,3,2,1)
        if rank==3:
            c=add(basis[2][0],basis[2][1],case+1)
            d=add(basis[2][-1],basis[2][1],-case-1)
            check('type22_second',c,d,2,2,2,0)
        check('type14_second',z,combo(4),1,4,2,0)
        check('type15_first',z,combo(5),1,5,1,0)
        check('type24_first',combo(2),combo(4),2,4,1,0)
        c=add(basis[3][0],basis[3][-1],case+1)
        d=basis[3][-1]
        check('type33_first',c,d,3,3,1,0)
    # Exercise the derived-only branches and the earlier exceptional D.
    z=basis[1][0];t=combo(2)
    dd=bracket(m,z,bracket(m,z,t))
    check('type14_previous_exception',z,dd,1,4,2,0)
    check('type15_derived_only',z,bracket(m,t,bracket(m,z,t)),1,5,1,0)
    if rank==3:
        dd=bracket(m,basis[2][0],basis[2][-1])
        check('type14_derived_only',z,dd,1,4,2,0)
        check('type24_derived_only',basis[2][0],dd,2,4,1,0)
print('PASS N8 class8 kernel checks:',len(records))
