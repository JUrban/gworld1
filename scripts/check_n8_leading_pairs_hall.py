#!/usr/bin/env python3
"""Compare the complete integral pair lists before changing representation."""
import json
from pathlib import Path
from n8_multigraded_magnus import Magnus
from n8_central import bracket,add
from n8_penultimate import mixed_candidates as old_mixed,equal_candidates as old_equal
from n8_leading_pairs_hall import mixed_candidates as new_mixed,equal_candidates as new_equal
out=Path('research/certificates/N8-leading-pairs-hall');out.mkdir(parents=True,exist_ok=True)
assert not (out/'checks.json').exists()
records=[]
for rank in [2,3]:
 m=Magnus(rank,6)
 for p,q in [(1,2),(1,3),(2,3),(3,3)]:
  C=m.layer(m.bydegree[p][0]['value'],p)
  D=m.layer(m.bydegree[q][-1]['value'],q)
  if p==q and C==D:continue
  for scale in [1,6]:
   w=add({},bracket(m,C,D),scale)
   if not w:continue
   old=old_mixed(m,w,p,q) if p<q else old_equal(m,w,p)
   new=new_mixed(m,w,p,q) if p<q else new_equal(m,w,p)
   assert old==new,(rank,p,q,scale,old,new)
   records.append(dict(rank=rank,p=p,q=q,scale=scale,pairs=new))
  # A nearby non-bracket need not remain a non-bracket: compare full decisions.
  w=add(bracket(m,C,D),m.layer(m.bydegree[p+q][-1]['value'],p+q))
  old=old_mixed(m,w,p,q) if p<q else old_equal(m,w,p)
  new=new_mixed(m,w,p,q) if p<q else new_equal(m,w,p)
  assert old==new
  records.append(dict(rank=rank,p=p,q=q,case='perturbed',pairs=new))
(out/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS N8 leading Hall representation comparison',len(records),'complete pair lists',flush=True)
