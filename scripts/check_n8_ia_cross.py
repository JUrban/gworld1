#!/usr/bin/env python3
"""Compare the orbit method with the separate class-five correction algorithm."""
import json,random,time
from pathlib import Path
from n8_ia_orbits import Magnus,decide_nonzero_degree_two,wcomm,wpow
from n8_class5 import solve as solve5

seed=9282611;rng=random.Random(seed);records=[]
for rank in (2,3):
    m=Magnus(rank,5)
    for case in range(8 if rank==2 else 4):
        # Primitive leading pair. Half the targets have known positive factors;
        # the others are independent higher-layer perturbations of [a,b].
        if case%2==0:
            x=[1];y=[2]
            for degree in (2,3,4):
                x+=wpow(rng.choice(m.bydegree[degree])['word'],rng.choice((-1,0,1)))
                y+=wpow(rng.choice(m.bydegree[degree])['word'],rng.choice((-1,0,1)))
            word=wcomm(x,y)
        else:
            word=wcomm([1],[2])
            for degree in (3,4,5):
                word+=wpow(rng.choice(m.bydegree[degree])['word'],rng.choice((-1,1)))
        started=time.monotonic();earlier=solve5(word,rank);ans=decide_nonzero_degree_two(m,word)
        assert ans['answer']==earlier['answer'],(rank,case,word,earlier,ans)
        record=dict(rank=rank,case=case,answer=ans['answer'],word=word,
                    x=ans.get('x'),y=ans.get('y'),seconds=round(time.monotonic()-started,3))
        records.append(record)
        print(json.dumps({k:v for k,v in record.items() if k not in ('word','x','y')}),flush=True)
out=Path(__file__).resolve().parents[1]/'research/certificates/N8-IA/cross-checks.json'
assert not out.exists();out.write_text(json.dumps(dict(seed=seed,records=records),indent=2)+'\n')
print('PASS N8 IA cross-checks:',len(records))
