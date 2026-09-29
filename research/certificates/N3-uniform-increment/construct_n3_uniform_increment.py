#!/usr/bin/env python3
"""Lift three times the class-six witness by an integral central correction.

The source relator subgroup is contained in gamma_4 of a free class-seven
group, hence is abelian.  Its full normal-closure lattice has 480 explicit
generators.  A mod-two solve only in its central layer produces an actual
integral degree-seven Hall word correction, with a positive square identity.
"""
import json
from itertools import product
from pathlib import Path
from flint import fmpz_mat
from n8_fast_magnus import Magnus
from n8_class3 import add,ONE,wcomm
from n8_class5 import reduced

base=json.loads(Path('research/certificates/N3-profile-lift-class6/certificate.json').read_text())
m=Magnus(3,7)
normal=[]
for ri,r in enumerate(base['source_relations']):
    for depth in range(4):
        for tail in product(range(1,4),repeat=depth):
            w=r
            for j in tail:w=reduced(wcomm(w,[j]))
            normal.append(dict(relation=ri,tail=list(tail),word=w))
assert len(normal)==480
monomials=[w for d in range(4,8) for w in product(range(3),repeat=d)]
values=[add(m.expansion(r['word']),ONE,-1) for r in normal]
rows=[[v.get(w,0) for w in monomials] for v in values]
matrix=fmpz_mat(rows);h,u=matrix.hnf(transform=True)
assert h==u*matrix and abs(u.det())==1
print('Normal lattice Hermite certificate checked',flush=True)
wv=add(m.expansion(base['word']),ONE,-1)
assert all(len(w)>=6 for w in wv)
old={(r['relation'],tuple(r['tail'])):n for r,n in
     zip(base['source_normal'],base['square_relator_coefficients']) if n}
c0=[old.get((r['relation'],tuple(r['tail'])),0) for r in normal]
r0={}
for n,v in zip(c0,values):r0=add(r0,v,n)
error=add({w:6*n for w,n in wv.items()},r0,-3)
assert all(len(w)==7 for w in error)

# Each HNF row with leading degree seven is an actual central word.
# Solve the parity equation, retaining its exact expression in original rows.
binary={}
for i in range(h.nrows()):
    row=[int(h[i,j]) for j in range(h.ncols())]
    pivot=next((j for j,n in enumerate(row) if n),None)
    if pivot is None or len(monomials[pivot])!=7:continue
    bits=sum((n%2)<<j for j,n in enumerate(row));rep=1<<i
    for p,(b,r) in sorted(binary.items()):
        if (bits>>p)&1:bits^=b;rep^=r
    if bits:
        p=(bits&-bits).bit_length()-1;binary[p]=(bits,rep)
bits=sum((error.get(w,0)%2)<<j for j,w in enumerate(monomials));rep=0
for p,(b,r) in sorted(binary.items()):
    if (bits>>p)&1:bits^=b;rep^=r
assert bits==0,'No central parity correction'
selected=[i for i in range(h.nrows()) if (rep>>i)&1]
central=[sum(int(h[i,j]) for i in selected) for j in range(h.ncols())]
correction={}
for w,n in zip(monomials,central):
    q=n-error.get(w,0)
    assert q%2==0
    if q:correction[w]=q//2
assert all(len(w)==7 for w in correction)
coords=m.coordinates(correction,7)
terms=[dict(hall_index=i,exponent=n,word=t['word'])
       for i,(n,t) in enumerate(zip(coords,m.bydegree[7])) if n]
coeffs=[3*n+sum(int(u[i,j]) for i in selected) for j,n in enumerate(c0)]
wcorrected=add({w:3*n for w,n in wv.items()},correction)
rhs={}
for n,v in zip(coeffs,values):rhs=add(rhs,v,n)
assert rhs=={w:2*n for w,n in wcorrected.items()}
actual=m.power(m.expansion(base['word']),3)
for term in terms:actual=m.mul(actual,m.power(m.expansion(term['word']),term['exponent']))
assert add(actual,ONE,-1)==wcorrected

out=Path('research/certificates/N3-uniform-increment')
out.mkdir(parents=True,exist_ok=False)
payload=dict(source_class=7,target_class=6,source_pair_bound=3,target_pair_bound=2,
             prefix_word=base['word'],prefix_power=3,central_correction=terms,
             source_relations=base['source_relations'],source_normal=normal,
             square_relator_coefficients=coeffs,
             target_certificate='../N3-profile-lift-class6/certificate.json')
(out/'certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
def gap(v):
    if isinstance(v,dict):return 'rec('+','.join(k+':='+gap(x) for k,x in v.items())+')'
    if isinstance(v,(list,tuple)):return '['+','.join(map(gap,v))+']'
    return json.dumps(v)
(out/'fixtures.g').write_text('N3IncrementCertificate := '+gap(payload)+';\n')
print('Central correction Hall factors',len(terms),'nonzero square coefficients',sum(bool(n) for n in coeffs))
print('Correction',[(t['hall_index'],t['exponent']) for t in terms])
print('PASS N3 uniform-increment integer certificate constructed')
