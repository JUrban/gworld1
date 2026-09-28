#!/usr/bin/env python3
"""Deterministic class-five fixtures covering leading degrees, gauges and controls."""
import json,random,time
from collections import Counter
from pathlib import Path
from n8_class5 import solve,bases,wcomm,wpow,reduced,expansion,comm,layer

SEED=9282605;rng=random.Random(SEED);fixtures=[];counts=Counter();gauges=[]
def rw(rank,length=4):return [rng.choice((-1,1))*rng.randrange(1,rank+1) for _ in range(length)]
def rl(basis,terms=2):
    return reduced(s for _ in range(terms) for s in wpow(rng.choice(basis),rng.choice((-1,1)))) if basis else []
def check(rank,word,expected,label):
    started=time.monotonic();ans=solve(word,rank)
    assert ans['answer']==expected,(rank,label,word,ans)
    counts[ans['case']+(' yes' if expected else ' no')]+=1
    fixtures.append([rank,word,expected,ans.get('x',[]),ans.get('y',[])])
    if 'period' in ans:gauges.append({'label':label,'rank':rank,'period':ans['period'],'residue':ans['residue']})
    print(json.dumps({'case':len(fixtures),'label':label,'rank':rank,'result':ans['case'],
                      'seconds':round(time.monotonic()-started,3),
                      'period':ans.get('period'),'residue':ans.get('residue')}),flush=True)

for rank in range(1,5):
    bb=bases(rank)
    expected=[rank,rank*(rank-1)//2,(rank**3-rank)//3,(rank**4-rank**2)//4]
    assert [len(bb[i]) for i in range(1,5)]==expected
    check(rank,[],True,'identity');check(rank,[1],False,'outside derived')
for rank in (2,3):
    bb=bases(rank)
    for k in range(4):
        check(rank,wcomm(rw(rank)+rl(bb[2],1),rw(rank)+rl(bb[3],1)),True,'general commutator')
        check(rank,wcomm(rw(rank),rl(bb[2])+rl(bb[3],1)),True,'leading degree three')
        check(rank,wcomm(rw(rank)+rl(bb[2],1),rl(bb[3])+rl(bb[4],1)),True,'leading degree four 13')
        check(rank,wcomm(rl(bb[2])+rl(bb[3],1),rl(bb[2])+rl(bb[3],1)),True,'leading degree four 22')
        check(rank,wcomm(rw(rank),rl(bb[4])),True,'central 14')
        check(rank,wcomm(rl(bb[2]),rl(bb[3])),True,'central 23')
bb=bases(2)
for k in (1,2,3):
    check(2,wcomm([1,1]+wpow(bb[3][0],k),[2,2]),True,'nonprimitive degree-two gauge')
    check(2,wcomm([1]+wpow(bb[2][0],k),wpow(bb[2][0],3)+list(bb[3][0])),True,'nonprimitive degree-three gauge')
bb=bases(4)
check(4,wcomm([1,2,3],[4,2]),True,'rank-four general')
check(4,wcomm(wcomm([1],[2])+list(bb[3][0]),wcomm([3],[4])),True,'rank-four leading 22')
check(4,wcomm(wcomm([1],[2]),wcomm(wcomm([3],[4]),[2])),True,'rank-four central 23')
check(2,wpow(wcomm([1],[2]),2),False,'known square obstruction in class-three quotient')
check(4,wcomm([1],[2])+wcomm([3],[4]),False,'rank-four exterior obstruction')
check(3,wcomm(wcomm([1],[2]),[3])+wcomm(wcomm([1],[3]),[2]),False,'class-three tensor obstruction')
c=wcomm([1],[2]);quartic=wcomm(wcomm(c,[1]),[1])+wcomm(wcomm(c,[2]),[2])
check(2,quartic,False,'class-four irreducible quadratic obstruction')
def ad4(a,b):return wcomm(a,wcomm(a,wcomm(a,wcomm(a,b))))
check(2,ad4([1],[2])+ad4([2],[1]),False,'degree-five extreme-weight obstruction')
out=Path(__file__).resolve().parents[1]/'research/certificates/N8-class5';out.mkdir(parents=True,exist_ok=True)
assert not (out/'fixtures.json').exists()
(out/'fixtures.json').write_text(json.dumps({'seed':SEED,'fixtures':fixtures,'gauges':gauges},indent=2)+'\n')
(out/'fixtures.g').write_text('N8Fixtures := '+json.dumps(fixtures)+';\n')
print(json.dumps({'seed':SEED,'cases':len(fixtures),'counts':dict(counts),'gauges':gauges},sort_keys=True))
print('PASS N8 class-five exact checks')
