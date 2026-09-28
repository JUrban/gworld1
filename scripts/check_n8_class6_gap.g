if LoadPackage("nq") <> true then FORCE_QUIT_GAP(1); fi;
Read("research/certificates/N8-class6/fixtures.g");
N8C6Groups:=rec();;
N8C6Group:=function(r,c)
    local key;
    key:=Concatenation(String(r),"_",String(c));
    if not IsBound(N8C6Groups.(key)) then
        N8C6Groups.(key):=NilpotentQuotient(FreeGroup(r),c);
    fi;
    return N8C6Groups.(key);
end;;
N8C6Eval:=function(group,word)
    local ans,gens,s;
    ans:=One(group);gens:=GeneratorsOfGroup(group);
    for s in word do ans:=ans*gens[AbsInt(s)]^SignInt(s);od;
    return ans;
end;;
N8C6Positive:=0;;
for item in N8C6Witnesses do
    group:=N8C6Group(item[1],item[2]);;
    if Comm(N8C6Eval(group,item[4]),N8C6Eval(group,item[5]))<>
       N8C6Eval(group,item[3]) then
        Print("FAIL class6 witness\n");FORCE_QUIT_GAP(1);
    fi;
    N8C6Positive:=N8C6Positive+1;
od;
N8C6Count:=0;;N8C6Negative:=0;;x:=fail;;y:=fail;;
for item in N8C6Steps do
    group:=N8C6Group(item[1],item[2]);;
    x:=N8C6Eval(group,item[4]);;y:=N8C6Eval(group,item[5]);;
    delta:=Comm(x,y)^-1*N8C6Eval(group,item[3]);;
    corrections:=Concatenation(
        List(item[6],w->Comm(N8C6Eval(group,w),y)),
        List(item[7],w->Comm(x,N8C6Eval(group,w))));;
    if not ForAll(Concatenation([delta],corrections),
                  h->ForAll(GeneratorsOfGroup(group),z->Comm(h,z)=One(group))) then
        Print("FAIL class6 centrality\n");FORCE_QUIT_GAP(1);
    fi;
    soluble:=delta in Subgroup(group,corrections);;
    if soluble<>item[8] then
        Print("FAIL class6 lifting membership\n");FORCE_QUIT_GAP(1);
    fi;
    N8C6Count:=N8C6Count+1;
    if not soluble then N8C6Negative:=N8C6Negative+1;fi;
od;
Print("PASS N8 class6 GAP: ",N8C6Positive," witnesses\n");
Print("Lifting steps: ",N8C6Count,"; negative: ",N8C6Negative,"\n");
QUIT;
