# Independent ordinary-group construction for nested nilpotency constraints.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
Read("research/certificates/N3-nested-cover/fixtures.g");

N3SimpleComms := function(gens, weight)
    local words, next, k, w, x, y;
    words := ShallowCopy(gens);
    for k in [2..weight] do
        next := [];
        for w in words do
            for x in gens do
                y := Comm(w,x);
                if y <> One(x) then AddSet(next,y); fi;
            od;
        od;
        words := next;
    od;
    return words;
end;

N3LayerRanks := function(g)
    local series, out, i, inv;
    series := LowerCentralSeries(g);
    out := [];
    for i in [1..Length(series)-1] do
        inv := AbelianInvariants(series[i]/series[i+1]);
        if ForAny(inv, n->n<>0) then Error("Torsion in a lower central factor"); fi;
        Add(out,Length(inv));
    od;
    return out;
end;

checked := 0;;
for fixture in N3NestedFixtures do
    stages := fixture[1];; expected := fixture[2];;
    for n in [1..Length(stages)] do
        rank := stages[n][1];; cutoff := stages[n][2];;
        f := FreeGroup(rank);; x := GeneratorsOfGroup(f);; rel := [];;
        for j in [1..n-1] do
            Append(rel,N3SimpleComms(x{[1..stages[j][1]]},stages[j][2]+1));
        od;
        p := f/rel;; ep := NqEpimorphismNilpotentQuotient(p,cutoff);;
        g := Image(ep);; y := List(GeneratorsOfGroup(p),a->Image(ep,a));;
        actual := N3LayerRanks(g);;
        while Length(actual)<cutoff do Add(actual,0); od;
        if actual<>expected[n] then Error("PBW layer-rank prediction failed"); fi;
        if Size(TorsionSubgroup(g))<>1 then Error("Unexpected group torsion"); fi;
        if n>1 then
            previousRank := stages[n-1][1];;
            h := Subgroup(g,y{[1..previousRank]});;
            actual := N3LayerRanks(h);;
            while Length(actual)<stages[n-1][2] do Add(actual,0); od;
            if actual<>expected[n-1] then Error("Nested subgroup changed"); fi;
            images := List([1..rank],i->One(g));;
            for j in [1..previousRank] do images[j]:=y[j]; od;
            retraction := GroupHomomorphismByImages(g,h,y,images);;
            if retraction=fail then Error("Coordinate retraction failed"); fi;
            for j in [1..previousRank] do
                if Image(retraction,y[j])<>y[j] then Error("Retraction not identity"); fi;
            od;
        fi;
        checked := checked+1;;
        Print("Nested stages ",stages{[1..n]},"; LCS ranks ",actual,"\n");
    od;
od;

# Negative control: a torsion-free class-two factor may have torsion in
# its abelianization. Adding one free generator and truncating at class two
# then creates an element of order four.
f := FreeGroup(4);; x := GeneratorsOfGroup(f);;
p := f/[Comm(x[1],x[2])*x[3]^-4,Comm(x[1],x[3]),Comm(x[2],x[3])];;
ep := NqEpimorphismNilpotentQuotient(p,2);; g := Image(ep);;
y := List(GeneratorsOfGroup(p),a->Image(ep,a));;
h := Subgroup(g,y{[1..3]});;
if Size(TorsionSubgroup(h))<>1 then Error("Control factor not torsion-free"); fi;
if Order(y[3])<>infinity then Error("Control central generator finite"); fi;
if Order(Comm(y[3],y[4]))<>4 then Error("Expected order-four obstruction absent"); fi;
Print("Negative control: torsion-free factor; order-four mixed commutator.\n");
Print("PASS N3 nested GAP checks: ",checked," stages and one negative control\n");
QUIT;
