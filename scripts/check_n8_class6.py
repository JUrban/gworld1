#!/usr/bin/env python3
"""Class-six exact tests, with group-word fixtures for every new lifting step."""
import json,random,time
from pathlib import Path
from n8_class6 import Magnus,decide_class6
from n8_ia_orbits import wcomm,wpow

SEED=9282620
rng=random.Random(SEED)
out=Path(__file__).resolve().parents[1]/'research/certificates/N8-class6'
out.mkdir(parents=True,exist_ok=True)
assert not (out/'checks.json').exists()
records=[];witnesses=[];steps=[]


def save(row):
    records.append(row)
    (out/'checks.json').write_text(json.dumps(dict(seed=SEED,records=records),indent=2)+'\n')
    (out/'fixtures.g').write_text('N8C6Witnesses := '+json.dumps(witnesses)+';\n'
                                +'N8C6Steps := '+json.dumps(steps)+';\n')
    print(json.dumps({k:v for k,v in row.items() if k not in ('word','result')}),flush=True)


def check(m,word,kind,expected=None,**extra):
    start=time.monotonic();audit=[]
    ans=decide_class6(m,word,audit)
    if expected is not None:assert ans['answer']==expected,(m.rank,kind,word,ans)
    if ans['answer']:witnesses.append([m.rank,6,word,ans['x'],ans['y']])
    for degree,x,y,u,v,soluble in audit:
        steps.append([m.rank,degree,word,x,y,u,v,soluble])
    save(dict(test=kind,rank=m.rank,answer=ans['answer'],word=word,result=ans,
              seconds=round(time.monotonic()-start,3),**extra))
    return ans


def append_layers(m,word,start,stop):
    result=list(word)
    for degree in range(start,stop+1):
        for h in rng.sample(m.bydegree[degree],min(2,len(m.bydegree[degree]))):
            result+=wpow(h['word'],rng.choice((-1,0,1)))
    return result


for rank in (2,3):
    m=Magnus(rank,6)
    for p,q in [(1,2),(1,3),(2,2),(1,4),(2,3),(1,5),(2,4),(3,3)]:
        for scale in (1,2):
            x=wpow(m.bydegree[p][0]['word'],scale)
            y=wpow(m.bydegree[q][-1]['word'],3 if scale==2 else 1)
            x=append_layers(m,x,p+1,6-q)
            y=append_layers(m,y,q+1,6-p)
            check(m,wcomm(x,y),'constructed_positive',True,p=p,q=q,scale=scale)
    # Independent perturbations in both newly covered leading layers.
    for degree in (3,4):
        base=wcomm([1],m.bydegree[degree-1][-1]['word'])
        for case in range(6):
            word=list(base)
            for layer in range(degree+1,7):
                h=rng.choice(m.bydegree[layer])
                word+=wpow(h['word'],rng.choice((-2,-1,1,2)))
            check(m,word,'middle_perturbation',leading=degree,case=case)
    # Negativity in class five already follows from the two-factor-line
    # obstruction explained in class5-proof.md, section 9.
    a,b=[2],[1]
    for _ in range(4):a=wcomm([1],a);b=wcomm([2],b)
    check(m,a+b,'negative_class5_quotient',False)
    check(m,[1],'abelian_boundary',False)
    check(m,[],'identity_boundary',True)

# One case exercises the dispatcher to the already checked all-class IA
# method. The new claims concern the middle layers, not this delegation.
m=Magnus(2,6)
check(m,wcomm([1],[2]),'degree_two_dispatch',True)

assert any(not r['answer'] for r in records if r['test']=='middle_perturbation')
assert any(not s[-1] for s in steps)
assert any(t.get('period',0)>1 for r in records for t in r['result'].get('trace',[]))
print('PASS N8 class6 checks:',len(records),'records;',len(witnesses),
      'positive witnesses;',len(steps),'new lifting steps')
