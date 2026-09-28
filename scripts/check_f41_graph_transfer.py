#!/usr/bin/env python3
"""Exact finite checks for the F41 graph argument, not a growth proof.

Exhaust all based cyclically reduced paths of topological length <=8
in the three rank-two leaf-free topological graphs. Separately generate
18 marked, immersed labelled graphs for independent GAP verification.
No numerical fitting of an asymptotic rate is performed.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
import hashlib
import json
from pathlib import Path
import random

OUT = Path('research/certificates/F41-graph-transfer')
GRAPHS = {
    'rose': {'edges': [(0, 0), (0, 0)], 'tree': []},
    'theta': {'edges': [(0, 1), (0, 1), (0, 1)], 'tree': [1]},
    'barbell': {'edges': [(0, 0), (0, 1), (1, 1)], 'tree': [2]},
}


def inverse(w):
    return tuple(-x for x in reversed(w))


def reduce_word(w):
    result = []
    for x in w:
        if result and result[-1] == -x:
            result.pop()
        else:
            result.append(x)
    return tuple(result)


def cyclic_reduce(w):
    w = reduce_word(w)
    i = 0
    while 2*i < len(w) and w[i] == -w[-i-1]:
        i += 1
    return w[i:len(w)-i] if i else w


def canonical(w):
    w = cyclic_reduce(w)
    return min(w[i:]+w[:i] for i in range(len(w))) if w else ()


def substitute(w, images):
    return reduce_word(x for a in w for x in (
        images[a-1] if a > 0 else inverse(images[-a-1])))


def whitehead_maps():
    result = []
    letters = (1, -1, 2, -2)
    for a in letters:
        others = [x for x in letters if x not in (a, -a)]
        for flags in product((False, True), repeat=2):
            subset = {a} | {x for x, flag in zip(others, flags) if flag}
            images = []
            for x in (1, 2):
                if x in (a, -a):
                    images.append((x,))
                else:
                    images.append(((-a,) if -x in subset else ()) + (x,)
                                  + ((a,) if x in subset else ()))
            result.append(tuple(images))
    return tuple(result)


WHITEHEAD = whitehead_maps()


@lru_cache(None)
def primitive(w):
    """Whitehead's length-reduction criterion, in rank two only."""
    w = canonical(w)
    while len(w) > 1:
        shorter = next((v for images in WHITEHEAD
                        if len(v := canonical(substitute(w, images))) < len(w)), None)
        if shorter is None:
            return False
        w = shorter
    return bool(w)


