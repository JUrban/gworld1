#!/usr/bin/env python3
"""Finite exact checks of the uniform iterated-adjoint obstruction lead.

Letters are the free generators T_j=delta^j T; words are tuples of indices.
This checks Lie identities and rational ranks, not the full group algorithm.
"""
import json
from pathlib import Path
from flint import fmpz_mat

def add(a,b,scale=1):
    result=dict(a)
    for word,n in b.items():
        result[word]=result.get(word,0)+scale*n
        if not result[word]:del result[word]
    return result
def mul(a,b):
    result={}
    for u,n in a.items():
        for v,k in b.items():result[u+v]=result.get(u+v,0)+n*k
    return {w:n for w,n in result.items() if n}
def bracket(a,b):return add(mul(a,b),mul(b,a),-1)
def jet(j):return {(j,):1}
def delta(a):
    result={}
    for word,n in a.items():
        for i in range(len(word)):
            changed=word[:i]+(word[i]+1,)+word[i+1:]
            result[changed]=result.get(changed,0)+n
    return {w:n for w,n in result.items() if n}
def functional(a):
    assert all(len(w)==3 for w in a)
    return sum(n*(-2)**w[2] for w,n in a.items())

records=[]
for n in range(1,17):
    domain=[bracket(jet(i),jet(n-1-i)) for i in range(n) if i<n-1-i]
    images=[delta(v) for v in domain]
    target=bracket(jet(0),jet(n))
    words=sorted(set(target).union(*(set(v) for v in images)))
    matrix=[[v.get(w,0) for w in words] for v in images]
    rank=fmpz_mat(matrix).rank() if matrix else 0
    extended=fmpz_mat(matrix+[[target.get(w,0) for w in words]]).rank()
    assert rank==len(domain)
    assert extended==rank+(n%2)
    # Distinct seed directions: multiplication by s+t on degree n-1.
    distinct=[[int(j==i or j==i+1) for j in range(n+1)] for i in range(n)]
    assert fmpz_mat(distinct).rank()==n
    assert fmpz_mat(distinct+[[int(j==0) for j in range(n+1)]]).rank()==n+1
    record=dict(n=n,kernel_dimension=int(n%2==0),same_seed_ranks=[rank,extended],
                distinct_seed_ranks=[n,n+1])
    if n%2==0:
        m=n//2;v={}
        for i in range(m):v=add(v,bracket(jet(i),jet(n-1-i)),(-1)**i)
        assert delta(v)==target
        q=bracket(jet(0),v)
        assert functional(q)==1-4**m!=0
        checked=0
        for i in range(n-1):
            for j in range(n-1-i):
                k=n-2-i-j
                assert functional(delta(bracket(jet(i),bracket(jet(j),jet(k)))))==0
                # Stronger associative-word check of the same functional.
                assert functional(delta({(i,j,k):1}))==0
                checked+=1
        record.update(m=m,obstruction_value=functional(q),domain_spanning_words=checked,
                      V=[[list(w),c] for w,c in sorted(v.items())],
                      Q=[[list(w),c] for w,c in sorted(q.items())])
    records.append(record)
out=Path('research/certificates/N8-iterated-adjoint-lead')
out.mkdir(parents=True,exist_ok=True);assert not (out/'jet-checks.json').exists()
(out/'jet-checks.json').write_text(json.dumps(dict(records=records,
    scope='Only homogeneous jet identities and ranks; full group decision procedure not implemented.'),indent=2)+'\n')
print('PASS N8 iterated-adjoint jet lead: n=1..16, eight nonzero quadratic obstructions')
