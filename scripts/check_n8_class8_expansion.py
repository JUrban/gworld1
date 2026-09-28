#!/usr/bin/env python3
"""Compare balanced expansion with the original exact word algorithm."""
import json,random,time
from pathlib import Path
from n8_class8_magnus import Magnus,SequentialMagnus
from n8_ia_orbits import wcomm,wpow
rng=random.Random(9282633);records=[]
for rank in [2,3]:
    m=Magnus(rank,8)
    for degree in range(1,9):
        for h in m.bydegree[degree]:
            assert m.expansion(h['word'])==h['value']
        records.append(dict(test='all_Hall_words',rank=rank,degree=degree,count=len(m.bydegree[degree])))
    for case in range(12):
        word=[rng.choice([-1,1])*rng.randrange(1,rank+1) for _ in range(20+case*3)]
        assert m.expansion(word)==SequentialMagnus.expansion(m,word)
        records.append(dict(test='sequential_comparison',rank=rank,word=word))
    for case in range(6):
        h=rng.choice(m.bydegree[3]);n=rng.choice([-33,-17,19,41])
        assert m.expansion(wpow(h['word'],n))==m.power(h['value'],n)
        records.append(dict(test='repeated_commutator_word',rank=rank,word=h['word'],exponent=n))
Path('research/certificates/N8-class8/expansion.json').write_text(json.dumps(dict(seed=9282633,records=records),indent=2)+'\n')
print('PASS N8 class8 balanced expansion:',len(records),'records')
