#!/usr/bin/env python3
"""Dependency-free verifier of the N3 class-five tensor certificate.

Does not import the constructor, Hall machinery, SymPy, FLINT, or GAP.
Uses signed one-based words and a truncated noncommutative polynomial ring.
The proof of why the finite lattice is the normal relator subgroup is in
research/notes/N3-published-cover-audit.md.
"""
import json
from itertools import combinations,product
from pathlib import Path

p=json.loads(Path('research/certificates/N3-pseudofree-class5/certificate.json').read_text())
assert p['rank']==3 and p['nilpotency_class']==5
one={():1}
def clean(v):return {w:n for w,n in v.items() if n}
def mul(a,b):
    out={}
    for v,x in a.items():
        for w,y in b.items():
            if len(v)+len(w)<=5:out[v+w]=out.get(v+w,0)+x*y
    return clean(out)
def expansion(word):
    out=dict(one)
    for s in word:
        assert 1<=abs(s)<=3
        letter={(abs(s)-1,)*k:(-1)**k if s<0 else 1 for k in range(6 if s<0 else 2)}
        out=mul(out,letter)
    return out
def inverse_word(w):return [-x for x in reversed(w)]
def comm_word(v,w):return inverse_word(v)+inverse_word(w)+v+w
def reduce_word(w):
    out=[]
    for s in w:
        if out and out[-1]==-s:out.pop()
        else:out.append(s)
    return out
expected=[]
for i,j in combinations(range(1,4),2):
    for k in [i,j]:expected.append(reduce_word(comm_word(comm_word([j],[i]),[k])))
assert p['relations']==expected
expected_normal=[]
for ri,r in enumerate(expected):
    for depth in range(3):
        for tail in product(range(1,4),repeat=depth):
            word=list(r)
            for j in tail:word=reduce_word(comm_word(word,[j]))
            expected_normal.append(dict(relation=ri,tail=list(tail),word=word))
assert p['normal_generators']==expected_normal and len(expected_normal)==78
assert len(p['witnesses'])==1
# The concise printed expression must be exactly the word being checked.
s=comm_word([2],[1]);t=comm_word([3],[1]);u=comm_word([3],[2])
printed_word=reduce_word(comm_word(comm_word(s,[3]),u)+comm_word(comm_word(t,[2]),u))
assert p['witnesses'][0]['word']==printed_word
printed_identity={(1,(3,3)):-1,(3,(2,2)):1,(4,(1,3)):-2,
                  (5,(1,2)):-2,(5,(2,1)):3}
assert p['witnesses'][0]['square_relator_coefficients']==[
    printed_identity.get((r['relation'],tuple(r['tail'])),0) for r in expected_normal]
rows=[]
for r in expected_normal:
    v=expansion(r['word']);assert v.pop(())==1
    assert all(3<=len(w)<=5 for w in v)
    rows.append(v)
for witness in p['witnesses']:
    v=expansion(witness['word']);assert v.pop(())==1 and v
    assert all(len(w)==5 for w in v)
    coeffs=witness['square_relator_coefficients'];assert len(coeffs)==78
    total={}
    for n,row in zip(coeffs,rows):
        assert isinstance(n,int)
        for w,t in row.items():total[w]=total.get(w,0)+n*t
    assert clean(total)=={w:2*n for w,n in v.items()}
    support=[tuple(w) for w in witness['mod2_separator']]
    assert len(set(support))==len(support)
    assert all(3<=len(w)<=5 and all(i in range(3) for i in w) for w in support)
    assert all(sum(row.get(w,0) for w in support)%2==0 for row in rows)
    assert sum(v.get(w,0) for w in support)%2==1
    # Negative control: the same positive identity does not establish z=1.
    assert clean(total)!=v
    print('Verified: nonzero central word, 2*v in normal lattice, mod-2 separator of v.')
print('PASS N3 standalone tensor torsion certificate',len(p['witnesses']))
