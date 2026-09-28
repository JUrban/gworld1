#!/usr/bin/env python3
"""Additional leading-recognition checks; these are not group decisions."""
import json
from pathlib import Path
from n8_class10_nonlinear import Magnus,shape,leading_family,bracket,add
out=Path('research/certificates/N8-class10-nonlinear-rank3-leading')
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
m=Magnus(3,8);records=[]
for name,z,t,scale in [
    ('non_z_two_form',m.layer(m.gens[0],1),m.layer(m.bydegree[2][-1]['value'],2),1),
    ('mixed_direction_and_form',add(m.layer(m.gens[0],1),m.layer(m.gens[2],1)),
     add(m.layer(m.bydegree[2][0]['value'],2),m.layer(m.bydegree[2][-1]['value'],2),2),-3)]:
    d,v=shape(m,z,t);w=add({},bracket(m,z,d),scale)
    result=leading_family(m,w);assert result and result[0]
    records.append(dict(test=name,z=m.coordinates(z,1),T=m.coordinates(t,2),scalar=scale,
                        W=m.coordinates(w,8),recognition=result))
(out/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS N8 class10 nonlinear rank3 leading: two exact rational-family recognition cases')
