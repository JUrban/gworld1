#!/usr/bin/env python3
"""Exact finite algorithm for the abelian splitting step in the N5 lead.

An element of Z^n + C_d1 + ... + C_dt is a column, free coordinates first.
A constraint (side, vector, modulus) asks vector in Z_side + modulus*Z;
modulus zero means exact containment. Return a projection onto Z_1.
This is the central lifting subroutine, not an implementation of the whole
nilpotent decomposition algorithm.
"""
from collections import deque
from itertools import product
from math import gcd,lcm
from sympy import Matrix
from n8_class3 import smith


def saturated_basis(columns,n):
    if not columns:return Matrix.zeros(n,0)
    a=Matrix.hstack(*(Matrix(v) for v in columns))
    d,s,_=smith(a);rank=sum(d[i,i]!=0 for i in range(min(d.shape)))
    return s.inv()[:,:rank]


def free_splittings(n,constraints):
    """One feasible projection for each possible rank, or the empty list."""
    if n==0:return [Matrix.zeros(0)]
    w=[saturated_basis([v for side,v,d in constraints if side==i and d==0],n) for i in (1,2)]
    a=Matrix.hstack(*w);r1,r2=w[0].cols,w[1].cols;k=r1+r2
    if a.rank()!=k:return []
    if k:
        d,s,_=smith(a)
        if any(abs(d[i,i])!=1 for i in range(k)):return []
        basis=Matrix.hstack(a,s.inv()[:,k:])
    else:basis=Matrix.eye(n)
    assert abs(basis.det())==1
    inverse=basis.inv();transformed=[(side,inverse*Matrix(v),d) for side,v,d in constraints]
    modulus=lcm(*(d for _,_,d in constraints if d>0)) if any(d>0 for _,_,d in constraints) else 1
    generators=[]
    for j in range(k,n):
        for i in range(n):
            if i==j:continue
            g=Matrix.eye(n);g[i,j]=1;generators.append(g)
    if k<n:
        g=Matrix.eye(n);g[k,k]=-1;generators.append(g)
        for i in range(k,n-1):
            g=Matrix.eye(n);g.row_swap(i,i+1);generators.append(g)
    def key(g):return tuple(int(x)%modulus for x in g)
    identity=Matrix.eye(n);seen={key(identity)};queue=deque([identity]);found={}
    while queue:
        g=queue.popleft();gi=g.inv()
        for extra in range(n-k+1):
            rank=r1+extra
            if rank in found:continue
            diag=[int(i<r1 or k<=i<k+extra) for i in range(n)]
            p=g*Matrix.diag(*diag)*gi
            ok=True
            for side,v,d in transformed:
                residual=(identity-p if side==1 else p)*v
                if (any(residual) if d==0 else any(int(x)%d for x in residual)):
                    ok=False;break
            if ok:found[rank]=basis*p*inverse
        if len(found)==n-k+1:break
        for h in generators:
            candidate=h*g;kk=key(candidate)
            if kk not in seen:seen.add(kk);queue.append(candidate)
    return [found[k] for k in sorted(found)]


def finite_idempotents(orders):
    t=len(orders)
    if not t:
        yield Matrix.zeros(0);return
    elements=list(product(*(range(d) for d in orders)))
    columns=[[v for v in elements if all(d*v[i]%orders[i]==0 for i in range(t))] for d in orders]
    for chosen in product(*columns):
        p=Matrix.hstack(*(Matrix(v) for v in chosen));delta=p*p-p
        if all(int(delta[i,j])%orders[i]==0 for i in range(t) for j in range(t)):yield p


def satisfies(p,n,orders,constraints):
    size=n+len(orders);identity=Matrix.eye(size)
    delta=p*p-p
    assert all(delta[i,j]==0 for i in range(n) for j in range(size))
    assert all(int(delta[n+i,j])%d==0 for i,d in enumerate(orders) for j in range(size))
    for side,v,d in constraints:
        residual=(identity-p if side==1 else p)*Matrix(v)
        if any((x!=0 if d==0 else int(x)%d!=0) for x in residual[:n]):return False
        for j,order in enumerate(orders):
            if int(residual[n+j])%gcd(d,order):return False
    return True


def split(n,orders,constraints,require_nontrivial=(True,True)):
    assert n>=0 and all(d>=2 for d in orders)
    assert all(side in (1,2) and len(v)==n+len(orders) and d>=0 for side,v,d in constraints)
    free=free_splittings(n,[(side,v[:n],d) for side,v,d in constraints])
    if not free:return None
    t=len(orders);elements=list(product(*(range(d) for d in orders)))
    for pt in finite_idempotents(orders):
        for columns in product(elements,repeat=n):
            beta=Matrix.hstack(*(Matrix(v) for v in columns)) if t and n else Matrix.zeros(t,n)
            ok=True
            for side,v,d in constraints:
                vv=Matrix(t,1,v[n:])-beta*Matrix(n,1,v[:n])
                residual=(Matrix.eye(t)-pt if side==1 else pt)*vv
                if any(int(residual[i])%gcd(d,orders[i]) for i in range(t)):
                    ok=False;break
            if not ok:continue
            for pf in free:
                p=Matrix.vstack(Matrix.hstack(pf,Matrix.zeros(n,t)),
                                Matrix.hstack(beta*pf-pt*beta,pt))
                finite1=any(int(pt[i,j])%orders[i] for i in range(t) for j in range(t))
                finite2=any(int((Matrix.eye(t)-pt)[i,j])%orders[i] for i in range(t) for j in range(t))
                nontrivial=(pf.rank()>0 or finite1,pf.rank()<n or finite2)
                if any(required and not actual for required,actual in zip(require_nontrivial,nontrivial)):continue
                assert satisfies(p,n,orders,constraints)
                return p
    return None


def relation_constraints(exponent_matrix,defects,n,orders,side):
    """Translate relator defects by a Smith row change, including zero rows."""
    e=Matrix(exponent_matrix);assert e.rows==len(defects)
    if e.rows==0:return []
    if e.cols:d,s,_=smith(e)
    else:d=Matrix.zeros(e.rows,0);s=Matrix.eye(e.rows)
    values=s*Matrix(defects);constraints=[]
    for i in range(e.rows):
        modulus=abs(int(d[i,i])) if i<e.cols else 0
        vector=[int(x) for x in values.row(i)]
        for j,order in enumerate(orders):vector[n+j]%=order
        constraints.append((side,vector,modulus))
    return constraints
