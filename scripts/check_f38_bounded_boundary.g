Read("research/certificates/F38-bounded-boundary/fixtures.g");;
F38BEval:=function(gens,word)
    local result,s;
    result:=One(gens[1]);
    for s in word do result:=result*gens[AbsInt(s)]^SignInt(s);od;
    return result;
end;;
F38BCyclicLength:=function(word)
    local letters;
    letters:=LetterRepAssocWord(word);
    while Length(letters)>1 and letters[1]=-Last(letters) do
        letters:=letters{[2..Length(letters)-1]};
    od;
    return Length(letters);
end;;
F38BRun:=function()
    local row,group,gens,images,lengths;
    for row in F38BoundaryRows do
        group:=FreeGroup(Length(row[1]));gens:=GeneratorsOfGroup(group);
        images:=List(row[1],w->F38BEval(gens,w));
        lengths:=[F38BCyclicLength(F38BEval(images,F38BoundaryU)),
                  F38BCyclicLength(F38BEval(images,F38BoundaryV))];
        if lengths<>row[2] then Error("F38 bounded-scope word mismatch");fi;
    od;
    Print("PASS F38 bounded GAP: ",Length(F38BoundaryRows)," word records\n");
end;;
F38BRun();;
QUIT_GAP(0);
