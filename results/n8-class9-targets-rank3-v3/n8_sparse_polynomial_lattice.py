#!/usr/bin/env python3
"""Exact Newton-polynomial lattice solver with disconnected-support reduction.

Returns the complete integer solution set as finitely many points, or as
residue classes modulo an explicit period. Uses a checked FLINT row-Hermite
transformation; no unrestricted integer-polynomial solver is assumed.
"""
from fractions import Fraction
from math import comb,factorial,lcm
from flint import fmpz_mat
from n8_component_hnf import hermite
from sympy import Poly,Rational,symbols,prod


def choose(t,j):
    ans=1
    for i in range(j):ans=ans*(t-i)//(i+1)
    return ans


def evaluate(coefficients,t):
    return [sum(Fraction(v[i])*choose(t,j) for j,v in enumerate(coefficients))
            for i in range(len(coefficients[0]))]


def differences(values):
    work=[list(v) for v in values];result=[]
    while work:
        result.append(work[0])
        work=[[b-a for a,b in zip(x,y)] for x,y in zip(work,work[1:])]
    return result


def integer_roots(coefficients):
    """All integer roots of a nonzero rational Newton polynomial."""
    x=symbols('x')
    expression=sum(Rational(v.numerator,v.denominator)*prod(x-i for i in range(j))/factorial(j)
                   for j,c in enumerate(coefficients) if (v:=Fraction(c)))
    p=Poly(expression,x,domain='QQ')
    assert not p.is_zero
    return sorted(int(r) for r in p.ground_roots() if r.q==1)


def encode(matrix):
    return [[[v.numerator,v.denominator] for x in row if (v:=Fraction(x)) is not None]
            for row in matrix]


def polynomial_system(columns,coefficients):
    """All k with sum_j binomial(k,j)*coeff[j] in span_Z(columns).

    particular is a rational polynomial in the original column coordinates;
    at every admitted k it is integral and solves the system. It is unique
    precisely when the column kernel is zero. Coefficients must be integral
    Newton vectors, so the target is integer-valued on every integer k.
    """
    assert coefficients and columns
    width=len(coefficients[0]);degree=len(coefficients)-1
    assert all(len(c)==width for c in columns+coefficients)
    assert all(Fraction(x).denominator==1 for c in coefficients for x in c)
    b=fmpz_mat(columns);h,u=hermite(b)
    assert h==u*b and abs(u.det())==1
    H=[[int(h[i,j]) for j in range(h.ncols())] for i in range(h.nrows())]
    U=[[int(u[i,j]) for j in range(u.ncols())] for i in range(u.nrows())]
    residual=[[Fraction(x) for x in row] for row in coefficients]
    z=[[Fraction(0) for _ in columns] for _ in coefficients]
    rank=0;pivots=[];congruences=[]
    for i,row in enumerate(H):
        pivot=next((j for j,x in enumerate(row) if x),None)
        if pivot is None:
            assert all(not x for rr in H[i:] for x in rr)
            break
        assert row[pivot]>0 and (not pivots or pivot>pivots[-1])
        pivots.append(pivot);rank+=1
        nonzero=[(k,v) for k,v in enumerate(row) if v]
        for j in range(len(coefficients)):
            z[j][i]=residual[j][pivot]/row[pivot]
            if z[j][i]:
                for k,v in nonzero:residual[j][k]-=z[j][i]*v
        denominator=lcm(*(z[j][i].denominator for j in range(len(coefficients))))
        numerator=[int(z[j][i]*denominator) for j in range(len(coefficients))]
        congruences.append([denominator,numerator])
    particular=[[Fraction(0) for _ in columns] for _ in coefficients]
    for j in range(len(coefficients)):
        for i,value in enumerate(z[j]):
            if value:
                for k,n in enumerate(U[i]):
                    if n:particular[j][k]+=value*n
    equations=[[residual[j][i] for j in range(len(coefficients))]
               for i in range(width)]
    equation=next((v for v in equations if any(v)),None)
    def allowed(k):
        return (all(sum(a*choose(k,j) for j,a in enumerate(eq))==0 for eq in equations)
                and all(sum(a*choose(k,j) for j,a in enumerate(nums))%d==0
                        for d,nums in congruences))
    if equation is not None:
        candidates=integer_roots(equation)
        values=[k for k in candidates if allowed(k)]
        mode='finite_points';period=None
    else:
        period=factorial(degree)*lcm(*(d for d,_ in congruences))
        candidates=None
        values=[k for k in range(period) if allowed(k)]
        mode='residue_classes'
    for k in values:
        solution=evaluate(particular,k)
        assert all(a.denominator==1 for a in solution)
        assert [sum(a*c[i] for a,c in zip(solution,columns) if a) for i in range(width)]==evaluate(coefficients,k)
    cert=dict(columns=columns,coefficients=coefficients,H=H,U=U,rank=rank,pivots=pivots,
              residual=encode(residual),particular=encode(particular),
              congruences=congruences,equation=encode([equation])[0] if equation else None,
              candidates=candidates,mode=mode,period=period,values=values)
    return dict(mode=mode,period=period,values=values,particular=particular,
                kernel=U[rank:],certificate=cert)
