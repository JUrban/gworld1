# Exact checks of the explicit maps in Dlugie, arXiv:2607.13316, Prop.2.3.
# This verifies the finite presentation identities, not residual finiteness.
# Braid multiplication acts by rho(uv)=rho(u) composed with rho(v).
F := FreeGroup(4);;
fg := GeneratorsOfGroup(F);;
pos := [];; neg := [];;
for i in [1..3] do
    yy := ShallowCopy(fg);;
    yy[i] := fg[i]*fg[i+1]*fg[i]^-1;; yy[i+1] := fg[i];;
    Add(pos,GroupHomomorphismByImagesNC(F,F,fg,yy));;
    yy := ShallowCopy(fg);;
    yy[i] := fg[i+1];; yy[i+1] := fg[i+1]^-1*fg[i]*fg[i+1];;
    Add(neg,GroupHomomorphismByImagesNC(F,F,fg,yy));;
od;
BraidAction := function(w)
    local out, letter, aut;
    out := ShallowCopy(fg);
    for letter in Reversed(w) do
        if letter>0 then aut:=pos[letter]; else aut:=neg[-letter]; fi;
        out := List(out,t->Image(aut,t));
    od;
    return out;
end;
InvWord := w->List(Reversed(w),i->-i);;
xx := [-1,3];; yy := [2,-1,3,-2];;
images := [[xx,Concatenation(InvWord(xx),yy)],
           [yy,Concatenation(yy,InvWord(xx),yy)]];;
for i in [1..2] do
    for j in [1..2] do
        lhs := Concatenation([i],[xx,yy][j],[-i]);;
        if BraidAction(lhs)<>BraidAction(images[i][j]) then
            Error("B4 conjugation identity failed");
        fi;
    od;
od;
# Negative control: the incorrect x rather than x^-1 in phi(sigma_1)(y).
if BraidAction([1,2,-1,3,-2,-1])=BraidAction(Concatenation(xx,yy)) then
    Error("Sign-error negative control failed");
fi;

K := FreeGroup(2);; kg := GeneratorsOfGroup(K);; x := kg[1];; y := kg[2];;
mp := [GroupHomomorphismByImagesNC(K,K,kg,[x,x^-1*y]),
       GroupHomomorphismByImagesNC(K,K,kg,[y,y*x^-1*y])];;
mn := [GroupHomomorphismByImagesNC(K,K,kg,[x,x*y]),
       GroupHomomorphismByImagesNC(K,K,kg,[x*y^-1*x,x])];;
Modular := function(q,w)
    local out, letter, aut;
    out := w;
    for letter in Reversed(q) do
        if letter>0 then aut:=mp[letter]; else aut:=mn[-letter]; fi;
        out := Image(aut,out);
    od;
    return out;
end;
for i in [1..2] do
    for w in kg do
        if Modular([i,-i],w)<>w or Modular([-i,i],w)<>w then
            Error("Modular inverse failed");
        fi;
    od;
od;
if List(kg,w->Modular([1,2,1],w))<>List(kg,w->Modular([2,1,2],w)) then
    Error("Modular braid relation failed");
fi;
PairMul := function(a,b)
    return [a[1]*Modular(a[2],b[1]),Concatenation(a[2],b[2])];
end;
PairEq := function(a,b)
    return a[1]=b[1] and BraidAction(a[2])=BraidAction(b[2]);
end;
sp := [[One(K),[1]],[One(K),[2]],[x,[1]]];;
for i in [1..2] do
    if not PairEq(PairMul(PairMul(sp[i],sp[i+1]),sp[i]),
                  PairMul(PairMul(sp[i+1],sp[i]),sp[i+1])) then
        Error("Semidirect-product braid relation failed");
    fi;
od;
if not PairEq(PairMul(sp[1],sp[3]),PairMul(sp[3],sp[1])) then
    Error("Semidirect-product commuting relation failed");
fi;
# Both maps on the kernel generators, and recovery of sigma_3.
sx := PairMul([One(K),[-1]],sp[3]);;
sy := PairMul(PairMul(sp[2],sx),[One(K),[-2]]);;
if not PairEq(sx,[x,[]]) or not PairEq(sy,[y,[]]) then
    Error("Kernel generators were not recovered");
fi;
if BraidAction(Concatenation([1],xx))<>BraidAction([3]) then
    Error("Third braid generator was not recovered");
fi;
Print("Checked four B4 conjugations, modular inverses and braid relation,\n",
      "three B4 relations in the semidirect product, and generator inverses;\n",
      "incorrect-sign negative control detected.\n");
Print("PASS FP21 explicit braid splitting identities\n");
QUIT;
