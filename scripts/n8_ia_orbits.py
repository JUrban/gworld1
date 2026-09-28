#!/usr/bin/env python3
"""Integral Magnus/IA prototype for the arbitrary-class N8 target stratum.

Conventions: signed one-based generator words; [x,y]=x^-1 y^-1 x y.
All series are truncated at a user-specified nilpotency class. This is a
research prototype; see independent-abelianization-proof.md for completeness.
"""
from functools import cached_property
from itertools import combinations,product
from sympy import Matrix
from sympy.polys.matrices import DomainMatrix
from n8_class3 import add,ONE,smith,winv,wcomm,wpow,lift_vector
from n8_class4 import factor_wedge
from n8_class5 import affine_solve,reduced


class Magnus:
    def __init__(self,rank,degree):
        assert rank>=2 and degree>=2
        self.rank=rank;self.degree=degree
        self.gens=[{():1,(i,):1} for i in range(rank)]
        self.hall=[dict(weight=1,pair=None,word=[i+1],value=g) for i,g in enumerate(self.gens)]
        for weight in range(2,degree+1):
            new=[]
            for i,a in enumerate(self.hall):
                for j in range(i):
                    b=self.hall[j]
                    if a['weight']+b['weight']!=weight:continue
                    if a['pair'] is not None and a['pair'][1]>j:continue
                    new.append(dict(weight=weight,pair=(i,j),word=reduced(wcomm(a['word'],b['word'])),
                                    value=self.comm(a['value'],b['value'])))
            self.hall.extend(new)
        self.bydegree={d:[h for h in self.hall if h['weight']==d] for d in range(1,degree+1)}
        self.projections={};self.offsets={};offset=0
        for d in range(1,degree+1):
            lie=[self.layer(h['value'],d) for h in self.bydegree[d]]
            words=sorted(set().union(*(set(x) for x in lie)))
            matrix=Matrix([[x.get(w,0) for x in lie] for w in words])
            _,pivots=DomainMatrix.from_Matrix(matrix).transpose().rref()
            assert len(pivots)==len(lie)
            self.projections[d]=(words,list(pivots),matrix[list(pivots),:].inv(),lie)
            if d>=2:self.offsets[d]=offset;offset+=rank*len(lie)
        self.ia_dimension=offset
        self.identity=IA(self,self.gens)

    def mul(self,a,b):
        out={}
        for u,x in a.items():
            for v,y in b.items():
                if len(u)+len(v)<=self.degree:
                    w=u+v;out[w]=out.get(w,0)+x*y
        return {w:c for w,c in out.items() if c}

    def inv(self,a):
        assert a.get(())==1
        b=add(a,ONE,-1);out=dict(ONE);term=dict(ONE)
        for k in range(1,self.degree+1):
            term=self.mul(term,b)
            if not term:break
            out=add(out,term,(-1)**k)
        return out

    def power(self,a,n):
        n=int(n)
        if n<0:a=self.inv(a);n=-n
        out=dict(ONE)
        while n:
            if n&1:out=self.mul(out,a)
            n//=2
            if n:a=self.mul(a,a)
        return out

    def comm(self,a,b):return self.mul(self.mul(self.mul(self.inv(a),self.inv(b)),a),b)
    def layer(self,a,d):return {w:c for w,c in a.items() if len(w)==d}

    def expansion(self,word):
        out=dict(ONE)
        for s in reduced(word):
            i=abs(s)-1;updated=dict(out)
            for w,c in out.items():
                for k in range(1,(1 if s>0 else self.degree-len(w))+1):
                    if len(w)+k>self.degree:break
                    t=w+(i,)*k;updated[t]=updated.get(t,0)+c*((-1)**k if s<0 else 1)
            out={w:c for w,c in updated.items() if c}
        return out

    def coordinates(self,p,d):
        words,rows,inverse,lie=self.projections[d]
        vector=inverse*Matrix([p.get(words[i],0) for i in rows])
        assert all(v.q==1 for v in vector),('nonintegral Lie coordinates',d)
        answer=list(map(int,vector));total={}
        for x,n in zip(lie,answer):total=add(total,x,n)
        assert total==p,('outside Lie layer',d,p)
        return answer

    def lift(self,coords,d):
        out=dict(ONE)
        for h,n in zip(self.bydegree[d],coords):out=self.mul(out,self.power(h['value'],n))
        return out

    def collect(self,g):
        residual=dict(g);word=[];coeffs=[]
        for d in range(1,self.degree+1):
            cc=self.coordinates(self.layer(residual,d),d);coeffs.extend(cc)
            for h,n in zip(self.bydegree[d],cc):word.extend(wpow(h['word'],n))
            residual=self.mul(self.inv(self.lift(cc,d)),residual)
        assert residual==ONE
        word=reduced(word);assert self.expansion(word)==g
        return word,coeffs

    def ia_group(self):
        maps=[]
        for d in range(2,self.degree+1):
            for i in range(self.rank):
                for h in self.bydegree[d]:
                    images=list(self.gens);images[i]=self.mul(images[i],h['value'])
                    maps.append(IA(self,images))
        # Every coordinate has its own unit pivot; the proof establishes that
        # these maps generate the entire IA group, hence are already complete.
        result=IABasis(self)
        for a in maps:result.insert(a)
        assert len(result.rows)==self.ia_dimension
        return result


