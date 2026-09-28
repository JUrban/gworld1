#!/usr/bin/env python3
"""Check the new quadratic-cokernel obstruction and HNF polynomial arithmetic."""
import json, random
from pathlib import Path
from flint import fmpz_mat
from n8_fast_magnus import Magnus
from n8_central import bracket
from n8_ia_orbits import add
from n8_polynomial_lattice import polynomial_system,evaluate
from n8_class7 import polynomial_lattice

SEED=9282628
rng=random.Random(SEED)
out=Path('research/certificates/N8-class8');out.mkdir(parents=True,exist_ok=True)
assert not (out/'obstruction.json').exists()
records=[];arithmetic=[]
for rank in [2,3]:
    m=Magnus(rank,7)
    for case in range(4):
        z=add(m.layer(m.bydegree[1][0]['value'],1),
              m.layer(m.bydegree[1][-1]['value'],1),case+1)
        t={}
        for h in m.bydegree[2]:t=add(t,m.layer(h['value'],2),rng.choice([-2,-1,1,2]))
        d=bracket(m,z,bracket(m,z,t))
        q=bracket(m,t,bracket(m,t,bracket(m,z,t)))
        cols=[bracket(m,m.layer(h['value'],3),d) for h in m.bydegree[3]]
        cols += [bracket(m,z,m.layer(h['value'],6)) for h in m.bydegree[6]]
        matrix=[m.coordinates(c,7) for c in cols]
        r1=fmpz_mat(matrix).rank();r2=fmpz_mat(matrix+[m.coordinates(q,7)]).rank()
        assert r1==len(cols) and r2==r1+1
        records.append(dict(rank=rank,z=m.coordinates(z,1),T=m.coordinates(t,2),
                            D=m.coordinates(d,4),Q=m.coordinates(q,7),ranks=[r1,r2]))
for case in range(40):
    rows=rng.randrange(1,5);n=rng.randrange(1,5)
    cols=[[rng.randrange(-3,4) for _ in range(rows)] for _ in range(n)]
    coeff=[[rng.randrange(-4,5) for _ in range(rows)] for _ in range(3)]
    old,oldcert=polynomial_lattice(cols,coeff)
    new=polynomial_system(cols,coeff)
    assert (old is not None)==bool(new['values'])
    if old is not None:
        if new['mode']=='finite_points':assert old in new['values']
        else:assert old%new['period'] in new['values']
    arithmetic.append(new['certificate'])
(out/'obstruction.json').write_text(json.dumps(dict(seed=SEED,records=records,
                                                  arithmetic=arithmetic),indent=2)+'\n')
print('PASS N8 class8 quadratic obstruction:',len(records),'kernels;',len(arithmetic),'arithmetic comparisons')
