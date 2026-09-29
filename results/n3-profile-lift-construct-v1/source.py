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

# A mod-two functional annihilating a multiplicatively/conjugation-stable
# additive envelope of the smaller-profile normal relator subgroup.
basis={}
for v,rhs in [(v,0) for v in target_values+target_products]+[(value,1)]:
    bits=sum((n%2)<<j for j,n in enumerate(vector(v)))
    for pivot,(b,c) in sorted(basis.items()):
        if (bits>>pivot)&1:bits^=b;rhs^=c
    if not bits:
        assert rhs==0,'No mod-two additive-envelope separator'
    else:
        pivot=(bits&-bits).bit_length()-1;basis[pivot]=(bits,rhs)
answer=0
for pivot,(b,c) in sorted(basis.items(),reverse=True):
    if ((b&answer).bit_count()%2)^c:answer|=1<<pivot
support=[w for j,w in enumerate(monomials) if (answer>>j)&1]
assert all(sum(v.get(w,0) for w in support)%2==0
           for v in target_values+target_products)
assert sum(value.get(w,0) for w in support)%2==1

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
             target_mod2_separator=support,hall_expression=terms)
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
print('Target separator',support)
print('PASS N3 class-six profile-lift integer certificate constructed')
