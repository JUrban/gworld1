#!/usr/bin/env python3
"""Bounded enumeration of the monogenic braid shelf, using the Artin action.

This enumerates term HEIGHT, not all special braids of a fixed strand number.
Words are signed Artin-generator indices; free-group letters are signed indices.
The braid product acts by composition rho(uv)=rho(u) o rho(v).
"""
import argparse
import hashlib
import json
from pathlib import Path


def reduce_word(word):
    out = []
    for x in word:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def inverse(word):
    return tuple(-x for x in reversed(word))


def shift(word):
    return tuple(x + 1 if x > 0 else x - 1 for x in word)


def shelf(a, b):
    return reduce_word(a + shift(b) + (1,) + inverse(shift(a)))


def artin(word, rank):
    images = [(i,) for i in range(1, rank + 1)]
    for letter in word:
        i = abs(letter) - 1
        x, y = images[i:i + 2]
        if letter > 0:
            images[i:i + 2] = [reduce_word(x + y + inverse(x)), x]
        else:
            images[i:i + 2] = [y, reduce_word(inverse(y) + x + y)]
    return tuple(images)


def strand_number(images):
    """Minimum standard B_n containing the braid, via its faithful Artin action.

Test both identity on the complementary basis and preservation of F_n.
Artin's characterization then identifies the restriction with an n-braid.
"""
    for n in range(1, len(images) + 1):
        if (all(images[i] == (i + 1,) for i in range(n, len(images)))
                and all(abs(x) <= n for w in images[:n] for x in w)):
            return n
    raise AssertionError('Full ambient rank must work')


def checks():
    for rank in range(2, 8):
        ident = artin((), rank)
        for i in range(1, rank):
            assert artin((i, -i), rank) == ident
            assert artin((-i, i), rank) == ident
            assert strand_number(artin((i,), rank)) == i + 1
        for i in range(1, rank - 1):
            assert artin((i, i + 1, i), rank) == artin((i + 1, i, i + 1), rank)
        for i in range(1, rank):
            for j in range(i + 2, rank):
                assert artin((i, j), rank) == artin((j, i), rank)
    assert shelf((1,), ()) == (1, 1, -2)
    assert shelf((), (1,)) == (2, 1)
    assert artin(shelf((1,), (1,)), 4) == artin((2, 1), 4)
    # A nontrivial pure braid is not detected by its permutation alone.
    assert strand_number(artin((1, 1), 4)) == 2
    assert strand_number(artin((2, 2), 4)) == 3


def enumerate_heights(height):
    rank = height + 1
    records = [dict(word=[], height=0, parents=None, strands=1)]
    known = {artin((), rank): 0}
    levels = []
    for h in range(1, height + 1):
        size = len(records)
        attempts = 0
        for i in range(size):
            for j in range(size):
                if max(records[i]['height'], records[j]['height']) != h - 1:
                    continue
                attempts += 1
                word = shelf(tuple(records[i]['word']), tuple(records[j]['word']))
                key = artin(word, rank)
                if key not in known:
                    known[key] = len(records)
                    records.append(dict(word=list(word), height=h, parents=[i, j],
                                        strands=strand_number(key)))
        by_strands = {str(n): sum(r['strands'] <= n for r in records)
                      for n in range(1, rank + 1)}
        level = dict(height=h, attempted_new_pairs=attempts, cumulative=len(records),
                     counts_in_Bn=by_strands,
                     max_artin_total_length=max(sum(map(len, k)) for k in known))
        levels.append(level)
        print(json.dumps(level), flush=True)
    return dict(bound='term height <= '+str(height), ambient_rank=rank,
                convention='a shelf b = a shift(b) sigma_1 shift(a)^-1',
                completeness='Only bounded term height; no fixed-strand exhaustion claim',
                levels=levels, records=records)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--height', type=int, default=4)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if args.height < 1:
        parser.error('height must be positive')
    path = Path(args.output)
    if path.exists():
        raise SystemExit('Refusing to overwrite an existing certificate')
    checks()
    result = enumerate_heights(args.height)
    data = (json.dumps(result, indent=2) + '\n').encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    print('certificate_sha256', hashlib.sha256(data).hexdigest())
    print('PASS bounded special-braid enumeration')


if __name__ == '__main__':
    main()
