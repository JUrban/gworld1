#!/usr/bin/env python3
"""Bounded group tests, with complete branch certificates, of the new stratum."""
import argparse,faulthandler,gzip,json,random,time
from pathlib import Path
from n8_iterated_adjoint import Magnus,decide_iterated_adjoint
from n8_ia_orbits import wcomm,wpow

parser=argparse.ArgumentParser()
parser.add_argument('--rank',type=int,default=2)
parser.add_argument('--class',dest='degree',type=int,required=True)
parser.add_argument('--directory',type=Path,required=True)
args=parser.parse_args();out=args.directory
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
rank=args.rank;c=args.degree;q=c-3;seed=9282660+10*c+rank;rng=random.Random(seed)
faulthandler.dump_traceback_later(60,repeat=True)
print('BEGIN basis',rank,c,flush=True);m=Magnus(rank,c)
halls={str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,c+1)}
(out/'halls.json').write_text(json.dumps(halls)+'\n')
records=[];witnesses=[];steps=[];polynomials=[]
def save():
    (out/'checks.json').write_text(json.dumps(dict(rank=rank,degree=c,seed=seed,records=records),indent=2)+'\n')
    (out/'polynomials.json.gz').write_bytes(gzip.compress(
        (json.dumps(polynomials,separators=(',',':'))+'\n').encode(),mtime=0))
    (out/'fixtures.g').write_text('N8C9Witnesses := '+json.dumps(witnesses)+';\n'
                                +'N8C9Steps := '+json.dumps(steps)+';\n')
def check(word,label,expected='unspecified'):
    print('BEGIN',label,flush=True);start=time.monotonic();audit=[]
    answer=decide_iterated_adjoint(m,word,audit)
    if expected!='unspecified':assert answer['answer'] is expected,(label,answer)
    if answer['answer']:witnesses.append([rank,c,word,answer['x'],answer['y']])
    for row in audit:
        if row['kind']=='polynomial':polynomials.append(row)
        else:steps.append([rank,row['degree'],word,row['x'],row['y'],row['axes'],row['soluble']])
    indexes={id(row['certificate']):i for i,row in enumerate(polynomials)}
    for row in answer['trace']:
        if 'polynomial' in row:
            row['polynomial_certificate_index']=indexes[id(row.pop('polynomial'))]
    records.append(dict(test=label,word=word,result=answer,seconds=time.monotonic()-start))
    save();print('RESULT',label,answer['answer'],round(records[-1]['seconds'],3),flush=True)
z=[1];t=list(m.bydegree[2][0]['word'])
if rank>=3:
    z+=[3];t+=m.bydegree[2][-1]['word']
d=list(t)
for _ in range(c-5):d=wcomm(z,d)
base=wcomm(z,d)
for k in [-1,2]:
    x=z+wpow(t,k)+rng.choice(m.bydegree[3])['word']
    y=d+wpow(rng.choice(m.bydegree[q+1])['word'],-1)+rng.choice(m.bydegree[q+2])['word']
    check(wcomm(x,y),f'constructed_positive_{k}',True)
check(wcomm(wpow(z,2),wpow(d,3)),'nonprimitive_leading_positive',True)
for i in range(2):check(base+m.bydegree[c][i]['word'],f'last_layer_perturbation_{i}')
check([], 'outside_identity',None);check([1],'outside_degree_one',None)
assert any(row['result']['answer'] is False for row in records)
if (c-5)%2==0:
    assert polynomials and any(not row['certificate']['values'] for row in polynomials)
else:assert not polynomials
faulthandler.cancel_dump_traceback_later()
print('PASS N8 iterated-adjoint groups:',rank,c,len(records),'records;',len(witnesses),
      'witnesses;',len(steps),'linear steps;',len(polynomials),'polynomials')
