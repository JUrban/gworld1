#!/usr/bin/env python3
"""Exact structural probes for the uncounted class-ten nonlinear family."""
import json
from pathlib import Path
from flint import fmpz_mat
from n8_class10_nonlinear import Magnus,shape,leading_family,bracket,add
from n8_penultimate import mixed_candidates

out=Path('research/certificates/N8-class10-nonlinear-lead')
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
m=Magnus(2,10);z=m.layer(m.gens[0],1);t=m.layer(m.bydegree[2][0]['value'],2)
d,v=shape(m,z,t);w=bracket(m,z,d)
assert bracket(m,z,v)==bracket(m,t,d)
leading=[]
for p in range(1,5):
    pairs=mixed_candidates(m,w,p,8-p)
    assert bool(pairs)==(p==1),(p,pairs)
    leading.append(dict(p=p,q=8-p,pairs=pairs))
first=[bracket(m,m.layer(h['value'],2),d) for h in m.bydegree[2]]
first += [bracket(m,z,m.layer(h['value'],8)) for h in m.bydegree[8]]
matrix=[m.coordinates(col,9) for col in first];rank=fmpz_mat(matrix).rank()
assert len(first)-rank==1
last=[bracket(m,m.layer(h['value'],3),d) for h in m.bydegree[3]]
last += [bracket(m,z,m.layer(h['value'],9)) for h in m.bydegree[9]]
matrix=[m.coordinates(col,10) for col in last];before=fmpz_mat(matrix).rank()
after=fmpz_mat(matrix+[m.coordinates(bracket(m,t,v),10)]).rank()
assert after==before+1
family=leading_family(m,w);assert family and family[0]

# Independent untruncated associative-word arithmetic on formal seed jets.
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
def derivative(p):
    result={}
    for word,value in p.items():
        for i,j in enumerate(word):
            w=word[:i]+(j+1,)+word[i+1:];result[w]=result.get(w,0)+value
    return {w:c for w,c in result.items() if c}
jets=[{(i,):1} for i in range(5)]
D=plus((2,comm(jets[0],jets[3])),(3,comm(jets[1],jets[2])))
V=plus((2,comm(jets[0],comm(jets[0],jets[2]))),(-1,comm(jets[1],comm(jets[0],jets[1]))))
assert derivative(V)==comm(jets[0],D)
def evaluate(p):
    result={}
    for word,value in p.items():
        term={():value}
        for j in word:term=product(term,{('A',):1,('B',):(-3)**j})
        result=plus((1,result),(1,term))
    return result
assert evaluate(comm(jets[0],V)).get(('A','A','A','B'),0)==20
A={('A',):1};B={('B',):1}
assert evaluate(V)==plus((20,comm(A,comm(A,B))),(4,comm(B,comm(A,B))))

# Check the pure outer-square coefficient used to prove uniqueness of z.
a={('z',):1};b={('b',):1};c={('c',):1}
def actual_shape(T):
    ts=[T]
    for _ in range(4):ts.append(comm(a,ts[-1]))
    return plus((2,comm(ts[0],ts[4])),(5,comm(ts[1],ts[3])))
outer=[]
for T,inner,expected in [(comm(b,c),('z','b','c','z','b','c'),-15),
                         (comm(a,b),('z','b','z','z','z','b'),20)]:
    W=actual_shape(T);q={}
    for u in ['z','b','c']:
        for v0 in ['z','b','c']:
            val=W.get((u,)+inner+(v0,),0)
            if val:
                key=tuple(sorted((u,v0)));q[key]=q.get(key,0)+val
    q={k:v0 for k,v0 in q.items() if v0};assert q=={('z','z'):expected},q
    outer.append(dict(inner=inner,coefficient=expected))

record=dict(rank=2,degree=10,leading_pairs=leading,
            C=m.coordinates(z,1),T=m.coordinates(t,2),D=m.coordinates(d,7),
            V=m.coordinates(v,8),W=m.coordinates(w,8),
            first_column_count=len(first),first_rank=rank,
            final_column_count=len(last),obstruction_ranks=[before,after],
            seed_identity_verified=True,AAAB_coefficient=20,pure_square_cases=outer,
            recognized_family=family)
(out/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,11)})+'\n')
print('PASS N8 class10 nonlinear lead: leading pairs, kernel, obstruction, formal identities and pure outer squares')
