#!/usr/bin/env python3
"""All leading types for fourth-from-last targets, arbitrary class>=7.

Candidate uniform argument: problems/N8/fourth-layer-proof.md.
Outside the target layer return None, never a false negative.
"""
from n8_iterated_adjoint import (Magnus, ONE, bracket, first, apply, finished,
    short_particular, polynomial_system, differences, evaluate)
from n8_leading_pairs_hall import mixed_candidates,equal_candidates
from n8_class10_tail import tail
from functools import reduce
from math import gcd


def decide_fourth_layer(m,word,audit=None):
    c=m.degree
    outside=dict(answer=None,case='outside_fourth_layer_scope',trace=[])
    if m.rank<2 or c<7:return outside
    g=m.expansion(word)
    if g==ONE or min(len(w) for w in g if w)!=c-3:return outside
    w=m.layer(g,c-3)
    key=tuple(sorted(w.items()))
    if not hasattr(m,"fourth_types_cache"):m.fourth_types_cache={}
    if key not in m.fourth_types_cache:
        types=[]
        for p in range(1,(c-3)//2+1):
            q=c-3-p
            entries=mixed_candidates(m,w,p,q) if p<q else equal_candidates(m,w,p)
            types.append((p,q,entries))
        m.fourth_types_cache[key]=types
    types=m.fourth_types_cache[key]
    summary=[dict(p=p,q=q0,integral_pairs=len(pairs)) for p,q0,pairs in types]
    pairs=[(p,q,cc,dd) for p,q,entries in types for cc,dd in entries];trace=[]
    def conclude(result):
        result['leading_types']=summary
        return result
    for branch,(p,q,cc,dd) in enumerate(pairs):
        assert 1<=p<=q and p+q==c-3
        x0,y0=m.lift(cc,p),m.lift(dd,q)
        step=first(m,g,x0,y0,p,q,1,audit)
        record=dict(branch=branch,p=p,q=q,C=cc,D=dd,total_branches=len(pairs),first_soluble=step is not None)
        trace.append(record)
        if step is None:continue
        vector,kernel=step
        assert len(kernel)<=1,'uniform first-kernel lemma failed'
        record['first_kernel_dimension']=len(kernel)
        if p==q:assert not kernel,'equal-weight first correction must be injective'
        if q==p+1:assert len(kernel)==1,'adjacent weights have exactly the Nielsen line'
        if not kernel:
            pair=apply(m,x0,y0,p,q,1,vector)
            last=tail(m,g,*pair,p,q,2,audit)
            record['joint_tail_soluble']=last is not None
            if last is not None:
                return conclude(finished(m,g,*last,trace,'fourth_layer'))
            continue
        vector=short_particular((vector,kernel));direction=kernel[0]
        def pair(k):return apply(m,x0,y0,p,q,1,[a+k*b for a,b in zip(vector,direction)])
        if q==p+1:
            count=len(m.bydegree[p+1])
            period=reduce(gcd,(abs(n) for n in dd),0)
            assert period>=1 and all(n==0 for n in direction[count:])
            scaled=[period*n for n in direction[:count]]
            assert scaled==dd or scaled==[-n for n in dd]
            sign=1 if scaled==dd else -1
            record['nielsen_period']=period;record['nielsen_results']=[]
            if audit is not None:
                audit.append(dict(kind='nielsen',rank=m.rank,p=p,q=q,degree=c,first_degree=c-2,
                    word=list(word),x0=m.collect(x0)[0],y0=m.collect(y0)[0],
                    vector=vector,kernel=direction,period=period,sign=sign))
            for k in range(period):
                current=pair(k)
                last=tail(m,g,*current,p,q,2,audit)
                record['nielsen_results'].append(dict(parameter=k,soluble=last is not None))
                if last is not None:
                    record['selected_parameter']=k
                    return conclude(finished(m,g,*last,trace,'fourth_layer'))
            continue
        degree=c-1
        def residual(k):
            delta=m.mul(m.inv(m.comm(*pair(k))),g)
            assert all(len(w)>=degree for w in delta if w)
            return m.coordinates(m.layer(delta,degree),degree)
        coefficients=differences([residual(k) for k in range(3)])
        for k in (-2,-1,3):assert evaluate(coefficients,k)==residual(k)
        C,D=m.layer(x0,p),m.layer(y0,q)
        columns=([bracket(m,m.layer(h['value'],p+2),D) for h in m.bydegree[p+2]]
                 +[bracket(m,C,m.layer(h['value'],q+2)) for h in m.bydegree[q+2]])
        system=polynomial_system([m.coordinates(col,degree) for col in columns],coefficients)
        assert system['mode']=='finite_points' and len(system['values'])<=2
        assert any(v[0] for v in system['certificate']['residual'][2]),'uniform quadratic obstruction failed'
        record['polynomial_degree']=degree;record['polynomial']=system['certificate']
        if audit is not None:
            audit.append(dict(kind='polynomial',rank=m.rank,p=p,q=q,degree=degree,word=list(word),
                x0=m.collect(x0)[0],y0=m.collect(y0)[0],vector=vector,kernel=direction,
                certificate=system['certificate'],
                samples=[[k,*[m.collect(z)[0] for z in pair(k)]] for k in (-1,0,1,2,3)]))
        record['parameter_tail_results']=[]
        for k in system['values']:
            # Keep the entire second-offset affine space in the joint tail.
            # A particular solution alone need not lift through the last layer.
            result=tail(m,g,*pair(k),p,q,2,audit)
            record['parameter_tail_results'].append(dict(parameter=k,soluble=result is not None))
            if result is not None:
                record['selected_parameter']=k
                return conclude(finished(m,g,*result,trace,'fourth_layer'))
    return conclude(dict(answer=False,case='all_fourth_layer_branches_failed',trace=trace))
