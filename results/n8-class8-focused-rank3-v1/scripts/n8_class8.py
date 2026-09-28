#!/usr/bin/env python3
"""Candidate all-rank class-eight algorithm; see problems/N8/class8-proof.md."""
from n8_class7 import (Magnus,ONE,apply,finished,mixed_candidates,equal_candidates,
                       decide_penultimate,decide_nonzero_degree_two,first,tail,
                       nielsen_choices,short_particular,tail_axes,tail_columns)
from n8_central import bracket
from n8_polynomial_lattice import polynomial_system,differences,evaluate


def polynomial_finish(m,g,x0,y0,vector,kernel,record,audit):
    assert len(kernel)<=1
    if not kernel:
        return tail(m,g,*apply(m,x0,y0,1,4,1,vector),1,4,2,audit)
    direction=kernel[0]
    def pair(k):
        return apply(m,x0,y0,1,4,1,[a+k*b for a,b in zip(vector,direction)])
    def degree7(k):
        delta=m.mul(m.inv(m.comm(*pair(k))),g)
        assert all(len(w)>=7 for w in delta if w)
        return m.coordinates(m.layer(delta,7),7)
    coeff7=differences([degree7(k) for k in range(3)])
    for k in [-2,-1,3]:assert evaluate(coeff7,k)==degree7(k)
    c=m.layer(x0,1);d=m.layer(y0,4)
    columns7=[bracket(m,m.layer(h['value'],3),d) for h in m.bydegree[3]]
    columns7 += [bracket(m,c,m.layer(h['value'],6)) for h in m.bydegree[6]]
    coordinates7=[m.coordinates(col,7) for col in columns7]
    system=polynomial_system(coordinates7,coeff7)
    assert not system['kernel']  # proved injectivity, not a numerical assumption
    record['degree7_polynomial']=system['certificate']
    if audit is not None:
        audit.append(dict(kind='polynomial7',rank=m.rank,word=m.collect(g)[0],
                          x0=m.collect(x0)[0],y0=m.collect(y0)[0],vector=vector,
                          kernel=direction,certificate=system['certificate'],
                          samples=[[k,*[m.collect(z)[0] for z in pair(k)]] for k in [-1,0,1,2,3]]))
    # The quadratic coefficient is outside the rational correction image;
    # the proof therefore gives finitely many roots, never a progression.
    assert system['mode']=='finite_points'
    assert len(system['values'])<=2
    for k in system['values']:
        v=evaluate(system['particular'],k)
        assert all(x.denominator==1 for x in v)
        corrected=apply(m,*pair(k),1,4,2,list(map(int,v)))
        answer=tail(m,g,*corrected,1,4,3,audit)
        if answer is not None:
            record['selected_parameter']=k
            return answer
    return None


def decide_class8(m,word,audit=None):
    assert m.rank>=2 and m.degree==8
    g=m.expansion(word)
    if g==ONE:return dict(answer=True,x=[],y=[],trace=[],case='identity')
    leading=min(len(w) for w in g if w)
    if leading==1:return dict(answer=False,trace=[],case='abelian_obstruction')
    if leading==2:return decide_nonzero_degree_two(m,word)
    if leading>=7:return decide_penultimate(m,word)
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
            vector,kernel=step;rec['kernel_dimension']=len(kernel)
            answer=None
            if (p,q)==(1,4):
                answer=polynomial_finish(m,g,x0,y0,vector,kernel,rec,audit)
            elif leading==6:
                assert not kernel
                answer=tail(m,g,*apply(m,x0,y0,p,q,1,vector),p,q,2,audit)
            elif leading==4:
                assert not kernel
                x,y=apply(m,x0,y0,p,q,1,vector)
                second=first(m,g,x,y,p,q,2,audit)
                if second is None:continue
                sv,sk=second
                if p==1:
                    choices=nielsen_choices(sv,sk,dd,len(m.bydegree[q+2]))
                else:
                    assert not sk
                    choices=[sv]
                rec['second_period']=len(choices)
                for residue,choice in enumerate(choices):
                    answer=tail(m,g,*apply(m,x,y,p,q,2,choice),p,q,3,audit)
                    if answer is not None:
                        rec['selected_residue']=residue;break
            else:
                assert (p,q) in [(1,2),(2,3)]
                choices=nielsen_choices(vector,kernel,dd,len(m.bydegree[q+1]))
                rec['period']=len(choices)
                for residue,choice in enumerate(choices):
                    x,y=apply(m,x0,y0,p,q,1,choice)
                    if leading==3:
                        second=first(m,g,x,y,p,q,2,audit)
                        if second is None:continue
                        assert not second[1]
                        x,y=apply(m,x,y,p,q,2,second[0])
                    answer=tail(m,g,x,y,p,q,3 if leading==3 else 2,audit)
                    if answer is not None:
                        rec['selected_residue']=residue;break
            if answer is not None:return finished(m,g,*answer,trace,'class8_middle')
    return dict(answer=False,trace=trace,case='all_middle_branches_failed')
