#!/usr/bin/env python3
"""Compile the fixed toy equation (y+1)^2=p into one class-two group.

The full integer kernel is certified by a unimodular Hermite transform.
No bounded search is used to infer negative retract decisions.
"""
from itertools import combinations
import json
from pathlib import Path

from flint import fmpz_mat
import sympy as sp


def ints(m):
    return [[int(x) for x in row] for row in m.tolist()]


def main():
    root = Path('research/certificates/N9-fixed-circuit')
    assert not root.exists()
    labels = ['p', 'y', 'one', 'yp1', 'square']
    slots = {z: (4+2*i, 5+2*i) for i, z in enumerate(labels)}
    d = 4+2*len(labels)
    pairs = list(combinations(range(d), 2))
    pos = {ij: i for i, ij in enumerate(pairs)}
    rows, descriptions = [], []

    def equation(terms, description):
        row = [0]*len(pairs)
        for i, j, a in terms:
            if i < j:
                row[pos[i, j]] += a
            elif j < i:
                row[pos[j, i]] -= a
            else:
                assert a == 0
        rows.append(row)
        descriptions.append(description)

    for z, (u, v) in slots.items():
        equation([(0, u, 1)], f'axis U_{z}')
        equation([(1, v, 1)], f'axis V_{z}')
        equation([(1, u, 1), (0, v, 1)], f'equal scalar {z}')
    equation([(0, slots['one'][1], 1), (0, 1, -1)], 'one=1')
    equation([(0, slots['yp1'][1], 1), (0, slots['y'][1], -1),
              (0, slots['one'][1], -1)], 'yp1=y+one')
    equation([(slots['yp1'][0], slots['yp1'][1], 1),
              (0, slots['square'][1], -1)], 'square=yp1*yp1')
    equation([(0, slots['square'][1], 1), (0, slots['p'][1], -1)], 'square-p=0')
    equation([(0, 3, 1)], 'normalization M03=0')
    equation([(1, 2, 1)], 'normalization M12=0')
    equation([(1, 3, 1), (0, 2, -1)], 'normalization M13=M02')
    equation([(0, 2, 1), (0, slots['p'][1], -3)], 'normalization M02=3p')
    a = sp.Matrix(rows)
    af = fmpz_mat(ints(a.T))
    hf, uf = af.hnf(transform=True)
    assert hf == uf*af and abs(int(uf.det())) == 1
    h, u = sp.Matrix(hf.tolist()), sp.Matrix(uf.tolist())
    rank = a.rank()
    assert h[rank:, :] == sp.zeros(len(pairs)-rank, len(rows))
    assert h[:rank, :].rank() == rank
    kernel = u[rank:, :]
    assert a*kernel.T == sp.zeros(len(rows), kernel.rows)
    ui = u.inv()
    assert all(x.q == 1 for x in ui)
    forms = []
    for row in kernel.tolist():
        b = sp.zeros(d)
        for (i, j), value in zip(pairs, row):
            b[i, j], b[j, i] = value, -value
        forms.append(b)
    s = len(forms)
    records = []
    for y in [-4, -3, -2, -1, 0, 1, 2]:
        n = (y+1)**2
        values = {'p': n, 'y': y, 'one': 1, 'yp1': y+1, 'square': n}
        vv = [[1, 0], [0, 1], [0, 3*n], [-3*n, 0]]
        for z in labels:
            vv.extend([[values[z], 0], [0, values[z]]])
        vmat = sp.Matrix(vv)
        m = vmat[:, 0]*vmat[:, 1].T-vmat[:, 1]*vmat[:, 0].T
        flat = sp.Matrix([[m[i, j] for i, j in pairs]])
        assert a*flat.T == sp.zeros(len(rows), 1) and m.rank() == 2
        coords = flat*ui
        assert coords[:, :rank] == sp.zeros(1, rank)
        lam = list(map(int, coords[:, rank:]))
        assert flat == sp.Matrix([lam])*kernel
        t = 3*n+1
        alpha = [1]+[0]*(d-1)
        beta = [0, t, -1]+[0]*(d-3)
        q = [t*int(b[0, 1])-int(b[0, 2]) for b in forms]
        assert any(q) and sum(l*x for l, x in zip(lam, q)) == 1
        ru = m*sp.Matrix(beta)
        rv = (sp.Matrix(alpha).T*m).T
        assert m == ru*rv.T-rv*ru.T
        # For this specially chosen pair, the central corrections vanish.
        def correction(av):
            return sum(av[i]*(av[i]-1)//2*ru[i]*rv[i] for i in range(d)) + sum(
                av[i]*av[j]*rv[i]*ru[j] for i, j in pairs)
        ca, cb = correction(alpha), correction(beta)
        rt = ca*ru+cb*rv
        assert ca == cb == 0
        records.append({'n': n, 'y': y, 'lambda': lam, 'q': q,
                        'u': list(map(int, ru)), 'v': list(map(int, rv)),
                        'central': list(map(int, rt)), 'matrix': ints(m)})
    # With the modulus-three guard removed, the sign d=-1 encodes p=n+2.
    # n=2,p=4,y=1 is an explicit false positive for the intended square test.
    n, p, y = 2, 4, 1
    vals = {'p': p, 'y': y, 'one': 1, 'yp1': y+1, 'square': p}
    vv = [[1, 0], [0, 1], [0, p], [-p, 0]]
    for z in labels:
        vv.extend([[vals[z], 0], [0, vals[z]]])
    vmat = sp.Matrix(vv)
    wrong = -(vmat[:, 0]*vmat[:, 1].T-vmat[:, 1]*vmat[:, 0].T)
    unguarded = a.copy()
    unguarded[-1, pos[0, slots['p'][1]]] = -1
    wf = sp.Matrix([wrong[i, j] for i, j in pairs])
    assert unguarded*wf == sp.zeros(len(rows), 1)
    assert wrong.rank() == 2 and (n+1)*wrong[0, 1]-wrong[0, 2] == 1
    assert a*wf != sp.zeros(len(rows), 1)
    output = {'dimension': d, 'central_rank': s, 'labels': labels,
              'slots': slots, 'pairs': pairs, 'constraints': rows,
              'descriptions': descriptions, 'rank': rank,
              'hnf': ints(h), 'unimodular': ints(u), 'inverse': ints(ui),
              'kernel': ints(kernel), 'forms': [ints(b) for b in forms],
              'retractions': records,
              'wrong_sign_control': {'n': n, 'p': p, 'y': y, 'matrix': ints(wrong)},
              'scope': 'One fixed toy group, seven retractions for four parameter values; universal theorem is a written proof.'}
    root.mkdir(parents=True)
    (root/'checks-v1.json').write_text(json.dumps(output, indent=2)+'\n')
    keys = ['dimension', 'constraints', 'rank', 'hnf', 'unimodular', 'inverse', 'kernel', 'forms']
    gr = [[r[k] for k in ['n', 'y', 'lambda', 'q', 'u', 'v', 'central', 'matrix']] for r in records]
    (root/'fixtures-v1.g').write_text('N9Circuit := '+json.dumps([output[k] for k in keys])+';;\n'
                                     'N9CircuitRetractions := '+json.dumps(gr)+';;\n'
                                     'N9WrongSign := '+json.dumps(ints(wrong))+';;\n')
    print('Fixed circuit: (y+1)^2=p; dimension', d, 'central rank', s,
          'constraint rank', rank, 'saturated kernel certified')
    print('Witnesses (n,y)', [(r['n'], r['y']) for r in records])
    print('Negative sign control without modulus guard: n=2,y=1,p=4 passes wrong encoding')
    print('PASS N9 fixed-circuit lattice and integral witnesses')


if __name__ == '__main__':
    main()
