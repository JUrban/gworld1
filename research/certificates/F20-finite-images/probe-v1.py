#!/usr/bin/env python3
"""Complete pair tests in specified finite permutation groups; no general claim."""
from collections import deque
import hashlib
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/certificates/F20-finite-images'


def mul(a, b):
    """GAP's right-action permutation convention: a first, then b."""
    return tuple(b[i] for i in a)


def inv(a):
    b = [0] * len(a)
    for i, j in enumerate(a):
        b[j] = i
    return tuple(b)


def comm(a, b):
    return mul(mul(inv(a), inv(b)), mul(a, b))


def generated(generators):
    identity = tuple(range(len(generators[0])))
    seen = {identity}
    queue = deque([identity])
    while queue:
        x = queue.popleft()
        for g in generators:
            y = mul(x, g)
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return sorted(seen)


def class_reps(elements, generators):
    unused = set(elements)
    gens = [(g, inv(g)) for g in generators]
    reps = []
    sizes = []
    while unused:
        a = min(unused)
        orbit = {a}
        queue = deque([a])
        while queue:
            x = queue.popleft()
            for g, gi in gens:
                y = mul(mul(gi, x), g)
                if y not in orbit:
                    orbit.add(y)
                    queue.append(y)
        assert orbit <= unused
        unused.difference_update(orbit)
        reps.append(a)
        sizes.append(len(orbit))
    return reps, sizes


def hall_data():
    weights = [1, 1]
    parents = [None, None]
    for w in range(2, 8):
        length = len(weights)
        for i in range(length):
            for j in range(i):
                if weights[i] + weights[j] != w:
                    continue
                if parents[i] is not None and parents[i][1] > j:
                    continue
                weights.append(w)
                parents.append((i, j))
    assert [weights.count(w) for w in range(1, 8)] == [2, 1, 2, 3, 6, 9, 18]
    return weights, parents


def symmetric(n):
    cycle = tuple(list(range(1, n)) + [0])
    switch = tuple([1, 0] + list(range(2, n)))
    return [cycle, switch]


def projective(p):
    # Projective line is F_p followed by infinity. These come from
    # [[1,1],[0,1]] and [[0,-1],[1,0]].
    translate = tuple([(x+1) % p for x in range(p)] + [p])
    inversion = tuple([p] + [(-pow(x, -1, p)) % p for x in range(1, p)] + [0])
    return [translate, inversion]


def evaluate(a, b, parents):
    values = [a, b]
    for i, j in parents[2:]:
        values.append(comm(values[i], values[j]))
    return values


def main():
    OUT.mkdir(exist_ok=True)
    output = OUT/'checks-v1.json'
    fixture = OUT/'fixtures-v1.g'
    assert not output.exists() and not fixture.exists()
    weights, parents = hall_data()
    relators = [i for i, w in enumerate(weights) if w == 6]
    targets = [i for i, w in enumerate(weights) if w == 7]
    cases = [('S6', symmetric(6), 720), ('S7', symmetric(7), 5040)]
    cases += [(f'PSL2_{p}', projective(p), p*(p*p-1)//2) for p in [7, 11, 13, 17, 19]]
    records = []
    for name, gens, expected_order in cases:
        started = time.monotonic()
        elements = generated(gens)
        assert len(elements) == expected_order
        reps, sizes = class_reps(elements, gens)
        identity = tuple(range(len(gens[0])))
        counts = {'pairs': 0, 'commuting': 0, 'passed_two_engel_relators': 0,
                  'passed_all_nine_noncommuting': 0, 'surviving_target_pairs': 0}
        accepted = []
        witness = None
        for ai, a in enumerate(reps):
            for bi, b in enumerate(elements):
                counts['pairs'] += 1
                base = comm(b, a)
                if base == identity:
                    counts['commuting'] += 1
                    continue
                ea, eb = base, base
                for _ in range(4):
                    ea = comm(ea, a)
                    eb = comm(eb, b)
                if ea != identity or eb != identity:
                    continue
                counts['passed_two_engel_relators'] += 1
                values = evaluate(a, b, parents)
                assert values[relators[0]] == ea
                if any(values[i] != identity for i in relators):
                    continue
                counts['passed_all_nine_noncommuting'] += 1
                nontrivial = [i for i in targets if values[i] != identity]
                accepted.append([ai, bi, nontrivial])
                if nontrivial:
                    counts['surviving_target_pairs'] += 1
                    witness = {'a': a, 'b': b, 'target_indices': nontrivial}
        assert counts['pairs'] == len(reps)*len(elements)
        # Omitted-relators control: a weight-seven word really can survive
        # in each ambient group. This makes the complete non-hit meaningful.
        control_values = evaluate(gens[0], gens[1], parents)
        control_nontrivial = [i for i in targets if control_values[i] != identity]
        assert control_nontrivial
        record = {'name': name, 'degree': len(gens[0]), 'order': len(elements),
                  'generators': gens, 'representatives': reps, 'class_sizes': sizes,
                  'elements': elements, 'counts': counts, 'accepted': accepted,
                  'omitted_relators_nontrivial_targets': control_nontrivial,
                  'witness': witness, 'elapsed_seconds': time.monotonic()-started}
        records.append(record)
        print(name, json.dumps(counts), f"seconds={record['elapsed_seconds']:.3f}", flush=True)
    data = {'scope': 'All homomorphism pairs, up to conjugating the first generator, into exactly seven specified permutation groups; rank-two weight6 presentation and all18 weight7 targets only.',
            'convention': 'Right-action permutation multiplication; comm(a,b)=a^-1 b^-1 a b; zero-based arrays and Hall indices in JSON.',
            'weights': weights, 'parents': parents, 'records': records}
    output.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    rows = []
    for r in records:
        rows.append([r['name'],r['degree'],r['order'],
                     [[x+1 for x in g] for g in r['generators']],
                     [[x+1 for x in g] for g in r['representatives']],r['class_sizes'],
                     [[x+1 for x in g] for g in r['elements']],
                     [r['counts'][k] for k in ['pairs','commuting','passed_two_engel_relators','passed_all_nine_noncommuting','surviving_target_pairs']],
                     [[a+1,b+1,[i+1 for i in ts]] for a,b,ts in r['accepted']],
                     [i+1 for i in r['omitted_relators_nontrivial_targets']]])
    fixture.write_text('F20FiniteImages := '+json.dumps(rows,separators=(',',':'))+';\n')
    print('artifact bytes', output.stat().st_size, 'sha256', hashlib.sha256(output.read_bytes()).hexdigest(), flush=True)
    print('PASS F20 bounded nonnilpotent ambient finite-image search', flush=True)


if __name__ == '__main__':
    main()
