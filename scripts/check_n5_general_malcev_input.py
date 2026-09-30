#!/usr/bin/env python3
"""Independent exact matrix reconstruction, then the N5 Lie-stage solver."""
import json
from pathlib import Path
from sympy import Matrix, Rational, eye, zeros
from n5_rational_lie_decomposition import decompose
from check_n5_rational_lie import serial, gap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/certificates/N5-general-malcev-input'


def mat(rows):
    return Matrix([[Rational(x) for x in row] for row in rows])


def logarithm(m):
    u = m-eye(m.rows)
    assert u**m.rows == zeros(m.rows)
    return sum(((-1)**(k+1)*u**k/Rational(k) for k in range(1, m.rows)), zeros(m.rows))


def exponential(x):
    from math import factorial
    assert x**x.rows == zeros(x.rows)
    return sum((x**k/factorial(k) for k in range(x.rows)), zeros(x.rows))


def main():
    records = json.loads((OUT/'input-v1.json').read_text())
    results = []
    word_count = bracket_count = 0
    nonlinear_controls = []
    for f in records:
        h, d = f['hirsch_length'], f['matrix_dimension']
        assert f['relative_orders'] == [0]*h
        c = [[[Rational(x) for x in v] for v in row] for row in f['structure_constants']]
        if h:
            mats = [mat(x) for x in f['matrices']]
            logs = [logarithm(m) for m in mats]
            assert logs == [mat(x) for x in f['logs']]
            assert all(exponential(x) == m for x, m in zip(logs, mats))
            basis = Matrix.hstack(*(x.reshape(d*d, 1) for x in logs))
            assert basis.rank() == h
            _, rows = basis.T.rref()
            rows = list(rows)
            inverse = basis[rows, :].inv()

            def coordinates(x):
                v = x.reshape(d*d, 1)
                a = inverse*v[rows, :]
                assert basis*a == v
                return a

            for i in range(h):
                for j in range(h):
                    assert list(coordinates(logs[i]*logs[j]-logs[j]*logs[i])) == c[i][j]
                    bracket_count += 1
            # A deliberately corrupted structure constant cannot pass recovery.
            corrupted = list(c[0][0])
            corrupted[0] += 1
            assert basis*Matrix(corrupted) != zeros(d*d, 1)
            for w in f['word_checks']:
                m = eye(d)
                for x, k in zip(mats, w['exponents']):
                    m *= x**k
                assert m == mat(w['matrix'])
                l = logarithm(m)
                assert exponential(l) == m
                assert list(coordinates(l)) == [Rational(x) for x in w['log_coordinates']]
                if l != m-eye(d):
                    nonlinear_controls.append((f['name'], word_count))
                word_count += 1
        result = decompose(c)
        assert result['nilclass'] == f['nilclass']
        assert result['factor_dimensions'] == f['expected_dimensions']
        results.append(serial(dict(name=f['name'], structure_constants=c,
            expected=f['expected_dimensions'], result=result)))
        print(f['name'], 'class', f['nilclass'], 'factors', result['factor_dimensions'], flush=True)
    assert nonlinear_controls
    p = next(f for f in records if f['name'] == 'finite_relative_order')
    assert 2 in p['original_relative_orders'] and p['torsion_order'] == 1
    t = next(f for f in records if f['name'] == 'noncentral_finite_torsion')
    assert t['torsion_order'] == 8 and t['hirsch_length'] == 5
    with (OUT/'decompositions-v1.json').open('x') as stream:
        json.dump(dict(records=results, checked_words=word_count,
            checked_brackets=bracket_count, linear_log_shortcut_rejections=nonlinear_controls), stream, indent=2)
        stream.write('\n')
    with (OUT/'decompositions-v1.g').open('x') as stream:
        stream.write('N5MalcevLieFixtures := '+gap(results)+';\n')
    print('PASS N5 general Malcev Python:', len(records), 'groups;', word_count,
        'native words;', bracket_count, 'brackets;', len(nonlinear_controls), 'nonlinear logs')


if __name__ == '__main__':
    main()
