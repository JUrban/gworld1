#!/usr/bin/env python3
"""Bounded exact checks of signed piece-cover counting, not model theory.

Enumerate every reduced rank-two word at lengths 1..7. Enumerate covers
by 1..3 consecutive variable blocks, with zero or one fixed initial
letter, and all possible second positions/orientations for each block.
Intersect independently constructed word masks; compare their exact
counts with the signed-component/spanning-tree upper bound.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


def reduced_words(n):
    words = [()]
    for _ in range(n):
        words = [w+(a,) for w in words for a in (1, -1, 2, -2)
                 if not w or w[-1] != -a]
    return words


def compositions(n, k):
    if k == 1:
        if n > 0:
            yield (n,)
        return
    for i in range(1, n-k+2):
        for tail in compositions(n-i, k-1):
            yield (i,)+tail


def components(n, pairs, constants):
    adj = [[] for _ in range(n)]
    for a, length, b, sign in pairs:
        assert sign in (-1, 1)
        assert a != b or sign == -1
        for j in range(length):
            u, v = a+j, b+(j if sign == 1 else length-1-j)
            adj[u].append((v, sign))
            adj[v].append((u, sign))
    labels, signs, parts = {}, {}, []
    for root in range(n):
        if root in labels:
            continue
        labels[root], signs[root] = len(parts), 1
        part, queue = [], [root]
        for u in queue:
            part.append(u)
            for v, sign in adj[u]:
                if v in labels:
                    if signs[v] != signs[u]*sign:
                        return None
                else:
                    labels[v], signs[v] = len(parts), signs[u]*sign
                    queue.append(v)
        parts.append(part)
    # A singleton may only be a fixed coefficient position.
    assert all(len(p) >= 2 or p[0] in constants for p in parts)
    assert 2*len(parts) <= n+len(constants)
    quotient = [set() for _ in parts]
    for i in range(n-1):
        u, v = labels[i], labels[i+1]
        if u != v:
            quotient[u].add(v)
            quotient[v].add(u)
    seen, queue = {0}, [0]
    for u in queue:
        for v in quotient[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    assert len(seen) == len(parts), 'Quotient of a path must be connected'
    return len(parts)


def main():
    out = Path('research/certificates/F41-piece-covers')
    out.mkdir(parents=True, exist_ok=True)
    assert not (out/'checks.json').exists(), 'Never overwrite evidence'
    summaries, fixtures, fixture_keys = [], [], set()
    total = 0
    for n in range(1, 8):
        words = reduced_words(n)
        assert len(words) == 4*3**(n-1)

        @lru_cache(None)
        def mask(a, length, b, sign):
            answer = 0
            for i, w in enumerate(words):
                first, second = w[a:a+length], w[b:b+length]
                if sign == -1:
                    second = tuple(-x for x in reversed(second))
                if first == second:
                    answer |= 1 << i
            return answer

        for coefficient_count in (0, 1):
            if n <= coefficient_count:
                continue
            constants = {0} if coefficient_count else set()
            initial_mask = sum(1 << i for i, w in enumerate(words)
                               if not coefficient_count or w[0] == 1)
            stats = defaultdict(int)
            for k in range(1, min(3, n-coefficient_count)+1):
                for lengths in compositions(n-coefficient_count, k):
                    starts, next_start = [], coefficient_count
                    for length in lengths:
                        starts.append(next_start)
                        next_start += length
                    options = [
                        [(a, length, b, sign)
                         for b in range(n-length+1) for sign in (1, -1)
                         if a != b or sign == -1]
                        for a, length in zip(starts, lengths)]
                    for pairs in product(*options):
                        actual_mask = initial_mask
                        for pair in pairs:
                            actual_mask &= mask(*pair)
                        count = actual_mask.bit_count()
                        c = components(n, pairs, constants)
                        stats['schemes'] += 1
                        if c is None:
                            assert count == 0
                            stats['inconsistent_signed_schemes'] += 1
                        else:
                            assert count <= 4*3**(c-1)
                            stats['consistent_signed_schemes'] += 1
                            stats['maximum_components'] = max(stats['maximum_components'], c)
                        stats['nonempty_schemes'] += bool(count)
                        stats['maximum_word_count'] = max(stats['maximum_word_count'], count)
                        overlap = any(a != b and max(a, b) < min(a+length, b+length)
                                      for a, length, b, sign in pairs)
                        inverse = any(sign == -1 for a, length, b, sign in pairs)
                        key = (n, coefficient_count, overlap, inverse, c is None, bool(count))
                        if key not in fixture_keys:
                            fixture_keys.add(key)
                            fixtures.append([n, [[i+1, 1] for i in sorted(constants)],
                                             [[a+1, length, b+1, sign] for a, length, b, sign in pairs],
                                             count, c or 0])
            total += stats['schemes']
            summaries.append(dict(n=n, coefficient_count=coefficient_count,
                                  reduced_words=len(words), **stats))
    # A single repeated short piece is insufficient: words ending aa
    # at length 9 have 3^7 members, exceeding the all-covered bound.
    negative_count = sum(w[-2:] == (1, 1) for w in reduced_words(9))
    assert negative_count == 3**7 > 4*3**4
    record = dict(scope='Rank 2; lengths 1..7; all 1..3-block covers, with 0/1 initial coefficient',
                  total_schemes=total, summaries=summaries,
                  independent_gap_fixtures=len(fixtures),
                  uncovered_negative_control=dict(length=9, suffix=[1, 1], count=negative_count,
                                                   reason='Uncovered positions invalidate the half-length bound'))
    (out/'checks.json').write_text(json.dumps(record, indent=2)+'\n')
    (out/'fixtures.g').write_text('F41PieceFixtures := '+json.dumps(fixtures)+';\n')
    print(f'PASS F41 piece covers: {total} positional schemes; {len(fixtures)} GAP fixtures; uncovered control rejected')


if __name__ == '__main__':
    main()
