#!/usr/bin/env python3
"""Full three-exception weighted-Lie range, with an extra ambient generator.

Enumeration and tensor helpers reused from check_n8_exceptional_boundary.py
at commit 30e9e7b. No group-decision scope follows from these Lie checks alone.
"""
from functools import lru_cache
from pathlib import Path
import json,time
from flint import fmpz_mat
OUT=Path('research/certificates/N8-three-exception-range')
OUT.mkdir(parents=True,exist_ok=False)
def add(a,b,s=1):
    out=dict(a)
    for w,n in b.items():out[w]=out.get(w,0)+s*n
    return {w:n for w,n in out.items() if n}
def product(a,b):
    out={}
    for w,n in a.items():
        for v,k in b.items():out[w+v]=out.get(w+v,0)+n*k
    return {w:n for w,n in out.items() if n}
def br(a,b):return add(product(a,b),product(b,a),-1)
def expr(e):
    if isinstance(e,int):return {(e,):1}
    if e[0]=='+':return add(expr(e[1]),expr(e[2]))
    if e[0]=='-':return add(expr(e[1]),expr(e[2]),-1)
    return br(expr(e[0]),expr(e[1]))
def adj(a,k,b):
    for _ in range(k):b=[a,b]
    return b
def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))
@lru_cache(None)
def expand(w):
    if len(w)==1:return {w:1}
    i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
    return br(expand(w[:i]),expand(w[i:]))
def rank(columns):
    support=sorted(set().union(*(p.keys() for p in columns)))
    if not support:return 0
    return fmpz_mat([[p.get(w,0) for w in support] for p in columns]).rank()

begin=time.monotonic();weights=[1,4,5];C=expr(1);de=adj(1,6,2);D=expr(de);p,q=1,10
@lru_cache(None)
def words(n):
    if n==0:return ((),)
    return tuple((i,)+w for i,d in enumerate(weights,1) if d<=n for w in words(n-d))
def basis(n):return [expand(w) for w in words(n) if lyndon(w)]
rows=[]
for t in range(1,q-p):
    us,vs=basis(p+t),basis(q+t)
    cols=[br(U,D) for U in us]+[br(C,V) for V in vs]
    nul=len(cols)-rank(cols);assert nul==int(t in [3,5,7]),(t,nul)
    rows.append([t,len(us),len(vs),nul]);print('offset',rows[-1],flush=True)
directions=[]
for i in [0,2,4]:
    terms=[[adj(1,i+j,2),adj(1,5-j,2)] for j in range((6-i)//2)]
    ve=terms[0]
    for j,v in enumerate(terms[1:],1):ve=['-' if j%2 else '+',ve,v]
    ue=adj(1,i,2)
    assert br(C,expr(ve))==br(expr(ue),D)
    directions.append([3+i,ue,ve])
record=dict(weights=weights,p=p,q=q,kernels=rows,directions=directions,seconds=time.monotonic()-begin)
(OUT/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
fixtures=[['three_exceptions',weights,1,de,rows,directions]]
(OUT/'fixtures.g').write_text('N8BoundaryFixtures := '+json.dumps(fixtures)+';\n')
print('PASS N8 three-exception range: 8 complete kernels; 3 explicit directions',flush=True)
