#!/usr/bin/env python3
"""Exact controls for the F38(c) stabilizer obstruction, not a full solver."""
import json
from pathlib import Path

from f38_stabilizer_obstruction import (
    apply, check_auto, cyclic, finite_conjugacy_orbit, identity,
    mod3_matrix, necessary_condition,
)

OUT = Path('research/certificates/F38-stabilizer-obstruction')
OUT.mkdir(parents=True, exist_ok=True)
assert not (OUT/'checks-v1.json').exists(), 'Preserve earlier evidence'
records = []
fixtures = []


def save():
    (OUT/'checks-v1.json').write_text(json.dumps(records, indent=2)+'\n')
    (OUT/'fixtures-v1.g').write_text('F38StabilizerFixtures := '+json.dumps(fixtures)+';\n')


def check(rank, u, v, expected, label):
    result = necessary_condition(rank, u, v)
    assert result['status'] == expected, (label, result['status'])
    records.append(dict(label=label, rank=rank, u=u, v=v, result=result))
    for report in result['reports']:
        outcome = report['orbit_check']
        if outcome['finite']:
            fixtures.append([rank, list(report['fixed']), list(report['moved']),
                             'finite_orbit', report['generators'], outcome['orbit']])
        else:
            witness = outcome['witness']
            lengths = []
            w = tuple(report['moved'])
            for _ in range(5):
                lengths.append(len(cyclic(w)))
                w = apply(witness[0], w)
            fixtures.append([rank, list(report['fixed']), list(report['moved']),
                             'infinite_orbit_witness', witness, lengths])
    save()
    print(label, result['status'],
          [(r['graph']['vertices'], r['graph']['generators'],
            r['orbit_check']['matrix_states']) for r in result['reports']], flush=True)


yes = 'necessary_condition_passed_only'
no = 'not_boundedly_equivalent'
a, b = (1,), (2,)
boundary = (1, 1, 2, -1, -2)
comm = (1, 2, -1, -2)
check(2, a, b, no, 'different-primitives-rank2')
check(2, comm, a, no, 'commutator-versus-primitive-rank2')
check(2, a, boundary, yes, 'prior-Lee-rank2-bounded-pair')
# The same pair after a simultaneous automorphism, testing minimization.
images = ((1, 2, 2), (2,))
check(2, apply(images, a), apply(images, boundary), yes, 'Lee-pair-transformed')
check(3, a, boundary, no, 'Lee-pair-free-factor-boundary')
check(3, comm, (1, 3, -1, -3), no, 'different-commutators-rank3')
check(3, comm*2, comm*3, yes, 'same-cyclic-subgroup-rank3')
check(3, (1, 2), (1, 2)*3, yes, 'nonminimal-primitive-powers-rank3')

# These tests isolate the finite-orbit stage. A periodic class need not be
# fixed outside the level-three kernel. Inversion is even identity mod 2.
swap = (((2,), (1,)), ((2,), (1,)))
flip = (((-1,), (2,)), ((-1,), (2,)))
twist = (((1,), (2, 1, 1, 1)), ((1,), (2, -1, -1, -1)))
inner = (((1,), (-1, 2, 1)), ((1,), (1, 2, -1)))
for label, gens, word, expected in [
    ('finite-swap-orbit', [swap], a, True),
    ('finite-inversion-orbit-mod2-trap', [flip], a, True),
    ('level-three-nonperiodic-twist', [twist], b, False),
    ('inner-map-fixed-conjugacy', [inner], b, True),
]:
    for gen in gens:
        check_auto(gen)
    answer = finite_conjugacy_orbit(2, gens, word)
    assert answer['finite'] == expected
    if label.startswith('finite-'):
        assert len(answer['orbit']) == 2
    records.append(dict(label=label, rank=2, generators=gens, word=word, result=answer))
    if answer['finite']:
        fixtures.append([2, [], word, 'finite_orbit', gens, answer['orbit']])
    else:
        fixtures.append([2, [], word, 'infinite_orbit_witness', answer['witness'], []])
    save()
    print(label, answer['finite'], answer['matrix_states'], flush=True)
print('PASS F38 stabilizer obstruction: 8 pair cases; 4 orbit controls;',
      len(fixtures), 'GAP fixtures; no full bounded-equivalence solver')
