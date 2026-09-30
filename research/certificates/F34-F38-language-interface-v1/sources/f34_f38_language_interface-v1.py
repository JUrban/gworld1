#!/usr/bin/env python3
"""Exact interfaces around the still-unimplemented full EDT0L construction.

This module is NOT a general F34/F38 solver. It compiles the equation input,
and tests a supplied controlled tuple grammar. It cannot certify that such a
grammar contains every solution of the equations.
"""
from collections import Counter
from itertools import permutations
from math import prod

from f38_polynomial_identity import (
    cancellation_triangle, cyclic_reduce, inverse, regular_summary,
    solve, substitute, summary_inverse, summary_product, word_reduce,
)


def compile_equations(problem, rank, u, v=None):
    """Compile F34(a)/F38(a) to monoid equations with involution.

    Signed integers in monoid equations name variables or their inverses.
    All variables range over reduced words on signed letters 1,...,rank.
    Output projection retains X_i and V (F34), or X_i,P,Q,U,V (F38).
    """
    if problem not in ('F34', 'F38') or type(rank) is not int or rank < 1:
        raise ValueError('Expected F34/F38 and positive integer rank')
    words = [u] if problem == 'F34' else [u, v]
    for word in words:
        if word is None or any(type(a) is not int or not 1 <= abs(a) <= rank
                               for a in word):
            raise ValueError('Invalid signed input word')
    names = [None]
    constraints = {}

    def fresh(name, constraint='reduced'):
        names.append(name)
        constraints[len(names)-1] = constraint
        return len(names)-1

    xs = [fresh('X%d' % i) for i in range(1, rank+1)]
    if problem == 'F34':
        output = fresh('V', 'positive')
        equations = [(list(u), output)]
    else:
        p, q = fresh('P'), fresh('Q')
        out_u, out_v = fresh('U', 'cyclic'), fresh('V', 'cyclic')
        equations = [([-p, *u, p], out_u), ([-q, *v, q], out_v)]
    projection = list(range(1, len(names)))
    products, monoid = [], []
    for expression, target in equations:
        if len(expression) <= 1:
            monoid.append([expression, [target]])
            continue
        prefix = expression[0]
        for index, atom in enumerate(expression[1:], 1):
            suffix = target if index == len(expression)-1 else fresh('prefix_%d' % len(products))
            s, t, r = [fresh('%s_%d' % (c, len(products))) for c in ('S', 'T', 'R')]
            products.append([prefix, atom, suffix, s, t, r])
            monoid.extend([[[prefix], [s, t]], [[atom], [-t, r]],
                           [[suffix], [s, r]]])
            prefix = suffix
    return dict(problem=problem, rank=rank, u=list(u), v=list(v) if v is not None else None,
                names=names, constraints=constraints, projection=projection,
                group_equations=equations, products=products, monoid_equations=monoid,
                missing_stage='Full constrained equation-to-EDT0L construction')


def evaluate_tokens(tokens, values):
    return tuple(letter for token in tokens for letter in
                 (values[token] if token > 0 else inverse(values[-token])))


def constraint_holds(kind, word):
    if word_reduce(word) != tuple(word):
        return False
    if kind == 'reduced':
        return True
    if kind == 'cyclic':
        return not word or word[0] != -word[-1]
    if kind == 'positive':
        return all(a > 0 for a in word)
    raise ValueError('Unknown regular constraint')


def check_assignment(system, values):
    if set(values) != set(range(1, len(system['names']))):
        return False
    rank = system['rank']
    if any(any(type(a) is not int or not 1 <= abs(a) <= rank for a in word)
           for word in values.values()):
        return False
    return (all(constraint_holds(kind, values[int(i)])
                for i, kind in system['constraints'].items()) and
            all(evaluate_tokens(left, values) == evaluate_tokens(right, values)
                for left, right in system['monoid_equations']))


def complete_assignment(system, original_values):
    """The unique maximal-cancellation lift of an original group solution.

    There may be other auxiliary presentations; existence in both directions
    is what the decision reduction requires. Reject a nonsolution.
    """
    if set(original_values) != set(system['projection']):
        raise ValueError('Supply exactly the original projected variables')
    values = {i: tuple(word) for i, word in original_values.items()}
    for left, right, target, s, t, r in system['products']:
        x, y = evaluate_tokens([left], values), evaluate_tokens([right], values)
        a, b, c = cancellation_triangle(x, y)
        product = a+c
        if target in values and values[target] != product:
            raise ValueError('Original assignment is not a group solution')
        values.update({target: product, s: a, t: b, r: c})
    if not check_assignment(system, values):
        raise ValueError('Original assignment fails equations or regular constraints')
    return values


def monoid_value(word):
    """Endpoints/zero times the semilattice of positive/negative occurrence.

    Product is concatenation, NOT free reduction. The full finite carrier has
    4*(2+(2r)^2) elements; unreachable carrier values cause no difficulty.
    """
    return regular_summary(word), (int(any(a > 0 for a in word)) |
                                  (2*int(any(a < 0 for a in word))))


def monoid_product(x, y):
    return summary_product(x[0], y[0]), x[1] | y[1]


def monoid_inverse(x):
    return summary_inverse(x[0]), ((x[1] & 1) << 1) | ((x[1] & 2) >> 1)


def monoid_accepts(kind, value):
    ends, signs = value
    if ends is None:
        return False
    return (kind == 'reduced' or
            (kind == 'cyclic' and (not ends or ends[0] != -ends[-1])) or
            (kind == 'positive' and not signs & 2))


def multiply_polynomials(p, q):
    out = Counter()
    for x, a in p.items():
        for y, b in q.items():
            out[tuple(i+j for i, j in zip(x, y))] += a*b
    return {e: c for e, c in out.items() if c}


