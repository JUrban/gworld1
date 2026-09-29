# Exact controls for infinitely many automorphism orbits of cyclic retracts.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
(function()
    local f,x,rel,p,ep,g,y,m,v,h,r,gens,bad,tail;
    f:=FreeGroup(4); x:=GeneratorsOfGroup(f);
    rel:=[Comm(x[1],x[3]),Comm(x[1],x[4]),
          Comm(x[2],x[3]),Comm(x[2],x[4])];
    p:=f/rel; ep:=NqEpimorphismNilpotentQuotient(p,2);
    g:=Image(ep); y:=List(GeneratorsOfGroup(p),a->Image(ep,a));
    if HirschLength(g)<>6 or Size(TorsionSubgroup(g))<>1 then
        Error("Wrong Heisenberg product");
    fi;
    for m in [1,2,5,17] do
        v:=y[1]*y[3]^m; h:=Subgroup(g,[v]);
        gens:=[v,One(g),One(g),One(g)];
        r:=GroupHomomorphismByImages(g,g,y,gens);
        if r=fail or Image(r,v)<>v or Image(r)<>h or Order(v)<>infinity then
            Error("Cyclic retraction failed");
        fi;
        Print("RETRACT m=",m," abelian coordinate contents=1,",m,"\n");
    od;
    # An integral unimodular abelianization shear that changes m need
    # not lift to an endomorphism.  It violates [a,d]=1.
    for tail in [1,2,-3] do
        gens:=[y[1]*y[3]^tail,y[2],y[3],y[4]];
        if Comm(gens[1],gens[4])=One(g) then Error("Negative control vanished"); fi;
        bad:=GroupHomomorphismByImages(g,g,y,gens);
        if bad<>fail then Error("Nonhomomorphic shear accepted"); fi;
    od;
    Print("PASS N9 cyclic retract family and nonlifting shears\n");
end)();
QUIT;
