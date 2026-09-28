#!/usr/bin/env python3
"""Deterministic end-to-end cases for the terminating M0 construction."""
import json
from pathlib import Path

from check_m0_finite_fields import comm, compose, identity
from m0_kronecker_witness import singular_character, witness

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'research/certificates/M0-Kronecker'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cases = [
        ('rank1_zero', [[]], 'nonautomorphism_certificate'),
        ('rank1_prime11', [[1]*11], 'nonautomorphism_certificate'),
        ('rank1_inverse', [[-1]], 'metabelian_automorphism'),
        ('rank2_identity', identity(2), 'metabelian_automorphism'),
        ('rank2_abelian_singular', [[1, 2], [1, 2]], 'nonautomorphism_certificate'),
    ]
    for n in [2, 3, 4]:
        images = identity(n)
        images[0] += comm([1], [2])
        cases.append((f'cubic_extension_rank{n}', images, 'nonautomorphism_certificate'))
    images = identity(3)
    images[0] += comm([1], [-2])
    cases.append(('negative_Laurent_exponent', images, 'nonautomorphism_certificate'))
    images = identity(3)
    images[0] += comm([1], [2])*6
    cases.append(('endpoint_prime_exclusion', images, 'nonautomorphism_certificate'))
    images = identity(3)
    images[0] += comm([1], [2])
    left, right = [[1, 2], [2], [3]], [[2], [1], [-3]]
    cases.append(('domain_and_range_changes', compose(left, compose(images, right)),
                  'nonautomorphism_certificate'))
    cases.append(('free_automorphism_rank3', compose(left, right), 'metabelian_automorphism'))
    records = []
    for name, images, expected in cases:
        r = witness(images)
        r.update(name=name, images=images)
        assert r['status'] == expected
        if name.startswith('cubic_extension'):
            assert r['p'] == 2 and len(r['modulus']) == 4
        if name == 'endpoint_prime_exclusion':
            assert r['p'] == 5
        if name == 'negative_Laurent_exponent':
            assert r['kronecker']['shift'] < 0
        records.append(r)
        (OUT/'checks.json').write_text(json.dumps(dict(records=records), indent=2)+'\n')
        print(name, r['status'], r.get('p'), r.get('modulus'), flush=True)

    # Coefficient/degree edge cases for the mathematical substitution lemma.
    polys = [
        {(0, 0): 2, (1, 0): -1},
        {(0, 0): 6, (1, 0): -5},
        {(-2, 1): 1, (0, -1): -1, (2, 1): 1},
        {(0, 0): 1, (1, 0): -1, (2, 0): 1},
    ]
    polynomial_records = []
    for delta in polys:
        f, chi, _, _, t, data = singular_character(delta)
        polynomial_records.append(dict(delta=[[list(e), c] for e, c in delta.items()],
                                       p=f.p, modulus=f.modulus, chi=chi, t=t, data=data))
    (OUT/'polynomials.json').write_text(json.dumps(polynomial_records, indent=2)+'\n')

    lines = ['M0ConstructorRecords := [']
    for r in records:
        values = dict(name=r['name'], status=r['status'], images=r['images'],
                      p=r.get('p', 0), modulus=r.get('modulus', []),
                      chi=r.get('chi', []), basis=r.get('basis', []),
                      inverse=r.get('inverse', []), expected=r.get('fox', []),
                      image_word=r.get('image_word', []),
                      normalization=r.get('normalization', []),
                      normalization_inverse=r.get('normalization_inverse', []),
                      determinant=r.get('determinant', []))
        lines.append('rec('+','.join(k+':='+json.dumps(v) for k, v in values.items())+'),')
    lines[-1] = lines[-1].rstrip(',')
    lines.append('];')
    (OUT/'checks.g').write_text('\n'.join(lines)+'\n')
    counts = {s: sum(r['status'] == s for r in records)
              for s in sorted({r['status'] for r in records})}
    print(json.dumps(dict(records=len(records), counts=counts,
                         fields=sorted({r['p']**(len(r['modulus'])-1)
                                        for r in records if 'p' in r}),
                         max_basis_word=max(len(w) for r in records for w in r.get('basis', [])))))
    print('PASS M0 Kronecker witness constructor')


if __name__ == '__main__':
    main()
