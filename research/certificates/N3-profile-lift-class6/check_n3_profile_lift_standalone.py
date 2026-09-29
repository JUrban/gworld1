#!/usr/bin/env python3
"""Standalone integer check of the class-six profile-lift obstruction.

No GAP, FLINT, SymPy, Hall collection, or constructor imports.  The target
certificate is a normal multiplicative echelon subgroup of truncated units,
not an additive relaxation of that subgroup.  See the accompanying note.
"""
import json
from itertools import combinations, product
from pathlib import Path

p=json.loads(Path('research/certificates/N3-profile-lift-class6/certificate.json').read_text())
assert (p['rank'],p['nilpotency_class'],p['source_pair_bound'],p['target_pair_bound'])==(3,6,3,2)
one={():1}
def clean(v):return {w:n for w,n in v.items() if n}
def add(a,b,t=1):
    out=dict(a)
    for w,n in b.items():out[w]=out.get(w,0)+t*n
    return clean(out)
def mul(a,b):
    out={}
    for v,n in a.items():
        for w,k in b.items():
            if len(v)+len(w)<=6:out[v+w]=out.get(v+w,0)+n*k
    return clean(out)
def inv(a):
    assert a.get(())==1
    v=add(a,one,-1);term=one;out=one
    for k in range(1,7):
        term=mul(term,v)
        if not term:break
        out=add(out,term,(-1)**k)
    return out
def power(a,n):
    assert isinstance(n,int)
    if n<0:a=inv(a);n=-n
    out=one
    while n:
        if n%2:out=mul(out,a)
        n//=2
        if n:a=mul(a,a)
    return out
def expansion(word):
    out=one
    for s in word:
        assert isinstance(s,int) and 1<=abs(s)<=3
        letter={(abs(s)-1,)*k:(-1)**k if s<0 else 1
                for k in range(7 if s<0 else 2)}
        out=mul(out,letter)
    return out
def winv(w):return [-s for s in reversed(w)]
def reduce_word(w):
    out=[]
    for s in w:
        if out and out[-1]==-s:out.pop()
        else:out.append(s)
    return out
def commword(v,w):return reduce_word(winv(v)+winv(w)+v+w)
def relations(bound):
    out=[]
    for i,j in combinations(range(1,4),2):
        for tail in product([i,j],repeat=bound-1):
            w=commword([j],[i])
            for k in tail:w=commword(w,[k])
            out.append(w)
    return out
def normal(rel,depth_max):
    out=[]
    for ri,r in enumerate(rel):
        for depth in range(depth_max+1):
            for tail in product(range(1,4),repeat=depth):
                w=r
                for k in tail:w=commword(w,[k])
                out.append(dict(relation=ri,tail=list(tail),word=w))
    return out
source=relations(3);target=relations(2)
assert p['source_relations']==source and p['target_relations']==target
assert p['source_normal']==normal(source,2) and len(p['source_normal'])==156
assert p['target_normal']==normal(target,3) and len(p['target_normal'])==240
w=expansion(p['word']);v=add(w,one,-1)
assert v and all(len(t)==6 for t in v)
coeffs=p['square_relator_coefficients']
assert coeffs==[-1 if i in [38,86,134] else 0 for i in range(156)]
rhs=one
for record,n in zip(p['source_normal'],coeffs):
    if n:rhs=mul(rhs,power(expansion(record['word']),n))
assert mul(w,w)==rhs and w!=rhs

# Independently parse each printed bracket expression.
def parse_expression(s):
    def parse(i):
        if s[i] in 'abc':return ['abc'.index(s[i])+1],i+1
        assert s[i]=='['
        a,i=parse(i+1);assert s[i]==','
        b,i=parse(i+1);assert s[i]==']'
        return commword(a,b),i+1
    ans,end=parse(0);assert end==len(s)
    return ans
printed=one
for term in p['hall_expression']:
    tw=parse_expression(term['expression'])
    assert tw==term['word']
    printed=mul(printed,power(expansion(tw),term['exponent']))
assert printed==w

key=lambda t:(len(t),t)
basis=[]
for row in p['target_echelon_basis']:
    b={():1}
    for term in row['polynomial']:
        t=tuple(term['monomial']);n=term['coefficient']
        assert t not in b and 3<=len(t)<=6 and all(j in range(3) for j in t)
        assert isinstance(n,int) and n
        b[t]=n
    pivot=tuple(row['pivot'])
    assert pivot==min((t for t in b if t),key=key) and b[pivot]>0
    basis.append((pivot,b))
pivots=[pivot for pivot,_ in basis]
assert pivots==sorted(set(pivots),key=key) and len(basis)==180
def reduce(g):
    for pivot,b in basis:
        n,r=divmod(g.get(pivot,0),b[pivot])
        if r:return False,dict(pivot=list(pivot),divisor=b[pivot],coefficient=g[pivot])
        if n:g=mul(power(b,-n),g)
    return g==one,None

# Commutator corrections are central (degree six).  Checking them suffices
# for all ordered integral products of basis elements to form a subgroup.
comm_checks=0
for (pv,a),(pw,b) in combinations(basis,2):
    if len(pv)+len(pw)>6:continue
    comm=mul(mul(mul(inv(a),inv(b)),a),b)
    assert all(not t or len(t)==6 for t in comm)
    assert reduce(comm)[0]
    comm_checks+=1
normal_checks=0
for _,b in basis:
    for i in [1,2,3]:
        for sign in [1,-1]:
            x=expansion([sign*i]);conjugate=mul(mul(inv(x),b),x)
            assert reduce(conjugate)[0]
            normal_checks+=1
for record in p['target_normal']:assert reduce(expansion(record['word']))[0]
member,obstruction=reduce(w)
assert not member and obstruction==p['target_nonmembership']
assert reduce(one)[0] and reduce(mul(w,w))[0]
print('Positive square identity: three relator conjugation-differences, integral coefficients -1.')
print('Target certificate:',len(basis),'rows;',comm_checks,'central commutator checks;',
      normal_checks,'signed conjugation checks; 240 relator checks.')
print('Nonmembership:',obstruction)
print('PASS N3 class-six profile-lift standalone certificate')
