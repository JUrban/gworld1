#!/usr/bin/env python3
"""Targeted N5 audit: composite congruences and dependent relator defects.

The rank-two finite-ring oracle is separate from the integral stabilizer
enumeration. Finite central extensions are checked by enumerating changes
of lifts directly, without Smith transformations.
"""
import json
from itertools import product
from pathlib import Path
from sympy import Matrix
from n5_central_constraints import split, satisfies, relation_constraints, lifting_corrections

OUT = Path('research/certificates/N5-integrality')
OUT.mkdir(parents=True, exist_ok=True)
assert not (OUT / 'checks.json').exists()
records, fixtures, lift_records = [], [], []


def matrix_list(a):
    return [[int(x) for x in a.row(i)] for i in range(a.rows)]


def rank_mod_prime(a, p):
    aa, bb, cc, dd = (x % p for x in a)
    if (aa * dd - bb * cc) % p:
        return 2
    return int(any((aa, bb, cc, dd)))


def ring_oracle(constraints, modulus, primes, nontrivial):
    """Enumerate all 2x2 idempotents; retain constant local rank.

    For Z/4 and Z/6, a constant-rank idempotent is conjugate to a
    standard projector by an SL_2 matrix, hence lifts over Z. The
    mathematical justification is recorded in the accompanying audit.
    """
    arbitrary, liftable = [], []
    for a, b, c, d in product(range(modulus), repeat=4):
        if any(x % modulus for x in
               (a*a+b*c-a, a*b+b*d-b, c*a+d*c-c, c*b+d*d-d)):
            continue
        ok = True
        for side, (x, y), m in constraints:
            px, py = a*x+b*y, c*x+d*y
            rx, ry = (x-px, y-py) if side == 1 else (px, py)
            if rx % m or ry % m:
                ok = False
                break
        if not ok:
            continue
        ranks = [rank_mod_prime((a,b,c,d), p) for p in primes]
        arbitrary.append([[a,b],[c,d]])
        if len(set(ranks)) == 1 and (not nontrivial or ranks[0] == 1):
            liftable.append([[a,b],[c,d]])
    return arbitrary, liftable


def check(label, n, orders, constraints, expected, require=(True,True), oracle=None):
    p = split(n, orders, constraints, require)
    assert (p is not None) == expected, (label, p)
    record = dict(label=label, n=n, orders=orders, constraints=constraints,
                  require_nontrivial=require, expected=expected,
                  projection=None if p is None else matrix_list(p))
    if oracle:
        modulus, primes = oracle
        arbitrary, liftable = ring_oracle(constraints, modulus, primes, all(require))
        assert bool(liftable) == expected, (label, liftable)
        record.update(modulus=modulus, arbitrary_ring_projectors=len(arbitrary),
                      constant_rank_projectors=len(liftable),
                      first_ring_projector=arbitrary[0] if arbitrary else None)
    if p is not None:
        fixtures.append([[0]*n+orders, matrix_list(p), constraints, list(map(int,require))])
    records.append(record)
    print(json.dumps(record), flush=True)


check('rank two at 2, rank zero at 3 cannot lift', 2, [],
      [(1,[1,0],2),(1,[0,1],2),(2,[1,0],3),(2,[0,1],3)], False,
      require=(False,False), oracle=(6,[2,3]))
assert records[-1]['arbitrary_ring_projectors'] == 1
check('rank one at 2, rank two at 3 cannot lift', 2, [],
      [(1,[1,0],2),(2,[0,1],2),(1,[1,0],3),(1,[0,1],3)], False,
      require=(False,False), oracle=(6,[2,3]))
assert records[-1]['arbitrary_ring_projectors'] == 1
check('crossed CRT directions lift integrally', 2, [],
      [(1,[1,0],2),(2,[0,1],2),(1,[0,1],3),(2,[1,0],3)], True,
      oracle=(6,[2,3]))
check('prime-power primitive direction', 2, [],
      [(1,[1,2],4),(2,[0,1],4)], True, oracle=(4,[2]))
check('prime-power nonzero vector forced into both factors', 2, [],
      [(1,[2,0],4),(2,[2,0],4)], False, oracle=(4,[2]))
check('exact forced summands and incompatible complement ranks', 3, [],
      [(1,[1,0,0],0),(2,[0,1,0],0),(1,[0,0,1],2),(2,[0,0,1],3)], False)
check('exact forced summands and integral complement shear', 3, [],
      [(1,[1,0,0],0),(2,[0,1,0],0),(1,[0,1,1],6)], True)
check('mixed free and composite torsion shear', 1, [6],
      [(1,[1,1],0),(2,[0,2],0)], True)
check('mixed centre parity obstruction', 1, [6],
      [(1,[2,1],0),(2,[0,3],0)], False)
check('torsion cannot repair incompatible free ranks', 1, [6],
      [(1,[1,0],2),(2,[1,0],3)], False, require=(False,False))

# Direct finite lift enumeration is independent of the Smith algorithm.
orders=[4,6]
elements=list(product(range(4),range(6)))
p=Matrix([[1,0],[0,0]])
cases=[
    ([[2,4],[-3,-6],[4,8]], [[1,2],[3,3],[2,4]], 1),
    ([[2,4],[-3,-6],[4,8]], [[1,2],[3,3],[2,4]], 2),
    ([[2,4],[-3,-6],[4,8]], [[1,2],[3,3],[2,5]], 1),
    ([[2,4],[-3,-6],[4,8]], [[2,0],[3,0],[0,0]], 2),
    ([[-2,1],[4,-2],[0,3]], [[1,1],[2,4],[0,3]], 1),
    ([[-2,1],[4,-2],[0,3]], [[1,1],[2,4],[0,3]], 2),
    ([[0,0],[6,0],[-3,0]], [[0,0],[0,0],[0,3]], 1),
    ([[0,0],[6,0],[-3,0]], [[0,2],[0,0],[0,3]], 1),
]
for i,(e,defects,side) in enumerate(cases,1):
    surviving=1 if side==1 else 0
    modulus=orders[surviving]
    witness=None
    for zs in product(elements,repeat=2):
        if all((v[surviving]+sum(row[j]*zs[j][surviving] for j in range(2)))%modulus==0
               for row,v in zip(e,defects)):
            witness=zs
            break
    cc=relation_constraints(e,defects,0,orders,side)
    accepted=satisfies(p,0,orders,cc)
    assert accepted==(witness is not None), (i,e,defects,cc)
    corrections=lifting_corrections(e,defects,2,0,orders,side,p) if accepted else []
    if accepted:
        assert all((v[surviving]+sum(row[j]*corrections[j][surviving] for j in range(2)))%modulus==0
                   for row,v in zip(e,defects))
    lift_records.append([orders,e,defects,side,matrix_list(p),int(accepted),corrections])
    print(json.dumps(dict(relator_case=i,accepted=accepted)),flush=True)

(OUT/'checks.json').write_text(json.dumps(dict(splittings=records,lift_records=lift_records),indent=2)+'\n')
(OUT/'fixtures.g').write_text('N5IntegrityFixtures := '+json.dumps(fixtures)+';\nN5LiftFixtures := '+json.dumps(lift_records)+';\n')
print('PASS N5 integrality audit:',len(records),'splitting cases;',len(lift_records),'relator systems;',len(fixtures),'positive projections')
