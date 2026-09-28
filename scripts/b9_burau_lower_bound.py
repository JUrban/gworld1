#!/usr/bin/env python3
"""One bounded shelf step; distinct finite Burau images certify a lower bound.

Colliding images are NOT asserted to be equal braids. No faithfulness claim
is used. Every saved braid has a recursive special-braid witness.
"""
import argparse
import hashlib
import json
from pathlib import Path

from b9_special_braids import shelf

P = 1000003
T = 2


def burau(word, rank):
    m = [[int(i == j) for j in range(rank)] for i in range(rank)]
    tinv = pow(T, -1, P)
    for a in word:
        i = abs(a) - 1
        for row in m:
            x, y = row[i:i + 2]
            if a > 0:
                row[i:i + 2] = [((1 - T) * x + y) % P, T * x % P]
            else:
                row[i:i + 2] = [y * tinv % P, (x + (T - 1) * tinv * y) % P]
    return tuple(tuple(row) for row in m)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    source = Path(args.input)
    target = Path(args.output)
    if target.exists():
        raise SystemExit('Refusing to overwrite a certificate')
    previous = json.loads(source.read_text())
    records = [{k: v for k, v in r.items() if k != 'strands'}
               for r in previous['records']]
    height = max(r['height'] for r in records) + 1
    rank = height + 1
    ident = burau([], rank)
    for i in range(1, rank):
        assert burau([i, -i], rank) == ident
        assert burau([-i, i], rank) == ident
    for i in range(1, rank - 1):
        assert burau([i, i + 1, i], rank) == burau([i + 1, i, i + 1], rank)
    for i in range(1, rank):
        for j in range(i + 2, rank):
            assert burau([i, j], rank) == burau([j, i], rank)
    # The same finite representation already separates the previous records.
    known = {burau(r['word'], rank): j for j, r in enumerate(records)}
    assert len(known) == len(records)
    size = len(records)
    for i in range(size):
        for j in range(size):
            w = shelf(tuple(records[i]['word']), tuple(records[j]['word']))
            key = burau(w, rank)
            if key not in known:
                known[key] = len(records)
                records.append(dict(word=list(w), height=1 + max(
                    records[i]['height'], records[j]['height']), parents=[i, j]))
    output = dict(bound='term height <= '+str(height), ambient_rank=rank,
                  conclusion='At least this many special braids; no upper bound',
                  modulus=P, parameter=T, lower_bound=len(records),
                  input_path=str(source), input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  attempted_pairs=size * size, records=records)
    raw = (json.dumps(output, indent=2)+'\n').encode()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    print(json.dumps({k: v for k, v in output.items() if k != 'records'}))
    print('certificate_sha256', hashlib.sha256(raw).hexdigest())
    print('PASS finite Burau lower bound')


if __name__ == '__main__':
    main()
