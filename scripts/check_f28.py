#!/usr/bin/env python3
"""Exact matrix checks for the F28 construction; no bounded check proves freeness."""
from fractions import Fraction as Q
from itertools import product
import json

I=(Q(1),Q(0),Q(0),Q(1))
A=(Q(1),Q(2),Q(0),Q(1))
B=(Q(1),Q(0),Q(2),Q(1))
T=(Q(0),Q(-1),Q(2),Q(1))
def mul(x,y):
    a,b,c,d=x;e,f,g,h=y
    return a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h
def det(x):a,b,c,d=x;return a*d-b*c
def inv(x):a,b,c,d=x;t=det(x);return d/t,-b/t,-c/t,a/t
def power(x,n):
    if n<0:return power(inv(x),-n)
    y=I
    while n:
        if n%2:y=mul(y,x)
        x=mul(x,x);n//=2
    return y
def conj(x):return mul(mul(T,x),inv(T))
def eqpsl(x,y):return x==y or x==tuple(-z for z in y)

domain=[A,mul(mul(B,A),inv(B)),power(B,2)]
images=[power(B,-2),mul(mul(inv(B),power(A,2)),B),mul(inv(B),A)]
signs=[]
for x,y in zip(domain,images):
    assert eqpsl(conj(x),y)
    signs.append(1 if conj(x)==y else -1)
assert signs==[1,1,-1]
# Positive definite form: T^t P T = 2P, with P=[[4,1],[1,2]].
P=(Q(4),Q(1),Q(1),Q(2))
transpose=lambda x:(x[0],x[2],x[1],x[3])
assert mul(mul(transpose(T),P),T)==tuple(2*z for z in P)
assert P[0]>0 and det(P)>0
assert mul(T,T)==tuple(x-2*y for x,y in zip(T,I))

# All freely reduced nonempty words through length eight, exact matrices.
# For the domain test, the b-exponent parity must agree with c/2 modulo 2.
# Check every forward orbit exits the domain; the proof supplies termination.
letters={1:A,-1:inv(A),2:B,-2:inv(B)}
level=[((),I,0)];counts={};maximum=0;maxword=None;tested=0
for length in range(1,9):
    nxt=[]
    for w,m,p in level:
        for letter,x in letters.items():
            if w and w[-1]==-letter:continue
            word=w+(letter,);value=mul(m,x);parity=(p+(abs(letter)==2))%2
            assert det(value)==1 and not eqpsl(value,I)
            assert int(value[2]/2)%2==parity
            steps=0;h=value
            while all(z.denominator==1 for z in h) and int(h[2])%4==0:
                h=conj(h);steps+=1
                # A finite cap catches implementation errors; it is not used in the proof.
                assert steps<1000,(word,h)
            counts[steps]=counts.get(steps,0)+1;tested+=1
            if steps>maximum:maximum=steps;maxword=word
            nxt.append((word,value,parity))
    level=nxt
print(json.dumps({'words_through_length':8,'nonempty_words_checked':tested,
    'image_lift_signs':signs,'domain_survival_histogram':counts,
    'maximum_domain_steps':maximum,'one_maximizing_word':maxword},indent=2))
print('PASS F28 exact matrix identities and bounded word audit')
