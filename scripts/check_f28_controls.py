#!/usr/bin/env python3
"""Exact controls showing why both boundedness and aperiodicity are necessary."""
from fractions import Fraction as F
I=(F(1),F(0),F(0),F(1))
A=(F(1),F(2),F(0),F(1));B=(F(1),F(0),F(2),F(1))
def mul(x,y):
 a,b,c,d=x;e,f,g,h=y
 return a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h
def inv(x):
 a,b,c,d=x;k=a*d-b*c
 return d/k,-b/k,-c/k,a/k
def conj(t,x):return mul(mul(t,x),inv(t))
def neg(x):return tuple(-z for z in x)
# Hyperbolic scaling: <a> is a nontrivial forward-invariant subgroup.
D=(F(2),F(0),F(0),F(1))
assert conj(D,A)==mul(A,A)
# Finite-order elliptic conjugation: <a,b^2> is invariant (in fact exchanged).
J=(F(0),F(-1),F(2),F(0))
assert mul(J,J)==tuple(-2*z for z in I)
assert conj(J,A)==inv(mul(B,B))
assert conj(J,mul(B,B))==inv(A)
print('PASS F28 controls: scaling preserves <a>; periodic elliptic map preserves <a,b^2>')