def grammar_case(grammar, problem, rank):
    """Build separated component counts and det(B), or det(B)*(|U|-|V|).

    Alphabet symbols are strings. terminal_letters maps each terminal symbol
    to its signed free generator. Morphisms must specify EVERY symbol, with
    erasure represented by []. Edge order is converted to application order
    if the supplied automaton uses composition order.
    """
    alphabet = grammar['alphabet']
    terminals = grammar['terminal_letters']
    if (problem not in ('F34', 'F38') or type(rank) is not int or rank < 1 or
            not alphabet or len(set(alphabet)) != len(alphabet) or
            any(not isinstance(a, str) for a in alphabet) or
            not set(terminals) <= set(alphabet) or
            any(type(a) is not int for a in terminals.values()) or
            set(terminals.values()) != set(range(-rank, 0)) | set(range(1, rank+1)) or
            len(terminals) != 2*rank):
        raise ValueError('Invalid alphabet/terminal mapping')
    selected = ['X%d' % i for i in range(1, rank+1)]
    if problem == 'F38':
        selected += ['U', 'V']
    seeds = grammar['seeds']
    if not set(selected) <= set(seeds) or any(
            a not in alphabet for seed in seeds.values() for a in seed):
        raise ValueError('Invalid tuple seeds')
    # Even components absent from the polynomial must be terminal at acceptance.
    selected += [name for name in seeds if name not in selected]
    size = len(alphabet)
    n = size*len(selected)
    pos = {a: i for i, a in enumerate(alphabet)}
    matrices = []
    for h in grammar['morphisms']:
        if set(h) != set(alphabet) or any(a not in pos for w in h.values() for a in w):
            raise ValueError('Morphism must explicitly define every alphabet symbol')
        matrices.append([[h[alphabet[j % size]].count(alphabet[i % size])
                          if i//size == j//size else 0 for j in range(n)]
                         for i in range(n)])

    def linear(component, weights):
        result = {}
        for a, coefficient in weights.items():
            if coefficient:
                e = [0]*n
                e[selected.index(component)*size+pos[a]] = 1
                result[tuple(e)] = coefficient
        return result

    determinant = Counter()
    for perm in permutations(range(rank)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(rank) for j in range(i+1, rank))
        term = {(0,)*n: sign}
        for row, column in enumerate(perm, 1):
            entry = linear(selected[column], {a: (1 if signed == row else -1 if signed == -row else 0)
                                               for a, signed in terminals.items()})
            term = multiply_polynomials(term, entry)
        determinant.update(term)
    polynomial = {e: c for e, c in determinant.items() if c}
    if problem == 'F38':
        difference = linear('U', {a: 1 for a in terminals})
        difference.update(linear('V', {a: -1 for a in terminals}))
        polynomial = multiply_polynomials(polynomial, difference)
    order = grammar['order']
    if order not in ('application', 'composition'):
        raise ValueError('Explicit application/composition order required')
    reverse = order == 'composition'
    return dict(seed=[seeds[name].count(a) for name in selected for a in alphabet],
                matrices=matrices,
                edges=[[b, a, h] if reverse else [a, b, h] for a, b, h in grammar['edges']],
                initials=grammar['finals'] if reverse else grammar['initials'],
                finals=grammar['initials'] if reverse else grammar['finals'],
                terminal_indices=[i*size+pos[a] for i in range(len(selected)) for a in terminals],
                polynomial=[[c, list(e)] for e, c in polynomial.items()],
                selected_components=selected)


def test_grammar(grammar, problem, rank):
    """Exact polynomial test ON THIS GRAMMAR; not a full problem decision."""
    result = solve(grammar_case(grammar, problem, rank))
    result['complete_problem_decision'] = False
    result['scope'] = 'Supplied grammar only; full equation solution language not certified'
    if result['witness'] is not None:
        words = {name: tuple(seed) for name, seed in grammar['seeds'].items()}
        for edge in result['witness']['path']:
            h = grammar['morphisms'][grammar['edges'][edge][2]]
            words = {name: tuple(a for b in word for a in h[b]) for name, word in words.items()}
        result['tuple_witness'] = {name: list(word) for name, word in words.items()}
    return result


def verify_problem_witness(system, grammar, result):
    """Check an actual tuple from the grammar against the original problem.

    A successful F34 tuple witnesses potential positivity via the proved
    Stallings reduction. A successful F38 tuple distinguishes an injective
    endomorphism; KLSS Corollary 1.4 is still needed to pass to automorphisms.
    """
    if result.get('witness') is None:
        raise ValueError('No nonzero witness')
    terminal = grammar['terminal_letters']
    try:
        original = {i: tuple(terminal[a] for a in result['tuple_witness'][system['names'][i]])
                    for i in system['projection']}
    except KeyError as error:
        raise ValueError('Witness has missing or nonterminal original components') from error
    lifted = complete_assignment(system, original)
    xs = [original[i] for i in range(1, system['rank']+1)]
    # Evaluate determinant separately from the count polynomial.
    matrix = [[sum((a == i)-(a == -i) for a in word) for word in xs]
              for i in range(1, system['rank']+1)]
    d = sum((-1)**sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) *
            prod(matrix[i][p[i]] for i in range(len(p)))
            for p in permutations(range(system['rank'])))
    value = d
    if system['problem'] == 'F38':
        value *= (len(cyclic_reduce(substitute(system['u'], xs))) -
                  len(cyclic_reduce(substitute(system['v'], xs))))
    if not d or value != result['witness']['value'] or not value:
        raise ValueError('Nonzero polynomial witness does not match group semantics')
    return dict(determinant=d, polynomial_value=value, auxiliary_variables=len(lifted)-len(original),
                original_values={system['names'][i]: list(w) for i, w in original.items()})
