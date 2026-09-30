#!/usr/bin/env python3
"""Exact bounded audit, including a group target sensitive to scale allocation."""
import json
from functools import reduce
from math import gcd
from pathlib import Path

from n8_central import add, bracket
from n8_component_linear import affine_solution
from n8_ia_orbits import wpow, wcomm
from n8_multigraded_magnus import Magnus
from n8_penultimate import lie_tensor, mixed_candidates as old_mixed
from n8_projective_leading_pairs import leading_pairs

OUT = Path('research/certificates/N8-projective-leading-pairs')
OUT.mkdir(parents=True, exist_ok=True)
assert not (OUT / 'checks-v1.json').exists(), 'Preserve earlier evidence'
records, fixtures, branches = [], [], []


def save():
    (OUT / 'checks-v1.json').write_text(json.dumps(records, indent=2) + '\n')
    (OUT / 'fixtures-v1.g').write_text(
        'N8ProjectiveLeadingFixtures := ' + json.dumps(fixtures) + ';\n'
        + 'N8ProjectiveLeadingBranches := ' + json.dumps(branches) + ';\n')


def pairset(pairs):
    return {(tuple(c), tuple(d)) for c, d in pairs}


def check(m, p, q, target, label, expected_pairs=None):
    pairs, trace = leading_pairs(m, target, p, q)
    if p < q:
        old = old_mixed(m, target, p, q)
        assert pairset(old) == pairset(pairs), (label, old, pairs)
    if expected_pairs is not None:
        assert len(pairs) == expected_pairs, (label, len(pairs))
    for c, d in pairs:
        assert bracket(m, lie_tensor(m, c, p), lie_tensor(m, d, q)) == target
    records.append({'label': label, 'rank': m.rank, 'class': m.degree,
                    'p': p, 'q': q, 'pairs': pairs, 'trace': trace})
    save()
    print(label, len(pairs), 'pairs', flush=True)
    return pairs


m = Magnus(2, 4)
a, b = [m.layer(g, 1) for g in m.gens]
z = bracket(m, a, b)
az, bz = bracket(m, a, z), bracket(m, b, z)
A, B, C = bracket(m, a, az), bracket(m, a, bz), bracket(m, b, bz)
check(m, 1, 3, add({}, B, 6), 'Jacobi-two-directions-content6', 16)
check(m, 1, 3, add(A, C, -2), 'irrational-directions', 0)
check(m, 1, 3, add({}, A, 12), 'double-direction-content12', 12)

for rank, p, q in [(2, 1, 2), (2, 2, 3), (2, 3, 4), (3, 1, 2), (3, 2, 3)]:
    m = Magnus(rank, p + q)
    c = [2 * (i + 1) for i in range(len(m.bydegree[p]))]
    d = [3 * (-1)**i * (i + 1) for i in range(len(m.bydegree[q]))]
    w = bracket(m, lie_tensor(m, c, p), lie_tensor(m, d, q))
    pairs = check(m, p, q, w, f'generated-{rank}-{p}-{q}')
    assert (tuple(c), tuple(d)) in pairset(pairs)

m = Magnus(3, 4)
c, d = [2, 0, 0], [0, 3, 0]
w = bracket(m, lie_tensor(m, c, 2), lie_tensor(m, d, 2))
check(m, 2, 2, w, 'equal-weight-index6', 12)

# This group example is new: check all branches, not merely the first success.
m = Magnus(2, 5)
zword = wcomm([2], [1])
dword = wcomm(zword, [1])
xword, yword = [1, 1] + zword, wpow(dword, 3)
gword = wcomm(xword, yword)
g = m.expansion(gword)
assert all(len(word) in (0, 4, 5) for word in g)
w = m.layer(g, 4)
group_rows = []
for p, q in [(1, 3), (2, 2)]:
    pairs, trace = leading_pairs(m, w, p, q)
    for c, d in pairs:
        xbase, ybase = m.lift(c, p), m.lift(d, q)
        base = m.comm(xbase, ybase)
        residual = m.mul(m.inv(base), g)
        assert all(len(word) in (0, 5) for word in residual)
        C, D = lie_tensor(m, c, p), lie_tensor(m, d, q)
        columns = ([bracket(m, m.layer(h['value'], p + 1), D) for h in m.bydegree[p + 1]]
                   + [bracket(m, C, m.layer(h['value'], q + 1)) for h in m.bydegree[q + 1]])
        hall_columns = [m.coordinates(col, 5) for col in columns]
        rhs = m.coordinates(m.layer(residual, 5), 5)
        solution = affine_solution(hall_columns, rhs)
        primitive = reduce(gcd, (abs(value) for value in c), 0) == 1
        row = {'p': p, 'q': q, 'C': c, 'D': d, 'primitive_C': primitive,
               'columns': hall_columns, 'rhs': rhs, 'soluble': solution is not None}
        xbaseword, ybaseword = m.collect(xbase)[0], m.collect(ybase)[0]
        correction_words = ([wcomm(h['word'], ybaseword) for h in m.bydegree[p + 1]]
                            + [wcomm(xbaseword, h['word']) for h in m.bydegree[q + 1]])
        branches.append([2, 5, gword, xbaseword, ybaseword, correction_words, int(solution is not None)])
        if solution is not None:
            vector, kernel = solution
            cut = len(m.bydegree[p + 1])
            x = m.mul(xbase, m.lift(vector[:cut], p + 1))
            y = m.mul(ybase, m.lift(vector[cut:], q + 1))
            assert m.comm(x, y) == g
            row.update(correction=vector, kernel=kernel)
            fixtures.append([2, 5, gword, m.collect(x)[0], m.collect(y)[0]])
        group_rows.append(row)

records.append({'label': 'scale-sensitive-group-target', 'rank': 2, 'class': 5,
                'xword': xword, 'yword': yword, 'gword': gword, 'branches': group_rows})
save()  # Preserve the computed outcome even if the proposed control fails.
assert group_rows and any(row['soluble'] for row in group_rows)
assert any(row['primitive_C'] for row in group_rows)
assert all(not row['soluble'] for row in group_rows if row['primitive_C'])
print('PASS N8 projective complete leading pairs:', len(records) - 1, 'Lie cases;',
      len(group_rows), 'group branches;', len(fixtures), 'positive witnesses;',
      sum(row['primitive_C'] for row in group_rows), 'primitive branches fail', flush=True)
