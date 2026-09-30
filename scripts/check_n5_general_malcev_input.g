Read("scripts/n5_general_malcev_input.g");
Read("scripts/n5_class2_json.g");
if LoadPackage("nq")<>true then Error("nq required");fi;
N5MalcevPowerControl:=function()
    local c,g;
    c:=FromTheLeftCollector(4);
    SetRelativeOrder(c,1,2);SetPower(c,1,[3,1]);
    SetConjugate(c,2,1,[2,1,4,1]);
    SetConjugate(c,3,2,[3,1,4,-2]);
    UpdatePolycyclicCollector(c);
    if not IsConfluent(c) then Error("power control inconsistent");fi;
    g:=PcpGroupByCollector(c);
    if not IsTorsionFree(g) or RelativeOrdersOfPcp(Pcp(g))[1]<>2 then
        Error("power control not torsion-free with finite relative order");
    fi;
    return g;
end;
N5MalcevFixtures:=function()
    local h,c3,c4,d8;
    h:=NilpotentQuotient(FreeGroup(2),2);
    c3:=NilpotentQuotient(FreeGroup(2),3);
    c4:=NilpotentQuotient(FreeGroup(2),4);
    d8:=Image(IsomorphismPcpGroup(SmallGroup(8,3)));
    return [
        ["trivial",AbelianPcpGroup([]),[]],
        ["finite_nonabelian",d8,[]],
        ["abelian3",AbelianPcpGroup([0,0,0]),[1,1,1]],
        ["heisenberg",h,[3]],
        ["free_class3",c3,[5]],
        ["free_class4",c4,[8]],
        ["mixed_classes",DirectProduct(c3,h,AbelianPcpGroup([0])),[1,3,5]],
        ["noncentral_finite_torsion",DirectProduct(c3,d8),[5]],
        ["finite_relative_order",N5MalcevPowerControl(),[3]]
    ];
end;
N5RunMalcevFixtures:=function()
    local fixtures,records,f,m;
    fixtures:=N5MalcevFixtures();records:=[];
    for f in fixtures do
        m:=N5GeneralMalcevInput(f[2]);
        m.data.name:=f[1];m.data.expected_dimensions:=f[3];
        m.data.original_relative_orders:=RelativeOrdersOfPcp(Pcp(f[2]));
        m.data.original_nilclass:=NilpotencyClassOfGroup(f[2]);
        Add(records,m.data);
        Print(f[1],": Hirsch ",m.data.hirsch_length,", matrix dimension ",m.data.matrix_dimension,"\n");
    od;
    N5WriteCoordinateJson("research/certificates/N5-general-malcev-input/input-v1.json",records);
    Print("PASS N5 general Malcev native input: ",Length(records)," groups\n");
end;
N5RunMalcevFixtures();
QUIT;
