#!/usr/bin/env python3
"""Bounded class-ten group checks; retain the complete branch evidence."""
import gzip,json,time
from pathlib import Path
from n8_class10 import Magnus,decide_class10
from n8_ia_orbits import wcomm,wpow

out=Path('research/certificates/N8-class10-rank2')
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
for index,u in enumerate([wcomm(z,t),wcomm([2],t)]):
    d=wcomm(z,wcomm(z,u))
    check(wcomm(z+u,d),f'15_exception_{index}_positive',True)
    check(wcomm(z+u,d)+m.bydegree[10][0]['word'],f'15_exception_{index}_perturbed')

for p,q in [(1,2),(1,3),(1,4),(2,3),(1,5),(2,4),(3,3),(1,6),(2,5),(3,4)]:
    x=list(m.bydegree[p][0]['word']);y=list(m.bydegree[q][-1]['word'])
    x+=m.bydegree[p+1][0]['word']+m.bydegree[p+2][-1]['word']
    y+=m.bydegree[q+1][-1]['word']+m.bydegree[q+2][0]['word']
    word=wcomm(x,y)
    check(word,f'type{p}{q}_corrected_positive',True)
    if (p,q) in [(1,3),(2,4),(3,3),(1,6)]:
        check(word+m.bydegree[10][0]['word'],f'type{p}{q}_last_perturbation')
check([], 'identity',True)
check([1],'abelian_negative',False)
assert coupled,'The new coupled branch was not exercised'
assert any(r['kind']=='polynomial_late' for r in polynomials),'No new quadratic final branch exercised'
print('PASS N8 full class10 groups:',len(records),'records;',len(witnesses),'witnesses;',
      len(steps),'linear decisions;',len(coupled),'coupled;',len(polynomials),'polynomials',flush=True)
