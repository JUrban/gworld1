# Reproduce the compact integer-constructed word, independent of the earlier
# huge nq torsion-generator preimage and of the integer-lattice arithmetic.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
Read("research/certificates/N3-profile-lift-class6/fixtures.g");
Read("research/certificates/N3-uniform-increment/fixtures.g");
N3UniformEval:=function(gens,word)
    local z,s;
    z:=One(gens[1]);
    for s in word do z:=z*gens[AbsInt(s)]^SignInt(s); od;
    return z;
end;
N3UniformWord:=function(gens)
    local z,t;
    z:=N3UniformEval(gens,N3IncrementCertificate.prefix_word)^3;
    for t in N3IncrementCertificate.central_correction do
        z:=z*N3UniformEval(gens,t.word)^t.exponent;
    od;
    return z;
end;
f:=FreeGroup(3);; x:=GeneratorsOfGroup(f);;
for spec in [[N3LiftCertificate.source_relations,7],[N3LiftCertificate.target_relations,6]] do
    rel:=List(spec[1],w->N3UniformEval(x,w));;
    p:=f/rel;; ep:=NqEpimorphismNilpotentQuotient(p,spec[2]);;
    g:=Image(ep);; y:=[];;
    for a in GeneratorsOfGroup(p) do Add(y,Image(ep,a)); od;
    z:=N3UniformWord(y);;
    if z=One(g) or z^2<>One(g) or Order(z)<>2 then Error("Order-two image failed"); fi;
    Print("Verified order two: ",Length(rel)," pair relators, full class ",spec[2],".\n");
od;
ep:=NqEpimorphismNilpotentQuotient(f,7);; g:=Image(ep);;
y:=List(x,a->Image(ep,a));; z:=N3UniformWord(y);; rhs:=One(g);;
for i in [1..Length(N3IncrementCertificate.source_normal)] do
    n:=N3IncrementCertificate.square_relator_coefficients[i];;
    if n<>0 then rhs:=rhs*N3UniformEval(y,N3IncrementCertificate.source_normal[i].word)^n; fi;
od;
if z^2<>rhs or z=rhs or z=One(g) then Error("Free class-seven identity failed"); fi;
Print("Verified the positive square identity in the free rank-three class-seven group.\n");
Print("PASS N3 uniform-increment GAP certificate\n");
QUIT;
