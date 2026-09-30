# Reusable verbatim fixture definitions from check_n5_general_malcev_input.g.
if LoadPackage("nq")<>true or LoadPackage("polycyclic")<>true then Error("nq/polycyclic required");fi;
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
