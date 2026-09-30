#!/usr/bin/env python3
"""Complete leading branches following Section 2 of N8/general-proof.md.

Unequal weights: finite projective charts, rational points, and *all*
signed integral scale allocations. Equal weights: oriented Hermite bases
of the integral exterior support plane. No block-quadratic factor step
is called. This module does not implement later nonlinear group lifting.
"""
from fractions import Fraction
from functools import reduce
from math import gcd

from sympy import divisors

from n8_projective_factors import all_mixed_factors


def leading_pairs(m, target, p, q):
    """Return (pairs, trace); equal-weight pairs are modulo exact SL2 moves."""
    assert 1 <= p <= q and p + q <= m.degree and target
    assert all(len(word) == p + q for word in target)
    if p == q:
        from n8_leading_pairs_hall import equal_candidates
        pairs = equal_candidates(m, target, p)
        return pairs, {'method': 'exterior-Hermite', 'representatives': len(pairs)}

    directions, charts = all_mixed_factors(m, target, p, q)
    answer, allocations = [], []
    for row in directions:
        c = row['c']
        d = [Fraction(value) for value in row['d']]
        assert reduce(gcd, (abs(value) for value in c), 0) == 1
        integral = all(value.denominator == 1 for value in d)
        assert integral == row['integral']
        if not integral:
            allocations.append({'C0': c, 'D0': row['d'], 'signed_scales': []})
            continue
        d = [int(value) for value in d]
        content = reduce(gcd, (abs(value) for value in d), 0)
        assert content > 0, 'Nonzero target has nonzero second factor'
        scales = [sign * int(k) for k in divisors(content) for sign in (1, -1)]
        for k in scales:
            assert all(value % k == 0 for value in d)
            answer.append(([k * value for value in c], [value // k for value in d]))
        allocations.append({'C0': c, 'D0': d, 'content': content, 'signed_scales': scales})
    assert len({(tuple(c), tuple(d)) for c, d in answer}) == len(answer)
    return answer, {'method': 'projective-rational-points-and-signed-divisors',
                    'charts': charts, 'allocations': allocations}
