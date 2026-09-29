# Finite identity controls for the infinite symbolic example in the note.
# Boundary x_(n+1) is fixed in this finite model. It is NOT a computation
# of the infinite support closure; that conclusion uses the written proof.
n := 8;;
f := FreeGroup(2*(n+2));; gens := GeneratorsOfGroup(f);;
x := gens{[1..n+2]};; y := gens{[n+3..2*(n+2)]};;
h := [];;
for i in [1..n+1] do Add(h,x[i]*Comm(y[i+1],x[i+1])); od;
images := Concatenation(h,[x[n+2]],List([1..n+2],i->One(f)));;
pi := GroupHomomorphismByImages(f,f,gens,images);;
qimages := Concatenation(x,List([1..n+2],i->One(f)));;
q := GroupHomomorphismByImages(f,f,gens,qimages);;
if pi=fail or q=fail then Error("Free-group homomorphism failed"); fi;
for a in gens do
    if Image(pi,Image(pi,a))<>Image(pi,a) then Error("Not idempotent"); fi;
od;
for i in [1..n+1] do
    if Image(pi,h[i])<>h[i] or Image(q,h[i])<>x[i] then
        Error("Splitting identity failed");
    fi;
    exponents := List([1..Length(gens)],j->ExponentSumWord(h[i],gens[j]));;
    expected := List([1..Length(gens)],j->0);;
    expected[i]:=1;;
    if exponents<>expected then Error("Abelianization not diagonal"); fi;
    if Position(LetterRepAssocWord(h[i]),i+1)=fail then
        Error("Next x not in support");
    fi;
od;
# The deleted commutator stays nontrivial even in a class-two group.
unit := IdentityMat(3,Integers);; a := ShallowCopy(unit);;
a := List(unit,ShallowCopy);; b := List(unit,ShallowCopy);;
a[1][2]:=1;; b[2][3]:=1;;
if Comm(a,b)=unit then Error("Metabelian nontriviality control failed"); fi;
Print("PASS M4 support-chain controls: 20 idempotence identities, 9 lifts, UT3 separator\n");
QUIT;
