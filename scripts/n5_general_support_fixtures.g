Read("scripts/n5_general_malcev_fixtures.g");
N5SupportFixtures:=function()
    local fs,f,name,g,factors,records,h,c3,d8,ambient,a,b,glued;
    fs:=N5MalcevFixtures();records:=[];
    for f in fs do
        name:=f[1];g:=f[2];factors:=[g];
        if name="mixed_classes" then factors:=List([1,2,3],i->Image(Embedding(g,i)));fi;
        if name="noncentral_finite_torsion" then factors:=List([1,2],i->Image(Embedding(g,i)));fi;
        Add(records,rec(name:=name,group:=g,ambient:=g,factors:=factors,expected_dimensions:=f[3],glued:=false));
    od;
    h:=NilpotentQuotient(FreeGroup(2),2);c3:=NilpotentQuotient(FreeGroup(2),3);
    d8:=Image(IsomorphismPcpGroup(SmallGroup(8,3)));
    ambient:=DirectProduct(c3,h,d8);
    Add(records,rec(name:="mixed_classes_and_torsion",group:=ambient,ambient:=ambient,
        factors:=List([1,2,3],i->Image(Embedding(ambient,i))),expected_dimensions:=[3,5],glued:=false));
    ambient:=DirectProduct(c3,c3);
    Add(records,rec(name:="repeated_class3",group:=ambient,ambient:=ambient,
        factors:=List([1,2],i->Image(Embedding(ambient,i))),expected_dimensions:=[5,5],glued:=false));
    ambient:=DirectProduct(c3,h);a:=GeneratorsOfGroup(c3);b:=GeneratorsOfGroup(h);
    a:=List(a,x->Image(Embedding(ambient,1),x));b:=List(b,x->Image(Embedding(ambient,2),x));
    glued:=Subgroup(ambient,Concatenation([a[1]*b[1],a[1]^2],a{[2..Length(a)]},b{[2..Length(b)]}));
    if Index(ambient,glued)<>2 then Error("glued fixture index");fi;
    Add(records,rec(name:="index_two_gluing",group:=glued,ambient:=ambient,
        factors:=List([1,2],i->Image(Embedding(ambient,i))),expected_dimensions:=[3,5],glued:=true));
    return records;
end;