class IA:
    def __init__(self,algebra,images):
        self.m=algebra;self.images=tuple(images);self._inverse=None

    @cached_property
    def key(self):return tuple(tuple(sorted(g.items())) for g in self.images)
    def is_identity(self):return all(g==h for g,h in zip(self.images,self.m.gens))

    def apply(self,polynomial):
        aug=[add(x,ONE,-1) for x in self.images];cache={():ONE}
        def monomial(w):
            if w not in cache:cache[w]=self.m.mul(monomial(w[:-1]),aug[w[-1]])
            return cache[w]
        result={}
        for w,n in polynomial.items():result=add(result,monomial(w),n)
        return result

    def compose(self,other):
        if self.is_identity():return other
        if other.is_identity():return self
        return IA(self.m,[self.apply(g) for g in other.images])

    def inverse(self):
        if self._inverse is not None:return self._inverse
        images=list(self.m.gens)
        for d in range(2,self.m.degree+1):
            images=[add(g,self.m.layer(add(self.apply(g),base,-1),d),-1)
                    for g,base in zip(images,self.m.gens)]
        ans=IA(self.m,images);self._inverse=ans;ans._inverse=self
        assert self.compose(ans).is_identity()
        return ans

    def power(self,n):
        n=int(n)
        if n<0:return self.inverse().power(-n)
        out=self.m.identity;a=self
        while n:
            if n&1:out=out.compose(a)
            n//=2
            if n:a=a.compose(a)
        return out

    def comm(self,other):
        return self.inverse().compose(other.inverse()).compose(self).compose(other)

    @cached_property
    def lead(self):
        differences=[add(g,h,-1) for g,h in zip(self.images,self.m.gens)]
        degree=min((len(w) for p in differences for w in p),default=None)
        if degree is None:return None
        assert degree>=2
        row=[]
        for p in differences:row.extend(self.m.coordinates(self.m.layer(p,degree),degree))
        i=next(i for i,a in enumerate(row) if a)
        return degree,self.m.offsets[degree]+i,row[i]


