#!/usr/bin/env python3
"""Exact single-commutator algorithm for targets in gamma_(c-1).

Uses the prior homogeneous factor lemma, then one central integer lift.
All commutators use x^-1 y^-1 x y. See the accompanying candidate proof.
"""
from functools import reduce
from itertools import combinations, product
from math import gcd
from sympy import Matrix, Poly, divisors, factor_list, symbols
from n8_central import (Magnus, add, bracket, decide_central,
                       linear_solution, primitive_lie_line)
from n8_ia_orbits import ONE, factor_wedge


def lie_tensor(m, coordinates, degree):
    out = {}
    for h, n in zip(m.bydegree[degree], coordinates):
        out = add(out, m.layer(h['value'], degree), n)
    return out


def mixed_candidates(m, w, p, q):
    """All integral unequal-weight factor pairs, without primitive scaling loss."""
    assert p < q
    quadratics = {}
    for word, n in w.items():
        assert len(word) == p + q
        i, j, k = word[:p], word[p:q], word[q:]
        key = tuple(sorted((i, k)))
        row = quadratics.setdefault(j, {})
        row[key] = row.get(key, 0) + n
    row = next(({key: n for key, n in row.items() if n}
                for j, row in sorted(quadratics.items()) if any(row.values())), None)
    if row is None:
        return []
    blocks = list(product(range(m.rank), repeat=p))
    variables = symbols('t:' + str(len(blocks)))
    positions = {word: i for i, word in enumerate(blocks)}
    expression = sum(n * variables[positions[i]] * variables[positions[k]]
                     for (i, k), n in row.items())
    answer = []
    seen = set()
    for polynomial, multiplicity in factor_list(expression, *variables)[1]:
        poly = Poly(polynomial, *variables)
        if poly.total_degree() != 1 or poly.coeff_monomial(1):
            continue
        tensor = {word: poly.coeff_monomial(var)
                  for word, var in zip(blocks, variables) if poly.coeff_monomial(var)}
        cc = primitive_lie_line(m, tensor, p)
        if cc is None or tuple(cc) in seen:
            continue
        seen.add(tuple(cc))
        c = lie_tensor(m, cc, p)
        columns = [bracket(m, c, m.layer(h['value'], q)) for h in m.bydegree[q]]
        result = linear_solution(columns, w)
        if result is None:
            continue
        dd, kernel = result
        assert not kernel, 'different-weight homogeneous centralizer must vanish'
        content = reduce(gcd, (abs(n) for n in dd), 0)
        assert content
        for absolute in divisors(content):
            for k in (int(absolute), -int(absolute)):
                answer.append(([k*n for n in cc], [n//k for n in dd]))
    return answer


def equal_candidates(m, w, p):
    """One oriented basis per integral leading-plane sublattice."""
    basis = [m.layer(h['value'], p) for h in m.bydegree[p]]
    pairs = list(combinations(range(len(basis)), 2))
    result = linear_solution([bracket(m, basis[i], basis[j]) for i,j in pairs], w)
    if result is None:
        return []
    coordinates, kernel = result
    assert not kernel
    matrix = Matrix.zeros(len(basis))
    for (i,j), n in zip(pairs, coordinates):
        matrix[i,j] = n
        matrix[j,i] = -n
    if matrix.rank() != 2:
        return []
    plane, index = factor_wedge(matrix)
    answer = []
    for a in divisors(index):
        a = int(a)
        e = index // a
        for b in range(a):
            coordinates = plane * Matrix([[a,b], [0,e]])
            answer.append((list(map(int, coordinates[:,0])),
                           list(map(int, coordinates[:,1]))))
    return answer


def decide_penultimate(m, word):
    g = m.expansion(word)
    assert all(len(w) in (0, m.degree-1, m.degree) for w in g), \
        'target must lie in gamma_(c-1)'
    if not m.layer(g, m.degree-1):
        result = decide_central(m, word)
        result['delegated_central'] = True
        return result
    degree = m.degree-1
    w = m.layer(g, degree)
    trace = []
    for p in range(1, degree//2 + 1):
        q = degree-p
        candidates = mixed_candidates(m,w,p,q) if p<q else equal_candidates(m,w,p)
        for i, (cc,dd) in enumerate(candidates):
            c, d = lie_tensor(m,cc,p), lie_tensor(m,dd,q)
            assert bracket(m,c,d) == w
            xx, yy = m.lift(cc,p), m.lift(dd,q)
            base = m.comm(xx,yy)
            residual = m.mul(m.inv(base),g)
            assert all(len(t) in (0,m.degree) for t in residual)
            columns = ([bracket(m,m.layer(h['value'],p+1),d)
                        for h in m.bydegree[p+1]]
                       + [bracket(m,c,m.layer(h['value'],q+1))
                          for h in m.bydegree[q+1]])
            correction = linear_solution(columns,m.layer(residual,m.degree))
            record = dict(p=p,q=q,branch=i,total_branches=len(candidates),
                          C=cc,D=dd,soluble=correction is not None)
            trace.append(record)
            if correction is None:
                continue
            vector, kernel = correction
            cut = len(m.bydegree[p+1])
            x = m.mul(xx,m.lift(vector[:cut],p+1))
            y = m.mul(yy,m.lift(vector[cut:],q+1))
            assert m.comm(x,y) == g
            record.update(correction=vector,kernel_dimension=len(kernel))
            return dict(answer=True,p=p,q=q,x=m.collect(x)[0],y=m.collect(y)[0],trace=trace)
    return dict(answer=False,trace=trace)
