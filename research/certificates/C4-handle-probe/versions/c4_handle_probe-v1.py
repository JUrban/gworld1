#!/usr/bin/env python3
"""Exact Dfo FullHRed implementation and bounded deterministic slow-input probe.

Generators are signed integers. A step removes the first-ending handle, applies
Dfo (1.4), then completely freely reduces. Input free reduction is recorded
separately. This is neither GreedyHRed nor the reversed-index Dhn variant.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import random

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/certificates/C4-handle-probe'


def decode(s):
    return tuple((ord(c.lower())-ord('a')+1)*(1 if c.islower() else -1) for c in s)


def encode(word):
    return ''.join(chr(ord('a')+abs(x)-1).upper() if x<0 else chr(ord('a')+x-1) for x in word)


def inverse(word): return tuple(-x for x in reversed(word))


def free(word):
    out=[]
    for x in word:
        assert isinstance(x,int) and x!=0
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)


def first_handle(word):
    last={}
    for q,x in enumerate(word):
        j=abs(x);p=last.get(j)
        if p is not None and word[p]==-x and last.get(j-1,-1)<p:
            signs={v//abs(v) for v in word[p+1:q] if abs(v)==j+1}
            assert len(signs)<=1,('nonpermitted first handle',word,p,q)
            return p,q
        last[j]=q
    return None


def step(word,p,q):
    j=abs(word[p]); e=word[p]//j
    assert word[q]==-word[p]
    assert all(abs(x) not in (j-1,j) for x in word[p+1:q])
    assert len({x//abs(x) for x in word[p+1:q] if abs(x)==j+1})<=1
    middle=[];expanded=0
    for x in word[p+1:q]:
        if abs(x)==j+1:
            middle.extend((-e*(j+1),(x//abs(x))*j,e*(j+1)));expanded+=1
        else:middle.append(x)
    raw=word[:p]+tuple(middle)+word[q+1:]
    result=free(raw)
    assert sum(result)==sum(raw)  # only a free-reduction check, not writhe
    assert sum(x//abs(x) for x in result)==sum(x//abs(x) for x in word)
    return result,{'p':p,'q':q,'generator':j,'expanded_adjacent_letters':expanded,
        'raw_length':len(raw),'after_length':len(result),'free_cancellations':(len(raw)-len(result))//2}


def run(word,max_steps=20000,max_length=20000,trace=False):
    original=tuple(word);word=free(word)
    record={'input':list(original),'input_length':len(original),'initial_free_length':len(word),
      'initial_free_cancellations':(len(original)-len(word))//2,'steps':0,
      'expanded_adjacent_letters':0,'peak_after_free':len(word),'peak_raw':len(word),
      'total_scanned_handle_letters':0,'status':'complete'}
    width=1+max(map(abs,word),default=0)
    if trace:record['trace']=[]
    while True:
        h=first_handle(word)
        if h is None:break
        if record['steps']>=max_steps:
            record['status']='step_limit';break
        result,info=step(word,*h)
        record['steps']+=1
        record['expanded_adjacent_letters']+=info['expanded_adjacent_letters']
        record['total_scanned_handle_letters']+=h[1]-h[0]-1
        record['peak_raw']=max(record['peak_raw'],info['raw_length'])
        record['peak_after_free']=max(record['peak_after_free'],len(result))
        if width<=3:assert len(result)<=len(word)
        if trace:
            info['word_sha256']=hashlib.sha256(encode(result).encode()).hexdigest()
            record['trace'].append(info)
        word=result
        if len(word)>max_length:
            record['status']='length_limit';break
    record['output']=list(word)
    if record['status']=='complete':assert first_handle(word) is None
    return record


PUBLISHED=['ABacBCBaCbaa','bABcBCBaCbaa','bbABcbABCbABCbaa','bbAcbCABCbABCbaa',
    'bbAcbCAcBCABCbaa','bbAcbABCABCbaa','bbAcbABCAcBCaa','bbAcbABABCaa',
    'bbAcbAABCa','bbAcbAbABC']


def audit():
    word=decode(PUBLISHED[0]);actual=[encode(word)]
    while (h:=first_handle(word)) is not None:
        word,_=step(word,*h);actual.append(encode(word))
    assert actual==PUBLISHED,(actual,PUBLISHED)
    # A forbidden main handle from Dfo must not be chosen before the nested one.
    w=decode('abcBA');assert first_handle(w)==(1,3)
    assert run(w)['output']==list(decode('CBabc'))
    for w in ['', 'aA','Aa','abAB','abaBAB','acAC','abcCBA']:
        r=run(decode(w));assert r['status']=='complete'
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'published-trace.json').write_text(json.dumps(run(decode(PUBLISHED[0]),trace=True),indent=2)+'\n')
    print('PASS C4 exact published nine-step FullHRed trace and boundary controls',flush=True)


def reduced_words(k,n):
    alphabet=tuple(range(1,k+1))+tuple(range(-1,-k-1,-1))
    if n==0:
        yield ();return
    for prefix in reduced_words(k,n-1):
        for x in alphabet:
            if not prefix or prefix[-1]!=-x:yield prefix+(x,)


def score(r):return (r['expanded_adjacent_letters'],r['steps'],r['peak_after_free'])


def probe():
    audit();rng=random.Random(20260929)
    summary={'scope':'Bounded observations only; no asymptotic C4 conclusion.',
      'seed':20260929,'limits':{'steps_per_word':20000,'length_per_word':20000},
      'exhaustive':[],'families':[],'evolution':[],'capped':[]}
    champions={};total=0
    def observe(w):
        nonlocal total
        r=run(w);total+=1
        if r['status']!='complete':summary['capped'].append(r)
        width=1+max(map(abs,w),default=0)
        if width not in champions or score(r)>score(champions[width]):champions[width]=r
        return r
    for k,bound in [(2,8),(3,6)]:
        for n in range(1,bound+1):
            count=0;best=None
            for w in reduced_words(k,n):
                r=observe(w);count+=1
                if best is None or score(r)>score(best):best=r
            summary['exhaustive'].append({'strands':k+1,'length':n,'count':count,'best':best})
            print('exhaustive',k+1,n,count,'best',score(best),flush=True)
    # The first pattern gives the original paper's known quadratic B3 family.
    patterns=[decode(s) for s in ['bbaa','abC','abCB','abCBA','abcb','aBc','abcB','abCbc','abCdcB','abCD','abCd']]
    for p in patterns:
        for central in range(1,1+max(map(abs,p))):
            for m in [1,2,4,8,16,24]:
                u=p*m;w=free(u+(central,)+inverse(u))
                r=observe(w)
                summary['families'].append({'conjugator_pattern':encode(p),'central_generator':central,'power':m,'record':r})
    for k in [3,4]:
        alphabet=tuple(range(1,k+1))+tuple(range(-1,-k-1,-1))
        for length in [24,48,96]:
            current=tuple(rng.choice(alphabet) for _ in range(length));r=observe(free(current));best=r
            for trial in range(1500):
                if trial%150==0:current=tuple(rng.choice(alphabet) for _ in range(length));r=observe(free(current))
                candidate=list(current)
                for _ in range(1 if rng.random()<0.8 else 3):candidate[rng.randrange(length)]=rng.choice(alphabet)
                candidate=tuple(candidate);test=observe(free(candidate))
                if score(test)>=score(r) or rng.random()<0.015:current=candidate;r=test
                if score(test)>score(best):best=test
            summary['evolution'].append({'strands':k+1,'raw_length':length,'trials':1500,'best':best})
            print('evolution',k+1,length,'best',score(best),'actual length',best['input_length'],flush=True)
    summary['total_evaluated']=total
    summary['champions']={str(k):run(r['input'],trace=True) for k,r in champions.items()}
    (OUT/'probe.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('PASS C4 bounded probe completed',total,'evaluations;',len(summary['capped']),'capped observations',flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['audit','probe']);a=p.parse_args()
    audit() if a.mode=='audit' else probe()
