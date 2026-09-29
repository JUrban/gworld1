#!/usr/bin/env python3
"""Run the pinned CBraid checker on known controls and matrix candidates."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import subprocess

from b9_special_braids import artin, strand_number


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    assert not args.output.exists()
    old = json.loads(Path('research/certificates/B9/height4.json').read_text())
    controls = [{'word': r['word'], 'ambient_rank': 7, 'expected': r['strands']}
                for r in old['records']]
    # A pure braid may have trivial permutation yet use the last strand.
    for n in range(2, 8):
        controls.extend([{'word': [n-1, n-1], 'ambient_rank': n, 'expected': n},
                         {'word': [n-1, -(n-1)], 'ambient_rank': n, 'expected': 1}])
    rng = random.Random(2026092919)
    for n in range(3, 8):
        for _ in range(20):
            w = [rng.choice([-1, 1]) * rng.randrange(1, n) for _ in range(10)]
            controls.append({'word': w, 'ambient_rank': n,
                             'expected': strand_number(artin(w, n))})
    source = json.loads(args.input.read_text())
    records = controls + [{'word': h['word'], 'ambient_rank': source['candidate_ambient_rank']}
                          for h in source['hits']]
    text = ''.join(' '.join(map(str, [i, r['ambient_rank'], len(r['word']), *r['word']])) + '\n'
                   for i, r in enumerate(records))
    binary = Path('large-artifacts/tools/b9_strands_cbraid')
    run = subprocess.run([str(binary)], input=text, text=True, capture_output=True, check=True)
    assert not run.stderr, run.stderr
    results = [json.loads(line) for line in run.stdout.splitlines()]
    assert len(results) == len(records)
    for i, (r, result) in enumerate(zip(records, results)):
        assert result['index'] == i
        assert result['ambient_rank'] == r['ambient_rank']
        if i < len(controls):
            assert result['minimum_strands'] == r['expected'], (i, r, result)
            assert artin(result['word'], r['ambient_rank']) == artin(r['word'], r['ambient_rank'])
    hitresults = results[len(controls):]
    counts = Counter(r['minimum_strands'] for r in hitresults)
    out = {'input': str(args.input), 'input_sha256': hashlib.sha256(args.input.read_bytes()).hexdigest(),
           'binary_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(),
           'controls': controls, 'control_count': len(controls), 'seed': 2026092919,
           'candidate_count': len(hitresults), 'counts_by_exact_strands': dict(counts),
           'results': hitresults,
           'limits': 'CBraid canonical-form decision; positive novel braid identities still need independent verification.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + '\n')
    print('controls', len(controls), 'candidate_counts_by_exact_strands', dict(counts))
    print('PASS B9 exact strand checks')


if __name__ == '__main__':
    main()
