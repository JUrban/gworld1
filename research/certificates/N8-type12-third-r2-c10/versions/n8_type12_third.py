#!/usr/bin/env python3
"""All leading types with p<=2 for third-from-last targets, arbitrary class>=8.

Full decisions only when no normalized integral leading pair has another type.
Return None for other leading types/outside layers, never a false negative.
See research/notes/N8-type2-first-kernel-lead.md for the extra type-two argument.
"""
from n8_iterated_adjoint import (Magnus, ONE, bracket, first, apply, finished,
    short_particular, polynomial_system, differences, evaluate)
from n8_type1_third import leading_types


def decide_type12_third(m,word,audit=None):
    c=m.degree
    outside=dict(answer=None,case='outside_type12_third_scope',trace=[])
    if m.rank<2 or c<8:return outside
    g=m.expansion(word)
    if g==ONE or min(len(w) for w in g if w)!=c-2:return outside
    types=leading_types(m,m.layer(g,c-2))
    summary=[dict(p=p,q=q0,integral_pairs=len(pairs)) for p,q0,pairs in types]
    if any(p>2 and pairs for p,q0,pairs in types):
        outside.update(case='other_integral_leading_type',leading_types=summary)
        return outside
    pairs=[(p,q,cc,dd) for p,q,entries in types for cc,dd in entries];trace=[]
    def conclude(result):
        result['leading_types']=summary
        return result
    for branch,(p,q,cc,dd) in enumerate(pairs):
        assert p in (1,2) and q>p+1
        x0,y0=m.lift(cc,p),m.lift(dd,q)
        step=first(m,g,x0,y0,p,q,1,audit)
        record=dict(branch=branch,p=p,q=q,C=cc,D=dd,total_branches=len(pairs),first_soluble=step is not None)
        trace.append(record)
        if step is None:continue
        vector,kernel=step
        assert len(kernel)<=1,'uniform first-kernel lemma failed'
        record['first_kernel_dimension']=len(kernel)
        if not kernel:
            pair=apply(m,x0,y0,p,q,1,vector)
            last=first(m,g,*pair,p,q,2,audit)
            record['last_soluble']=last is not None
            if last is not None:
                return conclude(finished(m,g,*apply(m,*pair,p,q,2,last[0]),trace,'type12_third'))
            continue
        vector=short_particular((vector,kernel));direction=kernel[0]
        def pair(k):return apply(m,x0,y0,p,q,1,[a+k*b for a,b in zip(vector,direction)])
        def residual(k):
            delta=m.mul(m.inv(m.comm(*pair(k))),g)
            assert all(len(w)>=c for w in delta if w)
            return m.coordinates(m.layer(delta,c),c)
        coefficients=differences([residual(k) for k in range(3)])
        for k in (-2,-1,3):assert evaluate(coefficients,k)==residual(k)
        C,D=m.layer(x0,p),m.layer(y0,q)
        columns=([bracket(m,m.layer(h['value'],p+2),D) for h in m.bydegree[p+2]]
                 +[bracket(m,C,m.layer(h['value'],q+2)) for h in m.bydegree[q+2]])
        system=polynomial_system([m.coordinates(col,c) for col in columns],coefficients)
        assert system['mode']=='finite_points' and len(system['values'])<=2
        assert any(v[0] for v in system['certificate']['residual'][2]),'uniform quadratic obstruction failed'
        record['polynomial_degree']=c;record['polynomial']=system['certificate']
        if audit is not None:
            audit.append(dict(kind='polynomial',rank=m.rank,p=p,q=q,degree=c,word=list(word),
                x0=m.collect(x0)[0],y0=m.collect(y0)[0],vector=vector,kernel=direction,
                certificate=system['certificate'],
                samples=[[k,*[m.collect(z)[0] for z in pair(k)]] for k in (-1,0,1,2,3)]))
        for k in system['values']:
            correction=evaluate(system['particular'],k)
            assert all(v.denominator==1 for v in correction)
            result=apply(m,*pair(k),p,q,2,list(map(int,correction)))
            record['selected_parameter']=k
            return conclude(finished(m,g,*result,trace,'type12_third'))
    return conclude(dict(answer=False,case='all_type12_third_branches_failed',trace=trace))
