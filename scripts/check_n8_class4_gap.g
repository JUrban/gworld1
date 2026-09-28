if LoadPackage("nq") <> true then FORCE_QUIT_GAP(1); fi;
Read("research/certificates/N8-class4/fixtures.g");
N8Groups := [FreeGroup(1)];
for n in [2..4] do
    N8Groups[n] := NilpotentQuotient(FreeGroup(n),4);
od;
N8Eval := function(group, word)
    local ans, gens, letter;
    ans := One(group); gens := GeneratorsOfGroup(group);
    for letter in word do ans := ans * gens[AbsInt(letter)]^SignInt(letter); od;
    return ans;
end;
N8Checked := 0;
for item in N8Fixtures do
    if item[3] then
        group := N8Groups[item[1]];
        if Comm(N8Eval(group,item[4]),N8Eval(group,item[5])) <> N8Eval(group,item[2]) then
            Print("FAIL witness at ",N8Checked,"\n"); FORCE_QUIT_GAP(1);
        fi;
        N8Checked := N8Checked+1;
    fi;
od;
Print("PASS N8 class-four GAP independently evaluated witnesses: ",N8Checked,"\n");
QUIT;
