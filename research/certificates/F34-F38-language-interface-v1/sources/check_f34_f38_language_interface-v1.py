#!/usr/bin/env python3
"""Finite and infinite-language controls for the F34/F38 interface.

No equation-to-EDT0L implementation or general problem decision is claimed.
The GAP export contains native original words and every monoid equation.
"""
import argparse
from datetime import datetime, timezone
import hashlib
from itertools import product
import json
from pathlib import Path

from f34_f38_language_interface import (
    check_assignment, compile_equations, complete_assignment, constraint_holds,
    monoid_accepts, monoid_inverse, monoid_product, monoid_value,
    test_grammar, verify_problem_witness,
)


def reduce_word(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def inv(word):
    return tuple(-a for a in reversed(word))


def image(word, xs):
    return reduce_word(a for token in word for a in
                       (xs[token-1] if token > 0 else inv(xs[-token-1])))


def cyclic(word):
    word = reduce_word(word)
    i = 0
    while len(word)-2*i > 1 and word[i] == -word[-i-1]:
        i += 1
    return word[:i], word[i:len(word)-i] if i else word


def rejected(fn):
    try:
        fn()
    except (ValueError, AssertionError, KeyError):
        return
    raise AssertionError('Expected rejection')


def gap(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'fail'
    if isinstance(value, (tuple, list)):
        return '['+','.join(gap(x) for x in value)+']'
    if isinstance(value, dict):
        return 'rec('+','.join(k+':='+gap(v) for k, v in value.items())+')'
    return json.dumps(value)


def grammar(rank, components, morphisms, edges, finals, order='application'):
    terminals = {('a%d' % abs(a) if a > 0 else 'A%d' % abs(a)): a
                 for a in range(-rank, rank+1) if a}
    seeds = {name: ['s_'+name] for name in components}
    alphabet = list(terminals)+[seed[0] for seed in seeds.values()]
    hs = [{a: list(change.get(a, [a])) for a in alphabet} for change in morphisms]
    return dict(alphabet=alphabet, terminal_letters=terminals, seeds=seeds,
                morphisms=hs, edges=edges, initials=[0], finals=finals, order=order)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    outdir = Path(args.output)
    outdir.mkdir(parents=True, exist_ok=False)
    short = [w for n in range(3) for w in product((-2, -1, 1, 2), repeat=n)
             if reduce_word(w) == w]
    tuples = []
    rejected_originals = 0
    systems = [compile_equations('F34', 2, word) for word in ([], [1], [1, -2, 1], [1, 2, -1, -2])]
    systems += [compile_equations('F38', 2, u, v) for u, v in
                [([1, 2, -1], [2]), ([1, 2, -1, -2], [2, 1, -2, -1]), ([], [1])]]
    for system in systems:
        for xs in product(short, repeat=2):
            original = {1: xs[0], 2: xs[1]}
            by_name = {'X1': xs[0], 'X2': xs[1]}
            if system['problem'] == 'F34':
                by_name['V'] = image(system['u'], xs)
            else:
                p, u = cyclic(image(system['u'], xs))
                q, v = cyclic(image(system['v'], xs))
                by_name.update(P=p, Q=q, U=u, V=v)
            original = {i: by_name[system['names'][i]] for i in system['projection']}
            if any(not constraint_holds(system['constraints'][i], w) for i, w in original.items()):
                rejected(lambda: complete_assignment(system, original))
                rejected_originals += 1
                continue
            values = complete_assignment(system, original)
            assert check_assignment(system, values)
            # An actual signed token error must fail the strict monoid equations.
            changed = dict(values)
            changed[system['projection'][-1]] += (1,)
            assert not check_assignment(system, changed)
            tuples.append(dict(rank=2, values=[values[i] for i in range(1, len(system['names']))],
                               equations=system['monoid_equations'],
                               constraints=[system['constraints'][i] for i in range(1, len(system['names']))],
                               groups=system['group_equations']))
    raw = [w for n in range(4) for w in product((-2, -1, 1, 2), repeat=n)]
    for x in raw:
        assert monoid_inverse(monoid_value(x)) == monoid_value(inv(x))
        for kind in ('positive', 'reduced', 'cyclic'):
            assert monoid_accepts(kind, monoid_value(x)) == constraint_holds(kind, x)
        for y in raw:
            assert monoid_product(monoid_value(x), monoid_value(y)) == monoid_value(x+y)
    records = []

    def check(name, g, system, vanishes, valid=False):
        answer = test_grammar(g, system['problem'], system['rank'])
        assert answer['vanishes'] == vanishes
        assert answer['complete_problem_decision'] is False
        semantics = verify_problem_witness(system, g, answer) if valid else None
        if not vanishes and not valid:
            rejected(lambda: verify_problem_witness(system, g, answer))
        records.append(dict(name=name, grammar=g, system=system, certificate=answer,
                            witness_semantics=semantics))

    # Full unary F34 relation for u=x: (X,V)=(a^m,a^m), m>=0.
    f34one = compile_equations('F34', 1, [1])
    loop = {'s_X1': ['s_X1', 'a1'], 's_V': ['s_V', 'a1']}
    erase = {'s_X1': [], 's_V': []}
    g = grammar(1, ['X1', 'V'], [loop, erase], [[0, 0, 0], [0, 1, 1]], [1])
    check('unary_positive_infinite', g, f34one, False, True)
    # A terminal omitted from the polynomial still controls tuple acceptance.
    g = grammar(1, ['X1', 'V'], [{'s_X1': ['a1']}], [[0, 1, 0]], [1])
    check('nonterminal_output_v', g, f34one, True)
    # Empty and identity-only grammars must never claim a full negative answer.
    g = grammar(1, ['X1', 'V'], [erase], [], [1])
    check('empty_control_language', g, f34one, True)
    g = grammar(1, ['X1', 'V'], [erase], [[0, 1, 0]], [1])
    check('incomplete_identity_only_language', g, f34one, True)
    # Counts alone do not validate the equation or positivity.
    g = grammar(1, ['X1', 'V'], [{'s_X1': ['a1'], 's_V': []}], [[0, 1, 0]], [1])
    check('incorrect_equation_tuple', g, f34one, False)
    g = grammar(1, ['X1', 'V'], [{'s_X1': ['A1'], 's_V': ['A1']}], [[0, 1, 0]], [1])
    check('nonpositive_tuple', g, f34one, False)
    # Noncommuting morphisms test the composition convention, not just counts.
    expand = {'s_X1': ['s_X1', 'a1'], 's_V': ['s_V', 'a1']}
    for order, zero in [('application', False), ('composition', True)]:
        g = grammar(1, ['X1', 'V'], [expand, erase], [[0, 1, 0], [1, 2, 1]], [2], order)
        check('order_'+order, g, f34one, zero, not zero)
    # Rank-two nonsurjective injective endomorphism; det = 6.
    f34two = compile_equations('F34', 2, [1, 2])
    vals = {'X1': ['a1', 'a1'], 'X2': ['a2']*3, 'V': ['a1', 'a1']+['a2']*3}
    g = grammar(2, vals, [{'s_'+k: w for k, w in vals.items()}], [[0, 1, 0]], [1])
    check('rank_two_positive_det_six', g, f34two, False, True)
    f38 = compile_equations('F38', 2, [1], [2])
    vals = {'X1': ['a1']*2, 'X2': ['a2']*3, 'P': [], 'Q': [],
            'U': ['a1']*2, 'V': ['a2']*3}
    g = grammar(2, vals, [{'s_'+k: w for k, w in vals.items()}], [[0, 1, 0]], [1])
    check('rank_two_distinction_det_six', g, f38, False, True)
    vals['X2'] = ['a1']*3
    vals['V'] = ['a1']*3
    g = grammar(2, vals, [{'s_'+k: w for k, w in vals.items()}], [[0, 1, 0]], [1])
    check('singular_gate_unequal_lengths', g, f38, True)
    vals = {'X1': ['a1'], 'X2': ['a2'], 'P': [], 'Q': [], 'U': ['a1'], 'V': ['a2']}
    g = grammar(2, vals, [{'s_'+k: w for k, w in vals.items()}], [[0, 1, 0]], [1])
    check('nonsingular_equal_lengths', g, f38, True)
    # Nonterminal conjugator must prevent acceptance even though P is not counted.
    vals['V'] = ['a2']*2
    g = grammar(2, vals, [{'s_'+k: w for k, w in vals.items() if k != 'P'}], [[0, 1, 0]], [1])
    check('nonterminal_conjugator', g, f38, True)
    rejected(lambda: compile_equations('F34', 0, []))
    rejected(lambda: compile_equations('F38', 2, [3], []))
    summary = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                   accepted_equation_tuples=len(tuples), rejected_originals=rejected_originals,
                   monoid_product_pairs=len(raw)**2, involutions=len(raw),
                   regular_constraint_checks=3*len(raw), language_cases=len(records),
                   group_witnesses=sum(r['witness_semantics'] is not None for r in records),
                   scope='Interface checks; recompression remains unimplemented')
    (outdir/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    (outdir/'cases.json').write_text(json.dumps(records, indent=2)+'\n')
    (outdir/'equation-tuples.json').write_text(json.dumps(tuples, indent=2)+'\n')
    (outdir/'equation-tuples.g').write_text('GWLanguageTuples:='+gap(tuples)+';\n')
    print(json.dumps(summary, indent=2))
    print('PASS F34 F38 language interface')


if __name__ == '__main__':
    main()
