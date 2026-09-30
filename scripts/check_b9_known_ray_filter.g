# Separate native free-group replay; original fixtures are not enlarged.
Read("research/certificates/B9-known-ray-filter-v1/fixtures.g");
Read("research/certificates/B9/height4-fixtures.g");
Read("research/certificates/B9-positive-parameters/endpoints-v1.g");
(function()
    local f,x,action,shift,inv,red,shelf,eps,bases,parameters,pairs,maxstep,
          ray,step,a,c,temp,r,p,q,indices,k,e,matches,actual,source,
          pairchecks,comparisons,smallchecks,indexchecks,boundarychecks,n,pi,t,j;
    maxstep:=B9RayChecks.max_step;
    f:=FreeGroup(maxstep+6);x:=GeneratorsOfGroup(f);
    action:=function(word)
        local out,letter,i,b,d;
        out:=ShallowCopy(x);
        for letter in word do
            i:=AbsInt(letter);b:=out[i];d:=out[i+1];
            if letter>0 then out[i]:=b*d*b^-1;out[i+1]:=b;
            else out[i]:=d;out[i+1]:=d^-1*b*d;fi;
        od;
        return out;
    end;
    shift:=w->List(w,j->SignInt(j)*(AbsInt(j)+1));
    inv:=w->List(Reversed(w),j->-j);
    red:=function(w)
        local out,letter;
        out:=[];
        for letter in w do
            if not IsEmpty(out) and out[Length(out)]=-letter then Remove(out);
            else Add(out,letter);fi;
        od;
        return out;
    end;
    shelf:=function(b,d)return red(Concatenation(b,shift(d),[1],inv(shift(b))));end;
    eps:=w->Sum(List(w,SignInt));
    bases:=[[[],[]],[[],[1]],[[1],[1]],[[1,1,-2],[]]];
    parameters:=[[],[2],[1,2],[1,1,-2]];
    pairs:=[];
    for ray in [1..4] do
        a:=bases[ray][1];c:=bases[ray][2];
        Add(pairs,[[a,c]]);
        for step in [1..maxstep] do
            temp:=shelf(a,c);c:=a;a:=temp;
            Add(pairs[ray],[a,c]);
        od;
    od;
    pairchecks:=0;
    for r in B9RayChecks.rays do
        a:=pairs[r.ray+1][r.step+1][1];c:=pairs[r.ray+1][r.step+1][2];
        if action(a)<>action(r.a) or action(c)<>action(r.c) or eps(a)<>r.exponent then
            Error("Ray reconstruction");fi;
        if action(Concatenation(a,shift(c)))<>
           action(Concatenation(parameters[r.ray+1],ListWithIdenticalEntries(r.step,1))) then
            Error("Parameter ray identity");fi;
        pairchecks:=pairchecks+1;
    od;
    # Enumerate the two-step exponent recurrence, independently of its inverted formula.
    indexchecks:=0;
    for r in Concatenation(B9RayChecks.records,B9RayChecks.index_checks) do
        e:=r.exponent;indices:=[];
        for ray in [1..4] do
            p:=eps(bases[ray][1]);q:=eps(bases[ray][2]);
            for step in [0..2*Maximum(e,0)+2] do
                if p=e then Add(indices,[ray-1,step]);fi;
                temp:=q+1;q:=p;p:=temp;
            od;
        od;
        if indices<>r.candidates or Length(indices)>8 then Error("Candidate index coverage");fi;
        indexchecks:=indexchecks+1;
    od;
    comparisons:=0;
    for r in B9RayChecks.records do
        if r.kind="height4" then source:=B9Records[r.source_index+1][1];
        else source:=B9EndpointRecords[r.source_index+1][2];fi;
        actual:=action(source);
        if actual<>action(r.word) or eps(source)<>r.exponent then Error("Original fixture binding");fi;
        matches:=[];
        for j in r.candidates do
            if actual=action(pairs[j[1]+1][j[2]+1][1]) then Add(matches,j);fi;
            comparisons:=comparisons+1;
        od;
        if matches<>r.matches then Error("Exact first-color matching");fi;
        if r.kind="endpoint" and IsEmpty(matches) then Error("Endpoint not on known ray");fi;
    od;
    smallchecks:=0;
    for r in B9RayChecks.small_cases do
        if action(Concatenation(r.a,shift(r.c)))<>action(r.parameter) or
           action(r.parameter)<>action(Concatenation(parameters[r.ray+1],
                            ListWithIdenticalEntries(r.step,1))) then Error("Small pair/coset");fi;
        smallchecks:=smallchecks+1;
    od;
    boundarychecks:=0;
    for r in B9RayChecks.boundaries do
        n:=Length(r.permutation);pi:=();
        for t in r.word do j:=AbsInt(t);pi:=(j,j+1)*pi;od;
        if List([1..n],j->j^pi)<>r.permutation or n^pi=n then Error("Outside B3 boundary");fi;
        boundarychecks:=boundarychecks+1;
    od;
    # Necessary exception: 1 and sigma1 are both special in the same B2 coset.
    if action(shelf([],[]))<>action([1]) then Error("Identity-color exception");fi;
    if action([1,1])=action([]) then Error("Nontrivial pure-braid control");fi;
    Print("RAY_PAIRS=",pairchecks," INDEX_RECORDS=",indexchecks,
          " WORD_COMPARISONS=",comparisons," SMALL_PAIRS=",smallchecks,
          " BOUNDARIES=",boundarychecks,"\n");
    Print("PASS independent GAP B9 fixed first color ray filter\n");
end)();
QUIT;
