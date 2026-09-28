#!/usr/bin/env python3
"""Independent finite-subgroup oracle, modular oracle and integral controls."""
import json,random
from itertools import product
from pathlib import Path
from sympy import Matrix
from n5_central_constraints import split,relation_constraints

seed=9282613;rng=random.Random(seed);records=[];fixtures=[]
out=Path(__file__).resolve().parents[1]/'research/certificates/N5-central'
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()

def check(n,orders,cc,expected,label,require=(True,True)):
    answer=split(n,orders,cc,require)
    assert (answer is not None)==expected,(n,orders,cc,label,answer)
    if answer is not None:
        fixtures.append([[0]*n+list(orders),[[int(x) for x in answer.row(i)] for i in range(answer.rows)],cc,list(map(int,require))])
    records.append(dict(n=n,orders=orders,constraints=cc,expected=expected,label=label,
                        projection=None if answer is None else fixtures[-1][1]))
    (out/'checks.json').write_text(json.dumps(dict(seed=seed,records=records),indent=2)+'\n')
    (out/'fixtures.g').write_text('N5Fixtures := '+json.dumps(fixtures)+';\n')
    print(json.dumps(dict(case=len(records),label=label,answer=expected)),flush=True)

for n,orders,cc,expected,label in [
    (2,[],[(1,[2,0],0),(2,[0,3],0)],True,'saturated separated free lattices'),
    (2,[],[(1,[1,0],0),(2,[1,2],0)],False,'nonprimitive combined lattice'),
    (2,[],[(1,[1,0],0),(2,[1,0],0)],False,'intersecting forced lattices'),
    (2,[],[(1,[1,0],2),(2,[0,1],2)],True,'congruence split'),
    (2,[],[(1,[1,0],2),(2,[1,0],2)],False,'contradictory congruences'),
    (1,[2],[(1,[1,1],0),(2,[0,1],0)],True,'torsion shear required'),
    (1,[4],[(1,[2,1],0),(2,[0,2],0)],False,'torsion shear obstruction'),
    (0,[4],[],False,'cyclic prime-power indecomposable'),
    (0,[6],[],True,'coprime cyclic factors'),
    (0,[2,2],[],True,'elementary abelian factors'),
    (1,[],[],False,'infinite cyclic indecomposable'),
    (2,[],[],True,'free abelian rank two'),
]:check(n,orders,cc,expected,label)

# Enumerate subgroups as element sets, without endomorphism matrices.
def finite_splits(orders):
    elements=set(product(*(range(d) for d in orders)));zero=tuple(0 for d in orders)
    def plus(a,b):return tuple((x+y)%d for x,y,d in zip(a,b,orders))
    seen={frozenset([zero])};queue=list(seen)
    for h in queue:
        for x in elements-set(h):
            span=set(h);power=zero
            while True:
                power=plus(power,x)
                if power in h:break
                span.update(plus(y,power) for y in h)
            span=frozenset(span)
            if span not in seen:seen.add(span);queue.append(span)
    return elements,[(a,b) for a in seen for b in seen if len(a)>1 and len(b)>1
                     and len(a)*len(b)==len(elements) and len(a&b)==1],plus

for orders in ([4],[6],[2,2],[2,4],[3,3]):
    elements,pairs,plus=finite_splits(orders)
    for case in range(12):
        cc=[(rng.choice((1,2)),list(rng.choice(sorted(elements))),rng.choice((0,2,3,4))) for _ in range(3)]
        expected=False
        for a,b in pairs:
            if all(tuple(v) in {plus(x,tuple(d*y[i]%orders[i] for i in range(len(orders))))
                              for x in (a if side==1 else b) for y in elements} for side,v,d in cc):
                expected=True;break
        check(0,orders,cc,expected,'finite subgroup-set oracle')

# With only congruences modulo p, every projector over F_p lifts to an
# integral direct splitting: choose bases for image/kernel and rescale one
# column to determinant 1, then lift SL_n(F_p) elementary generators.
for n,p in ((2,2),(2,3),(3,2)):
    projectors=[]
    identity=Matrix.eye(n)
    for entries in product(range(p),repeat=n*n):
        q=Matrix(n,n,entries)
        if all(int(x)%p==0 for x in q*q-q) and any(q) and any(int(x)%p for x in identity-q):
            projectors.append(q)
    for case in range(15):
        cc=[(rng.choice((1,2)),[rng.randrange(p) for _ in range(n)],p) for _ in range(3)]
        expected=any(all(all(int(x)%p==0 for x in (identity-q if side==1 else q)*Matrix(v))
                         for side,v,d in cc) for q in projectors)
        check(n,[],cc,expected,'independent modular-projector oracle')

# Relator Smith reduction retains torsion constraints and zero rows.
cc=relation_constraints([[2]],[[1]],0,[2],1)
check(0,[2],cc,False,'nonsplit cyclic central extension',require=(False,True))
cc=relation_constraints([[2]],[[0]],0,[2],1)
check(0,[2],cc,True,'split cyclic central extension',require=(False,True))
cc=relation_constraints([[2,4],[1,2]],[[2,0],[1,1]],2,[],1)+[(2,[0,1],0)]
check(2,[],cc,False,'dependent relators retain central obstruction')

print('PASS N5 central constraints:',len(records),'cases;',len(fixtures),'positive projections')
