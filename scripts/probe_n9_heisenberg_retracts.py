#!/usr/bin/env python3
"""Exact class-two coordinate witnesses for the N9 rank-two criterion.

The independent checker constructs the presentations in native GAP/nq.
No bounded enumeration is used to exclude all retractions in negative cases.
"""
from itertools import combinations
import json
from pathlib import Path
import random

import sympy as sp

SEED = 2026092920


def alt(d, entries):
    b = sp.zeros(d)
    for i, j, v in entries:
        b[i, j] = v
        b[j, i] = -v
    return b


def coords(a, g):
    return tuple(map(int, a)), tuple(map(int, g))


def multiply(x, y, forms):
    a, g = x
    b, h = y
    return coords([u+v for u, v in zip(a, b)],
                  [g[l]+h[l]-sum(a[j]*b[i]*int(f[i, j]) for i, j in combinations(range(len(a)), 2))
                   for l, f in enumerate(forms)])


def power(x, n, forms):
    a, g = x
    return coords([n*v for v in a],
                  [n*g[l]-n*(n-1)//2*sum(a[i]*a[j]*int(f[i, j])
                                         for i, j in combinations(range(len(a)), 2))
                   for l, f in enumerate(forms)])


def commutator(x, y, forms):
    result = power(x, -1, forms)
    for z in [power(y, -1, forms), x, y]:
        result = multiply(result, z, forms)
    return result


