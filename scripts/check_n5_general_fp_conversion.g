Read("scripts/n5_general_fp_input.g");
Read("scripts/n5_class2_json.g");
Read("scripts/n5_general_support_fixtures.g");

N5CheckFpConversion:=function()
    local fixtures,f,g,iso,p,m,comparison,gens,records,base,free,fg,relators,
          oldfree,toNative,oldimages,ep,checks,rel;
    fixtures:=N5SupportFixtures();
    Add(fixtures,rec(name:="infinite_cyclic",group:=AbelianPcpGroup([0])));
    Add(fixtures,rec(name:="cyclic_six",group:=AbelianPcpGroup([6])));
    records:=[];
    for f in fixtures do
        g:=f.group;iso:=IsomorphismFpGroup(g);p:=Image(iso);m:=N5FpNilpotent(p,true);
        gens:=GeneratorsOfGroup(g);
        comparison:=GroupHomomorphismByImages(g,m.group,gens,List(gens,x->Image(m.epimorphism,Image(iso,x))));
        if comparison=fail or not IsTrivial(Kernel(comparison)) or Image(comparison)<>m.group then
            Error("fp conversion is not the known native group");fi;
        if NilpotencyClassOfGroup(g)<>NilpotencyClassOfGroup(m.group) then Error("converted class");fi;
        if N5FpNilpotent(p,false)<>fail then Error("missing-promise guard");fi;
        Add(records,rec(name:=f.name,nilclass:=NilpotencyClassOfGroup(g),hirsch_length:=HirschLength(g),
            torsion_order:=Size(TorsionSubgroup(g)),cyclic_shortcut:=m.used_cyclic_abelianization,
            native_signature:=m.data.native_signature,original_generator_images:=m.data.original_generator_images));
        Print(f.name,": class ",NilpotencyClassOfGroup(g),", faithful fp conversion\n");
    od;
    # Explicit Tietze extension t=x1*x2 of the class-three presentation.
    g:=NilpotentQuotient(FreeGroup(2),3);iso:=IsomorphismFpGroup(g);base:=Image(iso);
    oldfree:=GeneratorsOfGroup(FreeGroupOfFpGroup(base));free:=FreeGroup(Length(oldfree)+1);fg:=GeneratorsOfGroup(free);
    relators:=List(RelatorsOfFpGroup(base),r->MappedWord(r,oldfree,fg{[1..Length(oldfree)]}));
    Add(relators,Last(fg)^-1*fg[1]*fg[2]);p:=free/relators;
    oldimages:=List(GeneratorsOfGroup(base),x->PreImagesRepresentative(iso,x));
    toNative:=GroupHomomorphismByImages(p,g,GeneratorsOfGroup(p),Concatenation(oldimages,[oldimages[1]*oldimages[2]]));
    m:=N5FpNilpotent(p,true);
    comparison:=GroupHomomorphismByImages(g,m.group,oldimages,
        List(GeneratorsOfGroup(p){[1..Length(oldimages)]},x->Image(m.epimorphism,x)));
    if comparison=fail or not IsTrivial(Kernel(comparison)) or Image(comparison)<>m.group then
        Error("Tietze-extended conversion");fi;
    if not ForAll(GeneratorsOfGroup(p),x->Image(comparison,Image(toNative,x))=Image(m.epimorphism,x)) then
        Error("Tietze generator binding");fi;
    Add(records,rec(name:="class3_redundant_generator",nilclass:=3,hirsch_length:=5,
        torsion_order:=1,cyclic_shortcut:=m.used_cyclic_abelianization,
        native_signature:=m.data.native_signature,original_generator_images:=m.data.original_generator_images));
    N5WriteCoordinateJson("research/certificates/N5-general-fp/conversion-v1.json",records);
    Print("PASS N5 general fp conversion: ",Length(records)," presentations\n");
end;
N5CheckFpConversion();
QUIT;
