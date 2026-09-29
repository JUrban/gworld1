#!/usr/bin/env python3
"""Exact bounded probes of degree sorting; not an asymptotic F25 bound.

Type-II moves use Lee's (A,a) convention; cyclic words are identified only
by rotation, never inversion. All equal-length neighbours are exhausted.
"""
import argparse
from collections import deque
from itertools import product
import json
from pathlib import Path
import random

from f38_stabilizer_obstruction import apply, cyclic, check_auto, identity


def moves(rank):
    result = []
    for a in range(-rank, rank+1):
        if not a:
            continue
        others = [x for x in range(1, rank+1) if x != abs(a)]
        for bits in product((0, 1), repeat=2*len(others)):
            images = list(identity(rank)[0])
            inverse = list(images)
            support = []
            one_sided = []
            for j, x in enumerate(others):
                left, right = bits[2*j:2*j+2]
                images[x-1] = ((-a,) if left else ())+(x,)+((a,) if right else ())
                inverse[x-1] = ((a,) if left else ())+(x,)+((-a,) if right else ())
                if left:
                    support.append(-x)
                if right:
                    support.append(x)
                if left != right:
                    one_sided.append(x)
            images, inverse = tuple(images), tuple(inverse)
            check_auto((images, inverse))
            result.append(dict(multiplier=a, support=sorted(support),
                               degree=max(one_sided, default=0), images=images))
    return result


def frequency(w, rank):
    return tuple(sum(abs(a) == x for a in w) for x in range(1, rank+1))


def plateau(word, rank, ms, limit):
    root = cyclic(word)
    for m in ms:
        v = cyclic(apply(m['images'], root))
        if len(v) < len(root):
            return dict(status='not_minimal', shortening_move=m, shorter=v)
    vertices = [root]
    index = {root: 0}
    adjacency = []
    predecessors = [None]
    for i, w in enumerate(vertices):
        edges = []
        for j, m in enumerate(ms):
            v = cyclic(apply(m['images'], w))
            assert len(v) >= len(root), 'Whitehead minimum violated'
            if len(v) != len(root):
                continue
            assert frequency(v, rank) == frequency(root, rank)
            for b in m['support']:
                if -b not in m['support']:
                    assert frequency(w, rank)[abs(m['multiplier'])-1] >= frequency(w, rank)[abs(b)-1]
            if v not in index:
                if len(vertices) >= limit:
                    return dict(status='truncated', vertices_seen=len(vertices), limit=limit)
                index[v] = len(vertices)
                predecessors.append([i, j])
                vertices.append(v)
            if index[v] != i:
                edges.append([j, index[v]])
        adjacency.append(edges)
    return dict(status='complete', vertices=vertices, adjacency=adjacency,
                predecessors=predecessors, frequency=frequency(root, rank))


def sorted_reachable(start, graph, ms, max_degree):
    reachable = {start}
    for degree in range(max_degree+1):
        queue = deque(sorted(reachable))
        while queue:
            i = queue.popleft()
            for m, j in graph['adjacency'][i]:
                if ms[m]['degree'] == degree and j not in reachable:
                    reachable.add(j)
                    queue.append(j)
    return reachable


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--limit', type=int, default=12000)
    parser.add_argument('--samples', type=int, default=20)
    args = parser.parse_args()
    rank = 3
    ms = moves(rank)
    rng = random.Random(2026092901)
    seeds = [(1,1,2,2,3,3), (1,2,-1,-2,3,3),
             (1,1,2,2,3,3)*2, (1,1,2,2,2,3,3,3,3),
             (1,2,1,-2,3,1,3,-1)]
    for n in (3,4,5,6):
        for _ in range(args.samples):
            for _attempt in range(1000):
                raw = [x*rng.choice((-1,1)) for x in (1,2,3) for _ in range(n)]
                rng.shuffle(raw)
                if len(cyclic(raw)) == len(raw):
                    seeds.append(tuple(raw))
                    break
    records = []
    seen = set()
    for seed in seeds:
        if cyclic(seed) in seen:
            continue
        graph = plateau(seed, rank, ms, args.limit)
        record = dict(seed=seed, status=graph['status'])
        if graph['status'] != 'complete':
            record.update(graph)
            records.append(record)
            print(json.dumps(record), flush=True)
            continue
        seen.update(graph['vertices'])
        reach = sorted_reachable(0, graph, ms, rank)
        record.update(vertices=len(graph['vertices']), frequency=graph['frequency'],
                      sorted_from_root=len(reach))
        if len(reach) < len(graph['vertices']):
            # Every basepoint is tested for small plateaux. This is stronger
            # than selecting one ad hoc representative satisfying Hyp 1.3.
            record['tested_all_roots'] = len(graph['vertices']) <= 2000
            roots = range(len(graph['vertices'])) if record['tested_all_roots'] else [0]
            counts = [len(sorted_reachable(i, graph, ms, rank)) for i in roots]
            record['sorted_reach_counts'] = counts
            record['best_sorted_reach'] = max(counts)
            record['graph'] = graph
        records.append(record)
        print(json.dumps({k:v for k,v in record.items() if k not in ('graph','sorted_reach_counts')}), flush=True)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(dict(rank=rank, random_seed=2026092901,
                                    moves=ms, records=records), indent=2)+'\n')
    print('PASS F25 DEGREE PROBE: completed finite tests; no asymptotic claim', flush=True)


if __name__ == '__main__':
    main()
