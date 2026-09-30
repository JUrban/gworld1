#!/usr/bin/env python3
"""Test every leading type after a central weighted-exception perturbation."""
import argparse
import hashlib
import json
from pathlib import Path

from check_n5_rational_lie import serial
from check_n8_general_solver import gap_native
from n8_general_solver import GeneralSolver
from n8_ia_orbits import wpow
from n8_multigraded_magnus import Magnus


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    source = Path('research/certificates/N8-higher-leading-exception-v1/checks.json')
    previous = json.loads(source.read_text())[0]
    quadratic = next(e for e in previous['events'] if e['event'] == 'quadratic-exception')
    assert quadratic['functional'] == [int(i == 113) for i in range(186)]
    assert quadratic['polynomial'] == [[0, 1], [-2, 1], [1, 1]]
    m = Magnus(2, 11)
    central = m.bydegree[11][113]
    target_word = previous['target_word']+wpow(central['word'], 2)
    target = m.expansion(target_word)
    assert target == m.mul(m.expansion(previous['target_word']), m.power(central['value'], 2))
    row = dict(label='weight-two-exception-negative', rank=2, class_bound=11,
               target_word=target_word, base_target_word=previous['target_word'],
               central_layer_index=113, central_power=2, expected=False,
               source=str(source), source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
               hall=[[h['weight'], list(h['pair']) if h['pair'] else []] for h in m.hall], events=[])

    def save():
        data = serial([row])
        (args.output/'checks.json').write_text(json.dumps(data, indent=2)+'\n')
        (args.output/'fixtures.g').write_text('N8GeneralFixtures := '+gap_native(data)+';\n')

    def emit(event):
        row['events'].append(event)
        save()
        print(event['event'], event.get('weights', ''), event.get('offset', ''),
              event.get('integer_roots', ''), flush=True)

    solver = GeneralSolver(m, target, emit=emit)
    answer = solver.solve()
    row['accepted'] = answer is not None
    if answer is not None:
        assert m.comm(*answer) == target
        row['factor_coordinates'] = solver.prefix(answer)
    save()
    assert answer is None, 'The proposed negative target has a verified witness'
    assert [e['weights'] for e in row['events'] if e['event'] == 'complete-leading-list'] == [
        [1, 8], [2, 7], [3, 6], [4, 5]]
    assert row['events'][-1]['event'] == 'all-leading-branches-rejected'
    print('PASS N8 higher-leading full negative decision', flush=True)


if __name__ == '__main__':
    main()
