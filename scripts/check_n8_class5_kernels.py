#!/usr/bin/env python3
"""Exact sampled correction-kernel checks and equation-reduction controls."""
import json
from pathlib import Path
from sympy import Matrix
from n8_class5 import affine_solve,add,bracket,lie_bases,tensor_solve,coordinates

# Redundant equations with a conflicting right side must survive compression.
assert affine_solve([[2,4,6]],[2,4,7]) is None
assert affine_solve([[2,4,6]],[1,2,3]) is None
assert affine_solve([[2,4,6]],[2,4,6])==([1],[])
assert affine_solve([[2,4,6],[4,8,12]],[2,4,6]) is not None

records=[]
for rank in (2,3,4):
    b2=lie_bases(rank,2);b3=lie_bases(rank,3)
    for scale in (1,2,3):
        u={(0,):2*scale,(rank-1,):scale}
        v={(1,):3,(0,):-1}
        w=bracket(u,v)
        y=add(b2[0],b2[-1],2*scale)
        tests=[
            ('0',[bracket(c,v) for c in b2]+[bracket(u,d) for d in b2],0,None),
            ('A',[bracket(c,y) for c in b2]+[bracket(u,d) for d in b3],1,
             coordinates(y,rank,2)+[0]*len(b3)),
            ('B',[bracket(c,v) for c in b3]+[bracket(u,d) for d in b3],1,
             coordinates(bracket(u,w),rank,3)+coordinates(bracket(v,w),rank,3)),
        ]
        for name,columns,dimension,gauge in tests:
            particular,kernel=tensor_solve(columns,{})
            assert not any(particular)
            assert len(kernel)==dimension,(rank,scale,name,len(kernel))
            period=None
            if gauge:
                primitive=kernel[0];i=next(i for i,x in enumerate(primitive) if x)
                assert gauge[i]%primitive[i]==0
                period=gauge[i]//primitive[i]
                assert period and gauge==[period*x for x in primitive]
            records.append(dict(rank=rank,scale=scale,kernel=name,dimension=dimension,
                                gauge_multiple=period))
        print(json.dumps(records[-3:]),flush=True)
out=Path(__file__).resolve().parents[1]/'research/certificates/N8-class5/kernels.json'
assert not out.exists();out.write_text(json.dumps(records,indent=2)+'\n')
print('PASS N8 class-five 27 sampled kernels and 4 integer-system controls')
