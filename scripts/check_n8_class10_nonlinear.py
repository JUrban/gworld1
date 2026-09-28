#!/usr/bin/env python3
"""Bounded group decisions and retained certificates for the nonlinear family."""
import faulthandler,gzip,json,random,time
from pathlib import Path
from n8_class10_nonlinear import Magnus,decide_nonlinear
from n8_ia_orbits import wcomm,wpow

out=Path('research/certificates/N8-class10-nonlinear-rank2')
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
rank=2;c=10;q=7;seed=9282610;rng=random.Random(seed)
faulthandler.dump_traceback_later(60,repeat=True)
m=Magnus(rank,c)
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,c+1)})+'\n')
records=[];witnesses=[];steps=[];polynomials=[]
def save():
    (out/'checks.json').write_text(json.dumps(dict(rank=rank,degree=c,seed=seed,records=records),indent=2)+'\n')
    (out/'polynomials.json.gz').write_bytes(gzip.compress((json.dumps(polynomials,separators=(',',':'))+'\n').encode(),mtime=0))
    (out/'fixtures.g').write_text('N8C9Witnesses := '+json.dumps(witnesses)+';\nN8C9Steps := '+json.dumps(steps)+';\n')
def check(word,label,expected='unspecified'):
    print('BEGIN',label,flush=True);start=time.monotonic();audit=[]
    answer=decide_nonlinear(m,word,audit)
    if expected!='unspecified':assert answer['answer'] is expected,(label,answer)
    if answer['answer']:witnesses.append([rank,c,word,answer['x'],answer['y']])
    for row in audit:
        if row['kind']=='polynomial':polynomials.append(row)
        else:steps.append([rank,row['degree'],word,row['x'],row['y'],row['axes'],row['soluble']])
    indexes={id(row['certificate']):i for i,row in enumerate(polynomials)}
    for row in answer['trace']:
        if 'polynomial' in row:row['polynomial_certificate_index']=indexes[id(row.pop('polynomial'))]
    records.append(dict(test=label,word=word,result=answer,seconds=time.monotonic()-start))
    save();print('RESULT',label,answer['answer'],round(records[-1]['seconds'],3),flush=True)
z=[1];t=list(m.bydegree[2][0]['word']);jets=[t]
for _ in range(3):jets.append(wcomm(z,jets[-1]))
d=wpow(wcomm(jets[0],jets[3]),2)+wpow(wcomm(jets[1],jets[2]),3)
base=wcomm(z,d)
for k in [-1,2]:
    x=z+wpow(t,k)+rng.choice(m.bydegree[3])['word']
    y=d+wpow(rng.choice(m.bydegree[8])['word'],-1)+rng.choice(m.bydegree[9])['word']
    check(wcomm(x,y),f'constructed_positive_{k}',True)
check(wcomm(wpow(z,2),wpow(d,-3)),'nonprimitive_negative_scalar_positive',True)
for i in range(2):check(base+m.bydegree[10][i]['word'],f'last_layer_perturbation_{i}')
other=t
for _ in range(5):other=wcomm(z,other)
check(wcomm(z,other),'outside_same_degree_iterated_commutator',None)
check([], 'outside_identity',None);check([1],'outside_degree_one',None)
assert any(row['result']['answer'] is False for row in records)
assert polynomials and any(not row['certificate']['values'] for row in polynomials)
faulthandler.cancel_dump_traceback_later()
print('PASS N8 class10 nonlinear groups:',len(records),'records;',len(witnesses),
      'witnesses;',len(steps),'linear steps;',len(polynomials),'polynomials')
