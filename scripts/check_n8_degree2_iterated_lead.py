#!/usr/bin/env python3
"""Exact finite probes of the uncounted degree-two iterated-adjoint lead."""
import argparse,faulthandler,json,time
from pathlib import Path
from flint import fmpz_mat
from n8_multigraded_magnus import Magnus
from n8_central import bracket,add
from n8_penultimate import mixed_candidates

parser=argparse.ArgumentParser();parser.add_argument('--n',type=int,required=True)
args=parser.parse_args();n=args.n;assert n>=1
c=2*n+7;q=2*n+3
out=Path(f'research/certificates/N8-degree2-iterated-lead-n{n}')
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
faulthandler.dump_traceback_later(60,repeat=True)
print('BEGIN basis',2,c,flush=True);m=Magnus(2,c)
C=m.layer(m.bydegree[2][0]['value'],2)
T=add(m.layer(m.bydegree[3][0]['value'],3),m.layer(m.bydegree[3][-1]['value'],3),2)
def delta(t,j):
    for _ in range(j):t=bracket(m,C,t)
    return t
D=delta(T,n);W=bracket(m,C,D)
leading=[]
for p in range(1,(c-2)//2+1):
    pairs=mixed_candidates(m,W,p,c-2-p)
    assert bool(pairs)==(p==2),(p,pairs)
    leading.append(dict(p=p,q=c-2-p,pairs=pairs))
    print('LEADING',p,len(pairs),flush=True)
columns=([bracket(m,m.layer(h['value'],3),D) for h in m.bydegree[3]]
         +[bracket(m,C,m.layer(h['value'],q+1)) for h in m.bydegree[q+1]])
coords=[m.coordinates(v,c-1) for v in columns]
rank=fmpz_mat(coords).rank();assert len(columns)-rank==int(n%2==0)
record=dict(n=n,rank=2,degree=c,C=m.coordinates(C,2),T=m.coordinates(T,3),
            D=m.coordinates(D,q),W=m.coordinates(W,c-2),leading_pairs=leading,
            first_column_count=len(columns),first_rank=rank)
if n%2==0:
    v={}
    for i in range(n//2):v=add(v,bracket(m,delta(T,i),delta(T,n-1-i)),(-1)**i)
    assert bracket(m,T,D)==delta(v,1)
    direction=m.coordinates(T,3)+[-x for x in m.coordinates(v,q+1)]
    assert all(sum(a*col[i] for a,col in zip(direction,coords))==0 for i in range(len(coords[0])))
    Q=bracket(m,T,v)
    final=([bracket(m,m.layer(h['value'],4),D) for h in m.bydegree[4]]
           +[bracket(m,C,m.layer(h['value'],q+2)) for h in m.bydegree[q+2]])
    matrix=[m.coordinates(v,c) for v in final];before=fmpz_mat(matrix).rank()
    after=fmpz_mat(matrix+[m.coordinates(Q,c)]).rank();assert after==before+1
    record.update(kernel_direction=direction,V=m.coordinates(v,q+1),Q=m.coordinates(Q,c),
                  final_column_count=len(final),obstruction_ranks=[before,after])
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]]
                                      for d in range(1,c+1)})+'\n')
(out/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
faulthandler.cancel_dump_traceback_later()
print('PASS N8 degree-two iterated-adjoint lead:',n,c,'leading types, first kernel, and applicable quadratic obstruction')
