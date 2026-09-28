#!/usr/bin/env python3
"""Terminating M0 witness construction by an explicit Kronecker substitution.

No finite-field search cutoff. This is a mathematical termination statement,
not a practical time/memory guarantee; run under scripts/run_recorded.py.
Uses the earlier exact word/Fox primitives. GAP checks final certificates.
"""
import argparse
import json
from math import isqrt

from sympy import Matrix, Poly, symbols

from m0_witness import (
    abelianization, certificate, integer_primitive_lift, laurent_determinant,
    normalize_abelianization,
)
from check_m0_finite_fields import (
    Field, compose, fox, identity, inverse, kernel, matrix, reduce_word,
)


def prime_by_trial(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def smallest_prime_divisor(n):
    n = abs(n)
    assert n != 1
    if n == 0:
        return 2
    for d in range(2, isqrt(n)+1):
        if n % d == 0:
            return d
    return n


def singular_character(delta):
    """A nonunit Laurent polynomial of augmentation one has this torus zero."""
    assert len(delta) >= 2 and sum(delta.values()) == 1
    n = len(next(iter(delta)))
    spreads = [max(e[i] for e in delta)-min(e[i] for e in delta)
               for i in range(n)]
    base = max(2, 1+max(spreads))
    weights = [base**i for i in range(n)]
    exponents = {e: sum(a*b for a, b in zip(e, weights)) for e in delta}
    assert len(set(exponents.values())) == len(delta)
    shift = min(exponents.values())
    coefficients = {exponents[e]-shift: c for e, c in delta.items()}
    degree = max(coefficients)
    endpoint_product = coefficients[0]*coefficients[degree]
    p = 2
    while not prime_by_trial(p) or endpoint_product % p == 0:
        p += 1
    z = symbols('z')
    g = Poly.from_dict({(e,): c for e, c in coefficients.items()}, z, modulus=p)
    assert g.degree() == degree and g.eval(0) != 0 and g.eval(1) == 1
    factors = g.factor_list()[1]
    h = min((a.monic() for a, _ in factors),
            key=lambda a: (a.degree(), tuple(int(c) % p for c in a.all_coeffs())))
    assert h.degree() > 0 and h.is_irreducible and g.rem(h).is_zero
    modulus = [int(h.nth(i)) % p for i in range(h.degree()+1)]
    f = Field(p, modulus)
    # t is the residue class of z, including the degree-one model.
    t = p if f.d > 1 else (-modulus[0]) % p
    assert t not in (0, 1)
    chi = [f.power(t, w) for w in weights]
    value = 0
    for exponent, coefficient in delta.items():
        value = f.add(value, f.mul(coefficient % p,
                                  f.power(t, sum(a*b for a, b in zip(exponent, weights)))))
    assert value == 0
    # alpha(x_i)=x_(i+1) x_1^(-weight_(i+1)), alpha(x_n)=x_1.
    alpha = [[i+1]+[-1]*weights[i] for i in range(1, n)]+[[1]]
    undo = [[n]]+[[i]+[n]*weights[i] for i in range(1, n)]
    assert compose(alpha, undo) == identity(n) == compose(undo, alpha)
    assert [fox(w, chi, f)[0] for w in alpha] == [1]*(n-1)+[t]
    data = dict(base=base, weights=weights, shift=shift,
                polynomial=[[e, c] for e, c in sorted(coefficients.items())],
                degree=degree, prime=p, factor=modulus,
                field_order_bound=p**degree)
    return f, chi, alpha, undo, t, data


def primitive_column_at_root(v, t, f):
    """Lift elementary matrices using direct polynomial-basis coefficients."""
    n = len(v)+1
    assert any(v)
    if n == 2:
        return identity(n), identity(n), []
    current, steps = v[:], []

    def step(row, col, c):
        if c:
            current[row] = f.add(current[row], f.mul(c, current[col]))
            steps.append((row, col, c))

    if not current[0]:
        step(0, next(i for i, c in enumerate(current) if c), 1)
    for i in range(1, len(v)):
        step(i, 0, f.neg(f.div(current[i], current[0])))
    a = current[0]
    step(1, 0, 1)
    step(0, 1, f.div(f.add(1, f.neg(a)), a))
    step(1, 0, f.neg(a))
    assert current == [1]+[0]*(len(v)-1)
    basis, undo, transvections = identity(n), identity(n), []
    for row, col, c in reversed(steps):
        c = f.neg(c)
        tail = []
        for k, coefficient in enumerate(f.digits(c)):
            tail += [n]*k+[row+1]*coefficient+[-n]*k
        tail = reduce_word(tail)
        forward, backward = identity(n), identity(n)
        forward[col] += tail
        backward[col] += inverse(tail)
        basis = compose(forward, basis)
        undo = compose(undo, backward)
        transvections.append([row, col, c])
    assert fox(basis[0], [1]*(n-1)+[t], f)[1] == v+[0]
    assert compose(basis, undo) == identity(n) == compose(undo, basis)
    return basis, undo, transvections


def witness(images):
    n = len(images)
    assert n > 0 and all(a and abs(a) <= n for w in images for a in w)
    images = [reduce_word(w) for w in images]
    b = abelianization(images)
    det_b = int(Matrix(b).det())
    if abs(det_b) != 1:
        p = smallest_prime_divisor(det_b)
        assert prime_by_trial(p)
        f = Field(p, [0, 1])
        v = kernel([[a % p for a in row] for row in b], f)
        basis, undo = integer_primitive_lift(v, f)
        return certificate(images, f, [1]*n, basis, undo,
                           route='abelianization_complete', determinant_abelianization=det_b)
    beta, beta_inverse = normalize_abelianization(images)
    ia = compose(beta, images)
    delta = laurent_determinant(ia)
    assert sum(delta.values()) == 1
    encoded = [[list(e), c] for e, c in sorted(delta.items())]
    if len(delta) == 1:
        return dict(status='metabelian_automorphism', determinant=encoded,
                    normalization=beta, normalization_inverse=beta_inverse,
                    criterion='Bachmuth square Fox Jacobian criterion')
    f, chi, alpha, alpha_inverse, t, data = singular_character(delta)
    changed = compose(alpha_inverse, compose(ia, alpha))
    v = kernel(matrix(changed, [1]*(n-1)+[t], f), f)
    assert v is not None and v[-1] == 0
    theta, theta_inverse, transvections = primitive_column_at_root(v[:-1], t, f)
    basis = compose(alpha, theta)
    undo = compose(theta_inverse, alpha_inverse)
    original_chi = [fox(w, chi, f)[0] for w in beta]
    return certificate(images, f, original_chi, basis, undo,
                       route='singular_Fox_Kronecker', determinant=encoded,
                       normalization=beta, normalization_inverse=beta_inverse,
                       search_character=chi, character_basis=alpha,
                       character_basis_inverse=alpha_inverse, normalized_t=t,
                       transvections=transvections, kronecker=data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='JSON array of signed generator-image words')
    args = parser.parse_args()
    with open(args.input) as stream:
        print(json.dumps(witness(json.load(stream)), indent=2))
