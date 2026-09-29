# Bounded test of a possible repair, not a test of the whole N3 assertion.
# H(b,c): every coordinate pair has class <= b, all three have class <= c.
# Check the image of Tor(H(b,c)) in H(2,c), b >= 2.  A vanishing image
# would permit this particular canonical map to factor through a TF quotient.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;

N3ProfileModel := function(bound,cl)
    local f,x,rel,i,j,tail,w,k,p,ep,g,y;
    f:=FreeGroup(3); x:=GeneratorsOfGroup(f); rel:=[];
    for i in [1..2] do
        for j in [i+1..3] do
            for tail in Tuples([i,j],bound-1) do
                w:=Comm(x[j],x[i]);
                for k in tail do w:=Comm(w,x[k]); od;
                Add(rel,w);
            od;
        od;
    od;
    p:=f/rel; ep:=NqEpimorphismNilpotentQuotient(p,cl);
    g:=Image(ep); y:=List(GeneratorsOfGroup(p),a->Image(ep,a));
    return rec(group:=g,gens:=y,relation_count:=Length(rel));
end;

targets:=[];;
for spec in [[2,5],[3,5],[3,6],[3,7],[3,8],[4,7],[4,8]] do
    b:=spec[1];; c:=spec[2];;
    Print("START pair_bound=",b," full_bound=",c,"\n");
    if not IsBound(targets[c]) then targets[c]:=N3ProfileModel(2,c); fi;
    target:=targets[c];;
    if b=2 then source:=target; else source:=N3ProfileModel(b,c); fi;
    hom:=GroupHomomorphismByImagesNC(source.group,target.group,
                                   source.gens,target.gens);;
    tor:=TorsionSubgroup(source.group);;
    torimages:=List(GeneratorsOfGroup(tor),a->Image(hom,a));;
    image:=Subgroup(target.group,torimages);;
    if b=2 and Size(image)<>8 then Error("Known nonzero-map control failed"); fi;
    Print("RESULT pair_bound=",b," full_bound=",c,
          " relation_count=",source.relation_count,
          " source_class=",NilpotencyClassOfGroup(source.group),
          " source_hirsch=",HirschLength(source.group),
          " torsion_order=",Size(tor),
          " torsion_image_order=",Size(image),"\n");
od;
Print("PASS N3 bounded profile-lift probe completed\n");
QUIT;
