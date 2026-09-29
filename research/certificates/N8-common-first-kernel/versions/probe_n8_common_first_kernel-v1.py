#!/usr/bin/env python3
"""New structural question: can two independent weight-two directions occur?

Exact weighted free Lie algebra on two delta-chains; no group-level claim.
Lyndon words are generated and standard-bracketed in the tensor algebra.
"""
import functools,itertools,json,time
from pathlib import Path
from flint import fmpz_mat

OUT=Path('research/certificates/N8-common-first-kernel')
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
 return tuple(((s,j),)+v for j in range(weight-1) for s in range(2) for v in words(weight-j-2))
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

a={((0,0),):1};b={((1,0),):1}
records=[]
for q in range(2,11):
 start=time.monotonic();ds=basis(q);vs=basis(q+1)
 # Direct sums encoded by a fixed component prefix on tensor words.
 def tag(p,k):return {(k,)+w:c for w,c in p.items()}
 dcols=[add(tag(bracket(a,expansion(d)),0),tag(bracket(b,expansion(d)),1)) for d in ds]
 vcols=[tag(delta(expansion(v)),k) for k in range(2) for v in vs]
 allcols=dcols+vcols
 mat,support=matrix(allcols);nullity=len(allcols)-mat.rank()
 # A single prescribed direction has known exceptions, hence negative control
 # against treating every first correction map as injective.
 single=[bracket(a,expansion(d)) for d in ds]+[delta(expansion(v)) for v in vs]
 smat,_=matrix(single);single_nullity=len(single)-smat.rank()
 record={'q':q,'D_dimension':len(ds),'V_dimension':len(vs),'tensor_rows':len(support),
  'common_kernel_dimension':nullity,'single_direction_dimension':single_nullity,
  'seconds':time.monotonic()-start}
 records.append(record)
 (OUT/'checks.json').write_text(json.dumps({'scope':'Two formal weight-two seed chains only; bounded exact kernel dimensions, not a theorem.',
   'records':records},indent=2)+'\n')
 print(json.dumps(record),flush=True)
 assert nullity==0,('common direction counterexample dimension',record)
 assert single_nullity>=int(q in [2,4,6,7,8,10]),record
print('PASS N8 bounded common first-kernel probe',len(records),'weights',flush=True)
