#!/usr/bin/env python3
"""Reproducible exact controls for the N5 rational Lie decomposition stage."""
import argparse
import json
import random
from pathlib import Path
from sympy import Matrix, Poly, Rational, eye
from n5_rational_lie_decomposition import decompose, transform


def empty(n):
    return [[[0]*n for _ in range(n)] for _ in range(n)]


def put(c, i, j, k, value):
    c[i][j][k] = value
    c[j][i][k] = -value


def heisenberg(q=None):
    if q is None:
        c = empty(3)
        put(c, 0, 1, 2, 1)
        return c
    # Restriction of scalars from Q[z]/(z^2-q): x,zx,y,zy,w,zw.
    c = empty(6)
    put(c, 0, 2, 4, 1)
    put(c, 0, 3, 5, 1)
    put(c, 1, 2, 5, 1)
    put(c, 1, 3, 4, q)
    return c


def direct_sum(*factors):
    c = empty(sum(map(len, factors)))
    offset = 0
    for f in factors:
        for i in range(len(f)):
            for j in range(len(f)):
                for k in range(len(f)):
                    c[offset+i][offset+j][offset+k] = f[i][j][k]
        offset += len(f)
    return c


def serial(x):
    if isinstance(x, Matrix):
        return [[serial(v) for v in row] for row in x.tolist()]
    if isinstance(x, Poly):
        return [serial(v) for v in reversed(x.all_coeffs())]
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serial(v) for v in x]
    if isinstance(x, (int, str, bool)) or x is None:
        return x
    value = Rational(x)
    return str(value) if value.q != 1 else int(value)


def gap(x):
    if isinstance(x, dict):
        return 'rec(' + ','.join(k+':='+gap(v) for k, v in x.items()) + ')'
    if isinstance(x, list):
        return '[' + ','.join(gap(v) for v in x) + ']'
    if isinstance(x, str):
        try:
            Rational(x)
        except Exception:
            return json.dumps(x)
        return x
    return str(x).lower() if isinstance(x, bool) else str(x)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    filiform = empty(4)
    put(filiform, 0, 1, 2, 1)
    put(filiform, 0, 2, 3, 1)
    h5 = empty(5)
    put(h5, 0, 1, 4, 1)
    put(h5, 2, 3, 4, 1)
    mixed = direct_sum(heisenberg(2), heisenberg(3))
    fixtures = [
        ('zero', empty(0), []), ('abelian3', empty(3), [1, 1, 1]),
        ('heisenberg3', heisenberg(), [3]), ('filiform4', filiform, [4]),
        ('heisenberg5', h5, [5]), ('quadratic_field2', heisenberg(2), [6]),
        ('dual_numbers', heisenberg(0), [6]),
        ('split_quadratic', heisenberg(1), [3, 3]),
        ('mixed_fields', mixed, [6, 6]),
        ('repeated_field', direct_sum(heisenberg(2), heisenberg(2)), [6, 6]),
        ('central_factor', direct_sum(heisenberg(2), empty(2)), [1, 1, 6]),
        ('mixed_classes', direct_sum(heisenberg(), filiform, empty(1)), [1, 3, 4]),
    ]
    rng = random.Random(9302605)
    for tag, c, expected in list(fixtures)[5:]:
        n = len(c)
        change = eye(n)
        for _ in range(2*n):
            i, j = rng.sample(range(n), 2)
            change[:, j] += rng.choice([-2, -1, 1, 2])*change[:, i]
        change[:, 0] *= Rational(1, 2)
        fixtures.append((tag+'_rational_basis', transform(c, change), expected))
    records = []
    for tag, c, expected in fixtures:
        result = decompose(c)
        assert result['factor_dimensions'] == expected, (tag, result['factor_dimensions'])
        records.append(serial(dict(name=tag, structure_constants=c, expected=expected, result=result)))
        print(json.dumps({'fixture':tag, 'dimensions':expected,
                          'centroid_dimension':len(result.get('centroid_basis',[])),
                          'chosen_k':result.get('chosen_k')}), flush=True)
    invalid = empty(3)
    put(invalid, 0, 1, 2, 1)
    put(invalid, 1, 2, 1, 1)
    nonnilpotent = empty(2)
    put(nonnilpotent, 0, 1, 1, 1)
    rejected = []
    for name, c in [('bad_dimensions', [[[1]] , []]),
                    ('bad_jacobi', invalid), ('nonnilpotent', nonnilpotent)]:
        try:
            decompose(c)
        except ValueError as error:
            rejected.append({'name':name, 'reason':str(error)})
        else:
            raise AssertionError(('invalid input accepted', name))
    (args.output/'certificate.json').write_text(json.dumps({'seed':9302605,
        'records':records, 'negative_controls':rejected}, indent=2)+'\n')
    (args.output/'certificate.g').write_text('N5LieFixtures := '+gap(records)+';\n')
    print('PASS N5 rational Lie decomposition:',len(records),'fixtures;',len(rejected),'rejections')


if __name__ == '__main__':
    main()
