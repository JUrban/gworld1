#!/usr/bin/env python3
"""Look for polynomial double primitives in one free differential Lie chain.
Finite exact structural test, not an N8 decision algorithm.
"""
import functools,json,time
from pathlib import Path
from flint import fmpz_mat
OUT=Path('research/certificates/N8-double-primitive')
OUT.mkdir(parents=True,exist_ok=True)
assert not (OUT/'checks.json').exists()
def add(a,b,s=1):
 out=dict(a)
 for w,c in b.items():out[w]=out.get(w,0)+s*c
 return {w:c for w,c in out.items() if c}
def prod(a,b):
 out={}
 for w,c in a.items():
  for v,d in b.items():out[w+v]=out.get(w+v,0)+c*d
 return {w:c for w,c in out.items() if c}
def bracket(a,b):return add(prod(a,b),prod(b,a),-1)
def delta(a):
 out={}
 for w,c in a.items():
  for i,(seed,j) in enumerate(w):
   v=w[:i]+((seed,j+1),)+w[i+1:];out[v]=out.get(v,0)+c
 return {w:c for w,c in out.items() if c}
@functools.lru_cache(None)
def words(weight):
 if weight==0:return ((),)
 if weight<2:return ()
 return tuple(((s,j),)+v for j in range(weight-1) for s in range(1) for v in words(weight-j-2))
def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))
@functools.lru_cache(None)
def expansion(w):
 if len(w)==1:return {w:1}
 i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
 return bracket(expansion(w[:i]),expansion(w[i:]))
def basis(weight):return [w for w in words(weight) if lyndon(w)]
def matrix(columns):
 support=sorted(set().union(*(c.keys() for c in columns)))
 return fmpz_mat([[c.get(w,0) for w in support] for c in columns]),support


a={((0,0),):1}
records=[]
for q in range(2,15):
 start=time.monotonic();ds=basis(q);vs=basis(q+1);ws=basis(q+2)
 def tag(p,k):return {(k,)+w:c for w,c in p.items()}
 cols=[tag(bracket(a,expansion(d)),0) for d in ds]
 cols += [add(tag(delta(expansion(v)),0),tag(bracket(a,expansion(v)),1),-1) for v in vs]
 cols += [tag(delta(expansion(w)),1) for w in ws]
 mat,support=matrix(cols);nullity=len(cols)-mat.rank()
 rec={'q':q,'dimensions':[len(ds),len(vs),len(ws)],'rows':len(support),
      'double_primitive_dimension':nullity,'seconds':time.monotonic()-start}
 records.append(rec)
 (OUT/'checks.json').write_text(json.dumps({'scope':'One formal weight-two seed chain; bounded dimensions only. Signs of auxiliary primitives do not affect existence.', 'records':records},indent=2)+'\n')
 print(json.dumps(rec),flush=True)
print('PASS N8 bounded double-primitive probe',len(records),'weights',flush=True)
