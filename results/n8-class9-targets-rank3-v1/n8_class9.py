#!/usr/bin/env python3
"""Candidate class-nine algorithm; see problems/N8/class9-proof.md."""
from n8_class7 import (ONE,apply,finished,mixed_candidates,equal_candidates,
                       decide_penultimate,decide_nonzero_degree_two,first,
                       nielsen_choices,short_particular)
from n8_multigraded_magnus import Magnus
from n8_class8_tail import tail
from n8_central import bracket
from n8_polynomial_lattice import polynomial_system,differences,evaluate


def period_choices(vector,kernel,gauge):
    """All residues along the full integral kernel under an exact gauge."""
    assert len(kernel)==1
    direction=kernel[0]
    pivot=next(i for i,n in enumerate(direction) if n)
    assert gauge[pivot]%direction[pivot]==0
    period=gauge[pivot]//direction[pivot]
    assert period and all(a==period*b for a,b in zip(gauge,direction))
    vector=short_particular((vector,kernel))
    return [[a+k*b for a,b in zip(vector,direction)] for k in range(abs(period))]


def exceptional_finish(m,g,x0,y0,q,vector,kernel,record,audit,target_word):
    assert q in (4,6) and len(kernel)<=1
    if not kernel:
        x,y=apply(m,x0,y0,1,q,1,vector)
        if q==6:return tail(m,g,x,y,1,q,2,audit)
        second=first(m,g,x,y,1,q,2,audit)
        if second is None:return None
        assert not second[1]
        return tail(m,g,*apply(m,x,y,1,q,2,second[0]),1,q,3,audit)
    vector=short_particular((vector,kernel));direction=kernel[0]
    degree=q+3
    def pair(k):
        return apply(m,x0,y0,1,q,1,[a+k*b for a,b in zip(vector,direction)])
    def residual(k):
        delta=m.mul(m.inv(m.comm(*pair(k))),g)
        assert all(len(w)>=degree for w in delta if w)
        return m.coordinates(m.layer(delta,degree),degree)
    coefficients=differences([residual(k) for k in range(3)])
    for k in [-2,-1,3]:assert evaluate(coefficients,k)==residual(k)
    c=m.layer(x0,1);d=m.layer(y0,q)
    columns=([bracket(m,m.layer(h['value'],3),d) for h in m.bydegree[3]]
             +[bracket(m,c,m.layer(h['value'],q+2)) for h in m.bydegree[q+2]])
    coordinates=[m.coordinates(col,degree) for col in columns]
    system=polynomial_system(coordinates,coefficients)
    if q==4:assert not system['kernel']
    assert system['mode']=='finite_points' and len(system['values'])<=2
    record['polynomial_degree']=degree
    record['polynomial']=system['certificate']
    if audit is not None:
        audit.append(dict(kind='polynomial',rank=m.rank,q=q,degree=degree,
                          word=list(target_word),x0=m.collect(x0)[0],y0=m.collect(y0)[0],
                          vector=vector,kernel=direction,certificate=system['certificate'],
                          samples=[[k,*[m.collect(z)[0] for z in pair(k)]]
                                   for k in [-1,0,1,2,3]]))
    for k in system['values']:
        correction=evaluate(system['particular'],k)
        assert all(v.denominator==1 for v in correction)
        corrected=apply(m,*pair(k),1,q,2,list(map(int,correction)))
        if q==6:
            assert m.comm(*corrected)==g
            record['selected_parameter']=k
            return corrected
        answer=tail(m,g,*corrected,1,q,3,audit)
        if answer is not None:
            record['selected_parameter']=k
            return answer
    return None


def decide_class9(m,word,audit=None):
    assert m.rank>=2 and m.degree==9
    g=m.expansion(word)
    if g==ONE:return dict(answer=True,x=[],y=[],trace=[],case='identity')
    leading=min(len(w) for w in g if w)
    if leading==1:return dict(answer=False,trace=[],case='abelian_obstruction')
    if leading==2:return decide_nonzero_degree_two(m,word)
    if leading>=8:return decide_penultimate(m,word)
    trace=[];w=m.layer(g,leading)
    for p in range(1,leading//2+1):
        q=leading-p
        pairs=mixed_candidates(m,w,p,q) if p<q else equal_candidates(m,w,p)
        for branch,(cc,dd) in enumerate(pairs):
            x0,y0=m.lift(cc,p),m.lift(dd,q)
            step=first(m,g,x0,y0,p,q,1,audit)
            rec=dict(p=p,q=q,branch=branch,C=cc,D=dd,first_soluble=step is not None)
            trace.append(rec)
            if step is None:continue
            vector,kernel=step;rec['first_kernel_dimension']=len(kernel)
            answer=None
            if p==1 and q in (4,6):
                answer=exceptional_finish(m,g,x0,y0,q,vector,kernel,rec,audit,word)
            elif leading==6 or (p,q)==(2,5):
                assert not kernel
                answer=tail(m,g,*apply(m,x0,y0,p,q,1,vector),p,q,2,audit)
            elif (p,q)==(3,4):
                choices=nielsen_choices(vector,kernel,dd,len(m.bydegree[q+1]))
                rec['first_period']=len(choices)
                for residue,choice in enumerate(choices):
                    answer=tail(m,g,*apply(m,x0,y0,p,q,1,choice),p,q,2,audit)
                    if answer is not None:
                        rec['selected_residue']=residue;break
            elif leading==4:
                assert not kernel
                x,y=apply(m,x0,y0,p,q,1,vector)
                second=first(m,g,x,y,p,q,2,audit)
                if second is None:continue
                sv,sk=second
                if p==1:choices=nielsen_choices(sv,sk,dd,len(m.bydegree[q+2]))
                else:
                    assert not sk
                    choices=[sv]
                rec['second_period']=len(choices)
                for residue,choice in enumerate(choices):
                    answer=tail(m,g,*apply(m,x,y,p,q,2,choice),p,q,3,audit)
                    if answer is not None:
                        rec['selected_residue']=residue;break
            else:
                assert (p,q) in ((1,2),(2,3))
                choices=nielsen_choices(vector,kernel,dd,len(m.bydegree[q+1]))
                rec['first_period']=len(choices);rec['later_branches']=[]
                for residue,choice in enumerate(choices):
                    x,y=apply(m,x0,y0,p,q,1,choice)
                    second=first(m,g,x,y,p,q,2,audit)
                    if second is None:continue
                    assert not second[1]
                    x,y=apply(m,x,y,p,q,2,second[0])
                    if p==2:
                        answer=tail(m,g,x,y,p,q,3,audit)
                    else:
                        third=first(m,g,x,y,p,q,3,audit)
                        if third is None:continue
                        c=m.layer(x0,1);d=m.layer(y0,2);cd=bracket(m,c,d)
                        gauge=(m.coordinates(bracket(m,c,cd),4)
                               +m.coordinates(bracket(m,d,cd),5))
                        residues=period_choices(*third,gauge)
                        gauge_record=dict(first_residue=residue,third_period=len(residues))
                        rec['later_branches'].append(gauge_record)
                        for third_residue,third_choice in enumerate(residues):
                            answer=tail(m,g,*apply(m,x,y,p,q,3,third_choice),p,q,4,audit)
                            if answer is not None:
                                gauge_record['selected_third_residue']=third_residue;break
                    if answer is not None:
                        rec['selected_residue']=residue;break
            if answer is not None:return finished(m,g,*answer,trace,'class9_middle')
    return dict(answer=False,trace=trace,case='all_middle_branches_failed')
