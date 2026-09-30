#!/usr/bin/env python3
"""Add disjoint Nielsen-shear tails to the retained two-boundary alphabet."""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from certify_g9_two_ended_completion import act, atom, gap
from g9_flow_unfolding import endpoint, flow


def shear(word, k):
    positive = (2 if k >= 0 else -2,) * abs(k)
    negative = tuple(-x for x in reversed(positive))
    return tuple(x for a in word for x in
                 ((1,)+positive if a == 1 else negative+(-1,) if a == -1 else (a,)))


def flat(edges):
    return tuple((v[0], v[1], j+1, c) for v, j, c in edges)


def coordinates(word):
    edges = flow(2, word)
    height, y = endpoint(2, edges)
    assert height >= 3 and atom(word)
    x1, x2 = (min(v[1] for v, j, c in edges if j == 0 and v[0] == h)
              for h in (1, 2))
    d = x2-x1
    u, v = x1-d, y-x1-(height-1)*d
    return height, u, v, d


def normalized(word):
    height, u, v, d = coordinates(word)
    result = act(shear(word, -d), -u, -v)
    assert coordinates(result) == (height, 0, 0, 0)
    return height, flat(flow(2, result))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    source_paths = [Path('research/certificates/G9-steiner-seeds-v1/certificate.json'),
                    Path('research/certificates/G9-steiner-completion-v1/certificate.json')]
    seeds, old = [json.loads(p.read_text()) for p in source_paths]
    words = [tuple(w) for w in seeds['word_certificates']]
    groups = defaultdict(list)
    seed_data, seed_keys = {}, {}
    excluded = Counter()
    for index, word in enumerate(words):
        assert atom(word)
        height = endpoint(2, flow(2, word))[0]
        if height < 3:
            excluded[height] += 1
            continue
        height, u, v, d = coordinates(word)
        key = normalized(word)
        row = [index, u, v, d, len(word), sum(abs(a) == 1 for a in word)]
        groups[key].append(row)
        seed_data[index], seed_keys[index] = row, key
    keys = sorted(groups)
    positions = {key: i for i, key in enumerate(keys)}
    old_assignments = []
    for index, record in enumerate(old['orbit_records']):
        if record['height'] < 3:
            continue
        first = record['points'][0][3]
        key, d = seed_keys[first], seed_data[first][3]
        for point in record['points']:
            i = point[3]
            assert seed_keys[i] == key and seed_data[i][3] == d
        old_assignments.append([index, positions[key], d])
    assert len({(g, d) for _, g, d in old_assignments}) == len(old_assignments)
    checks = Counter()
    records, terms = [], Counter()
    for group_index, (height, canonical) in enumerate(keys):
        points = sorted(groups[(height, canonical)])
        low_d, high_d = min(p[3] for p in points), max(p[3] for p in points)
        assert sorted({p[3] for p in points}) == sorted(d for _, g, d in old_assignments if g == group_index)
        tails = []
        for sign in (1, -1):
            boundary = high_d+1 if sign == 1 else low_d-1
            choices = [(p[4]+p[5]*abs(boundary-p[3]), p[5], p[0], boundary-p[3]) for p in points]
            cost, vertical, index, start = min(choices)
            assert start*sign > 0
            terms[vertical, cost] += 1
            tails.append(dict(sign=sign, input_index=index, start_shear=start,
                              first_cost=cost, vertical_letters=vertical))
            initial = words[index]
            _, u, v, d0 = coordinates(initial)
            for n in (0, 1, 3):
                k = start+sign*n
                base = shear(initial, k)
                assert len(base) == cost+vertical*n
                assert coordinates(base) == (height, u, v, boundary+sign*n)
                for left, right in ((0, 0), (-2, 1), (1, -2)):
                    word = act(base, left, right)
                    assert len(word) == cost+vertical*n+abs(left)+abs(right)
                    assert coordinates(word) == (height, u+left, v+right, boundary+sign*n)
                    assert normalized(word) == (height, canonical)
                    assert flow(2, word) == flow(2, shear(act(initial, left, right), k))
                    checks['tail_boundary_controls'] += 1
        representative = words[points[0][0]]
        assert flow(2, shear(shear(representative, 2), -3)) == flow(2, shear(representative, -1))
        assert flow(2, shear(shear(representative, 1), -1)) == flow(2, representative)
        checks['shear_compositions'] += 2
        records.append(dict(height=height, canonical_flow=canonical, points=points,
                            occupied_d=sorted({p[3] for p in points}),
                            d_interval=[low_d, high_d], tails=tails))
    term_rows = [[vertical, degree, number] for (vertical, degree), number in sorted(terms.items())]

    def evaluate(t):
        previous = sum(c*t**i for i, c in enumerate(old['rational_numerator']))/(1-t)**2
        additional = sum(number*t**degree/(1-t**vertical) for vertical, degree, number in term_rows)
        return previous+((1+t)/(1-t))**2*additional

    scale = 10**9
    low, high = old['lower_numerator'], 3*scale
    assert evaluate(Fraction(scale, low)) > 1 and evaluate(Fraction(scale, high)) < 1
    while high-low > 1:
        mid = (low+high)//2
        if evaluate(Fraction(scale, mid)) >= 1:
            low = mid
        else:
            high = mid
    lower_value, upper_value = evaluate(Fraction(scale, low)), evaluate(Fraction(scale, high))
    assert low >= old['lower_numerator'] and high < 2943737759
    additions = []
    for degree in range(41):
        total = 0
        for vertical, initial, number in term_rows:
            for n in range(max(0, (degree-initial)//vertical+1)):
                horizontal = degree-initial-n*vertical
                total += number*(1 if horizontal == 0 else 4*horizontal)
        additions.append(total)
    assert additions[:15] == [0]*15
    result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Disjoint infinite shear tails added to the retained two-boundary atom alphabet',
                  sources=[dict(path=str(p), bytes=p.stat().st_size, sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in source_paths],
                  original_seed_count=len(words), excluded_height_counts=sorted(excluded.items()),
                  covered_seeds=len(seed_data), covered_old_orbits=len(old_assignments),
                  shear_orbits=len(records), old_orbit_assignments=old_assignments,
                  old_rational_numerator=old['rational_numerator'],
                  additional_terms=term_rows, additional_counts_through_40=additions,
                  lower_numerator=low, root_upper_numerator=high, denominator=scale,
                  lower_value=str(lower_value), upper_value=str(upper_value),
                  checks=dict(checks), orbit_records=records)
    (args.output/'certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    export = {k:v for k,v in result.items() if k not in ('created_utc','scope','sources','lower_value','upper_value')}
    (args.output/'fixtures.g').write_text('G9ShearTails:='+gap(export)+';\n')
    summary = {k:v for k,v in result.items() if k not in ('orbit_records','old_orbit_assignments','lower_value','upper_value','sources')}
    (args.output/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    print('PASS G9 disjoint shear-tail certificate')


if __name__ == '__main__':
    main()
