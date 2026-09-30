#!/usr/bin/env python3
"""Exact membership among the first colors of four known B9 parameter rays.

This is not a test for specialness, nor an exhaustion of special B4 braids.
The exponent formulas give at most eight comparisons for any input braid.
"""
from functools import lru_cache
from b9_special_braids import artin, shelf

BASE_PAIRS = (((), ()), ((), (1,)), ((1,), (1,)), ((1, 1, -2), ()))
BASE_PARAMETERS = ((), (2,), (1, 2), (1, 1, -2))


def exponent(word):
    if any(type(a) is not int or a == 0 for a in word):
        raise ValueError('Braid letters must be nonzero signed integers')
    return sum(1 if a > 0 else -1 for a in word)


def candidate_indices(p):
    """All (zero-based ray, step) whose first color has exponent p."""
    if type(p) is not int:
        raise ValueError('Integer exponent required')
    result = []
    for ray, (a, c) in enumerate(BASE_PAIRS):
        first, second = exponent(a), exponent(c)
        if p >= first:
            result.append((ray, 2*(p-first)))
        if p >= second+1:
            result.append((ray, 2*(p-second-1)+1))
    return sorted(result)


@lru_cache(maxsize=None)
def ray_pair(ray, step):
    if type(ray) is not int or not 0 <= ray < 4 or type(step) is not int or step < 0:
        raise ValueError('Invalid ray or step')
    a, c = BASE_PAIRS[ray]
    for _ in range(step):
        a, c = shelf(a, c), a
    return a, c


def matching_rays(word):
    word = tuple(word)
    candidates = candidate_indices(exponent(word))
    pairs = [(ray, step, ray_pair(ray, step)) for ray, step in candidates]
    rank = 1+max((abs(a) for a in word), default=0)
    rank = max(rank, 1+max((abs(a) for _, _, pair in pairs for w in pair for a in w), default=0))
    actual = artin(word, rank)
    return [(ray, step) for ray, step, pair in pairs if artin(pair[0], rank) == actual]
