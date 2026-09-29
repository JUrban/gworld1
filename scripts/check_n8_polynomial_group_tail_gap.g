# Independent NQ replay of a nonlinear polynomial family and its full tail.
# The fixture is not claimed to be a surviving absorbed-quadratic branch.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
if not IsBound(N8PolynomialGroupTailFile) then Error("Set fixture path");fi;
N8PolynomialGroupTail:=fail;;Read(N8PolynomialGroupTailFile);;
(function()
 local item,Require,started,Stage,tvar,Poly,Mat,Eval,At,Coefs,IRoots,
       needed,strings,i,j,h,input,group,gens,hall,Element,Correct,
       VectorElement,Family,base,target,known,found,axes,side,s,
       algebra,letters,Bracket,liehall,C,D,columns,dim,layer,rho,
       P,b,value,pair,comm,mat,rhs,col,actual,correction,changed,
       hh,kk,vec,columnchecks,jointchecks,directchecks,kernelchecks,
       critical,candidates,decision,A,bb,solution,H,U,K,r,last,pivot,
       accepted,fullkernels,degree;
 item:=N8PolynomialGroupTail;
 Require:=function(ok,msg)if not ok then Error(msg);fi;end;
 started:=Runtime();Stage:=function(s)Print(s," at ",Runtime()-started," ms\n");end;
 tvar:=Indeterminate(Rationals,"T");
 Poly:=function(data)
  if Length(data)=1 then return data[1][1]/data[1][2];fi;
  return Sum([1..Length(data)],i->data[i][1]/data[i][2]*tvar^(i-1));
 end;
 Mat:=data->List(data.entries,row->List(row,Poly));
 Eval:=function(p,t)if IsRat(p) then return p;fi;return Value(p,t);end;
 At:=function(A,t)return List(A,row->List(row,p->Eval(p,t)));end;
 Coefs:=function(p)if IsRat(p) then return [p];fi;return CoefficientsOfUnivariatePolynomial(p);end;
 IRoots:=function(p)
  local result,f,cs;result:=[];
  Require(not IsZero(p),"Root polynomial zero");
  if Length(Coefs(p))<=1 then return result;fi;
  for f in Factors(p) do
   cs:=Coefs(f);
   if Length(cs)=2 and IsInt(-cs[1]/cs[2]) then AddSet(result,-cs[1]/cs[2]);fi;
  od;return result;
 end;
 Require(item.weights=[1,4] and item.p=1 and item.q=10 and item.t=3
  and item.tail_offset=7,"Unsupported fixture setup");
 Require(2*item.tail_offset>item.class_bound-item.p-item.q,"Tail variables may interact");
 Require(2*(item.p+item.q+item.t)>item.class_bound,"Comparison tail not abelian");
 needed:=Union([1..item.retained],List(item.boundaries,i->i+1));strings:=[];
 Require(ForAll(item.boundaries,i->ForAll(item.hall[i+1][2],j->j<item.retained)),"Omitted boundary parent");
 for i in [1..Length(item.hall)] do
  h:=item.hall[i];
  if not i in needed then Add(strings,"");
  elif IsEmpty(h[2]) then Add(strings,["a","b"][i]);
  else Add(strings,Concatenation("[",strings[h[2][1]+1],",",strings[h[2][2]+1],"]"));fi;
 od;
 # Declare the heavier generator first. This only changes NQ's internal
 # elimination order; the Hall words and all mathematical data are fixed.
 input:=Concatenation("< b,a | ",JoinStringsWithSeparator(List(item.boundaries,i->strings[i+1]),", ")," >\n");
 Stage("Weighted presentation prepared (heavier generator first)");
 group:=NilpotentQuotient(:input_string:=input,class:=item.class_bound);
 Require(HirschLength(group)=item.retained and Size(TorsionSubgroup(group))=1,"Weighted group rank/torsion");
 gens:=GeneratorsOfGroup(group){[2,1]};hall:=[];
 for i in [1..Length(item.hall)] do
  h:=item.hall[i];
  if not i in needed then Add(hall,One(group));
  elif IsEmpty(h[2]) then Add(hall,gens[i]);
  else Add(hall,Comm(hall[h[2][1]+1],hall[h[2][2]+1]));fi;
 od;
 Require(ForAll(item.boundaries,i->hall[i+1]=One(group)),"Boundary relation");
 Stage("Native weighted quotient constructed");
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
 VectorElement:=function(vec)
  local result,j;result:=One(group);
  Require(Length(item.rows)=Length(vec) and ForAll(vec,IsInt),"Coordinate vector");
  for j in [1..Length(vec)] do result:=result*hall[item.rows[j]+1]^vec[j];od;return result;
 end;
 base:=List(item.base,Element);target:=Element(item.target);
 known:=List(item.known_pair,Element);found:=List(item.found_pair,Element);
 # The Hall lift is [b,a,a,a,a,a,a]. Its Lie leading term agrees
 # with ad_a^6(b), but the two nested group words differ above it.
 h:=gens[2];for i in [1..6] do h:=Comm(h,gens[1]);od;
 Require(base=[gens[1]^2,h^3],"Base family changed");
 Family:=function(t)
  local pair,layer,e;pair:=base;
  for layer in item.family_layers do
   e:=Eval(Poly(layer.exponent),t);
   pair:=Correct(pair,layer.axes,e*layer.kernel);
  od;return pair;
 end;
 Require(Comm(known[1],known[2])=target and Comm(found[1],found[2])=target,"Group witnesses");
 Stage("Known and computed group witnesses checked");
 axes:=[];
 for side in [0,1] do for i in [1..item.retained] do
  if [item.p,item.q][side+1]+item.tail_offset<=item.hall[i][1] and
   item.hall[i][1]<=item.class_bound-[item.q,item.p][side+1] then Add(axes,[side,i-1]);fi;
 od;od;
 Require(axes=item.tail_axes,"Incomplete tail variables");
 Require(item.rows=List(Filtered([1..item.retained],i->item.hall[i][1]>=item.p+item.q+item.t),i->i-1),"Incomplete output rows");
 Require(Correct(Family(2),item.tail_axes,item.joint_vectors[1])=known,"Planted target reconstruction");
 algebra:=FreeAssociativeAlgebraWithOne(Rationals,2,"a");letters:=GeneratorsOfAlgebraWithOne(algebra);
 Bracket:=function(a,b)return a*b-b*a;end;liehall:=[];
 for h in item.hall do
  if h[1]>item.q+7 then Add(liehall,Zero(algebra));
  elif IsEmpty(h[2]) then Add(liehall,letters[Length(liehall)+1]);
  else Add(liehall,Bracket(liehall[h[2][1]+1],liehall[h[2][2]+1]));fi;
 od;
 C:=2*letters[1];D:=letters[2];for i in [1..6] do D:=Bracket(letters[1],D);od;D:=3*D;
 Require(List(item.family_layers,l->l.offset)=[3,5],"Wrong family layers");
 Require(List(item.family_layers,l->Poly(l.exponent))=[tvar,tvar^2],"Wrong exponent polynomials");
 kernelchecks:=0;rho:=0;
 for s in [3,5,7] do
  axes:=[];
  for side in [0,1] do for i in [1..item.retained] do
   if item.hall[i][1]=[item.p,item.q][side+1]+s then Add(axes,[side,i-1]);fi;
  od;od;
  columns:=[];
  for h in axes do
   if h[1]=0 then Add(columns,Bracket(liehall[h[2]+1],D));
   else Add(columns,Bracket(C,liehall[h[2]+1]));fi;
  od;
  dim:=Dimension(VectorSpace(Rationals,Filtered(columns,x->not IsZero(x))));
  Require(Length(columns)-dim=1,"Exceptional kernel dimension");
  if s in [3,5] then
   layer:=First(item.family_layers,l->l.offset=s);
   Require(layer.axes=axes and Length(layer.kernel)=Length(axes) and Gcd(layer.kernel)=1,"Incomplete or nonprimitive kernel");
   Require(IsZero(Sum([1..Length(columns)],j->layer.kernel[j]*columns[j])),"Kernel identity");
   degree:=Length(layer.exponent)-1;
   for j in [1..Length(axes)] do
    if layer.kernel[j]<>0 then rho:=Maximum(rho,degree/item.hall[axes[j][2]+1][1]);fi;
   od;
  fi;kernelchecks:=kernelchecks+1;
 od;
 Require(rho=item.rho[1]/item.rho[2],"Parameter weight bound");
 Require(item.degree_bound=Int(item.class_bound*rho) and
  item.sample_values=[0..item.degree_bound],"Interpolation bound/samples");
 for mat in [item.P,item.b] do
  Require(ForAll(Concatenation(mat.entries),x->Length(x)<=item.degree_bound+1),"Polynomial exceeds bound");
 od;
 P:=Mat(item.P);b:=Mat(item.b);
 Require(Length(P)=Length(item.rows) and ForAll(P,row->Length(row)=Length(item.tail_axes))
  and Length(b)=Length(item.rows) and ForAll(b,row->Length(row)=1),"Polynomial dimensions");
 Stage("Complete kernels and degree bound checked");
 columnchecks:=0;jointchecks:=0;directchecks:=0;
 for value in item.sample_values do
  pair:=Family(value);comm:=Comm(pair[1],pair[2]);mat:=At(P,value);rhs:=List(At(b,value),row->row[1]);
  Require(comm*VectorElement(rhs)=target,"Polynomial target residual");
  for j in [1..Length(item.tail_axes)] do
   h:=item.tail_axes[j];correction:=hall[h[2]+1];
   # Exact group identities, independent of the tensor constructor.
   if h[1]=0 then actual:=comm^correction*Comm(correction,pair[2]);
   else actual:=Comm(pair[1],correction)*comm^correction;fi;
   col:=List(mat,row->row[j]);Require(comm*VectorElement(col)=actual,"Polynomial column");
   if value=0 and j in [1,Length(item.tail_axes)] then
    changed:=ShallowCopy(pair);changed[h[1]+1]:=changed[h[1]+1]*correction;
    Require(actual=Comm(changed[1],changed[2]),"Direct identity control");directchecks:=directchecks+1;
   fi;columnchecks:=columnchecks+1;
  od;
  for vec in item.joint_vectors do
   changed:=Correct([One(group),One(group)],item.tail_axes,vec);hh:=changed[1];kk:=changed[2];
   actual:=Comm(pair[1],kk)^hh*Comm(hh,kk)*(comm^hh*Comm(hh,pair[2]))^kk;
   Require(comm*VectorElement(mat*vec)=actual,"Joint linearity control");jointchecks:=jointchecks+1;
  od;
  Stage(Concatenation("Polynomial group sample ",String(value)," checked"));
 od;
 critical:=item.critical_row+1;
 Require(ForAll(P[critical],IsZero) and not IsZero(b[critical][1]),"Invalid zero-row obstruction");
 candidates:=IRoots(b[critical][1]);
 Require(candidates=item.integer_candidates and List(item.decisions,x->x.t)=candidates,"Incomplete integer candidates");
 accepted:=[];fullkernels:=0;
 for decision in item.decisions do
  A:=At(P,decision.t);bb:=List(At(b,decision.t),row->row[1]);
  Require(ForAll(Concatenation(A),IsInt) and ForAll(bb,IsInt),"Nonintegral specialization");
  solution:=SolutionIntMat(TransposedMat(A),bb);
  Require((solution=fail)=(decision.witness=fail),"Integer decision mismatch");
  if decision.witness<>fail then
   Require(ForAll(decision.witness,IsInt) and A*decision.witness=bb,"Integer witness");
   H:=Mat(decision.H);U:=Mat(decision.U);K:=Mat(decision.kernel);r:=RankMat(A);
   Require(r=decision.rank and H=U*TransposedMat(A) and ForAll(Concatenation(U),IsInt)
    and AbsInt(DeterminantMat(U))=1,"Integral Hermite identity");last:=0;
   for i in [1..Length(H)] do
    pivot:=PositionProperty(H[i],x->x<>0);
    if i<=r then Require(pivot<>fail and pivot>last and H[i][pivot]>0,"Hermite pivot");last:=pivot;
    else Require(pivot=fail,"Nonzero kernel row");fi;
   od;
   Require(K=TransposedMat(U{[r+1..Length(U)]}),"Incomplete integer kernel");
   Add(accepted,decision.t);fullkernels:=fullkernels+1;
  fi;
 od;
 Require(item.witness.t in accepted and item.witness=First(item.decisions,x->x.t=item.witness.t),"Uncertified final witness");
 Require(Correct(Family(item.witness.t),item.tail_axes,item.witness.witness)=found,"Witness reconstruction");
 Print("PASS N8 polynomial group tail GAP: class ",item.class_bound,"; ",columnchecks,
  " polynomial columns; ",jointchecks," joint controls; ",directchecks,
  " direct identity controls; ",kernelchecks," complete kernels; ",Length(candidates),
  " complete finite decisions; ",fullkernels," full integer kernels; 2 group witnesses\n");
end)();
QUIT_GAP(0);
