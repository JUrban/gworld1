#!/usr/bin/env python3
"""Connect rational and integral N5 stages for a specified class-two model.

The input describes G with a free central basis z_1,...,z_s and quotient
basis x_1,...,x_r for G/Z(G): [x_i,x_j]=product z_k^beta[i][j][k].
All generators have infinite relative order. The center must be exactly
the supplied subgroup; this is checked. This is the prior torsion-free
scope, not the complete arbitrary-input/torsion N5 implementation.
"""
from itertools import product
from math import lcm
from sympy import Matrix, Rational, eye, zeros
from n5_rational_lie_decomposition import decompose
from n5_central_constraints import saturated_basis, split


def integral_image(a):
    cols = []
    for j in range(a.cols):
        v = a[:, j]
        denom = lcm(*(Rational(x).q for x in v)) if len(v) else 1
        cols.append(list(v*denom))
    return saturated_basis(cols, a.rows)


def beta_value(beta, s, u, v):
    r = len(beta)
    return [sum(u[i]*v[j]*beta[i][j][k]
                for i in range(r) for j in range(r)) for k in range(s)]


def decide(beta, center_rank):
    r, s = len(beta), center_rank
    if s < 0 or any(len(row) != r or any(len(v) != s for v in row) for row in beta):
        raise ValueError('invalid class-two dimensions')
    if any(Rational(x).q != 1 for row in beta for v in row for x in v):
        raise ValueError('commutator coordinates must be integral')
    beta = [[[int(x) for x in v] for v in row] for row in beta]
    if any(beta[i][j][k] != -beta[j][i][k]
           for i in range(r) for j in range(r) for k in range(s)):
        raise ValueError('commutator form must be alternating')
    radical_equations = Matrix([[beta[i][j][k] for i in range(r)]
                                for j in range(r) for k in range(s)])
    if r and radical_equations.rank() != r:
        raise ValueError('specified central subgroup is not the full center')
    n = r+s
    lie = [[[0]*n for _ in range(n)] for _ in range(n)]
    for i in range(r):
        for j in range(r):
            lie[i][j][r:] = beta[i][j]
    rational = decompose(lie)
    seen = set()
    branches = []
    witness = None
    for mask in product((0, 1), repeat=len(rational['projections'])):
        p = sum((take*p for take, p in zip(mask, rational['projections'])), zeros(n))
        q = p[:r, :r]
        assert p[:r, r:] == zeros(r, s)
        assert q*q == q
        key = tuple(q)
        if key in seen:
            continue
        seen.add(key)
        a, b = integral_image(q), integral_image(eye(r)-q)
        change = a.row_join(b)
        assert change.shape == (r, r)
        index = abs(int(change.det()))
        branch = dict(mask=list(mask), quotient_projection=q,
                      quotient_bases=[a, b], quotient_index=index)
        branches.append(branch)
        if index != 1:
            branch['outcome'] = 'quotient_lattice_obstruction'
            continue
        assert all(not any(beta_value(beta, s, a[:, i], b[:, j]))
                   for i in range(a.cols) for j in range(b.cols))
        constraints = []
        for side, basis in enumerate((a, b), 1):
            for i in range(basis.cols):
                for j in range(i+1, basis.cols):
                    constraints.append((side, beta_value(beta, s, basis[:, i], basis[:, j]), 0))
        central = split(s, [], constraints, (a.cols == 0, b.cols == 0))
        branch['constraints'] = constraints
        if central is None:
            branch['outcome'] = 'central_splitting_obstruction'
            continue
        central_bases = [integral_image(central), integral_image(eye(s)-central)]
        factors = []
        for basis, z in zip((a, b), central_bases):
            factors.append([list(basis[:, i])+[0]*s for i in range(basis.cols)]
                           + [[0]*r+list(z[:, i]) for i in range(z.cols)])
        branch['outcome'] = 'decomposition'
        branch['central_projection'] = central
        branch['central_bases'] = central_bases
        branch['factor_generators'] = factors
        witness = len(branches)-1
        break
    return dict(quotient_rank=r, center_rank=s, beta=beta,
                lie_structure_constants=lie, rational=rational,
                answer=witness is not None, witness_branch=witness,
                branches=branches)
