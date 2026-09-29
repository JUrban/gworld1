#!/usr/bin/env python3
"""Search for a lower-strand special braid outside all earlier matrix images.

Matrix membership is only a necessary condition. Every positive hit remains
a candidate requiring an exact braid subgroup check. A non-hit is bounded.
"""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path

from b9_burau_lower_bound import P, T, burau
from b9_special_braids import inverse, shelf


def mm(a, b):
    n = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(n)) % P
                       for j in range(n)) for i in range(n))


def embed(a, shifted=False):
    n = len(a)
    m = [[int(i == j) for j in range(n + 1)] for i in range(n + 1)]
    off = int(shifted)
    for i in range(n):
        for j in range(n):
            m[i + off][j + off] = a[i][j]
    return tuple(map(tuple, m))


def supported(a, n):
    return all(a[i][j] == int(i == j)
               for i in range(len(a)) for j in range(len(a))
               if i >= n or j >= n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True, type=Path)
    ap.add_argument('--output', required=True, type=Path)
    args = ap.parse_args()
    assert not args.output.exists()
    data = json.loads(args.input.read_text())
    records = data['records']
    n = data['ambient_rank']
    a = [burau(r['word'], n) for r in records]
    ai = [burau(inverse(r['word']), n) for r in records]
    ident = burau([], n)
    assert all(mm(x, y) == ident and mm(y, x) == ident for x, y in zip(a, ai))
    known = {embed(x) for x in a}
    assert len(known) == len(records)
    buckets = defaultdict(list)
    for i, (x, xi) in enumerate(zip(a, ai)):
        row = x[-1]
        column = tuple(r[-1] for r in xi)
        if row[0] == 0 and column[0] == 0:
            buckets[(row, column)].append(i)
    expected_pairs = sum(len(v) ** 2 for v in buckets.values())
    print('parent_records', len(records), 'full_pair_count', len(records) ** 2,
          'eligible_buckets', len(buckets), 'eligible_pairs', expected_pairs, flush=True)
    ea = [embed(x) for x in a]
    sa = [embed(x, True) for x in a]
    sai = [embed(x, True) for x in ai]
    s1 = burau([1], n + 1)
    hits = []
    newkeys = set()
    bysupport = defaultdict(int)
    checked = 0
    for bucket in buckets.values():
        for i in bucket:
            for j in bucket:
                m = mm(mm(mm(ea[i], sa[j]), s1), sai[i])
                # The two fingerprint equations are exactly the final
                # row/column equations for this finite representation.
                assert supported(m, n)
                checked += 1
                for k in range(1, n + 1):
                    if supported(m, k):
                        bysupport[k] += 1
                        break
                if m not in known and m not in newkeys:
                    w = shelf(tuple(records[i]['word']), tuple(records[j]['word']))
                    assert burau(w, n + 1) == m
                    newkeys.add(m)
                    hits.append({'parents': [i, j], 'word': w, 'matrix': m,
                                 'term_height': 1 + max(records[i]['height'], records[j]['height']),
                                 'status': 'Necessary matrix condition only; exact subgroup check pending'})
    result = {'input': str(args.input), 'input_sha256': hashlib.sha256(args.input.read_bytes()).hexdigest(),
              'modulus': P, 'parameter': T, 'parent_count': len(records),
              'parent_ambient_rank': n, 'candidate_ambient_rank': n + 1,
              'full_pair_count': len(records) ** 2, 'eligible_pair_count': checked,
              'minimum_matrix_support_pair_counts': dict(bysupport), 'distinct_novel_matrix_hits': len(hits),
              'hits': hits,
              'scope': 'Complete finite-image filter on the saved parent representatives, not an exhaustion of special braids in a fixed B_n.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'hits'}))
    print('PASS B9 strand-drop matrix filter')


if __name__ == '__main__':
    main()
