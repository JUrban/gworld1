# Independent finite-field check of the B9 height-five lower bound.
# Certify specialness by exact free-word parent identities, and distinguish
# braids by a representation. No faithfulness of Burau is assumed.
Read("research/certificates/B9/height5-burau-fixtures.g");
F := FreeGroup(B9Rank-1);;
fg := GeneratorsOfGroup(F);;
EvalWord := function(w)
    local out,a;
    out := One(F);
    for a in w do out := out*fg[AbsInt(a)]^SignInt(a); od;
    return out;
end;
ShiftWord := w->List(w,a->SignInt(a)*(AbsInt(a)+1));;
ShelfWord := function(a,b)
    return Concatenation(a,ShiftWord(b),[1],List(Reversed(ShiftWord(a)),v->-v));
end;
if not IsPrimeInt(1000003) then Error("Modulus is not prime"); fi;
ff := GF(1000003);; one := One(ff);; t := 2*one;;
pos := [];; neg := [];;
for i in [1..B9Rank-1] do
    m := IdentityMat(B9Rank,ff);;
    m[i][i] := one-t;; m[i][i+1] := t;;
    m[i+1][i] := one;; m[i+1][i+1] := Zero(ff);;
    Add(pos,m);; Add(neg,m^-1);;
od;
MatrixWord := function(w)
    local out,j;
    out := IdentityMat(B9Rank,ff);
    for j in w do
        if j>0 then out:=out*pos[j]; else out:=out*neg[-j]; fi;
    od;
    return out;
end;
for i in [1..B9Rank-1] do
    if MatrixWord([i,-i])<>IdentityMat(B9Rank,ff) then Error("Inverse"); fi;
    for j in [1..B9Rank-1] do
        if AbsInt(i-j)=1 and MatrixWord([i,j,i])<>MatrixWord([j,i,j]) then
            Error("Braid relation");
        fi;
        if AbsInt(i-j)>1 and MatrixWord([i,j])<>MatrixWord([j,i]) then
            Error("Distant relation");
        fi;
    od;
od;
matrices := [];;
for i in [1..Length(B9Records)] do
    r := B9Records[i];;
    if ForAny(r[1],a->a=0 or AbsInt(a)>=B9Rank) then Error("Strands"); fi;
    if Length(r[3])=0 then
        if i<>1 or r[1]<>[] or r[2]<>0 then Error("Leaf"); fi;
    else
        if Length(r[3])<>2 or ForAny(r[3],j->j<1 or j>=i) then Error("Parents"); fi;
        u := B9Records[r[3][1]];; v := B9Records[r[3][2]];;
        if r[2]<>1+Maximum(u[2],v[2]) then Error("Height"); fi;
        if EvalWord(r[1])<>EvalWord(ShelfWord(u[1],v[1])) then Error("Word"); fi;
    fi;
    Add(matrices,MatrixWord(r[1]));;
od;
if Length(matrices)<>B9LowerBound or Length(Set(matrices))<>B9LowerBound then
    Error("Distinctness");
fi;
Print("Certified ",B9LowerBound," distinct special braids in B_",B9Rank,
      "; heights <= ",Maximum(List(B9Records,r->r[2])),"\n");
Print("PASS independent GAP finite Burau lower bound\n");
QUIT;
