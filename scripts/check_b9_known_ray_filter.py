#!/usr/bin/env python3
"""Check the new complete ray-index filter on existing B9 fixtures only."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from b9_known_ray_filter import BASE_PAIRS, BASE_PARAMETERS, candidate_indices, exponent, matching_rays, ray_pair
from b9_special_braids import artin, reduce_word, shift


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
    root = Path(__file__).resolve().parents[1]
    height_path = root/'research/certificates/B9/height4.json'
    endpoint_path = root/'research/certificates/B9-positive-parameters/endpoints-v1.json'
    height = json.loads(height_path.read_text())['records']
    endpoints = json.loads(endpoint_path.read_text())['records']
    records = []
    for kind, words in [('height4', [r['word'] for r in height]),
                        ('endpoint', [r['colors'][0] for r in endpoints])]:
        for index, word in enumerate(words):
            matches = matching_rays(word)
            if kind == 'endpoint':
                assert matches, 'Known endpoint must match a known ray'
            records.append(dict(kind=kind, source_index=index, word=word,
                                exponent=exponent(word),
                                candidates=candidate_indices(exponent(word)), matches=matches))
    # These are the eight small-first-color pairs, with known parameter cosets.
    small = [(), (1,), (1, 1, -2), (2, 1)]
    expected = [(0, 0), (1, 0), (0, 1), (2, 0),
                (3, 0), (0, 2), (1, 1), (2, 1)]
    small_cases = []
    for (a, c), (ray, step) in zip(((a, c) for a in small for c in [(), (1,)]), expected):
        parameter = a+shift(c)
        representative = BASE_PARAMETERS[ray]+(1,)*step
        assert artin(parameter, 5) == artin(representative, 5)
        small_cases.append(dict(a=a, c=c, parameter=parameter, ray=ray, step=step))
    # Boundary permutations showing f3,f4 are outside B3, with no matrix faithfulness claim.
    boundaries = []
    for step, rank in [(3, 4), (4, 5)]:
        a, c = ray_pair(0, step)
        permutation = list(range(1, rank+1))
        for letter in a:
            i = abs(letter)-1
            permutation[i], permutation[i+1] = permutation[i+1], permutation[i]
        assert permutation[-1] != rank
        boundaries.append(dict(step=step, word=a, permutation=permutation))
    # Index identity checked over the retained endpoint range, including absent exponents.
    index_checks = []
    for e in range(-2, 9):
        actual = candidate_indices(e)
        brute = [(ray, step) for ray in range(4) for step in range(19)
                 if exponent(ray_pair(ray, step)[0]) == e]
        assert actual == brute and len(actual) <= 8
        index_checks.append(dict(exponent=e, candidates=actual))
    max_step = max(step for r in records for ray, step in r['candidates'])
    rays = []
    for ray in range(4):
        for step in range(max_step+1):
            a, c = ray_pair(ray, step)
            assert reduce_word(a+shift(c)) == reduce_word(BASE_PARAMETERS[ray]+(1,)*step)
            p0, q0 = map(exponent, BASE_PAIRS[ray])
            expected_exponent = p0+step//2 if step % 2 == 0 else q0+1+step//2
            assert exponent(a) == expected_exponent
            rays.append(dict(ray=ray, step=step, a=a, c=c, exponent=expected_exponent))
    result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Exact known-ray membership; original 52 and 46 fixtures only; no B4 exhaustion',
                  inputs=[dict(path=str(path.relative_to(root)), sha256=hashlib.sha256(path.read_bytes()).hexdigest())
                          for path in [height_path, endpoint_path]],
                  records=records, small_cases=small_cases, boundaries=boundaries,
                  index_checks=index_checks, rays=rays,
                  height4_matches=sum(bool(r['matches']) for r in records if r['kind'] == 'height4'),
                  endpoint_matches=sum(bool(r['matches']) for r in records if r['kind'] == 'endpoint'),
                  max_step=max_step)
    (out/'checks.json').write_text(json.dumps(result, indent=2)+'\n')
    exported={key:result[key] for key in ['records','small_cases','boundaries','index_checks','rays','max_step']}
    (out/'fixtures.g').write_text('B9RayChecks:='+gap(exported)+';\n')
    print(json.dumps({key:result[key] for key in ['scope','height4_matches','endpoint_matches','max_step']}, indent=2))
    print('PASS B9 fixed first color ray filter')


if __name__ == '__main__':
    main()
