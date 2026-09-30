# Check higher leading weights and full integer block kernels, then native groups.
N8GeneralFiles:=["research/certificates/N8-higher-leading-equal-v1/fixtures.g",
                 "research/certificates/N8-higher-leading-exception-v1/fixtures.g"];;
(function()
 local file,row,e,weights,first,side,i,kernel,native,hnf,block,columns,
       transition,blocks,changes,positiveWeights,expected;
 hnf:=rows->Filtered(HermiteNormalFormIntegerMat(rows),r->ForAny(r,x->x<>0));
 blocks:=0;changes:=0;positiveWeights:=[];
 for file in N8GeneralFiles do
  Read(file);
  for row in N8GeneralFixtures do
   if not row.accepted then Error("Planted higher-leading fixture rejected");fi;
   weights:=[];
   for side in [1..2] do
    first:=First([1..Length(row.hall)],i->row.factor_coordinates[side][i]<>0);
    if first=fail then Error("Trivial output factor");fi;
    Add(weights,row.hall[first][1]);
   od;
   Add(positiveWeights,weights);block:=fail;
   for e in row.events do
    if e.event="exception-block" and e.point<>fail then
     block:=e;kernel:=TransposedMat(e.kernel);
     native:=NullspaceIntMat(TransposedMat(e.columns));
     if hnf(kernel)<>hnf(native) then Error("Incomplete weighted integer kernel");fi;
     if e.columns*e.point<>e.rhs then Error("Wrong weighted affine point");fi;
     blocks:=blocks+1;
    elif e.event="quadratic-exception" then
     if block=fail or block.branch<>e.branch then Error("Missing weighted block");fi;
     columns:=TransposedMat(e.adapted_kernel);
     transition:=List(columns,v->SolutionMat(kernel,v));
     if fail in transition or not ForAll(transition,r->ForAll(r,IsInt)) or
        AbsInt(DeterminantMat(transition))<>1 then Error("Weighted lattice change");fi;
     if block.weights<>[2,7] or block.offset<>1 then Error("Intended weighted exception missing");fi;
     changes:=changes+1;
    fi;
   od;
  od;
 od;
 if positiveWeights<>[[2,2],[2,7]] or blocks<>1 or changes<>1 then
  Error("Higher-leading branch coverage mismatch");
 fi;
 Print("Higher leading weights ",positiveWeights,"; full integer blocks ",blocks,
       "; unimodular changes ",changes,"\n");
end)();
Read("scripts/check_n8_general_solver_gap.g");
