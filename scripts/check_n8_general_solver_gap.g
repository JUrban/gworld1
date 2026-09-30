# Native free nilpotent groups replay the complete-recursion certificates.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
if not IsBound(N8GeneralFiles) then Error("Explicit fixture paths required");fi;
N8GeneralFixtures:=fail;;
NGAssert:=function(test,message) if not test then Error(message);fi;end;
NGHall:=function(gens,description)
 local hall,i,p;
 hall:=[];
 for i in [1..Length(description)] do
  p:=description[i][2];
  if Length(p)=0 then Add(hall,gens[i]);else Add(hall,Comm(hall[p[1]+1],hall[p[2]+1]));fi;
 od;
 return hall;
end;
NGVector:=function(hall,vector)
 local g,i;
 g:=One(hall[1]);
 for i in [1..Length(vector)] do
  NGAssert(IsInt(vector[i]),"Nonintegral group coordinate");
  g:=g*hall[i]^vector[i];
 od;
 return g;
end;
NGWord:=function(gens,word)
 local ans,i;
 ans:=One(gens[1]);for i in word do ans:=ans*gens[AbsInt(i)]^SignInt(i);od;
 return ans;
end;
NGCorrect:=function(pair,axes,vector,hall,description)
 local ans,j,a,indices;
 ans:=ShallowCopy(pair);
 for j in [1..Length(axes)] do
  a:=axes[j];indices:=Filtered([1..Length(hall)],i->description[i][1]=a[2]);
  ans[a[1]+1]:=ans[a[1]+1]*hall[indices[a[3]+1]]^vector[j];
 od;
 return ans;
end;
NGRoots:=function(poly)
 local a,b,c,disc,s,roots,t;
 c:=poly[1][1]/poly[1][2];b:=poly[2][1]/poly[2][2];a:=poly[3][1]/poly[3][2];
 NGAssert(a<>0,"Not a quadratic obstruction");
 disc:=b*b-4*a*c;roots:=[];
 if disc<0 then return roots;fi;
 s:=RootInt(NumeratorRat(disc))/RootInt(DenominatorRat(disc));
 if s*s<>disc then return roots;fi;
 for t in [(-b+s)/(2*a),(-b-s)/(2*a)] do if IsInt(t) then AddSet(roots,t);fi;od;
 return roots;
