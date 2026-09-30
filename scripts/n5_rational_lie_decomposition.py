#!/usr/bin/env python3
"""Exact rational direct decomposition for a finite nilpotent Lie algebra.

Input: bracket[i][j][k] in Q, with column-vector coordinates.
This supplies the rational Lie stage of N5, not its complete group algorithm.
The centroid method is established algebraic machinery, not a novelty claim.
"""
from math import comb
from sympy import Matrix, Poly, QQ, Rational, Symbol, eye, zeros

t = Symbol('t')


def columns(vectors, n):
    a = Matrix.hstack(*vectors) if vectors else zeros(n, 0)
    return Matrix.hstack(*a.columnspace()) if a.cols else a


def bracket(c, x, y):
    n = len(c)
    out = zeros(n, 1)
    for i in range(n):
        if not x[i]:
            continue
        for j in range(n):
            if y[j]:
                out += x[i] * y[j] * Matrix(c[i][j])
    return out


def validate(c):
    n = len(c)
    if any(len(row) != n or any(len(v) != n for v in row) for row in c):
        raise ValueError('invalid structure-constant dimensions')
    c = [[[Rational(x) for x in v] for v in row] for row in c]
    if not n:
        return c, 0
    basis = eye(n)
    for i in range(n):
        for j in range(n):
            if Matrix(c[i][j]) != -Matrix(c[j][i]):
                raise ValueError('bracket is not alternating')
            for k in range(j + 1, n):
                jacobi = (bracket(c, Matrix(c[i][j]), basis[:, k])
                          + bracket(c, Matrix(c[j][k]), basis[:, i])
                          + bracket(c, Matrix(c[k][i]), basis[:, j]))
                if any(jacobi):
                    raise ValueError('Jacobi identity fails')
    lower = basis
    for nilclass in range(1, n + 1):
        lower = columns([bracket(c, lower[:, i], basis[:, j])
                         for i in range(lower.cols) for j in range(n)], n)
        if not lower.cols:
            return c, nilclass
    raise ValueError('Lie algebra is not nilpotent')


def in_span(a, v):
    return a.row_join(v).rank() == a.cols


def transform(c, basis):
    """Structure constants in an invertible new column basis."""
    inverse = basis.inv()
    return [[list(inverse * bracket(c, basis[:, i], basis[:, j]))
             for j in range(basis.cols)] for i in range(basis.cols)]


def central_split(c):
    n = len(c)
    derived = columns([Matrix(c[i][j]) for i in range(n)
                       for j in range(i + 1, n)], n)
    equations = Matrix([[c[i][j][k] for i in range(n)]
                        for j in range(n) for k in range(n)])
    center = equations.nullspace()
    together = derived
    central = []
    for z in center:
        if not in_span(together, z):
            central.append(z)
            together = together.row_join(z)
    stem = derived
    for v in eye(n).columnspace():
        if not in_span(together, v):
            stem = stem.row_join(v)
            together = together.row_join(v)
    a = Matrix.hstack(*central) if central else zeros(n, 0)
    basis = stem.row_join(a)
    assert basis.cols == n and basis.det() != 0
    changed = transform(c, basis)
    d = stem.cols
    assert all(not any(changed[i][j][d:]) for i in range(n) for j in range(n))
    assert all(not any(changed[i][j]) for i in range(d, n) for j in range(n))
    return basis, [[changed[i][j][:d] for j in range(d)] for i in range(d)]


def centroid_equations(c):
    n = len(c)
    rows = []
    # Flatten T by rows: variable T[a,b] has index a*n+b.
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for side in (0, 1):
                    row = [0] * (n*n)
                    for v in range(n):
                        row[k*n+v] += c[i][j][v]
                        if side == 0:
                            row[v*n+i] -= c[v][j][k]
                        else:
                            row[v*n+j] -= c[i][v][k]
                    rows.append(row)
    return Matrix(rows)


def eval_poly(poly, a):
    out = zeros(a.rows)
    for coef in poly.all_coeffs():
        out = out*a + coef*eye(a.rows)
    return out


def decompose(c):
    c, nilclass = validate(c)
    n = len(c)
    if not n:
        return dict(dimension=0, nilclass=0, basis_change=eye(0),
                    stem_dimension=0, projections=[], factor_dimensions=[])
    basis, stem = central_split(c)
    d = len(stem)
    stem_projections = []
    info = {}
    if d:
        equations = centroid_equations(stem)
        centroid = [Matrix(d, d, list(v)) for v in equations.nullspace()]
        gram = Matrix([[(a*b).trace() for b in centroid] for a in centroid])
        degree = gram.rank()
        assert degree >= 1
        # Every pair of distinct absolute characters differs on this
        # polynomial in k, of degree < len(centroid).
        bound = comb(degree, 2) * (len(centroid)-1)
        for k in range(bound + 1):
            element = sum((k**i * a for i, a in enumerate(centroid)), zeros(d))
            characteristic = Poly(element.charpoly(t).as_expr(), t, domain=QQ)
            if characteristic.sqf_part().degree() == degree:
                break
        else:
            raise AssertionError('proved character-separation bound failed')
        factors = characteristic.factor_list()[1]
        crt_polynomials = []
        for irreducible, multiplicity in factors:
            modulus = irreducible**multiplicity
            other = characteristic.exquo(modulus)
            polynomial = (other * other.invert(modulus)).rem(characteristic)
            projection = eval_poly(polynomial, element)
            assert projection**2 == projection and projection.rank() > 0
            stem_projections.append(projection)
            crt_polynomials.append(polynomial)
        assert sum(stem_projections, zeros(d)) == eye(d)
        assert all(a*b == zeros(d) for i, a in enumerate(stem_projections)
                   for j, b in enumerate(stem_projections) if i != j)
        info = dict(centroid_basis=centroid, trace_gram=gram,
                    semisimple_dimension=degree, separation_bound=bound,
                    chosen_k=k, separating_element=element,
                    characteristic=characteristic,
                    irreducible_factors=factors, crt_polynomials=crt_polynomials)
    projections = []
    for p in stem_projections:
        q = zeros(n)
        q[:d, :d] = p
        projections.append(basis*q*basis.inv())
    for i in range(d, n):
        q = zeros(n)
        q[i, i] = 1
        projections.append(basis*q*basis.inv())
    assert sum(projections, zeros(n)) == eye(n)
    for p in projections:
        for i in range(n):
            for j in range(n):
                assert p*Matrix(c[i][j]) == bracket(c, p[:, i], eye(n)[:, j])
                assert p*Matrix(c[i][j]) == bracket(c, eye(n)[:, i], p[:, j])
    return dict(dimension=n, nilclass=nilclass, basis_change=basis,
                stem_dimension=d, projections=projections,
                factor_dimensions=sorted(p.rank() for p in projections), **info)
