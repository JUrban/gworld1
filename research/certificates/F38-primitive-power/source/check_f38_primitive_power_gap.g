Read("research/certificates/F38-primitive-power/formulas.g");;
Read("research/certificates/F38-primitive-power/normalizations.g");;
F38PFail:=function(s) Print("FAIL ",s,"\n");FORCE_QUIT_GAP(1);end;;
F38PEval:=function(gens,w)
    local out,x;
    out:=One(gens[1]);for x in w do out:=out*gens[AbsInt(x)]^SignInt(x);od;
    return out;
end;;
F38PClass:=function(word)
    local w,n;
    w:=LetterRepAssocWord(word);
    while Length(w)>1 and w[1]=-Last(w) do w:=w{[2..Length(w)-1]};od;
    n:=Length(w);if n=0 then return [];fi;
    return Minimum(List([0..n-1],i->Concatenation(w{[i+1..n]},w{[1..i]})));
end;;
F38PAuto:=function(gens,record)
    local images,inverse,i;
    images:=List(record[1],w->F38PEval(gens,w));
    inverse:=List(record[2],w->F38PEval(gens,w));
    for i in [1..Length(gens)] do
        if F38PEval(images,LetterRepAssocWord(inverse[i]))<>gens[i] or
           F38PEval(inverse,LetterRepAssocWord(images[i]))<>gens[i] then
            F38PFail("inverse pair");
        fi;
    od;
    return images;
end;;
F38PCarrierStep:=function(b,c,state,x)
    if x=b then if state=0 then return 1;else return fail;fi;fi;
    if x=-b then if state=1 then return 0;else return fail;fi;fi;
    if AbsInt(x)=c or state=0 then return state;fi;
    return fail;
end;;
F38PGraphCheck:=function(rank)
    local states,alphabet,twists,edges,i,x,j,next,keep,changed,remove,out,
          core,expected,d,rawcount;
    states:=Tuples([0,1],3);alphabet:=Concatenation([-rank..-1],[1..rank]);
    twists:=[[2,3],[3,2],[2,1]];edges:=[];
    for i in [1..8] do
        for x in alphabet do
            next:=List([1..3],j->F38PCarrierStep(twists[j][1],twists[j][2],states[i][j],x));
            if not fail in next then Add(edges,[i,x,Position(states,next)]);fi;
        od;
    od;
    rawcount:=Length(edges);keep:=[1..8];changed:=true;
    while changed do
        remove:=Filtered(keep,i->Number(edges,e->e[1]=i and e[3] in keep)<=1);
        changed:=Length(remove)>0;keep:=Difference(keep,remove);
    od;
    core:=Set(Filtered(edges,e->e[1] in keep and e[3] in keep));
    expected:=[];
    for d in Concatenation([1],[4..rank]) do
        i:=Position(states,[0,0,0]);Add(expected,[i,d,i]);Add(expected,[i,-d,i]);
    od;
    i:=Position(states,[0,0,1]);Add(expected,[i,1,i]);Add(expected,[i,-1,i]);
    if core<>Set(expected) then F38PFail("three-carrier product core");fi;
    Print("CARRIER rank=",rank," states=8 directed_edges=",rawcount," core_edges=",Length(core),"\n");
end;;
F38PRun:=function()
    local groups,genss,row,r,gens,b,c,n,images,word,lengths,j,mu,theta,
          fixed,moved,normal,v,i,number,positive,negative,normalized,expected;
    groups:=List([1..5],FreeGroup);genss:=List(groups,GeneratorsOfGroup);
    number:=0;
    for row in F38NielsenFormulas do
        r:=row[1];gens:=genss[r];word:=row[2];b:=row[3];c:=row[4];lengths:=[];
        for n in F38Powers do
            images:=ShallowCopy(gens);images[b]:=gens[b]*gens[c]^n;
            Add(lengths,Length(F38PClass(F38PEval(images,word))));
            number:=number+1;
        od;
        if lengths<>row[5] then F38PFail("Nielsen length formula samples");fi;
        for n in [row[7]+1,row[7]+7] do
            images:=ShallowCopy(gens);images[b]:=gens[b]*gens[c]^n;
            if Length(F38PClass(F38PEval(images,word)))<>row[6]*n+row[8] then
                F38PFail("eventual growth formula");
            fi;
            number:=number+1;
        od;
    od;
    positive:=0;negative:=0;
    for row in F38PrimitiveCases do
        r:=row[1];gens:=genss[r];fixed:=row[2];moved:=row[3];
        mu:=F38PAuto(gens,row[4]);
        if F38PClass(F38PEval(mu,fixed))<>List([1..row[5]],i->1) then
            F38PFail("primitive-power normalization");
        fi;
        normalized:=F38PClass(F38PEval(mu,moved));
        if row[6]<>0 then
            if normalized<>List([1..AbsInt(row[6])],i->SignInt(row[6])) then
                F38PFail("positive common-power identity");
            fi;
            positive:=positive+1;
        else
            theta:=F38PAuto(gens,row[9]);b:=row[7];c:=row[8];
            if F38PClass(F38PEval(theta,fixed))<>fixed then F38PFail("fixed input");fi;
            # Check mu theta = sigma mu on every basis element, exactly.
            images:=ShallowCopy(gens);images[b]:=gens[b]*gens[c];
            for j in [1..r] do
                if F38PEval(mu,LetterRepAssocWord(theta[j]))<>
                   F38PEval(images,LetterRepAssocWord(mu[j])) then
                    F38PFail("transported Nielsen automorphism");
                fi;
            od;
            if row[10]<=0 then F38PFail("missing positive slope");fi;
            n:=row[11]+5;images[b]:=gens[b]*gens[c]^n;
            if Length(F38PClass(F38PEval(images,normalized)))<>row[10]*n+row[12] then
                F38PFail("negative growth certificate");
            fi;
            negative:=negative+1;
        fi;
    od;
    for r in [3,4,5] do F38PGraphCheck(r);od;
    Print("formulas=",Length(F38NielsenFormulas)," native_substitutions=",number,
          " positive_normalizations=",positive," negative_transports=",negative,"\n");
    Print("PASS F38 PRIMITIVE POWER GAP\n");
end;;
F38PRun();;
QUIT_GAP(0);
