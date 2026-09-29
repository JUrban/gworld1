#!/usr/bin/env python3
"""Bounded exact audit of a different central-factor decision procedure."""
import json
from pathlib import Path

from sympy import symbols

from n8_central import Magnus, mixed_type
from n8_projective_factors import add, all_mixed_factors, bracket, rational_points

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/certificates/N8-projective-factors'
OUT.mkdir(parents=True, exist_ok=True)
assert not (OUT / 'checks.json').exists(), 'Preserve earlier evidence'
records = []
fixtures = []


def save():
    (OUT / 'checks.json').write_text(json.dumps(records, indent=2) + '\n')
    (OUT / 'fixtures.g').write_text('N8ProjectiveFixtures := ' + json.dumps(fixtures) + ';\n')


def linear(basis, coefficients):
    out = {}
    for tensor, value in zip(basis, coefficients):
        out = add(out, tensor, value)
    return out


def check(m, p, q, target, label, expected=None, directions=None):
    solutions, charts = all_mixed_factors(m, target, p, q)
    integral = [row for row in solutions if row['integral']]
    answer = bool(integral)
    old, _ = mixed_type(m, target, p, q)
    assert answer == (old is not None), (label, solutions, old)
    if expected is not None:
        assert answer == expected, label
    if directions is not None:
        assert len(solutions) == directions, (label, solutions)
    # All directions, including those not chosen by the old solver, are checked.
    basisp = [m.layer(h['value'], p) for h in m.bydegree[p]]
    basisq = [m.layer(h['value'], q) for h in m.bydegree[q]]
    for row in integral:
        cc, dd = row['c'], list(map(int, row['d']))
        assert bracket(m, linear(basisp, cc), linear(basisq, dd)) == target
        x, y = m.lift(cc, p), m.lift(dd, q)
        g = m.comm(x, y)
        assert m.layer(g, p + q) == target and g == add({(): 1}, target)
        fixtures.append([m.rank, m.degree, m.collect(g)[0], m.collect(x)[0], m.collect(y)[0]])
    records.append({'label': label, 'rank': m.rank, 'p': p, 'q': q,
                    'answer': answer, 'solutions': solutions, 'charts': charts})
    save()
    print(label, 'answer=', answer, 'directions=', len(solutions), flush=True)


m = Magnus(2, 4)
a, b = [m.layer(g, 1) for g in m.gens]
z = bracket(m, a, b)
az, bz = bracket(m, a, z), bracket(m, b, z)
A, B, C = bracket(m, a, az), bracket(m, a, bz), bracket(m, b, bz)
check(m, 1, 3, B, 'two-rational-directions-Jacobi', True, 2)
check(m, 1, 3, add(A, C, -2), 'two-irrational-directions', False, 0)
check(m, 1, 3, A, 'double-root-direction', True, 1)
for i, coordinates in enumerate([(1, 3, 2), (1, 0, 1), (2, -5, 2), (2, 1, -3), (0, 2, 1)]):
    check(m, 1, 3, linear([A, B, C], coordinates), 'binary-quadratic-' + str(i))

for rank, p, q in [(2, 1, 2), (2, 2, 3), (2, 3, 4), (3, 1, 2), (3, 2, 3)]:
    m = Magnus(rank, p + q)
    bp = [m.layer(h['value'], p) for h in m.bydegree[p]]
    bq = [m.layer(h['value'], q) for h in m.bydegree[q]]
    cc = [2 * (i + 1) for i in range(len(bp))]
    dd = [(-1) ** i * (i + 1) for i in range(len(bq))]
    target = bracket(m, linear(bp, cc), linear(bq, dd))
    check(m, p, q, target, 'generated-' + '-'.join(map(str, (rank, p, q))), True)

# Independent affine-scheme controls: repeated roots and a positive-dimensional
# chart. The latter must be refused, never reported as having no rational point.
x, y = symbols('x y')
points, trace = rational_points([(x-2)**2, y-x], (x, y))
assert points == [(2, 2)] and trace['dimension'] == 2
try:
    rational_points([x*y-1], (x, y))
except ValueError:
    pass
else:
    raise AssertionError('Positive-dimensional control was incorrectly accepted')
records.append({'label': 'affine-boundary-controls', 'nonreduced_dimension': 2,
                'rational_points': [[2, 2]], 'positive_dimension_rejected': True})
save()
print('PASS N8 projective factors:', len(records)-1, 'Lie cases;', len(fixtures),
      'integral witnesses; 2 affine controls')
