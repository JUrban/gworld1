#!/usr/bin/env python3
"""F38(c) decision via the candidate theorem in problems/F38/bounded-proof.md.

Imports classical peak reduction and level-three aperiodicity through the
existing finite stabilizer procedure. Positive answers additionally depend
on the new written application of Sela's graded shortening theorem.
This implementation does not compute a comparison constant.
"""
from f38_stabilizer_obstruction import (
    cyclic, stabilizer, finite_conjugacy_orbit, necessary_condition,
)


def inputs(rank, u, v):
    if type(rank) is not int or rank < 1:
        raise ValueError('A positive integer ambient rank is required')
    u, v = tuple(u), tuple(v)
    if any(type(x) is not int or x == 0 or abs(x) > rank for x in u+v):
        raise ValueError('Words must use signed nonzero basis indices')
    u, v = cyclic(u), cyclic(v)
    if not u or not v:
        raise ValueError('Nonidentity inputs required; ratios otherwise undefined')
    return u, v


def one_sided_comparison(rank, u, v):
    """Decide existence of C with ||alpha(v)|| <= C ||alpha(u)||."""
    u, v = inputs(rank, u, v)
    if rank == 1:
        return dict(status='bounded_one_side', rank=rank,
                    exact_ratio=[len(v), len(u)])
    generators, graph = stabilizer(rank, u)
    orbit = finite_conjugacy_orbit(rank, generators, v)
    report = dict(fixed=u, moved=v, generators=generators,
                  graph=graph, orbit_check=orbit)
    return dict(status='bounded_one_side' if orbit['finite'] else 'unbounded_one_side',
                report=report, theorem='problems/F38/bounded-proof.md')


def bounded_equivalence(rank, u, v):
    """Decide bounded translation equivalence in the specified ambient rank."""
    u, v = inputs(rank, u, v)
    if rank == 1:
        return dict(status='boundedly_equivalent', rank=rank,
                    exact_ratio=[len(v), len(u)])
    answer = necessary_condition(rank, u, v)
    if answer['status'] == 'necessary_condition_passed_only':
        answer['status'] = 'boundedly_equivalent'
    answer['theorem'] = 'problems/F38/bounded-proof.md'
    return answer
