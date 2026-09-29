#!/usr/bin/env python3
"""Targeted coupled-point/integrality controls, rank two and class eleven."""
import argparse,gzip,json,sys,time
from pathlib import Path
from n8_fifth_sixth_layer import Magnus,decide_fifth_sixth_layer
from n8_ia_orbits import wcomm,wpow
from n8_class5 import reduced
p=argparse.ArgumentParser();p.add_argument('--rank',type=int,required=True)
p.add_argument('--class-bound',type=int,required=True);p.add_argument('--directory',type=Path,required=True)
p.add_argument('--case',choices=['points','nonunit'],default='points')
a=p.parse_args();rank=a.rank;c=a.class_bound;out=a.directory
assert (rank,c)==(2,11)
out.mkdir(parents=True,exist_ok=True);assert not (out/'checks.json').exists()
versions=out/'versions';versions.mkdir(exist_ok=True)
for name,module in list(sys.modules.items()):
 path=getattr(module,'__file__',None)
 if path and Path(path).resolve().parent==Path('scripts').resolve():
  src=Path(path);(versions/src.name).write_bytes(src.read_bytes())
(versions/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
print('BEGIN Magnus',rank,c,flush=True);m=Magnus(rank,c)
(out/'halls.json').write_text(json.dumps({str(d):[h['word'] for h in m.bydegree[d]] for d in range(1,c+1)})+'\n')
records=[];witnesses=[];audit_all=[];polynomials=[]
def save():
 (out/'checks.json').write_text(json.dumps(dict(rank=rank,degree=c,records=records),indent=2)+'\n')
 (out/'audit.json.gz').write_bytes(gzip.compress((json.dumps(audit_all,separators=(',',':'))+'\n').encode(),mtime=0))
 (out/'witnesses.json').write_text(json.dumps(witnesses)+'\n')
def trim(value):
 if isinstance(value,list):return [trim(v) for v in value]
 if isinstance(value,dict):
  return {('polynomial_certificate_index' if k=='polynomial' else k):
          (next(i for i,v in enumerate(polynomials) if v is x) if k=='polynomial' else trim(x))
          for k,x in value.items()}
 return value
def check(word,label,expected='unspecified'):
 word=reduced(word);print('BEGIN',label,flush=True);started=time.monotonic();audit=[]
 result=decide_fifth_sixth_layer(m,word,audit)
 if expected!='unspecified':assert result['answer'] is expected,(label,result)
 if result['answer']:witnesses.append([rank,c,word,result['x'],result['y']])
 for row in audit:
  row.setdefault('rank',rank);row.setdefault('word',word)
  if row['kind'].startswith('polynomial'):polynomials.append(row['certificate'])
 audit_all.extend(audit)
 records.append(dict(test=label,word=word,result=trim(result),seconds=time.monotonic()-started));save()
 print('RESULT',label,result['answer'],round(records[-1]['seconds'],3),flush=True)
 return result
def ad(z,t,n):
 for _ in range(n):t=wcomm(z,t)
 return t
def family(left,right,p,q,label):
 base=wcomm(left,right)
 check(base,label+'_base',True)
 x=wpow(left,2)+wpow(m.bydegree[p+1][-1]['word'],-2)+m.bydegree[p+2][0]['word']
 y=wpow(right,-3)+m.bydegree[q+1][0]['word']+m.bydegree[q+4][-1]['word']
 check(wcomm(x,y),label+'_corrected',True)
 check(base+m.bydegree[c][0]['word'],label+'_top_perturbation')
 check(base+m.bydegree[p+q+1][0]['word'],label+'_first_perturbation')
 if rank==3 and p==q==2:
  # A nonzero metabelian top term cannot be a commutator of two
  # gamma_2 elements; its leading degree-four pair list has only (2,2).
  negative=check(base+ad([3],[2],c-1),label+'_metabelian_top_negative',False)
  assert all(t['p']==2 or t['integral_pairs']==0 for t in negative['leading_types'])
 if q-p in (1,2):
  check(wcomm(left,wpow(right,3))+m.bydegree[c][0]['word'],label+'_nonprimitive_nielsen')
z=[1];t=m.bydegree[2][0]['word'];u=ad(z,t,1);d=ad(z,u,2)
if a.case=='points':
 for sx,sy,fx,fy in [(1,1,1,0),(1,1,0,1),(2,3,1,0),(2,3,0,1),(2,3,1,1),(3,2,1,1)]:
  x=wpow(z,sx)+wpow(t,fx)+wpow(u,2)
  y=wpow(d,sy)+wpow(m.bydegree[6][-1]['word'],fy)+m.bydegree[9][-1]['word']
  check(wcomm(x,y),f'coupled_scales{sx}_{sy}_first{fx}_{fy}',True)
else:
 # The derivative first correction of y makes r1 rationally liftable,
 # while coprime leading scales impose a nontrivial integral parameter step.
 x=wpow(z,2)+wpow(u,2)
 y=wpow(d,3)+ad(z,d,1)+m.bydegree[9][-1]['word']
 check(wcomm(x,y),'coupled_nonunit_derivative_correction',True)
from collections import Counter
counts=Counter(row['kind'] for row in audit_all)
points=[r for r in audit_all if r['kind']=='coupled' and r['solution'] is not None and not r['solution'][1]]
nonunit=[r for r in audit_all if r['kind']=='coupled' and r['solution'] is not None and r['solution'][1] and abs(r['solution'][1][0][-1])>1]
if a.case=='points':assert points,'No point branch exercised'
else:assert nonunit,'No nonunit parameter step exercised'
print('PASS N8 coupled lifts:',len(records),'records;',len(points),'points;',len(nonunit),'nonunit steps;',dict(counts),flush=True)
