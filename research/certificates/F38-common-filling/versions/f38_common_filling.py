#!/usr/bin/env python3
"""Finite common-filling-carrier test for F38(c), using prior theorems.

Both conjugacy classes must fill the carrier. A positive answer implies
bounded comparison even under all injective homomorphisms. A negative
carrier search does NOT imply failure of the original automorphism test.
"""
from collections import deque
from itertools import combinations
from f38_stabilizer_obstruction import reduce_word, inv, cyclic, apply
from f38_filling_recognition import filling


def canonical(edges, base=0):
    """Connected folded inverse graph; retain positive oriented edges."""
    adjacency = {}
    for s, a, t in edges:
        assert a > 0
        for v, label, w in [(s, a, t), (t, -a, s)]:
            assert (v, label) not in adjacency or adjacency[v, label] == w
            adjacency[v, label] = w
    number = {base: 0}; queue = [base]
    for v in queue:
        for (_, a), w in sorted(adjacency.items()):
            if _ == v and w not in number:
                number[w] = len(number); queue.append(w)
    assert set(number) == {v for s, a, t in edges for v in (s, t)}
    return tuple(sorted((number[s], a, number[t]) for s, a, t in set(edges)))


def cycle_graph(word):
    word = cyclic(word); assert word
    edges = []
    for i, a in enumerate(word):
        j = (i+1) % len(word)
        edges.append((i, a, j) if a > 0 else (j, -a, i))
    return canonical(edges)


def quotient(graph, pairs):
    n = 1+max(max(s, t) for s, a, t in graph)
    parent = list(range(n))
    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]; v = parent[v]
        return v
    def join(v, w):
        v, w = root(v), root(w)
        if v == w: return False
        parent[max(v, w)] = min(v, w); return True
    for v, w in pairs: join(v, w)
    while True:
        transitions = {}; changed = False
        for s, a, t in graph:
            for v, label, w in [(s, a, t), (t, -a, s)]:
                key = root(v), label
                if key in transitions:
                    changed = join(w, transitions[key]) or changed
                else: transitions[key] = root(w)
        if not changed: break
    return canonical([(root(s), a, root(t)) for s, a, t in graph], root(0))


def fringe(word):
    """All folded quotient graphs, by successive vertex identifications."""
    initial = cycle_graph(word); seen = {initial}; pending = deque([initial])
    while pending:
        graph = pending.popleft()
        yield graph
        n = 1+max(max(s, t) for s, a, t in graph)
        for pair in combinations(range(n), 2):
            other = quotient(graph, [pair])
            if other not in seen:
                seen.add(other); pending.append(other)


def basis_data(graph):
    adjacency = {}
    for i, (s, a, t) in enumerate(graph):
        adjacency[s, a] = t, i, 1
        adjacency[t, -a] = s, i, -1
    paths = {0: ()}; tree = set(); queue = [0]
    for v in queue:
        for (source, a), (w, i, sign) in sorted(adjacency.items()):
            if source == v and w not in paths:
                paths[w] = paths[v]+(a,); tree.add(i); queue.append(w)
    basis = []; coordinates = {}
    for i, (s, a, t) in enumerate(graph):
        if i not in tree:
            coordinates[i] = len(basis)+1
            basis.append(reduce_word(paths[s]+(a,)+inv(paths[t])))
    assert len(basis) == len(graph)-len(paths)+1
    def rewrite(word, start=0):
        v = start; out = []
        for a in word:
            if (v, a) not in adjacency: return None
            v, i, sign = adjacency[v, a]
            if i in coordinates: out.append(sign*coordinates[i])
        if v != start: return None
        out = reduce_word(out)
        assert apply(basis, out) == reduce_word(paths[start]+tuple(word)+inv(paths[start]))
        return out
    return basis, paths, rewrite


def filling_in_basis(rank, word, cache):
    word = cyclic(word)
    if rank == 1:
        return dict(filling=bool(word), reason='nonzero_word_in_infinite_cyclic_group')
    # A word missing a basis letter, or containing a letter just once,
    # lies in a proper free factor. Avoid a needless high-rank orbit test.
    counts = [sum(abs(a) == i for a in word) for i in range(1, rank+1)]
    if min(counts) <= 1:
        return dict(filling=False, reason='missing_or_single_occurrence_basis_letter')
    key = rank, word
    if key not in cache: cache[key] = filling(rank, word)
    return cache[key]


def common_filling_carrier(rank, u, v):
    u, v = cyclic(u), cyclic(v)
    assert rank >= 1 and u and v
    assert all(1 <= abs(a) <= rank for a in u+v)
    cache = {}; considered = 0; closed_lifts = 0; filling_tests = []
    for graph in fringe(u):
        considered += 1
        basis, paths, rewrite = basis_data(graph); h = len(basis)
        left = rewrite(u); assert left is not None
        right_lifts = [(vertex, rewrite(v, vertex)) for vertex in paths]
        right_lifts = [(vertex, word) for vertex, word in right_lifts if word is not None]
        closed_lifts += len(right_lifts)
        if not right_lifts: continue
        first = filling_in_basis(h, left, cache)
        if 'outer_group' in first: filling_tests.append(first)
        if not first['filling']: continue
        for vertex, right in right_lifts:
            second = filling_in_basis(h, right, cache)
            if 'outer_group' in second: filling_tests.append(second)
            if not second['filling']: continue
            return dict(status='boundedly_equivalent_prior_common_filling_case',
                rank=rank, u=u, v=v, graphs_considered=considered,
                closed_lifts=closed_lifts, graph=graph, basis=basis,
                left=left, right=right, conjugator=paths[vertex],
                filling_tests=filling_tests, carrier_rank=h)
    return dict(status='no_common_filling_carrier_not_a_boundedness_decision',
        rank=rank, u=u, v=v, graphs_considered=considered,
        closed_lifts=closed_lifts, filling_tests=filling_tests)
