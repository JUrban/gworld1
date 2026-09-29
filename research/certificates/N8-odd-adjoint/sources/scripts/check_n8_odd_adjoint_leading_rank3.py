#!/usr/bin/env python3
"""Higher-rank scope recognition; no class11/rank3 group decisions."""
import json
from pathlib import Path
from n8_odd_adjoint import Magnus,shape,leading_family,bracket,add
out=Path('research/certificates/N8-odd-adjoint-leading-rank3')
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
m=Magnus(3,9);records=[]
for name,z,t,scale in [
    ('non_z_two_form',m.layer(m.gens[0],1),m.layer(m.bydegree[2][-1]['value'],2),1),
    ('mixed_direction_and_form',add(m.layer(m.gens[0],1),m.layer(m.gens[2],1)),
     add(m.layer(m.bydegree[2][0]['value'],2),m.layer(m.bydegree[2][-1]['value'],2),2),-3)]:
    print('BEGIN',name,flush=True)
    w=add({},bracket(m,z,shape(m,z,t,3)),scale)
    result=leading_family(m,w,3);assert result and result[0]
    records.append(dict(test=name,z=m.coordinates(z,1),T=m.coordinates(t,2),scalar=scale,
                        W=m.coordinates(w,9),recognition=result))
    (out/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
z=m.layer(m.gens[0],1);t0=m.layer(m.bydegree[2][0]['value'],2);t1=m.layer(m.bydegree[2][-1]['value'],2)
w=bracket(m,z,add(shape(m,z,t0,3),shape(m,z,t1,3)))
assert leading_family(m,w,3) is None
records.append(dict(test='outside_sum_of_two_independent_cubes',W=m.coordinates(w,9),recognition=None))
other=t0
for _ in range(7):other=bracket(m,z,other)
assert leading_family(m,other,3) is None
records.append(dict(test='outside_metabelian_nonzero_leading_term',W=m.coordinates(other,9),recognition=None))
(out/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS N8 odd-adjoint rank3 leading: two positive and two outside-scope controls',flush=True)
