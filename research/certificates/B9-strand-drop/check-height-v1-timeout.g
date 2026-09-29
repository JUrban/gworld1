# Independent of CBraid and the Python matrix enumeration.
# GAP recomputes EVERY finite Burau image of a term of height <=5,
# checks the special term DAG as free words, and verifies the B5
# representatives using the faithful Artin action on F7.
Read("research/certificates/B9-strand-drop/height-counterexamples-v1.g");
n := 7;; F := FreeGroup(n);; x := GeneratorsOfGroup(F);;
pos := [];; neg := [];;
for i in [1..n-1] do
    y := ShallowCopy(x);; y[i] := x[i]*x[i+1]*x[i]^-1;; y[i+1] := x[i];;
    Add(pos,GroupHomomorphismByImagesNC(F,F,x,y));;
    y := ShallowCopy(x);; y[i] := x[i+1];; y[i+1] := x[i+1]^-1*x[i]*x[i+1];;
    Add(neg,GroupHomomorphismByImagesNC(F,F,x,y));;
od;
ActionWord := function(w)
    local out,j,aut;
    out := ShallowCopy(x);
    for j in Reversed(w) do
        if j>0 then aut:=pos[j]; else aut:=neg[-j]; fi;
        out := List(out,v->Image(aut,v));
    od;
    return out;
end;
EvalWord := function(w)
    local out,j;
    out := One(F);
    for j in w do out:=out*x[AbsInt(j)]^SignInt(j); od;
    return out;
end;
ShiftWord := w->List(w,j->SignInt(j)*(AbsInt(j)+1));;
ShelfWord := function(a,b)
    return Concatenation(a,ShiftWord(b),[1],List(Reversed(ShiftWord(a)),j->-j));
end;
for i in [1..Length(B9Terms)] do
    r := B9Terms[i];;
    if Length(r[3])=0 then
        if i<>1 or r[1]<>[] or r[2]<>0 then Error("Leaf"); fi;
    else
        if Length(r[3])<>2 or ForAny(r[3],j->j<1 or j>=i) then Error("Parents"); fi;
        u:=B9Terms[r[3][1]];; v:=B9Terms[r[3][2]];;
        if r[2]<>1+Maximum(u[2],v[2]) then Error("Height"); fi;
        if EvalWord(r[1])<>EvalWord(ShelfWord(u[1],v[1])) then Error("Term word"); fi;
    fi;
od;
if not IsPrimeInt(1000003) then Error("Prime"); fi;
ff:=GF(1000003);; one:=One(ff);; t:=2*one;; ident:=IdentityMat(n,ff);;
bpos:=[];; bneg:=[];;
for i in [1..n-1] do
    m:=IdentityMat(n,ff);; m[i][i]:=one-t;; m[i][i+1]:=t;;
    m[i+1][i]:=one;; m[i+1][i+1]:=Zero(ff);;
    Add(bpos,m);; Add(bneg,m^-1);;
od;
MatrixWord := function(w)
    local out,j;
    out:=IdentityMat(n,ff);
    for j in w do
        if j>0 then out:=out*bpos[j]; else out:=out*bneg[-j]; fi;
    od;
    return out;
end;
ShiftMatrix := function(a)
    local b,i,j;
    if a[n]<>ident[n] or List(a,r->r[n])<>List(ident,r->r[n]) then
        Error("Cannot shift this support");
    fi;
    b:=IdentityMat(n,ff);
    for i in [1..n-1] do for j in [1..n-1] do b[i+1][j+1]:=a[i][j]; od; od;
    return b;
end;
for i in [1..n-1] do
    if ActionWord([i,-i])<>x or MatrixWord([i,-i])<>ident then Error("Inverse"); fi;
    for j in [1..n-1] do
        if AbsInt(i-j)=1 and (ActionWord([i,j,i])<>ActionWord([j,i,j]) or
            MatrixWord([i,j,i])<>MatrixWord([j,i,j])) then Error("Braid relation"); fi;
        if AbsInt(i-j)>1 and (ActionWord([i,j])<>ActionWord([j,i]) or
            MatrixWord([i,j])<>MatrixWord([j,i])) then Error("Distant relation"); fi;
    od;
od;
# Exact recurrence S_0={I}, S_h={I} union {A sh(B) s1 sh(A)^-1}.
# All parents for h<=5 are supported in the top five coordinates,
# so shift is determined by these fixed-rank matrix images.
images:=[ident];; counts:=[1];;
for h in [1..5] do
    shifted:=List(images,ShiftMatrix);; inverses:=List(shifted,a->a^-1);;
    next:=[ident];;
    for i in [1..Length(images)] do
        for j in [1..Length(images)] do
            Add(next,images[i]*shifted[j]*bpos[1]*inverses[i]);
        od;
    od;
    images:=Set(next);; Add(counts,Length(images));;
    Print("height ",h," distinct finite images ",Length(images),"\n");
od;
if counts<>[1,2,4,10,52,1930] then Error("Unexpected closure counts"); fi;
witnessImages:=[];;
for i in [1..Length(B9Witnesses)] do
    c:=B9Witnesses[i];; r:=B9Terms[c[1]];;
    if r[2]<>6 or ForAny(c[2],j->j=0 or AbsInt(j)>4) then Error("Support/height"); fi;
    a:=ActionWord(r[1]);; b:=ActionWord(c[2]);;
    if a<>b then Error("Artin identity"); fi;
    if a[5]=x[5] then Error("Minimal strand negative control"); fi;
    m:=MatrixWord(c[2]);;
    if m<>MatrixWord(r[1]) or m in images then Error("Height separation failed"); fi;
    Add(witnessImages,m);;
    Print("witness ",i," term height 6, minimum strands 5, outside height<=5; Artin lengths ",
          List(a,Length),"\n");
od;
if Length(Set(witnessImages))<>11 then Error("Witness distinctness"); fi;
Print("PASS independent GAP B9 height counterexamples\n");
QUIT;
