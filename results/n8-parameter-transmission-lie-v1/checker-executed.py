#!/usr/bin/env python3
"""Exact Lie obstruction probe for an uncounted parameter-transmission lead."""
from pathlib import Path
import json
import sympy as S
from n8_universal_gauges import WeightedTensor
from n8_weighted_automorphisms import add

out = Path('research/certificates/N8-parameter-transmission')
out.mkdir(parents=True, exist_ok=False)
m = WeightedTensor(1, 4, 15)
a, e = m.letters
es = [e]
for _ in range(4):
    es.append(m.bracket(a, es[-1]))
D = es[4]
V3 = add(m.bracket(e, es[3]), m.bracket(es[1], es[2]), -1)
V3 = {w: -x for w, x in V3.items()}
V5 = {w: -x for w, x in m.bracket(es[2], es[3]).items()}
assert not add(m.bracket(e, D), m.bracket(a, V3))
assert not add(m.bracket(es[2], D), m.bracket(a, V5))
Q = m.bracket(e, V3)
B = m.bracket(es[2], m.bracket(e, es[1]))
us, vs = m.layers[7][0], m.layers[14][0]
columns = [m.bracket(m.hall[i]['lie'], D) for i in us]
columns += [m.bracket(a, m.hall[i]['lie']) for i in vs]
rows, basis = m.layers[15]
def vector(poly):
    cc = basis.coordinates(poly)
    return S.Matrix(len(rows), 1, lambda i,j: S.Rational(cc.get(i, 0)))
A = S.Matrix.hstack(*(vector(x) for x in columns))
q, b = vector(Q), vector(B)
assert A.rank() == A.cols
assert A.row_join(q).rank() == A.cols+1
assert A.row_join(b).rank() == A.cols+1
joint = A.row_join(b)
solution = joint.gauss_jordan_solve(q)
assert solution[1].rows == 0
coeff = solution[0]
assert joint*coeff == q and coeff[-1] != 0
record = dict(weights=[1,4],class_bound=15,offset=6,
              first_coordinates=len(us),second_coordinates=len(vs),
              equations=A.rows,rank=A.rank(),
              Q_mod_A_multiple_of_B=str(coeff[-1]),
              lift=[str(x) for x in coeff[:-1]],
              statement='Lie obstruction only; no actual group branch decision')
(out/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
print('PASS N8 parameter transmission Lie probe')
