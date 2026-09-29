#!/usr/bin/env python3
"""Same complete leading-pair enumeration, with integral Hall-coordinate systems.

The block-quadratic factor and Hermite-sublattice steps are unchanged from
n8_penultimate.py. Each bracket column is checked in its exact Hall layer;
the verified component-Hermite solver replaces redundant tensor equations.
"""
from functools import reduce
from itertools import combinations,product
from math import gcd
from sympy import Matrix,Poly,divisors,factor_list,symbols
from n8_central import add,bracket,primitive_lie_line
from n8_penultimate import lie_tensor
from n8_ia_orbits import factor_wedge
from n8_component_linear import affine_solution

def hall_solution(m,columns,w,degree):
    return affine_solution([m.coordinates(col,degree) for col in columns],m.coordinates(w,degree))

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
        result = hall_solution(m, columns, w, p+q)
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
    result = hall_solution(m, [bracket(m, basis[i], basis[j]) for i,j in pairs], w, 2*p)
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


