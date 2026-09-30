Read("scripts/n5_class2_input.g");
Read("scripts/n5_class2_json.g");
N5Free := FreeGroup(2);
N5Gens := GeneratorsOfGroup(N5Free);
N5ExtWord := function(v)
    local w,i;
    w:=One(N5Free);
    for i in [1,3..Length(v)-1] do w:=w*N5Gens[v[i]]^v[i+1];od;
    return w;
end;
N5Presentation := N5Free/List([[2,-1,1,-1,2,1,1,1,1,-1,1,-1,2,-1,1,1,2,1,1,1],[2,-1,1,-1,2,1,1,1,2,-1,1,-1,2,-1,1,1,2,1,2,1],[1,-1,2,-1,1,1,2,1,1,-1,2,-1,1,1,2,1]],N5ExtWord);
N5Model := N5FpClassTwo(N5Presentation,true);
N5WriteCoordinateJson("/project/gworld1/research/certificates/N5-class2-input/standalone-g2-v1/coordinates.json",N5Model.data);
Print("PASS N5 fp export\n");
QUIT;
