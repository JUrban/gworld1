N8C9Fail:=function(message)
    Print("FAIL ",message,"\n");FORCE_QUIT_GAP(1);
end;;
# Set N8C9Directory before reading this checker.
# Exact identities: b^-1[xh,y]=[b,h][h,y]; b^-1[x,yh]=[x,h]^b[b,h], b=[x,y].
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
Read(Concatenation(N8C9Directory,"/fixtures.g"));
if IsExistingFile(Concatenation(N8C9Directory,"/polynomial-fixtures.g")) then
    Read(Concatenation(N8C9Directory,"/polynomial-fixtures.g"));
else
    Read(Concatenation(N8C9Directory,"/polynomial-fixtures.g.gz"));
fi;
Read("scripts/n8_gap_hall_cache.g");
N8C9Groups:=rec();;N8C9Caches:=[];;
N8C9Group:=function(r,c)
    local key;
    key:=Concatenation(String(r),"_",String(c));
    if not IsBound(N8C9Groups.(key)) then
        Print("BEGIN GAP quotient ",r," ",c,"\n");
        N8C9Groups.(key):=NilpotentQuotient(FreeGroup(r),c);
        Add(N8C9Caches,rec(group:=N8C9Groups.(key),cache:=NewDictionary([1],true)));
        N8C9SeedHallCache(N8C9Groups.(key),r,c,Last(N8C9Caches).cache);
        Print("READY GAP quotient ",r," ",c,"\n");
    fi;
    return N8C9Groups.(key);
end;;
N8C9Balanced:=function(group,word,cache)
    local found,ans,gens,s,cut;
    found:=LookupDictionary(cache,word);
    if found<>fail then return found;fi;
    if Length(word)<=16 then
        ans:=One(group);gens:=GeneratorsOfGroup(group);
        for s in word do ans:=ans*gens[AbsInt(s)]^SignInt(s);od;
    else
        cut:=QuoInt(Length(word),2);
        ans:=N8C9Balanced(group,word{[1..cut]},cache)
             *N8C9Balanced(group,word{[cut+1..Length(word)]},cache);
    fi;
    AddDictionary(cache,word,ans);
    return ans;
end;;
N8C9Eval:=function(group,word)
    local cache;
    cache:=First(N8C9Caches,row->IsIdenticalObj(row.group,group)).cache;
    return N8C9Balanced(group,word,cache);
end;;
N8C9Roots:=function(c)
    local den,a,b,d,delta,s,roots,n;
    den:=Lcm(List(c,DenominatorRat));c:=den*c;
    a:=c[3];b:=2*c[2]-c[3];d:=2*c[1];
    if a=0 then
        if b=0 or (-d) mod b<>0 then return [];fi;
        return [-d/b];
    fi;
    delta:=b*b-4*a*d;
    if delta<0 then return [];fi;
    s:=RootInt(delta);
    if s*s<>delta then return [];fi;
    roots:=[];
    for n in [-b-s,-b+s] do
        if n mod (2*a)=0 then AddSet(roots,n/(2*a));fi;
    od;
    return roots;
end;;
N8C9Decode:=a->List(a,row->List(row,v->v[1]/v[2]));;
N8C9Poly:=function(coeff,k)
    return coeff[1]+k*coeff[2]+(k*(k-1)/2)*coeff[3];
