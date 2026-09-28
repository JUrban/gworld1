#!/usr/bin/env python3
"""Exact word/finite-field checks for the M0 candidate. Not a proof by sampling.

Fields use polynomial-basis integer encoding, least significant digit first.
Words are signed, one-based generator indices. Left Fox columns are evaluated
directly by a prefix scan. A second GAP program checks the exported witnesses.
"""
import itertools
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/certificates/M0'


class Field:
    def __init__(self, p, modulus):
        self.p, self.modulus = p, modulus
        self.d = len(modulus) - 1
        self.q = p ** self.d

    def digits(self, a):
        result = []
        for _ in range(self.d):
            result.append(a % self.p)
            a //= self.p
        return result

    def encode(self, digits):
        return sum((a % self.p) * self.p ** i for i, a in enumerate(digits))

    def add(self, a, b):
        return self.encode([x+y for x, y in zip(self.digits(a), self.digits(b))])

    def neg(self, a):
        return self.encode([-x for x in self.digits(a)])

    def mul(self, a, b):
        x, y = self.digits(a), self.digits(b)
        z = [0] * (2*self.d - 1)
        for i in range(self.d):
            for j in range(self.d):
                z[i+j] += x[i]*y[j]
        for k in range(len(z)-1, self.d-1, -1):
            c = z[k] % self.p
            for i in range(self.d):
                z[k-self.d+i] -= c*self.modulus[i]
        return self.encode(z[:self.d])

    def power(self, a, n):
        if n < 0:
            assert a
            return self.power(self.power(a, self.q-2), -n)
        b = 1
        while n:
            if n & 1:
                b = self.mul(b, a)
            a = self.mul(a, a)
            n //= 2
        return b

    def div(self, a, b):
        assert b
        return self.mul(a, self.power(b, -1))

    def primitive(self):
        return next(a for a in range(1, self.q)
                    if len({self.power(a, k) for k in range(self.q-1)}) == self.q-1)


def reduce_word(w):
    out = []
    for a in w:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return out


def inverse(w):
    return [-a for a in reversed(w)]


def substitute(w, images):
    return reduce_word(itertools.chain.from_iterable(
        images[a-1] if a > 0 else inverse(images[-a-1]) for a in w))


def compose(a, b):
    """a after b."""
    return [substitute(w, a) for w in b]


def identity(n):
    return [[i+1] for i in range(n)]


def fox(w, chi, field):
    col, prefix = [0]*len(chi), 1
    for a in w:
        i = abs(a)-1
        if a > 0:
            col[i] = field.add(col[i], prefix)
            prefix = field.mul(prefix, chi[i])
        else:
            prefix = field.div(prefix, chi[i])
            col[i] = field.add(col[i], field.neg(prefix))
    return prefix, col


def matrix(images, chi, field):
    return list(map(list, zip(*(fox(w, chi, field)[1] for w in images))))


def matvec(a, v, f):
    out = []
    for row in a:
        value = 0
        for x, y in zip(row, v):
            value = f.add(value, f.mul(x, y))
        out.append(value)
    return out


def kernel(a, f):
    a = [row[:] for row in a]
    n = len(a[0]); pivots = []; row = 0
    for col in range(n):
        k = next((k for k in range(row, len(a)) if a[k][col]), None)
        if k is None:
            continue
        a[row], a[k] = a[k], a[row]
        c = a[row][col]
        a[row] = [f.div(x, c) for x in a[row]]
        for k in range(len(a)):
            if k != row:
                c = a[k][col]
                a[k] = [f.add(x, f.neg(f.mul(c, y))) for x, y in zip(a[k], a[row])]
        pivots.append(col); row += 1
    if len(pivots) == n:
        return None
    free = next(i for i in range(n) if i not in pivots)
    v = [0]*n; v[free] = 1
    for k, col in enumerate(pivots):
        v[col] = f.neg(a[k][free])
    return v


def coefficient_polynomial(c, t, f):
    # Degree < d suffices because K=F_p(t), even if t is not the modulus root.
    for coefficients in itertools.product(range(f.p), repeat=f.d):
        value = 0
        for a in reversed(coefficients):
            value = f.add(f.mul(value, t), a)
        if value == c:
            return coefficients
    raise AssertionError('t does not generate the field')


def lift_transvection(row, col, c, n, t, f):
    assert row != col and row < n-1 and col < n-1
    extra = []
    for k, a in enumerate(coefficient_polynomial(c, t, f)):
        extra += [n]*k + [row+1]*a + [-n]*k
    extra = reduce_word(extra)
    forward, backward = identity(n), identity(n)
    forward[col] += extra
    backward[col] += inverse(extra)
    return forward, backward


def primitive_column(v, t, f):
    """Produce an actual free basis, its inverse, and the elementary certificate."""
    n = len(v)+1
    assert any(v)
    if len(v) == 1:
        # The application only needs a nonzero vector on this line, not scaling.
        return identity(n), identity(n), []
    current = v[:]; reduction = []

    def step(row, col, c):
        if c:
            current[row] = f.add(current[row], f.mul(c, current[col]))
            reduction.append((row, col, c))

    if not current[0]:
        step(0, next(i for i, x in enumerate(current) if x), 1)
    for i in range(1, len(v)):
        step(i, 0, f.neg(f.div(current[i], current[0])))
    a = current[0]
    step(1, 0, 1)
    step(0, 1, f.div(f.add(1, f.neg(a)), a))
    step(1, 0, f.neg(a))
    assert current == [1]+[0]*(len(v)-1)
    basis, undo, cert = identity(n), identity(n), []
    for row, col, c in reversed(reduction):
        c = f.neg(c)
        forward, backward = lift_transvection(row, col, c, n, t, f)
        basis = compose(forward, basis)
        undo = compose(undo, backward)
        cert.append([row, col, c])
    chi = [1]*(n-1)+[t]
    assert fox(basis[0], chi, f)[1] == v+[0]
    assert compose(basis, undo) == identity(n) == compose(undo, basis)
    return basis, undo, cert


