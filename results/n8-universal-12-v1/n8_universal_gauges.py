#!/usr/bin/env python3
"""Exact finite constructor for universal commutator-preserving gauges.

This is NOT the complete N8 branch decision implementation. The checks
integrate every homogeneous kernel direction in specified weighted ranges.
All tensor coordinates use a=log(generator a), b=log(generator b).
"""
from fractions import Fraction as Q
from math import factorial, gcd, lcm
from functools import lru_cache
from pathlib import Path
import argparse, json, time
from n8_weighted_automorphisms import Tensor, Basis, add, scale

class WeightedTensor(Tensor):
    def __init__(self,p,q,c):
        self.rank,self.degree,self.weights=2,c,(p,q)
        self.one={():Q(1)}
        self.letters=[{(i,):Q(1)} for i in range(2)]
        self.hall=[dict(weight=w,pair=None,lie=x) for w,x in zip(self.weights,self.letters)]
        for d in range(1,c+1):
            pending=[]
            for i,a in enumerate(self.hall):
                for j,b in enumerate(self.hall[:i]):
                    if a['weight']+b['weight']!=d:continue
                    if a['pair'] is not None and a['pair'][1]>j:continue
                    pending.append(dict(weight=d,pair=(i,j),lie=self.bracket(a['lie'],b['lie'])))
            self.hall.extend(pending)
        self.layers={}
        for d in range(1,c+1):
            inds=[i for i,h in enumerate(self.hall) if h['weight']==d]
            basis=Basis()
            for i in inds:assert basis.insert(self.hall[i]['lie'])
            self.layers[d]=inds,basis
        self._groups={};self._logs={}
    @lru_cache(None)
    def weight(self,w):return sum(self.weights[i] for i in w)
    def mul(self,a,b):
        out={}
        for u,x in a.items():
            du=self.weight(u)
            for v,y in b.items():
                if du+self.weight(v)<=self.degree:
                    w=u+v;out[w]=out.get(w,0)+x*y
        return {w:x for w,x in out.items() if x}
    def layer(self,a,d):return {w:x for w,x in a.items() if self.weight(w)==d}
    def substitute(self,a,images):
        cache={():self.one}
        def mon(w):
            if w not in cache:cache[w]=self.mul(mon(w[:-1]),images[w[-1]])
            return cache[w]
        out={}
        for w,x in a.items():out=add(out,mon(w),x)
        return out
    def derivation(self,a,images):
        out={}
        for w,x in a.items():
            for i,z in enumerate(w):
                out=add(out,self.mul(self.mul({w[:i]:Q(1)},images[z]),{w[i+1:]:Q(1)}),x)
        return out
    def exp_derivation(self,a,images,n=1):
        out,term=dict(a),dict(a)
        for k in range(1,self.degree+1):
            term=self.derivation(term,images)
            if not term:break
            out=add(out,term,Q(n**k,factorial(k)))
        return out
    def inverse_substitution(self,images):
        tails=[add(x,y,-1) for x,y in zip(images,self.letters)]
        inverse=list(self.letters)
        for _ in range(self.degree+1):
            new=[add(a,self.substitute(t,inverse),-1) for a,t in zip(self.letters,tails)]
            if new==inverse:break
            inverse=new
        assert all(self.substitute(a,inverse)==b for a,b in zip(images,self.letters))
        assert all(self.substitute(a,images)==b for a,b in zip(inverse,self.letters))
        return inverse
    def columns(self,t):
        p,q=self.weights;a,b=self.letters
        ui=self.layers.get(p+t,([],None))[0];vi=self.layers.get(q+t,([],None))[0]
        columns=[self.bracket(self.hall[i]['lie'],b) for i in ui]
        columns += [self.bracket(a,self.hall[i]['lie']) for i in vi]
        return ui,vi,columns
    def split_coefficients(self,cc,ui,vi):
        U,V={},{}
        for j,x in cc.items():
            if j<len(ui):U=add(U,self.hall[ui[j]]['lie'],x)
            else:V=add(V,self.hall[vi[j-len(ui)]]['lie'],x)
        return U,V
    def kernels(self,t):
        ui,vi,columns=self.columns(t);B=Basis();chosen=[];answer=[]
        for j,column in enumerate(columns):
            rem,used=B.reduce(column)
            if rem:
                assert B.insert(column);chosen.append(j)
            else:
                cc={j:Q(1)}
                for i,x in used.items():cc[chosen[i]]=cc.get(chosen[i],0)-x
                denom=lcm(*(x.denominator for x in cc.values()))
                ints=[int(x*denom) for x in cc.values()];div=gcd(*ints)
                cc={j:int(x*denom)//div for j,x in cc.items() if x}
                U,V=self.split_coefficients(cc,ui,vi)
                assert not add(self.bracket(U,self.letters[1]),self.bracket(self.letters[0],V))
                answer.append((U,V))
        return answer
    def darboux(self):
        a,b=self.letters;W=self.log(self.comm(self.exp(a),self.exp(b)))
        images=list(self.letters);p,q=self.weights
        for d in range(p+q+1,self.degree+1):
            residual=self.layer(add(W,self.bracket(*images),-1),d)
            ui,vi,columns=self.columns(d-p-q);B=Basis();chosen=[]
            for j,column in enumerate(columns):
                if B.insert(column):chosen.append(j)
            used=B.coordinates(residual)
            U,V=self.split_coefficients({chosen[i]:x for i,x in used.items()},ui,vi)
            images=[add(images[0],U),add(images[1],V)]
        assert self.bracket(*images)==W
        return images,self.inverse_substitution(images),W

def terms_json(terms):return [[int(i),int(n)] for i,n in terms]
def poly_json(poly):return [[list(w),str(x)] for w,x in sorted(poly.items())]

def run_case(p,q,c,start,stop,out,max_factorial):
    begin=time.monotonic();m=WeightedTensor(p,q,c)
    sigma,tau,W=m.darboux();records=[];rejected=[];dims=[]
    a,b=m.letters
    for t in range(start,min(stop,c-p-q)+1):
        kernels=m.kernels(t);dims.append([t,len(kernels)])
        for j,(U,V) in enumerate(kernels):
            # A direction is a full homogeneous kernel, not just one killed
            # by truncating away its commutator error.
            assert p+q+t<=c
            images=(U,V)
            def maps(n):
                return [m.substitute(m.exp_derivation(x,images,n),sigma) for x in tau]
            chosen=None
            for k in range(1,max_factorial+1):
                n=factorial(k);plus=maps(n);minus=maps(-n)
                assert m.substitute(W,plus)==W and m.substitute(W,minus)==W
                coords=[m.collect(m.exp(x)) for x in plus+minus]
                if all(x.denominator==1 for terms in coords for _,x in terms):
                    chosen=(n,plus,minus,coords);break
                rejected.append([t,j,n])
            if chosen is None:raise RuntimeError(('Bounded integral-power search inconclusive',p,q,c,t,j))
            n,plus,minus,coords=chosen
            for i in range(2):
                assert m.substitute(plus[i],minus)==m.letters[i]
                assert m.substitute(minus[i],plus)==m.letters[i]
            for i,(lead,d) in enumerate(zip((U,V),(p+t,q+t))):
                diff=add(plus[i],m.letters[i],-1)
                assert all(m.weight(w)>=d for w in diff)
                assert m.layer(diff,d)==scale(lead,n)
            rec=dict(offset=t,kernel=j,power=n,direction=[poly_json(U),poly_json(V)],
                     plus=[terms_json(x) for x in coords[:2]],minus=[terms_json(x) for x in coords[2:]])
            records.append(rec)
            print('gauge',p,q,c,t,j,'power',n,flush=True)
    # Boundary relators are built independently as free-group Hall words
    # in GAP; no rational tensor code is loaded by that verifier.
    allhall=WeightedTensor(p,q,c+q).hall
    kept=len(m.hall)
    assert allhall[:kept]==m.hall
    boundaries=[i for i,h in enumerate(allhall) if h['weight']>c and h['pair'] is not None
                and all(j<kept for j in h['pair'])]
    payload=dict(weights=[p,q],class_bound=c,hall=[[h['weight'],list(h['pair']) if h['pair'] else []]
                  for h in allhall],retained=kept,boundaries=boundaries,kernel_dimensions=dims,
                  records=records,rejected_powers=rejected,seconds=time.monotonic()-begin)
    out.mkdir(parents=True,exist_ok=False)
    (out/'checks.json').write_text(json.dumps(payload,indent=2)+'\n')
    fixture=[p,q,c,payload['hall'],kept,boundaries,
             [[r['offset'],r['power'],r['plus'],r['minus']] for r in records]]
    (out/'fixtures.g').write_text('N8UniversalFixture := '+json.dumps(fixture)+';\n')
    print('PASS N8 universal gauges:',len(records),'maps;',dims,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--weights',type=int,nargs=2,required=True)
    ap.add_argument('--class-bound',type=int,required=True);ap.add_argument('--offsets',type=int,nargs=2,required=True)
    ap.add_argument('--output',type=Path,required=True);ap.add_argument('--max-factorial',type=int,default=12)
    x=ap.parse_args();run_case(*x.weights,x.class_bound,*x.offsets,x.output,x.max_factorial)
