# Independent GAP free-group calculation: all type-II moves, all vertices,
# every basis ordering, every start. Fixtures are zero-indexed.
Read("research/certificates/F25-degree-obstruction/fixtures.g");;
F25F := FreeGroup("a","b","c");;
F25Gens := GeneratorsOfGroup(F25F);;
F25Word := letters -> Product(letters, x -> F25Gens[AbsInt(x)]^SignInt(x));;
F25Canonical := function(word)
    local letters, n;
    letters := LetterRepAssocWord(word);
    while Length(letters)>1 and letters[1]=-letters[Length(letters)] do
        letters := letters{[2..Length(letters)-1]};
    od;
    n := Length(letters);
    if n=0 then return []; fi;
    return Minimum(List([0..n-1], i -> Concatenation(letters{[i+1..n]}, letters{[1..i]})));
end;;
F25Degree := function(move, order)
    local ones;
    ones := Filtered(move[2], x -> not -x in move[2]);
    if Length(ones)=0 then return 0; fi;
    return Maximum(List(ones, x -> Position(order, AbsInt(x))));
end;;
F25Run := function()
    local alphabet, spec, a, available, A, m, images, x, im, actualMoves,
          actualEdges, words, i, j, map, v, p, order, starts, reach, stage,
          changed, next, edge, expected, qi, total, lengths;
    alphabet := [-3,-2,-1,1,2,3];
    actualMoves := [];
    for a in alphabet do
        available := Difference(alphabet,[a,-a]);
        for A in Combinations(available) do
            images := [];
            for x in [1..3] do
                if x=AbsInt(a) then im := [x];
                elif x in A and -x in A then im := [-a,x,a];
                elif x in A then im := [x,a];
                elif -x in A then im := [-a,x];
                else im := [x]; fi;
                Add(images,im);
            od;
            Add(actualMoves,[a,A,images]);
        od;
    od;
    if Set(actualMoves)<>Set(F25Moves) then Error("Missing/incorrect moves"); fi;
    words := List(F25Vertices, F25Word);
    if Length(Set(F25Vertices))<>12 then Error("Vertex list"); fi;
    actualEdges := [];
    lengths := [];
    for i in [1..12] do
        if F25Canonical(words[i])<>F25Vertices[i] then Error("Canonical form"); fi;
        Add(actualEdges,[]);
        for j in [1..Length(F25Moves)] do
            m := F25Moves[j];
            map := GroupHomomorphismByImagesNC(F25F,F25F,F25Gens,List(m[3],F25Word));
            v := F25Canonical(Image(map,words[i]));
            if Length(v)<12 then Error("Not a Whitehead minimum"); fi;
            Add(lengths,Length(v));
            if Length(v)=12 then
                p := Position(F25Vertices,v);
                if p=fail then Error("Incomplete plateau"); fi;
                if p<>i then Add(actualEdges[i],[j-1,p-1]); fi;
            fi;
        od;
        if Set(actualEdges[i])<>Set(F25Edges[i]) then Error("Incorrect edges"); fi;
    od;
    # Check connectedness so listed vertices are all actually in this orbit.
    reach := [0];
    changed := true;
    while changed do
        next := ShallowCopy(reach);
        for i in reach do
            for edge in actualEdges[i+1] do AddSet(next,edge[2]); od;
        od;
        changed := next<>reach; reach := next;
    od;
    if Length(reach)<>12 then Error("Not connected"); fi;
    total := 0;
    for qi in [1..Length(F25Orders)] do
        order := F25Orders[qi];
        for starts in [0..11] do
            reach := [starts];
            for stage in [0..3] do
                changed := true;
                while changed do
                    next := ShallowCopy(reach);
                    for i in reach do
                        for edge in actualEdges[i+1] do
                            if F25Degree(F25Moves[edge[1]+1],order)=stage then
                                AddSet(next,edge[2]);
                            fi;
                        od;
                    od;
                    changed := next<>reach; reach := next;
                od;
            od;
            expected := F25ReachSets[qi][starts+1];
            if reach<>expected or Length(reach)=12 then Error("Sorting obstruction failed"); fi;
            total := total+1;
        od;
    od;
    Print("vertices=12 moves=",Length(F25Moves)," edges=",Sum(List(actualEdges,Length)),
          " substitutions=",Length(lengths)," sorted_reach_checks=",total,
          " image_lengths=",Set(lengths),"\n");
    Print("PASS F25 INDEPENDENT GAP DEGREE OBSTRUCTION\n");
end;;
F25Run();;
QUIT_GAP(0);
