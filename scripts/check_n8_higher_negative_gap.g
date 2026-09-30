# Reconstruct all exceptional obstructions of the higher-weight negative input.
N8GeneralFiles:=["research/certificates/N8-higher-negative-v1/fixtures.g"];;
N8GeneralFixtures:=fail;;
(function()
 local row,e,hnf,block,kernel,native,columns,transition,blocks,changes,lists,polys;
 hnf:=rows->Filtered(HermiteNormalFormIntegerMat(rows),r->ForAny(r,x->x<>0));
 Read(N8GeneralFiles[1]);
 if Length(N8GeneralFixtures)<>1 then Error("Expected one negative fixture");fi;
 row:=N8GeneralFixtures[1];
 if row.accepted or row.rank<>2 or row.class_bound<>11 then Error("Wrong fixture");fi;
 lists:=Filtered(row.events,e->e.event="complete-leading-list");
 if List(lists,e->e.weights)<>[[1,8],[2,7],[3,6],[4,5]] or
    List(lists,e->Length(e.pairs))<>[0,2,0,0] then Error("Leading-list coverage");fi;
 blocks:=0;changes:=0;polys:=[];block:=fail;
 for e in row.events do
  if e.event="exception-block" then
   if e.point=fail or e.weights<>[2,7] or e.offset<>1 then Error("Wrong block");fi;
   block:=e;kernel:=TransposedMat(e.kernel);
   native:=NullspaceIntMat(TransposedMat(e.columns));
   if hnf(kernel)<>hnf(native) then Error("Incomplete integer kernel");fi;
   if e.columns*e.point<>e.rhs then Error("Wrong affine point");fi;
   if Length(e.columns)<>99 or Length(e.axes)<>32 or Length(kernel)<>1 then
    Error("Unexpected block dimensions");fi;
   blocks:=blocks+1;
  elif e.event="quadratic-exception" then
   if block=fail or block.branch<>e.branch then Error("Missing block");fi;
   columns:=TransposedMat(e.adapted_kernel);
   transition:=List(columns,v->SolutionMat(kernel,v));
   if fail in transition or not ForAll(transition,r->ForAll(r,IsInt)) or
      AbsInt(DeterminantMat(transition))<>1 then Error("Lattice change");fi;
   if e.parameter_step<>1 or e.integer_roots<>[] then Error("Not negative");fi;
   Add(polys,e.polynomial);changes:=changes+1;
  fi;
 od;
 if blocks<>2 or changes<>2 or polys<>[[[2,1],[-2,1],[1,1]],[[2,1],[2,1],[1,1]]] or
    row.events[Length(row.events)].event<>"all-leading-branches-rejected" then
  Error("Full negative coverage mismatch");fi;
 Print("Higher-weight negative: two full integer kernels and unimodular changes; ",
       "polynomials T^2-2T+2 and T^2+2T+2\n");
end)();
Read("scripts/check_n8_general_solver_gap.g");