class IABasis:
    """A complete triangular subgroup basis in the central IA filtration."""
    def __init__(self,algebra):self.m=algebra;self.rows={};self.version=0
    def generators(self):return [self.rows[i] for i in sorted(self.rows)]

    def insert(self,g):
        while g.lead is not None:
            degree,i,a=g.lead
            if i not in self.rows:
                self.rows[i]=g if a>0 else g.inverse();self.version+=1;return
            pivot=self.rows[i];b=pivot.lead[2];assert b>0
            q,r=divmod(a,b)
            if q:g=pivot.power(-q).compose(g)
            if r:
                assert g.lead[1:]==(i,r)
                self.rows[i]=g;self.version+=1;g=pivot

    def reduce(self,g):
        while g.lead is not None:
            _,i,a=g.lead
            if i not in self.rows:return g
            pivot=self.rows[i];b=pivot.lead[2]
            q,r=divmod(a,b)
            if r:return g
            g=pivot.power(-q).compose(g)
        return g

    def complete(self):
        while True:
            old=self.version;gens=self.generators()
            for a,b in combinations(gens,2):
                if a.lead[0]+b.lead[0]-1>self.m.degree:continue
                for aa,bb in product((a,a.inverse()),(b,b.inverse())):
                    self.insert(aa.comm(bb))
            if old==self.version:return self

    def kernel(self,columns):
        gens=self.generators();assert len(gens)==len(columns)
        if not gens:return self
        if not any(any(c) for c in columns):return self
        _,nullspace=affine_solve(columns,[0]*len(columns[0]))
        out=IABasis(self.m)
        for v in nullspace:
            a=self.m.identity
            for g,n in zip(gens,v):
                if n:a=a.compose(g.power(n))
            out.insert(a)
        for a,b in combinations(gens,2):
            if a.lead[0]+b.lead[0]-1<=self.m.degree:out.insert(a.comm(b))
        out.complete()
        # Normal closure under the original K. Each new pivot either fills a
        # vacant depth or decreases its positive integer pivot; termination is
        # therefore finite. Completion handles internal collection relations.
        while True:
            old=out.version
            for a,b in product(out.generators(),gens):
                if a.lead[0]+b.lead[0]-1>self.m.degree:continue
                out.insert(a.comm(b));out.insert(a.comm(b.inverse()))
            out.complete()
            if old==out.version:return out


def orbit(m,group,start,target,trace=None):
    if m.layer(start,1)!=m.layer(target,1):return None
    a=m.identity;k=group
    for degree in range(2,m.degree+1):
        v=a.apply(start)
        delta=m.mul(m.inv(v),target)
        assert not any(0<len(w)<degree for w in delta)
        rhs=m.coordinates(m.layer(delta,degree),degree)
        gens=k.generators()
        columns=[m.coordinates(m.layer(m.mul(m.inv(v),g.apply(v)),degree),degree) for g in gens]
        result=affine_solve(columns,rhs)
        if trace is not None:trace.append(dict(degree=degree,generators=len(gens),soluble=result is not None))
        if result is None:return None
        adjustment=m.identity
        for g,n in zip(gens,result[0]):
            if n:adjustment=adjustment.compose(g.power(n))
        a=adjustment.compose(a)
        if degree<m.degree:k=k.kernel(columns)
    assert a.apply(start)==target
    return a


def fixed_leading_representatives(m,u,v):
    a=Matrix([u,v]);d,s,_=smith(a);si=s.inv()
    residues=[list(map(int,si*Matrix([i,j])))
              for i in range(abs(int(d[0,0]))) for j in range(abs(int(d[1,1])))]
    pairs=[(m.expansion(lift_vector(u)),m.expansion(lift_vector(v)))]
    for degree in range(2,m.degree):
        corrections=[]
        for selected in product(residues,repeat=len(m.bydegree[degree])):
            corrections.append((m.lift([x[0] for x in selected],degree),
                                m.lift([x[1] for x in selected],degree)))
        pairs=[(m.mul(x,c),m.mul(y,d)) for x,y in pairs for c,d in corrections]
    return pairs


def decide_nonzero_degree_two(m,word):
    g=m.expansion(word)
    if m.layer(g,1):return dict(answer=False,case='outside_derived')
    g2=m.layer(g,2);assert g2,'This prototype decides only the nonzero-degree-two stratum.'
    w=Matrix(m.rank,m.rank,lambda i,j:g2.get((i,j),0));assert w==-w.T
    if w.rank()!=2:return dict(answer=False,case='exterior_rank')
    from sympy import divisors
    plane,index=factor_wedge(w);group=m.ia_group();tried=0
    for a in divisors(index):
        a=int(a);c=index//a
        for b in range(a):
            u=list(map(int,a*plane[:,0]));v=list(map(int,b*plane[:,0]+c*plane[:,1]))
            for x,y in fixed_leading_representatives(m,u,v):
                tried+=1;aut=orbit(m,group,m.comm(x,y),g)
                if aut is not None:
                    xx,yy=aut.apply(x),aut.apply(y);assert m.comm(xx,yy)==g
                    return dict(answer=True,case='nonzero_degree2',tried=tried,
                                x=m.collect(xx)[0],y=m.collect(yy)[0])
    return dict(answer=False,case='nonzero_degree2',tried=tried)
