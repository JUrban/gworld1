#!/usr/bin/env python3
"""Bounded class-nine decisions, retaining witnesses and every branch audit."""
import argparse,faulthandler,json,random,time
from pathlib import Path
from n8_class9 import Magnus,decide_class9
from n8_ia_orbits import wcomm,wpow

parser=argparse.ArgumentParser()
parser.add_argument('--rank',type=int,choices=[2,3],required=True)
parser.add_argument('--directory',type=Path)
parser.add_argument('--focused',action='store_true')
args=parser.parse_args();rank=args.rank
seed=9282641+rank;rng=random.Random(seed)
out=args.directory or Path(f'research/certificates/N8-class9-rank{rank}')
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
records=[];witnesses=[];steps=[];polynomials=[]
faulthandler.dump_traceback_later(60,repeat=True)
print('BEGIN class-nine Hall basis',rank,flush=True)
m=Magnus(rank,9)
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]]
                                       for d in range(1,10)})+'\n')
def save():
    (out/'checks.json').write_text(json.dumps(dict(seed=seed,rank=rank,records=records),indent=2)+'\n')
    (out/'polynomials.json').write_text(json.dumps(polynomials,indent=2)+'\n')
    (out/'fixtures.g').write_text('N8C9Witnesses := '+json.dumps(witnesses)+';\n'
                                +'N8C9Steps := '+json.dumps(steps)+';\n')
def check(word,label,expected=None,**extra):
    print('BEGIN',label,extra,flush=True);start=time.monotonic();audit=[]
    answer=decide_class9(m,word,audit)
    if expected is not None:assert answer['answer']==expected,(label,answer)
    if answer['answer']:witnesses.append([rank,9,word,answer['x'],answer['y']])
    for row in audit:
        if row['kind']=='polynomial':polynomials.append(row)
        else:steps.append([rank,row['degree'],word,row['x'],row['y'],row['axes'],row['soluble']])
    result=dict(test=label,word=list(word),answer=answer['answer'],result=answer,
                seconds=round(time.monotonic()-start,3),**extra)
    records.append(result);save();print(label,answer['answer'],result['seconds'],flush=True)
def higher(word,start,stop):
    result=list(word)
    for degree in range(start,stop+1):
        result+=wpow(rng.choice(m.bydegree[degree])['word'],rng.choice([-1,0,1]))
    return result

types=[(1,2),(1,3),(2,2),(1,4),(2,3),(1,5),(2,4),(3,3),(1,6),(2,5),(3,4)]
if args.focused:types=[(1,2),(2,3),(1,6),(2,5),(3,4)]
for p,q in types:
    if p==q==2 and rank==2:continue
    x=list(m.bydegree[p][0]['word']);y=list(m.bydegree[q][-1]['word'])
    check(wcomm(higher(x,p+1,9-q),higher(y,q+1,9-p)),
          'constructed_positive',True,p=p,q=q)

z=[1];t=list(m.bydegree[2][0]['word'])
def delta_word(a,n):
    for _ in range(n):a=wcomm(z,a)
    return a
for q in [4,6]:
    d=delta_word(t,q-2)
    for k in [-1,2]:
        check(wcomm(z+wpow(t,k),higher(d,q+1,8)),
              'exceptional_positive',True,q=q,k=k)
    for layer in [q+3,9]:
        for i in range(2):
            check(wcomm(z,d)+m.bydegree[layer][i]['word'],
                  'exceptional_perturbation',q=q,layer=layer,case=i)

# A nontrivial third-period vector for the exact simultaneous-conjugation gauge.
check(wcomm(wpow(z,2),wpow(t,2)),'nonprimitive_type12',True)
# Exercise central and penultimate delegates without a costly general IA orbit.
check(wcomm(z,m.bydegree[7][0]['word']),'penultimate_positive',True)
check(wcomm(z,m.bydegree[8][0]['word']),'central_positive',True)
check([],'identity',True)
check([1],'nonzero_abelianization',False)
assert {row['q'] for row in polynomials}=={4,6}
assert any(not row['answer'] for row in records if row['test']=='exceptional_perturbation')
assert all(row['certificate']['mode']=='finite_points' for row in polynomials)
assert any(not row['certificate']['values'] for row in polynomials)
faulthandler.cancel_dump_traceback_later()
print('PASS N8 class9 targets:',rank,len(records),'targets;',len(witnesses),
      'witnesses;',len(steps),'linear steps;',len(polynomials),'polynomial branches')
