#!/usr/bin/env python3
"""Bounded end-to-end checks of the constructive M0 proof, seed 9282626."""
import json
from pathlib import Path
import random

from check_m0_finite_fields import comm, compose, identity, inverse, random_basis
from m0_witness import witness

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'research/certificates/M0-constructor'


def main():
    rng = random.Random(9282626)
    cases = []
    def add(name, images, expected=None, bound=9):
        cases.append((name, images, expected, bound))

    add('rank1_zero', [[]], 'nonautomorphism_certificate')
    add('rank1_double', [[1, 1]], 'nonautomorphism_certificate')
    add('rank1_inverse', [[-1]], 'metabelian_automorphism')
    add('abelian_singular', [[1, 2], [1, 2]], 'nonautomorphism_certificate')
    add('abelian_det6', [[1, 1], [2, 2, 2]], 'nonautomorphism_certificate')
    add('prime_bound', [[1]*11], 'inconclusive_bound', 7)

    # Modulo 3 the nontrivial part vanishes; modulo 2 its first possible
    # torus zero requires F4. This is selected by the search, not supplied.
    ext = identity(3)
    ext[0] += [3]+inverse(comm([1], [3]))*3+[-3]
    add('extension_field', ext, 'nonautomorphism_certificate')
    add('field_bound', ext, 'inconclusive_bound', 3)
    for n in [2, 3, 4]:
        for k in range(8):
            images = identity(n)
            for i in range(n):
                for _ in range(rng.randrange(3)):
                    a, b = rng.sample(range(1, n+1), 2)
                    u = [rng.choice([-1, 1])*a]
                    v = [rng.choice([-1, 1])*b]
                    conjugator = [rng.choice([-1, 1])*rng.randint(1, n)]
                    images[i] += conjugator+comm(u, v)+inverse(conjugator)
            # Apply independent changes on domain and range; abelianization
            # and character normalization must be computed from the input.
            left, _ = random_basis(n, rng, 2)
            right, _ = random_basis(n, rng, 2)
            add(f'random_{n}_{k}', compose(left, compose(images, right)))
        for k in range(3):
            basis, undo = random_basis(n, rng, 6)
            add(f'free_automorphism_{n}_{k}', basis, 'metabelian_automorphism')
        # A unimodular abelianization with negative pivot signs and shears.
        images = identity(n)
        images[0] += comm([1], [n])
        change, _ = random_basis(n, rng, 5)
        add(f'changed_singular_{n}', compose(change, images), 'nonautomorphism_certificate')

    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    for name, images, expected, bound in cases:
        record = witness(images, max_field_size=bound)
        record.update(name=name, images=images, bound=bound)
        if expected is not None:
            assert record['status'] == expected, (name, expected, record['status'])
        if name == 'extension_field':
            assert record['p'] == 2 and len(record['modulus']) == 3
        records.append(record)
        (OUT/'checks.json').write_text(json.dumps(dict(seed=9282626, records=records), indent=2)+'\n')
        print(name, record['status'], flush=True)

    lines = ['M0ConstructorRecords := [']
    for rec in records:
        values = dict(name=rec['name'], status=rec['status'], images=rec['images'],
                      p=rec.get('p', 0), modulus=rec.get('modulus', []),
                      chi=rec.get('chi', []), basis=rec.get('basis', []),
                      inverse=rec.get('inverse', []), expected=rec.get('fox', []),
                      image_word=rec.get('image_word', []),
                      normalization=rec.get('normalization', []),
                      normalization_inverse=rec.get('normalization_inverse', []),
                      determinant=rec.get('determinant', []))
        lines.append('rec('+','.join(k+':='+json.dumps(v) for k, v in values.items())+'),')
    lines[-1] = lines[-1].rstrip(',')
    lines.append('];')
    (OUT/'checks.g').write_text('\n'.join(lines)+'\n')
    counts = {s: sum(r['status'] == s for r in records) for s in sorted({r['status'] for r in records})}
    print(json.dumps(dict(records=len(records), counts=counts,
                         fields=sorted({r['p']**(len(r['modulus'])-1)
                                        for r in records if 'p' in r}),
                         max_basis_word=max((len(w) for r in records for w in r.get('basis', [])), default=0))))
    print('PASS M0 end-to-end witness constructor')


if __name__ == '__main__':
    main()
