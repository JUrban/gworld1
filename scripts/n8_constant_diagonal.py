#!/usr/bin/env python3
"""Exact rational diagonal equivalence for a constant matrix.

This is the constant special case of polynomial Smith equivalence over Q[T].
All nonzero invariant factors are units, so diagonal ones suffice. Integer
solvability still uses the original integer matrix and its full lattice.
"""
import sympy as S
from flint import fmpq_mat


def diagonal(A):
    A=S.Matrix(A);m,n=A.shape
    assert all(x.is_Rational for x in A)
    if not m or not n:return S.zeros(m,n),S.eye(m),S.eye(n)
    q=lambda x:str(x)
    original=fmpq_mat([[q(A[i,j]) for j in range(n)] for i in range(m)])
    augmented=fmpq_mat([[q(A[i,j]) for j in range(n)]+[int(i==j) for j in range(m)] for i in range(m)])
    reduced,fullrank=augmented.rref();assert fullrank==m
    R=fmpq_mat([[reduced[i,j] for j in range(n)] for i in range(m)])
    U=fmpq_mat([[reduced[i,n+j] for j in range(m)] for i in range(m)])
    pivots=[]
    for i in range(m):
        nonzero=[j for j in range(n) if R[i,j]]
        if nonzero:pivots.append(nonzero[0])
    r=len(pivots);assert len(set(pivots))==r
    order=pivots+[j for j in range(n) if j not in pivots]
    permutation=fmpq_mat(n,n)
    for j,i in enumerate(order):permutation[i,j]=1
    right=fmpq_mat(n,n)
    for i in range(n):right[i,i]=1
    permuted=R*permutation
    for i in range(r):
        for j in range(r,n):right[i,j]=-permuted[i,j]
    V=permutation*right;D=fmpq_mat(m,n)
    for i in range(r):D[i,i]=1
    assert U*original*V==D and U.det()!=0 and V.det()!=0
    def matrix(x):return S.Matrix(x.nrows(),x.ncols(),lambda i,j:S.Rational(str(x[i,j])))
    return matrix(D),matrix(U),matrix(V)
