#!/usr/bin/env python3
"""Bounded exact checks supporting the H4 output-size argument."""
from collections import deque
from itertools import product, permutations
import json
from pathlib import Path

OUT=Path('research/certificates/H4-output-size')
OUT.mkdir(parents=True,exist_ok=True)
assert not (OUT/'checks.json').exists()

def inverse(word): return tuple(-x for x in reversed(word))

def forbidden(rank,relators):
    result={(i,-i) for i in range(-rank,rank+1) if i}
    for relator in relators:
        for w in [tuple(relator),inverse(relator)]:
            for j in range(len(w)):
                v=w[j:]+w[:j]
                result.add(v[:len(w)//2+1])
    return result

def automaton(rank,relators):
    bad=forbidden(rank,relators)
    states={()}
    for f in bad:
        states.update(f[:j] for j in range(len(f)))
    # Some pattern prefixes themselves already contain a forbidden factor;
    # leave them unreachable rather than treating them as accepted states.
    states=sorted(states,key=lambda w:(len(w),w));index={s:i for i,s in enumerate(states)}
    alphabet=list(range(-rank,0))+list(range(1,rank+1))
    rows=[]
    for state in states:
        row=[]
        for a in alphabet:
            w=state+(a,)
            if any(len(f)<=len(w) and w[-len(f):]==f for f in bad):row.append(-1)
            else:
                tail=max((s for s in states if not s or w[-len(s):]==s),key=len)
                row.append(index[tail])
        rows.append(row)
    reachable={0};queue=deque([0])
    while queue:
        for b in rows[queue.popleft()]:
            if b>=0 and b not in reachable:reachable.add(b);queue.append(b)
    indegree={i:0 for i in reachable}
    for i in reachable:
        for b in rows[i]:
            if b>=0:indegree[b]+=1
    queue=deque(i for i in reachable if not indegree[i]);order=[]
    while queue:
        i=queue.popleft();order.append(i)
        for b in rows[i]:
            if b>=0:
                indegree[b]-=1
                if not indegree[b]:queue.append(b)
    acyclic=len(order)==len(reachable)
    m=rank+sum(map(len,relators));bound=1+2*rank+sum(len(w)**2 for w in relators)
    assert len(states)<=bound<=(m+1)**2
    longest=None;count=None
    if acyclic:
        length=[0]*len(states);ways=[0]*len(states);ways[0]=1
        for i in order:
            for b in rows[i]:
                if b>=0:length[b]=max(length[b],length[i]+1);ways[b]+=ways[i]
        longest=max(length);count=sum(ways);assert longest<len(states)
    def accepts(word):
        s=0
        for a in word:
            s=rows[s][alphabet.index(a)]
            if s<0:return False
        return True
    return dict(states=len(states),reachable=len(reachable),size=m,bound=bound,
                acyclic=acyclic,longest=longest,accepted_words=count),accepts,bad

def family(n):
    # x=1, t_i=i+2.
    return [[-(i+2),i+1,i+1] for i in range(1,n+1)]+[[n+2],[2,1,-2,-1,-1]]

records=[];fixtures=[];comparisons=0
for modulus in range(2,33):
    rels=[[1]*modulus];result,accept,bad=automaton(1,rels)
    assert result['acyclic'] and result['longest']==modulus//2
    assert result['accepted_words']==1+2*(modulus//2)
    residues={0}
    for sign in [-1,1]:
        for k in range(1,modulus+2):
            yes=accept([sign]*k);assert yes==(k<=modulus//2)
            if yes:assert (sign*k)%modulus;residues.add((sign*k)%modulus)
    assert len(residues)==modulus
    records.append(dict(case='cyclic_Dehn',order=modulus,**result))

# A finite group with a presentation which is not Dehn: C2^3.
rels=[[i,i] for i in range(1,4)]+[[-i,-j,i,j] for i in range(1,4) for j in range(i+1,4)]
result,accept,bad=automaton(3,rels)
assert not result['acyclic'] and accept([1,2,3,1,2,3])
records.append(dict(case='C2_cubed_non_Dehn',irreducible_identity=[1,2,3]*2,**result))
result,accept,bad=automaton(1,[])
assert not result['acyclic'] and all(accept([1]*k) for k in range(20))
records.append(dict(case='infinite_cyclic_control',**result))

for n in range(1,11):
    rank=n+2;rels=family(n);Q=2**n;M=2**Q-1
    result,accept,bad=automaton(rank,rels)
    assert result['size']==4*n+8 and not result['acyclic']
    # Exact pair multiplication for C_M semidirect C_Q, with t*x*t^-1=x^2.
    def mul(a,b):return ((a[0]+pow(2,a[1],M)*b[0])%M,(a[1]+b[1])%Q)
    def inv(a):return ((-pow(pow(2,a[1],M),-1,M)*a[0])%M,-a[1]%Q)
    generators=[(1,0)]+[(0,2**i%Q) for i in range(n+1)]
    for w in rels:
        value=(0,0)
        for a in w:value=mul(value,generators[a-1] if a>0 else inv(generators[-a-1]))
        assert value==(0,0)
    if n<=3:
        assert accept([1]*M)
        reached={(0,0)};queue=deque(reached)
        while queue:
            value=queue.popleft()
            for generator in generators[:2]:
                nxt=mul(value,generator)
                if nxt not in reached:reached.add(nxt);queue.append(nxt)
        assert len(reached)==M*Q
    fixtures.append([n,rank,rels,M,Q,M*Q])
    records.append(dict(case='short_finite_family',n=n,Q=Q,M=str(M),order=str(M*Q),**result))

# Compare the prefix automaton with a separate direct substring scan.
for rank,rels in [(1,[[1]*7]),(2,[[1,1],[2,2],[-1,-2,1,2]]),(3,family(1))]:
    result,accept,bad=automaton(rank,rels)
    alphabet=list(range(-rank,0))+list(range(1,rank+1))
    for length in range(6):
        for word in product(alphabet,repeat=length):
            direct=not any(word[j:j+len(f)]==f for f in bad for j in range(len(word)-len(f)+1))
            assert accept(word)==direct;comparisons+=1

(OUT/'checks.json').write_text(json.dumps(dict(records=records,substring_comparisons=comparisons),indent=2)+'\n')
(OUT/'fixtures.g').write_text('H4Fixtures := '+json.dumps(fixtures)+';\n')
print('PASS H4 output-size:',len(records),'cases;',comparisons,'independent substring comparisons')
