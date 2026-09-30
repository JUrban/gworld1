#!/usr/bin/env python3
"""Complete the retained rank-two atom alphabet by all terminal b-powers.

No larger bridge enumeration is performed. Infinite tails are geometric;
finite suffix controls do not replace the written orbit/factorization proof.
"""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from g9_flow_unfolding import bridge, endpoint, flow


def core_of(word):
    edges = flow(2, word)
    h, y = endpoint(2, edges)
    core = tuple((v[0], v[1], j+1, c) for v, j, c in edges if not (v[0] == h and j == 1))
    return (h, core), y


def atom(word):
    if not bridge(2, word):
        return False
    edges = flow(2, word)
    height, _ = endpoint(2, edges)
    crossings = Counter(v[0] for v, j, c in edges if j == 0)
    return all(crossings[h] != 1 for h in range(1, height))


def gap(value):
    if isinstance(value, (list, tuple)):
        return '['+','.join(gap(x) for x in value)+']'
    if isinstance(value, dict):
        return 'rec('+','.join(k+':='+gap(v) for k, v in value.items())+')'
    return json.dumps(value)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    args = p.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    source = Path('research/certificates/G9-bridge-atoms/certificate.json')
    raw = source.read_bytes()
    original = json.loads(raw)
    words = [tuple(w) for w in original['word_certificates']]
    groups = defaultdict(list)
    for i, word in enumerate(words):
        assert atom(word)
        core, y = core_of(word)
        groups[core].append((y, len(word), i))
    centers, tails = Counter(), Counter()
    records = []
    suffix_checks = 0
    for (height, core), points in sorted(groups.items()):
        points.sort()
        assert len({y for y, length, i in points}) == len(points)
        low, high = points[0][0], points[-1][0]
        costs = []
        chosen = []
        for y in range(low, high+1):
            value, i = min((length+abs(y-x), i) for x, length, i in points)
            costs.append(value)
            chosen.append(i)
            centers[value] += 1
        tails[costs[0]+1] += 1
        tails[costs[-1]+1] += 1
        # Check every central representative and two actual points on each tail.
        targets = list(range(low, high+1))+[low-1, low-3, high+1, high+3]
        for y in targets:
            cost, x, i = min((length+abs(y-x), x, i) for x, length, i in points)
            delta = y-x
            word = words[i]+((2 if delta >= 0 else -2),)*abs(delta)
            assert len(word) == cost and atom(word)
            assert core_of(word) == ((height, core), y)
            suffix_checks += 1
        # Every old alphabet element occurs at no greater representative cost.
        assert all(costs[y-low] <= length for y, length, i in points)
        records.append(dict(height=height, core=core, points=points, low=low, high=high,
                            costs=costs, chosen_indices=chosen,
                            left_tail_start=costs[0]+1, right_tail_start=costs[-1]+1))
    degree = max(max(centers, default=0)+1, max(tails, default=0))
    central = [centers[i] for i in range(degree+1)]
    tail = [tails[i] for i in range(degree+1)]
    # F(z) = C(z) + T(z)/(1-z). N=(1-z)C+T is finite.
    numerator = [centers[i]+tails[i]-centers[i-1] for i in range(degree+1)]
    counts = [centers[i]+sum(tails[j] for j in range(i+1)) for i in range(degree+1)]
    old_counts = original['counts_by_minimum_bridge_length']
    assert counts[:len(old_counts)] == old_counts

    def excess(integer, denominator):
        # Sign of (1-z)*(F(z)-1), with z=denominator/integer.
        coefficients = list(numerator)
        coefficients[0] -= 1
        coefficients[1] += 1
        return sum(c*denominator**j*integer**(degree-j) for j, c in enumerate(coefficients))

    denominator = 10**9
    low, high = denominator+1, 3*denominator
    assert excess(low, denominator) > 0 and excess(high, denominator) < 0
    while high-low > 1:
        mid = (low+high)//2
        if excess(mid, denominator) >= 0:
            low = mid
        else:
            high = mid
    assert low > original['lower_bound']['numerator']
    assert high < 2943737759
    result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  scope='All terminal horizontal powers of the existing certified atoms; no new bridge enumeration',
                  source=str(source), source_sha256=hashlib.sha256(raw).hexdigest(),
                  original_atoms=len(words), distinct_orbits=len(records), suffix_controls=suffix_checks,
                  original_cost_counts=old_counts, extended_initial_counts=counts,
                  central_coefficients=central, tail_coefficients=tail,
                  rational_numerator=numerator,
                  lower_numerator=low, root_upper_numerator=high, denominator=denominator,
                  lower_polynomial_excess=str(excess(low, denominator)),
                  upper_polynomial_excess=str(excess(high, denominator)),
                  orbit_records=records)
    (out/'certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    export={key:result[key] for key in ['original_atoms','distinct_orbits','original_cost_counts',
            'extended_initial_counts','central_coefficients','tail_coefficients','rational_numerator',
            'lower_numerator','root_upper_numerator','denominator','orbit_records']}
    (out/'fixtures.g').write_text('G9Horizontal:='+gap(export)+';\n')
    print(json.dumps({key:result[key] for key in ['original_atoms','distinct_orbits','suffix_controls',
                     'central_coefficients','tail_coefficients','lower_numerator','root_upper_numerator','denominator']}, indent=2))
    print('PASS G9 horizontal atom completion')


if __name__ == '__main__':
    main()
