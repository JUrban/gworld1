#!/usr/bin/env python3
"""Uncounted candidate extension to all gamma_8 targets in class ten.

Depends on the proposed first-kernel classification in the accompanying
lead. Inputs outside gamma_8 return None rather than a negative answer.
"""
from n8_class10_nonlinear import Magnus,decide_nonlinear
from n8_penultimate import mixed_candidates,equal_candidates,decide_penultimate
from n8_class6 import ONE,apply,finished
from n8_class9_linear import first

def decide_third(m,word,audit=None):
    if m.rank<2 or m.degree!=10:
        return dict(answer=None,case='outside_class10_gamma8',trace=[])
    g=m.expansion(word)
    if any(0<len(t)<8 for t in g):
        return dict(answer=None,case='outside_class10_gamma8',trace=[])
    if g==ONE or not m.layer(g,8):
        result=decide_penultimate(m,word)
        result['delegated_penultimate']=True
        return result
    w=m.layer(g,8);trace=[]
    for p in range(1,5):
        q=8-p
        pairs=mixed_candidates(m,w,p,q) if p<q else equal_candidates(m,w,p)
        for branch,(cc,dd) in enumerate(pairs):
            x0,y0=m.lift(cc,p),m.lift(dd,q)
            step=first(m,g,x0,y0,p,q,1,audit)
            record=dict(p=p,q=q,branch=branch,total_branches=len(pairs),
                        C=cc,D=dd,first_soluble=step is not None)
            trace.append(record)
            if step is None:continue
            vector,kernel=step
            record['first_kernel_dimension']=len(kernel)
            if kernel:
                assert (p,q)==(1,7) and len(kernel)==1
                result=decide_nonlinear(m,word,audit)
                assert result['answer'] is not None,'unclassified exceptional leading pair'
                result['delegated_nonlinear']=True
                result['preceding_trace']=trace
                return result
            pair=apply(m,x0,y0,p,q,1,vector)
            last=first(m,g,*pair,p,q,2,audit)
            record['last_soluble']=last is not None
            if last is None:continue
            return finished(m,g,*apply(m,*pair,p,q,2,last[0]),trace,'class10_gamma8')
    return dict(answer=False,case='all_class10_gamma8_branches_failed',trace=trace)
