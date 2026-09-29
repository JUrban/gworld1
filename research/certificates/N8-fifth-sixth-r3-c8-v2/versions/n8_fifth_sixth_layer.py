#!/usr/bin/env python3
"""Candidate uniform decision for leading degree c-4 or c-5, at least four.

The general-offset lemmas supply the finite branch reduction. Every remaining
integral tail is retained jointly; no arbitrary quotient witness is fixed.
"""
from functools import reduce
from math import gcd
from n8_multigraded_magnus import Magnus
from n8_class6 import ONE,apply,finished
from n8_fast_particular import short_particular
from n8_central import bracket
from n8_class9_linear import first
from n8_component_linear import affine_solution
from n8_sparse_polynomial_lattice import polynomial_system,differences,evaluate
from n8_leading_pairs_hall import mixed_candidates,equal_candidates
from n8_deep_tail import tail


def columns(m,x,y,p,q,j):
    C,D=m.layer(x,p),m.layer(y,q);degree=p+q+j
    values=([bracket(m,m.layer(h['value'],p+j),D) for h in m.bydegree[p+j]]
            +[bracket(m,C,m.layer(h['value'],q+j)) for h in m.bydegree[q+j]])
    return [m.coordinates(v,degree) for v in values]


def residual(m,g,pair,degree):
    value=m.mul(m.inv(m.comm(*pair)),g)
    assert all(not 0<len(w)<degree for w in value)
    return m.coordinates(m.layer(value,degree),degree)


