if LoadPackage("nq") <> true then FORCE_QUIT_GAP(1); fi;
if not IsBound(N8IAFixtureOverride) then
    Read("research/certificates/N8-IA/fixtures.g");
fi;
N8IAGroups := rec();;
N8IAEval := function(group,word)
    local ans,gens,s;
    ans:=One(group);gens:=GeneratorsOfGroup(group);
    for s in word do ans:=ans*gens[AbsInt(s)]^SignInt(s);od;
    return ans;
end;
N8IAChecked:=0;
for item in N8IAFixtures do
    key:=Concatenation(String(item[1]),"_",String(item[2]));
    if not IsBound(N8IAGroups.(key)) then
        N8IAGroups.(key):=NilpotentQuotient(FreeGroup(item[1]),item[2]);
    fi;
    group:=N8IAGroups.(key);
    if Comm(N8IAEval(group,item[4]),N8IAEval(group,item[5])) <> N8IAEval(group,item[3]) then
        Print("FAIL N8 IA witness ",N8IAChecked,"\n");FORCE_QUIT_GAP(1);
    fi;
    N8IAChecked:=N8IAChecked+1;
od;
Print("PASS N8 IA GAP independently evaluated witnesses: ",N8IAChecked,"\n");
QUIT;
