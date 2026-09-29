# Replace a huge expanded nq preimage by a fixed short prefix and central
# degree-seven Hall factors.  Exact equality in the presented group is checked.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
Read("research/certificates/N3-profile-lift-class6/fixtures.g");
N3ShortEval:=function(gens,word)
    local z,s;
    z:=One(gens[1]);
    for s in word do z:=z*gens[AbsInt(s)]^SignInt(s); od;
    return z;
end;
f:=FreeGroup(3);; x:=GeneratorsOfGroup(f);;
rel:=List(N3LiftCertificate.source_relations,w->N3ShortEval(x,w));;
p:=f/rel;; ep:=NqEpimorphismNilpotentQuotient(p,7);; g:=Image(ep);;
y:=List(GeneratorsOfGroup(p),a->Image(ep,a));;
rel:=List(N3LiftCertificate.target_relations,w->N3ShortEval(x,w));;
q:=f/rel;; eq:=NqEpimorphismNilpotentQuotient(q,6);; h:=Image(eq);;
v:=List(GeneratorsOfGroup(q),a->Image(eq,a));;
phi:=GroupHomomorphismByImagesNC(g,h,y,v);;
tor:=TorsionSubgroup(g);; z:=First(GeneratorsOfGroup(tor),a->Image(phi,a)<>One(h));;
if z=fail then Error("Expected surviving torsion"); fi;
prefix:=N3ShortEval(y,N3LiftCertificate.word);;
delta:=prefix^-1*z;;
hall:=[];;
for i in [1..3] do Add(hall,rec(weight:=1,right:=0,word:=x[i],image:=y[i])); od;
for wt in [2..7] do
    new:=[];;
    for i in [1..Length(hall)] do
        for j in [1..i-1] do
            if hall[i].weight+hall[j].weight=wt and hall[i].right<=j then
                Add(new,rec(weight:=wt,right:=j,word:=Comm(hall[i].word,hall[j].word),
                            image:=Comm(hall[i].image,hall[j].image)));
            fi;
        od;
    od;
    Append(hall,new);
od;
top:=Filtered(hall,a->a.weight=7);;
if Length(top)<>312 then Error("Hall rank mismatch"); fi;
images:=List(top,a->a.image);; central:=Subgroup(g,images);;
if not delta in central then Error("Difference not in degree seven"); fi;
ff:=FreeGroup(312);; zz:=GeneratorsOfGroup(ff);;
rho:=GroupHomomorphismByImagesNC(ff,central,zz,images);;
SetIsSurjective(rho,true);;
pre:=PreImagesRepresentative(rho,delta);;
coeffs:=List([1..312],i->0);; ext:=ExtRepOfObj(pre);;
for i in [1,3..Length(ext)-1] do coeffs[ext[i]]:=coeffs[ext[i]]+ext[i+1]; od;
check:=One(g);;
for i in [1..312] do check:=check*images[i]^coeffs[i]; od;
if check<>delta or prefix*check<>z then Error("Central lift mismatch"); fi;
Print("ORDER ",Order(z)," TARGET_ORDER ",Order(Image(phi,z)),"\n");
Print("COEFFICIENTS ",coeffs,"\n");
Print("PASS N3 uniform-increment short certificate extracted\n");
QUIT;
