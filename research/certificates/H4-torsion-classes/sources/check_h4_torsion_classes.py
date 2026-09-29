#!/usr/bin/env python3
"""Exact finite checks for the strengthened H4 torsion-class obstruction.

No randomness. Explicit doubling orbits for n=1..4; exact Burnside sums
for n=1..8. This does not prove the all-n or free-product arguments.
"""
from math import gcd
from pathlib import Path
import json


def main():
    out = Path('research/certificates/H4-torsion-classes')
    out.mkdir(parents=True, exist_ok=True)
    assert not (out / 'checks.json').exists(), 'Never overwrite evidence'
    records = []
    fixtures = []
    for n in range(1, 9):
        q = 2 ** n
        m = 2 ** q - 1
        fixed = [gcd(2 ** j - 1, m) for j in range(q)]
        assert fixed == [2 ** gcd(j, q) - 1 for j in range(q)]
        assert sum(fixed) % q == 0
        count = sum(fixed) // q
        divisor_sum = m + sum(2 ** (n-i-1) * (2 ** (2 ** i)-1)
                              for i in range(n))
        assert divisor_sum == sum(fixed)
        assert count * q >= m
        assert m > 2 ** (q-1)
        # The infinite input adds one free generator, and no relator.
        relators = [[-(i+2), i+1, i+1] for i in range(1, n+1)]
        relators += [[n+2], [2, 1, -2, -1, -1]]
        input_size = n + 3 + sum(map(len, relators))
        assert input_size == 4*n+9
        record = dict(n=n, Q=q, M=str(m), normal_cyclic_classes=str(count),
                      finite_input_size=4*n+8, infinite_input_size=input_size,
                      strict_log2_lower_bound=q-n-1)
        if n <= 4:
            unseen = set(range(m))
            orbits = []
            while unseen:
                a = min(unseen)
                orbit = [a]
                b = 2*a % m
                while b != a:
                    assert b not in orbit
                    orbit.append(b)
                    b = 2*b % m
                assert q % len(orbit) == 0
                unseen.difference_update(orbit)
                orbits.append(orbit)
            assert len(orbits) == count
            assert sum(map(len, orbits)) == m
            # Distinct normal-cyclic elements need not be nonconjugate:
            # x and x^2 are conjugate. We count complete orbits instead.
            assert count < m
            representatives = [orbit[0] for orbit in orbits]
            record['explicit_orbit_lengths'] = {
                str(size): sum(len(o) == size for o in orbits)
                for size in sorted(set(map(len, orbits)))
            }
            fixtures.append([n, m, q, count, representatives, relators])
        records.append(record)
    (out / 'checks.json').write_text(json.dumps(records, indent=2)+'\n')
    (out / 'fixtures.g').write_text('H4TorsionFixtures := '+json.dumps(fixtures)+';\n')
    print('PASS H4 torsion classes: 8 exact formula records; 4 explicit orbit partitions')


if __name__ == '__main__':
    main()
