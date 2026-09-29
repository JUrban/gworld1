#!/usr/bin/env python3
"""Independent Lazard-generator tensor replay of the seven deformation spaces."""
from pathlib import Path
import json,itertools,re
import sympy as S
from flint import fmpq_mat

def add(a,b,scale=1):
    out=dict(a)
    for w,n in b.items():out[w]=out.get(w,0)+scale*n
    return {w:n for w,n in out.items() if n}
def mul(a,b):
    out={}
    for u,x in a.items():
        for v,y in b.items():out[u+v]=out.get(u+v,0)+x*y
    return {w:n for w,n in out.items() if n}
def bracket(a,b):return add(mul(a,b),mul(b,a),-1)
def derivative(a):
    out={}
    for w,n in a.items():
        for i in range(len(w)):
            v=w[:i]+(w[i]+1,)+w[i+1:];out[v]=out.get(v,0)+n
    return {w:n for w,n in out.items() if n}
def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))
def expand(w):
    if len(w)==1:return {w:1}
    i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
    return bracket(expand(w[:i]),expand(w[i:]))
def basis(total,length):
    return [expand(w) for w in itertools.product(range(total+1),repeat=length)
            if sum(w)==total and lyndon(w)]
def columns(polys):
    rows=sorted(set().union(*(p.keys() for p in polys)))
    return S.Matrix(len(rows),len(polys),lambda i,j:polys[j].get(rows[i],0))
def rank(polys):
    A=columns(polys)
    return fmpq_mat([[str(x) for x in row] for row in A.tolist()]).rank()
def evaluate(poly,values):return sum(n*S.prod(x**i for x,i in zip(values,w)) for w,n in poly.items())

raw=Path('results/n8-successor-compatible-space-v1/stdout.log').read_text()
matches=re.findall(r'q=(\d+) full two-e deformation dimension=(\d+) compatible dimension=(\d+) ranks A,Q,B,QB=\s*\[\s*([\d, ]+)\s*\] absorption=(true|false)',raw)
expected={int(q):dict(deformation_dimension=int(d),compatible_dimension=int(c),ranks=[int(x) for x in ranks.split(',')],absorbed=flag=='true') for q,d,c,ranks,flag in matches}
assert set(expected)==set(range(8,21,2))
records=[]
for q in range(8,21,2):
    E=lambda i:{(i,):1};k=q-4
    dbasis=basis(q-7,2);vbasis=basis(q-8,3)
    early=[derivative(v) for v in vbasis]+[bracket(E(0),d) for d in dbasis]
    A=columns(early);null=A.nullspace();compatible=[]
    for v in null:
        poly={}
        for i,d in enumerate(dbasis):poly=add(poly,d,v[len(vbasis)+i])
        assert poly
        compatible.append(poly)
    assert rank(compatible)==len(compatible) if compatible else not null
    V={}
    for i in range(k//2):V=add(V,bracket(E(i),E(k-1-i)),(-1)**(i+1))
    assert not add(bracket(E(0),E(k)),derivative(V))
    Q=bracket(E(0),V);late=[derivative(v) for v in basis(q-6,3)]
    images=[bracket(E(2),d) for d in compatible]
    ranks=[rank(late),rank(late+[Q]),rank(late+images),rank(late+images+[Q])]
    result=dict(deformation_dimension=len(dbasis),compatible_dimension=len(compatible),ranks=ranks,absorbed=ranks[-1]==ranks[-2])
    assert result==expected[q],(q,result,expected[q])
    functional=[1,-2,1]
    assert all(evaluate(v,functional)==0 for v in late+images)
    qvalue=evaluate(Q,functional);assert qvalue==2*(1-2**k) and qvalue!=0
    result.update(q=q,quadratic_functional=int(qvalue));records.append(result)
    print('q',q,'independent E-index tensor ranks',ranks,'separating functional',qvalue,flush=True)
Path('research/certificates/N8-successor-compatible-space-python-v1.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS N8 independent successor-compatible spaces: 7 complete spaces and separating functionals')
