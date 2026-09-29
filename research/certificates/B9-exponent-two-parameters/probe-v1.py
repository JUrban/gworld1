#!/usr/bin/env python3
"""Test the adjacent-strand necessary condition in the epsilon(A)=2 sector."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import subprocess

from b9_special_braids import artin, inverse, reduce_word, shelf, shift, strand_number


def main():
    root = Path(__file__).resolve().parents[1]
    source = root / 'research/certificates/B9/height4.json'
    binary = root / 'large-artifacts/tools/b9_strands_cbraid'
    outdir = root / 'research/certificates/B9-exponent-two-parameters'
    outdir.mkdir(exist_ok=True)
    output = outdir / 'probe-v1.json'
    fixtures = outdir / 'fixtures-v1.g'
    assert not output.exists() and not fixtures.exists()
    old = json.loads(source.read_text())['records']
    assert len(old) == 52
    candidates = []
    for i, u in enumerate(old):
        for j, v in enumerate(old):
            r, s = u['strands'], v['strands']
            if not ((s == 1 and r <= 2) or (s >= 2 and r == s + 1)):
                continue
            a, c = shelf(tuple(u['word']), ()), shelf(tuple(v['word']), ())
            word = reduce_word(a + shift(c))
            candidates.append({'u_index': i, 'v_index': j, 'u_strands': r,
                               'v_strands': s, 'word': list(word)})
    rank = 7
    input_text = ''.join(' '.join(map(str, [i, rank, len(r['word']), *r['word']])) + '\n'
                         for i, r in enumerate(candidates))
    run = subprocess.run([str(binary)], input=input_text, text=True,
                         capture_output=True, check=True)
    assert not run.stderr, run.stderr
    answers = [json.loads(line) for line in run.stdout.splitlines()]
    assert len(answers) == len(candidates)
    bases = [(), (2,), (1, 2), (1, 1, -2)]
    base_images = [artin(reduce_word(w + (2, 1) + inverse(shift(w))), rank) for w in bases]
    hits = []
    for i, (record, answer) in enumerate(zip(candidates, answers)):
        assert answer['index'] == i and answer['ambient_rank'] == rank
        action = artin(tuple(record['word']), rank)
        assert artin(tuple(answer['word']), rank) == action
        actual = strand_number(action)
        assert actual == answer['minimum_strands'], (i, actual, answer)
        record.update(minimum_strands=actual, reduced_parameter=answer['word'])
        if actual <= 3:
            w = tuple(record['word'])
            image = artin(reduce_word(w + (2, 1) + inverse(shift(w))), rank)
            known = [k for k, v in enumerate(base_images) if image == v]
            record['known_cosets'] = known
            hits.append(i)
    # Boundary counterexample: permutation alone does not test support.
    u = (2, 1)
    v = (1,)
    boundary = reduce_word(shelf(u, ()) + shift(shelf(v, ())))
    explicit = (2, 1, 1, -2, -3, 2, 2, -3)
    assert artin(boundary, rank) == artin(explicit, rank)
    assert strand_number(artin(boundary, rank)) == 4
    pos = list(range(1, 5))
    crossings = Counter()
    for letter in explicit:
        k = abs(letter) - 1
        pair = tuple(sorted(pos[k:k + 2]))
        crossings[pair] += 1 if letter > 0 else -1
        pos[k], pos[k + 1] = pos[k + 1], pos[k]
    assert pos == [1, 2, 3, 4]
    assert crossings[2, 4] == 2 and crossings[3, 4] == -2
    output.write_text(json.dumps({
        'scope': 'Only underlying special terms of height<=4; adjacent-strand filter; no all-strand exhaustion',
        'source': str(source.relative_to(root)), 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'binary_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(),
        'ambient_rank': rank, 'candidate_count': len(candidates), 'hit_indices': hits,
        'counts_by_minimum_strands': dict(Counter(r['minimum_strands'] for r in candidates)),
        'boundary_word': list(explicit), 'boundary_crossing_totals': [[*p, n] for p, n in sorted(crossings.items())],
        'records': candidates,
    }, indent=2) + '\n')
    fixtures.write_text('B9ExponentTwoRecords := ' + json.dumps([
        [r['u_index'] + 1, r['v_index'] + 1, r['word'], r['minimum_strands'], r['reduced_parameter']]
        for r in candidates]) + ';\n')
    print('Candidates', len(candidates), 'minimum strands', dict(Counter(r['minimum_strands'] for r in candidates)))
    print('Hits', [(candidates[i]['u_index'], candidates[i]['v_index'], candidates[i]['known_cosets']) for i in hits])
    print('Boundary pure braid has linking(2,4)=1 and linking(3,4)=-1')
    print('PASS B9 exponent-two parameter probe with independent Artin actions')


if __name__ == '__main__':
    main()
