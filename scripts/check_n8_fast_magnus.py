#!/usr/bin/env python3
"""Compare arithmetic optimization against the preserved original algorithm."""
import json,random
from pathlib import Path
from itertools import product
from n8_fast_magnus import Magnus,OriginalMagnus

SEED=9282625
rng=random.Random(SEED);records=[]
for rank,degree in ((2,7),(3,7)):
    old=OriginalMagnus(rank,degree);new=Magnus(rank,degree)
    assert old.hall==new.hall
    records.append(dict(test='all_Hall_expansions',rank=rank,degree=degree,
                        count=len(new.hall)))
    words=[w for d in range(degree+1) for w in product(range(rank),repeat=d)]
    for case in range(12):
        polys=[]
        for _ in range(2):
            p={w:rng.randint(-3,3) for w in rng.sample(words,min(120,len(words)))}
            polys.append({w:c for w,c in p.items() if c})
        assert old.mul(*polys)==new.mul(*polys)
        records.append(dict(test='random_series_product',rank=rank,degree=degree,case=case))
    for case in range(8):
        w=[rng.choice((-1,1))*rng.randint(1,rank) for _ in range(12)]
        v=[rng.choice((-1,1))*rng.randint(1,rank) for _ in range(12)]
        a,b=old.expansion(w),old.expansion(v)
        assert new.expansion(w)==a and new.expansion(v)==b
        assert old.inv(a)==new.inv(a)
        assert old.comm(a,b)==new.comm(a,b)
        records.append(dict(test='word_inverse_commutator',rank=rank,degree=degree,
                            word=w,other=v))
out=Path('research/certificates/N8-class7-all-rank/magnus-comparison.json')
out.write_text(json.dumps(dict(seed=SEED,records=records),indent=2)+'\n')
print('PASS N8 fast Magnus:',len(records),'records')
