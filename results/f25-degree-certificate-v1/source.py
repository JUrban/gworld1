#!/usr/bin/env python3
"""Extract a complete small obstruction to extending Lee's degree sorting."""
from itertools import permutations
import json
from pathlib import Path
from probe_f25_degree_order import sorted_reachable

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
    result = dict(rank=3, word=graph['vertices'][0],
                  word_convention='signed generators; least cyclic rotation, not inversion',
                  claim='No basepoint and no ordering of the basis reaches this whole type-II plateau using nondecreasing-degree moves.',
                  moves=moves, graph=graph, all_order_checks=checks,
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
    print(json.dumps(dict(word=result['word'], witness=result['witness'],
                         reach_sizes=[[len(s) for s in c['reach_sets']] for c in checks])))
    print('PASS F25 DEGREE CERTIFICATE')


if __name__ == '__main__':
    main()
