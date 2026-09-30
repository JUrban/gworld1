#!/usr/bin/env python3
"""Necessary permutation bounds only; no special-braid existence claims."""
import argparse
from itertools import permutations
import json
from pathlib import Path

from check_b9_three_strand_underlying import compose, extend, invperm, shperm, nu
from probe_b9_four_strand_permutations import ip


def bounds(n, prev):
    out = {0: {tuple(range(1, n+1))}, 1: {ip(p, 1) for p in prev}}
    smaller = list(permutations(range(1, n)))
    for k in range(2, n):
        out[k] = {ip(p, k) for p in smaller}
    for k, rows in out.items():
        assert all(nu(p) == k for p in rows)
        out[k] = {p for p in rows if p.index(1) < 2}
    return out


def reconstruct(b, n):
    for first in range(1, n+1):
        if b[first] != first:
            continue
        f = [first, b[0]]
        for i in range(3, n+1):
            f.append(b[f[-1]])
        if sorted(f) != list(range(1, n+1)):
            continue
        f = tuple(f)
        if ip(f, 1) == b:
            yield f


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-q', type=int, default=7)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    prev = {(1,)}
    by_n = {1: {0: prev}}
    for n in range(2, args.max_q+2):
        by_n[n] = bounds(n, prev)
        prev = set().union(*by_n[n].values())
    inventories = []
    for q in range(3, args.max_q+1):
        allowed_f = set().union(*by_n[q+1].values())
        rows = []
        for p, gs in by_n[q].items():
            for g in sorted(gs):
                c = ip(g, 1)
                for small_a in [(1,2,3), (2,3,1), (3,1,2)]:
                    a = small_a + tuple(range(4, q+3))
                    b = compose(a, invperm(shperm(c)))
                    for f in reconstruct(b, q+1):
                        if f not in allowed_f:
                            continue
                        actual = compose(ip(f, 1), shperm(c))
                        assert actual == a
                        rows.append({'g': g, 'f': f, 'a': small_a,
                                     'nu_g': p, 'nu_f': nu(f)})
        exceptions = [r for r in rows if r['a'] != (1,2,3)
                      or r['nu_f'] != r['nu_g']+1]
        # Embedded valid small-strand pairs must not disappear.
        assert any(r['g'] == tuple(range(1,q+1)) for r in rows)
        high = [r for r in rows if r['g'][-1] != q or r['f'][-1] != q+1]
        high_exceptions = [r for r in high if r in exceptions]
        inventory = {'q': q, 'g_bound': sum(map(len,by_n[q].values())),
                     'f_bound': len(allowed_f), 'survivors': rows,
                     'exceptions': exceptions, 'visible_high_support_exceptions': high_exceptions}
        inventories.append(inventory)
        print('q', q, 'g/f bounds', inventory['g_bound'], len(allowed_f),
              'survivors', len(rows), 'exceptions', len(exceptions),
              'visible high exceptions', len(high_exceptions), flush=True)
        if high_exceptions:
            print('first high exception', high_exceptions[0], flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump({'scope': 'Necessary permutation bounds only; fixed positions do not determine minimum braid support.',
                   'inventories': inventories}, stream, indent=2)
        stream.write('\n')
    print('PASS B9 general necessary permutation inventory')


if __name__ == '__main__':
    main()
