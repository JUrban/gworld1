# Bounded audit of GSW's torsion-freeness assertion for a monotone profile.
# On three generators: singleton class=1, pair class=2, full class=C.
# No result here would by itself answer the arbitrary locally nilpotent cover question.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
f := FreeGroup(3);; x := GeneratorsOfGroup(f);; rel := [];;
for i in [1..3] do
    for j in [i+1..3] do
        w := Comm(x[j],x[i]);;
        Add(rel,Comm(w,x[i]));; Add(rel,Comm(w,x[j]));;
    od;
od;
p := f/rel;;
for cl in [3..8] do
    Print("Starting class ",cl,"\n");
    g := NilpotentQuotient(p,cl);;
    orders := RelativeOrdersOfPcp(Pcp(g));;
    Print("Class ",cl,"; Hirsch length ",HirschLength(g),
          "; finite nontrivial relative orders ",Filtered(orders,n->n>1),"\n");
    if ForAny(orders,n->n>1) then
        t := TorsionSubgroup(g);;
        Print("Torsion subgroup size ",Size(t),"; generators ",GeneratorsOfGroup(t),"\n");
    fi;
od;
Print("PASS N3 bounded pair-class-two probe completed\n");
QUIT;
