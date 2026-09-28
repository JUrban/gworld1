#!/usr/bin/env python3
"""Bounded and invariant checks supporting, but not implementing, F38(a)."""
import argparse
from collections import deque
from datetime import datetime, timezone
import hashlib
from itertools import product
import json
from pathlib import Path
import random
from f38_polynomial_identity import (
    solve, apply_matrix, evaluate_polynomial, word_reduce, inverse,
    cyclic_reduce, substitute, cancellation_triangle, regular_summary,
    summary_product, summary_inverse, summary_is_cyclic,
)

ROOT = Path(__file__).resolve().parents[1]


def terms(n, entries):
    result = []
    for coefficient, indices in entries:
        powers = [0] * n
        for i in indices:
            powers[i] += 1
        result.append([coefficient, powers])
    return result


def case(name, seed, matrices, polynomial, expected, edges=None,
         initials=None, finals=None, terminal_indices=None):
    result = dict(name=name, seed=seed, matrices=matrices, polynomial=polynomial,
                  expected=expected, initials=initials or [0],
                  finals=finals if finals is not None else [0],
                  edges=edges if edges is not None else
                        [[0, 0, i] for i in range(len(matrices))])
    if terminal_indices is not None:
        result['terminal_indices'] = terminal_indices
    return result


def polynomial_cases():
    parabola = [[1, 2, 1], [0, 1, 1], [0, 0, 1]]
    p = terms(3, [(1, [0, 2]), (-1, [1, 1])])
    cases = [case('parabola_identity', [0, 0, 1], [parabola], p, True),
             case('parabola_nonidentity', [0, 0, 1], [parabola],
                  p + terms(3, [(1, [2, 2])]), False)]
    # Product of (y-i*z), i=0,...,5; six initial samples vanish.
    poly = {(0, 0, 0): 1}
    for i in range(6):
        nxt = {}
        for exponent, coefficient in poly.items():
            for coordinate, scalar in [(1, 1), (2, -i)]:
                e = list(exponent)
                e[coordinate] += 1
                e = tuple(e)
                nxt[e] = nxt.get(e, 0) + coefficient * scalar
        poly = nxt
    cases.append(case('six_zero_samples_then_failure', [0, 0, 1], [parabola],
                      [[c, list(e)] for e, c in poly.items() if c], False))
    swap = [[0, 1], [1, 0]]
    alternating = [[0, 1, 0], [1, 0, 0]]
    px1 = terms(2, [(1, [0]), (-1, [])])
    cases += [case('control_even', [1, 0], [swap], px1, True, edges=alternating),
              case('control_odd', [1, 0], [swap], px1, False,
                   edges=alternating, finals=[1])]
    a, b = [[1, 1], [0, 1]], [[1, 0], [1, 1]]
    difference = terms(2, [(1, [0]), (-1, [1])])
    path = [[0, 1, 0], [1, 2, 1]]
    cases += [case('application_order', [1, 0], [a, b], difference, True,
                   edges=path, finals=[2]),
              case('reversed_application_order', [1, 0], [b, a], difference,
                   False, edges=path, finals=[2])]
    terminalize, double = [[1, 1], [0, 0]], [[1, 0], [0, 2]]
    nonterminal_count = terms(2, [(1, [1])])
    cases += [case('terminal_filter', [0, 1], [terminalize, double],
                   nonterminal_count, True, terminal_indices=[0]),
              case('missing_terminal_filter_control', [0, 1], [terminalize, double],
                   nonterminal_count, False),
              case('empty_terminal_language', [0, 1], [double],
                   terms(2, [(1, [])]), True, terminal_indices=[0]),
              case('erasing_morphism_empty_output', [0, 1],
                   [double, [[0, 0], [0, 0]]], terms(2, [(1, [])]), False,
                   terminal_indices=[0]),
              case('empty_control_language', [1, 0], [a], terms(2, [(1, [])]),
                   True, edges=[], finals=[1]),
              case('zero_polynomial', [1, 1], [a, b], [], True)]
    # Degree-three determinant times length difference, coordinates
    # (B11,B12,B21,B22,lenU,lenV). These are controlled-matrix fixtures,
    # not grammars produced by a free-group equation solver.
    gate = terms(6, [(1, [0, 3, 4]), (-1, [1, 2, 4]),
                     (-1, [0, 3, 5]), (1, [1, 2, 5])])
    diagonal = [[2 if i == j else 0 for j in range(6)] for i in range(6)]
    cases += [case('determinant_singular_gate', [1, 2, 2, 4, 3, 7],
                   [diagonal], gate, True),
              case('determinant_equal_lengths', [2, 1, 1, 3, 7, 7],
                   [diagonal], gate, True),
              case('determinant_nonzero_difference', [2, 1, 1, 3, 7, 6],
                   [diagonal], gate, False)]
    # Actual tuple morphisms: with seeds s,t and alphabet a,b,s,t, loop
    # s->sa,t->tb, then erase s,t. The outputs are (a^m,b^m), m>=0.
    # This specifically checks separate component counts and seed copying.
    morphisms = [[[0], [1], [2, 0], [3, 1]], [[0], [1], [], []]]
    matrices = []
    for morphism in morphisms:
        matrices.append([[morphism[j % 4].count(i % 4) if i//4 == j//4 else 0
                          for j in range(8)] for i in range(8)])
    for name, seeds, poly, expected in [
        ('tuple_component_quadratic', [2, 3], terms(8, [(1,[0,0]),(-1,[0,5])]), True),
        ('tuple_component_distinction', [2, 3], terms(8, [(1,[0]),(-1,[4])]), False),
        ('tuple_duplicated_seed', [2, 2], terms(8, [(1,[0]),(-1,[4])]), True),
    ]:
        seed = [int(i % 4 == seeds[i//4]) for i in range(8)]
        c = case(name, seed, matrices, poly, expected,
                 edges=[[0,0,0],[0,1,1]], finals=[1], terminal_indices=[0,1,4,5])
        c['tuple_morphisms'] = morphisms
        c['tuple_seeds'] = seeds
        c['tuple_alphabet_size'] = 4
        cases.append(c)
    # A branching finite control family exhaustively enumerable in full.
    rng = random.Random(38092026)
    for index in range(24):
        n = 2 + index % 2
        matrices = [[[rng.randrange(3) for _ in range(n)] for _ in range(n)]
                    for _ in range(2)]
        seed = [rng.randrange(3) for _ in range(n)]
        polynomial = terms(n, [(rng.choice([-2, -1, 1, 2]),
                                [rng.randrange(n) for _ in range(rng.randrange(4))])
                               for _ in range(5)])
        edges = [[q, q + 1, m] for q in range(5) for m in range(2)]
        c = case('finite_control_%02d' % index, seed, matrices, polynomial,
                 None, edges=edges, finals=[5])
        values = []
        for choices in product(range(2), repeat=5):
            counts = tuple(seed)
            for m in choices:
                counts = apply_matrix(matrices[m], counts)
            values.append(evaluate_polynomial(counts, polynomial))
        c['expected'] = all(value == 0 for value in values)
        c['exhaustive_paths'] = len(values)
        cases.append(c)
    return cases


def words(rank, max_length):
    output = [()]
    layer = [()]
    for _ in range(max_length):
        layer = [w + (a,) for w in layer for a in range(-rank, rank + 1)
                 if a and (not w or w[-1] != -a)]
        output += layer
    return output


def det(matrix):
    if not matrix:
        return 1
    return sum((-1) ** j * matrix[0][j] *
               det([row[:j] + row[j+1:] for row in matrix[1:]])
               for j in range(len(matrix)))


def group_checks():
    short = words(2, 3)
    triangle_count = 0
    for x in short:
        for y in short:
            s, t, r = cancellation_triangle(x, y)
            assert x == s + t and y == inverse(t) + r
            assert word_reduce(x + y) == s + r
            triangle_count += 1
    # Test the recognizing monoid on ALL words, not only reduced ones.
    raw = [w for length in range(4) for w in product([-2, -1, 1, 2], repeat=length)]
    monoid_products = 0
    for x in raw:
        assert regular_summary(inverse(x)) == summary_inverse(regular_summary(x))
        assert summary_is_cyclic(regular_summary(x)) == (
            x == word_reduce(x) and (not x or x[0] != -x[-1]))
        for y in raw:
            assert regular_summary(x + y) == summary_product(
                regular_summary(x), regular_summary(y))
            monoid_products += 1
    # KLSS Corollary 1.5 at M=2: a*b*a^-3*b^-1 and a^2*b*a^-2*b^-1.
    u, v = (1, 2, -1, -1, -1, -2), (1, 1, 2, -1, -1, -2)
    records = []
    image_words = words(2, 2)
    for x, y in product(image_words, repeat=2):
        images = [x, y]
        matrix = [[w.count(i) - w.count(-i) for w in images] for i in [1, 2]]
        determinant = det(matrix)
        lu, lv = len(cyclic_reduce(substitute(u, images))), len(cyclic_reduce(substitute(v, images)))
        assert determinant * (lu - lv) == 0
        records.append(dict(rank=2, images=[list(w) for w in images],
                            u=list(u), v=list(v), determinant=determinant,
                            lengths=[lu, lv], gated_value=determinant * (lu-lv)))
    assert any(r['lengths'][0] != r['lengths'][1] for r in records)
    assert any(r['determinant'] != 0 for r in records)
    special = next(r for r in records if r['images'] == [[1], []])
    assert special['determinant'] == 0 and special['lengths'] == [2, 0]
    # F3 examples: a genuinely distinguishing Nielsen map, equal/inverse
    # words, conjugates, an injective nonsurjective map, and zero inputs.
    base = (1, 2, -1, 3, 2)
    for images in [[(1,), (2,), (3,)], [(1, 2), (2,), (3,)],
                   [(1, 1), (2,), (3,)], [(), (2,), (3,)]]:
        for first, second in [(base, inverse(base)), (base, (3,) + base + (-3,)),
                              ((1,), (2,)), ((), (1,)), ((), ())]:
            matrix = [[w.count(i)-w.count(-i) for w in images] for i in [1,2,3]]
            determinant = det(matrix)
            lengths = [len(cyclic_reduce(substitute(w, images))) for w in [first, second]]
            records.append(dict(rank=3, images=[list(w) for w in images],
                                u=list(first), v=list(second), determinant=determinant,
                                lengths=lengths, gated_value=determinant*(lengths[0]-lengths[1])))
    return dict(cancellation_triangles=triangle_count, regular_monoid_products=monoid_products,
                raw_words=len(raw), word_records=records)


def gap_value(x):
    if x is None:
        return 'fail'
    if isinstance(x, bool):
        return 'true' if x else 'false'
    if isinstance(x, int):
        return str(x)
    if isinstance(x, str):
        return json.dumps(x)
    if isinstance(x, (tuple, list)):
        return '[' + ','.join(gap_value(v) for v in x) + ']'
    if isinstance(x, dict):
        return 'rec(' + ','.join(k + ':=' + gap_value(v) for k, v in x.items()) + ')'
    raise TypeError(type(x))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    certificates = []
    for c in polynomial_cases():
        answer = solve(c)
        assert answer['vanishes'] == c['expected'], c['name']
        if c['name'] == 'six_zero_samples_then_failure':
            assert len(answer['witness']['path']) >= 6
        certificates.append(answer)
        print(c['name'], answer['vanishes'], 'basis', answer['basis_vectors'], flush=True)
    group = group_checks()
    result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Finite polynomial-identity stage and elementary free-word reductions only; no recompression implementation.',
                  random_seed=38092026, polynomial_cases=certificates, group_checks=group)
    (out/'checks.json').write_text(json.dumps(result, indent=2)+'\n')
    (out/'fixtures.g').write_text('F38Cases := '+gap_value(certificates)+';;\n'+
                                'F38Words := '+gap_value(group['word_records'])+';;\n')
    for name in ['f38_polynomial_identity.py', 'check_f38_polynomial.py']:
        (out/name).write_bytes((ROOT/'scripts'/name).read_bytes())
    print('PASS F38 polynomial stage:',len(certificates),'controlled systems;',
          group['cancellation_triangles'],'cancellation triangles;',
          group['regular_monoid_products'],'monoid products;',
          len(group['word_records']),'word records')


if __name__ == '__main__':
    main()
