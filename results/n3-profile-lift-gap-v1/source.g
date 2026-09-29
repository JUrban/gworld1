# GAP/nq reproduction of the final fixed-word certificate.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
Read("research/certificates/N3-profile-lift-class6/fixtures.g");
N3LiftEval:=function(gens,word)
    local z,s;
    z:=One(gens[1]);
    for s in word do z:=z*gens[AbsInt(s)]^SignInt(s); od;
    return z;
end;
f:=FreeGroup(3);; x:=GeneratorsOfGroup(f);;
for relwords in [N3LiftCertificate.source_relations,N3LiftCertificate.target_relations] do
    rel:=List(relwords,w->N3LiftEval(x,w));;
    p:=f/rel;; ep:=NqEpimorphismNilpotentQuotient(p,6);;
    g:=Image(ep);; y:=List(GeneratorsOfGroup(p),a->Image(ep,a));;
    z:=N3LiftEval(y,N3LiftCertificate.word);;
    if z=One(g) or z^2<>One(g) or Order(z)<>2 then Error("Order-two image failed"); fi;
    for a in y do if Comm(z,a)<>One(g) then Error("Centrality failed"); fi; od;
    Print("Verified nontrivial central order-two word with ",Length(rel)," pair relators.\n");
od;
ep:=NqEpimorphismNilpotentQuotient(f,6);; g:=Image(ep);;
y:=List(x,a->Image(ep,a));; z:=N3LiftEval(y,N3LiftCertificate.word);;
rhs:=One(g);;
for i in [1..Length(N3LiftCertificate.source_normal)] do
    n:=N3LiftCertificate.square_relator_coefficients[i];;
    if n<>0 then rhs:=rhs*N3LiftEval(y,N3LiftCertificate.source_normal[i].word)^n; fi;
od;
if z^2<>rhs or z=rhs or z=One(g) then Error("Free-group square identity failed"); fi;
Print("Verified positive square identity in the free rank-three class-six group.\n");
Print("PASS N3 class-six profile-lift GAP certificate\n");
QUIT;