end;
NGCounts:=rec(fixtures:=0,positive:=0,linear_blocks:=0,columns:=0,quadratics:=0,quadratic_samples:=0);;
NGCase:=function(row)
 local cache,model,full,gens,hall,target,event,stop,start,base,basecomm,indices,rhs,
       columns,j,unit,actual,expected,pair,soluble,block,last,qs,t,vec,ev,lambda,
       q2,correctionaxes,side,w,adapted,firstcount,polyvalue;
 cache:=[];
 model:=function(c)
  local group;
  if not IsBound(cache[c]) then
   group:=NilpotentQuotient(FreeGroup(row.rank),c);
   cache[c]:=rec(group:=group,gens:=GeneratorsOfGroup(group){[1..row.rank]});
   cache[c].hall:=NGHall(cache[c].gens,row.hall);
  fi;
  return cache[c];
 end;
 full:=model(row.class_bound);target:=NGWord(full.gens,row.target_word);
 if row.accepted then
  pair:=List(row.factor_coordinates,v->NGVector(full.hall,v));
  NGAssert(Comm(pair[1],pair[2])=target,"Positive witness failed");
  NGCounts.positive:=NGCounts.positive+1;
 fi;
 block:=fail;
 for event in row.events do
  if event.event in ["linear-tail","linear-obstruction","exception-block"] then
   start:=Sum(event.weights)+event.offset;
   if event.event="linear-tail" then stop:=row.class_bound;
   elif event.event="exception-block" then stop:=Sum(event.weights)+2*event.offset-1;
   else stop:=start;fi;
   ev:=model(stop);hall:=ev.hall;
   indices:=Filtered([1..Length(hall)],i->row.hall[i][1]>=start and row.hall[i][1]<=stop);
   base:=List(event.prefix_coordinates,v->NGVector(hall,v));basecomm:=Comm(base[1],base[2]);
   rhs:=basecomm^-1*NGWord(ev.gens,row.target_word);
   NGAssert(rhs=NGVector(hall{indices},event.rhs),"Native RHS mismatch");
   columns:=[];
   for j in [1..Length(event.axes)] do
    unit:=List(event.axes,x->0);unit[j]:=1;
    pair:=NGCorrect(base,event.axes,unit,hall,row.hall);
    actual:=basecomm^-1*Comm(pair[1],pair[2]);
    expected:=NGVector(hall{indices},List(event.columns,r->r[j]));
    NGAssert(actual=expected,"Native integral column mismatch");Add(columns,actual);
   od;
   soluble:=rhs in Subgroup(ev.group,columns);
   if event.event="linear-obstruction" then NGAssert(not soluble,"False integer obstruction");
   else
    if event.event="linear-tail" then vec:=event.solution;else vec:=event.point;fi;
    NGAssert(soluble=(vec<>fail),"Native subgroup membership mismatch");
    if vec<>fail then
     pair:=NGCorrect(base,event.axes,vec,hall,row.hall);
     NGAssert(Comm(pair[1],pair[2])=NGWord(ev.gens,row.target_word),"Affine solution failed");
    fi;
   fi;
   NGCounts.linear_blocks:=NGCounts.linear_blocks+1;
   NGCounts.columns:=NGCounts.columns+Length(columns);
   if event.event="exception-block" then block:=event;fi;
  elif event.event="quadratic-exception" then
   NGAssert(block<>fail and block.branch=event.branch,"Missing exception prefix");
   stop:=Sum(block.weights)+2*block.offset;ev:=model(stop);hall:=ev.hall;
   indices:=Filtered([1..Length(hall)],i->row.hall[i][1]=stop);
   base:=List(block.prefix_coordinates,v->NGVector(hall,v));
   adapted:=TransposedMat(event.adapted_kernel);qs:=event.coefficients;
   for t in [-2..3] do
    vec:=block.point+t*adapted[1];pair:=NGCorrect(base,block.axes,vec,hall,row.hall);
    actual:=Comm(pair[1],pair[2])^-1*NGWord(ev.gens,row.target_word);
    expected:=NGVector(hall{indices},qs[1]+t*qs[2]+t*t*qs[3]);
    NGAssert(actual=expected,"Native quadratic sample mismatch");
    NGCounts.quadratic_samples:=NGCounts.quadratic_samples+1;
   od;
   lambda:=event.functional;q2:=qs[3];
   NGAssert(lambda*q2<>0,"Vanishing separating functional");
   NGAssert(ForAll(TransposedMat(event.annihilated_columns),v->lambda*v=0),"Functional misses later column");
   correctionaxes:=[];
   for side in [0,1] do
    w:=block.weights[side+1]+2*block.offset;
    for j in [0..Length(Filtered(row.hall,h->h[1]=w))-1] do Add(correctionaxes,[side,w,j]);od;
   od;
   firstcount:=Length(correctionaxes);
   pair:=NGCorrect(base,block.axes,block.point,hall,row.hall);
   for j in [1..firstcount] do
    unit:=List(correctionaxes,x->0);unit[j]:=1;
    last:=NGCorrect(pair,correctionaxes,unit,hall,row.hall);
    actual:=Comm(pair[1],pair[2])^-1*Comm(last[1],last[2]);
    NGAssert(actual=NGVector(hall{indices},List(event.annihilated_columns,r->r[j])),"Last-layer column mismatch");
   od;
   for j in [2..Length(adapted)] do
    last:=NGCorrect(base,block.axes,block.point+adapted[j],hall,row.hall);
    actual:=Comm(last[1],last[2])^-1*NGWord(ev.gens,row.target_word);
    expected:=NGVector(hall{indices},qs[1]+List(event.annihilated_columns,r->r[firstcount+j-1]));
    NGAssert(actual=expected,"Later-block column mismatch");
   od;
   for j in [1..3] do
    polyvalue:=event.polynomial[j][1]/event.polynomial[j][2];
    NGAssert(lambda*qs[j]=polyvalue,"Projected polynomial mismatch");
   od;
   NGAssert(NGRoots(event.polynomial)=event.integer_roots,"Integer roots incomplete");
   NGCounts.quadratics:=NGCounts.quadratics+1;
  fi;
 od;
 NGCounts.fixtures:=NGCounts.fixtures+1;Print("native recursion ",row.label," verified\n");
end;
for filename in N8GeneralFiles do
 Read(filename);for row in N8GeneralFixtures do NGCase(row);od;
od;
Print("PASS N8 general GAP ",NGCounts,"\n");
QUIT;
