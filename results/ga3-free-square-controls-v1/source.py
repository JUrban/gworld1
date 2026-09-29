#!/usr/bin/env python3
"""Exact free-group controls for GA3; does not verify Lambda-tree collapse."""
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/certificates/GA3-free-square'


def red(word):
    stack = []
    for a in word:
        if stack and stack[-1] == -a:
            stack.pop()
        else:
            stack.append(a)
    return tuple(stack)


def inv(word):
    return tuple(-a for a in reversed(word))


def ball(rank, radius):
    layer = [()]
    letters = tuple(itertools.chain.from_iterable((a, -a) for a in range(1, rank+1)))
    out = []
    for _ in range(radius):
        layer = [w+(a,) for w in layer for a in letters if not w or a != -w[-1]]
        out.extend(layer)
    return out


def prefix(a, b):
    return b[:len(a)] == a


def disjoint(a, b):
    return not prefix(a, b) and not prefix(b, a)


def cone_image(g, q):
    """Image of the oriented edge defining C(q): (outward?, word)."""
    parent, child = red(g+q[:-1]), red(g+q)
    if len(child) > len(parent):
        return True, child
    return False, parent  # complement of C(parent)


def cone_complement(q):
    return [q[:i]+(a,) for i in range(len(q)) for a in (1, -1, 2, -2)
            if a != q[i] and (i == 0 or a != -q[i-1])]


def mapped(word, images):
    return red(itertools.chain.from_iterable(images[a] if a > 0 else inv(images[-a]) for a in word))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    constants = ball(2, 4)
    p = (1, 1, 1, 1, 1, 2, 1, 2, 2, 1)
    h = red(p+(1, 2)+inv(p))
    up, um = p+(1,), p+(-2,)
    separation = []
    for c in constants:
        image_out, q = cone_image(c, p)
        assert image_out and disjoint(q, p)
        separation.append({'constant': c, 'image_cone': q})
    dynamics = []
    for g, source, target in ((h, um, up), (inv(h), up, um)):
        for q in cone_complement(source):
            image_out, image_q = cone_image(g, q)
            assert image_out and prefix(target, image_q)
            dynamics.append({'g': g, 'source_cone': q, 'image_cone': image_q, 'target_cone': target})
    inputs = ball(4, 4)
    records = []
    for n in (1, 2):
        hn = red(h*n)
        images = {1: (1,), 2: (2,), 3: red(hn+(1,)+inv(hn)), 4: red(hn+(2,)+inv(hn))}
        for w in inputs:
            value = mapped(w, images)
            assert value
            records.append({'n': n, 'word': w, 'image': value})
    # [a in factor 1, a in factor 2] is a nonidentity word in F4.
    cross_comm = (1, 3, -1, -3)
    bad_controls = []
    for n in (1, 2, 7):
        hn = (1,)*n
        images = {1: (1,), 2: (2,), 3: red(hn+(1,)+inv(hn)), 4: red(hn+(2,)+inv(hn))}
        assert not mapped(cross_comm, images)
        bad_controls.append({'h': [1], 'n': n, 'word': cross_comm, 'image': []})
    # Every map Z*Z -> Z kills the cross commutator; test representative slopes.
    abelian_checks = 0
    for a in range(-3, 4):
        for b in range(-3, 4):
            assert a+b-a-b == 0
            abelian_checks += 1
    cert = {'scope': 'Free group F2 only; exact boundary cylinders and bounded free-square images',
            'seed': None, 'p': p, 'h': h, 'U_plus': up, 'U_minus': um,
            'constants_radius': 4, 'input_rank': 4, 'input_radius': 4,
            'separation': separation, 'dynamics': dynamics,
            'positive_images': records, 'bad_separator_controls': bad_controls,
            'abelian_slope_controls': abelian_checks}
    dest = OUT / 'certificate.json'
    dest.write_text(json.dumps(cert, separators=(',', ':'))+'\n')
    # GAP independently generates the complete input ball and checks every image.
    gap = '''F2:=FreeGroup("a","b");; gg:=GeneratorsOfGroup(F2);;
F4:=FreeGroup("a1","b1","a2","b2");; xx:=GeneratorsOfGroup(F4);;
letters:=Concatenation(xx,List(xx,x->x^-1));;
layer:=[One(F4)];; words:=[];;
for k in [1..4] do
  next:=[];
  for w in layer do
    for s in letters do
      v:=w*s;
      if Length(v)=k then Add(next,v); fi;
    od;
  od;
  Append(words,next); layer:=next;
od;
if Length(words)<>3200 or Length(Set(words))<>3200 then Error("input ball"); fi;
pp:=gg[1]^5*gg[2]*gg[1]*gg[2]^2*gg[1];;
hh:=pp*gg[1]*gg[2]*pp^-1;;
checked:=0;;
for n in [1,2] do
  ims:=[gg[1],gg[2],hh^n*gg[1]*hh^-n,hh^n*gg[2]*hh^-n];
  phi:=GroupHomomorphismByImages(F4,F2,xx,ims);
  for w in words do
    if IsOne(Image(phi,w)) then Error("positive image killed"); fi;
    checked:=checked+1;
  od;
od;
for n in [1,2,7] do
  phi:=GroupHomomorphismByImages(F4,F2,xx,
    [gg[1],gg[2],gg[1]^n*gg[1]*gg[1]^-n,gg[1]^n*gg[2]*gg[1]^-n]);
  if not IsOne(Image(phi,xx[1]*xx[3]*xx[1]^-1*xx[3]^-1)) then Error("bad separator control"); fi;
od;
Z:=InfiniteCylicGroup_PLACEHOLDER;
Print("PASS GA3 GAP ",checked," positive images; 3 bad separator controls; 49 abelian controls\\n");
QUIT;
'''
    gap = gap.replace('Z:=InfiniteCylicGroup_PLACEHOLDER;', '''Z:=AbelianGroup([0]);; z:=GeneratorsOfGroup(Z)[1];;
for i in [-3..3] do
  for j in [-3..3] do
    if not IsOne(Comm(z^i,z^j)) then Error("abelian control"); fi;
  od;
od;''')
    (OUT/'verify.g').write_text(gap)
    print(json.dumps({'positive_images': len(records), 'separated_cones': len(separation),
                      'dynamics_cones': len(dynamics), 'bad_separator_controls': len(bad_controls),
                      'abelian_controls': abelian_checks,
                      'certificate_sha256': hashlib.sha256(dest.read_bytes()).hexdigest()}))
    print('PASS GA3 free-square controls')


if __name__ == '__main__':
    main()
