# Independent checks of bounded braid-shelf records.
# GAP free-group substitutions check Artin actions; finite matrices give
# a separate (possibly nonfaithful) witness that records are distinct.
Read("research/certificates/B9/height4-fixtures.g");
F := FreeGroup(5);;
x := GeneratorsOfGroup(F);;
pos := [];; neg := [];;
for i in [1..4] do
    y := ShallowCopy(x);;
    y[i] := x[i]*x[i+1]*x[i]^-1;; y[i+1] := x[i];;
    Add(pos,GroupHomomorphismByImagesNC(F,F,x,y));;
    y := ShallowCopy(x);;
    y[i] := x[i+1];; y[i+1] := x[i+1]^-1*x[i]*x[i+1];;
    Add(neg,GroupHomomorphismByImagesNC(F,F,x,y));;
od;
ActionWord := function(w)
    local out,j,aut;
    out := ShallowCopy(x);
    for j in Reversed(w) do
        if j > 0 then aut := pos[j]; else aut := neg[-j]; fi;
        out := List(out,v->Image(aut,v));
    od;
    return out;
end;
MinimumStrands := function(out)
    local n,j,ok;
    for n in [1..5] do
        ok := true;
        for j in [1..5] do
            if j>n and out[j]<>x[j] then ok:=false; fi;
            if j<=n and ForAny(LetterRepAssocWord(out[j]),a->AbsInt(a)>n) then
                ok:=false;
            fi;
        od;
        if ok then return n; fi;
    od;
    Error("No ambient rank");
end;
ShiftWord := w->List(w,a->SignInt(a)*(AbsInt(a)+1));;
ShelfWord := function(a,b)
    return Concatenation(a,ShiftWord(b),[1],List(Reversed(ShiftWord(a)),v->-v));
end;
ff := GF(1000003);; one := One(ff);; t := 2*one;;
bpos := [];; bneg := [];;
for i in [1..4] do
    m := IdentityMat(5,ff);;
    m[i][i] := one-t;; m[i][i+1] := t;;
    m[i+1][i] := one;; m[i+1][i+1] := Zero(ff);;
    Add(bpos,m);; Add(bneg,m^-1);;
od;
MatrixWord := function(w)
    local out,j;
    out := IdentityMat(5,ff);
    for j in w do
        if j>0 then out:=out*bpos[j]; else out:=out*bneg[-j]; fi;
    od;
    return out;
end;
# Controls for both representations, including the braid relations.
for i in [1..4] do
    if ActionWord([i,-i])<>x or MatrixWord([i,-i])<>IdentityMat(5,ff) then
        Error("Inverse control failed");
    fi;
od;
for i in [1..3] do
    if ActionWord([i,i+1,i])<>ActionWord([i+1,i,i+1]) or
       MatrixWord([i,i+1,i])<>MatrixWord([i+1,i,i+1]) then
        Error("Braid relation failed");
    fi;
od;
for i in [1..4] do
    for j in [1..4] do
        if AbsInt(i-j)>1 and MatrixWord([i,j])<>MatrixWord([j,i]) then
            Error("Distant relation failed");
        fi;
    od;
od;
actions := [];; matrices := [];;
for r in B9Records do
    a := ActionWord(r[1]);;
    if MinimumStrands(a)<>r[4] then Error("Strand count disagreement"); fi;
    if Length(r[3])=2 then
        u := B9Records[r[3][1]];; v := B9Records[r[3][2]];;
        if r[2]<>Maximum(u[2],v[2])+1 or
           a<>ActionWord(ShelfWord(u[1],v[1])) then Error("Term mismatch"); fi;
    else
        if a<>x or r[2]<>0 then Error("Leaf mismatch"); fi;
    fi;
    Add(actions,a);; Add(matrices,MatrixWord(r[1]));;
od;
if Length(Set(actions))<>52 then Error("Distinctness failed"); fi;
# Check completeness of each finite-height closure independently.
for h in [1..4] do
    earlier := Filtered(B9Records,r->r[2]<h);;
    expected := Filtered([1..Length(B9Records)],j->B9Records[j][2]<=h);;
    obtained := [x];;
    for u in earlier do
        for v in earlier do Add(obtained,ActionWord(ShelfWord(u[1],v[1]))); od;
    od;
    if Set(obtained)<>Set(actions{expected}) then Error("Closure mismatch"); fi;
od;
Print("Artin distinct=",Length(Set(actions)),"; Burau mod 1000003 at t=2 distinct=",
      Length(Set(matrices)),"; counts by strands=",
      List([1..5],n->Number(B9Records,r->r[4]<=n)),"\n");
Print("PASS independent GAP bounded braid-shelf checks\n");
QUIT;
