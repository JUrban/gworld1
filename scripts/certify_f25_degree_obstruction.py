#!/usr/bin/env python3
"""Extract a complete small obstruction to extending Lee's degree sorting."""
from itertools import permutations
import json
from pathlib import Path
from probe_f25_degree_order import sorted_reachable
from f38_stabilizer_obstruction import cyclic
from itertools import product

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'research/certificates/F25-degree-obstruction'


def main():
    probe = json.loads((ROOT/'research/certificates/F25-degree-probe/probe.json').read_text())
    chosen = next(r for r in probe['records'] if r.get('vertices') == 12 and len(r['seed']) == 12)
    graph, moves = chosen['graph'], probe['moves']
    checks = []
    for ordering in permutations((1, 2, 3)):
        position = {x: i+1 for i, x in enumerate(ordering)}
        reordered = []
        for m in moves:
            one_sided = [abs(x) for x in m['support'] if -x not in m['support']]
            reordered.append(dict(m, degree=max((position[x] for x in one_sided), default=0)))
        checks.append(dict(ordering=ordering, reach_sets=[sorted(sorted_reachable(i, graph, reordered, 3)) for i in range(12)]))
    assert all(len(r) < 12 for check in checks for r in check['reach_sets'])
    reachable = set(checks[0]['reach_sets'][0])
    target = min(set(range(12))-reachable)
    path = []
    at = target
    while at:
        parent, move = graph['predecessors'][at]
        path.append(move)
        at = parent
    path.reverse()
    adjacency = [{j for _, j in edges} for edges in graph['adjacency']]
    assert all(len(neighbours) == 2 for neighbours in adjacency)
    cycle = [0]
    previous, at = None, 0
    while True:
        nxt = min(adjacency[at]-({previous} if previous is not None else set()))
        if nxt == 0:
            break
        cycle.append(nxt)
        previous, at = at, nxt
    assert len(cycle) == 12 and len(set(cycle)) == 12
    cycle_degrees = []
    for i, j in zip(cycle, cycle[1:]+cycle[:1]):
        ds = {moves[m]['degree'] for m, target in graph['adjacency'][i] if target == j}
        assert len(ds) == 1
        cycle_degrees.append(next(iter(ds)))
    permuted_orbit = set()
    for perm in permutations((1,2,3)):
        for signs in product((-1,1), repeat=3):
            for word in graph['vertices']:
                image = tuple((1 if x>0 else -1)*signs[abs(x)-1]*perm[abs(x)-1] for x in word)
                permuted_orbit.add(cyclic(image))
    result = dict(rank=3, word=graph['vertices'][0],
                  word_convention='signed generators; least cyclic rotation, not inversion',
                  claim='No basepoint and no ordering of the basis reaches this whole type-II plateau using nondecreasing-degree moves.',
                  moves=moves, graph=graph, all_order_checks=checks,
                  cycle=cycle, cycle_degrees=cycle_degrees,
                  signed_permutation_orbit_size=len(permuted_orbit),
                  witness=dict(start=0, target=target, moves=path,
                               degrees=[moves[i]['degree'] for i in path]),
                  scope='Obstruction to dropping the unequal-frequency hypothesis; not a counterexample to F25 or to Lee under its stated hypotheses.')
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/'certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    gap = ['# Generated exact fixtures; scripts/check_f25_degree_obstruction_gap.g recomputes all edges.']
    gap.append('F25Vertices := '+str(graph['vertices'])+';')
    gap.append('F25Moves := '+str([[m['multiplier'], m['support'], m['images']] for m in moves])+';')
    gap.append('F25Edges := '+str(graph['adjacency'])+';')
    gap.append('F25Orders := '+str([c['ordering'] for c in checks]).replace('(', '[').replace(')', ']')+';')
    gap.append('F25ReachSets := '+str([c['reach_sets'] for c in checks])+';')
    (OUT/'fixtures.g').write_text('\n'.join(gap)+'\n')
    letters = {i:chr(96+i) for i in (1,2,3)}
    letters.update({-i:chr(64+i) for i in (1,2,3)})
    rows = ['Uppercase letters denote inverses. Canonical cyclic representatives.', '',
            '| Vertex | Word | Next vertex | Degree |', '|---|---|---|---|']
    for k,i in enumerate(cycle):
        rows.append(f"| {i} | {''.join(letters[x] for x in graph['vertices'][i])} | {cycle[(k+1)%12]} | {cycle_degrees[k]} |")
    rows.extend(['', f'Full signed-permutation closure: {len(permuted_orbit)} cyclic words.',
                 f'Witness path indices: {path}; images: '+str([moves[m]['images'] for m in path]),
                 f'Target vertex {target}: '+''.join(letters[x] for x in graph['vertices'][target])])
    (OUT/'graph-table.md').write_text('\n'.join(rows)+'\n')
    print(json.dumps(dict(word=result['word'], witness=result['witness'],
                         cycle=cycle, cycle_degrees=cycle_degrees,
                         signed_permutation_orbit_size=len(permuted_orbit),
                         reach_sizes=[[len(s) for s in c['reach_sets']] for c in checks])))
    print('PASS F25 DEGREE CERTIFICATE')


if __name__ == '__main__':
    main()
