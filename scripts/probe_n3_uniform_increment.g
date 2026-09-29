# Does increasing EVERY nonempty profile bound by one kill torsion in the
# canonical image? Target pair=2, full=6; source pair=3, full=7.
# Singleton bounds 1 versus 2 make no difference for cyclic coordinate groups.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
Read("research/certificates/N3-profile-lift-class6/fixtures.g");
N3IncrementEval:=function(gens,word)
    local z,s;
    z:=One(gens[1]);
    for s in word do z:=z*gens[AbsInt(s)]^SignInt(s); od;
    return z;
end;
f:=FreeGroup(3);; x:=GeneratorsOfGroup(f);;
rel:=List(N3LiftCertificate.source_relations,w->N3IncrementEval(x,w));;
p:=f/rel;; ep:=NqEpimorphismNilpotentQuotient(p,7);; g:=Image(ep);;
y:=List(GeneratorsOfGroup(p),a->Image(ep,a));;
rel:=List(N3LiftCertificate.target_relations,w->N3IncrementEval(x,w));;
q:=f/rel;; eq:=NqEpimorphismNilpotentQuotient(q,6);; h:=Image(eq);;
v:=List(GeneratorsOfGroup(q),a->Image(eq,a));;
phi:=GroupHomomorphismByImagesNC(g,h,y,v);;
tor:=TorsionSubgroup(g);; image:=Image(phi,tor);;
Print("Source torsion order ",Size(tor),"; target image order ",Size(image),"\n");
for z in GeneratorsOfGroup(tor) do
    if Image(phi,z)<>One(h) then
        word:=PreImagesRepresentative(ep,z);;
        if Image(ep,word)<>z then Error("Preimage mismatch"); fi;
        Print("WITNESS_ORDER ",Order(z)," TARGET_ORDER ",Order(Image(phi,z)),"\n");
        Print("WORD ",LetterRepAssocWord(UnderlyingElement(word)),"\n");
        break;
    fi;
od;
Print("PASS N3 bounded uniform-increment probe completed\n");
QUIT;
