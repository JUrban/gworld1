# Exact audit of the central-product obstruction and nilpotent-coproduct repair.
# No decision procedure or counterexample for fixed-ambient problem N9(a).
# Commutator convention throughout: x^-1*y^-1*x*y.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
SetInfoLevel(InfoWarning,0);

f := FreeGroup(4);;
fg := GeneratorsOfGroup(f);;
a := fg[1];; b := fg[2];; x := fg[3];; y := fg[4];;
base := NilpotentQuotient(FreeGroup(2),2);;
bg := GeneratorsOfGroup(base){[1..2]};;
z := Comm(bg[1],bg[2]);;
if Order(z)<>infinity then Error("Base commutator must have infinite order"); fi;
cross := [Comm(x,a),Comm(x,b),Comm(y,a),Comm(y,b)];;

CheckN9Parameter := function(c)
    local rel,good,gg,target,ret,emb,bad,dg,old,attempted,zero_map;
    rel := Comm(x,y)*Comm(a,b)^(-c);;
    good := NilpotentQuotient(f/[rel],2);;
    gg := GeneratorsOfGroup(good){[1..4]};;
    target := [bg[1],bg[2],bg[1]^c,bg[2]];;
    ret := GroupHomomorphismByImages(good,base,gg,target);;
    emb := GroupHomomorphismByImages(base,good,bg,gg{[1..2]});;
    if ret=fail or emb=fail then Error("Corrected maps are not homomorphisms"); fi;
    if ForAny(bg,t->Image(ret,Image(emb,t))<>t) then
        Error("Corrected retraction does not split the inclusion");
    fi;
    if Image(ret,Comm(gg[3],gg[4]))<>z^c then
        Error("Corrected commutator equation failed");
    fi;
    if HirschLength(good)<>9 then Error("Unexpected corrected ambient rank"); fi;

    bad := NilpotentQuotient(f/Concatenation([rel],cross),2);;
    dg := GeneratorsOfGroup(bad){[1..4]};;
    old := Subgroup(bad,dg{[1..2]});;
    if HirschLength(bad)<>5 or HirschLength(old)<>3 then
        Error("Central-product ambient or embedded base rank is wrong");
    fi;
    if Order(Comm(dg[1],dg[2]))<>infinity then
        Error("Central product killed the embedded base commutator");
    fi;
    if ForAny([1,2],i->ForAny([3,4],j->Comm(dg[i],dg[j])<>One(bad))) then
        Error("Expected cross-commutation missing");
    fi;
    attempted := GroupHomomorphismByImages(bad,base,dg,target);;
    if c<>0 and attempted<>fail then
        Error("Incorrect central-product assignment should fail");
    fi;
    # For c=0 the chosen y->b still fails cross-commutation. A genuine
    # retraction exists by sending both new generators to identity.
    if attempted<>fail then Error("Cross-commutation negative control missed"); fi;
    zero_map := GroupHomomorphismByImages(bad,base,dg,
        [bg[1],bg[2],One(base),One(base)]);;
    if (c=0)<>(zero_map<>fail) then Error("Zero-input control failed"); fi;
    if c<>0 and Comm(target[3],target[2])=One(base) then
        Error("Explicit violated relation did not detect the error");
    fi;
    Print(Concatenation("c=",String(c),": coproduct quotient split verified; central-product assignment rejected; ranks9,5,3.\n"));
end;
for c in [-2,0,1,3] do CheckN9Parameter(c); od;
Print("PASS N9 central-product obstruction and coproduct repair\n");
QUIT;
