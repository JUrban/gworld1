# Native abelian/trivial groups check command boundaries independently.
if LoadPackage("polycyclic")<>true then FORCE_QUIT_GAP(1);fi;
N8WordBoundaryCheck:=function(row)
 local r,c,group,gens,target,i,factors,side,j;
 r:=row.input.rank;c:=row.input.class_bound;
 if c=0 or r=0 then
  group:=AbelianPcpGroup([]);gens:=List([1..r],x->One(group));
 else group:=AbelianPcpGroup(List([1..r],x->0));gens:=GeneratorsOfGroup(group);fi;
 target:=One(group);
 for i in row.input.word do target:=target*gens[AbsInt(i)]^SignInt(i);od;
 if row.result.answer<>(target=One(group)) then Error("Boundary decision mismatch");fi;
 if row.result.answer then
  factors:=[One(group),One(group)];
  for side in [1,2] do
   for j in [1..Length(row.result.factor_coordinates[side])] do
    factors[side]:=factors[side]*gens[j]^row.result.factor_coordinates[side][j];
   od;
  od;
  if Comm(factors[1],factors[2])<>target then Error("Boundary witness failure");fi;
 fi;
end;
for row in N8WordBoundaries do N8WordBoundaryCheck(row);od;
Print("PASS N8 word GAP boundaries ",Length(N8WordBoundaries),"\n");
