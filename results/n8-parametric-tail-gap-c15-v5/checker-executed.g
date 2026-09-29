# Independent exact group replay of polynomial-tail fixtures.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
if not IsBound(N8ParametricTailFile) then Error("Set fixture path");fi;
N8ParametricTail:=fail;;Read(N8ParametricTailFile);;
(function()
 local item,Require,Hall,Element,Correct,Poly,MatrixAt,VectorElement,
       free,fhall,group,gens,hall,base,target,known,found,relators,
       value,line,pair,comm,mat,rhs,side,i,j,col,changed,pred,vec,actual,
       systems,columnchecks,jointchecks,negativechecks,scale,algebra,
       letters,liehall,h,C,D,Bracket,columns,dim,offset,axes,ker,
       successor,tailgroup,tailpcp,higher,highvectors,jointvectors,basecomm,
       needed,started,Stage,hallstrings,nqinput,correction,directchecks;
 item:=N8ParametricTail;
 started:=Runtime();Stage:=function(s)Print(s," at ",Runtime()-started," ms\n");end;
 Require:=function(ok,msg)if not ok then Error(msg);fi;end;
 needed:=Union([1..item.retained],List(item.boundaries,i->i+1));
 Require(ForAll(item.boundaries,i->ForAll(item.hall[i+1][2],j->j<item.retained)),"Boundary needs an omitted parent");
 Hall:=function(gens,description)
  local out,h,i;
  out:=[];
  for i in [1..Length(description)] do
   h:=description[i];
   if not i in needed then Add(out,One(gens[1]));
   elif Length(h[2])=0 then Add(out,gens[Length(out)+1]);
   else Add(out,Comm(out[h[2][1]+1],out[h[2][2]+1]));fi;
  od;return out;
 end;
 Element:=function(terms)
  local out,h;
  out:=One(group);
  for h in terms do out:=out*hall[h[1]+1]^h[2];od;
  return out;
 end;
 Correct:=function(pair,axes,vector)
  local out,j;
  out:=ShallowCopy(pair);
  for j in [1..Length(axes)] do
   out[axes[j][1]+1]:=out[axes[j][1]+1]*hall[axes[j][2]+1]^vector[j];
  od;return out;
 end;
 Poly:=function(data,t)
  return Sum([1..Length(data)],i->data[i][1]/data[i][2]*t^(i-1));
 end;
 MatrixAt:=function(data,t)return List(data.entries,row->List(row,x->Poly(x,t)));end;
 VectorElement:=function(vector)
  local out,j;
  Require(Length(vector)=Length(item.rows) and ForAll(vector,IsInt),"Nonintegral Hall vector");
  out:=One(group);
  for j in [1..Length(vector)] do out:=out*hall[item.rows[j]+1]^vector[j];od;
  return out;
 end;
 Require(item.p+item.q+2*(item.t+2)>item.class_bound,"Tail variables may interact");
 Require(2*(item.p+item.q+item.t)>item.class_bound,"Comparison tail not abelian");
 Require(item.degree_bound=QuoInt(item.class_bound,item.p+item.t),"Unjustified interpolation degree");
 Require(item.sample_values=[0..item.degree_bound],"Missing polynomial samples");
 for mat in [item.P,item.b,item.certificate.P,item.certificate.b] do
  Require(ForAll(Concatenation(mat.entries),x->Length(x)<=item.degree_bound+1),"Polynomial exceeds interpolation degree");
 od;
 if item.negative<>fail then
  for mat in [item.negative.certificate.P,item.negative.certificate.b] do
   Require(ForAll(Concatenation(mat.entries),x->Length(x)<=item.degree_bound+1),"Negative polynomial exceeds interpolation degree");
  od;
 fi;
 for axes in [item.axes3,item.axes4,item.axes_tail] do
  for h in axes do Require(h[1] in [0,1],"Unknown factor side");od;
 od;
 for h in item.axes3 do
  Require(item.hall[h[2]+1][1]=[item.p,item.q][h[1]+1]+item.t,"Offset3 weight");
 od;
 for h in item.axes4 do
  Require(item.hall[h[2]+1][1]=[item.p,item.q][h[1]+1]+item.t+1,"Successor weight");
 od;
 for h in item.axes_tail do
  Require(item.hall[h[2]+1][1]>=[item.p,item.q][h[1]+1]+item.t+2,"Low tail coordinate");
 od;
 axes:=[];
 for side in [0,1] do for i in [1..item.retained] do
  if item.hall[i][1]>=[item.p,item.q][side+1]+item.t+2 and
     item.hall[i][1]<=item.class_bound-[item.q,item.p][side+1] then
   Add(axes,[side,i-1]);
  fi;
 od;od;
 Require(axes=item.axes_tail,"Incomplete tail coordinates");
 Require(item.rows=List(Filtered([1..item.retained],i->item.hall[i][1]>=item.p+item.q+item.t),i->i-1),"Incomplete output coordinates");
 # NQ accepts nested commutator expressions directly. Expanding them as
 # free-group words and then stringifying them is exponentially wasteful.
 hallstrings:=[];
 for i in [1..Length(item.hall)] do
  h:=item.hall[i];
  if not i in needed then Add(hallstrings,"");
  elif IsEmpty(h[2]) then Add(hallstrings,["a","b"][i]);
  else Add(hallstrings,Concatenation("[",hallstrings[h[2][1]+1],",",hallstrings[h[2][2]+1],"]"));fi;
 od;
 nqinput:=Concatenation("< a,b | ",JoinStringsWithSeparator(List(item.boundaries,i->hallstrings[i+1]),", ")," >\n");
 if IsBound(N8ParametricTailPresentationFile) then PrintTo(N8ParametricTailPresentationFile,nqinput);fi;
 Stage("Compact weighted relators constructed");
 group:=NilpotentQuotient(:input_string:=nqinput,class:=item.class_bound);
 Stage("Weighted quotient constructed");
 Require(HirschLength(group)=item.retained and Size(TorsionSubgroup(group))=1,"Weighted group rank/torsion");
 gens:=GeneratorsOfGroup(group){[1..2]};hall:=Hall(gens,item.hall);
 Require(ForAll(item.boundaries,i->hall[i+1]=One(group)),"Boundary relation");
 base:=List(item.base,Element);target:=Element(item.target);
 known:=List(item.known_pair,Element);found:=List(item.found_pair,Element);
 Require(Comm(known[1],known[2])=target,"Known witness");
 Require(Comm(found[1],found[2])=target,"Computed witness");
 Stage("Known and computed group witnesses checked");
 # Independently confirm the full exceptional kernel pattern in the
 # weighted two-generator algebra, without the Python matrices.
 algebra:=FreeAssociativeAlgebraWithOne(Rationals,2,"a");letters:=GeneratorsOfAlgebraWithOne(algebra);
 Bracket:=function(a,b)return a*b-b*a;end;
 liehall:=[];
 for h in item.hall do
  if h[1]>item.q+5 then Add(liehall,Zero(algebra));
  elif IsEmpty(h[2]) then Add(liehall,letters[Length(liehall)+1]);
  else Add(liehall,Bracket(liehall[h[2][1]+1],liehall[h[2][2]+1]));fi;
 od;
 C:=item.x_scale*letters[1];D:=letters[2];for i in [1..4] do D:=Bracket(letters[1],D);od;
 D:=item.y_scale*D;
 for offset in [3,4,5] do
  axes:=[];
  for side in [0,1] do for i in [1..item.retained] do
   if item.hall[i][1]=[item.p,item.q][side+1]+offset then Add(axes,[side,i-1]);fi;
  od;od;
  columns:=[];
  for h in axes do
   if h[1]=0 then Add(columns,Bracket(liehall[h[2]+1],D));
   else Add(columns,Bracket(C,liehall[h[2]+1]));fi;
  od;
  dim:=Dimension(VectorSpace(Rationals,Filtered(columns,x->not IsZero(x))));
  Require((offset=4 and Length(columns)=dim) or
          (offset<>4 and Length(columns)-dim=1),"Unexpected exceptional kernel");
  if offset=3 then
   Require(axes=item.axes3 and Gcd(item.kernel3)=1,"Incomplete or nonprimitive kernel");
   Require(IsZero(Sum([1..Length(columns)],i->item.kernel3[i]*columns[i])),"Kernel identity");
  fi;
  if offset=4 then Require(axes=item.axes4,"Incomplete successor coordinates");fi;
 od;
 Stage("Complete kernel dimensions checked");
 # Verify that the supplied integral affine line is complete, in the
 # actual group's successor layer. That tail is abelian here, so its
 # polycyclic exponent vectors give independent rational rank checks.
 successor:=item.p+item.q+item.t+1;
 tailgroup:=Subgroup(group,List(Filtered([1..item.retained],i->item.hall[i][1]>=successor),i->hall[i]));
 higher:=Subgroup(group,List(Filtered([1..item.retained],i->item.hall[i][1]>successor),i->hall[i]));
 Require(IsAbelian(tailgroup),"Successor comparison tail not abelian");
 tailpcp:=Pcp(tailgroup);basecomm:=Comm(base[1],base[2]);
 Require(basecomm^-1*target in tailgroup,"Offset3 right side is not zero");
 highvectors:=List(GeneratorsOfGroup(higher),h->ExponentsByPcp(tailpcp,h));
 changed:=Correct(base,item.axes3,item.kernel3);
 actual:=basecomm^-1*Comm(changed[1],changed[2]);
 jointvectors:=[ExponentsByPcp(tailpcp,actual)];
 for h in item.axes4 do
  changed:=ShallowCopy(base);changed[h[1]+1]:=changed[h[1]+1]*hall[h[2]+1];
  actual:=basecomm^-1*Comm(changed[1],changed[2]);
  Add(jointvectors,ExponentsByPcp(tailpcp,actual));
 od;
 Require(RankMat(Concatenation(jointvectors,highvectors))-RankMat(highvectors)=Length(item.axes4),"Joint successor kernel is not one-dimensional");
 Require(Length(item.direction)=Length(item.axes4)+1 and Gcd(item.direction)=1 and
         item.direction[1]<>0,"Line direction is not primitive or has zero parameter step");
 for value in [0,1] do
  line:=item.point+value*item.direction;
  changed:=Correct(base,item.axes3,line[1]*item.kernel3);
  changed:=Correct(changed,item.axes4,line{[2..Length(line)]});
  Require(Comm(changed[1],changed[2])^-1*target in higher,"Affine line fails successor equations");
 od;
 Stage("Complete integral successor line checked");
 columnchecks:=0;jointchecks:=0;negativechecks:=0;directchecks:=0;
 for value in item.sample_values do
  line:=item.point+value*item.direction;
  pair:=Correct(base,item.axes3,line[1]*item.kernel3);
  pair:=Correct(pair,item.axes4,line{[2..Length(line)]});
  comm:=Comm(pair[1],pair[2]);mat:=MatrixAt(item.P,value);
  rhs:=List(MatrixAt(item.b,value),r->r[1]);
  Require(comm*VectorElement(rhs)=target,"Polynomial target residual");
  scale:=item.certificate.input_scale;
  Require(MatrixAt(item.certificate.P,value)=scale*mat and
          MatrixAt(item.certificate.b,value)=List(rhs,x->[scale*x]),"Arithmetic certificate input mismatch");
  Stage(Concatenation("Polynomial group sample ",String(value)," residual checked"));
  for j in [1..Length(item.axes_tail)] do
   h:=item.axes_tail[j];correction:=hall[h[2]+1];
   # Exact identities in any group, with [x,y]=x^-1*y^-1*x*y:
   # [x*h,y]=[x,y]^h*[h,y], [x,y*h]=[x,h]*[x,y]^h.
   # NQ performs every operation; no truncated Python formula is used.
   if h[1]=0 then actual:=comm^correction*Comm(correction,pair[2]);
   else actual:=Comm(pair[1],correction)*comm^correction;fi;
   col:=List(mat,row->row[j]);pred:=VectorElement(col);
   Require(comm*pred=actual,"Polynomial correction column");
   if j in [1,Length(item.axes_tail)] then
    changed:=ShallowCopy(pair);changed[h[1]+1]:=changed[h[1]+1]*correction;
    Require(actual=Comm(changed[1],changed[2]),"Exact commutator identity control");
    directchecks:=directchecks+1;
   fi;
   columnchecks:=columnchecks+1;
  od;
  Stage(Concatenation("Polynomial group sample ",String(value)," columns checked"));
  for vec in item.joint_vectors do
   changed:=Correct(pair,item.axes_tail,vec);
   Require(comm*VectorElement(mat*vec)=Comm(changed[1],changed[2]),"Joint linearity control");
   jointchecks:=jointchecks+1;
  od;
  if item.negative<>fail then
   rhs:=ShallowCopy(rhs);rhs[item.negative.row+1]:=rhs[item.negative.row+1]+1;
   Require(comm*VectorElement(rhs)=target*hall[item.negative.hall_index+1],"Negative target mismatch");
   scale:=item.negative.certificate.input_scale;
   Require(MatrixAt(item.negative.certificate.P,value)=scale*mat and
           MatrixAt(item.negative.certificate.b,value)=List(rhs,x->[scale*x]),"Negative certificate input mismatch");
   negativechecks:=negativechecks+1;
  fi;
  Stage(Concatenation("Polynomial group sample ",String(value)," checked"));
 od;
 value:=item.certificate.witness.t;line:=item.point+value*item.direction;
 pair:=Correct(base,item.axes3,line[1]*item.kernel3);
 pair:=Correct(pair,item.axes4,line{[2..Length(line)]});
 pair:=Correct(pair,item.axes_tail,item.certificate.witness.witness);
 Require(pair=found,"Arithmetic witness does not reconstruct the group factors");
 Print("PASS N8 parametric tail GAP: class ",item.class_bound,"; ",columnchecks,
       " polynomial columns; ",jointchecks," joint controls; ",negativechecks,
       " negative targets; ",directchecks," direct identity controls; 3 complete kernels; 1 complete integral line; 2 group witnesses\n");
end)();
QUIT_GAP(0);
