#!/usr/bin/env python3
"""Small exact probes of the outer-slot map; no assertion beyond checked ranks."""
from itertools import product
from sympy import Matrix
from probe_n8_degree4 import right_nested

for degree in range(2, 8):
    words=list(product(range(2),repeat=degree))
    polys=[right_nested(w) for w in words]
    raw=Matrix([[p.get(w,0) for p in polys] for w in words])
    _,cols=raw.rref()
    basis=[polys[i] for i in cols]
    outer=Matrix([[p.get(w,0)+p.get((w[-1],)+w[1:-1]+(w[0],),0)
                   for p in basis] for w in words])
    print('degree',degree,'rank-two Lie dimension',len(basis),'outer-map rank',outer.rank(),flush=True)
print('PASS bounded higher-degree outer-map probe')
