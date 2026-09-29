#!/usr/bin/env python3
"""Independent integer certificate check, including the full target check.

The only imported verifier is the dependency-free class-six checker.
No constructor, GAP, FLINT, SymPy, or external Hall arithmetic is imported.
"""
import json
import runpy
from itertools import product
from pathlib import Path

base=runpy.run_path('scripts/check_n3_profile_lift_standalone.py')
p=json.loads(Path('research/certificates/N3-uniform-increment/certificate.json').read_text())
assert (p['source_class'],p['target_class'],p['source_pair_bound'],p['target_pair_bound'])==(7,6,3,2)
assert p['prefix_word']==base['p']['word'] and p['prefix_power']==3
assert p['source_relations']==base['source']
one={():1}
def add(a,b,t=1):
    out=dict(a)
    for w,n in b.items():out[w]=out.get(w,0)+t*n
    return {w:n for w,n in out.items() if n}
def mul(a,b):
    out={}
    for v,n in a.items():
        for w,k in b.items():
            if len(v)+len(w)<=7:out[v+w]=out.get(v+w,0)+n*k
    return {w:n for w,n in out.items() if n}
def inv(a):
    assert a.get(())==1
    v=add(a,one,-1);term=one;out=one
    for k in range(1,8):
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
                for k in range(8 if s<0 else 2)}
        out=mul(out,letter)
    return out
normal=[]
for ri,r in enumerate(p['source_relations']):
    for depth in range(4):
        for tail in product(range(1,4),repeat=depth):
            w=r
            for j in tail:w=base['commword'](w,[j])
            normal.append(dict(relation=ri,tail=list(tail),word=w))
assert p['source_normal']==normal and len(normal)==480
w=power(expansion(p['prefix_word']),3)
assert len(p['central_correction'])==56
for term in p['central_correction']:
    correction=expansion(term['word'])
    assert all(not t or len(t)==7 for t in correction)
    w=mul(w,power(correction,term['exponent']))
assert w!=one and all(not t or len(t)>=6 for t in w)
coeffs=p['square_relator_coefficients']
assert len(coeffs)==480 and all(isinstance(n,int) for n in coeffs)
assert sum(bool(n) for n in coeffs)==24
rhs=one
for record,n in zip(normal,coeffs):
    if n:rhs=mul(rhs,power(expansion(record['word']),n))
assert mul(w,w)==rhs and w!=rhs
projection={t:n for t,n in w.items() if len(t)<=6}
assert projection==base['power'](base['w'],3)
assert not base['reduce'](projection)[0]
assert base['reduce'](base['mul'](projection,projection))[0]
print('Class-seven square identity: 56 central correction factors, 24 normal-relator factors.')
print('Projection to class six is the cube of the independently certified nontrivial order-two image.')
print('PASS N3 uniform-increment standalone certificate')
