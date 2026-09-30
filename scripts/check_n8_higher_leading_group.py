#!/usr/bin/env python3
"""Target higher leading weights in the existing full N8 recursion."""
import argparse
import json
import time
from pathlib import Path

from check_n5_rational_lie import serial
from check_n8_general_solver import gap_native
from n8_general_solver import GeneralSolver
from n8_ia_orbits import wcomm, wpow
from n8_multigraded_magnus import Magnus


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['equal', 'exception'], required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    start = time.monotonic()
    c = wcomm([2], [1])
    u = wcomm([2], c)
    if args.mode == 'equal':
        d = wcomm([3], [1])
        v = wcomm([3], wcomm([2], d))
        fixtures = [('equal-weight-two-scaled', 3, 6, wpow(c, 2)+u, wpow(d, 3)+v)]
    else:
        d = wcomm(c, wcomm(c, u))
        fixtures = [('weight-two-exception', 2, 11, c+wpow(u, 2), d)]
    records = []

    def save():
        data = serial(records)
        (args.output/'checks.json').write_text(json.dumps(data, indent=2)+'\n')
        (args.output/'fixtures.g').write_text('N8GeneralFixtures := '+gap_native(data)+';\n')

    for label, rank, degree, x, y in fixtures:
        print('BEGIN', label, rank, degree, flush=True)
        m = Magnus(rank, degree)
        target_word = wcomm(x, y)
        target = m.expansion(target_word)
        row = dict(label=label, rank=rank, class_bound=degree, target_word=target_word,
                   planted_words=[x, y],
                   hall=[[h['weight'], list(h['pair']) if h['pair'] else []] for h in m.hall],
                   expected=True, events=[])
        records.append(row)

        def emit(event):
            row['events'].append(event)
            save()
            print(label, event['event'], event.get('weights', ''),
                  event.get('offset', ''), event.get('parameter_step', ''), flush=True)

        solver = GeneralSolver(m, target, emit=emit)
        answer = solver.solve()
        row['accepted'] = answer is not None
        if answer is not None:
            assert m.comm(*answer) == target
            row['factor_coordinates'] = solver.prefix(answer)
        save()
        assert row['accepted'], 'Planted commutator not recognized'
    summary = dict(seconds=time.monotonic()-start,
                   leading_types=[e['weights'] for r in records for e in r['events']
                                  if e['event'] == 'complete-leading-list'],
                   exceptional_offsets=[e['offset'] for r in records for e in r['events']
                                        if e['event'] == 'quadratic-exception'])
    (args.output/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary), flush=True)
    print('PASS N8 higher-leading group probe', args.mode, flush=True)


if __name__ == '__main__':
    main()