end;;
Read("scripts/n8_gap_integer_components.g");
N8C9Arithmetic:=function(c,require_injective)
    local B,H,U,rank,i,j,pivots,pivot,last,part,residual,z,den,nums,equation,
          candidates,values,k,good,eq,remainder;
    B:=c.columns;H:=c.H;U:=c.U;rank:=c.rank;
    if not N8C9Unimodular(U) then N8C9Fail("Hermite unimodularity");fi;
    for i in [1..Length(U)] do
        if N8C9SparseProduct(U[i],B)<>H[i] then N8C9Fail("Hermite identity");fi;
    od;
    pivots:=[];last:=0;
    for i in [1..Length(H)] do
        pivot:=PositionProperty(H[i],x->x<>0);
        if i<=rank then
            if pivot=fail or pivot<=last or H[i][pivot]<0 then
                N8C9Fail("Hermite echelon shape");fi;
            Add(pivots,pivot);last:=pivot;
        elif pivot<>fail then N8C9Fail("Hermite rank");fi;
    od;
    if List(pivots,i->i-1)<>c.pivots or (require_injective and rank<>Length(B)) then
        N8C9Fail("polynomial correction rank");fi;
    part:=N8C9Decode(c.particular);residual:=N8C9Decode(c.residual);
    for j in [1..3] do
        if part[j]*B+residual[j]<>c.coefficients[j] or
           ForAny(pivots,i->residual[j][i]<>0) then
            N8C9Fail("rational polynomial reduction");fi;
    od;
    z:=[];
    for j in [1..3] do
        Add(z,ListWithIdenticalEntries(Length(H),0));remainder:=ShallowCopy(c.coefficients[j]);
        for i in [1..rank] do
            z[j][i]:=remainder[pivots[i]]/H[i][pivots[i]];
            if z[j][i]<>0 then remainder:=remainder-z[j][i]*H[i];fi;
        od;
        if remainder<>residual[j] or N8C9SparseProduct(z[j],U)<>part[j] then
            N8C9Fail("independent echelon reduction");fi;
    od;
    for i in [1..rank] do
        den:=Lcm(List(z,row->DenominatorRat(row[i])));
        nums:=List(z,row->den*row[i]);
        if [den,nums]<>c.congruences[i] then N8C9Fail("integrality congruence");fi;
    od;
    equation:=fail;
    for i in [1..Length(B[1])] do
        eq:=List(residual,row->row[i]);
        if ForAny(eq,x->x<>0) then equation:=eq;break;fi;
    od;
    if equation=fail or c.mode<>"finite_points" or c.period<>fail then
        N8C9Fail("missing quadratic cokernel obstruction");fi;
    candidates:=N8C9Roots(equation);
    if candidates<>c.candidates then N8C9Fail("quadratic root list");fi;
    values:=[];
    for k in candidates do
        good:=ForAll(N8C9Poly(residual,k),x->x=0);
        for i in [1..rank] do
            if not IsInt(N8C9Poly(List(z,row->[row[i]]),k)[1]) then good:=false;fi;
        od;
        if good then Add(values,k);fi;
    od;
    if values<>c.values then N8C9Fail("complete integral parameter list");fi;
end;;

# nq stores its lower central series as suffixes of the defining pcp.
# On gamma_s with 2s>class these coordinates add, so integer row-lattice
# membership is exactly subgroup membership. Check the suffix and support.
N8C9Membership:=function(group,degree,columns,target)
    local pcp,gens,lcs,low,suffix,cut,allcoords,row,rows,rhs,solution,product,i;
    if Length(columns)=0 then return target=One(group);fi;
    pcp:=Pcp(group);gens:=GeneratorsOfPcp(pcp);
    if gens<>GeneratorsOfGroup(group) or
       ForAny(RelativeOrdersOfPcp(pcp),n->n<>0) then
        N8C9Fail("unexpected ambient pcp");fi;
    lcs:=LowerCentralSeriesOfGroup(group);low:=QuoInt(degree,2)+1;
    if Length(lcs)>degree+1 then N8C9Fail("nilpotency class bound");fi;
    suffix:=GeneratorsOfGroup(lcs[low]);cut:=Length(gens)-Length(suffix);
    if suffix<>gens{[cut+1..Length(gens)]} then
        N8C9Fail("lower central pcp suffix");fi;
    allcoords:=List(Concatenation(columns,[target]),g->ExponentsByPcp(pcp,g));
    for row in allcoords do
        if ForAny(row{[1..cut]},n->n<>0) then
            N8C9Fail("increment outside certified abelian tail");fi;
    od;
    rows:=List(allcoords{[1..Length(columns)]},row->row{[cut+1..Length(gens)]});
    rhs:=Last(allcoords){[cut+1..Length(gens)]};
    solution:=N8C9IntegerSolution(rows,rhs);
    if solution=fail then return false;fi;
    if solution*rows<>rhs then N8C9Fail("integer tail solution");fi;
    product:=One(group);
    for i in [1..Length(columns)] do
        if solution[i]<>0 then product:=product*columns[i]^solution[i];fi;
    od;
    if product<>target then N8C9Fail("tail solution group product");fi;
    return true;
