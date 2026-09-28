#!/usr/bin/env python3
"""Deterministic checks spanning all cases of the class-four candidate."""
import json,random
from pathlib import Path
from collections import Counter
from n8_class4 import solve, bases, wcomm, wpow

rng=random.Random(9282604)
fixtures=[]
counts=Counter()

def randomword(rank,length=7):
    return [rng.choice((-1,1))*rng.randrange(1,rank+1) for _ in range(length)]

def randomlayer(basis):
    return [s for w in basis for s in wpow(w,rng.randrange(-2,3))]

def check(rank,word,expected,label):
    ans=solve(word,rank)
    assert ans['answer']==expected,(rank,label,word,ans)
    counts[ans['case']+(' yes' if expected else ' no')]+=1
    fixtures.append([rank,word,expected,ans.get('x',[]),ans.get('y',[])])

for rank in range(1,5):
    check(rank,[],True,'identity')
    check(rank,[1],False,'outside derived')
for rank in range(2,5):
    b2,b3=bases(rank)
    for k in range(8):
        check(rank,wcomm(randomword(rank),randomword(rank)),True,'general commutator')
        check(rank,wcomm(randomword(rank),wcomm(randomword(rank),randomword(rank))),True,'degree3 leading')
        check(rank,wcomm(randomword(rank),randomlayer(b3)),True,'degree4 (1,3)')
        check(rank,wcomm(randomlayer(b2),randomlayer(b2)),True,'degree4 (2,2)')
check(2,wpow(wcomm([1],[2]),2),False,'known square obstruction')
check(4,wcomm([1],[2])+wcomm([3],[4]),False,'rank-four exterior image')
check(3,wcomm(wcomm([1],[2]),[3])+wcomm(wcomm([1],[3]),[2]),False,'nonfactorable degree3')
c=wcomm([1],[2])
quartic=wcomm(wcomm(c,[1]),[1])+wcomm(wcomm(c,[2]),[2])
check(2,quartic,False,'irreducible binary quadratic in central degree4')
out=Path(__file__).resolve().parents[1]/'research/certificates/N8-class4'
out.mkdir(parents=True,exist_ok=True)
(out/'fixtures.json').write_text(json.dumps({'seed':9282604,'fixtures':fixtures},indent=2)+'\n')
(out/'fixtures.g').write_text('N8Fixtures := '+json.dumps(fixtures)+';\n')
print(json.dumps({'seed':9282604,'cases':len(fixtures),'counts':dict(counts)},sort_keys=True))
print('PASS N8 class-four exact checks')