def comm(a, b):
    # xyx^-1y^-1; recorded explicitly, independent of GAP's Comm convention.
    return a+b+inverse(a)+inverse(b)


def random_basis(n, rng, steps=3):
    basis, undo = identity(n), identity(n)
    for _ in range(steps):
        i, j = rng.sample(range(n), 2)
        forward, backward = identity(n), identity(n)
        if rng.randrange(3) == 0:
            forward[i], forward[j] = forward[j], forward[i]
            backward = [w[:] for w in forward]
        else:
            e = rng.choice([-1, 1])
            forward[i].append(e*(j+1)); backward[i].append(-e*(j+1))
        basis = compose(forward, basis)
        undo = compose(undo, backward)
    assert compose(basis, undo) == identity(n) == compose(undo, basis)
    return basis, undo


def main():
    rng = random.Random(9282617)
    fields = [Field(3, [0,1]), Field(5,[0,1]), Field(2,[1,1,1]),
              Field(2,[1,1,0,1]), Field(3,[1,0,1]), Field(2,[1,1,0,0,1])]
    records = []
    def save(kind, f, chi, basis, undo, **extra):
        rec = dict(kind=kind, p=f.p, modulus=f.modulus, chi=chi,
                   basis=basis, inverse=undo, fox=fox(basis[0], chi, f)[1], **extra)
        records.append(rec)
    # Every vector for small W; sampled vectors for the larger spaces.
    for f in fields:
        t = f.primitive()
        for n in [3,4]:
            if f.q <= 4 and n == 3:
                vectors = list(itertools.product(range(f.q), repeat=n-1))
            else:
                vectors = [tuple(rng.randrange(f.q) for _ in range(n-1)) for _ in range(8)]
            for v in vectors:
                if not any(v):
                    continue
                basis, undo, cert = primitive_column(list(v), t, f)
                save('orbit', f, [1]*(n-1)+[t], basis, undo, transvections=cert)
    # All generator images in the rank-three examples are individually primitive.
    examples = []
    for n in [2,3,4]:
        f = fields[0]; images = identity(n)
        if n == 2:
            images[0] += comm([1],[2])
        else:
            images[0] += comm([2],[n])
            images[1] += comm([1],[n])
        examples.append((f, 2, images))
    f = fields[2]; images = identity(3)
    images[0] += [3,3]+comm([2],[3])+[-3,-3]
    images[1] += comm([1],[3])
    examples.append((f, f.primitive(), images))
    for f, t, images in examples:
        n = len(images); chi = [1]*(n-1)+[t]
        jac = matrix(images, chi, f); v = kernel(jac, f)
        assert v is not None and not v[-1]
        basis, undo, cert = primitive_column(v[:-1], t, f)
        assert fox(substitute(basis[0], images), chi, f)[1] == [0]*n
        save('singular', f, chi, basis, undo, images=images, transvections=cert)
        for _ in range(4):
            beta, beta_inv = random_basis(n, rng)
            changed = compose(beta, compose(images, beta_inv))
            chi2 = [fox(w, chi, f)[0] for w in beta_inv]
            basis2 = compose(beta, basis)
            undo2 = compose(undo, beta_inv)
            assert kernel(matrix(changed, chi2, f), f) is not None
            assert fox(substitute(basis2[0], changed), chi2, f)[1] == [0]*n
            save('singular_changed_basis', f, chi2, basis2, undo2, images=changed)
    # Positive controls: actual free-group automorphisms have invertible Fox
    # matrices at every character, including non-normalized and trivial ones.
    for f in fields:
        for n in [2,3,4]:
            basis, undo = random_basis(n, rng, steps=5)
            for _ in range(3):
                chi = [rng.randrange(1, f.q) for _ in range(n)]
                assert kernel(matrix(basis, chi, f), f) is None
                save('automorphism_control', f, chi, basis, undo)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/'checks.json').write_text(json.dumps(dict(seed=9282617, records=records), indent=2)+'\n')
    # GAP reads JSON-free literal records. Field elements are decoded as
    # polynomials in a root of the recorded modulus, not as GAP integer indices.
    lines = ['M0Records := [']
    for rec in records:
        values = dict(p=rec['p'], modulus=rec['modulus'], chi=rec['chi'],
                      basis=rec['basis'], inverse=rec['inverse'], expected=rec['fox'],
                      images=rec.get('images', []), kind=rec['kind'])
        lines.append('rec('+','.join(k+':='+json.dumps(v) for k,v in values.items())+'),')
    lines[-1] = lines[-1].rstrip(','); lines.append('];')
    (OUT/'checks.g').write_text('\n'.join(lines)+'\n')
    counts = {k:sum(r['kind']==k for r in records) for k in sorted({r['kind'] for r in records})}
    print(json.dumps(dict(records=len(records), counts=counts,
        max_word_length=max(len(w) for r in records for w in r['basis']))))
    print('PASS M0 finite-field word checks')


if __name__ == '__main__':
    main()
