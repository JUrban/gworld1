#!/usr/bin/env python3
"""Reproduce and retain the exact rank-three class-eight collection failure."""
import json,random,traceback
from pathlib import Path
from n8_class8 import Magnus,decide_class8
from n8_ia_orbits import ONE,wcomm,wpow
from n8_class5 import reduced

rng=random.Random(9282632);m=Magnus(3,8)
def higher(word,start,stop):
    word=list(word)
    for d in range(start,stop+1):
        h=rng.choice(m.bydegree[d]);word+=wpow(h['word'],rng.choice([-1,0,1]))
    return word
for p,q in [(2,2),(1,4),(1,5),(2,4),(3,3)]:
    x=m.bydegree[p][0]['word'];y=m.bydegree[q][-1]['word']
    wcomm(higher(x,p+1,8-q),higher(y,q+1,8-p))
z=[1,3];t=m.bydegree[2][0]['word']+m.bydegree[2][-1]['word']
d=wcomm(z,wcomm(z,t));target=wcomm(z+wpow(t,-1),higher(d,5,7))
original=m.collect
captured=[]
def diagnose(g):
    try:return original(g)
    except AssertionError:
        residual=dict(g);word=[];coeffs=[];product=ONE;used=[]
        for degree in range(1,9):
            cc=m.coordinates(m.layer(residual,degree),degree);coeffs.extend(cc)
            lift=m.lift(cc,degree);product=m.mul(product,lift)
            for h,n in zip(m.bydegree[degree],cc):
                if n:
                    used.append(dict(degree=degree,n=n,word=h['word'],
                                     correct_hall_value=m.expansion(h['word'])==h['value']))
                word.extend(wpow(h['word'],n))
            residual=m.mul(m.inv(lift),residual)
        word=reduced(word);expansion=m.expansion(word)
        diff={w:expansion.get(w,0)-g.get(w,0) for w in set(g)|set(expansion)
              if expansion.get(w,0)!=g.get(w,0)}
        record=dict(target=target,word=word,coefficients=coeffs,used=used,
                    residual_identity=residual==ONE,product_matches=product==g,
                    series=[[list(w),v] for w,v in g.items()],
                    difference=[[list(w),v] for w,v in diff.items()])
        Path('research/certificates/N8-class8/collect-failure.json').write_text(json.dumps(record,indent=2)+'\n')
        print('FAILURE SUMMARY',dict(word_length=len(word),used=len(used),
               bad_halls=[h for h in used if not h['correct_hall_value']],
               difference=len(diff),residual_identity=residual==ONE,product_matches=product==g),flush=True)
        captured.append(record)
        raise
m.collect=diagnose
try:decide_class8(m,target,[])
except AssertionError:
    if not captured:raise
    print('PASS N8 class8 collection failure reproduced and archived')
else:raise AssertionError('expected the saved failure')
