#!/usr/bin/env python3
"""Exact finite-language check and export of the existing B9 endpoint evidence."""
from collections import deque
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/certificates/B9-positive-parameters'
SOURCE = ROOT / 'research/certificates/B9-coloring-cosets/two-cones-v1.json.states.jsonl'


def transition(z, letter):
    z = list(z)
    i = letter - 1
    z[i:i + 2] = [False, z[i]]
    return tuple(z)


def nfa_step(states, letter):
    # NFA for 1* | 2 1* | 2* 1 2 1*, with initial epsilon closure {1,2,4}.
    edges = {(1, 1): 1, (2, 2): 3, (3, 1): 3,
             (4, 2): 4, (4, 1): 5, (5, 2): 6, (6, 1): 6}
    return frozenset(edges[s, letter] for s in states if (s, letter) in edges)


def main():
    OUT.mkdir(exist_ok=True)
    for name in ['automaton-v1.json', 'endpoints-v1.json', 'endpoints-v1.g']:
        if (OUT / name).exists():
            raise SystemExit('Refusing to overwrite ' + name)
    initial = ((True, True, True), frozenset({1, 2, 4}))
    queue = deque([initial])
    paths = {initial: []}
    records = []
    while queue:
        z, states = state = queue.popleft()
        assert z[2] == bool(states & {1, 3, 6})
        edges = []
        for letter in [1, 2]:
            nxt = (transition(z, letter), nfa_step(states, letter))
            if nxt not in paths:
                paths[nxt] = paths[state] + [letter]
                queue.append(nxt)
            edges.append({'letter': letter, 'zero_flags': nxt[0], 'nfa_states': sorted(nxt[1])})
        records.append({'zero_flags': z, 'nfa_states': sorted(states),
                        'representative': paths[state], 'accepting': z[2], 'edges': edges})
    # Omitting the third branch must fail on sigma1 sigma2.
    states = frozenset({1, 2})
    z = (True, True, True)
    for letter in [1, 2]:
        states, z = nfa_step(states, letter), transition(z, letter)
    assert z[2] and not (states & {1, 3, 6})
    assert not transition(transition((True, True, True), 2), 2)[2]
    endpoints = []
    for line_number, line in enumerate(SOURCE.read_text().splitlines(), 1):
        row = json.loads(line)
        if row['colors'][2] == []:
            endpoints.append({'source_line': line_number, 'path': row['path'], 'colors': row['colors']})
    assert len(endpoints) == 46
    (OUT / 'automaton-v1.json').write_text(json.dumps({
        'language': '1* | 2 1* | 2* 1 2 1*',
        'method': 'Exhaustive reachable product automaton, not a word-length cutoff',
        'states': records, 'negative_controls': ['omit third branch: witness 12', 'reject 22'],
    }, indent=2) + '\n')
    (OUT / 'endpoints-v1.json').write_text(json.dumps({
        'source': str(SOURCE.relative_to(ROOT)),
        'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'scope': 'Exactly the 46 saved third-color-unit endpoints; no search extension',
        'records': endpoints,
    }, indent=2) + '\n')
    fixtures = [[r['path'], r['colors'][0], r['colors'][1], r['source_line']] for r in endpoints]
    (OUT / 'endpoints-v1.g').write_text('B9EndpointRecords := ' + json.dumps(fixtures) + ';\n')
    print(f'Finite product automaton: {len(records)} states, {2 * len(records)} transitions')
    print('Exported 46 existing endpoints with source line numbers; two controls passed')
    print('PASS B9 positive-parameter language and endpoint export')


if __name__ == '__main__':
    main()
