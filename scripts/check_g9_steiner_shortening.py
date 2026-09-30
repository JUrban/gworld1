#!/usr/bin/env python3
"""Shorten the same 62003 central representatives by finite Steiner DP."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import itertools
import json
from pathlib import Path

from certify_g9_two_ended_completion import act, atom, coordinates
from g9_steiner_shortening import shorten, steiner


def controls():
    # All connected simple graphs on four vertices, every nonempty terminal set.
    checks = 0
    universe = list(itertools.combinations(range(4), 2))
    for bits in range(1 << len(universe)):
        edges = [e for i, e in enumerate(universe) if bits >> i & 1]
        graph = [[] for _ in range(4)]
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, i))
            graph[v].append((u, i))
        for terminals_mask in range(1, 16):
            terminals = [i for i in range(4) if terminals_mask >> i & 1]
            exact = None
            for length in range(len(edges)+1):
                for subset in itertools.combinations(range(len(edges)), length):
                    reached = {terminals[0]}
                    while True:
                        larger = reached | {u for i in subset for u in edges[i]
                                            if any(v in reached for v in edges[i])}
                        if larger == reached:
                            break
                        reached = larger
                    if set(terminals) <= reached:
                        exact = length
                        break
                if exact is not None:
                    break
            if exact is None:
                try:
                    steiner(graph, terminals)
                except ValueError as error:
                    assert 'Disconnected' in str(error)
                else:
                    raise AssertionError('Disconnected control accepted')
            else:
                selected, value = steiner(graph, terminals)
                assert value == exact == len(selected)
            checks += 1
    return checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    print('EXHAUSTIVE_TINY_GRAPH_CONTROLS', controls(), flush=True)
    paths = [Path('research/certificates/G9-two-ended-completion-v1/certificate.json'),
             Path('research/certificates/G9-bridge-atoms/certificate.json'),
             Path('research/certificates/G9-flow-shortening-probe-v1/certificate.json')]
    old, original, prior = [json.loads(p.read_text()) for p in paths]
    words = [tuple(w) for w in original['word_certificates']]
    previous = {(r['orbit_index'], r['x'], r['z']): r['shortened_cost']
                for r in prior['improved_representatives']}
    summary, component_counts, records = Counter(), Counter(), []
    for oi, orbit in enumerate(old['orbit_records']):
        xmin, xmax, zmin, zmax = orbit['rectangle']
        for x in range(xmin, xmax+1):
            for z in range(zmin, zmax+1):
                index = orbit['chosen_indices'][x-xmin][z-zmin]
                _, (old_x, old_z) = coordinates(words[index])
                word = act(words[index], x-old_x, z-old_z)
                assert len(word) == orbit['costs'][x-xmin][z-zmin]
                result, connectors, evidence = shorten(word)
                assert atom(result) and coordinates(result) == coordinates(word)
                old_best = previous.get((oi, x, z), len(word))
                assert len(result) <= old_best
                summary['central_words_checked'] += 1
                summary['shortened_from_original'] += len(result) < len(word)
                summary['improved_over_heuristic'] += len(result) < old_best
                summary['total_letters_saved_from_original'] += len(word)-len(result)
                summary['total_letters_saved_over_heuristic'] += old_best-len(result)
                summary['maximum_contracted_vertices'] = max(
                    summary['maximum_contracted_vertices'], evidence['contracted_vertices'])
                component_counts[evidence['required_components']] += 1
                if len(result) < len(word):
                    records.append(dict(orbit_index=oi, x=x, z=z,
                        original_input=index, original_cost=len(word),
                        previous_cost=old_best, shortened_cost=len(result),
                        word=result, connectors=connectors, steiner=evidence))
                if summary['central_words_checked'] % 10000 == 0:
                    print('CHECKED', summary['central_words_checked'],
                          'NEW_IMPROVEMENTS', summary['improved_over_heuristic'], flush=True)
    certificate = dict(created_utc=datetime.now(timezone.utc).isoformat(),
        sources=[dict(path=str(p), sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths],
        scope='Same central orbit representatives; literal flow witnesses, no new growth bound yet',
        tiny_graph_controls=960, summary=dict(summary),
        required_component_counts=dict(component_counts), improved_representatives=records)
    (out/'certificate.json').write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps({**certificate['summary'], 'component_counts': dict(component_counts)}, indent=2))
    print('PASS G9 finite Steiner shortening')


if __name__ == '__main__':
    main()
