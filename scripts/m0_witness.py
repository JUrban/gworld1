#!/usr/bin/env python3
"""Construct a finite Fox certificate for a non-automorphism of M_n.

Input: signed-letter free words representing images of a finite free basis.
The search bound is explicit: exhausting it returns inconclusive, never yes.
The determinant criterion used for yes is Bachmuth's metabelian theorem.
Word and field primitives are shared with the earlier M0 checks; GAP is the
independent certificate verifier. No finite search is a proof of M0.
"""
import itertools
import argparse
import json

from sympy import Matrix, Poly, symbols, primerange

from check_m0_finite_fields import (
    Field, compose, fox, identity, inverse, kernel, matrix,
    primitive_column, reduce_word, substitute,
)


def abelianization(images):
    n = len(images)
    return [[sum((a == i+1)-(a == -i-1) for a in w)
             for w in images] for i in range(n)]


def shear(n, row, col, coefficient):
    """Integral matrix I+c E_(row,col), lifted to a Nielsen move."""
    assert row != col
    forward, backward = identity(n), identity(n)
    tail = [row+1 if coefficient >= 0 else -row-1]*abs(coefficient)
    forward[col] += tail
    backward[col] += inverse(tail)
    return forward, backward


def normalize_abelianization(images):
    """Return beta, beta^-1 with beta o images IA; require unimodular input."""
    a = abelianization(images)
    n = len(a)
    assert abs(int(Matrix(a).det())) == 1
    basis, undo = identity(n), identity(n)

    def apply(forward, backward):
        nonlocal basis, undo, a
        e = abelianization(forward)
        a = [[sum(e[i][k]*a[k][j] for k in range(n))
              for j in range(n)] for i in range(n)]
        basis = compose(forward, basis)
        undo = compose(undo, backward)

    def swap(i, j):
        s = identity(n)
        s[i], s[j] = s[j], s[i]
        apply(s, s)

    for k in range(n):
        if not a[k][k]:
            swap(k, next(i for i in range(k+1, n) if a[i][k]))
        for i in range(k+1, n):
            while a[i][k]:
                q = a[i][k] // a[k][k]
                apply(*shear(n, i, k, -q))
                if a[i][k]:
                    swap(i, k)
        assert abs(a[k][k]) == 1
        if a[k][k] == -1:
            s = identity(n)
            s[k] = [-k-1]
            apply(s, s)
        for i in range(k):
            apply(*shear(n, i, k, -a[i][k]))
    assert a == [[int(i == j) for j in range(n)] for i in range(n)]
    assert compose(basis, undo) == identity(n) == compose(undo, basis)
    return basis, undo


def normalize_character(chi, field):
    """Nielsen basis alpha with chi(alpha(x_i))=(1,...,1,t)."""
    n = len(chi)
    s = field.primitive()
    logs = {field.power(s, i): i for i in range(field.q-1)}
    exponents = [logs[a] for a in chi]
    assert any(exponents)
    basis, undo = identity(n), identity(n)

    def apply(forward, backward):
        nonlocal basis, undo, exponents
        e = abelianization(forward)
        exponents = [sum(exponents[i]*e[i][j] for i in range(n))
                     for j in range(n)]
        basis = compose(basis, forward)
        undo = compose(backward, undo)

    def swap(i, j):
        s = identity(n)
        s[i], s[j] = s[j], s[i]
        apply(s, s)

    for i in range(n-1):
        if not exponents[-1] and exponents[i]:
            swap(i, n-1)
        while exponents[i]:
            q = exponents[i] // exponents[-1]
            apply(*shear(n, n-1, i, -q))
            if exponents[i]:
                swap(i, n-1)
    t = field.power(s, exponents[-1])
    assert t != 1
    assert [fox(w, chi, field)[0] for w in basis] == [1]*(n-1)+[t]
    assert compose(basis, undo) == identity(n) == compose(undo, basis)
    return basis, undo, t


def integer_primitive_lift(v, field):
    """Lift a nonzero prime-field vector by elementary integral matrices."""
    n = len(v)
    assert field.d == 1 and any(v)
    if n == 1:
        return identity(n), identity(n)
    current, steps = v[:], []

    def step(row, col, c):
        if c:
            current[row] = field.add(current[row], field.mul(c, current[col]))
            steps.append((row, col, c))

    if not current[0]:
        step(0, next(i for i, x in enumerate(current) if x), 1)
    for i in range(1, n):
        step(i, 0, field.neg(field.div(current[i], current[0])))
    a = current[0]
    step(1, 0, 1)
    step(0, 1, field.div(field.add(1, field.neg(a)), a))
    step(1, 0, field.neg(a))
    assert current == [1]+[0]*(n-1)
    basis, undo = identity(n), identity(n)
    for row, col, c in reversed(steps):
        forward, backward = shear(n, row, col, field.neg(c))
        basis = compose(forward, basis)
        undo = compose(undo, backward)
    assert fox(basis[0], [1]*n, field)[1] == v
    assert compose(basis, undo) == identity(n) == compose(undo, basis)
    return basis, undo


def poly_add(a, b, scalar=1):
    out = a.copy()
    for k, v in b.items():
        out[k] = out.get(k, 0)+scalar*v
        if not out[k]:
            del out[k]
    return out


def poly_mul(a, b):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            k = tuple(i+j for i, j in zip(u, v))
            out[k] = out.get(k, 0)+x*y
    return {k: v for k, v in out.items() if v}


