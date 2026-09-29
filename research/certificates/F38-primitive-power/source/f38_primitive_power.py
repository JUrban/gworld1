#!/usr/bin/env python3
"""F38(c) classification when an input is a primitive power, rank >=3.

Returns unsupported outside that scope. A negative answer contains a
Nielsen growth formula and an actual transported automorphism witness.
"""
from f38_stabilizer_obstruction import (apply, cyclic, compose, identity,
    inverse_auto, whiteheads, check_auto)


def nielsen(rank, changed, multiplier, power=1):
    assert 1 <= changed <= rank and 1 <= multiplier <= rank and changed != multiplier
    images = list(identity(rank)[0])
    inverse = list(images)
    suffix = (multiplier if power >= 0 else -multiplier,)*abs(power)
    images[changed-1] = (changed,)+suffix
    inverse[changed-1] = (changed,)+tuple(-x for x in suffix)
    return tuple(images), tuple(inverse)


def nielsen_profile(word, changed, multiplier):
    w = cyclic(word)
    positions = [i for i,x in enumerate(w) if abs(x) != multiplier]
    if not positions:
        return dict(nonmultiplier=[], gaps=[], slopes=[], growth=0,
                    threshold=0, eventual_intercept=len(w), constant=len(w))
    w = w[positions[0]:]+w[:positions[0]]
    letters, gaps = [], []
    for x in w:
        if abs(x) != multiplier:
            letters.append(x)
            gaps.append(0)
        else:
            gaps[-1] += 1 if x>0 else -1
    slopes = [int(x==changed)-int(letters[(i+1)%len(letters)]==-changed)
              for i,x in enumerate(letters)]
    for i,x in enumerate(letters):
        if letters[(i+1)%len(letters)] == -x:
            assert slopes[i] == 0 and gaps[i] != 0
    return dict(nonmultiplier=letters, gaps=gaps, slopes=slopes,
                growth=sum(abs(s) for s in slopes),
                threshold=max(abs(k) for k in gaps),
                eventual_intercept=len(letters)+sum(k*s if s else abs(k) for k,s in zip(gaps,slopes)),
                constant=None)


def profile_length(profile, power):
    if profile['constant'] is not None:
        return profile['constant']
    return len(profile['nonmultiplier'])+sum(abs(k+power*s) for k,s in zip(profile['gaps'],profile['slopes']))


def witness_twists(rank):
    assert rank >= 3
    return [(2,3),(3,2),(2,1)]+[(j,2) for j in range(4,rank+1)]


def normalize_primitive_power(rank, word):
    w = cyclic(word)
    if not w:
        raise ValueError('Nonidentity input required')
    for length in range(1,len(w)+1):
        if len(w)%length == 0 and w[:length]*(len(w)//length) == w:
            root, exponent = w[:length], len(w)//length
            break
    mu = identity(rank)
    current = cyclic(root)
    if len(current)>1:
        moves = whiteheads(rank)
        while True:
            for move in moves:
                nxt = cyclic(apply(move[0],current))
                if len(nxt)<len(current):
                    current = nxt
                    mu = compose(move,mu)
                    break
            else:
                break
    if len(current) != 1:
        return None
    letter = current[0]
    images = list(identity(rank)[0])
    if abs(letter)==1:
        images[0] = (1 if letter>0 else -1,)
    else:
        images[0] = (abs(letter),)
        images[abs(letter)-1] = (1 if letter>0 else -1,)
    inverse = [None]*rank
    for i,(x,) in enumerate(images,1):
        inverse[abs(x)-1] = (i if x>0 else -i,)
    rename = tuple(images),tuple(inverse)
    check_auto(rename)
    mu = compose(rename,mu)
    assert cyclic(apply(mu[0],w)) == (1,)*exponent
    return dict(root=root, exponent=exponent, automorphism=mu)


def primitive_power_comparison(rank,u,v):
    if rank < 3:
        return dict(status='unsupported_rank')
    u,v = cyclic(u),cyclic(v)
    if not u or not v:
        raise ValueError('Nonidentity inputs required')
    normal = normalize_primitive_power(rank,u)
    swapped = False
    if normal is None:
        normal = normalize_primitive_power(rank,v)
        u,v = v,u
        swapped = True
    if normal is None:
        return dict(status='unsupported_no_primitive_power')
    mu = normal['automorphism']
    moved = cyclic(apply(mu[0],v))
    result = dict(rank=rank, fixed=u, moved=v, swapped=swapped,
                  normalization=normal, normalized_moved=moved)
    if all(abs(x)==1 for x in moved):
        result.update(status='bounded_same_primitive_cyclic_group',
                      fixed_exponent=normal['exponent'], moved_exponent=sum(moved),
                      length_ratio_numerator=len(moved),length_ratio_denominator=normal['exponent'])
        return result
    for changed,multiplier in witness_twists(rank):
        profile = nielsen_profile(moved,changed,multiplier)
        if profile['growth']:
            theta = compose(inverse_auto(mu),compose(nielsen(rank,changed,multiplier),mu))
            check_auto(theta)
            assert cyclic(apply(theta[0],u)) == u
            result.update(status='not_boundedly_equivalent', changed=changed,
                          multiplier=multiplier, profile=profile, witness=theta,
                          normalization_lipschitz=max(map(len,mu[0])))
            return result
    raise AssertionError('Primitive-power classification proof violated')
