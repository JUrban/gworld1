#!/usr/bin/env python3
"""Fourth-layer checks, including a joint-tail necessity control."""
import argparse,gzip,hashlib,json,random,sys,time
from pathlib import Path
from n8_fourth_layer import Magnus,decide_fourth_layer
from n8_class9_linear import first
from n8_deep_tail import tail
from n8_class6 import apply
from n8_class7 import short_particular
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
 answer=decide_fourth_layer(m,word,audit)
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
for p0 in ([3,4] if (rank,c)==(2,11) else [2,3] if c==10 else [2]):
 q0=c-3-p0
 left=list(m.bydegree[p0][0]['word']);right=list(m.bydegree[q0][-1]['word'])
 if p0==q0:assert left!=right
 base=wcomm(left,right)
 answer=check(base,f'type{p0}_{q0}_base',True)
 assert answer['trace'][-1]['p']==p0
 assert answer['trace'][-1]['first_kernel_dimension']==int(q0==p0+1)
 x=wpow(left,2)+wpow(m.bydegree[p0+1][-1]['word'],-2)+m.bydegree[p0+2][0]['word']
 y=wpow(right,-3)+m.bydegree[q0+1][0]['word']+m.bydegree[q0+3][-1]['word']
 check(wcomm(x,y),f'type{p0}_{q0}_corrected',True)
 check(base+m.bydegree[c][0]['word'],f'type{p0}_{q0}_top_perturbation')
 check(base+m.bydegree[c-2][0]['word'],f'type{p0}_{q0}_first_perturbation')
 if q0==p0+1:
  check(wcomm(left,wpow(right,3))+m.bydegree[c][0]['word'],'nonprimitive_nielsen_perturbation')
if (rank,c)==(2,11):
 # First exceptional direction for nonlinear D of weight7.
 d=wpow(wcomm(t,ad(z,t,3)),2)+wpow(wcomm(ad(z,t,1),ad(z,t,2)),3)
elif (rank,c)==(2,10):d=ad(z,t,4)
else:d=ad(z,t,2)
q0=c-4;base=wcomm(z,d)
answer=check(base,'type1_exceptional_positive',True)
assert answer['trace'][-1]['first_kernel_dimension']==1
x=z+wpow(t,-2)+m.bydegree[3][-1]['word']
y=d+wpow(m.bydegree[q0+1][0]['word'],-1)+m.bydegree[q0+3][-1]['word']
check(wcomm(x,y),'type1_exceptional_corrected',True)
check(base+m.bydegree[c-1][0]['word'],'quadratic_layer_perturbation')
check(base+m.bydegree[c][0]['word'],'last_linear_layer_perturbation')
if (rank,c)==(2,11):
 # Offset2 has a Nielsen kernel. Its primitive direction is needed to
 # fix the last integral obstruction; retaining one representative fails.
 left=list(m.bydegree[3][0]['word']);right=list(m.bydegree[5][-1]['word'])
 yword=wpow(right,3)+m.bydegree[6][0]['word'];target=wcomm(left+right,yword)
 check(target,'joint_tail_needed_positive',True)
 x=m.expansion(left);y=m.expansion(yword);g=m.expansion(target);extra=[]
 second=first(m,g,x,y,3,5,2,extra);assert second is not None and len(second[1])==1
 naive=apply(m,x,y,3,5,2,short_particular(second))
 failed=tail(m,g,*naive,3,5,3,extra);assert failed is None,'control did not distinguish a single representative'
 full=tail(m,g,x,y,3,5,2,extra);assert full is not None
 for row in extra:steps.append([rank,row['degree'],target,row['x'],row['y'],row['axes'],row['soluble']])
 (out/'joint-tail-control.json').write_text(json.dumps(dict(word=target,x=left,y=yword,
   second_kernel=second[1],naive_soluble=False,joint_soluble=True),indent=2)+'\n');save()
check([],'outside_identity',None);check([1],'outside_degree_one',None)
assert any(row['result']['answer'] is False for row in records)
assert polynomials
print('PASS N8 all fourth-layer:',len(records),'records;',len(witnesses),'witnesses;',
      len(steps),'linear decisions;',len(polynomials),'polynomials;',len(nielsen),'Nielsen lines',flush=True)
