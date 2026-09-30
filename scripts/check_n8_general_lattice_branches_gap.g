# Native full integer-kernel and unimodular-step checks, before group replay.
N8LatticeHNF:=function(rows)
 return Filtered(HermiteNormalFormIntegerMat(rows),r->ForAny(r,x->x<>0));
end;
N8LatticeCounts:=rec(blocks:=0,fixed:=0,nonunit:=0,changes:=0);;
N8LatticeCase:=function(row)
 local block,e,kernel,native,first,projected,j,cols,coefficients,transition,step;
 block:=fail;
 for e in row.events do
  if e.event="exception-block" and e.point<>fail then
   block:=e;kernel:=TransposedMat(e.kernel);
   native:=NullspaceIntMat(TransposedMat(e.columns));
   if N8LatticeHNF(kernel)<>N8LatticeHNF(native) then Error("Incomplete integer block kernel");fi;
   if e.columns*e.point<>e.rhs then Error("Wrong affine block point");fi;
   N8LatticeCounts.blocks:=N8LatticeCounts.blocks+1;
  elif e.event="fixed-exception" then
   if block=fail or block.branch<>e.branch then Error("Missing block");fi;
   first:=Length(Filtered(block.axes,a->a[2]=block.weights[a[1]+1]+block.offset));
   if not ForAll(block.kernel{[1..first]},r->ForAll(r,x->x=0)) then Error("Parameter is not fixed");fi;
   if e.point<>block.point{[1..first]} then Error("Fixed prefix changed");fi;
   N8LatticeCounts.fixed:=N8LatticeCounts.fixed+1;
  elif e.event="quadratic-exception" then
   kernel:=TransposedMat(block.kernel);cols:=TransposedMat(e.adapted_kernel);
   transition:=List(cols,v->SolutionMat(kernel,v));
   if fail in transition or not ForAll(transition,r->ForAll(r,IsInt)) then Error("Nonintegral lattice change");fi;
   if AbsInt(DeterminantMat(transition))<>1 then Error("Lattice change is not unimodular");fi;
   first:=Length(Filtered(block.axes,a->a[2]=block.weights[a[1]+1]+block.offset));
   projected:=List(cols,v->v{[1..first]});
   if not ForAll(projected{[2..Length(projected)]},r->ForAll(r,x->x=0)) then Error("Later direction moves first parameter");fi;
   step:=Gcd(projected[1]);
   if AbsInt(step)<>AbsInt(e.parameter_step) then Error("First-parameter step changed");fi;
   N8LatticeCounts.changes:=N8LatticeCounts.changes+1;
   if AbsInt(step)>1 then N8LatticeCounts.nonunit:=N8LatticeCounts.nonunit+1;fi;
  fi;
 od;
end;
for row in N8GeneralFixtures do N8LatticeCase(row);od;
if N8LatticeCounts.fixed<>2 or N8LatticeCounts.nonunit<>1 then Error("Targeted branch coverage missing");fi;
Print("PASS N8 integer lattice branches ",N8LatticeCounts,"\n");
