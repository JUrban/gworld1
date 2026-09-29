#!/usr/bin/env python3
"""Exact finite length envelopes, not a decision of linear boundedness.

The one-way stabilizer orbit decides whether any finite-valued envelope
exists. On success, a finite Whitehead pair graph computes its values up
to a requested first-word length. Classical peak reduction is imported.
"""
from f38_stabilizer_obstruction import (apply, cyclic, compose, identity,
    whiteheads, stabilizer, finite_conjugacy_orbit)


def length_envelope(rank, u, v, bound, max_states=None):
    u, v = cyclic(u), cyclic(v)
    if not u or not v:
        raise ValueError('Nonidentity inputs required')
    if rank < 2 or bound < 0:
        raise ValueError('This implementation expects rank>=2 and bound>=0')
    generators, stab_graph = stabilizer(rank, u)
    orbit = finite_conjugacy_orbit(rank, generators, v)
    report = dict(rank=rank, u=u, v=v, bound=bound,
                  stabilizer_generators=generators, stabilizer_graph=stab_graph,
                  stabilizer_orbit=orbit)
    if not orbit['finite']:
        report['status'] = 'no_finite_global_envelope'
        return report
    moves = whiteheads(rank)
    mu = identity(rank)
    first, second = u, v
    while True:
        for move in moves:
            nxt = cyclic(apply(move[0], first))
            if len(nxt) < len(first):
                first, second = nxt, cyclic(apply(move[0], second))
                mu = compose(move, mu)
                break
        else:
            break
    minimum = len(first)
    report.update(minimum=minimum, minimizer=mu, root=(first, second), moves=moves)
    if bound < minimum:
        report.update(status='empty_below_minimum', envelope=[None]*(bound+1))
        return report
    vertices = [(first, second)]
    index = {vertices[0]: 0}
    predecessors, adjacency = [None], []
    for i, (left, right) in enumerate(vertices):
        edges = []
        for j, move in enumerate(moves):
            x = cyclic(apply(move[0], left))
            assert len(x) >= minimum
            if len(x) > bound:
                continue
            y = cyclic(apply(move[0], right))
            assert len(y) <= 2*len(right)
            assert len(right) <= 2*len(y)
            pair = (x,y)
            if pair not in index:
                if max_states is not None and len(vertices) >= max_states:
                    report.update(status='incomplete_resource_guard', vertices_seen=len(vertices))
                    return report
                index[pair] = len(vertices)
                vertices.append(pair)
                predecessors.append([i,j])
            edges.append([j,index[pair]])
        adjacency.append(edges)
    maxima = [None]*(bound+1)
    for left,right in vertices:
        n = len(left)
        maxima[n] = max(maxima[n] or 0,len(right))
    envelope = maxima[:]
    for n in range(minimum+1,bound+1):
        envelope[n] = max(envelope[n] or 0,envelope[n-1])
    B = envelope[minimum]
    assert all(envelope[n] <= B*2**(n-minimum) for n in range(minimum,bound+1))
    report.update(status='finite_envelope_exact_prefix', vertices=vertices,
                  predecessors=predecessors, adjacency=adjacency,
                  maxima_at_exact_length=maxima, envelope=envelope,
                  exponential_constant=B, exponential_base=2,
                  linear_bound_status='not_decided')
    return report
