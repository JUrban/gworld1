# General type-(1,q) replay; final lattice may have a kernel.
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
# Independently establish completeness of each first affine line.
N8OddFirstLine:=function(item)
    local g,x,y,base,target,u,v,columns,pcp,rows,rank,product,i;
    g:=N8C9Group(item.rank,item.degree-1);
    x:=N8C9Eval(g,item.x0);y:=N8C9Eval(g,item.y0);
    base:=Comm(x,y);target:=base^-1*N8C9Eval(g,item.word);
    u:=List(N8C9Halls[2],w->N8C9Eval(g,w));
    v:=List(N8C9Halls[item.q+1],w->N8C9Eval(g,w));
    columns:=Concatenation(List(u,a->Comm(a,y)),List(v,b->Comm(x,b)));
    pcp:=Pcp(g);rows:=List(columns,a->ExponentsByPcp(pcp,a));rank:=RankMat(rows);
    if Length(columns)-rank<>1 or Gcd(List(item.kernel,AbsInt))<>1 then
        N8C9Fail("complete primitive first kernel");fi;
    product:=One(g);
    for i in [1..Length(columns)] do product:=product*columns[i]^item.kernel[i];od;
    if product<>One(g) then N8C9Fail("first kernel direction");fi;
    product:=One(g);
    for i in [1..Length(columns)] do product:=product*columns[i]^item.vector[i];od;
    if product<>target then N8C9Fail("first affine particular");fi;
    Print("FIRST AFFINE LINE VERIFIED\n");
end;;


# Recompute the nullity of every soluble first map, including the unique ones.
Read(Concatenation(N8C9Directory,"/extra-fixtures.g"));
N8Type1FirstCheck:=function(item)
 local g,x,y,base,columns,axis,h,rows,pcp,dim;
 g:=N8C9Group(item[1],item[2]);x:=N8C9Eval(g,item[3]);y:=N8C9Eval(g,item[4]);
 base:=Comm(x,y);columns:=[];
 for axis in item[5] do
  h:=N8C9Eval(g,axis[2]);
  if axis[1]=0 then Add(columns,Comm(base,h)*Comm(h,y));
  else Add(columns,Comm(x,h)^base*Comm(base,h));fi;
 od;
 pcp:=Pcp(g);rows:=List(columns,a->ExponentsByPcp(pcp,a));
 dim:=Length(columns)-RankMat(rows);
 if dim<>item[6] then N8C9Fail("first-map nullity");fi;
 Print("FIRST NULLITY ",dim," VERIFIED\n");
end;;
N8Type1ScopeCache:=rec();;
N8Type1ScopeCheck:=function(item)
 local r,d,g,key,columns,p,q,a,b,pcp,rows,target,answer,entry;
 r:=item[1];d:=item[2];g:=N8C9Group(r,d);key:=Concatenation(String(r),"_",String(d));
 if not IsBound(N8Type1ScopeCache.(key)) then
  columns:=[];
  for p in [2..QuoInt(d,2)] do
   q:=d-p;
   for a in N8C9Halls[p] do for b in N8C9Halls[q] do
    Add(columns,Comm(N8C9Eval(g,a),N8C9Eval(g,b)));
   od;od;
  od;
  pcp:=Pcp(g);rows:=List(columns,a->ExponentsByPcp(pcp,a));
  N8Type1ScopeCache.(key):=rec(rows:=rows,rank:=RankMat(rows));
 fi;
 entry:=N8Type1ScopeCache.(key);target:=ExponentsByPcp(Pcp(g),N8C9Eval(g,item[3]));
 answer:=RankMat(Concatenation(entry.rows,[target]))>entry.rank;
 if answer<>item[4] then N8C9Fail("leading metabelian scope");fi;
 Print("METABELIAN SCOPE ",answer," VERIFIED\n");
end;;
for item in N8Type1FirstMaps do N8Type1FirstCheck(item);od;
for item in N8Type1Scopes do N8Type1ScopeCheck(item);od;

N8C9Samples:=0;;N8C9NoParameters:=0;;hall:=[];;
for item in N8C9Polynomials do
    Print("BEGIN POLYNOMIAL ",item.degree,"\n");
    N8OddFirstLine(item);
    c:=item.certificate;
    N8C9Arithmetic(c,false);
    Print("ARITHMETIC VERIFIED\n");
    if Length(c.values)=0 then N8C9NoParameters:=N8C9NoParameters+1;fi;
    group:=N8C9Group(item.rank,item.degree);;
    hall:=List(N8C9Halls[item.degree],w->N8C9Eval(group,w));;
    central:=function(coords)
        local ans,i;
        ans:=One(group);
        for i in [1..Length(coords)] do
            if coords[i]<>0 then ans:=ans*hall[i]^coords[i];fi;
        od;
        return ans;
    end;;
    x0:=N8C9Eval(group,item.x0);;y0:=N8C9Eval(group,item.y0);;
    target:=N8C9Eval(group,item.word);;
    u:=List(N8C9Halls[2],w->N8C9Eval(group,w));;
    v:=List(N8C9Halls[item.q+1],w->N8C9Eval(group,w));;
    for sample in item.samples do
        k:=sample[1];coords:=item.vector+k*item.kernel;x:=x0;y:=y0;
        for i in [1..Length(u)] do
            if coords[i]<>0 then x:=x*u[i]^coords[i];fi;
        od;
        for i in [1..Length(v)] do
            if coords[Length(u)+i]<>0 then y:=y*v[i]^coords[Length(u)+i];fi;
        od;
        if x<>N8C9Eval(group,sample[2]) or y<>N8C9Eval(group,sample[3]) then
            N8C9Fail("affine parameter group lifts");fi;
        if Comm(x,y)^-1*target<>central(N8C9Poly(c.coefficients,k)) then
            N8C9Fail("quadratic coefficients");fi;
        N8C9Samples:=N8C9Samples+1;Print("SAMPLE ",N8C9Samples," VERIFIED\n");
    od;
    Print("BEGIN POLYNOMIAL COLUMNS\n");
    base:=Comm(x0,y0);axes:=Concatenation(List(N8C9Halls[3],w->[0,w]),
                                      List(N8C9Halls[item.q+2],w->[1,w]));;
    for i in [1..Length(axes)] do
        h:=N8C9Eval(group,axes[i][2]);
        if axes[i][1]=0 then change:=Comm(base,h)*Comm(h,y0);
        else change:=Comm(x0,h)^base*Comm(base,h);fi;
        if change<>central(c.columns[i]) then N8C9Fail("polynomial correction lattice");fi;
    od;
od;
Print("PASS N8 general type1 GAP: ",N8C9Positive," witnesses; ",N8C9Count,
      " linear decisions (",N8C9Negative," negative); ",Length(N8C9Polynomials),
      " polynomial decisions (",N8C9NoParameters," empty); ",N8C9Samples," samples; ",Length(N8Type1FirstMaps)," first nullities; ",Length(N8Type1Scopes)," scope checks\n");
QUIT_GAP(0);
