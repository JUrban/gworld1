#!/usr/bin/env python3
"""Exact prototype for the proposed class-four N8(b) extension."""
from itertools import combinations, product
from functools import reduce
from math import gcd
from sympy import Matrix, Poly, divisors, factor_list, symbols
from n8_class3 import (ONE, add, winv, wcomm, wpow, lift_vector,
                      lift_exterior, integer_solve, primitive_plane, central_factor)


def mul(a, b):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            if len(u)+len(v) <= 4:
                w = u+v
                out[w] = out.get(w, 0)+x*y
    return {w: c for w, c in out.items() if c}


def inv(a):
    assert a.get(()) == 1
    b = add(a, ONE, -1)
    term = dict(ONE)
    out = dict(ONE)
    for k in range(1, 5):
        term = mul(term, b)
        out = add(out, term, (-1)**k)
    return out


def comm(a, b):
    return mul(mul(mul(inv(a), inv(b)), a), b)


def expansion(word):
    out = dict(ONE)
    for s in word:
        assert s
        a = {(): 1, (abs(s)-1,): 1}
        out = mul(out, a if s > 0 else inv(a))
    return out


def layer(g, degree):
    return {w: c for w, c in g.items() if len(w) == degree}


def bases(rank):
    b2 = [wcomm([i+1], [j+1]) for i, j in combinations(range(rank), 2)]
    b3 = [wcomm(wcomm([j+1], [i+1]), [k+1])
          for i in range(rank) for j in range(i+1, rank) for k in range(i, rank)]
    return b2, b3


def linear_correction(g, x, y, cbasis, dbasis, degree, rank):
    ex, ey = expansion(x), expansion(y)
    delta = mul(inv(comm(ex, ey)), g)
    if any(0 < len(w) < degree for w in delta):
        return None
    indices = list(product(range(rank), repeat=degree))
    corr = ([comm(expansion(c), ey) for c in cbasis]
            + [comm(ex, expansion(d)) for d in dbasis])
    coeffs = integer_solve([[v.get(w, 0) for w in indices] for v in corr],
                           [delta.get(w, 0) for w in indices])
    if coeffs is None:
        return None
    cw = [s for b, k in zip(cbasis, coeffs[:len(cbasis)]) for s in wpow(b, k)]
    dw = [s for b, k in zip(dbasis, coeffs[len(cbasis):]) for s in wpow(b, k)]
    return x+cw, y+dw


def factor_wedge(w):
    p = primitive_plane(w)
    a, b = next((a, b) for a, b in combinations(range(w.rows), 2) if w[a, b])
    d = w[a, b]/(p[a, 0]*p[b, 1]-p[a, 1]*p[b, 0])
    assert d.q == 1
    if d < 0:
        p[:, 1] = -p[:, 1]
        d = -d
    assert d*(p[:, 0]*p[:, 1].T-p[:, 1]*p[:, 0].T) == w
    return p, int(d)


def central_22(g4, rank, b2):
    pairs = list(combinations(range(rank), 2))
    size = len(pairs)
    w = Matrix(size, size, lambda i, j: g4.get(pairs[i]+pairs[j], 0))
    if w != -w.T or w.rank() != 2:
        return None
    # Explicit reconstruction checks membership in Lambda^2(L2).
    total = {}
    for i, j in combinations(range(size), 2):
        total = add(total, layer(comm(expansion(b2[i]), expansion(b2[j])), 4), int(w[i,j]))
    if total != g4:
        return None
    p, d = factor_wedge(w)
    x = [s for b, k in zip(b2, list(d*p[:, 0])) for s in wpow(b, k)]
    y = [s for b, k in zip(b2, list(p[:, 1])) for s in wpow(b, k)]
    return x, y


def central_13(g, rank, b3):
    g4 = layer(g, 4)
    variables = symbols('t:'+str(rank))
    quadratic = None
    for j, k in product(range(rank), repeat=2):
        q = sum(g4.get((i,j,k,l), 0)*variables[i]*variables[l]
                for i,l in product(range(rank), repeat=2))
        q = q.expand()
        if q:
            quadratic = q
            break
    # The degree-four injectivity lemma guarantees this for a nonzero Lie element.
    assert quadratic is not None, ('outer-map lemma violation', g4)
    _, factors = factor_list(quadratic, *variables)
    for factor, _ in factors:
        poly = Poly(factor, *variables)
        if poly.total_degree() != 1:
            continue
        assert poly.coeff_monomial(1) == 0
        z = [poly.coeff_monomial(t) for t in variables]
        assert all(v.q == 1 for v in z)
        content = reduce(gcd, (abs(int(v)) for v in z))
        z = [int(v)//content for v in z]
        x = lift_vector(z)
        answer = linear_correction(g, x, [], [], b3, 4, rank)
        if answer is not None:
            return answer
    return None


def solve(word, rank):
    assert rank >= 1 and all(0 < abs(s) <= rank for s in word)
    g = expansion(word)

    def yes(pair, case):
        x, y = pair
        assert comm(expansion(x), expansion(y)) == g
        return {'answer': True, 'case': case, 'x': x, 'y': y}

    if g == ONE:
        return yes(([], []), 'identity')
    if layer(g, 1):
        return {'answer': False, 'case': 'outside_derived'}
    b2, b3 = bases(rank)
    g2, g3, g4 = (layer(g, i) for i in (2,3,4))
    if g2:
        w = Matrix(rank, rank, lambda i,j: g2.get((i,j),0))
        assert w == -w.T
        if w.rank() != 2:
            return {'answer': False, 'case': 'nondecomposable_degree2'}
        p, index = factor_wedge(w)
        for a in divisors(index):
            c = index//int(a)
            for b in range(int(a)):
                x = lift_vector(list(a*p[:,0]))
                y = lift_vector(list(b*p[:,0]+c*p[:,1]))
                pair = linear_correction(g, x, y, b2, b2, 3, rank)
                if pair is None:
                    continue
                pair = linear_correction(g, *pair, b3, b3, 4, rank)
                if pair is not None:
                    return yes(pair, 'nonzero_degree2')
        return {'answer': False, 'case': 'nonzero_degree2'}
    if g3:
        factors = central_factor(g3, rank)
        if factors is None:
            return {'answer': False, 'case': 'nonfactorable_degree3'}
        z0, y0 = factors
        content = reduce(gcd, (abs(v) for row in y0 for v in row))
        assert content
        for absolute in divisors(content):
            for sign in (-1,1):
                k = int(absolute)*sign
                x = lift_vector([k*v for v in z0])
                y = lift_exterior([[v//k for v in row] for row in y0])
                pair = linear_correction(g, x, y, b2, b3, 4, rank)
                if pair is not None:
                    return yes(pair, 'nonzero_degree3')
        return {'answer': False, 'case': 'nonzero_degree3'}
    pair = central_22(g4, rank, b2)
    if pair is not None:
        return yes(pair, 'central_22')
    pair = central_13(g, rank, b3)
    if pair is not None:
        return yes(pair, 'central_13')
    return {'answer': False, 'case': 'central_degree4'}


if __name__ == '__main__':
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rank',type=int)
    parser.add_argument('word',help='JSON list of signed generator indices')
    args=parser.parse_args()
    print(json.dumps(solve(json.loads(args.word),args.rank)))
