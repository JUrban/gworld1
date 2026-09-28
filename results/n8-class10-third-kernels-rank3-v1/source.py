#!/usr/bin/env python3
"""Bounded exact probes of a proposed class-ten first-kernel classification.

No all-rank conclusion follows from these finite matrix ranks.
"""
import argparse
import json
from pathlib import Path
from flint import fmpz_mat
from n8_multigraded_magnus import Magnus
from n8_central import add, bracket

parser=argparse.ArgumentParser()
parser.add_argument('--rank',type=int,choices=[2,3],required=True)
parser.add_argument('--directory',type=Path,required=True)
args=parser.parse_args()
out=args.directory
out.mkdir(parents=True,exist_ok=True)
assert not (out/'checks.json').exists()
print('BEGIN Hall construction',args.rank,9,flush=True)
m=Magnus(args.rank,9)
basis={d:[m.layer(h['value'],d) for h in m.bydegree[d]] for d in range(1,10)}
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]]
                                       for d in range(1,10)})+'\n')
records=[]
def delta(z,t,k=1):
    for _ in range(k):t=bracket(m,z,t)
    return t
def check(label,c,d,p,q,expected,direction=None):
    print('BEGIN',label,flush=True)
    assert c and d and p+q==8
    cols=[bracket(m,u,d) for u in basis[p+1]]+[bracket(m,c,v) for v in basis[q+1]]
    matrix=[m.coordinates(col,9) for col in cols]
    nullity=len(cols)-fmpz_mat(matrix).rank()
    row=dict(label=label,p=p,q=q,C=m.coordinates(c,p),D=m.coordinates(d,q),
             columns=len(cols),nullity=nullity,expected=expected)
    if direction is not None:
        u,v=direction
        vector=m.coordinates(u,p+1)+m.coordinates(v,q+1)
        assert any(vector)
        assert all(sum(a*col[i] for a,col in zip(vector,matrix))==0
                   for i in range(len(matrix[0])))
        row['direction']=vector
    records.append(row)
    (out/'checks.json').write_text(json.dumps(dict(rank=args.rank,records=records),indent=2)+'\n')
    print(json.dumps({k:v for k,v in row.items() if k not in ['C','D','direction']}),flush=True)
    assert nullity==expected,row

z=basis[1][0];t=basis[2][0]
jets=[delta(z,t,i) for i in range(4)]
p=add(bracket(m,t,jets[3]),bracket(m,t,jets[3]))
p=add(p,bracket(m,jets[1],jets[2]),3)
v=add(bracket(m,t,bracket(m,t,jets[2])),bracket(m,t,bracket(m,t,jets[2])))
v=add(v,bracket(m,jets[1],bracket(m,t,jets[1])),-1)
check('17-nonlinear-exception',z,p,1,7,1,(t,add({},v,-1)))
check('17-length-one',z,delta(z,t,5),1,7,0)
check('17-length-two-off-ratio',z,bracket(m,t,jets[3]),1,7,0)
check('17-length-three',z,bracket(m,t,bracket(m,t,jets[1])),1,7,0)
check('17-mixed-length',z,add(p,delta(z,t,5)),1,7,0)
for j in [0,len(basis[7])//2,len(basis[7])-1]:
    check('17-hall-'+str(j),z,basis[7][j],1,7,0)
if args.rank==3:
    s=basis[2][-1];sj=[delta(z,s,i) for i in range(4)]
    ps=add(bracket(m,s,sj[3]),bracket(m,s,sj[3]))
    ps=add(ps,bracket(m,sj[1],sj[2]),3)
    check('17-polarization-rank-two',z,add(p,ps),1,7,0)
    check('17-mixed-seeds',z,bracket(m,t,sj[3]),1,7,0)

for p0,q0 in [(2,6),(3,5),(4,4)]:
    for j in range(3):
        c=basis[p0][j%len(basis[p0])]
        d=basis[q0][(j+1)%len(basis[q0])]
        check(str(p0)+str(q0)+'-hall-'+str(j),c,d,p0,q0,0)
    c=add(basis[p0][0],basis[p0][-1],2)
    d=add(basis[q0][1],basis[q0][-1],-1)
    check(str(p0)+str(q0)+'-mixed',c,d,p0,q0,0)

check('26-derived-length-two',t,bracket(m,t,basis[4][-1]),2,6,0)
check('26-two-B-letters',t,bracket(m,basis[3][0],basis[3][-1]),2,6,0)
check('35-derived-second',basis[3][0],bracket(m,t,basis[3][-1]),3,5,0)
if args.rank==3:
    c=bracket(m,basis[2][0],basis[2][1])
    d=bracket(m,basis[2][0],basis[2][2])
    check('44-pure-two-letter',c,d,4,4,0)
    check('26-pure-three-letter',t,bracket(m,t,bracket(m,t,basis[2][-1])),2,6,0)
# Scope control: equal leading directions are excluded by normalization.
check('44-dependent-control',basis[4][0],basis[4][0],4,4,len(basis[5]))
print('PASS N8 class10 third-layer kernels:',args.rank,len(records),flush=True)
