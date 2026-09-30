Read("scripts/n5_general_support.g");
Read("scripts/n5_class2_json.g");
Read("scripts/n5_general_support_fixtures.g");
Read("scripts/n5_rational_lie_gap_checker.g");
Read("research/certificates/N5-general-support/decompositions-v1.g");
N5CheckGeneralSupport:=function()
    local records,fixtures,idx,f,m,c,r,counts,h,projections,subset,p,out,kmap,k,s,
          supports,expected,zambient,subgroup,side,complement,j,indices,record,subsets,distinct;
    records:=[];fixtures:=N5SupportFixtures();counts:=0;
    for idx in [1..Length(fixtures)] do
        f:=fixtures[idx];m:=N5GeneralMalcevInput(f.group);r:=N5SupportLieFixtures[idx];
        if f.name<>r.name then Error("fixture order");fi;
        c:=r.structure_constants;h:=m.data.hirsch_length;
        if N5RationalData(c)<>m.data.structure_constants then Error("rebuilt Malcev basis changed");fi;
        N5LieReplay(r);projections:=r.result.projections;
        kmap:=NaturalHomomorphismByNormalSubgroup(f.group,Centre(f.group));k:=Image(kmap);s:=TorsionSubgroup(k);
        supports:=[];record:=rec(name:=f.name,torsion_kernel_order:=Size(s),partitions:=[]);
        subsets:=Combinations([1..Length(projections)]);
        for subset in subsets do
            if h=0 then p:=[];else p:=NullMat(h,h,Rationals);fi;
            for j in subset do p:=p+projections[j];od;
            out:=N5RationalSupport(m,c,p);
            # Bring every subgroup to the same quotient object, rather than
            # comparing subgroups of independently constructed isomorphic K's.
            side:=Image(kmap,out.kernel);Add(supports,side);
            out.data.partition:=subset;Add(record.partitions,out.data);counts:=counts+1;
        od;
        if supports[Position(subsets,[])]<>s or
           supports[Position(subsets,[1..Length(projections)])]<>k then Error("zero/full support boundary");fi;
        for j in [1..Length(supports)] do
            complement:=supports[Position(subsets,Difference([1..Length(projections)],subsets[j]))];
            if Intersection(supports[j],complement)<>s then Error("complement intersection");fi;
        od;
        expected:=[];zambient:=Centre(f.ambient);
        for subset in Combinations([1..Length(f.factors)]) do
            subgroup:=zambient;
            for j in subset do subgroup:=ClosureGroup(subgroup,f.factors[j]);od;
            subgroup:=Intersection(f.group,subgroup);
            side:=ClosureGroup(Image(kmap,subgroup),s);
            if not side in expected then Add(expected,side);fi;
        od;
        distinct:=[];
        for side in supports do if not side in distinct then Add(distinct,side);fi;od;
        if Length(distinct)<>Length(expected) or not ForAll(distinct,x->x in expected) then
            Error("native known-factor support mismatch");fi;
        indices:=[];
        for j in [1..Length(supports)] do
            complement:=supports[Position(subsets,Difference([1..Length(projections)],subsets[j]))];
            Add(indices,Index(k,ClosureGroup(supports[j],complement)));
        od;
        if f.glued then
            if Set(indices)<>[1,2] then Error("gluing obstruction not retained");fi;
        elif Set(indices)<>[1] then Error("known product support generation");fi;
        record.complementary_generation_indices:=indices;record.distinct_supports:=Length(distinct);
        Add(records,record);
        Print(f.name,": ",Length(supports)," partitions, ",record.distinct_supports,
            " supports, generation indices ",Set(indices),"\n");
    od;
    N5WriteCoordinateJson("research/certificates/N5-general-support/checks-v1.json",records);
    Print("PASS N5 general rational supports: ",Length(records)," groups; ",counts," partitions\n");
end;
N5CheckGeneralSupport();
QUIT;
