#!/usr/bin/env python3
"""Bounded exact tensor calculation for the class-four extension lead."""
from itertools import permutations, product
from sympy import Matrix

def bracket(a,b):
    out={}
    for u,x in a.items():
        for v,y in b.items():
            out[u+v]=out.get(u+v,0)+x*y
            out[v+u]=out.get(v+u,0)-x*y
    return {w:c for w,c in out.items() if c}

def right_nested(p):
    ans={(p[-1],):1}
    for i in reversed(p[:-1]):ans=bracket({(i,):1},ans)
    return ans

basis=[right_nested(p+(3,)) for p in permutations(range(3))]
coordinates=list(permutations(range(4)))
raw=Matrix([[b.get(w,0) for b in basis] for w in coordinates])
sym=Matrix([[b.get(w,0)+b.get((w[-1],)+w[1:-1]+(w[0],),0) for b in basis] for w in coordinates])
assert raw.rank()==6
print('Multilinear degree-four Lie dimension:',raw.rank())
print('Symmetrized outer-slot map rank:',sym.rank())
print('Kernel:',sym.nullspace())
pivots=sym.T.rref()[1]
print('Independent output coordinates:',[coordinates[i] for i in pivots])
print('Minor:',sym[list(pivots),:])
if len(pivots)==6:print('Determinant:',sym[list(pivots),:].det())
print('PASS degree-four probe completed; this is a calculation, not a claim')
