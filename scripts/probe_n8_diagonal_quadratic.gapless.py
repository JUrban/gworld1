#!/usr/bin/env python3
"""Complete finite Lie spaces for a possible quadratic-separation functional.

E_i are free Lie generators and delta(E_i)=E_(i+1).  For all homogeneous
D,V with delta V=[E_0,D], test [E_0,V] after the positional polynomial
substitution x_last=x_first, sum(x_i)=0.  This is a structural probe,
not a group equation decision procedure.
"""
from functools import lru_cache
from math import factorial,gcd
from pathlib import Path
import json,time
from flint import fmpz_mat

OUT=Path('research/certificates/N8-diagonal-quadratic-v1.json')
assert not OUT.exists()

def add(a,b,s=1):
    out=dict(a)
    for w,n in b.items():out[w]=out.get(w,0)+s*n
    return {w:n for w,n in out.items() if n}
def mul(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():out[u+v]=out.get(u+v,0)+c*d
    return {w:n for w,n in out.items() if n}
def bracket(a,b):return add(mul(a,b),mul(b,a),-1)
def delta(a):
    out={}
    for w,n in a.items():
        for i in range(len(w)):
            v=w[:i]+(w[i]+1,)+w[i+1:]
            out[v]=out.get(v,0)+n
    return {w:n for w,n in out.items() if n}
@lru_cache(None)
def compositions(total,length):
    if total<0:return ()
    if length==0:return ((),) if total==0 else ()
    return tuple((i,)+w for i in range(total+1)
                 for w in compositions(total-i,length-1))
def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))
@lru_cache(None)
def expand(w):
    if len(w)==1:return {w:1}
    i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
    return bracket(expand(w[:i]),expand(w[i:]))
def basis(total,length):
    return [expand(w) for w in compositions(total,length) if lyndon(w)]
def matrix(columns):
    support=sorted(set().union(*(c.keys() for c in columns)))
    return fmpz_mat(len(support),len(columns),
                   [c.get(w,0) for w in support for c in columns])
def primitive_column(M,j,length):
    col=[int(M[i,j]) for i in range(length)]
    g=0
    for x in col:g=gcd(g,x)
    assert g
    return [x//g for x in col]
def combine(polys,coeff):
    out={}
    for p,c in zip(polys,coeff):
        if c:out=add(out,p,c)
    return out
def restrict(q,m):
    out={}
    for w,c in q.items():
        assert len(w)==m+2
        base=(w[0]+w[-1],)+w[1:m]
        n=w[m]
        for powers in compositions(n,m):
            factor=(-1)**n*2**powers[0]*factorial(n)
            for a in powers:factor//=factorial(a)
            v=tuple(a+b for a,b in zip(base,powers))
            out[v]=out.get(v,0)+c*factor
    return {w:n for w,n in out.items() if n}
def serial(p):return [[list(w),n] for w,n in sorted(p.items())]

records=[]; E0={(0,):1}
for m in range(1,5):
    for k in range(11):
        started=time.monotonic()
        ds=basis(k,m);vs=basis(k-1,m+1)
        A=matrix([bracket(E0,d) for d in ds]+[delta(v) for v in vs])
        null,dim=A.nullspace()
        assert not any(A*null)
        directions=[];images=[]
        for j in range(dim):
            coeff=primitive_column(null,j,len(ds)+len(vs))
            D=combine(ds,coeff[:len(ds)])
            V=combine(vs,[-n for n in coeff[len(ds):]])
            assert D and delta(V)==bracket(E0,D)
            Q=bracket(E0,V);R=restrict(Q,m)
            directions.append((D,V,Q));images.append(R)
        assert matrix([d[0] for d in directions]).rank()==dim
        Rmat=matrix(images);rank=Rmat.rank()
        rec=dict(E_letters=m,index_sum=k,D_dimension=len(ds),
                 V_dimension=len(vs),compatible_dimension=dim,
                 restriction_rank=rank,restriction_kernel_dimension=dim-rank,
                 seconds=time.monotonic()-started)
        if dim>rank:
            nk,nd=Rmat.nullspace();assert nd==dim-rank
            coeff=primitive_column(nk,0,dim)
            D=combine([d[0] for d in directions],coeff)
            V=combine([d[1] for d in directions],coeff)
            Q=bracket(E0,V)
            assert D and not restrict(Q,m) and delta(V)==bracket(E0,D)
            rec['kernel_example']=dict(D=serial(D),V=serial(V),Q=serial(Q))
        records.append(rec)
        OUT.write_text(json.dumps({'scope':'Finite Lie-space restriction probe only',
                                   'records':records},indent=2)+'\n')
        print(json.dumps({a:b for a,b in rec.items() if a!='kernel_example'}),flush=True)
assert len(records)==44
assert records[0]['compatible_dimension']==records[0]['restriction_kernel_dimension']==1
print('PASS N8 diagonal quadratic complete-space probe: 44 spaces',flush=True)
