LoadPackage("fga");;
Read("research/certificates/F41-graph-transfer/fixtures.g");;

(function()
    local Word, CyclicWord, row, F, A, G, images, step, move, u, v,
          graphBasis, raw, cyc, labels, ambientBasis, H, phi, final,
          adj, id, e, source, target, graphType, ends, word, count;
    Word := function(group, ints)
        local result, x;
        result := One(group);
        for x in ints do
            result := result * GeneratorsOfGroup(group)[AbsInt(x)]^SignInt(x);
        od;
        return result;
    end;
    CyclicWord := function(group, w)
        local letters;
        letters := LetterRepAssocWord(w);
        while Length(letters)>1 and letters[1]=-letters[Length(letters)] do
            letters := letters{[2..Length(letters)-1]};
        od;
        return Word(group, letters);
    end;
    count := 0;
    for row in F41Fixtures do
        F := FreeGroup(2);
        A := FreeGroup(Length(row[9]));
        G := FreeGroup(row[1]);
        images := GeneratorsOfGroup(F);
        for move in row[3] do
            step := ShallowCopy(GeneratorsOfGroup(F));
            step[move[1]] := step[move[1]] * step[move[2]]^move[3];
            phi := GroupHomomorphismByImages(F,F,GeneratorsOfGroup(F),step);
            images := List(images,w->Image(phi,w));
        od;
        Assert(0, images=List(row[4],w->Word(F,w)));
        phi := GroupHomomorphismByImages(F,F,GeneratorsOfGroup(F),images);
        Assert(0,Index(F,Image(phi))=1);
        u := Word(F,row[2]);
        v := CyclicWord(F,Image(phi,u));
        Assert(0,v=Word(F,row[5]));
        graphBasis := List(row[6],w->Word(A,w));
        phi := GroupHomomorphismByImages(F,A,GeneratorsOfGroup(F),graphBasis);
        raw := Image(phi,v);
        Assert(0,raw=Word(A,row[7]));
        cyc := CyclicWord(A,raw);
        Assert(0,cyc=Word(A,row[8]));
        labels := List(row[9],w->Word(G,w));
        phi := GroupHomomorphismByImages(A,G,GeneratorsOfGroup(A),labels);
        ambientBasis := List(graphBasis,w->Image(phi,w));
        H := Subgroup(G,ambientBasis);
        Assert(0,RankOfFreeGroup(H)=2);
        final := Image(phi,cyc);
        Assert(0,final=Word(G,row[10]));
        Assert(0,final=CyclicWord(G,final));
        Assert(0,Length(final)=Sum(row[8],e->Length(labels[AbsInt(e)])));
        # The graph immersion and cyclic path are checked independently.
        if Length(row[9])=2 then
            ends := [[1,1],[1,1]];
        elif row[6][1]=[2,-1] then
            ends := [[1,2],[1,2],[1,2]];
        else
            ends := [[1,1],[1,2],[2,2]];
        fi;
        adj := [[],[]];
        for id in [1..Length(ends)] do
            source := ends[id][1]; target := ends[id][2];
            word := row[9][id];
            Add(adj[source],word[1]);
            Add(adj[target],-word[Length(word)]);
        od;
        Assert(0,ForAll(adj,a->Length(a)=Length(Set(a))));
        for id in [1..Length(ends)] do
            Assert(0,Number(row[8],e->AbsInt(e)=id)>=2);
        od;
        count := count+1;
    od;
    Print("PASS F41 GAP graph fixtures: ",count,"\n");
end)();
QUIT;