def laurent_determinant(images):
    """Exact integer Laurent polynomial, with exponent tuples as keys."""
    n = len(images)
    columns = []
    for word in images:
        prefix, column = [0]*n, [{} for _ in range(n)]
        for a in word:
            i = abs(a)-1
            if a < 0:
                prefix[i] -= 1
            column[i] = poly_add(column[i], {tuple(prefix): 1}, 1 if a > 0 else -1)
            if a > 0:
                prefix[i] += 1
        columns.append(column)
    determinant = {}
    for perm in itertools.permutations(range(n)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = {(0,)*n: sign}
        for col, row in enumerate(perm):
            term = poly_mul(term, columns[col][row])
        determinant = poly_add(determinant, term)
    return determinant


def finite_fields(max_size):
    """One irreducible polynomial presentation of each field up to max_size."""
    sizes = []
    for p in primerange(2, max_size+1):
        d, q = 1, int(p)
        while q <= max_size:
            sizes.append((q, int(p), d))
            d += 1
            q *= int(p)
    z = symbols('z')
    for q, p, d in sorted(sizes):
        if d == 1:
            yield Field(p, [0, 1])
            continue
        for coefficients in itertools.product(range(p), repeat=d):
            if not coefficients[0]:
                continue
            poly = Poly(z**d+sum(c*z**i for i, c in enumerate(coefficients)), z, modulus=p)
            if poly.is_irreducible:
                yield Field(p, list(coefficients)+[1])
                break
        else:
            raise AssertionError('No irreducible polynomial found')


def certificate(images, field, chi, basis, undo, **extra):
    n = len(images)
    assert compose(basis, undo) == identity(n) == compose(undo, basis)
    image_word = substitute(basis[0], images)
    assert fox(image_word, chi, field)[1] == [0]*n
    assert any(fox(basis[0], chi, field)[1])
    return dict(status='nonautomorphism_certificate', p=field.p,
                modulus=field.modulus, chi=chi, basis=basis, inverse=undo,
                images=images, image_word=image_word,
                fox=fox(basis[0], chi, field)[1], **extra)


def witness(images, max_field_size=16):
    n = len(images)
    assert n > 0 and all(a and abs(a) <= n for w in images for a in w)
    images = [reduce_word(w) for w in images]
    b = abelianization(images)
    det_b = int(Matrix(b).det())
    if abs(det_b) != 1:
        # Only a bounded prime search is performed in this implementation.
        for p in primerange(2, max_field_size+1):
            p = int(p)
            if det_b % p:
                continue
            f = Field(p, [0, 1])
            v = kernel([[a % p for a in row] for row in b], f)
            basis, undo = integer_primitive_lift(v, f)
            return certificate(images, f, [1]*n, basis, undo,
                               route='abelianization', determinant_abelianization=det_b)
        return dict(status='inconclusive_bound', stage='prime_divisor', bound=max_field_size)

    beta, beta_inverse = normalize_abelianization(images)
    ia_images = compose(beta, images)
    delta = laurent_determinant(ia_images)
    assert sum(delta.values()) == 1
    encoded_delta = [[list(k), v] for k, v in sorted(delta.items())]
    if len(delta) == 1 and abs(next(iter(delta.values()))) == 1:
        return dict(status='metabelian_automorphism', determinant=encoded_delta,
                    normalization=beta, normalization_inverse=beta_inverse,
                    criterion='Bachmuth square Fox Jacobian criterion')

    characters_tested = 0
    for f in finite_fields(max_field_size):
        for ch in itertools.product(range(1, f.q), repeat=n):
            chi = list(ch)
            characters_tested += 1
            if kernel(matrix(ia_images, chi, f), f) is None:
                continue
            alpha, alpha_inverse, t = normalize_character(chi, f)
            changed = compose(alpha_inverse, compose(ia_images, alpha))
            normalized_chi = [1]*(n-1)+[t]
            v = kernel(matrix(changed, normalized_chi, f), f)
            assert v is not None and v[-1] == 0
            theta, theta_inverse, transvections = primitive_column(v[:-1], t, f)
            basis = compose(alpha, theta)
            undo = compose(theta_inverse, alpha_inverse)
            assert fox(substitute(basis[0], ia_images), chi, f)[1] == [0]*n
            # beta o phi has zero Fox column at chi. The invertible beta
            # Jacobian gives the original certificate at chi o beta.
            original_chi = [fox(w, chi, f)[0] for w in beta]
            return certificate(
                images, f, original_chi, basis, undo, route='singular_Fox',
                determinant_abelianization=det_b, determinant=encoded_delta,
                normalization=beta, normalization_inverse=beta_inverse,
                search_character=chi, character_basis=alpha,
                character_basis_inverse=alpha_inverse, normalized_t=t,
                transvections=transvections, characters_tested=characters_tested)
    return dict(status='inconclusive_bound', stage='finite_fields', bound=max_field_size,
                determinant=encoded_delta, characters_tested=characters_tested)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='JSON file containing the array of generator-image words')
    parser.add_argument('--max-field-size', type=int, default=16)
    args = parser.parse_args()
    if args.max_field_size < 2:
        parser.error('The field-size bound must be at least two.')
    with open(args.input) as stream:
        images = json.load(stream)
    print(json.dumps(witness(images, args.max_field_size), indent=2))
