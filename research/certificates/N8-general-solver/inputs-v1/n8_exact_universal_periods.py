#!/usr/bin/env python3
"""Callable exact universal periods, generalized from delayed-gauge controls.

Uses check_n8_delayed_gauges.py's proved degree bound and coefficient clearing,
not the older bounded factorial search. This is a stage of the N8 candidate.
"""
from fractions import Fraction as Q
from math import lcm
import sympy as S
from check_n8_polynomial_group_tail import Group
from n8_weighted_automorphisms import add, scale
from n8_universal_gauges import poly_json, terms_json
from parametric_integer_linear import T, encode_poly


def exact_period(m, direction, offset, expansion=None):
    p, q = m.weights
    assert offset > 0 and p+q+offset <= m.degree
    assert all(m.weight(w) == weight+offset
               for value, weight in zip(direction, (p, q)) for w in value)
    assert not add(m.bracket(direction[0], m.letters[1]),
                   m.bracket(m.letters[0], direction[1]))
    sigma, tau, W = expansion or m.darboux()

    def maps(n):
        return [m.substitute(m.exp_derivation(x, direction, n), sigma) for x in tau]

    def coordinates(n):
        return [dict(m.collect(m.exp(x))) for x in maps(n)]

    trial = coordinates(1)+coordinates(-1)
    polynomials = None
    if all(x.denominator == 1 for row in trial for x in row.values()):
        power, method = 1, 'verified-unit-period'
    else:
        # A coefficient with parameter degree j has weight >= j*offset.
        # Collection preserves that filtration, so this is an a priori bound.
        bound = m.degree//offset
        samples = [coordinates(n) for n in range(bound+1)]
        polynomials = [[S.interpolate([(n, S.Rational(samples[n][side].get(i, Q(0))))
                         for n in range(bound+1)], T).expand()
                        for i in range(len(m.hall))] for side in range(2)]
        denominators = []
        for side, row in enumerate(polynomials):
            for i, f in enumerate(row):
                assert f.subs(T, 0) == int(i == side)
                denominators += [int(S.Poly(f, T).nth(j).q) for j in range(1, bound+1)]
        power = lcm(1, *denominators)
        method = 'all-polynomial-coefficients'
        for n in (-1, bound+1, power, -power):
            actual = coordinates(n)
            assert all(S.Rational(actual[side].get(i, Q(0))) == f.subs(T, n)
                       for side, row in enumerate(polynomials) for i, f in enumerate(row))
    plus, minus = maps(power), maps(-power)
    coords = [m.collect(m.exp(x)) for x in plus+minus]
    assert all(x.denominator == 1 for row in coords for _, x in row)
    assert m.substitute(W, plus) == W and m.substitute(W, minus) == W
    for i, weight in enumerate((p, q)):
        assert m.substitute(plus[i], minus) == m.letters[i]
        assert m.substitute(minus[i], plus) == m.letters[i]
        delta = add(plus[i], m.letters[i], -1)
        assert all(m.weight(w) >= weight+offset for w in delta)
        assert m.layer(delta, weight+offset) == scale(direction[i], power)
    record = dict(offset=offset, power=power, method=method,
        direction=[poly_json(x) for x in direction],
        plus=[terms_json(x) for x in coords[:2]], minus=[terms_json(x) for x in coords[2:]])
    if polynomials is not None:
        record.update(degree_bound=m.degree//offset,
            polynomials=[[encode_poly(f) for f in row] for row in polynomials])
    return record
