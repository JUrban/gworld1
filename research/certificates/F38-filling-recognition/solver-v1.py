#!/usr/bin/env python3
"""Prior filling criterion as a positive branch of the F38(c) research tool.

Gupta--Kapovich: filling iff the outer conjugacy stabilizer is finite.
Kapovich--Lustig: two filling words have uniformly comparable tree lengths.
This does not decide every pair of non-filling words.
"""
from itertools import combinations

from f38_stabilizer_obstruction import (
    cyclic, finite_conjugacy_orbit, necessary_condition, stabilizer,
)


def outer_detection_words(rank):
    """Fixing these oriented conjugacy classes forces an automorphism inner."""
    assert rank >= 2
    return [(i,) for i in range(1, rank + 1)] + list(
        combinations(range(1, rank + 1), 2))


def finite_outer_group(rank, generators):
    """Decide finiteness in Out, allowing infinite inner representatives.

    Handel--Mosher aperiodicity makes every finite conjugacy orbit pointwise
    fixed by the level-three subgroup. That subgroup is trivial in Out iff
    it fixes all the detecting words. Each orbit decision terminates.
    """
    checks = []
    for word in outer_detection_words(rank):
        result = finite_conjugacy_orbit(rank, generators, word)
        checks.append(dict(word=word, result=result))
        if not result['finite']:
            return dict(finite=False, checks=checks, witness=result['witness'],
                        moved=word)
    return dict(finite=True, checks=checks)


def filling(rank, word):
    assert rank >= 2 and cyclic(word), 'Rank >=2 and nonidentity required'
    generators, graph = stabilizer(rank, word)
    result = finite_outer_group(rank, generators)
    return dict(filling=result['finite'], word=word, graph=graph,
                generators=generators, outer_group=result)


def bounded_comparison(rank, u, v):
    """Return a certified answer or explicitly leave the pair unresolved."""
    assert rank >= 2 and cyclic(u) and cyclic(v)
    obstruction = necessary_condition(rank, u, v)
    if obstruction['status'] == 'not_boundedly_equivalent':
        return obstruction
    first = obstruction['reports'][0]
    finiteness = finite_outer_group(rank, first['generators'])
    # The two stabilizers are commensurable after the necessary condition
    # passed; if the first is finite, then the second is finite too.
    status = ('boundedly_equivalent_prior_filling_case' if finiteness['finite']
              else 'unresolved_nonfilling_stabilizers_commensurable')
    return dict(status=status, obstruction=obstruction,
                first_outer_group=finiteness)
