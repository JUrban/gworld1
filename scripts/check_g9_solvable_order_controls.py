#!/usr/bin/env python3
"""Negative controls for incorrectly commuting deck translations/reflections."""
import json
from pathlib import Path
from collections import defaultdict
from g9_solvable_flows import SolvableFlows


def frozen(x):return tuple(map(frozen,x)) if isinstance(x,list) else x


class WrongTranslation(SolvableFlows):
    def translate(self,d,edges,start):
        return tuple(sorted((self.mul(d,p,start),j,c) for p,j,c in edges))


class WrongReflection(SolvableFlows):
    def reflect_edges(self,d,edges):
        result=defaultdict(int)
        for p,j,c in edges:
            p=self.reflect(d,p)
            if j==0:p=self.mul(d,self.gen(d,-1),p);c=-c
            result[(p,j)]+=c
        return self.clean(result)


out=Path('research/certificates/G9-solvable-extension/order-controls.json')
assert not out.exists()
data=json.loads(out.with_name('checks.json').read_text());results=[]
for broken in [WrongTranslation,WrongReflection]:
    failures=[]
    for record in data['gap_fixtures']:
        rank,depth,w,u,spans,g,h=frozen(record)
        group=broken(rank)
        if group.decode(depth,h,spans)!=g:
            failures.append(dict(rank=rank,depth=depth,word=w,unfolded=u,spans=spans))
        for method in ['zero','gen','mul','inv','reflect','word']:getattr(group,method).cache_clear()
    assert failures,(broken.__name__,'negative controls failed to expose wrong order')
    results.append(dict(broken_formula=broken.__name__,detected=len(failures),witness=failures[0]))
out.write_text(json.dumps(results,indent=2)+'\n')
print([(r['broken_formula'],r['detected']) for r in results])
print('PASS G9 NONCOMMUTATIVE ORDER CONTROLS')
