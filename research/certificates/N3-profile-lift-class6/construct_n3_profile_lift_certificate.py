#!/usr/bin/env python3
"""Construct an exact class-six obstruction to the pair-bound 2 -> 3 repair.

Input word comes from GAP. All positive and negative certificate arithmetic
is reconstructed over integers in a separate Magnus implementation.
"""
import ast
import json
from itertools import combinations, product
from pathlib import Path
from flint import fmpz_mat
from n8_fast_magnus import Magnus
from n8_class3 import add, ONE, wcomm
from n8_class5 import reduced

degree=6
m=Magnus(3,degree)
log=Path('results/n3-profile-lift-extract-v1/stdout.log').read_text()
word=ast.literal_eval(log.split('WORD ',1)[1].split('PASS ',1)[0].strip())
value=add(m.expansion(word),ONE,-1)
assert value and all(len(w)==6 for w in value)
monomials=[w for d in range(3,7) for w in product(range(3),repeat=d)]

def make_relations(bound):
    rel=[]
    for i,j in combinations(range(1,4),2):
        for tail in product([i,j],repeat=bound-1):
            w=wcomm([j],[i])
            for k in tail:w=reduced(wcomm(w,[k]))
            rel.append(reduced(w))
    return rel

def make_normal(rel,depth_max):
    normal=[]
    for ri,r in enumerate(rel):
        for depth in range(depth_max+1):
            for tail in product(range(1,4),repeat=depth):
                w=list(r)
                for k in tail:w=reduced(wcomm(w,[k]))
                normal.append(dict(relation=ri,tail=list(tail),word=w))
    return normal

source_rel=make_relations(3)
source_normal=make_normal(source_rel,2)
target_rel=make_relations(2)
target_normal=make_normal(target_rel,3)
assert len(source_normal)==156 and len(target_normal)==240
source_values=[add(m.expansion(r['word']),ONE,-1) for r in source_normal]
target_values=[add(m.expansion(r['word']),ONE,-1) for r in target_normal]
target_low=[add(m.expansion(w),ONE,-1) for w in target_rel]
target_products=[m.mul(u,v) for u in target_low for v in target_low]
def vector(v):return [v.get(w,0) for w in monomials]
rows=list(map(vector,source_values))
a=fmpz_mat(rows); h,u=a.hnf(transform=True)
assert h==u*a and abs(u.det())==1
remainder=[2*n for n in vector(value)]; coefficients=[0]*len(rows)
for i in range(h.nrows()):
    row=[int(h[i,j]) for j in range(h.ncols())]
    pivot=next((j for j,n in enumerate(row) if n),None)
    if pivot is None:continue
    assert remainder[pivot]%row[pivot]==0
    t=remainder[pivot]//row[pivot]
    remainder=[v-t*b for v,b in zip(remainder,row)]
    coefficients=[v+t*int(u[i,j]) for j,v in enumerate(coefficients)]
assert not any(remainder)
assert [sum(t*row[j] for t,row in zip(coefficients,rows))
        for j in range(len(monomials))]==[2*n for n in vector(value)]

# The attempted mod-two additive-envelope certificate was insufficient.
# Build an integral multiplicative echelon basis in 1 + (degree >= 3).
# This ambient subgroup has class two at truncation degree six.  Verify
# commutator closure and invariance under all original generator conjugations.
order=lambda w:(len(w),w)
basis={}
def insert(g):
    while g!=ONE:
        pivot=min((w for w in g if w),key=order)
        if pivot not in basis:
            basis[pivot]=g if g[pivot]>0 else m.inv(g)
            return
        b=basis[pivot]
        q,r=divmod(g[pivot],b[pivot])
        g=m.mul(m.power(b,-q),g)
        if r:
            basis[pivot]=g
            g=b
for v in target_values:insert(add(v,ONE))
low=[v for w,v in basis.items() if len(w)==3]
for v,w in combinations(low,2):insert(m.comm(v,w))
basis=sorted(basis.items(),key=lambda item:order(item[0]))
def reduce_to_basis(g):
    for pivot,b in basis:
        q,r=divmod(g.get(pivot,0),b[pivot])
        if r:return False,g,pivot,b[pivot]
        if q:g=m.mul(m.power(b,-q),g)
    return g==ONE,g,None,None
for v in target_values:assert reduce_to_basis(add(v,ONE))[0]
for v,w in combinations(low,2):assert reduce_to_basis(m.comm(v,w))[0]
for _,b in basis:
    for x in m.gens:
        for s in [1,-1]:
            y=m.power(x,s)
            assert reduce_to_basis(m.mul(m.mul(m.inv(y),b),y))[0]
member,remainder,bad_pivot,bad_divisor=reduce_to_basis(add(value,ONE))
assert not member

# Print a Hall expression for human inspection; the verifier does not use it.
coords=m.coordinates(value,6)
def bracket(h):
    if h['pair'] is None:return 'abc'[h['word'][0]-1]
    i,j=h['pair'];return '['+bracket(m.hall[i])+','+bracket(m.hall[j])+']'
terms=[dict(exponent=n,expression=bracket(t),word=t['word'])
       for n,t in zip(coords,m.bydegree[6]) if n]
payload=dict(rank=3,nilpotency_class=6,source_pair_bound=3,target_pair_bound=2,
             word=word,source_relations=source_rel,target_relations=target_rel,
             source_normal=source_normal,target_normal=target_normal,
             square_relator_coefficients=coefficients,
             target_echelon_basis=[dict(pivot=w,polynomial=[dict(monomial=v,coefficient=n)
                for v,n in sorted(b.items(),key=lambda item:order(item[0])) if v])
                for w,b in basis],
             target_nonmembership=dict(pivot=bad_pivot,divisor=bad_divisor,
                coefficient=remainder.get(bad_pivot) if bad_pivot else None),
             hall_expression=terms)
out=Path('research/certificates/N3-profile-lift-class6')
out.mkdir(parents=True,exist_ok=False)
(out/'certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
def gap(v):
    if isinstance(v,dict):return 'rec('+','.join(k+':='+gap(x) for k,x in v.items())+')'
    if isinstance(v,(list,tuple)):return '['+','.join(map(gap,v))+']'
    return json.dumps(v)
(out/'fixtures.g').write_text('N3LiftCertificate := '+gap(payload)+';\n')
print('Word length',len(word),'Hall terms',terms)
print('Square identity nonzero coefficients',[(i,n) for i,n in enumerate(coefficients) if n])
print('Target echelon rows',len(basis),'nonmembership',payload['target_nonmembership'])
print('PASS N3 class-six profile-lift integer certificate constructed')
