#!/usr/bin/env python3
"""Exact polynomial-identity test on regularly controlled count matrices.

This is the finite linear-algebra stage of the F38(a) candidate, not an
implementation of the imported free-group equation/recompression theorem.
Matrices act on columns; path order is application order. Reverse a source
control automaton first if it uses function-composition order.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations_with_replacement


def monomials(n, degree):
    result = []
    for d in range(degree + 1):
        for indices in combinations_with_replacement(range(n), d):
            exponents = [0] * n
            for i in indices:
                exponents[i] += 1
            result.append(tuple(exponents))
    return result


def evaluate_monomial(counts, exponents):
    result = 1
    for count, exponent in zip(counts, exponents):
        result *= count ** exponent
    return result


def evaluate_polynomial(counts, polynomial):
    return sum(coefficient * evaluate_monomial(counts, exponents)
               for coefficient, exponents in polynomial)


def apply_matrix(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


class Span:
    """Rational row echelon basis, keeping path representatives separately."""
    def __init__(self):
        self.rows = {}

    def add(self, vector):
        row = {i: Fraction(x) for i, x in enumerate(vector) if x}
        while row:
            pivot = min(row)
            if pivot not in self.rows:
                scale = row[pivot]
                self.rows[pivot] = {i: x / scale for i, x in row.items()}
                return True
            scale = row[pivot]
            for i, x in self.rows[pivot].items():
                row[i] = row.get(i, 0) - scale * x
                if not row[i]:
                    del row[i]
        return False


def solve(case):
    """Return a closed-span certificate and an actual path if identity fails.

    case fields: seed, matrices, edges [source,target,matrix_index], initials,
    finals, polynomial [[integer coefficient, exponent vector],...], and an
    optional set terminal_indices. All matrices and seeds are nonnegative
    integer counts. The finite support product handles terminal filtering.
    """
    seed = tuple(case['seed'])
    n = len(seed)
    assert n > 0 and all(type(x) is int and x >= 0 for x in seed)
    matrices = case['matrices']
    for matrix in matrices:
        assert len(matrix) == n and all(len(row) == n for row in matrix)
        assert all(type(x) is int and x >= 0 for row in matrix for x in row)
    polynomial = case['polynomial']
    assert all(type(c) is int and len(e) == n and
               all(type(x) is int and x >= 0 for x in e) for c, e in polynomial)
    degree = max((sum(e) for c, e in polynomial if c), default=0)
    mons = monomials(n, degree)
    outgoing = {}
    for index, (source, target, matrix_index) in enumerate(case['edges']):
        assert 0 <= matrix_index < len(matrices)
        outgoing.setdefault(source, []).append((index, target, matrix_index))
    finals = set(case['finals'])
    terminal = set(case.get('terminal_indices', range(n)))
    spans, representatives = {}, {}
    queue = deque((state, seed, ()) for state in case['initials'])
    witness = None
    attempted = 0
    while queue:
        state, counts, path = queue.popleft()
        support = tuple(i for i, x in enumerate(counts) if x)
        key = state, support
        span = spans.setdefault(key, Span())
        vector = tuple(evaluate_monomial(counts, e) for e in mons)
        attempted += 1
        if not span.add(vector):
            continue
        record = {'counts': list(counts), 'path': list(path)}
        representatives.setdefault(key, []).append(record)
        value = evaluate_polynomial(counts, polynomial)
        if state in finals and set(support) <= terminal and value and witness is None:
            witness = {'state': state, **record, 'value': value}
        for edge_index, target, matrix_index in outgoing.get(state, []):
            queue.append((target, apply_matrix(matrices[matrix_index], counts),
                          path + (edge_index,)))
    certificate = dict(case)
    certificate.update(degree=degree, monomials=[list(e) for e in mons],
                       vanishes=witness is None, witness=witness,
                       attempted_vectors=attempted,
                       basis=[{'state': state, 'support': list(support),
                               'records': representatives[state, support]}
                              for state, support in sorted(representatives)])
    certificate['basis_vectors'] = sum(len(b['records']) for b in certificate['basis'])
    return certificate


def word_reduce(word):
    output = []
    for letter in word:
        if output and output[-1] == -letter:
            output.pop()
        else:
            output.append(letter)
    return tuple(output)


def inverse(word):
    return tuple(-x for x in reversed(word))


def cyclic_reduce(word):
    word = word_reduce(word)
    start, stop = 0, len(word)
    while stop - start >= 2 and word[start] == -word[stop - 1]:
        start += 1
        stop -= 1
    return word[start:stop]


def substitute(word, images):
    return word_reduce(x for letter in word
                       for x in (images[letter - 1] if letter > 0
                                 else inverse(images[-letter - 1])))


def cancellation_triangle(x, y):
    """Return S,T,R with x=S T, y=T^-1 R, reduced(xy)=S R."""
    assert word_reduce(x) == tuple(x) and word_reduce(y) == tuple(y)
    cancellation = 0
    while (cancellation < min(len(x), len(y)) and
           x[len(x) - cancellation - 1] == -y[cancellation]):
        cancellation += 1
    cut = len(x) - cancellation
    return tuple(x[:cut]), tuple(x[cut:]), tuple(y[cancellation:])


def regular_summary(word):
    """Finite involutive monoid: zero for unreduced; otherwise endpoints.

    This suffices to impose both reduced and cyclically reduced constraints.
    The identity is (), the absorbing zero is None, and other values are
    (first_letter,last_letter). No length bound enters the summary.
    """
    if tuple(word) != word_reduce(word):
        return None
    return (word[0], word[-1]) if word else ()


def summary_product(x, y):
    if x is None or y is None:
        return None
    if not x:
        return y
    if not y:
        return x
    return None if x[-1] == -y[0] else (x[0], y[-1])


def summary_inverse(x):
    if x is None or not x:
        return x
    return -x[-1], -x[0]


def summary_is_cyclic(x):
    return x is not None and (not x or x[0] != -x[-1])
