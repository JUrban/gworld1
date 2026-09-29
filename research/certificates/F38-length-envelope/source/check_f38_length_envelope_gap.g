# Independent GAP reconstruction of every bounded pair graph.
Read("research/certificates/F38-length-envelope/fixtures.g");;
Read("research/certificates/F38-length-envelope/negative-fixtures.g");;
F38EFail := function(s) Print("FAIL ",s,"\n"); FORCE_QUIT_GAP(1); end;;
F38EEval := function(gens,word)
    local out,x;
    out := One(gens[1]);
    for x in word do out := out*gens[AbsInt(x)]^SignInt(x); od;
    return out;
end;;
F38EClass := function(word)
    local w,n;
    w := LetterRepAssocWord(word);
    while Length(w)>1 and w[1]=-Last(w) do w:=w{[2..Length(w)-1]}; od;
    n:=Length(w);
    if n=0 then return []; fi;
    return Minimum(List([0..n-1],i->Concatenation(w{[i+1..n]},w{[1..i]})));
end;;
F38EImages := function(gens,auto)
    local images,inverse,i;
    images:=List(auto[1],w->F38EEval(gens,w));
    inverse:=List(auto[2],w->F38EEval(gens,w));
    for i in [1..Length(gens)] do
        if F38EEval(images,LetterRepAssocWord(inverse[i]))<>gens[i] or
           F38EEval(inverse,LetterRepAssocWord(images[i]))<>gens[i] then
            F38EFail("inverse pair");
        fi;
    od;
    return images;
end;;
F38EWhiteheads := function(rank)
    local out,perm,signs,a,A,alphabet,images,x,im;
    out:=[];
    for perm in PermutationsList([1..rank]) do
        for signs in Tuples([-1,1],rank) do
            AddSet(out,List([1..rank],i->[signs[i]*perm[i]]));
        od;
    od;
    alphabet:=Concatenation([-rank..-1],[1..rank]);
    for a in alphabet do
        for A in Combinations(Difference(alphabet,[a,-a])) do
            images:=[];
            for x in [1..rank] do
                if x=AbsInt(a) then im:=[x];
                elif x in A and -x in A then im:=[-a,x,a];
                elif x in A then im:=[x,a];
                elif -x in A then im:=[-a,x];
                else im:=[x]; fi;
                Add(images,im);
            od;
            AddSet(out,images);
        od;
    od;
    RemoveSet(out,List([1..rank],i->[i]));
    return out;
end;;
F38ERun := function()
    local row,rank,F,gens,K,m,mu,moves,vertices,edges,envelope,B,
          i,j,x,y,p,actual,reach,next,changed,edge,computed,k,
          image,ab,nchecks,edgechecks,substitutions,negatives;
    nchecks:=0;edgechecks:=0;substitutions:=0;negatives:=0;
    for row in F38EnvelopeFixtures do
        rank:=row[1]; F:=FreeGroup(rank); gens:=GeneratorsOfGroup(F);
        K:=row[4];m:=row[5];mu:=F38EImages(gens,row[6]);
        moves:=List(row[7],a->F38EImages(gens,a));
        if Set(List(row[7],a->a[1]))<>F38EWhiteheads(rank) then
            F38EFail("incomplete Whitehead move set");
        fi;
        vertices:=row[8];edges:=row[9];envelope:=row[10];B:=row[11];
        if [F38EClass(F38EEval(mu,row[2])),F38EClass(F38EEval(mu,row[3]))]<>vertices[1] then
            F38EFail("root minimizer transport");
        fi;
        if Length(Set(vertices))<>Length(vertices) then F38EFail("duplicate pair vertices");fi;
        computed:=List([0..K],i->-1);
        for i in [1..Length(vertices)] do
            x:=vertices[i][1];y:=vertices[i][2];
            if F38EClass(F38EEval(gens,x))<>x or F38EClass(F38EEval(gens,y))<>y then
                F38EFail("noncanonical vertex");
            fi;
            computed[Length(x)+1]:=Maximum(computed[Length(x)+1],Length(y));
            actual:=[];
            for j in [1..Length(moves)] do
                x:=F38EClass(F38EEval(moves[j],vertices[i][1]));
                y:=F38EClass(F38EEval(moves[j],vertices[i][2]));
                substitutions:=substitutions+2;
                if Length(x)<m then F38EFail("not a Whitehead minimum");fi;
                if Length(y)>2*Length(vertices[i][2]) or Length(vertices[i][2])>2*Length(y) then
                    F38EFail("cyclic length factor2 bound");
                fi;
                if Length(x)<=K then
                    p:=Position(vertices,[x,y]);
                    if p=fail then F38EFail("bounded graph not closed");fi;
                    Add(actual,[j-1,p-1]);
                fi;
            od;
            if Set(actual)<>Set(edges[i]) then F38EFail("edge mismatch");fi;
            edgechecks:=edgechecks+Length(actual);
        od;
        reach:=[0];changed:=true;
        while changed do
            next:=ShallowCopy(reach);
            for i in reach do for edge in edges[i+1] do AddSet(next,edge[2]);od;od;
            changed:=next<>reach;reach:=next;
        od;
        if Length(reach)<>Length(vertices) then F38EFail("disconnected pair graph");fi;
        for k in [m+1..K] do computed[k+1]:=Maximum(computed[k+1],computed[k]);od;
        if computed<>envelope or computed[m+1]<>B then F38EFail("incorrect exact envelope");fi;
        for k in [m..K] do
            if computed[k+1]>B*2^(k-m) then F38EFail("envelope bound");fi;
        od;
        nchecks:=nchecks+1;
        Print("ENVELOPE graph=",nchecks," rank=",rank," vertices=",Length(vertices),
              " prefix=",computed," B=",B,"\n");
    od;
    for row in F38StabilizerFixtures do
        rank:=row[1];F:=FreeGroup(rank);gens:=GeneratorsOfGroup(F);
        image:=F38EImages(gens,row[5]);
        if F38EClass(F38EEval(image,row[2]))<>F38EClass(F38EEval(gens,row[2])) or
           F38EClass(F38EEval(image,row[3]))=F38EClass(F38EEval(gens,row[3])) then
            F38EFail("negative witness classes");
        fi;
        for j in [1..rank] do
            ab:=ExponentSums(image[j]);
            for i in [1..rank] do
                if (i=j and ab[i] mod 3<>1) or (i<>j and ab[i] mod 3<>0) then
                    F38EFail("negative witness level3");
                fi;
            od;
        od;
        negatives:=negatives+1;
    od;
    Print("graphs=",nchecks," directed_edges=",edgechecks," free_word_substitutions=",
          substitutions," negative_witnesses=",negatives,"\n");
    Print("PASS F38 LENGTH ENVELOPE GAP\n");
end;;
F38ERun();;
QUIT_GAP(0);