def decide_fifth_sixth_layer(m,word,audit=None):
    outside=dict(answer=None,case='outside_fifth_sixth_layer_scope',trace=[])
    g=m.expansion(word);c=m.degree
    if m.rank<2 or g==ONE:return outside
    d=min(len(w) for w in g if w)
    if d<4 or c-d not in (4,5):return outside
    w=m.layer(g,d);key=(d,tuple(sorted(w.items())))
    if not hasattr(m,'fifth_sixth_types_cache'):m.fifth_sixth_types_cache={}
    if key not in m.fifth_sixth_types_cache:
        types=[]
        for p in range(1,d//2+1):
            q=d-p
            entries=mixed_candidates(m,w,p,q) if p<q else equal_candidates(m,w,p)
            types.append((p,q,entries))
        m.fifth_sixth_types_cache[key]=types
    types=m.fifth_sixth_types_cache[key]
    summary=[dict(p=p,q=q,integral_pairs=len(v)) for p,q,v in types]
    trace=[]
    def emit(row):
        if audit is not None:audit.append(row)
    def metadata(x,y,p,q,j):
        return dict(rank=m.rank,p=p,q=q,offset=j,class_bound=c,
                    word=list(word),x0=m.collect(x)[0],y0=m.collect(y)[0])
    def solve(x,y,p,q,j):
        step=first(m,g,x,y,p,q,j,audit)
        if step is not None:
            emit(dict(kind='nullity',degree=d+j,dimension=len(step[1]),**metadata(x,y,p,q,j)))
        return step
    def line_pair(x,y,p,q,j,vector,direction,k):
        return apply(m,x,y,p,q,j,[a+k*b for a,b in zip(vector,direction)])
    def nielsen(x,y,p,q,j,vector,direction,record):
        assert q==p+j
        dd=m.coordinates(m.layer(y,q),q);count=len(m.bydegree[q])
        period=reduce(gcd,(abs(n) for n in dd),0)
        assert period>0 and all(n==0 for n in direction[count:])
        scaled=[period*n for n in direction[:count]]
        assert scaled==dd or scaled==[-n for n in dd]
        sign=1 if scaled==dd else -1
        record['nielsen_period']=period
        emit(dict(kind='nielsen',degree=d+j,vector=vector,kernel=direction,
                  period=period,sign=sign,**metadata(x,y,p,q,j)))
        return range(period)
    def polynomial(x,y,p,q,j,vector,direction,pair,record,extra=None):
        degree=d+2*j
        coeff=differences([residual(m,g,pair(k),degree) for k in range(3)])
        for k in (-2,-1,3):assert evaluate(coeff,k)==residual(m,g,pair(k),degree)
        system=polynomial_system(columns(m,x,y,p,q,2*j),coeff)
        assert system['mode']=='finite_points' and len(system['values'])<=2
        assert any(v[0] for v in system['certificate']['residual'][2]),'nonzero quadratic obstruction'
        record['polynomial']=system['certificate']
        emit(dict(kind='polynomial_late' if extra else 'polynomial',degree=degree,
                  vector=vector,kernel=direction,certificate=system['certificate'],
                  samples=[[k,*[m.collect(z)[0] for z in pair(k)]] for k in (-1,0,1,2,3)],
                  **metadata(x,y,p,q,j),**(extra or {})))
        return system['values']
    def second(x,y,p,q,record):
        step=solve(x,y,p,q,2);record['soluble']=step is not None
        if step is None:return None
        vector,kernel=step;record['kernel_dimension']=len(kernel)
        assert len(kernel)<=1
        if q<p+2:assert not kernel
        if q==p+2:assert len(kernel)==1
        if not kernel:return tail(m,g,*apply(m,x,y,p,q,2,vector),p,q,3,audit)
        vector=short_particular(step);direction=kernel[0]
        def pair(k):return line_pair(x,y,p,q,2,vector,direction,k)
        if q==p+2:
            record['parameter_results']=[]
            for k in nielsen(x,y,p,q,2,vector,direction,record):
                result=tail(m,g,*pair(k),p,q,3,audit)
                record['parameter_results'].append(dict(parameter=k,soluble=result is not None))
                if result is not None:return result
            return None
        assert q>p+2
        # A3 is injective. Solve it jointly with the entire offset-two line.
        coeff=differences([residual(m,g,pair(k),d+3) for k in range(2)])
        for k in (-2,-1,2,3):assert evaluate(coeff,k)==residual(m,g,pair(k),d+3)
        homogeneous=columns(m,x,y,p,q,3)
        coupled=affine_solution(homogeneous+[[-v for v in coeff[1]]],coeff[0])
        emit(dict(kind='coupled',degree=d+3,vector=vector,kernel=direction,
                  columns=homogeneous,coefficients=coeff,solution=coupled,
                  samples=[[k,*[m.collect(z)[0] for z in pair(k)]] for k in (-1,0,1,2)],
                  **metadata(x,y,p,q,2)))
        record['coupled_soluble']=coupled is not None
        if coupled is None:return None
        base,basis=coupled;assert len(basis)<=1
        base=short_particular(coupled);record['coupled_kernel_dimension']=len(basis)
        if not basis:
            lifted=apply(m,*pair(base[-1]),p,q,3,base[:-1])
            return tail(m,g,*lifted,p,q,4,audit)
        line=basis[0];assert line[-1]!=0
        record['coupled_parameter_step']=line[-1]
        def lifted(t):
            coords=[a+t*b for a,b in zip(base,line)]
            return apply(m,*pair(coords[-1]),p,q,3,coords[:-1])
        values=polynomial(x,y,p,q,2,vector,direction,lifted,record,
                          dict(coupled_base=base,coupled_direction=line))
        record['parameter_results']=[]
        for t in values:
            # Offset-four AND offset-five corrections remain jointly variable.
            result=tail(m,g,*lifted(t),p,q,4,audit)
            record['parameter_results'].append(dict(parameter=t,soluble=result is not None))
            if result is not None:return result
        return None
    for p,q,entries in types:
        for C,D in entries:
            x,y=m.lift(C,p),m.lift(D,q)
            record=dict(p=p,q=q,C=C,D=D,second_branches=[]);trace.append(record)
            step=solve(x,y,p,q,1);record['first_soluble']=step is not None
            if step is None:continue
            vector,kernel=step;record['first_kernel_dimension']=len(kernel)
            assert len(kernel)<=1
            if p==q:assert not kernel
            if q==p+1:assert len(kernel)==1
            if kernel:
                vector=short_particular(step);direction=kernel[0]
                def pair(k):return line_pair(x,y,p,q,1,vector,direction,k)
                values=(nielsen(x,y,p,q,1,vector,direction,record) if q==p+1 else
                        polynomial(x,y,p,q,1,vector,direction,pair,record))
            else:
                def pair(k):return apply(m,x,y,p,q,1,vector)
                values=[0]
            for k in values:
                branch=dict(first_parameter=k);record['second_branches'].append(branch)
                result=second(*pair(k),p,q,branch)
                branch['completed']=result is not None
                if result is not None:
                    answer=finished(m,g,*result,trace,'fifth_sixth_layer')
                    answer.update(leading_types=summary,leading_degree=d)
                    return answer
    return dict(answer=False,case='all_fifth_sixth_layer_branches_failed',trace=trace,
                leading_types=summary,leading_degree=d)
