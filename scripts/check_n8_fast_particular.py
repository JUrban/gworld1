#!/usr/bin/env python3
"""Exact comparison with the earlier SymPy nearest-plane implementation."""
import json,random,time
from pathlib import Path
from flint import fmpz_mat
from n8_class7 import short_particular as old
from n8_fast_particular import short_particular as new
out=Path('research/certificates/N8-fast-particular');out.mkdir(parents=True,exist_ok=False)
rng=random.Random(9292801);records=[]
for n in [1,2,4,8,12,20]:
 for k in sorted({0,1,n//2,n}):
  for scale in [1,11]:
   while True:
    kernel=[[scale*rng.randrange(-5,6) for _ in range(n)] for _ in range(k)]
    if not k or fmpz_mat(kernel).rank()==k:break
   vector=[rng.randrange(-1000,1001) for _ in range(n)]
   started=time.monotonic();a=old((vector,kernel));old_time=time.monotonic()-started
   started=time.monotonic();b=new((vector,kernel));new_time=time.monotonic()-started
   assert a==b,(vector,kernel,a,b)
   records.append(dict(vector=vector,kernel=kernel,answer=b,old_seconds=old_time,new_seconds=new_time))
(out/'checks.json').write_text(json.dumps(dict(seed=9292801,records=records),indent=2)+'\n')
print('PASS N8 exact nearest-plane comparison:',len(records),'cases')
