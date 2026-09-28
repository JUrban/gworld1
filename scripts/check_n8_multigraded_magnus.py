#!/usr/bin/env python3
"""Cross-check the new exact Hall projection against the old implementation."""
import json,random
from pathlib import Path
from n8_class8_magnus import Magnus as Old
from n8_multigraded_magnus import Magnus as New
from n8_ia_orbits import add
from n8_central import primitive_lie_line
from sympy import Rational

seed=9282639;rng=random.Random(seed)
records=[]
for rank,degree in [(2,9),(3,7)]:
    print('BEGIN comparison',rank,degree,flush=True)
    old=Old(rank,degree);new=New(rank,degree)
    assert old.hall==new.hall
    count=0
    for d in range(1,degree+1):
        for case in range(8):
            coords=[rng.choice([-2,-1,0,0,0,1,2]) for _ in old.bydegree[d]]
            tensor={}
            for h,n in zip(old.bydegree[d],coords):
                tensor=add(tensor,old.layer(h['value'],d),n)
            assert old.coordinates(tensor,d)==new.coordinates(tensor,d)==coords
            rational=add({},tensor,Rational(1,3))
            assert primitive_lie_line(old,rational,d)==primitive_lie_line(new,rational,d)
            count+=1
    for case in range(4):
        word=[rng.choice([-rank,-1,1,rank]) for _ in range(5)]
        g=old.expansion(word)
        assert g==new.expansion(word)
        assert old.collect(g)==new.collect(g)
    # Associative tensors outside the Lie layer must still be rejected.
    for algebra in [old,new]:
        assert primitive_lie_line(algebra,{(0,0):1},2) is None
        try:algebra.coordinates({(0,0):1},2)
        except AssertionError:pass
        else:raise AssertionError('Accepted an associative non-Lie tensor')
    records.append(dict(rank=rank,degree=degree,hall_elements=len(old.hall),
                        coordinate_and_rational_line_checks=count,group_collect_checks=4))
out=Path('research/certificates/N8-class9')
out.mkdir(parents=True,exist_ok=True)
assert not (out/'multigraded-check.json').exists()
(out/'multigraded-check.json').write_text(json.dumps(dict(seed=seed,records=records),indent=2)+'\n')
print('PASS N8 multigraded Magnus: identical Hall data, coordinates, rational lines and collection')
