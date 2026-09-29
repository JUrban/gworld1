#!/usr/bin/env python3
"""Recursive exact flows for F_r/F_r^(d), with noncommutative deck groups.

At depth 1 an element is its exponent vector. At depth d>1 it is
(endpoint_in_depth_d_minus_1, sorted (base, zero_based_axis, coefficient)).
The endpoint is redundant but retained to make multiplication explicit.
"""
from collections import defaultdict
from functools import lru_cache


class SolvableFlows:
    def __init__(self,rank):
        assert rank>=1
        self.rank=rank

    @lru_cache(None)
    def zero(self,d):
        assert d>=1
        return (0,)*self.rank if d==1 else (self.zero(d-1),())

    @lru_cache(None)
    def gen(self,d,s):
        assert 1<=abs(s)<=self.rank
        j=abs(s)-1;sign=1 if s>0 else -1
        if d==1:return tuple(sign if i==j else 0 for i in range(self.rank))
        ep=self.gen(d-1,s)
        return ep,((self.zero(d-1) if s>0 else ep,j,sign),)

    @staticmethod
    def clean(edges):
        return tuple(sorted((p,j,c) for (p,j),c in edges.items() if c))

    @lru_cache(None)
    def mul(self,d,g,h):
        if d==1:return tuple(a+b for a,b in zip(g,h))
        edges=defaultdict(int,{(p,j):c for p,j,c in g[1]})
        for p,j,c in h[1]:edges[(self.mul(d-1,g[0],p),j)]+=c
        return self.mul(d-1,g[0],h[0]),self.clean(edges)

    @lru_cache(None)
    def inv(self,d,g):
        if d==1:return tuple(-x for x in g)
        ep=self.inv(d-1,g[0])
        return ep,tuple(sorted((self.mul(d-1,ep,p),j,-c) for p,j,c in g[1]))

    @lru_cache(None)
    def reflect(self,d,g):
        if d==1:return (-g[0],)+g[1:]
        edges=defaultdict(int)
        for p,j,c in g[1]:
            p=self.reflect(d-1,p)
            if j==0:p=self.mul(d-1,p,self.gen(d-1,-1));c=-c
            edges[(p,j)]+=c
        return self.reflect(d-1,g[0]),self.clean(edges)

    def height(self,d,g):
        while d>1:g=g[0];d-=1
        return g[0]

    @lru_cache(None)
    def word(self,d,w):
        if d==1:return tuple(sum(1 if s>0 else -1 for s in w if abs(s)==j+1) for j in range(self.rank))
        p=self.zero(d-1);edges=defaultdict(int)
        for s in w:
            j=abs(s)-1
            if s<0:p=self.mul(d-1,p,self.gen(d-1,s))
            edges[(p,j)]+=1 if s>0 else -1
            if s>0:p=self.mul(d-1,p,self.gen(d-1,s))
        return p,self.clean(edges)

    def endpoint(self,d,edges,start):
        """Recover the endpoint in depth d from a flow on its Cayley graph."""
        boundary=defaultdict(int)
        for p,j,c in edges:
            boundary[p]-=c;boundary[self.mul(d,p,self.gen(d,j+1))]+=c
        boundary[start]+=1
        nz=[(p,c) for p,c in boundary.items() if c]
        assert len(nz)==1 and nz[0][1]==1
        return nz[0][0]

    def translate(self,d,edges,start):
        return tuple(sorted((self.mul(d,start,p),j,c) for p,j,c in edges))

    def reflect_edges(self,d,edges):
        result=defaultdict(int)
        for p,j,c in edges:
            p=self.reflect(d,p)
            if j==0:p=self.mul(d,p,self.gen(d,-1));c=-c
            result[(p,j)]+=c
        return self.clean(result)

    def decode(self,d,g,spans):
        assert d>=2 and spans and all(a>b>0 for a,b in zip(spans,spans[1:]))
        oldstart=self.zero(d-1);newstart=oldstart;lo=0;sign=1;out=defaultdict(int)
        for span in spans:
            hi=lo+span
            chunk=tuple((p,j,c) for p,j,c in g[1] if lo<self.height(d-1,p)+(j==0)<=hi)
            finish=self.endpoint(d-1,chunk,newstart)
            assert self.height(d-1,finish)==hi
            piece=self.translate(d-1,chunk,self.inv(d-1,newstart))
            delta=self.mul(d-1,self.inv(d-1,newstart),finish)
            if sign<0:piece=self.reflect_edges(d-1,piece);delta=self.reflect(d-1,delta)
            for p,j,c in self.translate(d-1,piece,oldstart):out[(p,j)]+=c
            oldstart=self.mul(d-1,oldstart,delta);newstart=finish;lo=hi;sign=-sign
        assert newstart==g[0]
        assert all(0<self.height(d-1,p)+(j==0)<=lo for p,j,c in g[1])
        return oldstart,self.clean(out)
