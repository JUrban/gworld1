#!/usr/bin/env python3
"""Bounded exact checks of proposed class-nine kernels and obstruction.

This is supporting evidence, not a proof in all ranks. Preserve partial
output on failure/timeout; output directories are never overwritten.
"""
import argparse
import faulthandler
import json
import random
from pathlib import Path
from flint import fmpz_mat
from n8_class8_magnus import Magnus
from n8_central import bracket
from n8_ia_orbits import add

parser=argparse.ArgumentParser()
parser.add_argument('--rank',type=int,choices=[2,3],required=True)
parser.add_argument('--directory',type=Path)
args=parser.parse_args()
rank=args.rank;seed=9282635+rank;rng=random.Random(seed)
out=args.directory or Path(f'research/certificates/N8-class9-kernels-rank{rank}')
out.mkdir(parents=True,exist_ok=True)
assert not (out/'checks.json').exists()
records=[];obstructions=[]
faulthandler.dump_traceback_later(60,repeat=True)
print('BEGIN Hall/Magnus construction',rank,9,flush=True)
m=Magnus(rank,9)
basis={d:[m.layer(h['value'],d) for h in m.bydegree[d]] for d in range(1,10)}
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]]
                                       for d in range(1,10)})+'\n')
def save():
    (out/'checks.json').write_text(json.dumps(dict(seed=seed,rank=rank,records=records,
                                                obstructions=obstructions),indent=2)+'\n')
def combo(degree):
    answer={}
    for h in rng.sample(basis[degree],min(3,len(basis[degree]))):
        answer=add(answer,h,rng.choice([-2,-1,1,2]))
    assert answer
    return answer
def delta(z,a,times=1):
    for _ in range(times):a=bracket(m,z,a)
    return a
def check(label,c,d,p,q,j,expected,direction=None):
    print('BEGIN',label,flush=True)
    cols=[bracket(m,u,d) for u in basis[p+j]]+[bracket(m,c,v) for v in basis[q+j]]
    degree=p+q+j
    matrix=[m.coordinates(col,degree) for col in cols]
    nullity=len(cols)-fmpz_mat(matrix).rank()
    row=dict(test=label,p=p,q=q,j=j,C=m.coordinates(c,p),D=m.coordinates(d,q),
             columns=len(cols),nullity=nullity,expected=expected)
    if direction is not None:
        u,v=direction
        vector=m.coordinates(u,p+j)+m.coordinates(v,q+j)
        assert any(vector)
        assert all(sum(a*col[k] for a,col in zip(vector,matrix))==0
                   for k in range(len(matrix[0])))
        row['predicted_direction']=vector
    records.append(row);save();print(json.dumps(row),flush=True)
    assert nullity==expected,row
for case in range(3):
    z=combo(1);t=combo(2)
    check('type12_third',z,t,1,2,3,1,(delta(z,t,2),bracket(m,t,delta(z,t))))
    check('type23_second',combo(2),combo(3),2,3,2,0)
    d=delta(z,t,4)
    v0=add(bracket(m,t,delta(z,t,3)),bracket(m,delta(z,t),delta(z,t,2)),-1)
    check('type16_exception',z,d,1,6,1,1,(t,add({},v0,-1)))
    check('type16_general',z,combo(6),1,6,1,0)
    check('type25_first',combo(2),combo(5),2,5,1,0)
    c=combo(3);d=combo(4)
    check('type34_first',c,d,3,4,1,1,(d,{}))
    if case<2:
        d=delta(z,t,4);quadratic=bracket(m,t,v0)
        cols=[bracket(m,u,d) for u in basis[3]]+[delta(z,v) for v in basis[8]]
        matrix=[m.coordinates(col,9) for col in cols]
        r1=fmpz_mat(matrix).rank()
        r2=fmpz_mat(matrix+[m.coordinates(quadratic,9)]).rank()
        row=dict(z=m.coordinates(z,1),T=m.coordinates(t,2),D=m.coordinates(d,6),
                 Q=m.coordinates(quadratic,9),ranks=[r1,r2],columns=len(cols))
        obstructions.append(row);save();print('OBSTRUCTION',r1,r2,flush=True)
        assert r2==r1+1

z=basis[1][0];e=basis[2][0];b=basis[3][-1]
check('type16_EW',z,bracket(m,e,delta(z,b)),1,6,1,0)
check('type16_BB',z,bracket(m,basis[3][0],basis[3][-1]),1,6,1,0)
check('type25_EB',e,bracket(m,e,b),2,5,1,0)
if rank==3:
    a=bracket(m,basis[2][0],basis[2][-1])
    check('type16_EEE',z,bracket(m,e,a),1,6,1,0)
    check('type34_EE',b,a,3,4,1,1,(a,{}))
faulthandler.cancel_dump_traceback_later()
print('PASS N8 class9 kernels:',rank,len(records),'kernels;',len(obstructions),'obstructions')
