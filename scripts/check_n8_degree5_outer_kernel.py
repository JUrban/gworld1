#!/usr/bin/env python3
"""Produce an exact rational degree-five obstruction to full outer injectivity."""
from itertools import permutations
from pathlib import Path
from sympy import Matrix, ilcm
import json
def nested(word):
    if len(word)==1:return {word:1}
    out={}
    for w,c in nested(word[1:]).items():
        for t,a in [((word[0],)+w,c),(w+(word[0],),-c)]:out[t]=out.get(t,0)+a
    return {w:c for w,c in out.items() if c}
n=5;words=list(permutations(range(n)));basis=[p+(n-1,) for p in permutations(range(n-1))]
polys=[nested(p) for p in basis]
outer=Matrix([[p.get(w,0)+p.get((w[-1],)+w[1:-1]+(w[0],),0) for p in polys] for w in words])
kernel=outer.nullspace();assert len(kernel)==4
v=kernel[0];den=ilcm(*[x.q for x in v]);v=[int(x*den) for x in v]
g={}
for p,a in zip(polys,v):
 for w,c in p.items():g[w]=g.get(w,0)+a*c
g={w:c for w,c in g.items() if c}
assert g and all(g.get(w,0)+g.get((w[-1],)+w[1:-1]+(w[0],),0)==0 for w in words)
record={'degree':5,'basis_convention':'right-nested, final generator 4, indices 0..4',
 'rational_rank':24-len(kernel),'kernel_dimension':len(kernel),
 'witness_brackets':[{'word':list(w),'coefficient':a} for w,a in zip(basis,v) if a],
 'witness_tensor_terms':[{'word':list(w),'coefficient':c} for w,c in sorted(g.items())]}
path=Path('research/certificates/N8-degree5-outer-kernel.json')
assert not path.exists();path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
print('PASS N8 degree-five rational outer-map kernel')
