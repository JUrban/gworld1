Read("scripts/n5_general_pipeline.g");
Read("scripts/n5_class2_json.g");
Read("scripts/n5_general_support_fixtures.g");
Read("research/certificates/N5-general-support/decompositions-v1.g");
N5ExportGeneralPipeline:=function()
    local records,fixtures,i,f,m,r,data;
    records:=[];fixtures:=N5SupportFixtures();
    for i in [1..Length(fixtures)] do
        f:=fixtures[i];m:=N5GeneralMalcevInput(f.group);r:=N5SupportLieFixtures[i];
        if r.name<>f.name or N5RationalData(r.structure_constants)<>m.data.structure_constants then
            Error("general pipeline input binding");fi;
        data:=N5GeneralCentralData(m,r.structure_constants,r.result.projections);
        data.name:=f.name;
        data.expected:=f.name in ["abelian3","mixed_classes","noncentral_finite_torsion",
                                 "mixed_classes_and_torsion","repeated_class3"];
        Add(records,data);
        Print(f.name,": ",Length(data.branches)," central-lifting branches; ",
            data.statistics.subgroup_pairs," subgroup pairs\n");
    od;
    N5WriteCoordinateJson("research/certificates/N5-general-pipeline/input-v1.json",records);
    Print("PASS N5 general pipeline export: ",Length(records)," groups\n");
end;
N5ExportGeneralPipeline();
QUIT;