end;;

N8C9Positive:=0;;
for item in N8C9Witnesses do
    group:=N8C9Group(item[1],item[2]);;
    if Comm(N8C9Eval(group,item[4]),N8C9Eval(group,item[5]))<>
       N8C9Eval(group,item[3]) then N8C9Fail("word witness");fi;
    N8C9Positive:=N8C9Positive+1;
    Print("WITNESS ",N8C9Positive,"\n");
od;
N8C9Count:=0;;N8C9Negative:=0;;
for item in N8C9Steps do
    Print("BEGIN LINEAR ",N8C9Count+1,"\n");
    group:=N8C9Group(item[1],item[2]);;
    x:=N8C9Eval(group,item[4]);;y:=N8C9Eval(group,item[5]);;
    base:=Comm(x,y);;delta:=base^-1*N8C9Eval(group,item[3]);;
    corrections:=[];
    Print("BEGIN COLUMNS ",Length(item[6]),"\n");
    for axis in item[6] do
        h:=N8C9Eval(group,axis[2]);
        if axis[1]=0 then Add(corrections,Comm(base,h)*Comm(h,y));
        else Add(corrections,Comm(x,h)^base*Comm(base,h));fi;
    od;
    Print("BEGIN MEMBERSHIP\n");
    soluble:=N8C9Membership(group,item[2],corrections,delta);
    if soluble<>item[7] then N8C9Fail("linear branch membership");fi;
    N8C9Count:=N8C9Count+1;
    Print("LINEAR ",N8C9Count," ",soluble,"\n");
    if not soluble then N8C9Negative:=N8C9Negative+1;fi;
od;
# Generic offsets: the prefix retains the previously audited group/lattice
# verifier; this section independently reconstructs every new branch.
N8NewCentral:=function(group,degree,coords)
 local ans,h,i;
 h:=List(N8C9Halls[degree],w->N8C9Eval(group,w));ans:=One(group);
 if Length(h)<>Length(coords) then N8C9Fail("central coordinate width");fi;
 for i in [1..Length(h)] do if coords[i]<>0 then ans:=ans*h[i]^coords[i];fi;od;
 return ans;
end;;
N8NewApply:=function(group,pair,p,q,j,coords)
 local x,y,u,v,i;
 x:=pair[1];y:=pair[2];
 u:=List(N8C9Halls[p+j],w->N8C9Eval(group,w));
 v:=List(N8C9Halls[q+j],w->N8C9Eval(group,w));
 if Length(coords)<>Length(u)+Length(v) then N8C9Fail("correction width");fi;
 for i in [1..Length(u)] do if coords[i]<>0 then x:=x*u[i]^coords[i];fi;od;
 for i in [1..Length(v)] do
  if coords[Length(u)+i]<>0 then y:=y*v[i]^coords[Length(u)+i];fi;
 od;
 return [x,y];
end;;
N8NewColumns:=function(group,pair,p,q,j)
 local x,y,base,ans,h,w;
 x:=pair[1];y:=pair[2];base:=Comm(x,y);ans:=[];
 for w in N8C9Halls[p+j] do
  h:=N8C9Eval(group,w);Add(ans,Comm(base,h)*Comm(h,y));
 od;
 for w in N8C9Halls[q+j] do
  h:=N8C9Eval(group,w);Add(ans,Comm(x,h)^base*Comm(base,h));
 od;
 return ans;
end;;
N8NewAffine:=function(matrix,rhs,base,kernel)
 local nullity,v;
 if base*matrix<>rhs then N8C9Fail("affine particular");fi;
 nullity:=Length(matrix)-RankMat(matrix);
 if nullity<>Length(kernel) or nullity>1 then N8C9Fail("affine nullity");fi;
 for v in kernel do
  if ForAny(v*matrix,x->x<>0) or Gcd(v)<>1 then N8C9Fail("primitive affine kernel");fi;
 od;
