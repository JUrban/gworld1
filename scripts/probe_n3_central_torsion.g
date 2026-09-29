# A bounded test of stronger local-bound enlargements for N3.
# Only torsion in the LAST lower-central layer is examined.  Its absence
# does not imply that the entire source group is torsion-free.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
MakeReadWriteGlobal("USE_COMBINATORIAL_COLLECTOR");
USE_COMBINATORIAL_COLLECTOR:=true;
MakeReadOnlyGlobal("USE_COMBINATORIAL_COLLECTOR");
if not IsBound(N3PairBound) then N3PairBound:=4; fi;
if not IsBound(N3FullBound) then N3FullBound:=8; fi;

N3CentralModel:=function(bound,cl)
    local f,x,rel,i,j,tail,w,k,p,ep,g,y,lcs;
    f:=FreeGroup(3); x:=GeneratorsOfGroup(f); rel:=[];
    for i in [1..2] do
        for j in [i+1..3] do
            for tail in Tuples([i,j],bound-1) do
                w:=Comm(x[j],x[i]);
                for k in tail do w:=Comm(w,x[k]); od;
                Add(rel,w);
            od;
        od;
    od;
    Print("QUOTIENT start ",bound," ",cl,"\n");
    p:=f/rel; ep:=NqEpimorphismNilpotentQuotient(p,cl);
    g:=Image(ep); y:=List(GeneratorsOfGroup(p),a->Image(ep,a));
    Print("QUOTIENT ready ",bound," ",cl," Hirsch ",HirschLength(g),"\n");
    lcs:=LowerCentralSeries(g);
    if Length(lcs)<>cl+1 then Error("Unexpected nilpotency class"); fi;
    # nq has already computed the exact abelian factors.  At the last
    # layer the factor is the subgroup itself.  Avoid recomputing all
    # pairwise commutators of its hundreds of known-central generators.
    SetIsAbelian(lcs[cl],true);
    return rec(group:=g,gens:=y,ep:=ep,last:=lcs[cl],
               last_invariants:=g!.LowerCentralFactors[cl],
               rel:=rel,freegens:=x);
end;

N3CentralMain:=function(bound,cl)
    local s,t,tor,hom,z,im,w,images,sub;
    s:=N3CentralModel(bound,cl);
    Print("LAST_LAYER invariants ",s.last_invariants,"\n");
    if ForAll(s.last_invariants,n->n=0) then
        Print("RESULT no last-layer torsion; full torsion not tested\n");
        return;
    fi;
    tor:=TorsionSubgroup(s.last);
    Print("LAST_LAYER torsion order ",Size(tor),"\n");
    if Size(tor)=1 then
        Print("RESULT no last-layer torsion; full torsion not tested\n");
        return;
    fi;
    t:=N3CentralModel(2,cl);
    # The target satisfies every source defining relation.  Its class
    # is the same cl; these facts justify the induced quotient map.
    for w in s.rel do
        if MappedWord(w,s.freegens,t.gens)<>One(t.group) then
            Error("Source relation does not vanish in target");
        fi;
    od;
    hom:=GroupHomomorphismByImagesNC(s.group,t.group,s.gens,t.gens);
    images:=[];
    for z in GeneratorsOfGroup(tor) do
        if Order(z)=infinity or Order(z)=1 then Error("Bad torsion generator"); fi;
        im:=Image(hom,z); Add(images,im);
        Print("TORSION source order ",Order(z)," image order ",Order(im),"\n");
        if im<>One(t.group) then
            w:=PreImagesRepresentative(s.ep,z);
            if Image(s.ep,w)<>z then Error("Preimage failure"); fi;
            Print("WITNESS word ",LetterRepAssocWord(UnderlyingElement(w)),"\n");
        fi;
    od;
    sub:=Subgroup(t.group,images);
    Print("RESULT central torsion image order ",Size(sub),"\n");
end;
N3CentralMain(N3PairBound,N3FullBound);
Print("PASS N3 central torsion probe completed\n");
QUIT;
