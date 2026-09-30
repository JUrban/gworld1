#!/usr/bin/env python3
"""Complete bridge atoms by independent bottom/top horizontal displacements.

The infinite orbit classification and geometric tails are justified in the
accompanying proof. This exports finite, exactly checkable orbit data only.
"""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from g9_flow_unfolding import bridge, endpoint, flow


def atom(word):
    if not bridge(2, word):
        return False
    edges = flow(2, word)
    height, _ = endpoint(2, edges)
    crossings = Counter(v[0] for v, j, c in edges if j == 0)
    return all(crossings[h] != 1 for h in range(1, height))


def coordinates(word):
    edges = flow(2, word)
    height, y = endpoint(2, edges)
    assert height >= 2 and ((0, 0), 0, 1) in edges
    x = min(v[1] for v, j, c in edges if j == 0 and v[0] == 1)
    core = tuple((v[0], v[1]-x, j+1, c) for v, j, c in edges
                 if not (j == 0 and v[0] == 0)
                 and not (j == 1 and v[0] in (1, height)))
    assert core
    return (height, core), (x, y-x)


def act(word, k, ell):
    assert word[0] == 1
    return ((1,) + (2 if k >= 0 else -2,)*abs(k) + word[1:]
            + (2 if ell >= 0 else -2,)*abs(ell))


def gap(value):
    if isinstance(value, (list, tuple)):
        return '['+','.join(gap(x) for x in value)+']'
    if isinstance(value, dict):
        return 'rec('+','.join(k+':='+gap(v) for k, v in value.items())+')'
    return json.dumps(value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    source = Path('research/certificates/G9-bridge-atoms/certificate.json')
    raw = source.read_bytes()
    original = json.loads(raw)
    words = [tuple(w) for w in original['word_certificates']]
    groups = defaultdict(list)
    height_one = []
    for index, word in enumerate(words):
        assert atom(word)
        height, y = endpoint(2, flow(2, word))
        if height == 1:
            representative = (1,)+(2 if y >= 0 else -2,)*abs(y)
            assert flow(2, representative) == flow(2, word)
            assert len(representative) == len(word)
            height_one.append([y, len(word), index])
        else:
            key, (x, z) = coordinates(word)
            groups[key].append((x, z, len(word), index))
    assert len({p[0] for p in height_one}) == len(height_one)
    centers, strips, quadrants = Counter({1: 1}), Counter({2: 2}), Counter()
    records = []
    checks = Counter()
    for (height, core), points in sorted(groups.items()):
        points.sort()
        assert len({(x, z) for x, z, cost, i in points}) == len(points)
        xmin, xmax = min(p[0] for p in points), max(p[0] for p in points)
        zmin, zmax = min(p[1] for p in points), max(p[1] for p in points)

        def envelope(x, z):
            return min((cost+abs(x-x0)+abs(z-z0), i, x0, z0)
                       for x0, z0, cost, i in points)

        def check(x, z):
            cost, index, x0, z0 = envelope(x, z)
            word = act(words[index], x-x0, z-z0)
            assert len(word) == cost and atom(word)
            assert coordinates(word) == ((height, core), (x, z))
            return cost, index

        base_x, base_z, _, base_index = points[0]
        for x, z, cost, index in points:
            assert flow(2, act(words[base_index], x-base_x, z-base_z)) == flow(2, words[index])
            checks['original_flow_equalities'] += 1
        # Composition is checked on actual complete flows, including cancellation.
        assert flow(2, act(act(words[base_index], -2, 3), 1, -2)) == flow(2, act(words[base_index], -1, 1))
        checks['action_compositions'] += 1
        costs, chosen = [], []
        for x in range(xmin, xmax+1):
            row_costs, row_chosen = [], []
            for z in range(zmin, zmax+1):
                cost, index = check(x, z)
                row_costs.append(cost)
                row_chosen.append(index)
                centers[cost] += 1
                checks['central_representatives'] += 1
            costs.append(row_costs)
            chosen.append(row_chosen)
        for x, z, cost, index in points:
            assert costs[x-xmin][z-zmin] <= cost

        boundary = ([(xmin, z, -1, 0) for z in range(zmin, zmax+1)]
                    + [(xmax, z, 1, 0) for z in range(zmin, zmax+1)]
                    + [(x, zmin, 0, -1) for x in range(xmin, xmax+1)]
                    + [(x, zmax, 0, 1) for x in range(xmin, xmax+1)])
        for x, z, dx, dz in boundary:
            cost = costs[x-xmin][z-zmin]
            strips[cost+1] += 1
            for distance in (1, 3):
                assert check(x+distance*dx, z+distance*dz)[0] == cost+distance
                checks['strip_controls'] += 1
        for x, dx in ((xmin, -1), (xmax, 1)):
            for z, dz in ((zmin, -1), (zmax, 1)):
                cost = costs[x-xmin][z-zmin]
                quadrants[cost+2] += 1
                for distance_x, distance_z in ((1, 1), (2, 3)):
                    assert check(x+distance_x*dx, z+distance_z*dz)[0] == cost+distance_x+distance_z
                    checks['quadrant_controls'] += 1
        records.append(dict(height=height, core=core, points=points,
                            rectangle=[xmin, xmax, zmin, zmax], costs=costs,
                            chosen_indices=chosen))

    degree = max(max(centers)+2, max(strips)+1, max(quadrants))
    central = [centers[i] for i in range(degree+1)]
    strip = [strips[i] for i in range(degree+1)]
    quadrant = [quadrants[i] for i in range(degree+1)]
    numerator = [centers[i]-2*centers[i-1]+centers[i-2]
                 + strips[i]-strips[i-1]+quadrants[i] for i in range(degree+1)]
    counts = [centers[i]+sum(strips[j]+(i-j+1)*quadrants[j] for j in range(i+1))
              for i in range(degree+1)]
    old_counts = original['counts_by_minimum_bridge_length']
    assert counts[:len(old_counts)] == old_counts

    def excess(integer, denominator):
        coefficients = list(numerator)
        coefficients[0] -= 1
        coefficients[1] += 2
        coefficients[2] -= 1
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
    assert low > 2668423113 and high < 2943737759
    result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Two-ended horizontal completion of the same retained atoms; no larger bridge enumeration',
                  source=str(source), source_sha256=hashlib.sha256(raw).hexdigest(),
                  original_atoms=len(words), height_one_points=sorted(height_one),
                  rank_two_orbits=len(records), checks=dict(checks),
                  original_cost_counts=old_counts, extended_initial_counts=counts,
                  central_coefficients=central, strip_coefficients=strip,
                  quadrant_coefficients=quadrant, rational_numerator=numerator,
                  lower_numerator=low, root_upper_numerator=high, denominator=denominator,
                  lower_polynomial_excess=str(excess(low, denominator)),
                  upper_polynomial_excess=str(excess(high, denominator)),
                  orbit_records=records)
    (out/'certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    export = {key: value for key, value in result.items()
              if key not in ('created_utc', 'scope', 'source', 'source_sha256',
                             'lower_polynomial_excess', 'upper_polynomial_excess')}
    (out/'fixtures.g').write_text('G9TwoEnded:='+gap(export)+';\n')
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ('orbit_records', 'height_one_points',
                                     'lower_polynomial_excess', 'upper_polynomial_excess')}, indent=2))
    print('PASS G9 two-ended atom completion')


if __name__ == '__main__':
    main()
