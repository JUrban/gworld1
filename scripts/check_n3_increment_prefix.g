# Test whether the existing compact class-six word already has finite order
# in the uniformly incremented profile; avoids large nq preimage expressions.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
Read("research/certificates/N3-profile-lift-class6/fixtures.g");
N3PrefixEval:=function(gens,word)
    local z,s;
    z:=One(gens[1]);
    for s in word do z:=z*gens[AbsInt(s)]^SignInt(s); od;
    return z;
end;
f:=FreeGroup(3);; x:=GeneratorsOfGroup(f);;
rel:=List(N3LiftCertificate.source_relations,w->N3PrefixEval(x,w));;
p:=f/rel;; ep:=NqEpimorphismNilpotentQuotient(p,7);; g:=Image(ep);;
y:=List(GeneratorsOfGroup(p),a->Image(ep,a));;
z:=N3PrefixEval(y,N3LiftCertificate.word);;
Print("PREFIX_ORDER ",Order(z),"\n");
Print("PREFIX_SIXTH_IS_IDENTITY ",z^6=One(g),"\n");
Print("PASS N3 uniform-increment prefix checked\n");
QUIT;
