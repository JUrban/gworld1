Read("research/certificates/F38-stabilizer-obstruction/fixtures-v1.g");;
F38SFail:=function(s) Print("FAIL ",s,"\n");FORCE_QUIT_GAP(1);end;;
F38SEval:=function(gens,word)
    local result,s;
    result:=One(gens[1]);
    for s in word do result:=result*gens[AbsInt(s)]^SignInt(s);od;
    return result;
end;;
F38SClass:=function(word)
    local w,n,i,rotations;
    w:=LetterRepAssocWord(word);
    while Length(w)>1 and w[1]=-Last(w) do
        w:=w{[2..Length(w)-1]};
    od;
    n:=Length(w);if n=0 then return [];fi;
    rotations:=[];
    for i in [0..n-1] do
        Add(rotations,Concatenation(w{[i+1..n]},w{[1..i]}));
    od;
    return Minimum(rotations);
end;;
F38SAuto:=function(gens,record)
    local images,inverse,i;
    images:=List(record[1],w->F38SEval(gens,w));
    inverse:=List(record[2],w->F38SEval(gens,w));
    for i in [1..Length(gens)] do
        if F38SEval(images,LetterRepAssocWord(inverse[i]))<>gens[i] or
           F38SEval(inverse,LetterRepAssocWord(images[i]))<>gens[i] then
            F38SFail("two-sided inverse");
        fi;
    od;
    return images;
end;;
F38SMain:=function()
    local row,rank,F,gens,fixed,moved,images,orbit,gen,w,n,i,j,ab,
          counts,negative,positive,automorphisms,transitions,lengths,value;
    counts:=0;negative:=0;positive:=0;automorphisms:=0;transitions:=0;
    for row in F38StabilizerFixtures do
        rank:=row[1];F:=FreeGroup(rank);gens:=GeneratorsOfGroup(F);
        fixed:=F38SClass(F38SEval(gens,row[2]));
        moved:=F38SClass(F38SEval(gens,row[3]));
        if row[4]="infinite_orbit_witness" then
            images:=F38SAuto(gens,row[5]);automorphisms:=automorphisms+1;
            for j in [1..rank] do
                ab:=ExponentSums(images[j]);
                for i in [1..rank] do
                    if (ab[i]-(KroneckerDelta(i,j))) mod 3<>0 then
                        F38SFail("not in level-three kernel");
                    fi;
                od;
            od;
            if F38SClass(F38SEval(images,row[2]))<>fixed or
               F38SClass(F38SEval(images,row[3]))=moved then
                F38SFail("witness conjugacy classes");
            fi;
            value:=F38SEval(gens,row[3]);lengths:=[];
            for n in [1..Length(row[6])] do
                Add(lengths,Length(F38SClass(value)));
                value:=F38SEval(images,LetterRepAssocWord(value));
            od;
            if lengths<>row[6] then F38SFail("sample iteration lengths");fi;
            negative:=negative+1;
        elif row[4]="finite_orbit" then
            orbit:=Set(List(row[6],w->F38SClass(F38SEval(gens,w))));
            if not moved in orbit or Length(orbit)<>Length(row[6]) then
                F38SFail("orbit base or duplicate");
            fi;
            for gen in row[5] do
                images:=F38SAuto(gens,gen);automorphisms:=automorphisms+1;
                if F38SClass(F38SEval(images,row[2]))<>fixed then
                    F38SFail("stabilizer generator");
                fi;
                for w in orbit do
                    if not F38SClass(F38SEval(images,w)) in orbit then
                        F38SFail("finite orbit not invariant");
                    fi;
                    transitions:=transitions+1;
                od;
            od;
            positive:=positive+1;
        else F38SFail("unknown fixture kind");fi;
        counts:=counts+1;
        Print("F38 STABILIZER VERIFIED ",counts," ",row[4]," rank=",rank,"\n");
    od;
    Print("PASS F38 stabilizer GAP: ",negative," infinite-orbit witnesses; ",
          positive," finite invariant orbits; ",automorphisms,
          " inverse pairs; ",transitions," orbit transitions\n");
end;;
F38SMain();
QUIT_GAP(0);
