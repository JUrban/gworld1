#!/usr/bin/env python3
"""Bounded group tests for the candidate class-ten gamma_8 extension."""
import gzip,json,random,time
from pathlib import Path
from n8_class10_third import Magnus,decide_third
from n8_ia_orbits import wcomm,wpow

out=Path('research/certificates/N8-class10-third-rank2')
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
rank=2;degree=10;seed=9282618;rng=random.Random(seed)
m=Magnus(rank,degree)
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]]
                                       for d in range(1,degree+1)})+'\n')
records=[];witnesses=[];steps=[];polynomials=[]
def save():
    (out/'checks.json').write_text(json.dumps(dict(rank=rank,degree=degree,seed=seed,records=records),indent=2)+'\n')
    (out/'polynomials.json.gz').write_bytes(gzip.compress((json.dumps(polynomials,separators=(',',':'))+'\n').encode(),mtime=0))
    (out/'fixtures.g').write_text('N8C9Witnesses := '+json.dumps(witnesses)+';\nN8C9Steps := '+json.dumps(steps)+';\n')
def check(word,label,expected='unspecified'):
    print('BEGIN',label,flush=True);start=time.monotonic();audit=[]
    result=decide_third(m,word,audit)
    if expected!='unspecified':assert result['answer'] is expected,(label,result)
    if result['answer']:witnesses.append([rank,degree,word,result['x'],result['y']])
    for row in audit:
        if row['kind']=='polynomial':polynomials.append(row)
        else:steps.append([rank,row['degree'],word,row['x'],row['y'],row['axes'],row['soluble']])
    indexes={id(row['certificate']):i for i,row in enumerate(polynomials)}
    for row in result['trace']:
        if 'polynomial' in row:row['polynomial_certificate_index']=indexes[id(row.pop('polynomial'))]
    records.append(dict(label=label,word=word,result=result,seconds=time.monotonic()-start))
    save();print('RESULT',label,result['answer'],round(records[-1]['seconds'],3),flush=True)

for p,q in [(1,7),(2,6),(3,5),(4,4)]:
    x=list(m.bydegree[p][0]['word']);y=list(m.bydegree[q][-1]['word'])
    x+=m.bydegree[p+1][0]['word']+m.bydegree[p+2][-1]['word']
    y+=m.bydegree[q+1][-1]['word']+m.bydegree[q+2][0]['word']
    base=wcomm(x,y)
    check(base,f'type{p}{q}_corrected_positive',True)
    check(base+m.bydegree[10][0]['word'],f'type{p}{q}_last_perturbation')
    if p in [2,4]:
        check(wcomm(wpow(x,2),wpow(y,3)),f'type{p}{q}_nonprimitive_positive',True)

z=[1];t=list(m.bydegree[2][0]['word']);jets=[t]
for _ in range(3):jets.append(wcomm(z,jets[-1]))
d=wpow(wcomm(jets[0],jets[3]),2)+wpow(wcomm(jets[1],jets[2]),3)
check(wcomm(z+t,d+m.bydegree[8][0]['word']),'exception_delegates_positive',True)
# Independently justified non-bracket leading term from central-target proof.
u=[2];v=[1]
for _ in range(7):u=wcomm([1],u);v=wcomm([2],v)
check(u+wpow(v,-2),'Eisenstein_leading_negative',False)
check(wcomm(m.bydegree[4][0]['word'],m.bydegree[5][0]['word']),
      'penultimate_delegated_positive',True)
check([], 'identity',True)
check([1],'outside_degree_one',None)
check(wcomm([1],t),'outside_degree_three',None)
assert any(row['result']['answer'] is False for row in records)
print('PASS N8 class10 third-layer groups:',len(records),'records;',len(witnesses),
      'witnesses;',len(steps),'linear steps;',len(polynomials),'polynomials',flush=True)
