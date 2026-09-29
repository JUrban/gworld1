#!/usr/bin/env python3
"""Independent integer-lattice replay of the saved finite-cover transitions.

GAP supplies the finite quotient tables. Hall words, lifted cycles and Hermite
forms are constructed again here; no GAP relation matrices are reused.
"""
import argparse
import hashlib
import json
from pathlib import Path

from sympy import Matrix, zeros
from sympy.matrices.normalforms import hermite_normal_form

ROOT = Path(__file__).resolve().parents[1]


def inverse(w):
    return tuple(-s for s in w[::-1])


def comm(u, v):
    return inverse(u) + inverse(v) + u + v


def hall_words(c):
    entries = [(1, None, (1,)), (1, None, (2,))]
    for weight in range(2, c + 2):
        size = len(entries)
        for i in range(size):
            for j in range(i):
                u, v = entries[i], entries[j]
                if u[0] + v[0] == weight and (u[1] is None or u[1][1] <= j):
                    entries.append((weight, (i, j), comm(u[2], v[2])))
    expected = {2: 1, 3: 2, 4: 3, 5: 6, 6: 9, 7: 18}
    for weight in range(2, c + 2):
        assert sum(h[0] == weight for h in entries) == expected[weight]
    return ([h[2] for h in entries if h[0] == c],
            [h[2] for h in entries if h[0] == c + 1])


def transitions_check(trans):
    n = len(trans[0])
    assert len(trans) == 4 and all(sorted(row) == list(range(n)) for row in trans)
    for i in range(2):
        assert all(trans[i + 2][trans[i][v]] == v for v in range(n))
    seen, queue = {0}, [0]
    for v in queue:
        for step in trans:
            if step[v] not in seen:
                seen.add(step[v])
                queue.append(step[v])
    assert len(seen) == n


def cycle(trans, word, start):
    n = len(trans[0])
    row = [0] * (2 * n)
    v = start
    for letter in word:
        j = abs(letter) - 1
        if letter > 0:
            row[2 * v + j] += 1
            v = trans[j][v]
        else:
            v = trans[j + 2][v]
            row[2 * v + j] -= 1
    assert v == start, 'Relator or target is not a closed lifted path'
    # Independent boundary check, including loops and parallel edges.
    boundary = [0] * n
    for s, coefficient in enumerate(row):
        v, j = divmod(s, 2)
        boundary[v] -= coefficient
        boundary[trans[j][v]] += coefficient
    assert not any(boundary)
    return row


def lattice_check(trans, relators, targets):
    transitions_check(trans)
    n = len(trans[0])
    columns = [cycle(trans, w, v) for w in relators for v in range(n)]
    matrix = Matrix(columns).T if columns else zeros(2 * n, 0)
    lattice = hermite_normal_form(matrix)
    survivors = []
    for i, word in enumerate(targets, 1):
        vector = Matrix(cycle(trans, word, 0))
        if hermite_normal_form(lattice.row_join(vector)) != lattice:
            survivors.append(i)
    return lattice.cols, n + 1 - lattice.cols, survivors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('inputs', nargs='+', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists(), 'Preserve earlier evidence'
    trans = [[1, 0], [0, 1], [1, 0], [0, 1]]
    word = comm((2,), (1,))
    assert lattice_check(trans, [], [word]) == (0, 3, [1])
    assert lattice_check(trans, [word], [word]) == (1, 2, [])
    assert lattice_check(trans, [word + word], [word]) == (1, 2, [1])
    records = []
    for path in args.inputs:
        source = hashlib.sha256(path.read_bytes()).hexdigest()
        for entry in json.loads(path.read_text()):
            trans = [[v - 1 for v in row] for row in entry['transitions']]
            relators, targets = hall_words(entry['weight'])
            rank, betti, surviving = lattice_check(trans, relators, targets)
            assert (rank, betti, surviving) == (
                entry['relation_rank'], entry['betti'], entry['surviving_targets'])
            record = {key: entry[key] for key in (
                'order', 'small_group_id', 'weight', 'relation_rank', 'betti',
                'surviving_targets')}
            record.update(source=str(path), source_sha256=source)
            records.append(record)
            print('VERIFIED', entry['order'], entry['small_group_id'], entry['weight'],
                  'betti', betti, 'survivors', surviving, flush=True)
    args.output.write_text(json.dumps({'controls': 3, 'records': records}, indent=2) + '\n')
    print('PASS F20 independent cover homology:', len(records), 'covers; 3 controls')


if __name__ == '__main__':
    main()
