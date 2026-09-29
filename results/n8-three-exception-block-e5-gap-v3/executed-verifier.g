# Independent NQ group and integral-lattice replay of the third-exception blocks.
# Adapted from the two-exception checker at ff5ff05; all new scopes checked below.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
if not IsBound(N8ThreeExceptionBlockFile) then Error("Set fixtures");fi;
N8ThreeExceptionBlock:=fail;;Read(N8ThreeExceptionBlockFile);;
(function()
 local item,Require,tvar,Poly,Mat,Eval,At,needed,strings,i,j,h,input,group,gens,hall,
       Element,Correct,VectorElement,base,target,known,found,comm0,central,
       lowrows,endrows,axes,side,s,A,rhs,H,U,K,J,change,r,last,pivot,
       changed,actual,col,z,point,cols,rows,small,checks,End,B,polynomial,
       q2,coeff,values,pair,comm,vec,endchecks,nielsen,high,first,colnum,Dword;
 item:=N8ThreeExceptionBlock;
 Require:=function(ok,msg)if not ok then Error(msg);fi;end;
 tvar:=Indeterminate(Rationals,"T");
 Poly:=function(data)
  if Length(data)=1 then return data[1][1]/data[1][2];fi;
  return Sum([1..Length(data)],i->data[i][1]/data[i][2]*tvar^(i-1));
 end;
 Mat:=data->List(data.entries,row->List(row,Poly));
 Eval:=function(p,t)if IsRat(p) then return p;fi;return Value(p,t);end;
 At:=function(A,t)return List(A,row->List(row,p->Eval(p,t)));end;
 Require(item.p=1 and item.q=item.weights[2]+6 and item.t=item.weights[2]-1
  and item.exceptions=[item.t,item.t+2,item.t+4] and
  item.class_bound=item.p+item.q+2*item.t,"Unsupported weight bounds");
 Require(item.block_exceptions=Filtered(item.exceptions,s->s<2*item.t),"Incomplete exception positions");
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
 group:=NilpotentQuotient(:input_string:=input,class:=item.class_bound);
 Require(HirschLength(group)=item.retained and ForAll(RelativeOrdersOfPcp(Pcp(group)),x->x=0),"Weighted group rank/torsion");
 Require(IsWeightedCollector(Collector(group)),"Collector must support nilpotent weights");
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
  and item.hall[i][1]<item.class_bound),i->i-1);
 endrows:=List(Filtered([1..item.retained],i->item.hall[i][1]=item.class_bound),i->i-1);
 Require(lowrows=item.low_rows and endrows=item.end_rows,"Incomplete output rows");
 axes:=[];
 for s in [item.t..2*item.t-1] do for side in [0,1] do
  for i in [1..item.retained] do
   if item.hall[i][1]=[item.p,item.q][side+1]+s then Add(axes,[side,i-1]);fi;
  od;
 od;od;
 Require(axes=item.block_axes,"Incomplete block axes");axes:=[];
 for side in [0,1] do for i in [1..item.retained] do
  if item.hall[i][1]=[item.p,item.q][side+1]+2*item.t then Add(axes,[side,i-1]);fi;
 od;od;
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
 Require(comm0^-1*target*VectorElement(lowrows,rhs)^-1 in central,"Block right side");
 for j in [1..Length(item.block_axes)] do
  z:=List([1..Length(item.block_axes)],k->0);z[j]:=1;
  changed:=Correct(base,item.block_axes,z);actual:=comm0^-1*Comm(changed[1],changed[2]);
  col:=List(A,row->row[j]);
  Require(actual*VectorElement(lowrows,col)^-1 in central,"Block column");
 od;
 for z in item.joint_vectors do
  changed:=Correct(base,item.block_axes,z);
  Require(comm0^-1*Comm(changed[1],changed[2])*VectorElement(lowrows,A*z)^-1 in central,"Joint block control");
 od;
 Print("Block columns and joint controls checked\n");
 H:=Mat(item.H);U:=Mat(item.U);K:=Mat(item.kernel);J:=Mat(item.J);change:=Mat(item.change);
 r:=RankMat(A);Require(Length(item.block_axes)-r=Length(item.block_exceptions),"Incomplete block rank");
 Require(H=U*TransposedMat(A) and ForAll(Concatenation(U),IsInt)
   and AbsInt(DeterminantMat(U))=1,"Integral Hermite identity");last:=0;
 for i in [1..Length(H)] do
  pivot:=PositionProperty(H[i],x->x<>0);
  if i<=r then Require(pivot<>fail and pivot>last and H[i][pivot]>0,"Hermite pivot");last:=pivot;
  else Require(pivot=fail,"Nonzero kernel row");fi;
 od;
 Require(K=TransposedMat(U{[r+1..Length(U)]}) and A*item.point=rhs,"Incomplete integral affine lattice");
 Require(ForAll(Concatenation(change),IsInt) and AbsInt(DeterminantMat(change))=1 and J=K*change,"Parameter lattice changed");
 Require(Length(item.first_rows)=Length(item.block_exceptions) and Length(item.steps)=Length(item.block_exceptions),"Missing lattice steps");
 for colnum in [1..Length(item.block_exceptions)] do
  first:=item.first_rows[colnum]+1;s:=item.block_exceptions[colnum];
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
  if s in item.block_exceptions then Require(Length(cols)-RankMat(small)=1,"Missing exception");
  else Require(Length(cols)=RankMat(small),"Unexpected intervening kernel");fi;
  checks:=checks+1;
 od;
 End:=Mat(item.Aend);B:=Mat(item.later_columns);polynomial:=Mat(item.polynomial);
 Require(Length(item.end_axes)-RankMat(End)=item.final_kernel_dimension and
  item.final_kernel_dimension=Number(item.exceptions,s->s=2*item.t),"Terminal exception/kernel mismatch");
 Require(ForAll(item.polynomial.entries,row->Length(row[1])<=3),"Polynomial degree exceeds proved bound");
 q2:=List((At(polynomial,2)-2*At(polynomial,1)+At(polynomial,0))/2,row->row[1]);
 Require(RankMat(List([1..Length(End)],i->Concatenation(End[i],[q2[i]])))=RankMat(End)+1,"Quadratic obstruction vanished");
 Require(RankMat(List([1..Length(End)],i->Concatenation(End[i],B[i])))-RankMat(End)=item.later_column_cokernel_rank,"Wrong later-column rank");
 for values in item.samples do
  point:=item.point+J*values;
  pair:=Correct(base,item.block_axes,point);comm:=Comm(pair[1],pair[2]);
  vec:=List(At(polynomial,values[1]),row->row[1])+B*values{[2..Length(values)]};
  Require(comm*VectorElement(endrows,vec)=target,"Quadratic group residual");
 od;
 Require(Length(item.samples)=Length(item.block_exceptions)+5,"Missing samples/controls");
 Print("Quadratic samples checked\n");
 endchecks:=0;
 for values in [List(item.block_exceptions,s->0),List(item.block_exceptions,s->1)] do
  point:=item.point+J*values;
  pair:=Correct(base,item.block_axes,point);comm:=Comm(pair[1],pair[2]);
  for j in [1..Length(item.end_axes)] do
   z:=List(item.end_axes,h->0);z[j]:=1;changed:=Correct(pair,item.end_axes,z);
   Require(comm*VectorElement(endrows,List(End,row->row[j]))=Comm(changed[1],changed[2]),"Terminal correction column");
   endchecks:=endchecks+1;
  od;
 od;
 Require(Mat(item.families.A)=List([1..Length(End)],i->Concatenation(End[i],-B[i])) and
   Mat(item.families.b)=polynomial,"Polynomial-family input mismatch");
 values:=item.witness;point:=item.point+J*values.parameters;
 pair:=Correct(Correct(base,item.block_axes,point),item.end_axes,values.corrections);
 Require(pair=found,"Arithmetic witness reconstruction");
 Print("PASS N8 three-exception block GAP: class ",item.class_bound,"; ",Length(item.block_axes),
  " block columns; ",endchecks," terminal columns; ",Length(item.samples)," quadratic samples; ",checks,
  " complete block kernels; full integer lattice rank ",Length(item.block_exceptions),"; terminal kernel ",item.final_kernel_dimension,"; 2 group witnesses\n");
end)();
QUIT_GAP(0);
