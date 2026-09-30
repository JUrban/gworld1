#!/usr/bin/env python3
"""Construct a shorter representative of the same strict bridge flow.

This is a finite support-connection heuristic, not a geodesic oracle.
Every added connector is traversed once in each direction.
"""
from collections import defaultdict, deque

from g9_flow_unfolding import bridge, flow, path


def ends(edge):
    base, axis = edge
    target = list(base)
    target[axis] += 1
    return base, tuple(target)


def shorten(word):
    word = tuple(word)
    assert bridge(2, word)
    vertices = path(2, word)
    traversed = set()
    for p, q, letter in zip(vertices, vertices[1:], word):
        traversed.add((p if letter > 0 else q, abs(letter)-1))
    net = {(v, j): c for v, j, c in flow(2, word)}
    parent = {v: v for v in vertices}

    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(u, v):
        a, b = root(u), root(v)
        if a == b:
            return False
        parent[a] = b
        return True

    required = set()
    for edge in net:
        u, v = ends(edge)
        required.update((u, v))
        union(u, v)
    connectors = set()
    for edge in sorted(traversed-net.keys()):
        if union(*ends(edge)):
            connectors.add(edge)
    assert len({root(v) for v in required}) == 1
    # Remove leaves with no required flow support; keep necessary Steiner vertices.
    incidence = defaultdict(set)
    for edge in connectors:
        for v in ends(edge):
            incidence[v].add(edge)
    leaves = deque(v for v in incidence if v not in required and len(incidence[v]) == 1)
    while leaves:
        v = leaves.popleft()
        if v in required or len(incidence[v]) != 1:
            continue
        edge = next(iter(incidence[v]))
        connectors.remove(edge)
        for u in ends(edge):
            incidence[u].remove(edge)
            if u not in required and len(incidence[u]) == 1:
                leaves.append(u)
    adjacency = defaultdict(list)
    for edge, coefficient in sorted(net.items()):
        u, v = ends(edge)
        if coefficient < 0:
            u, v = v, u
        letter = (edge[1]+1)*(1 if coefficient > 0 else -1)
        adjacency[u].extend([(v, letter)]*abs(coefficient))
    for edge in sorted(connectors):
        u, v = ends(edge)
        adjacency[u].append((v, edge[1]+1))
        adjacency[v].append((u, -(edge[1]+1)))
    stack = [((0, 0), None)]
    reverse_word = []
    while stack:
        v, letter = stack[-1]
        if adjacency[v]:
            stack.append(adjacency[v].pop())
        else:
            stack.pop()
            if letter is not None:
                reverse_word.append(letter)
    result = tuple(reversed(reverse_word))
    assert not any(adjacency.values())
    assert len(result) == sum(abs(c) for c in net.values())+2*len(connectors)
    assert len(result) <= len(word)
    assert flow(2, result) == flow(2, word) and bridge(2, result)
    return result, tuple(sorted(connectors))
