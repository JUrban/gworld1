# Independent native group replay by complete degree-two coefficient reconstruction.
# Derived from the direct class26 verifier; avoids large-exponent sample collection.
# Adapted from the third-exception checker from this work period.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
# Polycyclic disables combinatorial collection by a process-global default.
# Enable it before constructing the collector; its weight test still runs.
MakeReadWriteGlobal("USE_COMBINATORIAL_COLLECTOR");;
USE_COMBINATORIAL_COLLECTOR:=true;;
MakeReadOnlyGlobal("USE_COMBINATORIAL_COLLECTOR");;
if not IsBound(N8DelayedQuadraticFile) then Error("Set fixtures");fi;
N8DelayedQuadratic:=fail;;Read(N8DelayedQuadraticFile);;
(function()
 local item,Require,tvar,Poly,Mat,Eval,At,needed,strings,i,j,h,input,group,gens,hall,
       Element,Correct,VectorElement,base,target,known,found,comm0,central,
       lowrows,endrows,axes,side,s,A,rhs,H,U,K,J,change,r,last,pivot,
       changed,actual,col,z,point,cols,rows,small,checks,End,B,polynomial,
       q2,coeff,values,pair,comm,vec,endchecks,nielsen,high,first,colnum,Dword,tailpcp,allrows,Coords,linearPC,endPC,targetPC,quadratics,
       wi,wj,other,unitpair,unitvec,deltaPC,polyPC,term,quadraticCount;
 item:=N8DelayedQuadratic;
 Require:=function(ok,msg)if not ok then Error(msg);fi;end;
 tvar:=Indeterminate(Rationals,"T");
 Poly:=function(data)
  if Length(data)=1 then return data[1][1]/data[1][2];fi;
  return Sum([1..Length(data)],i->data[i][1]/data[i][2]*tvar^(i-1));
 end;
 Mat:=data->List(data.entries,row->List(row,Poly));
 Eval:=function(p,t)if IsRat(p) then return p;fi;return Value(p,t);end;
 At:=function(A,t)return List(A,row->List(row,p->Eval(p,t)));end;
 Require(item.p=1 and item.q=10 and item.t=7 and item.weights=[1,4] and item.class_bound=26,"Unsupported delayed setup");
 Require(item.exceptions=[7] and item.block_kernel_offsets=[7,9,11,13] and item.universal_offsets=[9,11,13],"Incomplete kernel positions");
 Require(3*item.t>item.class_bound-item.p-item.q and item.t+9>item.class_bound-item.p-item.q,"Uncontrolled parameter interactions");
 needed:=Union([1..item.retained],List(item.boundaries,i->i+1));strings:=[];
 Require(ForAll(item.boundaries,i->ForAll(item.hall[i+1][2],j->j<item.retained)),"Omitted boundary parent");
 for i in [1..Length(item.hall)] do
  h:=item.hall[i];
  if not i in needed then Add(strings,"");
  elif IsEmpty(h[2]) then Add(strings,["a","b"][i]);
  else Add(strings,Concatenation("[",strings[h[2][1]+1],",",strings[h[2][2]+1],"]"));fi;
 od;
 input:=Concatenation("< b,a | ",JoinStringsWithSeparator(List(item.boundaries,i->strings[i+1]),", ")," >\n");
 Print("Prepared compact block quotient\n");
 if IsBound(N8PreparedGroup) then
  Require(IsBound(N8PreparedInput) and N8PreparedInput=input,"Cached presentation differs");
  group:=N8PreparedGroup;
 else
  group:=NilpotentQuotient(:input_string:=input,class:=item.class_bound);
 fi;
 Require(HirschLength(group)=item.retained and ForAll(RelativeOrdersOfPcp(Pcp(group)),x->x=0),"Weighted group rank/torsion");
 Require(IsWeightedCollector(Collector(group)),"Collector must support nilpotent weights");
 if not IsBound(N8UseHallPolynomials) or N8UseHallPolynomials then
  Print("Computing native Hall multiplication polynomials\n");
  AddHallPolynomials(Collector(group));
 else
  Print("Using native combinatorial collector without multiplication polynomials\n");
 fi;
 Print("Block quotient ready, Hirsch length ",item.retained,"\n");
 gens:=GeneratorsOfGroup(group){[2,1]};hall:=[];
 for i in [1..Length(item.hall)] do
  h:=item.hall[i];
  if not i in needed then Add(hall,One(group));
  elif IsEmpty(h[2]) then Add(hall,gens[i]);
  else Add(hall,Comm(hall[h[2][1]+1],hall[h[2][2]+1]));fi;
 od;
 Require(ForAll(item.boundaries,i->hall[i+1]=One(group)),"Boundary relation");
 Element:=function(terms)
  local result,h;result:=One(group);
  for h in terms do result:=result*hall[h[1]+1]^h[2];od;return result;
 end;
 Correct:=function(pair,axes,vec)
  local result,j;result:=ShallowCopy(pair);
  Require(Length(axes)=Length(vec) and ForAll(vec,IsInt),"Correction dimensions/integrality");
  for j in [1..Length(axes)] do
   result[axes[j][1]+1]:=result[axes[j][1]+1]*hall[axes[j][2]+1]^vec[j];
  od;return result;
 end;
 VectorElement:=function(rows,vec)
  local result,j;result:=One(group);
  Require(Length(rows)=Length(vec) and ForAll(vec,IsInt),"Coordinate vector");
  for j in [1..Length(rows)] do result:=result*hall[rows[j]+1]^vec[j];od;return result;
 end;
 lowrows:=List(Filtered([1..item.retained],i->item.p+item.q+item.t<=item.hall[i][1]
  and item.hall[i][1]<item.p+item.q+2*item.t),i->i-1);
 endrows:=List(Filtered([1..item.retained],i->item.hall[i][1]>=item.p+item.q+2*item.t),i->i-1);
 Require(lowrows=item.low_rows and endrows=item.end_rows,"Incomplete output rows");
 axes:=[];
 for s in [item.t..2*item.t-1] do for side in [0,1] do
  for i in [1..item.retained] do
   if item.hall[i][1]=[item.p,item.q][side+1]+s then Add(axes,[side,i-1]);fi;
  od;
 od;od;
 Require(axes=item.block_axes,"Incomplete block axes");axes:=[];
 for s in [2*item.t..item.class_bound-item.p-item.q] do
  for side in [0,1] do for i in [1..item.retained] do
   if item.hall[i][1]=[item.p,item.q][side+1]+s then Add(axes,[side,i-1]);fi;
  od;od;
 od;
 Require(axes=item.end_axes,"Incomplete terminal axes");
 base:=List(item.base,Element);target:=Element(item.target);
 Dword:=gens[2];for i in [1..6] do Dword:=Comm(Dword,gens[1]);od;
 Require(base=[gens[1]^2,Dword^3],"Incorrect base group words/scales");
 Print("Base and target reconstructed\n");
 known:=List(item.known_pair,Element);found:=List(item.found_pair,Element);
 Print("Both witness pairs reconstructed\n");
 Require(Comm(known[1],known[2])=target and Comm(found[1],found[2])=target,"Group witnesses");
 Print("Group witnesses checked\n");
 comm0:=Comm(base[1],base[2]);central:=Subgroup(group,List(endrows,i->hall[i+1]));
 A:=Mat(item.A);rhs:=List(Mat(item.rhs),row->row[1]);
 allrows:=Concatenation(lowrows,endrows);
 # These errors have weight at least18, so this whole tail is abelian
 # in class26. Its native integral Pcp coordinates are additive.
 tailpcp:=Pcp(Subgroup(group,List(allrows,i->hall[i+1])));
 Require(Length(tailpcp)=Length(allrows),"Incomplete abelian-tail basis");
 Coords:=x->ExponentsByPcp(tailpcp,x);
 targetPC:=Coords(comm0^-1*target);linearPC:=[];
 endPC:=List(endrows,i->Coords(hall[i+1]));
 Print("Native additive tail coordinates ready\n");
 Require(comm0^-1*target*VectorElement(lowrows,rhs)^-1 in central,"Block right side");
 for j in [1..Length(item.block_axes)] do
  z:=List([1..Length(item.block_axes)],k->0);z[j]:=1;
  changed:=Correct(base,item.block_axes,z);actual:=comm0^-1*Comm(changed[1],changed[2]);
  Add(linearPC,Coords(actual));col:=List(A,row->row[j]);
  Require(actual*VectorElement(lowrows,col)^-1 in central,"Block column");
 od;
 for z in item.joint_vectors do
  changed:=Correct(base,item.block_axes,z);
  Require(comm0^-1*Comm(changed[1],changed[2])*VectorElement(lowrows,A*z)^-1 in central,"Joint block control");
 od;
 Print("Block columns and joint controls checked\n");
 H:=Mat(item.H);U:=Mat(item.U);K:=Mat(item.kernel);J:=Mat(item.J);change:=Mat(item.change);
 r:=RankMat(A);Require(Length(item.block_axes)-r=Length(item.block_kernel_offsets),"Incomplete block rank");
 Require(H=U*TransposedMat(A) and ForAll(Concatenation(U),IsInt)
   and AbsInt(DeterminantMat(U))=1,"Integral Hermite identity");last:=0;
 for i in [1..Length(H)] do
  pivot:=PositionProperty(H[i],x->x<>0);
  if i<=r then Require(pivot<>fail and pivot>last and H[i][pivot]>0,"Hermite pivot");last:=pivot;
  else Require(pivot=fail,"Nonzero kernel row");fi;
 od;
 Require(K=TransposedMat(U{[r+1..Length(U)]}) and A*item.point=rhs,"Incomplete integral affine lattice");
 Require(ForAll(Concatenation(change),IsInt) and AbsInt(DeterminantMat(change))=1 and J=K*change,"Parameter lattice changed");
 Require(Length(item.first_rows)=Length(item.block_kernel_offsets) and Length(item.steps)=Length(item.block_kernel_offsets),"Missing lattice steps");
 for colnum in [1..Length(item.block_kernel_offsets)] do
  first:=item.first_rows[colnum]+1;s:=item.block_kernel_offsets[colnum];
  Require(item.block_axes[first][1]=0 and item.hall[item.block_axes[first][2]+1][1]=item.p+s,"Wrong first coordinate");
  Require(J[first][colnum]=item.steps[colnum] and item.steps[colnum]>0 and
   ForAll([colnum+1..Length(item.steps)],k->J[first][k]=0),"Lattice step lost");
  Require(ForAll([1..Length(J)],j->item.hall[item.block_axes[j][2]+1][1]>=[item.p,item.q][item.block_axes[j][1]+1]+s or J[j][colnum]=0),"Direction begins too early");
 od;
 Print("Complete block lattice checked\n");
 checks:=0;
 for s in [item.t..2*item.t-1] do
  rows:=Filtered([1..Length(lowrows)],i->item.hall[lowrows[i]+1][1]=item.p+item.q+s);
  cols:=Filtered([1..Length(item.block_axes)],j->item.hall[item.block_axes[j][2]+1][1]=[item.p,item.q][item.block_axes[j][1]+1]+s);
  small:=List(rows,i->A[i]{cols});
  if s in item.block_kernel_offsets then Require(Length(cols)-RankMat(small)=1,"Missing exception");
  else Require(Length(cols)=RankMat(small),"Unexpected intervening kernel");fi;
  checks:=checks+1;
 od;
 End:=Mat(item.Aend);B:=Mat(item.later_columns);polynomial:=Mat(item.polynomial);
 Require(Length(item.end_axes)-RankMat(End)=item.final_kernel_dimension and
  item.final_kernel_dimension=1,"Missing later universal kernel");
 for s in [14,15] do
  rows:=Filtered([1..Length(endrows)],i->item.hall[endrows[i]+1][1]=item.p+item.q+s);
  cols:=Filtered([1..Length(item.end_axes)],j->item.hall[item.end_axes[j][2]+1][1]=[item.p,item.q][item.end_axes[j][1]+1]+s);
  small:=List(rows,i->End[i]{cols});
  Require(Length(cols)-RankMat(small)=Number([15],k->k=s),"Terminal homogeneous kernel mismatch");
 od;
 Require(ForAll(item.polynomial.entries,row->Length(row[1])<=3),"Polynomial degree exceeds proved bound");
 q2:=List((At(polynomial,2)-2*At(polynomial,1)+At(polynomial,0))/2,row->row[1]);
 Require(RankMat(List([1..Length(End)],i->Concatenation(End[i],[q2[i]])))=RankMat(End)+1,"Quadratic obstruction vanished");
 Require(RankMat(List([1..Length(End)],i->Concatenation(End[i],B[i])))-RankMat(End)=item.later_column_cokernel_rank,"Wrong later-column rank");
 # Every commutator term involving three correction occurrences is
 # beyond26: minima are34 (three first-input occurrences),33 (two
 # first and one second),42 (one first and two second),52 (three second).
 # Ordered powers contribute binomial(z_i,2) on a single coordinate.
 Require(3*(item.p+item.t)+item.q>26 and
  2*(item.p+item.t)+item.q+item.t>26 and
  item.p+item.t+2*(item.q+item.t)>26 and
  3*(item.q+item.t)+item.p>26,"Missing cubic coefficient");
 quadratics:=[];quadraticCount:=0;
 for i in [1..Length(item.block_axes)] do
  wi:=item.hall[item.block_axes[i][2]+1][1];
  other:=[item.q,item.p][item.block_axes[i][1]+1];
  if 2*wi+other<=26 then
   unitvec:=List(item.block_axes,x->0);unitvec[i]:=2;
   unitpair:=Correct(base,item.block_axes,unitvec);
   deltaPC:=Coords(comm0^-1*Comm(unitpair[1],unitpair[2]))-2*linearPC[i];
   Add(quadratics,[i,i,deltaPC]);quadraticCount:=quadraticCount+1;
  fi;
  for j in [i+1..Length(item.block_axes)] do
   wj:=item.hall[item.block_axes[j][2]+1][1];
   if (item.block_axes[i][1]<>item.block_axes[j][1] and wi+wj<=26) or
      (item.block_axes[i][1]=item.block_axes[j][1] and wi+wj+other<=26) then
    unitvec:=List(item.block_axes,x->0);unitvec[i]:=1;unitvec[j]:=1;
    unitpair:=Correct(base,item.block_axes,unitvec);
    deltaPC:=Coords(comm0^-1*Comm(unitpair[1],unitpair[2]))-linearPC[i]-linearPC[j];
    Add(quadratics,[i,j,deltaPC]);quadraticCount:=quadraticCount+1;
   fi;
  od;
 od;
 Print("All ",quadraticCount," possible native quadratic coefficients reconstructed\n");
 for values in item.samples do
  point:=item.point+J*values;polyPC:=point*linearPC;
  for term in quadratics do
   if term[1]=term[2] then
    polyPC:=polyPC+Binomial(point[term[1]],2)*term[3];
   else polyPC:=polyPC+point[term[1]]*point[term[2]]*term[3];fi;
  od;
  vec:=List(At(polynomial,values[1]),row->row[1])+B*values{[2..Length(values)]};
  Require(targetPC-polyPC=vec*endPC,"Complete native polynomial residual");
 od;
 Require(Length(item.samples)=Length(item.block_kernel_offsets)+5,"Missing samples/controls");
 Print("Quadratic samples checked\n");
 # Terminal offsets14/15 have no possible quadratic interaction with
 # block offsets>=7 through target offset15. A unit check at the base
 # therefore verifies the same column for every block parameter value.
 endchecks:=0;
 for j in [1..Length(item.end_axes)] do
  z:=List(item.end_axes,h->0);z[j]:=1;changed:=Correct(base,item.end_axes,z);
  Require(Coords(comm0^-1*Comm(changed[1],changed[2]))=
   List(End,row->row[j])*endPC,"Complete terminal correction column");
  endchecks:=endchecks+1;
 od;
 Require(Mat(item.families.A)=List([1..Length(End)],i->Concatenation(End[i],-B[i])) and
   Mat(item.families.b)=polynomial,"Polynomial-family input mismatch");
 values:=item.witness;point:=item.point+J*values.parameters;
 pair:=Correct(Correct(base,item.block_axes,point),item.end_axes,values.corrections);
 Require(pair=found,"Arithmetic witness reconstruction");
 Print("PASS N8 delayed quadratic polynomial GAP: class ",item.class_bound,"; ",Length(item.block_axes),
  " block columns; ",endchecks," terminal columns; ",Length(item.samples)," polynomial evaluations; ",quadraticCount," complete quadratic coefficients; ",checks,
  " complete block kernels; full integer lattice rank ",Length(item.block_kernel_offsets),"; terminal kernel ",item.final_kernel_dimension,"; 2 group witnesses\n");
end)();
QUIT_GAP(0);
