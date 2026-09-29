#!/usr/bin/env python3
"""Structural probes for an uncounted nonlinear family in classes 4m+7."""
import json
from math import comb
from pathlib import Path
from flint import fmpz_mat
from n8_multigraded_magnus import Magnus
from n8_central import add, bracket
from n8_penultimate import mixed_candidates

OUT=Path('research/certificates/N8-odd-adjoint-lead')
OUT.mkdir(parents=True,exist_ok=True)
assert not (OUT/'checks.json').exists()


def plus(*terms):
    result={}
    for scalar,p in terms:
        for word,value in p.items():result[word]=result.get(word,0)+scalar*value
    return {w:c for w,c in result.items() if c}


def product(p,q):
    result={}
    for u,a in p.items():
        for v,b in q.items():result[u+v]=result.get(u+v,0)+a*b
    return {w:c for w,c in result.items() if c}


def comm(p,q):return plus((1,product(p,q)),(-1,product(q,p)))


def ad(t,u,n):
    for _ in range(n):u=comm(t,u)
    return u


def derivative(p):
    result={}
    for word,value in p.items():
        for i,j in enumerate(word):
            w=word[:i]+(j+1,)+word[i+1:]
            result[w]=result.get(w,0)+value
    return {w:c for w,c in result.items() if c}


def shape(z,t,h):
    return plus(*[(-(-1)**i,comm(ad(t,z,i),ad(t,z,h-i))) for i in range((h+1)//2)])


def jet_shape(h):
    t,t1,t2=({(i,):1} for i in range(3))
    terms=[(1,ad(t,t2,h-1))]
    terms.extend((1,ad(t,comm(t1,ad(t,t1,h-1-i)),i-1)) for i in range(1,h))
    terms.extend(((-1)**i,comm(ad(t,t1,i),ad(t,t1,h-2-i))) for i in range((h-1)//2))
    return plus(*terms)


def outer_square(w,inner,alphabet):
    result={}
    for a in alphabet:
        for b in alphabet:
            coefficient=w.get((a,)+inner+(b,),0)
            pair=tuple(sorted((a,b)))
            result[pair]=result.get(pair,0)+coefficient
    return {word:value for word,value in result.items() if value}


formal=[]
for h in (1,3,5,7):
    print('BEGIN formal odd index',h,flush=True)
    t,t1=({(i,):1} for i in range(2))
    d=jet_shape(h);v=ad(t,t1,h);w=derivative(d)
    assert derivative(v)==comm(t,d)
    assert d[(0,)*(h-1)+(2,)]==1
    if h>=3:assert w[(1,)+(0,)*(h-2)+(2,)]==h+2
    assert comm(t,v)[(0,)*(h+1)+(1,)]==1
    a,b,c=({(i,):1} for i in ('a','b','c'))
    outer=[]
    for T,inner,expected in [
        (comm(b,c),('b','c')*(h-1)+('a','b','c'),-comb(h+2,2)),
        (comm(a,b),('b',)+('a','b')*(h-1)+('a','a'),-2**(h+1))]:
        D=shape(a,T,h);V=ad(T,comm(a,T),h);W=comm(a,D)
        assert comm(a,V)==comm(T,D)
        qq=outer_square(W,inner,('a','b','c'))
        assert qq=={('a','a'):expected},(h,qq,expected)
        outer.append(dict(inner=inner,coefficient=expected))
    formal.append(dict(h=h,class_bound=2*h+5,outer_squares=outer,
                       kernel_identity=True,nondivisible_word_coefficient=h+2 if h>=3 else None,
                       obstruction_word_coefficient=1))

print('BEGIN actual rank-two class-eleven Hall probe',flush=True)
m=Magnus(2,11)
z=m.layer(m.gens[0],1);t=m.layer(m.bydegree[2][0]['value'],2)
def mad(t,u,n):
    for _ in range(n):u=bracket(m,t,u)
    return u
d={}
for i in range(2):d=add(d,bracket(m,mad(t,z,i),mad(t,z,3-i)),-(-1)**i)
v=mad(t,bracket(m,z,t),3);w=bracket(m,z,d);quad=bracket(m,t,v)
assert bracket(m,z,v)==bracket(m,t,d)
leading=[]
for p in range(1,5):
    pairs=mixed_candidates(m,w,p,9-p)
    assert bool(pairs)==(p==1),(p,pairs)
    leading.append(dict(p=p,q=9-p,pairs=pairs))
columns=[bracket(m,m.layer(h['value'],2),d) for h in m.bydegree[2]]
columns += [bracket(m,z,m.layer(h['value'],9)) for h in m.bydegree[9]]
matrix=[m.coordinates(col,10) for col in columns]
nullity=len(columns)-fmpz_mat(matrix).rank()
direction=m.coordinates(t,2)+[-x for x in m.coordinates(v,9)]
assert nullity==1
assert all(sum(a*row[j] for a,row in zip(direction,matrix))==0 for j in range(len(matrix[0])))
last=[bracket(m,m.layer(h['value'],3),d) for h in m.bydegree[3]]
last += [bracket(m,z,m.layer(h['value'],10)) for h in m.bydegree[10]]
matrix=[m.coordinates(col,11) for col in last]
ranks=[fmpz_mat(matrix).rank(),fmpz_mat(matrix+[m.coordinates(quad,11)]).rank()]
assert ranks[1]==ranks[0]+1
actual=dict(rank=2,degree=11,C=m.coordinates(z,1),T=m.coordinates(t,2),
            D=m.coordinates(d,8),V=m.coordinates(v,9),Q=m.coordinates(quad,11),
            leading=leading,first_nullity=nullity,first_columns=len(columns),
            direction=direction,obstruction_ranks=ranks)
record=dict(formal=formal,actual=actual)
(OUT/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
halls=[[],*[ [h['word'] for h in m.bydegree[d]] for d in range(1,12)]]
(OUT/'fixtures.g').write_text('N8OddHalls := '+json.dumps(halls[1:])+';\nN8OddData := '+json.dumps([actual[k] for k in ['C','T','D','V','Q','direction','obstruction_ranks']])+';\n')
print('PASS N8 odd-adjoint lead: 4 formal indices, 8 outer squares, rank-two class11 leading pairs, kernel and obstruction',flush=True)
