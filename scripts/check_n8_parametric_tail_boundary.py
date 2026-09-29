#!/usr/bin/env python3
"""A real mixed tail term at c-d=10; the linear-tail bound is strict."""
from pathlib import Path
import json,time
from check_n8_parametric_tail import Group
from n8_weighted_automorphisms import add

start=time.monotonic();m=Group(1,4,19)
a,e=m.group_hall(0),m.group_hall(1);y=e
for _ in range(4):y=m.comm(a,y)
u=m.layers[6][0][0];v=m.layers[13][0][0]
U,V=m.group_hall(u),m.group_hall(v)
f00=m.comm(a,y);f10=m.comm(m.mul(a,U),y)
f01=m.comm(a,m.mul(y,V));f11=m.comm(m.mul(a,U),m.mul(y,V))
mixed=add(add(add(f11,f10,-1),f01,-1),f00)
expected=m.bracket(m.hall[u]['lie'],m.hall[v]['lie'])
assert mixed==expected and mixed
assert all(m.weight(w)==19 for w in mixed)
out=Path('research/certificates/N8-parametric-tail/boundary19');out.mkdir(parents=True,exist_ok=False)
data=dict(weights=[1,4],class_bound=19,p=1,q=8,s=5,u=u,v=v,
          hall=[[h['weight'],list(h['pair']) if h['pair'] else []] for h in m.hall],
          mixed=[[list(w),int(n)] for w,n in sorted(mixed.items())],
          seconds=time.monotonic()-start)
(out/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
(out/'fixtures.g').write_text('N8TailBoundary := '+json.dumps([data['hall'],u,v,data['mixed']])+';\n')
print('PASS N8 parametric boundary: class19 actual group mixed term; ',len(mixed),'nonzero tensor coefficients',flush=True)
