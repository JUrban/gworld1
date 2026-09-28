# Independent GAP/nq check of the explicit Magnus certificate words.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
Read("research/certificates/N3-pseudofree-class5/fixtures.g");
N3Eval := function(gens,word)
    local v,s;
    v := One(gens[1]);
    for s in word do
        if s>0 then v:=v*gens[s]; else v:=v*gens[-s]^-1; fi;
    od;
    return v;
end;
f := FreeGroup(3);; x := GeneratorsOfGroup(f);;
rel := List(N3Certificate.relations,w->N3Eval(x,w));;
p := f/rel;; ep := NqEpimorphismNilpotentQuotient(p,5);;
g := Image(ep);; y := List(GeneratorsOfGroup(p),s->Image(ep,s));;
if not ForAll(N3Certificate.relations,w->N3Eval(y,w)=One(g)) then
    Error("Presentation relator failed");
fi;
if NilpotencyClassOfGroup(g)<>5 then Error("Unexpected nilpotency class"); fi;
for w in N3Certificate.witnesses do
    z := N3Eval(y,w.word);;
    if z=One(g) or z^2<>One(g) or Order(z)<>2 then
        Error("Order-two witness failed in the presented quotient");
    fi;
    if not ForAll(y,t->Comm(z,t)=One(g)) then Error("Witness not central"); fi;
    Print("Quotient witness order=2, central=true, coordinates=",
          ExponentsByPcp(Pcp(g),z),"\n");
od;
if Size(TorsionSubgroup(g))<>8 then Error("Unexpected torsion subgroup size"); fi;

# Check each positive square identity also in the free class-five group.
ef := NqEpimorphismNilpotentQuotient(f,5);; gf := Image(ef);;
xf := List(x,s->Image(ef,s));;
normal := List(N3Certificate.normal_generators,r->N3Eval(xf,r.word));;
for w in N3Certificate.witnesses do
    z := N3Eval(xf,w.word);; rhs := One(gf);;
    for i in [1..Length(normal)] do
        rhs := rhs*normal[i]^w.square_relator_coefficients[i];
    od;
    if z^2<>rhs or z=One(gf) then Error("Free-group square identity failed"); fi;
    # Negative control: z itself must not equal this square identity.
    if z=rhs then Error("Exponent-one control failed"); fi;
od;
Print("Verified all six defining relations, the positive square identity in\n",
      "the free class-five group, and a nontrivial central order-two image.\n");
Print("PASS N3 class-five torsion GAP certificate\n");
QUIT;
