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
N5Presentation := N5Free/List([[1,6],[2,-1,1,2]],N5ExtWord);
N5Model := N5FpClassTwo(N5Presentation,true);
Read("/project/gworld1/research/certificates/N5-class2-input/standalone-c6-v1/decision.g");

if not ForAll(RecNames(N5Model.data),k->N5Model.data.(k)=N5Decision.(k)) then
    Error("reconstructed input differs from decision input");fi;
N5Words := [];
if N5Decision.answer then
    N5Factors := N5InputFactors(N5Model,N5Decision);
    N5Words := List(N5Factors.words,ws->List(ws,w->ExtRepOfObj(UnderlyingElement(w))));
fi;
N5WriteCoordinateJson("/project/gworld1/research/certificates/N5-class2-input/standalone-c6-v1/answer.json",rec(answer:=N5Decision.answer,factor_words:=N5Words));
Print("PASS N5 fp replay\n");
QUIT;
