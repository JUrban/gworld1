#!/usr/bin/env python3
"""Export existing interface certificates and rank-three polynomial controls."""
import argparse
import json
from pathlib import Path
from check_f34_f38_language_interface import gap, grammar
from f34_f38_language_interface import grammar_case


def export(name, g, problem, rank, certificate=None):
    c = grammar_case(g, problem, rank) if certificate is None else certificate
    alphabet = g['alphabet']
    selected = c['selected_components']
    return dict(name=name, rank=rank, problem=problem, certificate=c,
                alphabet_size=len(alphabet),
                terminal_letters=[g['terminal_letters'].get(a, 0) for a in alphabet],
                selected=selected,
                seeds=[[alphabet.index(a)+1 for a in g['seeds'][name]] for name in selected],
                morphisms=[[[alphabet.index(a)+1 for a in h[b]] for b in alphabet]
                           for h in g['morphisms']],
                with_span=certificate is not None)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    records = json.loads(Path(args.input).read_text())
    output = [export(r['name'], r['grammar'], r['system']['problem'], r['system']['rank'],
                     r['certificate']) for r in records]
    for problem in ('F34', 'F38'):
        names = ['X1', 'X2', 'X3', 'V'] if problem == 'F34' else ['X1', 'X2', 'X3', 'P', 'Q', 'U', 'V']
        g = grammar(3, names, [], [], [0])
        output.append(export('rank_three_'+problem, g, problem, 3))
    target = Path(args.output)
    if target.exists():
        raise ValueError('Refusing to overwrite export')
    target.write_text('GWLanguageCases:='+gap(output)+';\n')
    print('Exported %d language/polynomial cases' % len(output))
    print('PASS F34 F38 GAP export')


if __name__ == '__main__':
    main()