end;;
N8NewLine:=function(row)
 local g,pair,cols,pcp,rows,target;
 g:=N8C9Group(row.rank,row.p+row.q+row.offset);
 pair:=[N8C9Eval(g,row.x0),N8C9Eval(g,row.y0)];
 cols:=N8NewColumns(g,pair,row.p,row.q,row.offset);pcp:=Pcp(g);
 rows:=List(cols,h->ExponentsByPcp(pcp,h));
 target:=ExponentsByPcp(pcp,Comm(pair[1],pair[2])^-1*N8C9Eval(g,row.word));
 N8NewAffine(rows,target,row.vector,[row.kernel]);
end;;
N8NewRun:=function()
 local row,g,pair0,pair,target,actual,pcp,dim,k,sample,matrix,sol,
       c,chosen,coords,base,direction,period,shift,content,
       nullCount,nielsenCount,coupledCount,coupledNegative,pointCount,lineCount,
       nonunitCount,polyCount,lateCount,emptyCount,sampleCount;
 nullCount:=0;nielsenCount:=0;coupledCount:=0;coupledNegative:=0;
 pointCount:=0;lineCount:=0;nonunitCount:=0;polyCount:=0;lateCount:=0;
 emptyCount:=0;sampleCount:=0;
 for row in N8NewNullities do
  g:=N8C9Group(row.rank,row.degree);
  pair0:=[N8C9Eval(g,row.x0),N8C9Eval(g,row.y0)];
  actual:=N8NewColumns(g,pair0,row.p,row.q,row.offset);pcp:=Pcp(g);
  dim:=Length(actual)-RankMat(List(actual,h->ExponentsByPcp(pcp,h)));
  if dim<>row.dimension then N8C9Fail("correction nullity");fi;
  nullCount:=nullCount+1;Print("NULLITY ",nullCount," ",dim," VERIFIED\n");
 od;
 for row in N8NewNielsen do
  N8NewLine(row);g:=N8C9Group(row.rank,row.q);
  pair0:=[N8C9Eval(g,row.x0),N8C9Eval(g,row.y0)];
  content:=Gcd(List(ExponentsByPcp(Pcp(g),pair0[2]),AbsInt));
  if content<>row.period or row.q<>row.p+row.offset then N8C9Fail("Nielsen period");fi;
  pair:=N8NewApply(g,pair0,row.p,row.q,row.offset,row.vector);
  shift:=N8NewApply(g,pair0,row.p,row.q,row.offset,row.vector+row.period*row.kernel);
  if shift<>[pair[2]^row.sign*pair[1],pair[2]] then N8C9Fail("Nielsen leading shift");fi;
  g:=N8C9Group(row.rank,row.class_bound);
  pair0:=[N8C9Eval(g,row.x0),N8C9Eval(g,row.y0)];
  if Comm(pair0[2]^row.sign*pair0[1],pair0[2])<>Comm(pair0[1],pair0[2]) then
   N8C9Fail("Nielsen exact identity");fi;
  nielsenCount:=nielsenCount+1;Print("NIELSEN ",nielsenCount," VERIFIED\n");
 od;
 for row in N8NewCoupled do
  N8NewLine(row);g:=N8C9Group(row.rank,row.degree);
  pair0:=[N8C9Eval(g,row.x0),N8C9Eval(g,row.y0)];target:=N8C9Eval(g,row.word);
  actual:=N8NewColumns(g,pair0,row.p,row.q,3);
  if actual<>List(row.columns,v->N8NewCentral(g,row.degree,v)) then
   N8C9Fail("coupled group columns");fi;
  if RankMat(row.columns)<>Length(row.columns) then N8C9Fail("successor injectivity");fi;
  for sample in row.samples do
   k:=sample[1];pair:=N8NewApply(g,pair0,row.p,row.q,2,row.vector+k*row.kernel);
   if pair<>List(sample{[2,3]},w->N8C9Eval(g,w)) or Comm(pair[1],pair[2])^-1*target<>
      N8NewCentral(g,row.degree,row.coefficients[1]+k*row.coefficients[2]) then
    N8C9Fail("coupled affine residual");fi;
  od;
  matrix:=Concatenation(row.columns,[-row.coefficients[2]]);
  sol:=N8C9IntegerSolution(matrix,row.coefficients[1]);
  if (sol=fail)<>(row.solution=fail) then N8C9Fail("coupled integer solvability");fi;
  if sol=fail then coupledNegative:=coupledNegative+1;
  else
   N8NewAffine(matrix,row.coefficients[1],row.solution[1],row.solution[2]);
   if Length(row.solution[2])=0 then pointCount:=pointCount+1;
   else
    lineCount:=lineCount+1;
    if Last(row.solution[2][1])=0 then N8C9Fail("zero projected line step");fi;
    if AbsInt(Last(row.solution[2][1]))>1 then nonunitCount:=nonunitCount+1;fi;
   fi;
  fi;
  coupledCount:=coupledCount+1;Print("COUPLED ",coupledCount," VERIFIED\n");
 od;
 for row in N8C9Polynomials do
  N8NewLine(row);c:=row.certificate;N8C9Arithmetic(c,false);
  if not ForAny(c.residual[3],v->v[1]<>0) then N8C9Fail("nonzero quadratic obstruction");fi;
  g:=N8C9Group(row.rank,row.degree);
  pair0:=[N8C9Eval(g,row.x0),N8C9Eval(g,row.y0)];target:=N8C9Eval(g,row.word);
  actual:=N8NewColumns(g,pair0,row.p,row.q,2*row.offset);
  if actual<>List(c.columns,v->N8NewCentral(g,row.degree,v)) then
   N8C9Fail("polynomial group columns");fi;
  if row.kind="polynomial_late" then
   lateCount:=lateCount+1;
   chosen:=First(N8NewCoupled,r->r.word=row.word and r.x0=row.x0 and r.y0=row.y0
                and r.vector=row.vector and r.kernel=row.kernel);
   if chosen=fail or chosen.solution=fail then N8C9Fail("missing coupled stage");fi;
   matrix:=Concatenation(chosen.columns,[-chosen.coefficients[2]]);
   N8NewAffine(matrix,chosen.coefficients[1],row.coupled_base,[row.coupled_direction]);
   if Last(row.coupled_direction)=0 then N8C9Fail("zero late line step");fi;
  fi;
  for sample in row.samples do
   k:=sample[1];
   if row.kind="polynomial_late" then
    coords:=row.coupled_base+k*row.coupled_direction;
    pair:=N8NewApply(g,pair0,row.p,row.q,2,row.vector+Last(coords)*row.kernel);
    pair:=N8NewApply(g,pair,row.p,row.q,3,coords{[1..Length(coords)-1]});
   else pair:=N8NewApply(g,pair0,row.p,row.q,1,row.vector+k*row.kernel);fi;
   if pair<>List(sample{[2,3]},w->N8C9Eval(g,w)) or Comm(pair[1],pair[2])^-1*target<>
      N8NewCentral(g,row.degree,N8C9Poly(c.coefficients,k)) then
    N8C9Fail("polynomial lift or residual");fi;
   sampleCount:=sampleCount+1;
  od;
  if Length(c.values)=0 then emptyCount:=emptyCount+1;fi;
  polyCount:=polyCount+1;Print("POLYNOMIAL ",polyCount," VERIFIED\n");
 od;
 Print("PASS N8 fifth/sixth layer GAP: ",N8C9Positive," witnesses; ",N8C9Count,
       " linear decisions (",N8C9Negative," negative); ",nullCount," nullities; ",
       nielsenCount," Nielsen periods; ",coupledCount," coupled (",coupledNegative,
       " negative, ",pointCount," points, ",lineCount," lines, ",nonunitCount,
       " nonunit steps); ",polyCount," polynomials (",lateCount," late, ",emptyCount,
       " empty); ",sampleCount," polynomial samples\n");
end;;
N8NewRun();;
QUIT_GAP(0);
