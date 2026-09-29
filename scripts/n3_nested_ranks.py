#!/usr/bin/env python3
"""Exact PBW rank predictions for a few nested nilpotent presentations.

No random sampling. The separate GAP checker constructs the groups from
ordinary group relators, without using this Lie-series calculation.
"""
import json
from pathlib import Path

CASES = [
    [(2, 1), (3, 3), (4, 5)],
    [(2, 2), (3, 4), (4, 4)],
    [(1, 1), (2, 2), (3, 5)],
    [(2, 1), (4, 4)],
    [(2, 3), (3, 3)],
]


def multiply(a, b, cutoff):
    return [sum(a[i] * b[k-i] for i in range(k+1))
            for k in range(cutoff+1)]


def next_ranks(old, added, cutoff):
    # 1/H_{U(L * Lie(X))} = 1/H_{U(L)} - |X| t.
    inverse = [1] + [0]*cutoff
    for d, rank in enumerate(old, 1):
        if d > cutoff:
            assert rank == 0
            continue
        factor = [1] + [0]*cutoff
        factor[d] = -1
        for _ in range(rank):
            inverse = multiply(inverse, factor, cutoff)
    inverse[1] -= added
    # -t D'/D = sum_n (sum_{d|n} d*l_d) t^n, D = 1/H.
    logarithmic = [0]*(cutoff+1)
    ranks = [0]*(cutoff+1)
    for n in range(1, cutoff+1):
        logarithmic[n] = -n*inverse[n] - sum(
            inverse[i]*logarithmic[n-i] for i in range(1, n))
        numerator = logarithmic[n] - sum(
            d*ranks[d] for d in range(1, n) if n % d == 0)
        assert numerator >= 0 and numerator % n == 0
        ranks[n] = numerator//n
    return ranks[1:]


def main():
    records = []
    for stages in CASES:
        old, previous, layers = [], 0, []
        for total, cutoff in stages:
            old = next_ranks(old, total-previous, cutoff)
            previous = total
            layers.append(old)
        records.append({'stages': stages, 'ranks': layers})
    # Closed free-Lie controls, including constant-class nesting.
    assert next_ranks([], 3, 5) == [3, 3, 8, 18, 48]
    assert records[-1]['ranks'][-1] == [3, 3, 8]
    target = Path('research/certificates/N3-nested-cover')
    target.mkdir(parents=True, exist_ok=True)
    (target/'ranks.json').write_text(json.dumps(records, indent=2)+'\n')
    (target/'fixtures.g').write_text('N3NestedFixtures := '+json.dumps([
        [r['stages'], r['ranks']] for r in records])+';;\n')
    print(json.dumps(records))
    print('PASS N3 nested PBW rank predictions')


if __name__ == '__main__':
    main()
