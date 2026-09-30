#!/usr/bin/env python3
"""Complete central lifting on a supplied complete N5 quotient-branch list."""
from sympy import eye
from n5_central_constraints import split, relation_constraints, lifting_corrections
from check_n5_rational_lie import serial


def solve(data):
    orders = data['center_orders']
    n = orders.count(0)
    assert all(d == 0 for d in orders[:n]) and all(d > 1 for d in orders[n:])
    results = []
    witness = None
    for index, branch in enumerate(data['branches']):
        parts = branch['parts']
        constraints = []
        for side, part in enumerate(parts, 1):
            constraints += relation_constraints(part['exponents'], part['defects'], n, orders[n:], side)
        p = split(n, orders[n:], constraints, tuple(part['require_nontrivial_center'] for part in parts))
        result = dict(branch=index+1, constraints=constraints, answer=p is not None)
        if p is not None:
            corrections = [lifting_corrections(part['exponents'], part['defects'],
                len(part['lifts']), n, orders[n:], side, p) for side, part in enumerate(parts, 1)]
            result.update(central_projection=p, corrections=corrections)
            if witness is None:
                witness = index+1
        results.append(serial(result))
    return dict(answer=witness is not None, witness_branch=witness, branches=results)