def root(w):
    for d in range(1, len(w)+1):
        if len(w) % d == 0 and w == w[:d]*(len(w)//d):
            return w[:d]
    raise AssertionError('nonempty input required')


def adjacency(graph):
    adj = defaultdict(list)
    for i, (a, b) in enumerate(graph['edges'], 1):
        adj[a].append((i, b))
        adj[b].append((-i, a))
    return adj


def collapse(w, graph):
    non_tree = [i for i in range(1, len(graph['edges'])+1)
                if i not in graph['tree']]
    renumber = {e: i for i, e in enumerate(non_tree, 1)}
    return tuple((1 if e > 0 else -1)*renumber[abs(e)]
                 for e in w if abs(e) in renumber)


def exhaustive_graph_check(bound=8):
    summary = {}
    for name, graph in GRAPHS.items():
        adj = adjacency(graph)
        counts = Counter()
        for start in adj:
            encodings = {}

            def walk(path, vertex):
                if path and vertex == start and path[-1] != -path[0]:
                    z = collapse(path, graph)
                    assert z and cyclic_reduce(z) == z
                    assert z not in encodings or encodings[z] == path
                    encodings[z] = path
                    counts['cyclic_based_paths'] += 1
                    mult = Counter(map(abs, path))
                    fills = not primitive(canonical(root(z)))
                    if fills:
                        assert len(mult) == len(graph['edges'])
                        assert min(mult.values()) >= 2
                        counts['filling_nonprimitive_paths'] += 1
                    else:
                        if len(mult) < len(graph['edges']):
                            counts['proper_factor_unused_edge_controls'] += 1
                        if 1 in mult.values():
                            assert primitive(canonical(z))
                            counts['single_traverse_primitive_controls'] += 1
                if len(path) < bound:
                    for edge, end in adj[vertex]:
                        if not path or edge != -path[-1]:
                            walk(path+(edge,), end)

            walk((), start)
        assert counts['filling_nonprimitive_paths'] > 0
        assert counts['single_traverse_primitive_controls'] > 0
        summary[name] = dict(counts)
    return summary


def tree_path(graph, start, end):
    adj = adjacency(graph)
    todo = [(start, ())]
    seen = {start}
    while todo:
        vertex, path = todo.pop()
        if vertex == end:
            return path
        for e, nxt in adj[vertex]:
            if abs(e) in graph['tree'] and nxt not in seen:
                seen.add(nxt)
                todo.append((nxt, path+(e,)))
    raise AssertionError('not a maximal tree')


def graph_basis(graph):
    return tuple(tree_path(graph, 0, a)+(i,)+tree_path(graph, b, 0)
                 for i, (a, b) in enumerate(graph['edges'], 1)
                 if i not in graph['tree'])


def random_labels(graph, rank, rng):
    letters = tuple(x for i in range(1, rank+1) for x in (i, -i))
    for _ in range(10000):
        labels = []
        for _edge in graph['edges']:
            w = ()
            for _ in range(rng.randint(1, 5)):
                w += (rng.choice([a for a in letters if not w or a != -w[-1]]),)
            labels.append(w)
        outgoing = defaultdict(list)
        for (a, b), w in zip(graph['edges'], labels):
            outgoing[a].append(w[0])
            outgoing[b].append(-w[-1])
        if all(len(v) == len(set(v)) for v in outgoing.values()):
            return tuple(labels)
    raise AssertionError('bounded label generation failed')


def fixtures(seed=20260928):
    rng = random.Random(seed)
    records = []
    seeds = ((1, 1, 2, 2, 2), (1, 2, -1, -2), (1, 1, 2, 2))
    for name, graph in GRAPHS.items():
        for rank in (3, 4):
            for u in seeds:
                assert not primitive(canonical(u))
                images = ((1,), (2,))
                moves = []
                for _ in range(6):
                    i = rng.randrange(2)
                    j = 1-i
                    sign = rng.choice((-1, 1))
                    # Postcompose by a Nielsen map on the abstract alphabet.
                    step = [(1,), (2,)]
                    step[i] = (i+1, sign*(j+1))
                    images = tuple(substitute(w, step) for w in images)
                    moves.append([i+1, j+1, sign])
                v = cyclic_reduce(substitute(u, images))
                basis = graph_basis(graph)
                raw_path = substitute(v, basis)
                path = cyclic_reduce(raw_path)
                assert collapse(path, graph) == v
                mult = [path.count(e)+path.count(-e)
                        for e in range(1, len(graph['edges'])+1)]
                assert all(m >= 2 for m in mult)
                labels = random_labels(graph, rank, rng)
                word = substitute(path, labels)
                lengths = list(map(len, labels))
                n, ell = len(word), len(path)
                assert cyclic_reduce(word) == word
                assert n == sum(m*l for m, l in zip(mult, lengths))
                assert n-ell >= 2*sum(l-1 for l in lengths)
                records.append(dict(graph=name, ambient_rank=rank, u=u,
                                    nielsen_moves=moves, automorphism_images=images,
                                    abstract_word=v, graph_basis=basis,
                                    raw_path=raw_path, cyclic_path=path,
                                    labels=labels, word=word, lengths=lengths,
                                    multiplicities=mult, ambient_length=n,
                                    topological_length=ell))
    return records


def gap_literal(value):
    if isinstance(value, (list, tuple)):
        return '['+','.join(gap_literal(v) for v in value)+']'
    return str(value)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    summary = exhaustive_graph_check()
    records = fixtures()
    # Explicit negative control: noninjective evaluations cover all words.
    for g in ((1,), (1, 2, -1, 3), (1, 2, -1, -2)):
        assert substitute((1, 1, 2, 2, 2), (inverse(g), g)) == g
    (OUT/'fixtures.json').write_text(json.dumps(records, indent=2)+'\n')
    gap_rows = [[r['ambient_rank'], r['u'], r['nielsen_moves'],
                 r['automorphism_images'], r['abstract_word'],
                 r['graph_basis'], r['raw_path'], r['cyclic_path'],
                 r['labels'], r['word']] for r in records]
    (OUT/'fixtures.g').write_text('F41Fixtures := '+gap_literal(gap_rows)+';;\n')
    result = dict(seed=20260928, path_bound=8, graph_checks=summary,
                  labelled_fixtures=len(records),
                  noninjective_negative_controls=3,
                  max_fixture_ambient_length=max(r['ambient_length'] for r in records),
                  limitations='Finite consistency checks; not an asymptotic proof or independent specialist review.')
    (OUT/'checks.json').write_text(json.dumps(result, indent=2)+'\n')
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in OUT.iterdir() if p.name != 'artifact-hashes.json'}
    (OUT/'artifact-hashes.json').write_text(json.dumps(hashes, indent=2)+'\n')
    print(json.dumps(result))
    print('PASS F41 finite graph transfer checks')


if __name__ == '__main__':
    main()
