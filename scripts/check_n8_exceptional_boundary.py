#!/usr/bin/env python3
"""Complete weighted-Lie kernel ranges at the first separation boundary.

Exact finite controls, not an end-to-end commutator decision algorithm.
"""
from functools import lru_cache
from pathlib import Path
import json, time
from flint import fmpz_mat

OUT=Path('research/certificates/N8-exceptional-boundary')
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

cases=[
    ('gap6_separated',[1,3,4],adj(1,4,2),[2,4]),
    ('gap7_overlapping',[1,4,5],adj(1,4,2),[3,5]),
    ('below_minimum_weight',[2,4,5],adj(1,1,2),[]),
    ('at_minimum_weight',[2,4,5],adj(1,2,2),[2]),
]
records=[]
for name,weights,de,expected in cases:
    begin=time.monotonic();C=expr(1);D=expr(de);p=weights[0]
    q={sum(weights[i-1] for i in w) for w in D}.pop()
    @lru_cache(None)
    def words(n):
        if n==0:return ((),)
        return tuple((i,)+w for i,d in enumerate(weights,1) if d<=n for w in words(n-d))
    def basis(n):return [expand(w) for w in words(n) if lyndon(w)]
    rows=[]
    for t in range(1,q-p):
        us,vs=basis(p+t),basis(q+t)
        cols=[br(U,D) for U in us]+[br(C,V) for V in vs]
        nullity=len(cols)-rank(cols)
        assert nullity==int(t in expected),(name,t,nullity)
        if nullity:assert t<=q-3*p
        rows.append([t,len(us),len(vs),nullity])
    directions=[]
    if name in ('gap6_separated','gap7_overlapping'):
        # [C,V]=[U,D]; the actual correction direction is (U,-V).
        u=2;v=['-',[u,adj(1,3,u)],[adj(1,1,u),adj(1,2,u)]]
        later=adj(1,2,u);later_v=[later,adj(1,1,later)]
        for t,ue,ve in [(expected[0],u,v),(expected[1],later,later_v)]:
            assert br(C,expr(ve))==br(expr(ue),D)
            directions.append([t,ue,ve])
    elif name=='at_minimum_weight':
        v=[2,[1,2]];assert br(C,expr(v))==br(expr(2),D)
        directions.append([2,2,v])
    record=dict(name=name,weights=weights,C=1,D=de,p=p,q=q,kernels=rows,
                directions=directions,exceptional=expected,seconds=time.monotonic()-begin)
    records.append(record);print(json.dumps(record),flush=True)
(OUT/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
fixtures=[[r['name'],r['weights'],r['C'],r['D'],r['kernels'],r['directions']] for r in records]
(OUT/'fixtures.g').write_text('N8BoundaryFixtures := '+json.dumps(fixtures)+';\n')
print('PASS N8 exceptional boundary: 4 complete pre-Nielsen ranges; 5 explicit directions',flush=True)
