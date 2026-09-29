#!/usr/bin/env python3
"""Alternative unequal-weight homogeneous bracket algorithm via finite charts.

Does not use the rotation lemma or block-quadratic factorization. See
problems/N8/projective-factor-audit.md. Exact QQ Groebner arithmetic; no
efficiency guarantee. The input target is nonzero and homogeneous.
"""
from functools import reduce
from itertools import product
from math import gcd, lcm

from sympy import Matrix, Poly, QQ, groebner, symbols

from n8_ia_orbits import add


def bracket(m, c, d):
    return add(m.mul(c, d), m.mul(d, c), -1)


def rational_points(equations, variables):
    """All rational points of a zero-dimensional affine QQ scheme."""
    equations = [f for f in equations if f != 0]
    gb = groebner(equations, *variables, order='lex', domain=QQ)
    trace = {'groebner': [str(f.as_expr()) for f in gb.polys]}
    if len(gb.polys) == 1 and gb.polys[0].as_expr() == 1:
        trace.update(dimension=0, rational_points=0)
        return [], trace
    if not gb.is_zero_dimensional:
        raise ValueError('Positive-dimensional chart: finite-fibre hypothesis failed')
    leading = [p.LM(order=gb.order).exponents for p in gb.polys]
    bounds = []
    for j in range(len(variables)):
        pure = [ex[j] for ex in leading
                if ex[j] and all(ex[k] == 0 for k in range(len(variables)) if k != j)]
        assert pure, 'Zero-dimensional leading ideal must contain pure powers'
        bounds.append(min(pure))
    standard = [ex for ex in product(*(range(b) for b in bounds))
                if not any(all(x >= y for x, y in zip(ex, lm)) for lm in leading)]
    positions = {ex: j for j, ex in enumerate(standard)}
    monomials = [prod_monomial(variables, ex) for ex in standard]
    roots = []
    charpolys = []
    for variable in variables:
        mat = Matrix.zeros(len(standard))
        for column, monomial in enumerate(monomials):
            remainder = Poly(gb.reduce(variable * monomial)[1], *variables, domain=QQ)
            for exponent, coefficient in remainder.terms():
                if coefficient:
                    mat[positions[exponent], column] = coefficient
        polynomial = mat.charpoly().as_poly()
        roots.append(sorted(polynomial.ground_roots()))
        charpolys.append(str(polynomial.as_expr()))
    points = []
    for point in product(*roots):
        substitution = dict(zip(variables, point))
        if all(f.subs(substitution) == 0 for f in equations):
            points.append(point)
    trace.update(dimension=len(standard), standard_monomials=[list(ex) for ex in standard],
                 characteristic_polynomials=charpolys,
                 rational_root_sets=[[str(x) for x in rr] for rr in roots],
                 rational_points=len(points))
    return points, trace


def prod_monomial(variables, exponents):
    out = 1
    for variable, exponent in zip(variables, exponents):
        out *= variable ** exponent
    return out


def all_mixed_factors(m, target, p, q):
    assert 1 <= p < q and p + q <= m.degree and target
    assert all(len(word) == p + q for word in target)
    ubasis = [m.layer(h['value'], p) for h in m.bydegree[p]]
    vbasis = [m.layer(h['value'], q) for h in m.bydegree[q]]
    products = [[bracket(m, a, b) for b in vbasis] for a in ubasis]
    words = sorted(set(target).union(*(set(t) for row in products for t in row)))
    solutions = []
    charts = []
    for first in range(len(ubasis)):
        cx = symbols('c:' + str(len(ubasis) - first - 1))
        dy = symbols('d:' + str(len(vbasis)))
        c = [0] * first + [1] + list(cx)
        equations = [sum(c[i] * dy[j] * products[i][j].get(word, 0)
                         for i in range(len(ubasis)) for j in range(len(vbasis)))
                     - target.get(word, 0) for word in words]
        points, trace = rational_points(equations, cx + dy)
        trace['first_nonzero_index'] = first
        charts.append(trace)
        for point in points:
            cc = [QQ(0)] * first + [QQ(1)] + [QQ.from_sympy(x) for x in point[:len(cx)]]
            dd = [QQ.from_sympy(x) for x in point[len(cx):]]
            denominator = lcm(*(int(x.denominator) for x in cc))
            integral_c = [int(x * denominator) for x in cc]
            content = reduce(gcd, integral_c, 0)
            integral_c = [x // content for x in integral_c]
            scale = QQ(denominator, content)
            scaled_d = [x / scale for x in dd]
            integral = all(x.denominator == 1 for x in scaled_d)
            solutions.append({'c': integral_c, 'd': [str(x) for x in scaled_d],
                              'integral': integral})
    return solutions, charts
