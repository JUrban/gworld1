#!/usr/bin/env python3
"""Exact all-parameter first-column obstruction probe; no braid search."""
import json
from pathlib import Path

import sympy as sp


def main():
    n = sp.Symbol('n', integer=True)
    m = sp.Symbol('m', nonnegative=True, integer=True)
    identity = sp.eye(6)
    generators = []
    for i in range(5):
        g = identity.copy()
        g[i, i], g[i, i + 1], g[i + 1, i], g[i + 1, i + 1] = 2, -1, 1, 0
        assert (g - identity) ** 2 == sp.zeros(6)
        generators.append(g)
    for i, g in enumerate(generators):
        for j, h in enumerate(generators):
            if abs(i - j) == 1:
                assert g * h * g == h * g * h
            if abs(i - j) > 1:
                assert g * h == h * g
    blocks = [(1, n), (3, n-2), (2, 1-n), (3, 2), (4, -1),
              (2, 1), (1, 1), (3, n-1), (4, 2-n), (2, -n)]
    beta = identity
    shifted_inverse = identity
    for i, power in blocks:
        beta *= identity + power * (generators[i-1] - identity)
    for i, power in reversed(blocks):
        shifted_inverse *= identity - power * (generators[i] - identity)
    beta = beta.applyfunc(sp.expand)
    shifted_inverse = shifted_inverse.applyfunc(sp.expand)
    unit = identity[:, 0]
    assert all(g * unit == unit for g in generators[1:])
    assert shifted_inverse * unit == unit
    first_color = (beta * generators[0] * shifted_inverse).applyfunc(sp.expand)
    column = (beta * generators[0] * unit).applyfunc(sp.factor)
    assert first_color[:, 0].applyfunc(sp.expand) == column.applyfunc(sp.expand)
    for g in generators[:2]:
        assert all(g[row, col] == identity[row, col]
                   for row in range(3, 6) for col in range(6))
    rows = []
    for i in range(6):
        value = sp.factor(column[i])
        coefficients = list(map(int, sp.Poly(value.subs(n, m+3), m).all_coeffs()))
        sign = (all(c >= 0 for c in coefficients) and coefficients[-1] > 0) or (
            all(c <= 0 for c in coefficients) and coefficients[-1] < 0)
        rows.append({'coordinate': i+1, 'polynomial': str(value),
                     'coefficients_at_n_equals_m_plus_3_descending': coefficients,
                     'strict_constant_sign_for_n_ge_3': sign})
        print(rows[-1])
    obstruction = any(r['strict_constant_sign_for_n_ge_3'] for r in rows[3:])
    out = Path('research/certificates/B9-family-first-column-v1')
    out.mkdir(exist_ok=False)
    data = {'first_color': 'I1(beta_n)', 'parameter_range': 'integer n>=3',
            'column': rows, 'universal_partner_obstruction': obstruction,
            'scope': 'If true, excludes every braid c, without a specialness assumption.'}
    (out/'certificate.json').write_text(json.dumps(data, indent=2)+'\n')
    (out/'fixtures.g').write_text('B9FamilyFirstColumn := '+json.dumps([
        list(map(int, sp.Poly(column[i], n).all_coeffs()))[::-1]
        for i in range(6)])+';\n')
    print('Universal partner obstruction:', obstruction)
    print('PASS exact B9 family first-column probe')


if __name__ == '__main__':
    main()
