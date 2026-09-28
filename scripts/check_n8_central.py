#!/usr/bin/env python3
"""Exact central-target checks, including independent metabelian obstructions."""
import json,random,time
from pathlib import Path
from n8_ia_orbits import wcomm,wpow
from n8_central import Magnus,bracket,decide_central,mixed_type,equal_type,add
from n8_class5 import solve as solve5

seed=9282612;rng=random.Random(seed)
out=Path(__file__).resolve().parents[1]/'research/certificates/N8-central'
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
records=[];fixtures=[]
def record(row):
    records.append(row)
    (out/'checks.json').write_text(json.dumps(dict(seed=seed,records=records),indent=2)+'\n')
    (out/'fixtures.g').write_text('N8IAFixtures := '+json.dumps(fixtures)+';\n')
    print(json.dumps({k:v for k,v in row.items() if k not in ('word','result')}),flush=True)

def ad(a,b,n):
    for _ in range(n):b=wcomm(a,b)
    return b

for rank,degree in [(2,4),(2,5),(2,6),(2,7),(2,8),(3,6)]:
    started=time.monotonic();m=Magnus(rank,degree)
    record(dict(test='build',rank=rank,degree=degree,seconds=round(time.monotonic()-started,3)))
    for p in range(1,degree//2+1):
        q=degree-p
        for scale in (1,2):
            x=wpow(m.bydegree[p][0]['word'],scale)
            y=m.bydegree[q][-1]['word']
            word=wcomm(x,y)
            # Some rank-two equal-weight spaces have dimension one and only
            # yield the identity. Keep this control, but identify it explicitly.
            expected_nontrivial=m.expansion(word)!={():1}
            started=time.monotonic();ans=decide_central(m,word);assert ans['answer']
            fixtures.append([rank,degree,word,ans['x'],ans['y']])
            record(dict(test='positive',rank=rank,degree=degree,p=p,q=q,scale=scale,
                        nontrivial=expected_nontrivial,seconds=round(time.monotonic()-started,3),
                        word=word,result=ans))
    # In the rank-two metabelian Lie quotient this target is
    # [a,b]*(a^(c-2)+2*b^(c-2)). The polynomial has no rational linear factor
    # by Eisenstein at 2. A bracket of two derived elements has zero image;
    # a bracket with a linear factor would force such a polynomial factor.
    if rank==2:
        word=ad([1],[2],degree-1)+wpow(ad([2],[1],degree-1),-2)
        started=time.monotonic();ans=decide_central(m,word);assert not ans['answer']
        if degree==5:assert not solve5(word,rank)['answer']
        record(dict(test='negative_metabelian_Eisenstein',rank=rank,degree=degree,
                    seconds=round(time.monotonic()-started,3),word=word,result=ans))
    if rank==3:
        basis=[m.layer(h['value'],3) for h in m.bydegree[3]]
        w=add(bracket(m,basis[0],basis[1]),bracket(m,basis[2],basis[3]))
        ans,trace=equal_type(m,w,3)
        assert ans is None and trace==dict(reason='exterior_rank',rank=4)
        record(dict(test='negative_equal_type_rank_four',rank=rank,degree=degree,result=trace))

# This comparison uses the separate class-five implementation and includes
# arbitrary sums of central Hall coordinates, not just generated witnesses.
m=Magnus(2,5)
for case in range(8):
    word=[]
    for h in m.bydegree[5]:word+=wpow(h['word'],rng.randrange(-2,3))
    started=time.monotonic();ans=decide_central(m,word);earlier=solve5(word,2)
    assert ans['answer']==earlier['answer'],(word,ans,earlier)
    if ans['answer']:fixtures.append([2,5,word,ans['x'],ans['y']])
    record(dict(test='class5_cross',rank=2,degree=5,case=case,answer=ans['answer'],
                seconds=round(time.monotonic()-started,3),word=word,result=ans))

print('PASS N8 central checks:',len(records),'records;',len(fixtures),'positive witnesses')
