#!/usr/bin/env python3
"""Candidate full class-ten algorithm; see problems/N8/class10-proof.md."""
from n8_class7 import (ONE,apply,finished,mixed_candidates,equal_candidates,
                       decide_penultimate,decide_nonzero_degree_two,first,
                       nielsen_choices,short_particular)
from n8_multigraded_magnus import Magnus
from n8_class10_tail import tail
from n8_central import bracket
from n8_sparse_polynomial_lattice import polynomial_system,differences,evaluate


from n8_class9 import period_choices,exceptional_finish
from n8_class9_linear import first
from n8_class10_completion import first_six,second_five
from n8_class10_third import decide_third

def decide_class10(m,word,audit=None):
    assert m.rank>=2 and m.degree==10
    g=m.expansion(word)
    if g==ONE:return dict(answer=True,x=[],y=[],trace=[],case='identity')
    leading=min(len(w) for w in g if w)
    if leading==1:return dict(answer=False,trace=[],case='abelian_obstruction')
    if leading==2:return decide_nonzero_degree_two(m,word)
    if leading>=8:return decide_third(m,word,audit)
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
            if p==1 and q==4:
                answer=exceptional_finish(m,g,x0,y0,q,vector,kernel,rec,audit,word)
            elif p==1 and q==6:
                answer=first_six(m,g,x0,y0,vector,kernel,rec,audit,word)
            elif leading==6:
                assert not kernel
                x,y=apply(m,x0,y0,p,q,1,vector)
                second=first(m,g,x,y,p,q,2,audit)
                if second is None:continue
                sv,sk=second;rec['second_kernel_dimension']=len(sk)
                if p==1:
                    answer=second_five(m,g,x,y,sv,sk,rec,audit,word)
                elif p==2:
                    choices=nielsen_choices(sv,sk,dd,len(m.bydegree[q+2]))
                    rec['second_period']=len(choices)
                    for residue,choice in enumerate(choices):
                        answer=tail(m,g,*apply(m,x,y,p,q,2,choice),p,q,3,audit)
                        if answer is not None:rec['selected_second_residue']=residue;break
                else:
                    assert p==q==3 and not sk
                    answer=tail(m,g,*apply(m,x,y,p,q,2,sv),p,q,3,audit)
            elif (p,q)==(2,5):
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
                    x2,y2=apply(m,x,y,p,q,2,choice)
                    third=first(m,g,x2,y2,p,q,3,audit)
                    if third is None:continue
                    assert not third[1]
                    answer=tail(m,g,*apply(m,x2,y2,p,q,3,third[0]),p,q,4,audit)
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
            if answer is not None:return finished(m,g,*answer,trace,'class10_middle')
    return dict(answer=False,trace=trace,case='all_middle_branches_failed')
