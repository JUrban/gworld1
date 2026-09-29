#!/usr/bin/env python3
"""Bounded class11 group decisions for the odd-adjoint family."""
import gzip,json,random,time
from pathlib import Path
from n8_odd_adjoint import Magnus,decide_odd_adjoint
from n8_ia_orbits import wcomm,wpow

out=Path('research/certificates/N8-odd-adjoint-groups-rank2')
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
rank=2;c=11;h=3;q=8;seed=9292611;rng=random.Random(seed)
m=Magnus(rank,c)
(out/'halls.json').write_text(json.dumps({str(d):[item['word'] for item in m.bydegree[d]] for d in range(1,c+1)})+'\n')
records=[];witnesses=[];steps=[];polynomials=[]
def save():
    (out/'checks.json').write_text(json.dumps(dict(rank=rank,degree=c,seed=seed,records=records),indent=2)+'\n')
    (out/'polynomials.json.gz').write_bytes(gzip.compress((json.dumps(polynomials,separators=(',',':'))+'\n').encode(),mtime=0))
    (out/'fixtures.g').write_text('N8C9Witnesses := '+json.dumps(witnesses)+';\nN8C9Steps := '+json.dumps(steps)+';\n')
def check(word,label,expected='unspecified'):
    print('BEGIN',label,flush=True);start=time.monotonic();audit=[]
    answer=decide_odd_adjoint(m,word,audit)
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
z=[1];t=list(m.bydegree[2][0]['word']);powers=[z]
for _ in range(h):powers.append(wcomm(t,powers[-1]))
d=[]
for i in range((h+1)//2):d+=wpow(wcomm(powers[i],powers[h-i]),-(-1)**i)
base=wcomm(z,d)
check(base,'displayed_positive',True)
for k in (-1,2):
    x=z+wpow(t,k)+rng.choice(m.bydegree[3])['word']
    y=d+wpow(rng.choice(m.bydegree[q+1])['word'],-1)+rng.choice(m.bydegree[q+2])['word']
    check(wcomm(x,y),'constructed_positive_'+str(k),True)
check(wcomm(wpow(z,2),wpow(d,-3)),'nonprimitive_negative_scalar_positive',True)
for i in range(2):check(base+m.bydegree[c][i]['word'],'last_layer_perturbation_'+str(i))
check(base+m.bydegree[c-1][0]['word'],'first_layer_perturbation')
other=t
for _ in range(c-4):other=wcomm(z,other)
check(wcomm(z,other),'outside_same_degree_linear_adjoint',None)
check([],'outside_identity',None);check([1],'outside_degree_one',None)
assert any(row['result']['answer'] is False for row in records)
assert polynomials and any(not row['certificate']['values'] for row in polynomials)
print('PASS N8 odd-adjoint groups:',len(records),'records;',len(witnesses),'witnesses;',len(steps),'linear steps;',len(polynomials),'polynomials',flush=True)
