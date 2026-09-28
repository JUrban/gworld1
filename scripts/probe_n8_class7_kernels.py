#!/usr/bin/env python3
"""Bounded rational kernel audit for a possible class-seven extension.

No all-rank kernel theorem is inferred from these samples.
"""
import json
import random
from pathlib import Path
from sympy import Matrix
from n8_central import Magnus, add, bracket

SEED = 9282620
rng = random.Random(SEED)
output = Path('research/certificates/N8-class7/kernel-probe.json')
assert not output.exists()
output.parent.mkdir(parents=True, exist_ok=True)
records = []


def kernel(columns):
    words = sorted(set().union(*(set(c) for c in columns)))
    return Matrix([[c.get(w, 0) for c in columns] for w in words]).nullspace()


def save(r):
    records.append(r)
    output.write_text(json.dumps(dict(seed=SEED, records=records), indent=2)+'\n')
    print(json.dumps(r), flush=True)


for rank in (2, 3):
    m = Magnus(rank, 6)
    basis = {d: [m.layer(h['value'], d) for h in m.bydegree[d]] for d in range(1, 6)}
    a = {(0,): 1}
    candidates = [('basis4_'+str(i), d) for i, d in enumerate(basis[4])]
    candidates += [('ad_a_squared_'+str(i), bracket(m, a, bracket(m, a, u)))
                   for i, u in enumerate(basis[2])]
    for i in range(12):
        d = {}
        for j in rng.sample(range(len(basis[4])), min(3, len(basis[4]))):
            d = add(d, basis[4][j], rng.choice([-2, -1, 1, 2]))
        candidates.append(('random_'+str(i), d))
    for name, d in candidates:
        cols = [bracket(m, u, d) for u in basis[2]] + [bracket(m, a, v) for v in basis[5]]
        null = kernel(cols)
        save(dict(rank=rank, case=name, type='1_4_first_correction',
                  D=m.coordinates(d,4), kernel_dimension=len(null),
                  U_components=[[str(x) for x in v[:len(basis[2])]] for v in null]))
    # The spaces [L3,L3] and [L2,L4] should be disjoint. Their
    # individual internal relations are retained, not misread as failures.
    cols23 = [bracket(m,u,v) for i,u in enumerate(basis[3]) for v in basis[3][i+1:]]
    cols24 = [bracket(m,u,v) for u in basis[2] for v in basis[4]]
    n23, n24, ntotal = len(kernel(cols23)),len(kernel(cols24)),len(kernel(cols23+cols24))
    save(dict(rank=rank,type='degree6_bracket_intersection',
              columns_33=len(cols23),columns_24=len(cols24),
              kernel_33=n23,kernel_24=n24,kernel_combined=ntotal,
              intersection_dimension=ntotal-n23-n24))
print('PASS bounded class-seven kernel probe')
