#!/usr/bin/env python3
"""Decide a necessary stabilizer condition for F38(c), not F38(c) itself.

Uses Whitehead peak reduction and Handel--Mosher's level-three aperiodicity.
On failure returns an exact automorphism witness. On success only the
stabilizer condition has passed; no bounded-length conclusion follows here.
"""
from itertools import permutations, product


def reduce_word(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def inv(word):
    return tuple(-a for a in word[::-1])


def cyclic(word):
    word = reduce_word(word)
    while len(word) > 1 and word[0] == -word[-1]:
        word = word[1:-1]
    if not word:
        return ()
    return min(word[i:] + word[:i] for i in range(len(word)))


def apply(images, word):
    return reduce_word(a for s in word for a in
                       (images[s-1] if s > 0 else inv(images[-s-1])))


def compose(f, g):
    """f after g; automorphisms are pairs (images, inverse images)."""
    return (tuple(apply(f[0], w) for w in g[0]),
            tuple(apply(g[1], w) for w in f[1]))


def identity(rank):
    images = tuple((i,) for i in range(1, rank + 1))
    return images, images


def inverse_auto(f):
    return f[1], f[0]


def check_auto(f):
    n = len(f[0])
    assert len(f[1]) == n
    assert compose(f, inverse_auto(f)) == identity(n)
    assert compose(inverse_auto(f), f) == identity(n)


def whiteheads(rank):
    out = {}
    for perm in permutations(range(1, rank + 1)):
        for signs in product((-1, 1), repeat=rank):
            images = tuple((s*p,) for s, p in zip(signs, perm))
            inverse = [None] * rank
            for i, word in enumerate(images, 1):
                inverse[abs(word[0])-1] = (i if word[0] > 0 else -i,)
            out[images] = (images, tuple(inverse))
    for a in range(-rank, rank + 1):
        if a == 0:
            continue
        others = [i for i in range(1, rank + 1) if i != abs(a)]
        for bits in product((0, 1), repeat=2*len(others)):
            images = list(identity(rank)[0])
            inverse = list(images)
            for j, x in enumerate(others):
                left, right = bits[2*j:2*j+2]
                images[x-1] = ((-a,) if left else ()) + (x,) + ((a,) if right else ())
                inverse[x-1] = ((a,) if left else ()) + (x,) + ((-a,) if right else ())
            out[tuple(images)] = tuple(images), tuple(inverse)
    out.pop(identity(rank)[0], None)
    result = list(out.values())
    for f in result:
        check_auto(f)
    return result


def stabilizer(rank, word):
    """Full outer conjugacy stabilizer, represented by actual automorphisms.

    Inner representatives/duplicates may remain. They act trivially on
    conjugacy classes and do not invalidate the generated outer subgroup.
    """
    assert cyclic(word), 'Nontrivial input required'
    moves = whiteheads(rank)
    u, mu = cyclic(word), identity(rank)
    reductions = 0
    while True:
        for f in moves:
            v = cyclic(apply(f[0], u))
            if len(v) < len(u):
                mu = compose(f, mu)
                u = v
                reductions += 1
                break
        else:
            break
    transports = {u: identity(rank)}
    queue = [u]
    generators = {}
    edges = 0
    for w in queue:
        transport = transports[w]
        for f in moves:
            v = cyclic(apply(f[0], w))
            assert len(v) >= len(u), 'Minimization was incomplete'
            if len(v) != len(u):
                continue
            edges += 1
            step = compose(f, transport)
            if v not in transports:
                transports[v] = step
                queue.append(v)
            loop = compose(inverse_auto(transports[v]), step)
            if loop != identity(rank):
                generators[loop[0]] = loop
    original_generators = []
    for loop in generators.values():
        f = compose(inverse_auto(mu), compose(loop, mu))
        assert cyclic(apply(f[0], word)) == cyclic(word)
        original_generators.append(f)
    return original_generators, dict(minimal_word=u, reductions=reductions,
                                    vertices=len(queue), edges=edges,
                                    generators=len(original_generators),
                                    whitehead_moves=len(moves))


def mod3_matrix(images):
    n = len(images)
    matrix = [[0]*n for _ in range(n)]
    for j, word in enumerate(images):
        for s in word:
            matrix[abs(s)-1][j] += 1 if s > 0 else -1
    return tuple(x % 3 for row in matrix for x in row)


def matrix_product(a, b, n):
    return tuple(sum(a[n*i+k]*b[n*k+j] for k in range(n)) % 3
                 for i in range(n) for j in range(n))


def finite_conjugacy_orbit(rank, generators, word):
    """Exact finite-orbit decision, via a finite mod-3 matrix search.

    Distinct conjugacy images at the same matrix give an aperiodic witness.
    Otherwise the completed matrix graph is an invariant finite orbit.
    """
    canonical = cyclic(word)
    if all(cyclic(apply(f[0], word)) == canonical for f in generators):
        return dict(finite=True, orbit=[canonical], matrix_states=0,
                    transitions=len(generators), shortcut='common_fixed_class')
    matrices = [mod3_matrix(f[0]) for f in generators]
    ident = identity(rank)
    base = mod3_matrix(ident[0])
    states = {base: (ident, cyclic(word))}
    queue = [base]
    edges = 0
    for a in queue:
        transport, current = states[a]
        for f, m in zip(generators, matrices):
            b = matrix_product(m, a, rank)
            image = cyclic(apply(f[0], current))
            edges += 1
            if b not in states:
                step = compose(f, transport)
                states[b] = step, image
                queue.append(b)
            elif states[b][1] != image:
                step = compose(f, transport)
                witness = compose(inverse_auto(states[b][0]), step)
                check_auto(witness)
                assert mod3_matrix(witness[0]) == base
                assert cyclic(apply(witness[0], word)) != cyclic(word)
                return dict(finite=False, witness=witness,
                            matrix_states=len(states), transitions=edges)
    return dict(finite=True, orbit=sorted({row[1] for row in states.values()}),
                matrix_states=len(states), transitions=edges)


def necessary_condition(rank, u, v):
    """Return a failure witness or a passed NECESSARY condition only."""
    assert cyclic(u) and cyclic(v), 'Identity/undefined ratios excluded'
    reports = []
    for fixed, moved in [(u, v), (v, u)]:
        gens, graph = stabilizer(rank, fixed)
        result = finite_conjugacy_orbit(rank, gens, moved)
        reports.append(dict(fixed=fixed, moved=moved, graph=graph,
                            generators=gens, orbit_check=result))
        if not result['finite']:
            witness = result['witness']
            assert cyclic(apply(witness[0], fixed)) == cyclic(fixed)
            return dict(status='not_boundedly_equivalent', reports=reports,
                        witness=witness, fixed=fixed, moved=moved)
    return dict(status='necessary_condition_passed_only', reports=reports)
