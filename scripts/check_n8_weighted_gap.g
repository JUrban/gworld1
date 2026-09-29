# Independent GAP/nq verification of the integral automorphisms themselves.
if LoadPackage("nq") <> true then FORCE_QUIT_GAP(1); fi;
if not IsBound(N8WeightedFiles) then
    Error("Set N8WeightedFiles to the explicit fixture paths");
fi;
N8WeightedGroups := rec();;
N8WeightedElement := function(hall,terms)
    local ans,item;
    ans:=One(hall[1]);
    for item in terms do ans:=ans*hall[item[1]+1]^item[2];od;
    return ans;
end;
N8WeightedCount:=0;; N8WeightedImages:=0;; N8WeightedCommutators:=0;;
for filename in N8WeightedFiles do
    Read(filename);
    for item in N8WeightedFixtures do
        key:=Concatenation(String(item[1]),"_",String(item[2]));
        if not IsBound(N8WeightedGroups.(key)) then
            N8WeightedGroups.(key):=NilpotentQuotient(FreeGroup(item[1]),item[2]);
        fi;
        group:=N8WeightedGroups.(key);
        originalGenerators:=GeneratorsOfGroup(group);
        hall:=[];
        for i in [1..Length(item[3])] do
            pair:=item[3][i][2];
            if Length(pair)=0 then Add(hall,originalGenerators[i]);
            else Add(hall,Comm(hall[pair[1]+1],hall[pair[2]+1]));fi;
        od;
        kgens:=List(item[4],terms->N8WeightedElement(hall,terms));
        plus:=List(item[5],terms->N8WeightedElement(hall,terms));
        minus:=List(item[6],terms->N8WeightedElement(hall,terms));
        subgroup:=Subgroup(group,kgens);
        if not ForAll(Concatenation(plus,minus),v->v in subgroup) then
            Error("An alleged integral image is outside K");
        fi;
        forward:=GroupHomomorphismByImages(subgroup,subgroup,kgens,plus);
        backward:=GroupHomomorphismByImages(subgroup,subgroup,kgens,minus);
        if forward=fail or backward=fail then Error("Not group homomorphisms");fi;
        for i in [1..Length(kgens)] do
            if Image(backward,Image(forward,kgens[i]))<>kgens[i] or
               Image(forward,Image(backward,kgens[i]))<>kgens[i] then
                Error("Two-sided inverse failure");
            fi;
            N8WeightedImages:=N8WeightedImages+2;
        od;
        vals:=List(item{[7..12]},terms->N8WeightedElement(hall,terms));
        if Comm(vals[1],vals[2])<>vals[5] or Comm(vals[3],vals[4])<>vals[6] then
            Error("Factor witness failure");
        fi;
        if Image(forward,vals[1])<>vals[3] or Image(forward,vals[2])<>vals[4]
           or Image(forward,vals[5])<>vals[6] then
            Error("Automorphism transport failure");
        fi;
        N8WeightedCommutators:=N8WeightedCommutators+2;
        N8WeightedCount:=N8WeightedCount+1;
    od;
od;
Print("PASS N8 weighted GAP: ",N8WeightedCount," automorphisms; ",
      N8WeightedImages," inverse images; ",N8WeightedCommutators," commutators\n");
QUIT;