def record(forms, alpha, beta, gamma, delta, lam, name):
    d, s = len(alpha), len(forms)
    alpha, beta, lam = list(map(int, alpha)), list(map(int, beta)), list(lam)
    h1, h2 = coords(alpha, gamma), coords(beta, delta)
    q = [int((sp.Matrix(alpha).T*b*sp.Matrix(beta))[0]) for b in forms]
    c = coords([0]*d, q)
    assert commutator(h1, h2, forms) == c
    assert any(q)
    m = sum((int(l)*b for l, b in zip(lam, forms)), sp.zeros(d))
    assert sum(l*q0 for l, q0 in zip(lam, q)) == 1
    assert m.rank() == 2
    u = list(map(int, m*sp.Matrix(beta)))
    v = list(map(int, sp.Matrix(alpha).T*m))
    assert m == sp.Matrix(u)*sp.Matrix(v).T-sp.Matrix(v)*sp.Matrix(u).T

    def correction(a, g):
        return (sum(a[i]*(a[i]-1)//2*u[i]*v[i] for i in range(d))
                + sum(a[i]*a[j]*v[i]*u[j] for i, j in combinations(range(d), 2))
                - sum(g0*l for g0, l in zip(g, lam)))

    aa, dd = correction(alpha, gamma), correction(beta, delta)
    t = [aa*u0+dd*v0 for u0, v0 in zip(u, v)]
    images = [multiply(multiply(power(h1, u0, forms), power(h2, v0, forms), forms),
                       power(c, t0, forms), forms) for u0, v0, t0 in zip(u, v, t)]
    images += [power(c, l, forms) for l in lam]
    zero = coords([0]*d, [0]*s)
    for i, j in combinations(range(d+s), 2):
        actual = commutator(images[i], images[j], forms)
        expected = zero
        if j < d:
            for l, b in enumerate(forms):
                expected = multiply(expected, power(images[d+l], int(b[i, j]), forms), forms)
        assert actual == expected

    def evaluate(x):
        result = zero
        for im, exponent in zip(images, x[0]+x[1]):
            result = multiply(result, power(im, exponent, forms), forms)
        return result

    assert evaluate(h1) == h1 and evaluate(h2) == h2
    assert all(evaluate(im) == im for im in images)
    return {'name': name, 'forms': [[[int(x) for x in row] for row in b.tolist()] for b in forms],
            'alpha': alpha, 'beta': beta, 'gamma': gamma, 'delta': delta,
            'q': q, 'lambda': lam, 'u': u, 'v': v, 't': t,
            'images': [[list(a), list(g)] for a, g in images]}


def main():
    root = Path('research/certificates/N9-Heisenberg')
    assert not (root/'checks-v1.json').exists()
    rng = random.Random(SEED)
    records = []
    for k in range(1, 5):
        d = 2*k
        forms = [alt(d, [(2*j, 2*j+1, 1)]) for j in range(k)]
        for trial in range(3):
            a = [rng.randrange(-3, 4) for _ in range(d)]
            b = [rng.randrange(-3, 4) for _ in range(d)]
            pivot = trial % k
            change = sp.eye(2)
            for _ in range(5):
                i = rng.randrange(2)
                change[i, :] += rng.choice([-2, -1, 1, 2])*change[1-i, :]
            if trial == 1:
                change.row_swap(0, 1)
            a[2*pivot:2*pivot+2] = list(map(int, change[0, :]))
            b[2*pivot:2*pivot+2] = list(map(int, change[1, :]))
            lam = [0]*k
            lam[pivot] = int(change.det())
            g = [rng.randrange(-5, 6) for _ in range(k)]
            e = [rng.randrange(-5, 6) for _ in range(k)]
            records.append(record(forms, a, b, g, e, lam, f'product-{k}-{trial}'))
    # Mixed forms: each individual form may have rank four; the selected
    # integral linear combination has rank two. Scramble the lattice basis.
    for sign in [-1, 1]:
        forms = [alt(4, [(0, 1, 1), (2, 3, 1)]), alt(4, [(0, 2, 1), (1, 3, 1)])]
        records.append(record(forms, [1, 0, 0, 0], [0, 1, 0, 0], [3, -2], [-4, 1],
                              [1, sign], f'split-pfaffian-{sign}'))
    for d in [4, 5, 6]:
        forms = [alt(d, [(0, j, 1 if j == 1 else rng.randrange(-2, 3)) for j in range(1, d)])]
        forms += [alt(d, [(i, j, rng.randrange(-2, 3)) for i, j in combinations(range(d), 2)])
                  for _ in range(2)]
        change = sp.eye(d)
        for _ in range(7):
            i, j = rng.sample(range(d), 2)
            change[i, :] += rng.choice([-1, 1])*change[j, :]
        inv = change.inv()
        changed = [change.T*b*change for b in forms]
        a, b = list(inv[:, 0]), list(inv[:, 1])
        records.append(record(changed, a, b, [2, -3, 1], [-1, 4, -2], [1, 0, 0], f'mixed-{d}'))
    negative = [
        {'kind': 'product_2_3', 'forms': [alt(4, [(0, 1, 1)]), alt(4, [(2, 3, 1)])],
         'alpha': [2, 0, 3, 0], 'beta': [0, 1, 0, 1]},
        {'kind': 'symplectic_rank4', 'forms': [alt(4, [(0, 1, 1), (2, 3, 1)])],
         'alpha': [1, 0, 0, 0], 'beta': [0, 1, 0, 0]},
        {'kind': 'anisotropic_pfaffian',
         'forms': [alt(4, [(0, 1, 1), (2, 3, 1)]), alt(4, [(0, 2, 1), (1, 3, -1)])],
         'alpha': [1, 0, 0, 0], 'beta': [0, 1, 0, 0]},
        {'kind': 'central_root', 'forms': [alt(2, [(0, 1, 2)])],
         'alpha': [1, 0], 'beta': [0, 1]},
    ]
    for r in negative:
        r['forms'] = [[[int(x) for x in row] for row in b.tolist()] for b in r['forms']]
    out = {'seed': SEED, 'positives': records, 'negatives': negative,
           'scope': 'Constructed positive retractions and four algebraic negative controls; no general integer-point algorithm.'}
    root.mkdir(parents=True, exist_ok=True)
    (root/'checks-v1.json').write_text(json.dumps(out, indent=2)+'\n')
    rows = [[r[k] for k in ['forms', 'alpha', 'gamma', 'beta', 'delta', 'lambda', 'u', 'v', 't', 'images']]
            for r in records]
    ng = [[r[k] for k in ['kind', 'forms', 'alpha', 'beta']] for r in negative]
    (root/'fixtures-v1.g').write_text('N9Positive := '+json.dumps(rows)+';;\nN9Negative := '+json.dumps(ng)+';;\n')
    print('positive retractions', len(records), 'negative controls', len(negative), 'seed', SEED)
    print('PASS N9 Heisenberg integral retraction construction')


if __name__ == '__main__':
    main()
