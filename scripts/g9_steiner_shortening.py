#!/usr/bin/env python3
"""Connect bridge-flow components in their finite bounding rectangle.

Subset dynamic programming is exact for the retained finite unit-edge graph.
Growth certificates only need the resulting literal words, not optimality.
"""
from collections import defaultdict
from heapq import heappop, heappush

from g9_flow_shortening import ends
from g9_flow_unfolding import bridge, flow


def steiner(graph, terminals):
    """Return a minimum connecting edge set; graph entries are (neighbor, edge)."""
    terminals = tuple(terminals)
    size = len(graph)
    if not terminals or len(set(terminals)) != len(terminals):
        raise ValueError('Distinct nonempty terminal set required')
    if len(terminals) > 8 or size > 250:
        raise ValueError('Finite probe cap exceeded; no decision returned')
    inf = 10**9
    distances, pointers = {}, {}
    for mask in range(1, 1 << len(terminals)):
        dist = [inf]*size
        trace = [None]*size
        if mask & (mask-1) == 0:
            vertex = terminals[mask.bit_length()-1]
            dist[vertex], trace[vertex] = 0, ('terminal',)
        else:
            # Enumerate each unordered split once by its least terminal bit.
            sub = (mask-1) & mask
            while sub:
                other = mask ^ sub
                if other and sub & (mask & -mask):
                    left, right = distances[sub], distances[other]
                    for vertex in range(size):
                        value = left[vertex]+right[vertex]
                        if value < dist[vertex]:
                            dist[vertex], trace[vertex] = value, ('merge', sub, other)
                sub = (sub-1) & mask
        queue = [(d, v) for v, d in enumerate(dist) if d < inf]
        from heapq import heapify
        heapify(queue)
        while queue:
            value, vertex = heappop(queue)
            if value != dist[vertex]:
                continue
            for other, edge in graph[vertex]:
                if value+1 < dist[other]:
                    dist[other], trace[other] = value+1, ('edge', vertex, edge)
                    heappush(queue, (value+1, other))
        distances[mask], pointers[mask] = dist, trace
    mask = (1 << len(terminals))-1
    best = distances[mask][terminals[0]]
    if best == inf:
        raise ValueError('Disconnected terminal graph')
    edges, visited = set(), set()
    stack = [(mask, terminals[0])]
    while stack:
        mask, vertex = stack.pop()
        if (mask, vertex) in visited:
            continue
        visited.add((mask, vertex))
        step = pointers[mask][vertex]
        if step[0] == 'merge':
            stack.extend([(step[1], vertex), (step[2], vertex)])
        elif step[0] == 'edge':
            edges.add(step[2])
            stack.append((mask, step[1]))
        else:
            assert step[0] == 'terminal'
    assert len(edges) == best
    return edges, best


def shorten(word):
    word = tuple(word)
    assert bridge(2, word)
    net = {(v, axis): c for v, axis, c in flow(2, word)}
    required = {v for edge in net for v in ends(edge)}
    height = max(v[0] for v in required)
    xmin, xmax = min(v[1] for v in required), max(v[1] for v in required)
    vertices = {(0, 0)} | {(h, x) for h in range(1, height+1)
                          for x in range(xmin, xmax+1)}
    assert required <= vertices
    parent = {v: v for v in vertices}

    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(u, v):
        parent[root(u)] = root(v)

    for edge in net:
        union(*ends(edge))
    component_roots = sorted({root(v) for v in required})
    labels = {v: i for i, v in enumerate(sorted({root(v) for v in vertices}))}
    graph = [[] for _ in labels]
    # Choose one deterministic original edge for each contracted adjacency.
    adjacency = {}
    for vertex in sorted(vertices):
        for axis in (0, 1):
            target = list(vertex)
            target[axis] += 1
            target = tuple(target)
            if target not in vertices:
                continue
            # There are no height-zero connectors. Its sole edge is required.
            if vertex[0] == 0 and (vertex, axis) not in net:
                continue
            left, right = labels[root(vertex)], labels[root(target)]
            if left == right:
                continue
            key = tuple(sorted((left, right)))
            adjacency.setdefault(key, (vertex, axis))
    for (left, right), edge in sorted(adjacency.items()):
        assert edge not in net
        graph[left].append((right, edge))
        graph[right].append((left, edge))
    terminals = [labels[v] for v in component_roots]
    connectors, minimum = steiner(graph, terminals)
    for edge in connectors:
        union(*ends(edge))
    assert len({root(v) for v in required}) == 1
    directed = defaultdict(list)
    for edge, coefficient in sorted(net.items()):
        u, v = ends(edge)
        if coefficient < 0:
            u, v = v, u
        letter = (edge[1]+1)*(1 if coefficient > 0 else -1)
        directed[u].extend([(v, letter)]*abs(coefficient))
    for edge in sorted(connectors):
        u, v = ends(edge)
        directed[u].append((v, edge[1]+1))
        directed[v].append((u, -(edge[1]+1)))
    stack, reverse_word = [((0, 0), None)], []
    while stack:
        vertex, letter = stack[-1]
        if directed[vertex]:
            stack.append(directed[vertex].pop())
        else:
            stack.pop()
            if letter is not None:
                reverse_word.append(letter)
    result = tuple(reversed(reverse_word))
    assert not any(directed.values())
    norm = sum(abs(c) for c in net.values())
    assert len(result) == norm+2*minimum <= len(word)
    assert bridge(2, result) and flow(2, result) == flow(2, word)
    return result, tuple(sorted(connectors)), {
        'required_components': len(terminals), 'contracted_vertices': len(graph),
        'contracted_edges': len(adjacency), 'minimum_connectors': minimum,
        'flow_norm': norm, 'height': height, 'horizontal_bounds': [xmin, xmax]}
