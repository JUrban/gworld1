#!/usr/bin/env python3
"""All-leading-type third-layer lifting controls."""
import argparse,gzip,hashlib,json,random,sys,time
from pathlib import Path
from n8_third_layer import Magnus,decide_third_layer
from n8_ia_orbits import wcomm,wpow
from n8_class5 import reduced
p=argparse.ArgumentParser();p.add_argument('--rank',type=int,required=True);p.add_argument('--class-bound',type=int,required=True);p.add_argument('--directory',type=Path,required=True)
a=p.parse_args();rank=a.rank;c=a.class_bound;q=c-4;out=a.directory
assert (rank,c) in [(2,11),(2,10),(3,8)]
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
versions=out/'versions';versions.mkdir(exist_ok=True)
for name,module in list(sys.modules.items()):
 path=getattr(module,'__file__',None)
 if path and Path(path).resolve().parent==Path('scripts').resolve():
  src=Path(path);(versions/src.name).write_bytes(src.read_bytes())
(versions/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
seed=9292700+rank*10+c;rng=random.Random(seed)
print('BEGIN Magnus',rank,c,flush=True);m=Magnus(rank,c)
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,c+1)})+'\n')
records=[];witnesses=[];steps=[];polynomials=[];nielsen=[]
def save():
 (out/'checks.json').write_text(json.dumps(dict(rank=rank,degree=c,seed=seed,records=records),indent=2)+'\n')
 (out/'nielsen.json').write_text(json.dumps(nielsen,indent=2)+'\n')
 (out/'polynomials.json.gz').write_bytes(gzip.compress((json.dumps(polynomials,separators=(',',':'))+'\n').encode(),mtime=0))
 (out/'fixtures.g').write_text('N8C9Witnesses := '+json.dumps(witnesses)+';\nN8C9Steps := '+json.dumps(steps).replace('true','true').replace('false','false')+';\n')
def check(word,label,expected='unspecified'):
 word=reduced(word);print('BEGIN',label,flush=True);start=time.monotonic();audit=[]
 answer=decide_third_layer(m,word,audit)
 if expected!='unspecified':assert answer['answer'] is expected,(label,answer)
 if answer['answer']:witnesses.append([rank,c,word,answer['x'],answer['y']])
 for row in audit:
  if row['kind']=='polynomial':polynomials.append(row)
  elif row['kind']=='nielsen':nielsen.append(row)
  else:steps.append([rank,row['degree'],word,row['x'],row['y'],row['axes'],row['soluble']])
 indexes={id(row['certificate']):i for i,row in enumerate(polynomials)}
 for row in answer['trace']:
  if 'polynomial' in row:row['polynomial_certificate_index']=indexes[id(row.pop('polynomial'))]
 records.append(dict(test=label,word=word,result=answer,seconds=time.monotonic()-start));save()
 print('RESULT',label,answer['answer'],round(records[-1]['seconds'],3),flush=True)
 return answer
def ad(word,value,n):
 for _ in range(n):value=wcomm(word,value)
 return value
z=[1];t=list(m.bydegree[2][0]['word'])
for p0 in ([3,4] if rank==2 else [3]):
 q0=c-2-p0
 left=list(m.bydegree[p0][0]['word'])
 right=list(m.bydegree[q0][-1]['word'])
 if p0==q0:assert left!=right
 base=wcomm(left,right)
 answer=check(base,f'type{p0}_{q0}_base',True)
 assert answer['trace'][-1]['p']==p0
 expected_nullity=int(q0==p0+1)
 assert answer['trace'][-1]['first_kernel_dimension']==expected_nullity
 x=wpow(left,2)+wpow(m.bydegree[p0+1][-1]['word'],-2)+m.bydegree[p0+2][0]['word']
 y=wpow(right,-3)+m.bydegree[q0+1][0]['word']+m.bydegree[q0+2][-1]['word']
 check(wcomm(x,y),f'type{p0}_{q0}_corrected_signed_nonprimitive',True)
 check(base+m.bydegree[c][0]['word'],f'type{p0}_{q0}_final_negative',False)
 check(base+m.bydegree[c-1][0]['word'],f'type{p0}_{q0}_first_perturbation',p0==q0)
 if q0==p0+1:
  # A nonprimitive D gives multiple exact Nielsen residues.
  special=wcomm(left+wpow(right,2),wpow(right,3))
  check(special,'nielsen_period_three',True)
  check(wcomm(left,wpow(right,3))+m.bydegree[c][0]['word'],
        'nielsen_period_negative',False)
# Previously supported types exercise the shared polynomial branch.
u=wcomm(z,t)
d=ad(t,u,2) if c==11 else ad(z,t,c-6)
check(wcomm(t,d),'prior_type2_positive',True)
check(wcomm(z,ad(z,t,c-5)),'prior_type1_positive',True)
check([],'outside_identity',None);check([1],'outside_degree_one',None)
assert any(branch['p']>=3 for rec in records for branch in rec['result']['trace'])
if c==11:
 assert nielsen and max(row['period'] for row in nielsen)>=3
 assert polynomials
print('PASS N8 all third-layer:',len(records),'records;',len(witnesses),'witnesses;',
      len(steps),'linear decisions;',len(polynomials),'polynomials;',len(nielsen),'Nielsen lines',flush=True)
