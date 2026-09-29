#!/usr/bin/env python3
"""Exact finite exterior-ring identities; no enumeration of GL_n(R)."""
import argparse
import hashlib
import json
from pathlib import Path
import random


def add(a, b):
    c = a.copy()
    for w, v in b.items():
        c[w] = (c.get(w, 0) + v) % 3
        if not c[w]:
            del c[w]
    return c


def neg(a):
    return {w: -v % 3 for w, v in a.items()}


def mul(a, b):
    c = {}
    for w, v in a.items():
        for t, u in b.items():
            if len(w) + len(t) > 2 or set(w) & set(t):
                continue
            s = -1 if sum(i > j for i in w for j in t) % 2 else 1
            key = tuple(sorted(w + t))
            c = add(c, {key: s * v * u % 3})
    return c


ONE = {(): 1}


def ident(n):
    return [[ONE.copy() if i == j else {} for j in range(n)] for i in range(n)]


def mm(a, b):
    n = len(a)
    c = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] = add(c[i][j], mul(a[i][k], b[k][j]))
    return c


def trans(n, i, j, a):
    t = ident(n)
    t[i][j] = a.copy()
    return t


def h(u, ui):
    return [(0, 1, u), (1, 0, neg(ui)), (0, 1, u),
            (0, 1, neg(ONE)), (1, 0, ONE), (0, 1, neg(ONE))]


def inverse_factors(fs):
    return [(i, j, neg(a)) for i, j, a in reversed(fs)]


def product(n, fs):
    p = ident(n)
    for i, j, a in fs:
        p = mm(p, trans(n, i, j, a))
    return p


def rank(a):
    a = [r.copy() for r in a]
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        a[row] = [v * pow(a[row][col], -1, 3) % 3 for v in a[row]]
        for i in range(len(a)):
            if i != row:
                k = a[i][col]
                a[i] = [(v - k * w) % 3 for v, w in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def proj(q, z):
    return [[sum(qi[k] * z[k][l] * qj[l]
                 for k in range(len(z)) for l in range(len(z)) if z[k][l]) % 3
             for qj in q] for qi in q]


def wire(a):
    return [[v, [i + 1 for i in w]] for w, v in sorted(a.items())]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    if (out / 'checks.json').exists():
        raise SystemExit('Refusing to overwrite checks.')
    n = 3
    m = 2 * n * n + 1
    d = 2 * m
    fs = [(0, 1, ONE)]
    z = {}
    for i in range(m):
        a, b = {(2 * i,): 1}, {(2 * i + 1,): 1}
        u, v = add(ONE, a), add(ONE, b)
        ui, vi = add(ONE, neg(a)), add(ONE, neg(b))
        assert mul(u, ui) == mul(ui, u) == ONE
        assert mul(v, vi) == mul(vi, v) == ONE
        c = mul(mul(mul(u, v), ui), vi)
        zi = {(2 * i, 2 * i + 1): 2}
        assert c == add(ONE, zi)
        part = h(u, ui) + h(v, vi) + inverse_factors(h(mul(v, u), mul(ui, vi)))
        expected = ident(n)
        expected[0][0] = c
        assert product(n, part) == expected
        fs += part
        z = add(z, zi)
    target = ident(n)
    target[0][0] = add(ONE, z)
    target[0][1] = ONE
    assert product(n, fs) == target
    assert len(fs) == 343 and mul(z, z) == {}
    zm = [[0] * d for _ in range(d)]
    for (i, j), v in z.items():
        zm[i][j], zm[j][i] = v, -v % 3
    assert rank(zm) == d
    eye = [[int(i == j) for j in range(d)] for i in range(d)]
    # Sharp-bound control: kill the first vector in 18 symplectic pairs.
    keep = [2 * i + 1 for i in range(m - 1)] + [d - 2, d - 1]
    qs = [[eye[i].copy() for i in keep]]
    rng = random.Random(7292026)
    for _ in range(6):
        q = [[rng.randrange(3) for _ in range(d)] for _ in keep]
        while rank(q) != len(keep):
            q = [[rng.randrange(3) for _ in range(d)] for _ in keep]
        qs.append(q)
    qranks = []
    for q in qs:
        assert rank(q) == d - 2 * n * n
        r = rank(proj(q, zm))
        assert r >= 2
        qranks.append(r)
    assert qranks[0] == 2
    boundary = [eye[2 * i + 1] for i in range(m)]
    assert rank(boundary) == m and rank(proj(boundary, zm)) == 0
    checks = dict(n=n, field=3, pairs=m, degree_one_dimension=d,
                  ring_dimension=1 + d + d * (d - 1) // 2,
                  factor_count=len(fs), pair_identities=m, z_rank=rank(zm),
                  quotient_ranks=qranks, boundary_quotient_rank=0,
                  seed=7292026,
                  limitation='Finite identity and rank checks; universal exclusion is the written proof.')
    (out / 'checks.json').write_text(json.dumps(checks, indent=2) + '\n')
    fixture = [n, d, [[i+1,j+1,wire(a)] for i,j,a in fs],
               [[wire(a) for a in row] for row in target], zm, qs, qranks, boundary]
    (out / 'fixtures.g').write_text('MA7Fixture := ' + repr(fixture) + ';\n')
    (out / 'fixture-sha256.txt').write_text(hashlib.sha256((out/'fixtures.g').read_bytes()).hexdigest()+'\n')
    print('PASS MA7 exterior identities', json.dumps(checks))


if __name__ == '__main__':
    main()
