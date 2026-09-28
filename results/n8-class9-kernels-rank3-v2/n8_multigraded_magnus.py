#!/usr/bin/env python3
"""Exact Magnus arithmetic with multidegree-block Hall projections.

Hall words and group series are unchanged. Each homogeneous tensor space
splits by letter counts; projection/inversion is done separately in each
block. This avoids a large sparse rational reduction over all words at once.
"""
from collections import defaultdict
from flint import fmpq,fmpq_mat
from sympy import Matrix,Rational
from n8_class8_magnus import Magnus as PreviousMagnus
from n8_ia_orbits import IA,wcomm
from n8_class5 import reduced


class BlockInverse:
    def __init__(self,dimension,blocks):
        self.dimension=dimension;self.blocks=blocks
    def __mul__(self,vector):
        assert vector.shape==(self.dimension,1)
        answer=[0]*self.dimension
        for columns,start,inverse in self.blocks:
            segment=vector[start:start+len(columns)]
            if not any(segment):continue
            rhs=fmpq_mat([[fmpq(int(v.p),int(v.q))] for v in segment])
            result=inverse*rhs
            for i,col in enumerate(columns):
                value=result[i,0]
                answer[col]=Rational(int(value.numerator),int(value.denominator))
        return Matrix(answer)


class Magnus(PreviousMagnus):
    def __init__(self,rank,degree):
        assert rank>=2 and degree>=2
        self.rank=rank;self.degree=degree
        self.gens=[{():1,(i,):1} for i in range(rank)]
        self.hall=[dict(weight=1,pair=None,word=[i+1],value=g)
                   for i,g in enumerate(self.gens)]
        for weight in range(2,degree+1):
            new=[]
            for i,a in enumerate(self.hall):
                for j in range(i):
                    b=self.hall[j]
                    if a['weight']+b['weight']!=weight:continue
                    if a['pair'] is not None and a['pair'][1]>j:continue
                    new.append(dict(weight=weight,pair=(i,j),
                                    word=reduced(wcomm(a['word'],b['word'])),
                                    value=self.comm(a['value'],b['value'])))
            self.hall.extend(new)
        self.bydegree={d:[h for h in self.hall if h['weight']==d]
                       for d in range(1,degree+1)}
        self.projections={};self.offsets={};offset=0
        for d in range(1,degree+1):
            lie=[self.layer(h['value'],d) for h in self.bydegree[d]]
            words=sorted(set().union(*(set(x) for x in lie)))
            positions={w:i for i,w in enumerate(words)}
            groups=defaultdict(list)
            for i,v in enumerate(lie):
                word=next(iter(v));key=tuple(word.count(j) for j in range(rank))
                assert all(tuple(w.count(j) for j in range(rank))==key for w in v)
                groups[key].append(i)
            selected=[];blocks=[]
            for key,columns in sorted(groups.items()):
                local_words=sorted(set().union(*(set(lie[i]) for i in columns)))
                matrix=fmpq_mat([[lie[i].get(w,0) for w in local_words] for i in columns])
                reduced_matrix,block_rank=matrix.rref()
                assert block_rank==len(columns)
                pivots=[next(j for j in range(len(local_words)) if reduced_matrix[i,j])
                        for i in range(block_rank)]
                square=fmpq_mat([[lie[i].get(local_words[j],0) for i in columns] for j in pivots])
                inverse=square.inv()
                assert inverse*square==fmpq_mat([[int(i==j) for j in columns] for i in columns])
                blocks.append((columns,len(selected),inverse))
                selected.extend(positions[local_words[j]] for j in pivots)
            assert len(selected)==len(lie)
            self.projections[d]=(words,selected,BlockInverse(len(lie),blocks),lie)
            if d>=2:self.offsets[d]=offset;offset+=rank*len(lie)
        self.ia_dimension=offset
        self.identity=IA(self,self.gens)
