#!/usr/bin/env python3
"""Class-six commutator algorithm; new middle layers use injective corrections."""
from n8_penultimate import (Magnus, decide_penultimate, mixed_candidates,
                            equal_candidates, lie_tensor)
from n8_central import bracket, linear_solution
from n8_ia_orbits import ONE, decide_nonzero_degree_two


def correction(m,g,x,y,p,q,j,audit=None):
    degree=p+q+j
    residual=m.mul(m.inv(m.comm(x,y)),g)
    assert all(not (0<len(w)<degree) for w in residual)
    c,d=m.layer(x,p),m.layer(y,q)
    columns=([bracket(m,m.layer(h['value'],p+j),d) for h in m.bydegree[p+j]]
             +[bracket(m,c,m.layer(h['value'],q+j)) for h in m.bydegree[q+j]])
    result=linear_solution(columns,m.layer(residual,degree))
    if audit is not None:
        audit.append([degree,m.collect(x)[0],m.collect(y)[0],
                      [h['word'] for h in m.bydegree[p+j]],
                      [h['word'] for h in m.bydegree[q+j]],result is not None])
    return result


def apply(m,x,y,p,q,j,vector):
    cut=len(m.bydegree[p+j])
    return (m.mul(x,m.lift(vector[:cut],p+j)),
            m.mul(y,m.lift(vector[cut:],q+j)))


def finished(m,g,x,y,trace,case):
    assert m.comm(x,y)==g
    return dict(answer=True,x=m.collect(x)[0],y=m.collect(y)[0],trace=trace,case=case)


def decide_class6(m,word,audit=None):
    assert m.degree==6
    g=m.expansion(word)
    if g==ONE:
        return dict(answer=True,x=[],y=[],trace=[],case='identity')
    leading=min(len(w) for w in g if w)
    if leading==1:
        return dict(answer=False,trace=[],case='abelian_obstruction')
    if leading==2:
        result=decide_nonzero_degree_two(m,word)
        result['class6_delegate']='independent_abelianization'
        return result
    if leading>=5:
        result=decide_penultimate(m,word)
        result['class6_delegate']='penultimate_or_central'
        return result
    trace=[]
    w=m.layer(g,leading)
    for p in range(1,leading//2+1):
        q=leading-p
        pairs=mixed_candidates(m,w,p,q) if p<q else equal_candidates(m,w,p)
        for branch,(cc,dd) in enumerate(pairs):
            x0,y0=m.lift(cc,p),m.lift(dd,q)
            first=correction(m,g,x0,y0,p,q,1,audit)
            record=dict(p=p,q=q,branch=branch,C=cc,D=dd,
                        degree=leading+1,soluble=first is not None)
            trace.append(record)
            if first is None:
                continue
            vector,kernel=first
            record['kernel_dimension']=len(kernel)
            if leading==4:
                assert not kernel,'new degree-five injectivity lemma failed'
                x1,y1=apply(m,x0,y0,p,q,1,vector)
                last=correction(m,g,x1,y1,p,q,2,audit)
                record['last_soluble']=last is not None
                if last is not None:
                    x2,y2=apply(m,x1,y1,p,q,2,last[0])
                    return finished(m,g,x2,y2,trace,'leading_degree_four')
                continue
            assert leading==3 and p==1 and q==2
            assert len(kernel)==1,'known degree-four kernel must have rank one'
            primitive=kernel[0]
            gauge=dd+[0]*len(m.bydegree[3])
            pivot=next(i for i,n in enumerate(primitive) if n)
            assert gauge[pivot]%primitive[pivot]==0
            period=gauge[pivot]//primitive[pivot]
            assert period and all(a==period*b for a,b in zip(gauge,primitive))
            record['period']=abs(period)
            record['residues']=[]
            for residue in range(abs(period)):
                choice=[a+residue*b for a,b in zip(vector,primitive)]
                x1,y1=apply(m,x0,y0,p,q,1,choice)
                second=correction(m,g,x1,y1,p,q,2,audit)
                step=dict(residue=residue,degree_five_soluble=second is not None)
                record['residues'].append(step)
                if second is None:
                    continue
                assert not second[1],'new (1,2) second-correction kernel lemma failed'
                x2,y2=apply(m,x1,y1,p,q,2,second[0])
                last=correction(m,g,x2,y2,p,q,3,audit)
                step['degree_six_soluble']=last is not None
                if last is not None:
                    x3,y3=apply(m,x2,y2,p,q,3,last[0])
                    return finished(m,g,x3,y3,trace,'leading_degree_three')
    return dict(answer=False,trace=trace,case='all_middle_branches_failed')
