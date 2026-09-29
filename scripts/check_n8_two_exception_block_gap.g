# Independent NQ group and integral-lattice replay of the two-exception block.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
if not IsBound(N8TwoExceptionBlockFile) then Error("Set fixtures");fi;
N8TwoExceptionBlock:=fail;;Read(N8TwoExceptionBlockFile);;
(function()
 local item,Require,tvar,Poly,Mat,Eval,At,needed,strings,i,j,h,input,group,gens,hall,
       Element,Correct,VectorElement,base,target,known,found,comm0,central,
       lowrows,endrows,axes,side,s,A,rhs,H,U,K,J,change,r,last,pivot,
       changed,actual,col,z,point,cols,rows,small,checks,End,B,polynomial,
       q2,coeff,values,pair,comm,vec,endchecks,nielsen,high,first;
 item:=N8TwoExceptionBlock;
 Require:=function(ok,msg)if not ok then Error(msg);fi;end;
 tvar:=Indeterminate(Rationals,"T");
 Poly:=function(data)
  if Length(data)=1 then return data[1][1]/data[1][2];fi;
  return Sum([1..Length(data)],i->data[i][1]/data[i][2]*tvar^(i-1));
 end;
 Mat:=data->List(data.entries,row->List(row,Poly));
 Eval:=function(p,t)if IsRat(p) then return p;fi;return Value(p,t);end;
 At:=function(A,t)return List(A,row->List(row,p->Eval(p,t)));end;
 Require(item.p=1 and item.q=item.weights[2]+4 and item.t=item.weights[2]-1
  and item.later=item.t+2 and item.later<2*item.t and
  item.class_bound=item.p+item.q+2*item.t,"Unsupported weight bounds");
 needed:=Union([1..item.retained],List(item.boundaries,i->i+1));strings:=[];
 Require(ForAll(item.boundaries,i->ForAll(item.hall[i+1][2],j->j<item.retained)),"Omitted boundary parent");
 for i in [1..Length(item.hall)] do
  h:=item.hall[i];
  if not i in needed then Add(strings,"");
  elif IsEmpty(h[2]) then Add(strings,["a","b"][i]);
  else Add(strings,Concatenation("[",strings[h[2][1]+1],",",strings[h[2][2]+1],"]"));fi;
 od;
 input:=Concatenation("< a,b | ",JoinStringsWithSeparator(List(item.boundaries,i->strings[i+1]),", ")," >\n");
 group:=NilpotentQuotient(:input_string:=input,class:=item.class_bound);
 Require(HirschLength(group)=item.retained and Size(TorsionSubgroup(group))=1,"Weighted group rank/torsion");
 gens:=GeneratorsOfGroup(group){[1..2]};hall:=[];
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
 known:=List(item.known_pair,Element);found:=List(item.found_pair,Element);
 Require(Comm(known[1],known[2])=target and Comm(found[1],found[2])=target,"Group witnesses");
 comm0:=Comm(base[1],base[2]);central:=Subgroup(group,List(endrows,i->hall[i+1]));
 A:=Mat(item.A);rhs:=List(Mat(item.rhs),row->row[1]);
 Require(comm0^-1*target*VectorElement(lowrows,rhs)^-1 in central,"Block right side");
 for j in [1..Length(item.block_axes)] do
  z:=List([1..Length(item.block_axes)],k->0);z[j]:=1;
  changed:=Correct(base,item.block_axes,z);actual:=comm0^-1*Comm(changed[1],changed[2]);
  col:=List(A,row->row[j]);
  Require(actual*VectorElement(lowrows,col)^-1 in central,"Block column");
 od;
 H:=Mat(item.H);U:=Mat(item.U);K:=Mat(item.kernel);J:=Mat(item.J);change:=Mat(item.change);
 r:=RankMat(A);Require(Length(item.block_axes)-r=2,"Block not two-dimensional");
 Require(H=U*TransposedMat(A) and ForAll(Concatenation(U),IsInt)
   and AbsInt(DeterminantMat(U))=1,"Integral Hermite identity");last:=0;
 for i in [1..Length(H)] do
  pivot:=PositionProperty(H[i],x->x<>0);
  if i<=r then Require(pivot<>fail and pivot>last and H[i][pivot]>0,"Hermite pivot");last:=pivot;
  else Require(pivot=fail,"Nonzero kernel row");fi;
 od;
 Require(K=TransposedMat(U{[r+1..Length(U)]}) and A*item.point=rhs,"Incomplete integral affine lattice");
 Require(ForAll(Concatenation(change),IsInt) and AbsInt(DeterminantMat(change))=1 and J=K*change,"Parameter lattice changed");
 first:=item.first_axis+1;
 Require(J[first][1]=item.parameter_step and J[first][1]<>0 and J[first][2]=0,"First parameter step");
 Require(ForAll([1..Length(J)],j->item.hall[item.block_axes[j][2]+1][1]>=[item.p,item.q][item.block_axes[j][1]+1]+item.later or J[j][2]=0),"Second parameter starts too early");
 checks:=0;
 for s in [item.t..2*item.t-1] do
  rows:=Filtered([1..Length(lowrows)],i->item.hall[lowrows[i]+1][1]=item.p+item.q+s);
  cols:=Filtered([1..Length(item.block_axes)],j->item.hall[item.block_axes[j][2]+1][1]=[item.p,item.q][item.block_axes[j][1]+1]+s);
  small:=List(rows,i->A[i]{cols});
  if s in [item.t,item.later] then Require(Length(cols)-RankMat(small)=1,"Missing exception");
  else Require(Length(cols)=RankMat(small),"Unexpected intervening kernel");fi;
  checks:=checks+1;
 od;
 End:=Mat(item.Aend);B:=List(Mat(item.B),row->row[1]);polynomial:=Mat(item.polynomial);
 Require(ForAll(item.polynomial.entries,row->Length(row[1])<=3),"Polynomial degree exceeds proved bound");
 q2:=List((At(polynomial,2)-2*At(polynomial,1)+At(polynomial,0))/2,row->row[1]);
 Require(RankMat(List([1..Length(End)],i->Concatenation(End[i],[q2[i]])))=RankMat(End)+1,"Quadratic obstruction vanished");
 Require((RankMat(List([1..Length(End)],i->Concatenation(End[i],[B[i]])))>RankMat(End))=item.obstruction_B_nonzero_mod_image,"Wrong second coefficient status");
 for values in item.samples do
  point:=item.point+List(J,row->values[1]*row[1]+values[2]*row[2]);
  pair:=Correct(base,item.block_axes,point);comm:=Comm(pair[1],pair[2]);
  vec:=List(At(polynomial,values[1]),row->row[1])+values[2]*B;
  Require(comm*VectorElement(endrows,vec)=target,"Quadratic group residual");
 od;
 Require(item.samples=[[0,0],[1,0],[2,0],[0,1],[1,1],[-2,3]],"Missing samples/controls");
 endchecks:=0;
 for values in [[0,0],[1,1]] do
  point:=item.point+List(J,row->values[1]*row[1]+values[2]*row[2]);
  pair:=Correct(base,item.block_axes,point);comm:=Comm(pair[1],pair[2]);
  for j in [1..Length(item.end_axes)] do
   z:=List(item.end_axes,h->0);z[j]:=1;changed:=Correct(pair,item.end_axes,z);
   Require(comm*VectorElement(endrows,List(End,row->row[j]))=Comm(changed[1],changed[2]),"Terminal correction column");
   endchecks:=endchecks+1;
  od;
 od;
 Require(Mat(item.families.A)=List([1..Length(End)],i->Concatenation(End[i],[-B[i]])) and
   Mat(item.families.b)=polynomial,"Polynomial-family input mismatch");
 values:=item.witness;point:=item.point+List(J,row->values.t*row[1]+values.s*row[2]);
 pair:=Correct(Correct(base,item.block_axes,point),item.end_axes,values.corrections);
 Require(pair=found,"Arithmetic witness reconstruction");
 nielsen:=item.nielsen;
 if nielsen<>fail then
  Require(2*item.t=item.q-item.p and Length(item.end_axes)-RankMat(End)=1,"Nielsen rank");
  Require(ForAll(End,row->row[nielsen.axis+1]=0) and item.end_axes[nielsen.axis+1]=[0,nielsen.hall_index],"Primitive Nielsen direction");
  Require(nielsen.period=3 and nielsen.residues=[0,1,2] and nielsen.powers=[-2,-1,1,2],"Incomplete Nielsen residues");
  high:=Subgroup(group,List(Filtered([1..item.retained],i->item.hall[i][1]>item.q),i->hall[i]));
  Require(base[1]^-1*base[2]*base[1]*hall[nielsen.hall_index+1]^-nielsen.period in high,"Nielsen leading period");
  for i in nielsen.powers do
   Require(Comm(base[2]^i*base[1],base[2])=comm0,"Exact Nielsen substitution");
  od;
 else Require(Length(item.end_axes)=RankMat(End),"Terminal kernel not injective");fi;
 Print("PASS N8 two-exception block GAP: class ",item.class_bound,"; ",Length(item.block_axes),
  " block columns; ",endchecks," terminal columns; 6 quadratic samples; ",checks,
  " complete block kernels; full two-parameter integer lattice; 2 group witnesses; Nielsen ",nielsen<>fail,"\n");
end)();
QUIT_GAP(0);
