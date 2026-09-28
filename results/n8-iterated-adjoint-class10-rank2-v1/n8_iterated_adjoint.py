#!/usr/bin/env python3
"""Candidate N8 algorithm for the iterated-adjoint third-from-last stratum.

Outside the proved scope the answer is None, never a negative decision.
All finite leading scales and all integral affine solutions are retained.
"""
from sympy import Matrix, Rational
from n8_multigraded_magnus import Magnus
from n8_penultimate import mixed_candidates, lie_tensor
from n8_central import bracket
from n8_class6 import ONE, apply, finished
from n8_class7 import short_particular
from n8_class9_linear import first
from n8_sparse_polynomial_lattice import polynomial_system, differences, evaluate


def adjoint(m,z,t,n):
    for _ in range(n):t=bracket(m,z,t)
    return t


def recognize(m,c,d,q):
    """Unique rational T with D=ad_C^(q-2)(T), if it exists."""
    columns=[adjoint(m,c,m.layer(h['value'],2),q-2) for h in m.bydegree[2]]
    matrix=Matrix([m.coordinates(col,q) for col in columns]).T
    try:vector,parameters=matrix.gauss_jordan_solve(Matrix(m.coordinates(d,q)))
    except ValueError:return None
    assert parameters.rows==0 and any(vector)
    t=lie_tensor(m,list(vector),2)
    assert adjoint(m,c,t,q-2)==d
    return [[int(v.p),int(v.q)] for v in vector]


def decide_iterated_adjoint(m,word,audit=None):
    assert m.rank>=2 and m.degree>=6
    g=m.expansion(word);c=m.degree;q=c-3;n=c-5
    outside=dict(answer=None,case='outside_iterated_adjoint_scope',trace=[])
    if g==ONE or min(len(w) for w in g if w)!=c-2:return outside
    leading=m.layer(g,c-2)
    pairs=mixed_candidates(m,leading,1,q)
    if not pairs:return outside
    recognized=[]
    for cc,dd in pairs:
        z=lie_tensor(m,cc,1);d=lie_tensor(m,dd,q)
        recognized.append(recognize(m,z,d,q))
    if not any(t is not None for t in recognized):return outside
    # The unique degree-one direction lemma implies all remaining scales qualify.
    assert all(t is not None for t in recognized)
    trace=[]
    for branch,((cc,dd),t) in enumerate(zip(pairs,recognized)):
        x0,y0=m.lift(cc,1),m.lift(dd,q)
        step=first(m,g,x0,y0,1,q,1,audit)
        record=dict(branch=branch,C=cc,D=dd,T=t,total_branches=len(pairs),
                    first_soluble=step is not None,n=n)
        trace.append(record)
        if step is None:continue
        vector,kernel=step
        assert len(kernel)==int(n%2==0)
        record['first_kernel_dimension']=len(kernel)
        if not kernel:
            pair=apply(m,x0,y0,1,q,1,vector)
            last=first(m,g,*pair,1,q,2,audit)
            if last is None:continue
            return finished(m,g,*apply(m,*pair,1,q,2,last[0]),trace,'iterated_adjoint')
        vector=short_particular((vector,kernel));direction=kernel[0]
        def pair(k):return apply(m,x0,y0,1,q,1,[a+k*b for a,b in zip(vector,direction)])
        def residual(k):
            delta=m.mul(m.inv(m.comm(*pair(k))),g)
            assert all(len(w)>=c for w in delta if w)
            return m.coordinates(m.layer(delta,c),c)
        coefficients=differences([residual(k) for k in range(3)])
        for k in [-2,-1,3]:assert evaluate(coefficients,k)==residual(k)
        z,d=m.layer(x0,1),m.layer(y0,q)
        columns=([bracket(m,m.layer(h['value'],3),d) for h in m.bydegree[3]]
                 +[bracket(m,z,m.layer(h['value'],q+2)) for h in m.bydegree[q+2]])
        system=polynomial_system([m.coordinates(col,c) for col in columns],coefficients)
        assert system['mode']=='finite_points' and len(system['values'])<=2
        assert any(system['certificate']['residual'][2][i][0]
                   for i in range(len(coefficients[0])))
        record['polynomial_degree']=c;record['polynomial']=system['certificate']
        if audit is not None:
            audit.append(dict(kind='polynomial',rank=m.rank,q=q,degree=c,word=list(word),
                              x0=m.collect(x0)[0],y0=m.collect(y0)[0],vector=vector,
                              kernel=direction,certificate=system['certificate'],
                              samples=[[k,*[m.collect(z)[0] for z in pair(k)]]
                                       for k in [-1,0,1,2,3]]))
        for k in system['values']:
            correction=evaluate(system['particular'],k)
            assert all(v.denominator==1 for v in correction)
            result=apply(m,*pair(k),1,q,2,list(map(int,correction)))
            assert m.comm(*result)==g
            record['selected_parameter']=k
            return finished(m,g,*result,trace,'iterated_adjoint')
    return dict(answer=False,case='all_iterated_adjoint_branches_failed',trace=trace)
