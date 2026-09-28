#!/usr/bin/env python3
"""Exact checks of degree-five injectivity, plus a higher-degree countercontrol."""
import json
import random
from itertools import combinations
from pathlib import Path
from n8_central import Magnus, add, bracket, linear_solution

SEED=9282619
rng=random.Random(SEED)
out=Path(__file__).resolve().parents[1]/'research/certificates/N8-class6'
out.mkdir(parents=True,exist_ok=True)
assert not (out/'kernels.json').exists()
records=[]


def save(row):
    records.append(row)
    (out/'kernels.json').write_text(json.dumps(dict(seed=SEED,records=records),indent=2)+'\n')
    print(json.dumps(row),flush=True)


def random_layer(m,d):
    result={}
    for h in rng.sample(m.bydegree[d],min(3,len(m.bydegree[d]))):
        result=add(result,m.layer(h['value'],d),rng.choice((-2,-1,1,2)))
    assert result
    return result


for rank in (2,3,4):
    m=Magnus(rank,5)
    basis2=[m.layer(h['value'],2) for h in m.bydegree[2]]
    basis3=[m.layer(h['value'],3) for h in m.bydegree[3]]
    basis4=[m.layer(h['value'],4) for h in m.bydegree[4]]
    columns=[bracket(m,a,b) for a in basis2 for b in basis3]
    ans=linear_solution(columns,{})
    assert not ans[1]
    save(dict(test='L2_tensor_L3_injection',rank=rank,columns=len(columns),kernel=0))
    for case in range(5):
        z=random_layer(m,1);y2=random_layer(m,2);y3=random_layer(m,3)
        # (1,2) second correction and (1,3) first correction.
        for label,first,second,y in [('kernel_C',basis3,basis4,y2),
                                     ('kernel_D',basis2,basis4,y3)]:
            columns=[bracket(m,a,y) for a in first]+[bracket(m,z,b) for b in second]
            result=linear_solution(columns,{})
            assert not result[1],(rank,label,case)
            save(dict(test=label,rank=rank,case=case,columns=len(columns),kernel=0))
        if len(basis2)>1:
            c,d=rng.sample(basis2,2)
            columns=[bracket(m,u,d) for u in basis3]+[bracket(m,c,v) for v in basis3]
            result=linear_solution(columns,{})
            assert not result[1]
            save(dict(test='kernel_E',rank=rank,case=case,columns=len(columns),kernel=0))

# A concrete nonzero kernel in the next degree prevents an unjustified
# generalization of the three special injectivity statements.
m=Magnus(2,7);a={(0,):1};b={(1,):1}
u=bracket(m,a,b);au=bracket(m,a,u);d=bracket(m,a,au)
v={w:-n for w,n in bracket(m,u,au).items()}
assert u and v and add(bracket(m,u,d),bracket(m,a,v))=={}
quadratic=bracket(m,u,v)
assert quadratic and all(len(w)==7 for w in quadratic)
save(dict(test='higher_degree_nonzero_kernel',rank=2,p=1,q=4,
          U=m.coordinates(u,2),D=m.coordinates(d,4),V=m.coordinates(v,5),
          quadratic_obstruction=m.coordinates(quadratic,7)))
print('PASS N8 class6 kernels:',len(records),'records')
