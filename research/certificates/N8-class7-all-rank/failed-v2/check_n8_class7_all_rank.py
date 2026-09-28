#!/usr/bin/env python3
"""Rank-three group tests of the class-seven extension, with GAP certificates."""
import json,random,time,faulthandler
from pathlib import Path
from n8_class7 import Magnus,decide_class7
from n8_ia_orbits import wcomm,wpow

SEED=9282623
faulthandler.dump_traceback_later(60,repeat=True)
rng=random.Random(SEED)
out=Path('research/certificates/N8-class7-all-rank')
out.mkdir(parents=True,exist_ok=True)
assert not (out/'checks.json').exists()
records=[];witnesses=[];steps=[];quadratics=[]
m=Magnus(3,7)
(out/'hall7.json').write_text(json.dumps([h['word'] for h in m.bydegree[7]])+'\n')
(out/'hall234.json').write_text(json.dumps([[h['word'] for h in m.bydegree[d]] for d in (2,3,4)])+'\n')

def save():
    (out/'checks.json').write_text(json.dumps(dict(seed=SEED,records=records),indent=2)+'\n')
    (out/'fixtures.g').write_text('N8C7Witnesses := '+json.dumps(witnesses)+';\n'
                                +'N8C7Steps := '+json.dumps(steps)+';\n')
    (out/'quadratics.json').write_text(json.dumps(quadratics,indent=2)+'\n')

def check(word,kind,expected=None,**extra):
    start=time.monotonic();audit=[]
    print('BEGIN',kind,extra,flush=True)
    result=decide_class7(m,word,audit)
    if expected is not None:assert result['answer']==expected,(kind,result)
    if result['answer']:witnesses.append([3,7,word,result['x'],result['y']])
    for row in audit:
        if row['kind']=='quadratic':quadratics.append(dict(word=word,**row))
        else:steps.append([3,row['degree'],word,row['x'],row['y'],row['axes'],row['soluble']])
    row=dict(test=kind,answer=result['answer'],word=word,result=result,
             seconds=round(time.monotonic()-start,3),**extra)
    records.append(row);save()
    print(json.dumps({k:v for k,v in row.items() if k not in ('word','result')}),flush=True)

def higher(word,start,stop):
    word=list(word)
    for d in range(start,stop+1):
        h=rng.choice(m.bydegree[d]);word+=wpow(h['word'],rng.choice((-1,0,1)))
    return word

for p,q in [(1,2),(1,3),(2,2),(1,4),(2,3)]:
    for scale in (1,2):
        x=wpow(m.bydegree[p][0]['word'],scale)
        y=wpow(m.bydegree[q][-1]['word'],3 if scale==2 else 1)
        check(wcomm(higher(x,p+1,7-q),higher(y,q+1,7-p)),
              'constructed_positive',True,p=p,q=q,scale=scale)

# z involves two ambient generators, T all three. The associated D is
# delta_z^2 T, so the kernel classification predicts a nonzero direction.
z=[1,3];t=m.bydegree[2][0]['word']+m.bydegree[2][-1]['word']
d=wcomm(z,wcomm(z,t))
for k in (-1,2):
    x=z+wpow(t,k);y=higher(d,5,6)
    check(wcomm(x,y),'mixed_generator_quadratic_positive',True,k=k)

for degree in (3,4,5):
    for case in range(3):
        word=wcomm([1],m.bydegree[degree-1][case]['word'])
        for layer in range(degree+1,8):
            word+=wpow(rng.choice(m.bydegree[layer])['word'],rng.choice((-1,1)))
        check(word,'middle_perturbation',leading=degree,case=case)

base=wcomm(z,d)
for case in range(3):
    check(base+m.bydegree[7][case]['word'],'quadratic_central_perturbation',case=case)
check([1],'abelian_boundary',False)
check([],'identity_boundary',True)
assert quadratics
assert any(any(q['certificate']['coefficients'][2]) for q in quadratics)
assert any(not r['answer'] for r in records if 'perturbation' in r['test'])
print('PASS N8 all-rank class7:',len(records),'targets;',len(witnesses),
      'witnesses;',len(steps),'linear steps;',len(quadratics),'quadratic branches')
faulthandler.cancel_dump_traceback_later()
