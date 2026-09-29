#!/usr/bin/env python3
"""Exact weighted-Lie controls for arbitrary leading p, including composites.

Finite model checks only. The all-rank proof is in third-layer-proof.md.
"""
from functools import lru_cache
import json,time
from pathlib import Path
from flint import fmpz_mat
OUT=Path('research/certificates/N8-general-offsets');OUT.mkdir(parents=True,exist_ok=False)

def add(a,b,s=1):
 out=dict(a)
 for w,n in b.items():out[w]=out.get(w,0)+s*n
 return {w:n for w,n in out.items() if n}
def product(a,b):
 out={}
 for w,n in a.items():
  for v,k in b.items():out[w+v]=out.get(w+v,0)+n*k
 return {w:n for w,n in out.items() if n}
def br(a,b):return add(product(a,b),product(b,a),-1)
def expression(e):
 if isinstance(e,int):return {(e,):1}
 return add(expression(e[1]),expression(e[2])) if e[0]=='+' else br(expression(e[0]),expression(e[1]))
def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))
@lru_cache(None)
def expand(w):
 if len(w)==1:return {w:1}
 i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
 return br(expand(w[:i]),expand(w[i:]))
def rank(columns):
 support=sorted(set().union(*(p.keys() for p in columns)))
 if not support:return 0
 return fmpz_mat([[p.get(w,0) for w in support] for p in columns]).rank()

def case(name,weights,c,u,d,t,expected,obstruction=True,next_expected=0):
 return dict(name=name,weights=weights,C=c,U=u,D=d,offset=t,expected=expected,
             obstruction=obstruction,next_expected=next_expected)
cases=[]
for name,weights,c,u,t in [
 ('offset2_p1_even_chain',[1,3,4],1,2,2),
 ('offset2_p2_composite_U',[2,2,2,3],3,[1,2],2),
 ('offset2_p3_composite_U',[2,3,3,4],3,[1,2],2),
 ('offset3_p1_composite_U',[1,2,2],1,[2,3],3),
]:cases.append(case(name,weights,c,u,[c,[c,u]],t,1))
# Nonlinear D in a single C-chain, distinct from the pure even-adjoint family.
c,u=1,2
j1=[c,u];j2=[c,j1];j3=[c,j2]
d=['+',['+', [u,j3],[u,j3]], ['+', [j1,j2], ['+',[j1,j2],[j1,j2]]]]
cases.append(case('offset2_p1_nonlinear_D',[1,3,4],c,u,d,2,1))
# The at-most-one assertion is deliberately not extended past Nielsen.
cases.append(case('post_Nielsen_dimension_three',[1,1],1,[1,[1,[1,[1,2]]]],2,4,3,False,0))
records=[]
for row in cases:
 start=time.monotonic();weights=row['weights'];C=expression(row['C']);D=expression(row['D']);U=expression(row['U'])
 def weight(poly):
  ds={sum(weights[i-1] for i in w) for w in poly};assert len(ds)==1;return ds.pop()
 p,q=weight(C),weight(D);t=row['offset']
 @lru_cache(None)
 def words(n):
  if n==0:return ((),)
  return tuple((i,)+w for i,d in enumerate(weights,1) if d<=n for w in words(n-d))
 def basis(n):return [expand(w) for w in words(n) if lyndon(w)]
 us,vs=basis(p+t),basis(q+t)
 columns=[br(x,D) for x in us]+[br(C,x) for x in vs]
 nullity=len(columns)-rank(columns);assert nullity==row['expected'],(row,nullity)
 next_us,next_vs=basis(p+t+1),basis(q+t+1)
 next_cols=[br(x,D) for x in next_us]+[br(C,x) for x in next_vs]
 next_nullity=len(next_cols)-rank(next_cols)
 assert next_nullity==row['next_expected'],(row,next_nullity)
 rec=dict(row,p=p,q=q,first_dimensions=[len(us),len(vs)],nullity=nullity,
          next_dimensions=[len(next_us),len(next_vs)],next_nullity=next_nullity)
 if row['obstruction']:
  V=br(U,br(C,U))
  if row['name']=='offset2_p1_nonlinear_D':
   V=add(br(U,br(U,br(C,br(C,U)))),br(br(C,U),br(U,br(C,U))),-1)
   V=add(V,br(U,br(U,br(C,br(C,U)))))
  assert br(C,V)==br(U,D)
  final=[br(x,D) for x in basis(p+2*t)]+[br(C,x) for x in basis(q+2*t)]
  before=rank(final);after=rank(final+[br(U,V)])
  assert after==before+1
  rec.update(final_dimensions=[len(basis(p+2*t)),len(basis(q+2*t))],final_rank=before,augmented_rank=after)
 rec['seconds']=time.monotonic()-start;records.append(rec)
 (OUT/'checks.json').write_text(json.dumps(records,indent=2)+'\n');print(json.dumps(rec),flush=True)
(OUT/'fixtures.g').write_text('N8GeneralOffsets := '+json.dumps([[r['name'],r['weights'],r['C'],r['U'],r['D'],r['expected'],r['obstruction'],r['first_dimensions'],r.get('final_dimensions',[]),r.get('final_rank',-1),r['offset'],r['next_dimensions'],r['next_nullity']] for r in records]).replace('true','true').replace('false','false')+';\n')
print('PASS N8 general offsets: 6 kernels and successors; 5 quadratic obstructions',flush=True)
