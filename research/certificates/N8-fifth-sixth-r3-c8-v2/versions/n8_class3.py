#!/usr/bin/env python3
"""Exact experimental single-commutator solver in F_r/gamma_4(F_r).

Input is a word in signed 1-based free generators. Arithmetic uses the integral
Magnus expansion truncated after degree three. See the accompanying proof note;
this implementation is supporting evidence, not a substitute for that proof.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd, lcm
from functools import reduce
from sympy import Matrix, ZZ, divisors
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ONE = {(): 1}


def add(a, b, factor=1):
    out = dict(a)
    for w, c in b.items():
        out[w] = out.get(w, 0) + factor*c
        if not out[w]:
            del out[w]
    return out


def mul(a, b):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            if len(u)+len(v) <= 3:
                w = u+v
                out[w] = out.get(w, 0)+x*y
    return {w: c for w, c in out.items() if c}


def inv(a):
    assert a.get(()) == 1
    b = add(a, ONE, -1)
    b2 = mul(b, b)
    return add(add(add(ONE, b, -1), b2), mul(b2, b), -1)


def comm(a, b):
    return mul(mul(mul(inv(a), inv(b)), a), b)


def expansion(word):
    out = dict(ONE)
    for s in word:
        assert s != 0
        a = {(): 1, (abs(s)-1,): 1}
        out = mul(out, a if s > 0 else inv(a))
    return out


def winv(word):
    return [-s for s in reversed(word)]


def wcomm(x, y):
    return winv(x)+winv(y)+list(x)+list(y)


def wpow(word, n):
    n = int(n)
    return list(word)*n if n >= 0 else winv(word)*(-n)


def lift_vector(v):
    return [s for i, n in enumerate(v) for s in wpow([i+1], n)]


def lift_exterior(y):
    return [s for i, j in combinations(range(len(y)), 2)
            for s in wpow(wcomm([i+1], [j+1]), y[i][j])]


def smith(a):
    dm = DomainMatrix.from_Matrix(a).convert_to(ZZ)
    d, s, t = smith_normal_decomp(dm)
    d, s, t = (x.to_Matrix() for x in (d, s, t))
    assert d == s*a*t
    return d, s, t


def integer_solve(columns, rhs):
    """Return an integer solution or None; rows with no coefficient are checked."""
    rows = []
    target = []
    for k, b in enumerate(rhs):
        row = [col[k] for col in columns]
        if any(row):
            rows.append(row)
            target.append(b)
        elif b:
            return None
    if not rows:
        return [0]*len(columns)
    a = Matrix(rows)
    d, s, t = smith(a)
    sb = s*Matrix(target)
    sol = [0]*a.cols
    for i in range(a.rows):
        diag = d[i, i] if i < a.cols else 0
        if diag:
            if sb[i] % diag:
                return None
            sol[i] = sb[i]//diag
        elif sb[i]:
            return None
    answer = list(t*Matrix(sol))
    assert a*Matrix(answer) == Matrix(target)
    return [int(x) for x in answer]


def primitive_plane(w):
    """Column basis of im_Q(w) intersect Z^r for a skew matrix of rank two."""
    r = w.rows
    assert w.rank() == 2
    annihilators = w.nullspace()
    if not annihilators:
        return Matrix.eye(r)
    rows = []
    for v in annihilators:
        denominator = lcm(*(int(x.q) for x in v))
        rows.append([int(denominator*x) for x in v])
    a = Matrix(rows)
    d, _, t = smith(a)
    rank = a.rank()
    assert all(d[i, i] for i in range(rank))
    p = t[:, rank:]
    assert p.cols == 2 and a*p == Matrix.zeros(a.rows, 2)
    return p


def central_factor(g3, r):
    """Solve g_abc=z_a Y_bc-Y_ab z_c by patch reconstruction and integrality."""
    at = lambda a, b, c: Q(g3.get((a, b, c), 0))
    for i in range(r):
        ts = [at(i, i, j) for j in range(r)]
        nonzero = next((j for j in range(r) if ts[j]), None)
        if nonzero is not None:
            j = nonzero
            zj = at(j, i, j)/(2*ts[j])
            z = [(at(j, i, k)-zj*ts[k])/ts[j] for k in range(r)]
            y = [[at(i, a, b)+ts[a]*z[b] for b in range(r)] for a in range(r)]
        else:
            y = [[at(i, a, b) for b in range(r)] for a in range(r)]
            pair = next(((j, k) for j, k in product(range(r), repeat=2) if y[j][k]), None)
            if pair is None:
                continue
            j, k = pair
            zk = -at(j, k, k)/y[j][k]
            z = [(at(a, j, k)+y[a][j]*zk)/y[j][k] for a in range(r)]
        if z[i] != 1:
            continue
        if any(y[a][b] != -y[b][a] for a, b in product(range(r), repeat=2)):
            continue
        if any(at(a, b, c) != z[a]*y[b][c]-y[a][b]*z[c]
               for a, b, c in product(range(r), repeat=3)):
            continue
        denominator = lcm(*(x.denominator for x in z))
        ints = [int(denominator*x) for x in z]
        content = reduce(gcd, map(abs, ints))
        z0 = [x//content for x in ints]
        scale = Q(denominator, content)
        y0 = [[v/scale for v in row] for row in y]
        if any(v.denominator != 1 for row in y0 for v in row):
            # Uniqueness of the rational rank-one tensor makes other patches redundant.
            return None
        return z0, [[int(v) for v in row] for row in y0]
    return None


def solve(word, rank):
    assert rank >= 1 and all(0 < abs(s) <= rank for s in word)
    g = expansion(word)
    if g == ONE:
        return {'answer': True, 'case': 'identity', 'x': [], 'y': []}
    if any(len(w) == 1 for w in g):
        return {'answer': False, 'case': 'outside_derived'}
    g2 = {w: c for w, c in g.items() if len(w) == 2}
    g3 = {w: c for w, c in g.items() if len(w) == 3}
    if not g2:
        factors = central_factor(g3, rank)
        if factors is None:
            return {'answer': False, 'case': 'central'}
        z, y = factors
        xw, yw = lift_vector(z), lift_exterior(y)
        assert comm(expansion(xw), expansion(yw)) == g
        return {'answer': True, 'case': 'central', 'x': xw, 'y': yw}
    w = Matrix(rank, rank, lambda i, j: g2.get((i, j), 0))
    assert w == -w.T
    if w.rank() != 2:
        return {'answer': False, 'case': 'nondecomposable_degree2'}
    p = primitive_plane(w)
    a, b = next((a, b) for a, b in combinations(range(rank), 2) if w[a, b])
    determinant = p[a, 0]*p[b, 1]-p[a, 1]*p[b, 0]
    index = w[a, b]/determinant
    assert index.q == 1
    if index < 0:
        p[:, 1] = -p[:, 1]
        index = -index
    index = int(index)
    wedge = p[:, 0]*p[:, 1].T-p[:, 1]*p[:, 0].T
    assert index*wedge == w
    triples = list(product(range(rank), repeat=3))
    pairs = list(combinations(range(rank), 2))
    basis_words = [wcomm([i+1], [j+1]) for i, j in pairs]
    basis_exp = [expansion(z) for z in basis_words]
    checked = 0
    for h11 in divisors(index):
        h22 = index//int(h11)
        for h12 in range(int(h11)):
            u = [int(x) for x in p[:, 0]*h11]
            v = [int(x) for x in p[:, 0]*h12+p[:, 1]*h22]
            x0, y0 = lift_vector(u), lift_vector(v)
            ex, ey = expansion(x0), expansion(y0)
            base = comm(ex, ey)
            residual = mul(inv(base), g)
            assert not any(len(s) in (1, 2) for s in residual)
            rhs = [residual.get(s, 0) for s in triples]
            corrections = ([comm(z, ey) for z in basis_exp]
                           + [comm(ex, z) for z in basis_exp])
            cols = [[z.get(s, 0) for s in triples] for z in corrections]
            coeffs = integer_solve(cols, rhs)
            checked += 1
            if coeffs is None:
                continue
            cword = [s for z, k in zip(basis_words, coeffs[:len(pairs)]) for s in wpow(z, k)]
            dword = [s for z, k in zip(basis_words, coeffs[len(pairs):]) for s in wpow(z, k)]
            xw, yw = x0+cword, y0+dword
            assert comm(expansion(xw), expansion(yw)) == g
            return {'answer': True, 'case': 'noncentral', 'x': xw, 'y': yw,
                    'lattice_index': index, 'lattices_checked': checked}
    return {'answer': False, 'case': 'noncentral', 'lattice_index': index,
            'lattices_checked': checked}


if __name__ == '__main__':
    import argparse
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rank', type=int)
    parser.add_argument('word', help='JSON list of signed generator indices')
    args = parser.parse_args()
    print(json.dumps(solve(json.loads(args.word), args.rank)))
