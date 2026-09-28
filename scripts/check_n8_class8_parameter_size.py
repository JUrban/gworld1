#!/usr/bin/env python3
"""Measure and verify affine-kernel shortening on the slow rank-three fixture."""
import json,random
from pathlib import Path
from n8_class8 import Magnus,mixed_candidates,first,short_particular
from n8_ia_orbits import wcomm,wpow
rng=random.Random(9282632);m=Magnus(3,8)
def higher(word,start,stop):
    word=list(word)
    for d in range(start,stop+1):
        h=rng.choice(m.bydegree[d]);word+=wpow(h['word'],rng.choice([-1,0,1]))
    return word
for p,q in [(2,2),(1,4),(1,5),(2,4),(3,3)]:
    wcomm(higher(m.bydegree[p][0]['word'],p+1,8-q),
          higher(m.bydegree[q][-1]['word'],q+1,8-p))
z=[1,3];t=m.bydegree[2][0]['word']+m.bydegree[2][-1]['word']
d=wcomm(z,wcomm(z,t));word=wcomm(z+wpow(t,-1),higher(d,5,7));g=m.expansion(word)
records=[]
for cc,dd in mixed_candidates(m,m.layer(g,5),1,4):
    result=first(m,g,m.lift(cc,1),m.lift(dd,4),1,4,1,None)
    if result is None:continue
    vector,kernel=result
    if not kernel:continue
    short=short_particular(result);direction=kernel[0]
    pivot=next(i for i,x in enumerate(direction) if x)
    assert (short[pivot]-vector[pivot])%direction[pivot]==0
    shift=(short[pivot]-vector[pivot])//direction[pivot]
    assert short==[v+shift*k for v,k in zip(vector,direction)]
    lengths=[len(h['word']) for degree in [2,5] for h in m.bydegree[degree]]
    before=sum(abs(v)*n for v,n in zip(vector,lengths));after=sum(abs(v)*n for v,n in zip(short,lengths))
    records.append(dict(C=cc,D=dd,original=vector,short=short,kernel=direction,shift=shift,
                        word_lengths=[before,after]))
    print('PARAMETER WORD LENGTHS',before,after,'shift',shift,flush=True)
Path('research/certificates/N8-class8/parameter-shortening.json').write_text(json.dumps(records,indent=2)+'\n')
assert records
print('PASS N8 class8 affine parameter shortening:',len(records),'branches')
