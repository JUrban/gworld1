#!/usr/bin/env python3
"""Bounded tests of unproved kernel statements for a full class-ten extension."""
import argparse,json
from pathlib import Path
from flint import fmpz_mat
from n8_multigraded_magnus import Magnus
from n8_central import add,bracket

p=argparse.ArgumentParser()
p.add_argument('--rank',type=int,choices=[2,3],required=True)
p.add_argument('--directory',type=Path,required=True)
a=p.parse_args();out=a.directory
out.mkdir(parents=True,exist_ok=True)
assert not (out/'checks.json').exists()
print('BEGIN Hall basis',a.rank,9,flush=True)
m=Magnus(a.rank,9)
b={d:[m.layer(h['value'],d) for h in m.bydegree[d]] for d in range(1,10)}
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,10)})+'\n')
records=[]
def delta(v,n=1):
    for _ in range(n):v=bracket(m,z,v)
    return v
def check(label,c,d,p,q,j,expected,direction=None):
    degree=p+q+j
    print('BEGIN',label,flush=True)
    assert c and d
    cols=[bracket(m,u,d) for u in b[p+j]]+[bracket(m,c,v) for v in b[q+j]]
    matrix=[m.coordinates(v,degree) for v in cols]
    nullity=len(cols)-fmpz_mat(matrix).rank()
    row=dict(label=label,p=p,q=q,offset=j,degree=degree,
             C=m.coordinates(c,p),D=m.coordinates(d,q),
             columns=len(cols),nullity=nullity,expected=expected)
    if direction is not None:
        u,v=direction;vector=m.coordinates(u,p+j)+m.coordinates(v,q+j)
        assert any(vector)
        assert all(sum(k*column[i] for k,column in zip(vector,matrix))==0 for i in range(len(matrix[0])))
        row['direction']=vector
    records.append(row)
    (out/'checks.json').write_text(json.dumps(dict(rank=a.rank,records=records),indent=2)+'\n')
    print(json.dumps({k:v for k,v in row.items() if k not in ['C','D','direction']}),flush=True)
    assert nullity==expected,row

z=b[1][0];t=b[2][0]
# These are the decisive extra kernels, before broad controls.
for index,u in enumerate([delta(t),b[3][-1],add(delta(t),b[3][-1],2)]):
    d=delta(u,2)
    check('15-second-exception-'+str(index),z,d,1,5,2,1,
          (u,add({},bracket(m,u,delta(u)),-1)))
    check('15-third-after-exception-'+str(index),z,d,1,5,3,0)
for index in [0,len(b[3])-1]:
    check('13-third-'+str(index),z,b[3][index],1,3,3,0)
for index in [0,len(b[4])-1]:
    d=b[4][index]
    check('24-second-'+str(index),t,d,2,4,2,1,(d,{}))
if len(b[2])>1:
    check('22-third',b[2][0],b[2][-1],2,2,3,0)
    d=bracket(m,b[2][0],b[2][-1])
    check('24-second-pure-EE',t,d,2,4,2,1,(d,{}))
    check('24-second-mixed',t,add(d,b[4][-1]),2,4,2,1,(add(d,b[4][-1]),{}))
check('33-second',b[3][0],b[3][-1],3,3,2,0)
check('33-second-mixed',add(b[3][0],b[3][-1],2),b[3][-1],3,3,2,0)
d=bracket(m,t,b[3][-1])
check('15-second-pure-EB',z,d,1,5,2,0)
check('15-second-mixed',z,add(delta(b[3][-1],2),d),1,5,2,0)
print('PASS N8 class10 completion kernels:',a.rank,len(records),flush=True)
