# Populate the actual word cache via independently rebuilt Hall commutator trees.
# This changes evaluation order, not any group equality or lattice test.
N8C9SeedHallCache:=function(group,r,c,cache)
    local F,fgens,gens,hall,weight,new,i,j,a,b,words;
    F:=FreeGroup(r);fgens:=GeneratorsOfGroup(F);gens:=GeneratorsOfGroup(group);
    hall:=List([1..r],i->rec(weight:=1,pair:=fail,word:=fgens[i],value:=gens[i]));
    if List(hall,h->LetterRepAssocWord(h.word))<>N8C9Halls[1] then
        N8C9Fail("Hall generator words");fi;
    for a in hall do AddDictionary(cache,LetterRepAssocWord(a.word),a.value);od;
    for weight in [2..c] do
        new:=[];
        for i in [1..Length(hall)] do
            a:=hall[i];
            for j in [1..i-1] do
                b:=hall[j];
                if a.weight+b.weight<>weight then continue;fi;
                if a.pair<>fail and a.pair[2]>j then continue;fi;
                Add(new,rec(weight:=weight,pair:=[i,j],word:=Comm(a.word,b.word),
                            value:=Comm(a.value,b.value)));
            od;
        od;
        words:=List(new,h->LetterRepAssocWord(h.word));
        if words<>N8C9Halls[weight] then N8C9Fail("Hall commutator tree words");fi;
        for i in [1..Length(new)] do AddDictionary(cache,words[i],new[i].value);od;
        Append(hall,new);
    od;
    Print("HALL CACHE VERIFIED ",r," ",c,"\n");
end;;
