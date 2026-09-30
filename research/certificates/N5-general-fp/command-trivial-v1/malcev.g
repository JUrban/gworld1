Read("scripts/n5_general_fp_input.g");
Read("scripts/n5_general_pipeline.g");
Read("scripts/n5_class2_json.g");
N5Free := FreeGroup(0);;
N5Gens := GeneratorsOfGroup(N5Free);;
N5ExtWord := function(v)
    local w,i;
    w:=One(N5Free);
    for i in [1,3..Length(v)-1] do w:=w*N5Gens[v[i]]^v[i+1];od;
    return w;
end;
N5Presentation := N5Free/List([],N5ExtWord);;
N5Model := N5FpNilpotent(N5Presentation,true);;
N5WriteCoordinateJson("/project/gworld1/research/certificates/N5-general-fp/command-trivial-v1/malcev.json",N5Model.data);
Print("PASS N5 general-fp malcev\n");
QUIT;
