# Independently evaluate returned witnesses in GAP nq's collected pc groups.
if LoadPackage("nq") <> true then FORCE_QUIT_GAP(1); fi;
Read("research/certificates/N8-class3/fixtures.g");
N8Groups := [FreeGroup(1)];
# nq 2.5.11 aborts on the rank-one/class-three request in this installation.
# Rank one is already infinite cyclic, so no quotient computation is needed.
for n in [2..5] do
    N8Groups[n] := NilpotentQuotient(FreeGroup(n),3);
od;
N8Eval := function(group, word)
    local ans, gens, letter;
    ans := One(group); gens := GeneratorsOfGroup(group);
    for letter in word do
        ans := ans * gens[AbsInt(letter)]^SignInt(letter);
    od;
    return ans;
end;
N8Checked := 0;
for item in N8Fixtures do
    if item[3] then
        group := N8Groups[item[1]];
        target := N8Eval(group,item[2]);
        x := N8Eval(group,item[4]); y := N8Eval(group,item[5]);
        if Comm(x,y) <> target then
            Print("FAIL witness at ",N8Checked,"\n"); FORCE_QUIT_GAP(1);
        fi;
        N8Checked := N8Checked+1;
    fi;
od;
Print("PASS N8 GAP independently evaluated witnesses: ",N8Checked,"\n");
QUIT;
