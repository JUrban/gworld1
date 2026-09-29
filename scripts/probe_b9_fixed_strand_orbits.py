#!/usr/bin/env python3
"""Bounded right-translation orbits in B5, looking for a structural lead.

For special a,b, iterating a -> a shelf b strictly increases the LD order.
Indefinite fixed-strand retention would therefore prove infinitude; a
bounded orbit retained here does NOT prove indefinite retention.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess

from b9_burau_lower_bound import burau
from b9_special_braids import inverse, shelf
from probe_b9_strand_drop import embed, mm, supported


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--steps', type=int, default=8)
    ap.add_argument('--word-cap', type=int, default=2000)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    assert not args.output.exists()
    paths = [Path('research/certificates/B9/height4.json'),
             Path('research/certificates/B9-strand-drop/height-counterexamples-v1.json')]
    old, new = [json.loads(p.read_text()) for p in paths]
    seeds = [{'word': r['word'], 'height_bound': r['height'], 'origin': ['height4', i]}
             for i, r in enumerate(old['records'])]
    seeds += [{'word': c['small_word'], 'height_bound': 6,
               'origin': ['height-counterexamples', i]}
              for i, c in enumerate(new['candidates'])]
    matrices = [burau(r['word'], 5) for r in seeds]
    assert len(set(matrices)) == len(seeds)
    shb_s1 = [mm(embed(m, True), burau([1], 6)) for m in matrices]
    trajectories = [{'seed': i, 'right': j, 'words': [r['word']], 'status': 'active'}
                    for i, r in enumerate(seeds) for j in range(len(seeds))]
    active = list(range(len(trajectories)))
    history = []
    binary = Path('large-artifacts/tools/b9_strands_cbraid')
    for step in range(1, args.steps + 1):
        candidates = []
        for k in active:
            tr = trajectories[k]
            a, b = tr['words'][-1], seeds[tr['right']]['word']
            w = shelf(tuple(a), tuple(b))
            if len(w) > args.word_cap:
                tr['status'] = 'word_cap'
                continue
            m = burau(a, 5)
            mi = burau(inverse(a), 5)
            c = mm(mm(embed(m), shb_s1[tr['right']]), embed(mi, True))
            if not supported(c, 5):
                tr['status'] = 'left_B5_by_matrix'
                continue
            candidates.append((k, w))
        if candidates:
            text = ''.join(' '.join(map(str, [k, 6, len(w), *w])) + '\n' for k, w in candidates)
            run = subprocess.run([str(binary)], input=text, text=True, capture_output=True, check=True)
            assert not run.stderr
            checked = [json.loads(line) for line in run.stdout.splitlines()]
            assert len(checked) == len(candidates)
        else:
            checked = []
        next_active = []
        for (k, w), r in zip(candidates, checked):
            assert r['index'] == k
            tr = trajectories[k]
            if r['minimum_strands'] > 5:
                tr['status'] = 'left_B5_exact'
                continue
            assert supported(burau(w, 6), 5)
            assert burau(w, 6) == burau(r['word'], 6)
            tr['words'].append(r['word'])
            next_active.append(k)
        history.append({'step': step, 'started': len(active), 'matrix_candidates': len(candidates),
                        'exact_retained': len(next_active)})
        print(history[-1], flush=True)
        active = next_active
        if not active:
            break
    for k in active:
        trajectories[k]['status'] = 'step_cap'
    longest = max(len(t['words'])-1 for t in trajectories)
    out = {'sources': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'binary_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(),
           'seeds': seeds, 'seed_count': len(seeds), 'trajectory_count': len(trajectories),
           'steps_cap': args.steps, 'word_cap': args.word_cap, 'history': history,
           'terminal_counts': dict(Counter(t['status'] for t in trajectories)),
           'longest_retention': longest,
           'longest_trajectories': [t for t in trajectories if len(t['words'])-1 == longest],
           'limits': 'Only repeated right translation by one of63 fixed seeds; bounded, no infinitude conclusion.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + '\n')
    print('longest retention', longest, 'terminal counts', out['terminal_counts'])
    print('PASS bounded B9 fixed-strand orbit probe')


if __name__ == '__main__':
    main()
