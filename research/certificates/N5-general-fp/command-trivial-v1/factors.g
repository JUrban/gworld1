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
Read("/project/gworld1/research/certificates/N5-general-fp/command-trivial-v1/lie.g");
if N5CoordinateJson(N5Model.data)<>N5ExactMalcevJson then Error("marked Malcev input changed");fi;
Read("/project/gworld1/research/certificates/N5-general-fp/command-trivial-v1/decision.g");

Read("scripts/n5_general_fp_factors.g");
N5Words := [];;
if N5Decision.answer then
    N5Factors := N5GeneralFpFactors(N5Model,N5Central,N5Decision);;
    N5Words := List(N5Factors.words,ws->List(ws,w->ExtRepOfObj(UnderlyingElement(w))));;
fi;
N5WriteCoordinateJson("/project/gworld1/research/certificates/N5-general-fp/command-trivial-v1/answer.json",rec(answer:=N5Decision.answer,factor_words:=N5Words));
Print("PASS N5 general-fp factors\n");
QUIT;
