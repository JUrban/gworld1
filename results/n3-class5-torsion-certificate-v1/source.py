#!/usr/bin/env python3
"""Exact class-five audit of the pseudo-free torsion-freeness assertion.

Three generators; each coordinate pair is class <=2; the full group is class <=5.
The normal relator subgroup in the free class-five group lies in the abelian
gamma_3. Its 78 generators are the six weight-three relators and their positive
conjugation differences through depth two. See the accompanying proof note.
"""
import json
from itertools import combinations, product
from pathlib import Path
from flint import fmpz_mat
from n8_fast_magnus import Magnus
from n8_class3 import add, ONE, wcomm
from n8_class5 import reduced

m=Magnus(3,5)
relations=[]
for i,j in combinations(range(1,4),2):
    for k in [i,j]:
        relations.append(reduced(wcomm(wcomm([j],[i]),[k])))
normal=[]
for ri,r in enumerate(relations):
    for depth in range(3):
        for tail in product(range(1,4),repeat=depth):
            w=list(r)
            for j in tail:w=reduced(wcomm(w,[j]))
            normal.append(dict(relation=ri,tail=list(tail),word=w,
                               value=add(m.expansion(w),ONE,-1)))
assert len(normal)==78
monomials=[w for d in range(3,6) for w in product(range(3),repeat=d)]
rows=[[r['value'].get(w,0) for w in monomials] for r in normal]
a=fmpz_mat(rows);h,u=a.hnf(transform=True)
assert h==u*a and abs(u.det())==1

def solve(v):
    rem=list(v);z=[0]*len(rows)
    for i in range(h.nrows()):
        row=[int(h[i,j]) for j in range(h.ncols())]
        pivot=next((j for j,n in enumerate(row) if n),None)
        if pivot is None:break
        if rem[pivot]%row[pivot]:return None
        z[i]=rem[pivot]//row[pivot]
        rem=[p-z[i]*q for p,q in zip(rem,row)]
    if any(rem):return None
    out=[sum(z[i]*int(u[i,j]) for i in range(len(z))) for j in range(len(z))]
    assert [sum(n*row[j] for n,row in zip(out,rows)) for j in range(len(v))]==v
    return out

def mod2_separator(v):
    # Solve row dot separator=0 for every normal generator, v dot separator=1.
    basis={}
    for row,rhs in [(r,0) for r in rows]+[(v,1)]:
        bits=sum((n%2)<<j for j,n in enumerate(row))
        for p,(b,c) in sorted(basis.items()):
            if (bits>>p)&1:bits^=b;rhs^=c
        if not bits:
            assert not rhs, 'No mod-2 separator'
        else:
            p=(bits&-bits).bit_length()-1;basis[p]=(bits,rhs)
    answer=0
    for p,(b,c) in sorted(basis.items(),reverse=True):
        if ((b&answer).bit_count()%2)^c:answer|=1<<p
    out=[(answer>>j)&1 for j in range(len(v))]
    assert all(sum(x*y for x,y in zip(row,out))%2==0 for row in rows)
    assert sum(x*y for x,y in zip(v,out))%2==1
    return out

hits=[]
for hi,item in enumerate(m.bydegree[5]):
    v=[item['value'].get(w,0) for w in monomials]
    if solve(v) is None:
        twice=solve([2*n for n in v])
        if twice is not None:
            sep=mod2_separator(v)
            hits.append(dict(hall_index_degree5=hi,word=item['word'],
                             square_relator_coefficients=twice,
                             mod2_separator=[list(w) for w,s in zip(monomials,sep) if s]))
            print('Order-two Hall witness',hi,'word length',len(item['word']),flush=True)
assert hits,'No individual Hall-word witness; investigate combinations instead'
out=Path('research/certificates/N3-pseudofree-class5');out.mkdir(parents=True,exist_ok=False)
payload=dict(rank=3,nilpotency_class=5,commutator='x^-1 y^-1 x y',
             profile=dict(singleton=1,pair=2,full=5),relations=relations,
             normal_generators=[{k:v for k,v in r.items() if k!='value'} for r in normal],
             witnesses=hits)
(out/'certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
def gap(v):
    if isinstance(v,dict):return 'rec('+','.join(k+':='+gap(x) for k,x in v.items())+')'
    if isinstance(v,list):return '['+','.join(map(gap,v))+']'
    return json.dumps(v)
(out/'fixtures.g').write_text('N3Certificate := '+gap(payload)+';\n')
print('PASS N3 exact class-five torsion certificates',len(hits))
