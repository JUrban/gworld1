#!/usr/bin/env python3
"""New exceptional lifts for the proposed full class-ten algorithm.

The proposed proof is research/notes/N8-class10-kernel-proof.md.
This module does not establish the all-rank lemmas by computation.
"""
from n8_class9 import apply,short_particular,bracket,differences,evaluate,polynomial_system,tail
from n8_class9_linear import first
from n8_component_linear import affine_solution

def columns(m,x,y,p,q,j):
    c=m.layer(x,p);d=m.layer(y,q);degree=p+q+j
    values=([bracket(m,m.layer(h['value'],p+j),d) for h in m.bydegree[p+j]]
            +[bracket(m,c,m.layer(h['value'],q+j)) for h in m.bydegree[q+j]])
    return [m.coordinates(v,degree) for v in values]

def residual(m,g,pair,degree):
    value=m.mul(m.inv(m.comm(*pair)),g)
    assert all(not 0<len(w)<degree for w in value)
    return m.coordinates(m.layer(value,degree),degree)

def first_six(m,g,x,y,vector,kernel,record,audit,word):
    """Old degree-nine obstruction, followed by the FULL class-ten tail."""
    if not kernel:return tail(m,g,*apply(m,x,y,1,6,1,vector),1,6,2,audit)
    assert len(kernel)==1
    vector=short_particular((vector,kernel));direction=kernel[0]
    def pair(k):return apply(m,x,y,1,6,1,[a+k*b for a,b in zip(vector,direction)])
    coeff=differences([residual(m,g,pair(k),9) for k in range(3)])
    for k in [-2,-1,3]:assert evaluate(coeff,k)==residual(m,g,pair(k),9)
    system=polynomial_system(columns(m,x,y,1,6,2),coeff)
    assert system['mode']=='finite_points' and len(system['values'])<=2
    record['polynomial_degree']=9;record['polynomial']=system['certificate']
    if audit is not None:
        audit.append(dict(kind='polynomial',rank=m.rank,q=6,degree=9,word=list(word),
                          x0=m.collect(x)[0],y0=m.collect(y)[0],vector=vector,kernel=direction,
                          certificate=system['certificate'],samples=[[k,*[m.collect(v)[0] for v in pair(k)]]
                                                                    for k in [-1,0,1,2,3]]))
    for k in system['values']:
        result=tail(m,g,*pair(k),1,6,2,audit)
        if result is not None:record['selected_parameter']=k;return result
    return None

def second_five(m,g,x,y,vector,kernel,record,audit,word):
    """One coupled integer system, then at most two final-layer parameters."""
    if not kernel:return tail(m,g,*apply(m,x,y,1,5,2,vector),1,5,3,audit)
    assert len(kernel)==1
    vector=short_particular((vector,kernel));direction=kernel[0]
    def pair(k):return apply(m,x,y,1,5,2,[a+k*b for a,b in zip(vector,direction)])
    coeff=differences([residual(m,g,pair(k),9) for k in range(2)])
    for k in [-2,-1,2,3]:assert evaluate(coeff,k)==residual(m,g,pair(k),9)
    homogeneous=columns(m,x,y,1,5,3)
    augmented=homogeneous+[[-v for v in coeff[1]]]
    coupled=affine_solution(augmented,coeff[0])
    record['coupled_soluble']=coupled is not None
    if audit is not None:
        audit.append(dict(kind='coupled',rank=m.rank,q=5,degree=9,word=list(word),
                          x0=m.collect(x)[0],y0=m.collect(y)[0],vector=vector,kernel=direction,
                          columns=homogeneous,coefficients=coeff,solution=coupled,
                          samples=[[k,*[m.collect(v)[0] for v in pair(k)]] for k in [-1,0,1,2]]))
    if coupled is None:return None
    base,basis=coupled
    assert len(basis)<=1
    base=short_particular((base,basis))
    record['coupled_kernel_dimension']=len(basis)
    if not basis:
        lifted=apply(m,*pair(base[-1]),1,5,3,base[:-1])
        final=first(m,g,*lifted,1,5,4,audit)
        if final is None:return None
        result=apply(m,*lifted,1,5,4,final[0]);assert m.comm(*result)==g
        record['selected_parameter']=base[-1]
        return result
    line=basis[0];assert line[-1]!=0
    def lifted(t):
        v=[a+t*b for a,b in zip(base,line)]
        return apply(m,*pair(v[-1]),1,5,3,v[:-1])
    coeff10=differences([residual(m,g,lifted(t),10) for t in range(3)])
    for t in [-2,-1,3]:assert evaluate(coeff10,t)==residual(m,g,lifted(t),10)
    system=polynomial_system(columns(m,x,y,1,5,4),coeff10)
    assert system['mode']=='finite_points' and len(system['values'])<=2
    assert any(v[0] for v in system['certificate']['residual'][2])
    record['polynomial_degree']=10;record['polynomial']=system['certificate']
    if audit is not None:
        audit.append(dict(kind='polynomial_late',rank=m.rank,q=5,degree=10,word=list(word),
                          x0=m.collect(x)[0],y0=m.collect(y)[0],vector=vector,kernel=direction,
                          coupled_base=base,coupled_direction=line,
                          certificate=system['certificate'],
                          samples=[[t,*[m.collect(v)[0] for v in lifted(t)]] for t in [-1,0,1,2,3]]))
    for t in system['values']:
        final=evaluate(system['particular'],t)
        assert all(v.denominator==1 for v in final)
        result=apply(m,*lifted(t),1,5,4,list(map(int,final)))
        assert m.comm(*result)==g
        record['selected_parameter']=base[-1]+t*line[-1]
        record['selected_final_parameter']=t
        return result
    return None
