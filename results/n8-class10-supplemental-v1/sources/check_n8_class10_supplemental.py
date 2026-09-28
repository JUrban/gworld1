#!/usr/bin/env python3
"""Bounded class-ten group checks; retain the complete branch evidence."""
import argparse,gzip,json,time
from pathlib import Path
from n8_class10 import Magnus,decide_class10
from n8_ia_orbits import wcomm,wpow

p=argparse.ArgumentParser();p.add_argument('--directory',type=Path,required=True);args=p.parse_args()
out=args.directory
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
m=Magnus(2,10);records=[];witnesses=[];steps=[];polynomials=[];coupled=[]
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,11)})+'\n')
def save():
    (out/'checks.json').write_text(json.dumps(dict(rank=2,degree=10,records=records),indent=2)+'\n')
    for name,data in [('polynomials',polynomials),('coupled',coupled)]:
        (out/(name+'.json.gz')).write_bytes(gzip.compress((json.dumps(data,separators=(',',':'))+'\n').encode(),mtime=0))
    (out/'fixtures.g').write_text('N8C9Witnesses := '+json.dumps(witnesses)+';\nN8C9Steps := '+json.dumps(steps)+';\n')
def check(word,label,expected=None):
    print('BEGIN',label,flush=True);start=time.monotonic();audit=[]
    result=decide_class10(m,word,audit)
    if expected is not None:assert result['answer'] is expected,(label,result)
    if result['answer']:witnesses.append([2,10,word,result['x'],result['y']])
    for row in audit:
        if row['kind'].startswith('polynomial'):polynomials.append(row)
        elif row['kind']=='coupled':coupled.append(row)
        else:steps.append([2,row['degree'],word,row['x'],row['y'],row['axes'],row['soluble']])
    indexes={id(r['certificate']):i for i,r in enumerate(polynomials)}
    for row in result['trace']:
        if 'polynomial' in row:row['polynomial_certificate_index']=indexes[id(row.pop('polynomial'))]
    records.append(dict(label=label,word=word,result=result,seconds=time.monotonic()-start))
    save();print('RESULT',label,result['answer'],round(records[-1]['seconds'],3),flush=True)

z=[1];t=m.bydegree[2][0]['word']
u=wcomm([2],t);d=wcomm(z,wcomm(z,u))
x=z+t+u;y=d+m.bydegree[6][-1]['word']
check(wcomm(x,y),'coupled_first_corrections_positive',True)
check(wcomm(x,y)+m.bydegree[9][0]['word'],'coupled_degree9_perturbation0')
check(wcomm(x,y)+m.bydegree[9][-1]['word'],'coupled_degree9_perturbation_last')
x=z+u;y=d
check(wcomm(x,y)+m.bydegree[9][0]['word'],'coupled_no_first_degree9_perturbation')
d6=t
for _ in range(4):d6=wcomm(z,d6)
check(wcomm(z+t,d6),'16_exception_positive',True)
check(wcomm(z+t,d6)+m.bydegree[10][0]['word'],'16_exception_final_perturbation')
x=wpow(t,2)+m.bydegree[4][0]['word'];y=wpow(m.bydegree[4][-1]['word'],3)
check(wcomm(x,y),'24_nonprimitive_Nielsen_positive',True)
assert any(row['solution'] is None for row in coupled),'No insoluble coupled system exercised'
assert any(row['solution'] is not None and len(row['solution'][1])==0 for row in coupled),'No singleton coupled solution exercised'
assert any(row['q']==6 for row in polynomials),'No degree-seven exceptional branch exercised'
print('PASS N8 full class10 supplemental:',len(records),'records;',len(witnesses),'witnesses;',len(steps),'linear;',len(coupled),'coupled;',len(polynomials),'polynomials',flush=True)
