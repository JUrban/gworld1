#!/usr/bin/env python3
"""Exact comparisons for support-component HNF and polynomial membership."""
import json,random
from pathlib import Path
from flint import fmpz_mat
from n8_component_hnf import hermite
from n8_polynomial_lattice import polynomial_system as old
from n8_sparse_polynomial_lattice import polynomial_system as new

seed=9282651;rng=random.Random(seed);records=[]
for case in range(80):
    rows=rng.randrange(1,10);width=rng.randrange(1,11)
    values=[[rng.randrange(-3,4) if (i+j)%3==case%3 else 0
             for j in range(width)] for i in range(rows)]
    rng.shuffle(values)
    order=list(range(width));rng.shuffle(order)
    values=[[row[j] for j in order] for row in values]
    if case%10==0:values=[[0]*width for _ in range(rows)]
    a=fmpz_mat(values);h,u=hermite(a)
    assert h==a.hnf() and h==u*a and abs(u.det())==1
    records.append(dict(matrix=values,H=[[int(v) for v in row] for row in h.tolist()],
                        U=[[int(v) for v in row] for row in u.tolist()]))
poly=[]
for case in range(30):
    rows=rng.randrange(1,5);width=rng.randrange(1,6)
    values=[[rng.randrange(-2,3) if (i+j)%2 else 0 for j in range(width)]
            for i in range(rows)]
    coefficients=[[rng.randrange(-2,3) for _ in range(width)] for _ in range(3)]
    if case%5==0:coefficients=[[0]*width for _ in range(3)]
    a=old(values,coefficients);b=new(values,coefficients)
    assert a['mode']==b['mode'] and a['values']==b['values'] and a['period']==b['period']
    assert a['certificate']['H']==b['certificate']['H']
    poly.append(b['certificate'])
out=Path('research/certificates/N8-class9');assert not (out/'component-hnf.json').exists()
(out/'component-hnf.json').write_text(json.dumps(dict(seed=seed,matrices=records,
                                                    polynomials=poly),indent=2)+'\n')
print('PASS N8 component HNF:',len(records),'normal forms;',len(poly),'polynomial comparisons')
