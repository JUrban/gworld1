# Extract one actual input word from the smallest failed profile lift.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
f:=FreeGroup(3);; x:=GeneratorsOfGroup(f);; rel:=[];;
for i in [1..2] do
    for j in [i+1..3] do
        for tail in Tuples([i,j],2) do
            w:=Comm(x[j],x[i]);;
            for k in tail do w:=Comm(w,x[k]); od;
            Add(rel,w);
        od;
    od;
od;
p:=f/rel;; ep:=NqEpimorphismNilpotentQuotient(p,6);;
g:=Image(ep);; tor:=TorsionSubgroup(g);;
if Size(tor)<>2 then Error("Unexpected torsion"); fi;
z:=GeneratorsOfGroup(tor)[1];;
Print("COORDINATES ",ExponentsByPcp(Pcp(g),z),"\n");
word:=PreImagesRepresentative(ep,z);;
if Image(ep,word)<>z then Error("Preimage mismatch"); fi;
Print("WORD ",LetterRepAssocWord(UnderlyingElement(word)),"\n");
Print("PASS N3 class-six profile-lift witness extracted\n");
QUIT;
