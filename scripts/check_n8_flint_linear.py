#!/usr/bin/env python3
"""Independent comparisons for the new integer-affine implementation."""
import json,random
from pathlib import Path
from n8_flint_linear import affine_solution
from n8_class5 import affine_solve

SEED=9282624
rng=random.Random(SEED);records=[]
for case in range(80):
    rows=rng.randrange(1,9);cols=rng.randrange(1,10)
    columns=[[rng.randrange(-4,5) for _ in range(rows)] for _ in range(cols)]
    if case%2:
        x=[rng.randrange(-3,4) for _ in range(cols)]
        rhs=[sum(a*c[j] for a,c in zip(x,columns)) for j in range(rows)]
    else:rhs=[rng.randrange(-10,11) for _ in range(rows)]
    h=affine_solution(columns,rhs);s=affine_solve(columns,rhs)
    assert (h is None)==(s is None)
    if h is not None:
        assert len(h[1])==len(s[1])
        assert all(not any(sum(a*c[j] for a,c in zip(v,columns)) for j in range(rows)) for v in h[1])
        # Each independent implementation's complete kernel lattice must
        # contain every basis vector returned by the other.
        for v in h[1]:assert affine_solve(s[1],v) is not None
        for v in s[1]:assert affine_solution(h[1],v) is not None
    records.append(dict(case=case,columns=columns,rhs=rhs,soluble=h is not None))
p=Path('research/certificates/N8-class7-all-rank/linear-comparison.json')
assert not p.exists();p.write_text(json.dumps(dict(seed=SEED,records=records),indent=2)+'\n')
print('PASS FLINT linear comparisons:',len(records))
