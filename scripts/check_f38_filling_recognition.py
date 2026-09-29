#!/usr/bin/env python3
"""Bounded exact controls; export free-group certificates for GAP replay."""
from collections import Counter
import json
from pathlib import Path
import random

from f38_filling_recognition import bounded_comparison, filling, finite_outer_group
from f38_stabilizer_obstruction import apply, check_auto, cyclic, identity

OUT = Path('research/certificates/F38-filling-recognition')
OUT.mkdir(parents=True, exist_ok=True)
assert not (OUT/'checks-v1.json').exists(), 'Preserve earlier evidence'
records = []
fixtures = []


def save():
    (OUT/'checks-v1.json').write_text(json.dumps(records, indent=2)+'\n')
    (OUT/'fixtures-v1.g').write_text(
        'F38StabilizerFixtures := '+json.dumps(fixtures)+';\n')


def export(rank, fixed, generators, result):
    for check in result['checks']:
        word, answer = check['word'], check['result']
        if answer['finite']:
            fixtures.append([rank, fixed, word, 'finite_orbit',
                             generators, answer['orbit']])
        else:
            fixtures.append([rank, fixed, word, 'infinite_orbit_witness',
                             answer['witness'], []])


def balanced_word(rank, seed):
    """Euler circuit containing each reduced directed bigram exactly once."""
    letters = list(range(1, rank+1)) + list(range(-rank, 0))
    rng = random.Random(seed)
    graph = {a: [b for b in letters if b != -a] for a in letters}
    for values in graph.values():
        rng.shuffle(values)
    stack, circuit = [1], []
    while stack:
        if graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        else:
            circuit.append(stack.pop())
    word = tuple(reversed(circuit))[:-1]
    bigrams = Counter(zip(word, word[1:]+word[:1]))
    assert bigrams == Counter({(a, b): 1 for a in letters for b in letters if b != -a})
    assert len(cyclic(word)) == 2*rank*(2*rank-1)
    return word


# Group controls separate finite Out from finite Aut, and require pair words.
swap = (((2,), (1,)), ((2,), (1,)))
flip = (((-1,), (2,)), ((-1,), (2,)))
inner = (((1,), (-1, 2, 1)), ((1,), (1, 2, -1)))
twist = (((1,), (2, 1, 1, 1)), ((1,), (2, -1, -1, -1)))
partial = (((1,), (1, 2, -1), (3,)), ((1,), (-1, 2, 1), (3,)))
for label, rank, generators, expected in [
    ('empty-group', 2, [], True),
    ('finite-swap', 2, [swap], True),
    ('finite-inversion-mod2-trap', 2, [flip], True),
    ('infinite-inner-representatives', 2, [inner], True),
    ('level-three-nielsen', 2, [twist], False),
    ('basis-classes-insufficient', 3, [partial], False),
]:
    for gen in generators:
        check_auto(gen)
    result = finite_outer_group(rank, generators)
    assert result['finite'] == expected, label
    if label == 'basis-classes-insufficient':
        assert all(c['result']['finite'] for c in result['checks'][:3])
        assert len(result['moved']) == 2
    records.append(dict(label=label, rank=rank, generators=generators, result=result))
    export(rank, [], generators, result)
    save()
    print(label, result['finite'], flush=True)


u, v = balanced_word(3, 0), balanced_word(3, 1)
small = balanced_word(2, 0)
for label, rank, word, expected in [
    ('balanced-rank3-seed0', 3, u, True),
    ('balanced-rank3-seed1', 3, v, True),
    ('proper-power-filling', 3, u*2, True),
    ('balanced-rank2-seed0', 2, small, True),
    ('primitive-rank3', 3, (1,), False),
    ('commutator-rank2', 2, (1, 2, -1, -2), False),
]:
    result = filling(rank, word)
    assert result['filling'] == expected, label
    records.append(dict(label=label, rank=rank, result=result))
    export(rank, word, result['generators'], result['outer_group'])
    save()
    print(label, result['filling'], result['graph'], flush=True)


for label, rank, left, right, expected in [
    ('two-filling-rank3', 3, u, v, 'boundedly_equivalent_prior_filling_case'),
    ('filling-versus-primitive', 3, u, (1,), 'not_boundedly_equivalent'),
    ('prior-Lee-rank2', 2, (1,), (1, 1, 2, -1, -2),
     'unresolved_nonfilling_stabilizers_commensurable'),
    ('Lee-free-factor-boundary-rank3', 3, (1,), (1, 1, 2, -1, -2),
     'not_boundedly_equivalent'),
]:
    result = bounded_comparison(rank, left, right)
    assert result['status'] == expected, (label, result['status'])
    obstruction = result.get('obstruction', result)
    for report in obstruction['reports']:
        export(rank, report['fixed'], report['generators'], dict(checks=[
            dict(word=report['moved'], result=report['orbit_check'])]))
    if 'first_outer_group' in result:
        export(rank, left, obstruction['reports'][0]['generators'],
               result['first_outer_group'])
    records.append(dict(label=label, rank=rank, u=left, v=right, result=result))
    save()
    print(label, result['status'], flush=True)

print('PASS F38 filling recognition: 6 group controls; 6 word controls; '
      '4 pair controls;', len(fixtures), 'GAP fixtures; prior positive scope only')
