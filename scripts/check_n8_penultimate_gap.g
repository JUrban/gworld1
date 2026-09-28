if LoadPackage("nq") <> true then FORCE_QUIT_GAP(1); fi;
Read("research/certificates/N8-penultimate/fixtures.g");
N8PenGroups := rec();;
N8PenGroup := function(r,c)
    local key;
    key:=Concatenation(String(r),"_",String(c));
    if not IsBound(N8PenGroups.(key)) then
        N8PenGroups.(key):=NilpotentQuotient(FreeGroup(r),c);
    fi;
    return N8PenGroups.(key);
end;;
N8PenEval := function(group,word)
    local ans,gens,s;
    ans:=One(group);gens:=GeneratorsOfGroup(group);
    for s in word do ans:=ans*gens[AbsInt(s)]^SignInt(s);od;
    return ans;
end;;
N8PenPositive:=0;;
for item in N8PenWitnesses do
    group:=N8PenGroup(item[1],item[2]);;
    target:=N8PenEval(group,item[3]);;
    if Comm(N8PenEval(group,item[4]),N8PenEval(group,item[5]))<>target then
        Print("FAIL N8 penultimate witness ",N8PenPositive,"\n");FORCE_QUIT_GAP(1);
    fi;
    N8PenPositive:=N8PenPositive+1;
od;
N8PenCount:=0;;N8PenNegative:=0;;
for item in N8PenBranches do
    group:=N8PenGroup(item[1],item[2]);;
    target:=N8PenEval(group,item[3]);;
    x:=N8PenEval(group,item[4]);;y:=N8PenEval(group,item[5]);;
    delta:=Comm(x,y)^-1*target;;
    corrections:=Concatenation(
        List(item[6],w->Comm(N8PenEval(group,w),y)),
        List(item[7],w->Comm(x,N8PenEval(group,w))));;
    if not ForAll(Concatenation([delta],corrections),
                  h->ForAll(GeneratorsOfGroup(group),z->Comm(h,z)=One(group))) then
        Print("FAIL N8 penultimate centrality\n");FORCE_QUIT_GAP(1);
    fi;
    soluble:=delta in Subgroup(group,corrections);;
    if soluble<>item[8] then
        Print("FAIL N8 penultimate membership branch ",N8PenCount,"\n");FORCE_QUIT_GAP(1);
    fi;
    N8PenCount:=N8PenCount+1;
    if not soluble then N8PenNegative:=N8PenNegative+1;fi;
od;
Print("PASS N8 penultimate GAP: ",N8PenPositive," witnesses; ",N8PenCount,
      " membership branches, including ",N8PenNegative," negative\n");
QUIT;
