# Bounded F20 probe. Method follows Moravec--Morse (2010), with a fresh
# iterative Hall enumeration and explicit target reductions.
# Pass -c 'F20Weight:=5;' or 6 before reading this file.
LoadPackage("kbmag");;
if not IsBound(F20Weight) then F20Weight:=6; fi;
if not IsBound(F20MaxRules) then F20MaxRules:=20000; fi;
if not IsBound(F20MaxLength) then F20MaxLength:=50; fi;
rank := 2;;
hall := [rec(weight:=1,parents:=[]),rec(weight:=1,parents:=[])];;
for w in [2..F20Weight+1] do
    size := Length(hall);;
    for i in [1..size] do
        for j in [1..i-1] do
            if hall[i].weight+hall[j].weight=w and
               (Length(hall[i].parents)=0 or hall[i].parents[2]<=j) then
                Add(hall,rec(weight:=w,parents:=[i,j]));;
            fi;
        od;
    od;
od;
n := Number(hall,h->h.weight<F20Weight);;
F := FreeGroup(n);;
fg := GeneratorsOfGroup(F);;
IndexGenerator := i->fg[n+1-i];;
expanded := [];; defining := [];;
for i in [1..Length(hall)] do
    h := hall[i];;
    if h.weight=1 then
        Add(expanded,IndexGenerator(i));;
    elif i<=n then
        u := h.parents[1];; v := h.parents[2];;
        Add(defining,IndexGenerator(i)/Comm(IndexGenerator(u),IndexGenerator(v)));;
        Add(expanded,IndexGenerator(i));;
    else
        Add(expanded,Comm(expanded[h.parents[1]],expanded[h.parents[2]]));;
    fi;
od;
kill := List(Filtered([1..Length(hall)],i->hall[i].weight=F20Weight),i->expanded[i]);;
targets := List(Filtered([1..Length(hall)],i->hall[i].weight=F20Weight+1),i->expanded[i]);;
rels := Concatenation(defining,kill);;
Print("Hall counts=",List([1..F20Weight+1],w->Number(hall,h->h.weight=w)),
      "; generators=",n,"; kill=",Length(kill),"; targets=",Length(targets),"\n");
G := F/rels;;
R := KBMAGRewritingSystem(G);;
SetOrderingOfKBMAGRewritingSystem(R,"recursive");;
opts := OptionsRecordOfKBMAGRewritingSystem(R);;
opts.maxeqns := F20MaxRules;;
opts.maxstates := 500000;;
if F20MaxLength<>false then
    opts.maxstoredlen := [F20MaxLength,F20MaxLength];;
fi;
SetInfoLevel(InfoRWS,1);;
answer := KnuthBendix(R);;
Print("KB return=",answer,"\n");
out := List(targets,w->ReducedWord(R,w));;
Print("Target reduced lengths=",List(out,Length),"\n");
Print("Trivial target reductions=",Number(out,w->Length(w)=0),"/",Length(targets),"\n");
Print("PASS bounded F20 rewriting probe completed (not a theorem marker)\n");
QUIT;
