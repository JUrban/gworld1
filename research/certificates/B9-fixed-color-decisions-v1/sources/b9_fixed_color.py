#!/usr/bin/env python3
"""Exact fixed-first-color fibre, with explicit incomplete resource outcomes.

Termination without resource caps imports Dehornoy's specialness algorithm.
The default caps prevent a failed computation from masquerading as a decision.
"""
from functools import lru_cache

from b9_special_braids import inverse, reduce_word, shelf, shift

WORD_CAP = 20000
IMAGE_CAP = 200000
REVERSAL_CAP = 100000


class ResourceLimit(RuntimeError):
    pass


def guarded(word):
    result = reduce_word(word)
    if len(result) > WORD_CAP:
        raise ResourceLimit('word length cap')
    return result


def rank(word):
    return max(2, 1+max(map(abs, word), default=0))


def exponent(word):
    return sum(1 if x > 0 else -1 for x in word)


@lru_cache(maxsize=512)
def action(word, n):
    images = [(i,) for i in range(1, n+1)]
    for a in word:
        i = abs(a)-1
        x, y = images[i:i+2]
        value = reduce_word(x+y+inverse(x)) if a > 0 else reduce_word(inverse(y)+x+y)
        if len(value) > IMAGE_CAP:
            raise ResourceLimit('faithful image length cap')
        images[i:i+2] = [value, x] if a > 0 else [y, value]
    return tuple(images)


def equal(a, b):
    a, b = tuple(a), tuple(b)
    if a == b:
        return True
    n = max(rank(a), rank(b))
    return action(a, n) == action(b, n)


def delete(word, n, keep):
    """Delete labelled input strands; the surviving endpoints are relabelled."""
    keep = set(keep)
    positions = list(range(1, n+1))
    result = []
    for a in word:
        i = abs(a)-1
        if positions[i] in keep and positions[i+1] in keep:
            j = sum(x in keep for x in positions[:i+1])
            result.append(j if a > 0 else -j)
        positions[i], positions[i+1] = positions[i+1], positions[i]
    return guarded(result), tuple(positions)


def unshift(word):
    n = rank(word)
    result, positions = delete(word, n, range(2, n+1))
    if positions[0] != 1 or not equal(word, shift(result)):
        return None
    return result


def compact(word):
    word = guarded(word)
    n = rank(word)
    while n > 2:
        smaller, positions = delete(word, n, range(1, n))
        if positions[-1] != n or not equal(word, smaller):
            break
        word = smaller
        n -= 1
    if equal(word, ()):
        return ()
    return word


def positive_fraction(word):
    original = tuple(word)
    word = list(guarded(word))
    steps = 0
    while True:
        index = next((i for i in range(len(word)-1) if word[i] < 0 < word[i+1]), None)
        if index is None:
            result = tuple(word)
            assert equal(result, original)
            return result, steps
        i, j = -word[index], word[index+1]
        replacement = [] if i == j else [j, -i] if abs(i-j) >= 2 else [j, i, -j, -i]
        word[index:index+2] = replacement
        word = list(guarded(word))
        steps += 1
        if steps > REVERSAL_CAP:
            raise ResourceLimit('word reversal step cap')


def special(word):
    word = tuple(word)
    n = rank(word)
    e = exponent(word)
    result = dict(word=word, ambient_rank=n, exponent=e)
    permutation = list(range(1, n+1))
    for a in word:
        i = abs(a)-1
        permutation[i], permutation[i+1] = permutation[i+1], permutation[i]
    nu = sum(permutation[j] == j for j in range(1, n))
    if e != nu:
        return dict(result, special=False, reason='exponent_permutation', permutation=permutation)
    if e == 0:
        return dict(result, special=equal(word, ()), reason='zero_exponent')
    if all(a > 0 for a in word):
        return dict(result, special=equal(word, tuple(range(n-1, 0, -1))), reason='positive_word')
    power = word
    for _ in range(n-e-1):
        power = compact(shelf(word, power))
    if not equal(power, tuple(range(n-1, 0, -1))):
        return dict(result, special=False, reason='right_power', power=power)
    fraction, steps = positive_fraction(word)
    colors = [() for _ in range(n)]
    trace = []
    for position, a in enumerate(fraction):
        i = abs(a)-1
        first, second = colors[i:i+2]
        if a > 0:
            next_pair = [compact(shelf(first, second)), first]
        else:
            test = guarded(inverse(second)+first+shift(second)+(-1,))
            divided = unshift(test)
            if divided is None:
                return dict(result, special=False, reason='failed_division', fraction=fraction,
                            reversal_steps=steps, trace=trace, failure_position=position,
                            failed_shift_word=test)
            next_pair = [second, compact(divided)]
        trace.append(dict(position=position, next_pair=next_pair))
        colors[i:i+2] = next_pair
    answer = all(equal(c, ()) for c in colors[1:])
    if answer:
        assert equal(colors[0], word)
    return dict(result, special=answer, reason='complete_coloring', fraction=fraction,
                reversal_steps=steps, trace=trace, final_colors=colors)


def fibre(word):
    word = tuple(word)
    n = max(3, rank(word))
    parameter, positions = delete(word, n, (1, 2, 3))
    difference = guarded(inverse(word)+parameter)
    c0 = unshift(difference)
    result = dict(word=word, ambient_rank=n, parameter=parameter,
                  difference=difference, input_endpoint_labels=positions)
    if c0 is None:
        return dict(result, status='complete', reason='no_parabolic_factorization', candidates=[], solutions=[])
    candidates = []
    solutions = []
    for k in range(-exponent(c0), n-1-exponent(c0)):
        c = guarded(c0+(1 if k >= 0 else -1,)*abs(k))
        classification = special(c)
        classification['power_index'] = k
        candidates.append(classification)
        if classification['special']:
            A = guarded(word+shift(c))
            expected = guarded(parameter+(2 if k >= 0 else -2,)*abs(k))
            assert equal(A, expected)
            solutions.append(dict(word=c, power_index=k, parameter_word=expected))
    if not equal(word, delete(word, n, (1, 2, 3))[0]):
        assert len(solutions) <= 1
    return dict(result, status='complete', reason='finite_specialness_tests', base_second=c0,
                candidates=candidates, solutions=solutions)
