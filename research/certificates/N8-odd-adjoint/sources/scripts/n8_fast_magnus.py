#!/usr/bin/env python3
"""Identical truncated integer series, skipping overdegree products in bulk."""
from n8_ia_orbits import Magnus as OriginalMagnus


class Magnus(OriginalMagnus):
    def mul(self,a,b):
        buckets=[[] for _ in range(self.degree+1)]
        for v,y in b.items():
            if len(v)<=self.degree:buckets[len(v)].append((v,y))
        allowed=[];prefix=[]
        for bucket in buckets:
            prefix=prefix+bucket
            allowed.append(prefix)
        out={}
        for u,x in a.items():
            remaining=self.degree-len(u)
            if remaining<0:continue
            for v,y in allowed[remaining]:
                w=u+v;out[w]=out.get(w,0)+x*y
        return {w:c for w,c in out.items() if c}
