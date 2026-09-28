#!/usr/bin/env python3
"""Bounded class-eight target checks with exact witness/branch certificates."""
import argparse,faulthandler,json,random,time
faulthandler.dump_traceback_later(60,repeat=True)
from pathlib import Path
from n8_class8 import Magnus,decide_class8
from n8_ia_orbits import wcomm,wpow

parser=argparse.ArgumentParser();parser.add_argument('--rank',type=int,choices=[2,3],required=True)
parser.add_argument('--directory',type=Path)
args=parser.parse_args();rank=args.rank
seed=9282629+rank;rng=random.Random(seed)
out=args.directory or Path(f'research/certificates/N8-class8-focused-rank{rank}')
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
records=[];witnesses=[];steps=[];polynomials=[]
m=Magnus(rank,8)
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]]
                                       for d in range(1,9)})+'\n')
def save():
    (out/'checks.json').write_text(json.dumps(dict(seed=seed,rank=rank,records=records),indent=2)+'\n')
    (out/'polynomials.json').write_text(json.dumps(polynomials,indent=2)+'\n')
    (out/'fixtures.g').write_text('N8C8Witnesses := '+json.dumps(witnesses)+';\n'
                                +'N8C8Steps := '+json.dumps(steps)+';\n')
def check(word,label,expected=None,**extra):
    print('BEGIN',label,extra,flush=True);start=time.monotonic();audit=[]
    result=decide_class8(m,word,audit)
    if expected is not None:assert result['answer']==expected,(label,result)
    if result['answer']:witnesses.append([rank,8,word,result['x'],result['y']])
    for row in audit:
        if row['kind']=='polynomial7':polynomials.append(row)
        else:steps.append([rank,row['degree'],word,row['x'],row['y'],row['axes'],row['soluble']])
    record=dict(test=label,answer=result['answer'],word=word,result=result,
                seconds=round(time.monotonic()-start,3),**extra)
    records.append(record);save()
    print(label,result['answer'],record['seconds'],flush=True)
def higher(word,start,stop):
    word=list(word)
    for d in range(start,stop+1):
        h=rng.choice(m.bydegree[d]);word+=wpow(h['word'],rng.choice([-1,0,1]))
    return word

for p,q in [(2,2),(1,4),(1,5),(2,4),(3,3)]:
    if p==q==2 and rank==2:continue
    x=m.bydegree[p][0]['word'];y=m.bydegree[q][-1]['word']
    check(wcomm(higher(x,p+1,8-q),higher(y,q+1,8-p)),
          'constructed_positive',True,p=p,q=q)

z=[1] if rank==2 else [1,3]
t=list(m.bydegree[2][0]['word'])
if rank==3:t+=m.bydegree[2][-1]['word']
d=wcomm(z,wcomm(z,t))
for k in [-1,2]:
    check(wcomm(z+wpow(t,k),higher(d,5,7)),
          'exceptional_positive',True,k=k)

for layer in [7,8]:
    for k in range(3):
        check(wcomm(z,d)+m.bydegree[layer][k]['word'],
              'exceptional_perturbation',layer=layer,case=k)
check([],'identity',True)
check([1],'nonzero_abelianization',False)
assert polynomials
assert any(not r['answer'] for r in records if 'perturbation' in r['test'])
assert all(p['certificate']['mode']=='finite_points' for p in polynomials)
faulthandler.cancel_dump_traceback_later()
print('PASS N8 class8 focused targets:',rank,len(records),'targets;',len(witnesses),
      'witnesses;',len(steps),'linear steps;',len(polynomials),'polynomial branches')
