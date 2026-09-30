#!/usr/bin/env python3
"""Universal m(v)=3 exclusion via finite permutations and one exact obstruction."""
import argparse
from itertools import permutations
import json
from pathlib import Path

from b9_special_braids import artin, inverse, reduce_word, shelf, shift


def compose(p, q):
    return tuple(p[j - 1] for j in q)


def invperm(p):
    return tuple(p.index(j) + 1 for j in range(1, len(p) + 1))


def shperm(p):
    return (1,) + tuple(j + 1 for j in p)


def extend(p):
    return p + (len(p) + 1,)


def i1perm(p):
    trans = (2, 1) + tuple(range(3, len(p) + 2))
    return compose(compose(extend(p), trans), invperm(shperm(p)))


def wordperm(w, n):
    p = list(range(1, n + 1))
    for letter in w:
        i = abs(letter) - 1
        p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def nu(p):
    return sum(p[j] == j for j in range(1, len(p)))


def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def burau(w, n):
    out = [[int(i == j) for j in range(n)] for i in range(n)]
    for letter in w:
        g = [[int(i == j) for j in range(n)] for i in range(n)]
        i = abs(letter) - 1
        block = [[2, -1], [1, 0]] if letter > 0 else [[0, 1], [-1, 2]]
        for r in range(2):
            for c in range(2):
                g[i+r][i+c] = block[r][c]
        out = matmul(out, g)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    # Complete small-strand sectors, not a term-height sample.
    vwords = [(1, 1, -2), (2, 1)]
    uwords = [shelf(v, ()) for v in vwords] + [(3, 2, 1)]
    possible = sorted(p for p in permutations(range(1, 5)) if nu(p) == 2)
    assert possible == [(1, 4, 2, 3), (2, 1, 4, 3), (3, 1, 2, 4)]
    unknown_rows = []
    for u in possible:
        for v in vwords:
            vp = wordperm(v, 3)
            ap = compose(i1perm(u), shperm(i1perm(vp)))
            assert ap[3:] != (4, 5)
            unknown_rows.append({'u_permutation':u, 'v_word':v,
                                 'A_permutation':ap, 'images_4_5':ap[3:]})
    known_rows = []
    survivors = []
    for u in uwords:
        for v in vwords:
            c = shelf(v, ())
            a = reduce_word(shelf(u, ()) + shift(c))
            ap = wordperm(a, 5)
            assert ap == compose(i1perm(wordperm(u, 4)), shperm(i1perm(wordperm(v, 3))))
            row = {'u_word':u, 'v_word':v, 'A_word':a, 'A_permutation':ap,
                   'images_4_5':ap[3:]}
            if ap[3:] == (4, 5):
                survivors.append((u, v))
                u_image, c_image = artin(u, 5), artin(c, 5)
                assert u_image[3] != c_image[3]
                uc = [r[3] for r in burau(u, 4)]
                cc = [r[3] for r in burau(c, 4)]
                assert uc == [0, 0, -1, 0] and cc == [-2, -4, -1, 2]
                row.update(u_x4=u_image[3], c_x4=c_image[3],
                           u_burau_column4=uc, c_burau_column4=cc)
            known_rows.append(row)
    assert survivors == [((3, 2, 1), (2, 1))]
    # Right multiplication by B3 fixes the fourth column. Positive control.
    u = (3, 2, 1)
    assert [r[3] for r in burau(u+(1, -2, 1), 4)] == [r[3] for r in burau(u, 4)]
    # Permutation-only exclusion really is insufficient in the retained case.
    only = next(r for r in known_rows if r['images_4_5'] == (4, 5))
    assert artin(tuple(only['A_word']), 5)[4] != (5,)
    data = {'scope':'Exclude all special u,v with m(v)=3 and I1(u) S(I1(v)) in B3, using prior structural theorems. Higher underlying strands unclassified.',
            'conventions':'Permutation functions compose rightmost first; Burau generator block [[2,-1],[1,0]].',
            'all_S4_permutations':24, 'nu2_permutations':possible,
            'unknown_exponent_two_rows':unknown_rows, 'known_sector_rows':known_rows,
            'permutation_survivors':survivors, 'result':'all excluded'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print('All24 S4 permutations filtered:3 nu=2; all6 unknown-sector pairs excluded')
    print('Known sectors:6 pairs; sole permutation survivor tau3,tau2 fails both exact obstructions')
    print('Burau columns:',only['u_burau_column4'],only['c_burau_column4'])
    print('PASS B9 three-strand underlying exclusion')


if __name__ == '__main__':
    main()
