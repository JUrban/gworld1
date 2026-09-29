# A negative control for confusing a metabelian quotient with its cover.
# All assertions are exact; no unbounded or heuristic group search.
F := FreeGroup("a", "b");;
a := F.1;; b := F.2;;
rels := [a^4,b^2,(a*b)^3];;
c := Comm(a,b);; d := Comm(c,c^a);;
G := F / rels;;
Q := F / Concatenation(rels,[d]);;
if Size(G) <> 24 or Size(Q) <> 6 then
  Error("Unexpected ordinary presentation orders");
fi;
S := Group((1,2,3,4),(1,2));;
hom := GroupHomomorphismByImages(G,S,GeneratorsOfGroup(G),[(1,2,3,4),(1,2)]);;
if hom = fail or not IsBijective(hom) then Error("Presentation mismatch"); fi;
aa := (1,2,3,4);; bb := (1,2);;
cc := Comm(aa,bb);; dd := Comm(cc,cc^aa);;
D2 := DerivedSubgroup(DerivedSubgroup(S));;
N := NormalClosure(S,Group(dd));;
if Size(D2) <> 4 or N <> D2 or dd = () then Error("Kernel control failed"); fi;
Squot := S/N;;
if Size(DerivedSubgroup(DerivedSubgroup(Squot))) <> 1 then Error("Quotient not metabelian"); fi;
if Size(DerivedSubgroup(DerivedSubgroup(Q))) <> 1 then Error("Fp quotient not metabelian"); fi;
Print("S4 double commutator: ",dd,"; derived kernel order: ",Size(N),"\n");
Print("Ordinary presentation orders: ",Size(G),", ",Size(Q),"\n");
Print("PASS: nonmetabelian solvable cover has certified metabelian quotient\n");
QUIT;
