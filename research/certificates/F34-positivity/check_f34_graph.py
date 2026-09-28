#!/usr/bin/env python3
"""Finite tests of positivity reflection; not a general F34 decision solver."""
from collections import deque
from datetime import datetime,timezone
from itertools import product
import argparse
import json
from pathlib import Path
import random
from f38_polynomial_identity import inverse,word_reduce,substitute
from check_f38_polynomial import det,gap_value,words


def fold_graph(images):
    edges=[]; vertices=1
    for word in images:
        source=0
        for i,label in enumerate(word):
            target=0 if i==len(word)-1 else vertices
            if target: vertices+=1
            edges.append((source,label,target));source=target
    parent=list(range(vertices))
    def find(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]];v=parent[v]
        return v
    changed=True
    while changed:
        changed=False; outgoing={}
        for a,label,b in edges:
            for source,letter,target in [(a,label,b),(b,-label,a)]:
                key=find(source),letter; end=find(target)
                if key in outgoing and find(outgoing[key])!=end:
                    x,y=find(outgoing[key]),end
                    parent[max(x,y)]=min(x,y);changed=True
                else: outgoing[key]=end
    positive=set()
    for a,label,b in edges:
        if label>0: positive.add((find(a),label,find(b)))
        else: positive.add((find(b),-label,find(a)))
    live={find(0)}|{a for a,_,b in positive}|{b for a,_,b in positive}
    numbering={v:i for i,v in enumerate([find(0)]+sorted(live-{find(0)}))}
    positive=sorted((numbering[a],label,numbering[b]) for a,label,b in positive)
    adjacency={};outgoing={i:[] for i in range(len(live))}
    for eid,(a,label,b) in enumerate(positive,1):
        for source,letter,target,signed in [(a,label,b,eid),(b,-label,a,-eid)]:
            assert (source,letter) not in adjacency
            adjacency[source,letter]=target,signed
            outgoing[source].append((letter,target,signed))
    paths={0:()};tree=set();queue=deque([0])
    while queue:
        source=queue.popleft()
        for letter,target,signed in sorted(outgoing[source]):
            if target not in paths:
                paths[target]=paths[source]+(letter,)
                tree.add(abs(signed));queue.append(target)
    assert len(paths)==len(live)
    outside=[i for i in range(1,len(positive)+1) if i not in tree]
    numbers={eid:i+1 for i,eid in enumerate(outside)}
    basis=[]
    for eid in outside:
        a,label,b=positive[eid-1]
        basis.append(word_reduce(paths[a]+(label,)+inverse(paths[b])))
    def read(word):
        vertex=0;traversals=[];coordinates=[]
        for letter in word:
            vertex,signed=adjacency[vertex,letter]
            traversals.append(signed)
            if abs(signed) in numbers:
                coordinates.append((1 if signed>0 else -1)*numbers[abs(signed)])
        assert vertex==0,'word does not close in folded graph'
        return tuple(traversals),word_reduce(coordinates)
    return dict(edges=positive,vertices=len(live),tree=sorted(tree),basis=basis),read


def certificate(rank,images,word,name):
    images=[word_reduce(w) for w in images];word=word_reduce(word)
    matrix=[[w.count(i)-w.count(-i) for w in images] for i in range(1,rank+1)]
    determinant=det(matrix);image=substitute(word,images)
    row=dict(name=name,rank=rank,images=images,word=word,image=image,
             determinant=determinant)
    if not determinant:return dict(row,status='singular_scope_control')
    if any(a<0 for a in image):return dict(row,status='image_not_positive_scope_control')
    graph,read=fold_graph(images)
    assert len(graph['basis'])==rank
    coordinates=[read(w)[1] for w in images]
    traversals,positive=read(image)
    assert all(e>0 for e in traversals) and all(e>0 for e in positive)
    assert substitute(positive,graph['basis'])==image
    assert substitute(word,coordinates)==positive
    for old,new in zip(images,coordinates):
        assert substitute(new,graph['basis'])==old
    return dict(row,status='positive_automorphism_witness',graph=graph,
                automorphism_images=coordinates,positive_word=positive,
                positive_path=traversals)


def random_automorphism(rank,steps,rng):
    identity=[(i,) for i in range(1,rank+1)]
    images=list(identity);backward=list(identity)
    for _ in range(steps):
        i,j=rng.sample(range(rank),2);sign=rng.choice([-1,1])
        step=list(identity);undo=list(identity)
        step[i]=(i+1,sign*(j+1));undo[i]=(i+1,-sign*(j+1))
        images=[substitute(w,step) for w in images]
        backward=[substitute(w,backward) for w in undo]
    assert [substitute(w,backward) for w in images]==identity
    assert [substitute(w,images) for w in backward]==identity
    return images,backward


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
    out=Path(args.output);out.mkdir(parents=True,exist_ok=False)
    rng=random.Random(34092026);records=[];map_count=0
    for rank in [2,3,4]:
        for family in ['identity','powers','cycles']:
            theta=[(i,) for i in range(1,rank+1)]
            if family=='powers':theta=[(i,)*(2+i%2) for i in range(1,rank+1)]
            if family=='cycles':theta=[(i,)*(2+i%2)+(i%rank+1,) for i in range(1,rank+1)]
            for steps in [3,7,10,15]:
                alpha,backward=random_automorphism(rank,steps,rng)
                images=[substitute(w,theta) for w in alpha];map_count+=1
                for length in [0,1,2,5,8]:
                    positive=tuple(rng.randrange(1,rank+1) for _ in range(length))
                    w=substitute(positive,backward)
                    rec=certificate(rank,images,w,f'{rank}-{family}-{steps}-{length}')
                    assert rec['status']=='positive_automorphism_witness'
                    records.append(rec)
    image_words=words(2,3);pairs=list(product(image_words,repeat=2));rng.shuffle(pairs)
    inspected=0;accepted_maps=0;candidates=words(2,4)[1:]
    for images in pairs[:200]:
        inspected+=1;found=0
        for w in candidates:
            rec=certificate(2,images,w,f'bounded-{inspected}-{found}')
            if rec['status']=='positive_automorphism_witness':
                records.append(rec);found+=1
                if found==3:break
        if found:accepted_maps+=1
        if accepted_maps==30:break
    for name,images,w in [
        ('singular_commutator_empty',[(1,),(1,)],(1,2,-1,-2)),
        ('singular_injective_positive',[(1,),(2,1,-2)],(1,)),
        ('identity_commutator_not_positive',[(1,),(2,)],(1,2,-1,-2)),
    ]:
        rec=certificate(2,images,w,name);assert rec['status']!='positive_automorphism_witness'
        records.append(rec)
    witnesses=[r for r in records if r['status']=='positive_automorphism_witness']
    assert any(any(a<0 for a in r['word']) and r['positive_word'] for r in witnesses)
    assert any(abs(r['determinant'])>1 for r in witnesses)
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),random_seed=34092026,
                scope='Graph reflection witnesses only; no general F34 decision solver.',
                designed_maps=map_count,short_maps_inspected=inspected,
                short_maps_with_positive_witnesses=accepted_maps,
                records=records,witnesses=len(witnesses),controls=len(records)-len(witnesses))
    (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'fixtures.g').write_text('F34Records := '+gap_value(records)+';;\n')
    (out/'check_f34_graph.py').write_bytes(Path(__file__).read_bytes())
    print('PASS F34 graph:',len(witnesses),'positive automorphism witnesses;',
          len(records)-len(witnesses),'scope controls;',inspected,'short maps inspected')


if __name__=='__main__':main()
