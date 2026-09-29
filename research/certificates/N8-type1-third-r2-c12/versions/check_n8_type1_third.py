#!/usr/bin/env python3
"""General type1 lifting controls outside the old pure-shape families."""
import argparse,gzip,hashlib,json,random,sys,time
from pathlib import Path
from n8_type1_third import Magnus,decide_type1_third
from n8_ia_orbits import wcomm,wpow
from n8_class5 import reduced
p=argparse.ArgumentParser();p.add_argument('--rank',type=int,required=True);p.add_argument('--class-bound',type=int,required=True);p.add_argument('--directory',type=Path,required=True)
a=p.parse_args();rank=a.rank;c=a.class_bound;q=c-3;out=a.directory
assert (rank,c) in [(2,11),(2,12),(3,7)]
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
versions=out/'versions';versions.mkdir(exist_ok=True)
for name,module in list(sys.modules.items()):
 path=getattr(module,'__file__',None)
 if path and Path(path).resolve().parent==Path('scripts').resolve():
  src=Path(path);(versions/src.name).write_bytes(src.read_bytes())
(versions/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
seed=9292600+rank*10+c;rng=random.Random(seed)
print('BEGIN Magnus',rank,c,flush=True);m=Magnus(rank,c)
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,c+1)})+'\n')
records=[];witnesses=[];steps=[];polynomials=[]
def save():
 (out/'checks.json').write_text(json.dumps(dict(rank=rank,degree=c,seed=seed,records=records),indent=2)+'\n')
 (out/'polynomials.json.gz').write_bytes(gzip.compress((json.dumps(polynomials,separators=(',',':'))+'\n').encode(),mtime=0))
 (out/'fixtures.g').write_text('N8C9Witnesses := '+json.dumps(witnesses)+';\nN8C9Steps := '+json.dumps(steps).replace('true','true').replace('false','false')+';\n')
def check(word,label,expected='unspecified'):
 word=reduced(word);print('BEGIN',label,flush=True);start=time.monotonic();audit=[]
 answer=decide_type1_third(m,word,audit)
 if expected!='unspecified':assert answer['answer'] is expected,(label,answer)
 if answer['answer']:witnesses.append([rank,c,word,answer['x'],answer['y']])
 for row in audit:
  if row['kind']=='polynomial':polynomials.append(row)
  else:steps.append([rank,row['degree'],word,row['x'],row['y'],row['axes'],row['soluble']])
 indexes={id(row['certificate']):i for i,row in enumerate(polynomials)}
 for row in answer['trace']:
  if 'polynomial' in row:row['polynomial_certificate_index']=indexes[id(row.pop('polynomial'))]
 records.append(dict(test=label,word=word,result=answer,seconds=time.monotonic()-start));save()
 print('RESULT',label,answer['answer'],round(records[-1]['seconds'],3),flush=True)
 return answer
z=[1];t=list(m.bydegree[2][0]['word'])
def dz(word,n):
 for _ in range(n):word=wcomm(z,word)
 return word
if (rank,c)==(2,11):
 # Weight-eight D contains a nonzero one-letter part AND the old cubic
 # odd-adjoint part. It is outside both previously recognized pure families.
 powers=[z]
 for _ in range(3):powers.append(wcomm(t,powers[-1]))
 d=dz(t,6)
 for i in range(2):d+=wpow(wcomm(powers[i],powers[3-i]),-(-1)**i)
elif (rank,c)==(2,12):
 # Weight-nine mixed shape, with nonzero metabelian image and zero first kernel.
 d=dz(t,7)+wcomm(t,dz(t,5))
else:
 # Rank-three control: a degree-four mixed shape, including two seed directions.
 s=list(m.bydegree[2][-1]['word']);d=dz(t,2)+wcomm(t,s)
base=wcomm(z,d)
answer=check(base,'mixed_shape_positive',True)
if c==11:assert answer['trace'][-1]['first_kernel_dimension']==1
else:assert answer['trace'][-1]['first_kernel_dimension']==0
x=z+wpow(t,-2)+rng.choice(m.bydegree[3])['word']
y=d+wpow(rng.choice(m.bydegree[q+1])['word'],-1)+rng.choice(m.bydegree[q+2])['word']
check(wcomm(x,y),'corrected_positive',True)
if c==11:check(wcomm(wpow(z,2),wpow(d,-3)),'nonprimitive_signed_scale_positive',True)
check(base+m.bydegree[c][0]['word'],'last_layer_perturbation')
check(base+m.bydegree[c-1][0]['word'],'first_layer_perturbation')
if rank==2:
 other=wcomm(t,dz(t,c-6))
 check(other,'other_integral_leading_type',None)
check([],'outside_identity',None);check([1],'outside_degree_one',None)
assert any(row['result']['answer'] is False for row in records)
if c==11:
 assert polynomials and any(not row['certificate']['values'] for row in polynomials)
print('PASS N8 general type1 third-layer:',len(records),'records;',len(witnesses),'witnesses;',len(steps),'linear decisions;',len(polynomials),'polynomials',flush=True)
