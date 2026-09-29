if LoadPackage("fga")<>true then FORCE_QUIT_GAP(1);fi;
Read("research/certificates/H4-torsion-classes/fixtures.g");
H4TFail:=function(message) Print("FAIL ",message,"\n");FORCE_QUIT_GAP(1);end;;
H4TMain:=function()
    local item,n,M,Q,expected,reps,rels,x,t,G,A,classes,normalClasses,
          covered,c,orbits,F,gens,frels,P,pgens,epi,K,iso,L,simplified,
          checked,kernels;
    checked:=0;kernels:=0;
    for item in H4TorsionFixtures do
        n:=item[1];M:=item[2];Q:=item[3];expected:=item[4];
        reps:=item[5];rels:=item[6];
        if n>3 then continue;fi;
        x:=PermList(Concatenation([2..M],[1]));
        t:=PermList(List([0..M-1],a->(((M+1)/2)*a) mod M+1));
        G:=Group(x,t);A:=Group(x);
        if Size(G)<>M*Q or t*x*t^-1<>x^2 then H4TFail("model");fi;
        classes:=ConjugacyClasses(G);
        normalClasses:=Filtered(classes,c->Representative(c) in A);
        if Length(normalClasses)<>expected then H4TFail("class count");fi;
        if Sum(normalClasses,Size)<>M then H4TFail("normal coverage");fi;
        covered:=Set(List(reps,a->PositionProperty(normalClasses,c->x^a in c)));
        if covered<>[1..expected] then H4TFail("orbit representatives");fi;
        if not IsConjugate(G,x,x^2) then H4TFail("fusion control");fi;
        checked:=checked+1;
        Print("H4 TORSION CLASSES VERIFIED n=",n," normal=",expected,
              " all=",Length(classes),"\n");
        if n<=2 then
            # Independently rewrite the finite-index kernel of K_n * Z -> K_n.
            # An empty relator list with |K_n| free generators verifies the
            # claimed free kernel for these two bounded input presentations.
            F:=FreeGroup(n+3);gens:=GeneratorsOfGroup(F);
            frels:=List(rels,w->Product(w,a->gens[AbsInt(a)]^SignInt(a)));
            P:=F/frels;pgens:=GeneratorsOfGroup(P);
            epi:=GroupHomomorphismByImages(P,G,pgens,
                Concatenation([x],List([0..n],i->t^(2^i)),[One(G)]));
            if epi=fail or not IsSurjective(epi) then H4TFail("epimorphism");fi;
            K:=Kernel(epi);
            iso:=IsomorphismFpGroup(K);L:=Image(iso);
            simplified:=SimplifiedFpGroup(L);
            if Length(RelatorsOfFpGroup(simplified))<>0 or
               Length(GeneratorsOfGroup(simplified))<>M*Q then
                H4TFail("free-kernel presentation");
            fi;
            kernels:=kernels+1;
            Print("H4 FREE KERNEL VERIFIED n=",n," rank=",M*Q,"\n");
        fi;
    od;
    Print("PASS H4 torsion GAP: ",checked," conjugacy-class partitions; ",
          kernels," free-kernel presentations\n");
end;;
H4TMain();
QUIT_GAP(0);
