#!/usr/bin/env python3
"""Exact lattice-flow bridge unfolding for free metabelian growth.

Words use signed 1-based basis indices. Positive edge (v,j) is v -> v+e_j.
Flows are immutable sorted tuples (base_vertex, zero_based_axis, coefficient).
"""
from collections import defaultdict
from math import isqrt


def inverse(word):
    return tuple(-a for a in word[::-1])


def path(rank,word):
    vertices=[(0,)*rank]
    for letter in word:
        p=list(vertices[-1]);p[abs(letter)-1]+=1 if letter>0 else -1
        vertices.append(tuple(p))
    return vertices


def flow(rank,word):
    p=[0]*rank;edges=defaultdict(int)
    for letter in word:
        j=abs(letter)-1
        if letter<0:p[j]-=1
        edges[(tuple(p),j)]+=1 if letter>0 else -1
        if letter>0:p[j]+=1
    return tuple(sorted((v,j,c) for (v,j),c in edges.items() if c))


def endpoint(rank,edges,start=None):
    if start is None:start=(0,)*rank
    boundary=defaultdict(int)
    for v,j,c in edges:
        q=list(v);q[j]+=1
        boundary[v]-=c;boundary[tuple(q)]+=c
    boundary[start]+=1
    support=[(v,c) for v,c in boundary.items() if c]
    assert len(support)==1 and support[0][1]==1, support
    return support[0][0]


def height_edge(v,j):
    return v[0]+int(j==0)


def strict_halfspace(rank,word):
    heights=[v[0] for v in path(rank,word)]
    return bool(word) and min(heights[1:])>0


def bridge(rank,word):
    heights=[v[0] for v in path(rank,word)]
    return bool(word) and min(heights[1:])>0 and max(heights)==heights[-1]


def unfold(rank,word):
    """Return a same-length bridge word and its strictly decreasing spans."""
    assert strict_halfspace(rank,word)
    heights=[v[0] for v in path(rank,word)]
    start=0;sign=1;spans=[];out=[];cuts=[]
    while start<len(word):
        span=max(sign*(h-heights[start]) for h in heights[start:])
        assert span>0
        end=max(i for i in range(start+1,len(heights))
                if sign*(heights[i]-heights[start])==span)
        piece=word[start:end]
        transformed=tuple(sign*a if abs(a)==1 else a for a in piece)
        assert bridge(rank,transformed)
        spans.append(span);cuts.append(end);out.extend(transformed)
        start=end;sign=-sign
    assert all(a>b for a,b in zip(spans,spans[1:]))
    assert sum(spans)<=len(word) and len(spans)*(len(spans)+1)//2<=len(word)
    assert len(out)==len(word) and bridge(rank,out)
    return tuple(out),tuple(spans),tuple(cuts)


def decode_unfolded(rank,edges,spans):
    """Recover the original flow from only the unfolded flow and span list."""
    assert spans and all(a>b>0 for a,b in zip(spans,spans[1:])) and spans[-1]>0
    old_start=(0,)*rank;new_start=(0,)*rank;low=0;sign=1
    original=defaultdict(int)
    for span in spans:
        high=low+span
        chunk=tuple((v,j,c) for v,j,c in edges if low<height_edge(v,j)<=high)
        new_end=endpoint(rank,chunk,new_start)
        assert new_end[0]==high
        for v,j,c in chunk:
            q=[old_start[i]+(sign if i==0 else 1)*(v[i]-new_start[i]) for i in range(rank)]
            if sign<0 and j==0:q[0]-=1;c=-c
            original[(tuple(q),j)]+=c
        delta=[new_end[i]-new_start[i] for i in range(rank)]
        delta[0]*=sign
        old_start=tuple(old_start[i]+delta[i] for i in range(rank))
        new_start=new_end;low=high;sign=-sign
    assert all(0<height_edge(v,j)<=low for v,j,c in edges)
    return tuple(sorted((v,j,c) for (v,j),c in original.items() if c))


def distinct_partition_prefix(n):
    """Number of finite strictly decreasing positive lists with sum <=n."""
    coeff=[1]+[0]*n
    for part in range(1,n+1):
        for total in range(n,part-1,-1):coeff[total]+=coeff[total-part]
    return sum(coeff)


def growth_interval_data(rank,n,ball_size):
    """Exact algebraic bounds; no floating-point value is a certificate."""
    assert rank>=1 and n>=1 and ball_size>=1
    p=distinct_partition_prefix(n+1)
    K=(n+1)**3*p*p
    return dict(rank=rank,n=n,ball_size=ball_size,partition_prefix=p,K=K,
                lower_power_numerator=ball_size,lower_power_denominator=K,
                lower_root_degree=n+2,lower_clamped_at=1,
                upper_power=ball_size,upper_root_degree=n)


def rational_code_bound(counts,denominator=1000000):
    """Largest p/denominator with sum counts[l]*(denominator/p)^l >=1.

    The positive root in the growth variable is a certified lower bound.
    Binary search uses integer arithmetic throughout.
    """
    counts={int(l):int(c) for l,c in counts.items() if c}
    assert counts and min(counts)>0
    degree=max(counts)
    def below(p):
        return sum(c*denominator**l*p**(degree-l) for l,c in counts.items())>=p**degree
    low=denominator;high=2*denominator
    assert below(low)
    while below(high):high*=2
    while high-low>1:
        mid=(low+high)//2
        if below(mid):low=mid
        else:high=mid
    return dict(numerator=low,denominator=denominator,counts=counts,
                root_upper_numerator=high,degree=degree)
