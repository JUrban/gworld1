#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from sympy import Matrix, eye
from n5_class2_torsionfree import decide, beta_value
from check_n5_rational_lie import serial, gap


def gap_record(x):
    if x is None:
        return 'fail'
    if isinstance(x, dict):
        return 'rec(' + ','.join(k+':='+gap_record(v) for k,v in x.items()) + ')'
    if isinstance(x, list):
        return '[' + ','.join(gap_record(v) for v in x) + ']'
    return gap(x)


def form(r, s, entries):
    beta = [[[0]*s for _ in range(r)] for _ in range(r)]
    for i, j, v in entries:
        beta[i][j] = v
        beta[j][i] = [-x for x in v]
    return beta


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    fixtures = [
        ('trivial', [], 0, False), ('cyclic', [], 1, False),
        ('abelian2', [], 2, True),
        ('heisenberg', form(2,1,[(0,1,[1])]), 1, False),
        ('heisenberg_scaled', form(2,1,[(0,1,[6])]), 1, False),
        ('heisenberg_central', form(2,2,[(0,1,[2,3])]), 2, True),
        ('two_heisenbergs', form(4,2,[(0,1,[1,0]),(2,3,[0,1])]), 2, True),
        ('quotient_glue2', form(4,2,[(0,1,[1,0]),(0,3,[0,1]),(2,3,[0,2])]), 2, False),
        ('center_glue2', form(4,2,[(0,1,[2,1]),(2,3,[0,1])]), 2, False),
        ('scaled_product', form(4,2,[(0,1,[2,0]),(2,3,[0,3])]), 2, True),
        ('heisenberg5', form(4,1,[(0,1,[1]),(2,3,[1])]), 1, False),
    ]
    # Basis changes are integral unimodular, preserving the actual group
    # rather than just its rational completion.
    for name, beta, s, expected in list(fixtures)[6:10]:
        r = len(beta)
        u = eye(r)
        u[0,2] = 2
        u[1,3] = -1
        z = Matrix([[1,1],[0,1]])
        changed = [[list(z.inv()*Matrix(beta_value(beta,s,u[:,i],u[:,j])))
                    for j in range(r)] for i in range(r)]
        fixtures.append((name+'_integral_basis', changed, s, expected))
    records, lies = [], []
    for name, beta, s, expected in fixtures:
        result = decide(beta, s)
        assert result['answer'] == expected, (name, result)
        # Rational factor counts alone give a false positive on BOTH
        # gluing controls. The negative answer must survive all branches.
        if 'glue' in name:
            assert result['rational']['factor_dimensions'] == [3,3]
        records.append(serial(dict(name=name, expected=expected, result=result)))
        lies.append(serial(dict(name=name, structure_constants=result['lie_structure_constants'],
                     expected=result['rational']['factor_dimensions'], result=result['rational'])))
        print(json.dumps({'name':name, 'answer':expected,
                          'rational_factors':result['rational']['factor_dimensions'],
                          'branch_outcomes':[b['outcome'] for b in result['branches']]}), flush=True)
    try:
        decide(form(1,1,[]),1)
    except ValueError as error:
        rejected = str(error)
    else:
        raise AssertionError('improper supplied center accepted')
    cert = dict(records=records, rejected_incomplete_center=rejected)
    (args.output/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    (args.output/'certificate.g').write_text('N5Class2Fixtures := '+gap_record(records)+';\n'
                                           +'N5LieFixtures := '+gap_record(lies)+';\n')
    print('PASS N5 class2 pipeline:',len(records),'fixtures; exact-center rejection')


if __name__ == '__main__':
    main()
