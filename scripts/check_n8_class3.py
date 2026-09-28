#!/usr/bin/env python3
"""Deterministic proof-oriented checks; positive witnesses exported for GAP."""
import json
from pathlib import Path
import random
from collections import Counter
from n8_class3 import expansion, comm, wcomm, wpow, solve, lift_vector, lift_exterior

ROOT = Path(__file__).resolve().parents[1]
SEED = 9282608
rng = random.Random(SEED)
fixtures = []
counts = Counter()


def check(rank, word, expected, label):
    result = solve(word, rank)
    assert result['answer'] == expected, (rank, label, word, result)
    if expected:
        assert comm(expansion(result['x']), expansion(result['y'])) == expansion(word)
    counts[result['case']+(' yes' if expected else ' no')] += 1
    fixtures.append([rank, word, expected, result.get('x', []), result.get('y', [])])


for rank in range(1, 6):
    check(rank, [], True, 'identity')
    check(rank, [1], False, 'outside derived')

for rank in range(2, 6):
    for k in range(20):
        x = [rng.choice((-1, 1))*rng.randrange(1, rank+1) for _ in range(rng.randrange(1, 13))]
        y = [rng.choice((-1, 1))*rng.randrange(1, rank+1) for _ in range(rng.randrange(1, 13))]
        check(rank, wcomm(x, y), True, f'random positive {k}')
    for k in range(20):
        z = [rng.randrange(-3, 4) for _ in range(rank)]
        exterior = [[0]*rank for _ in range(rank)]
        for i in range(rank):
            for j in range(i+1, rank):
                exterior[i][j] = rng.randrange(-2, 3)
                exterior[j][i] = -exterior[i][j]
        check(rank, wcomm(lift_vector(z), lift_exterior(exterior)), True, f'central positive {k}')

# Akhavan-Malayeri--Rhemtulla, Glasgow Math. J. 40 (1998), Theorem 1.
check(2, wpow(wcomm([1], [2]), 2), False, 'known square obstruction')
# Wedge rank four already obstructs a single commutator in class two.
check(4, wcomm([1], [2])+wcomm([3], [4]), False, 'rank-four wedge')
# A central rank-three example, audited separately in the accompanying note.
central_negative = wcomm(wcomm([1], [2]), [3])+wcomm(wcomm([1], [3]), [2])
check(3, central_negative, False, 'central nonfactorable tensor')

out = ROOT/'research/certificates/N8-class3'
out.mkdir(parents=True, exist_ok=True)
(out/'fixtures.json').write_text(json.dumps({'seed': SEED, 'fixtures': fixtures}, indent=2)+'\n')
(out/'fixtures.g').write_text('N8Fixtures := '+json.dumps(fixtures)+';\n')
print(json.dumps({'seed': SEED, 'cases': len(fixtures), 'counts': dict(counts)}, sort_keys=True))
print('PASS N8 class-three exact checks')
