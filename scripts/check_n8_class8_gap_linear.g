# Set N8C8Directory before reading this checker.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
Read(Concatenation(N8C8Directory,"/fixtures.g"));
Read(Concatenation(N8C8Directory,"/polynomial-fixtures.g"));
N8C8Groups:=rec();;N8C8Caches:=[];;
N8C8Group:=function(r,c)
    local key;
    key:=Concatenation(String(r),"_",String(c));
    if not IsBound(N8C8Groups.(key)) then
        N8C8Groups.(key):=NilpotentQuotient(FreeGroup(r),c);
        Add(N8C8Caches,rec(group:=N8C8Groups.(key),cache:=NewDictionary([1],true)));
        Print("GROUP READY ",key,"\n");
    fi;
    return N8C8Groups.(key);
end;;
N8C8Balanced:=function(group,word,cache)
    local found,ans,gens,s,cut;
    found:=LookupDictionary(cache,word);
    if found<>fail then return found;fi;
    if Length(word)<=16 then
        ans:=One(group);gens:=GeneratorsOfGroup(group);
        for s in word do ans:=ans*gens[AbsInt(s)]^SignInt(s);od;
    else
        cut:=QuoInt(Length(word),2);
        ans:=N8C8Balanced(group,word{[1..cut]},cache)
             *N8C8Balanced(group,word{[cut+1..Length(word)]},cache);
    fi;
    AddDictionary(cache,word,ans);
    return ans;
end;;
N8C8Eval:=function(group,word)
    local cache;
    cache:=First(N8C8Caches,row->IsIdenticalObj(row.group,group)).cache;
    return N8C8Balanced(group,word,cache);
end;;
N8C8Fail:=function(message)
    Print("FAIL ",message,"\n");FORCE_QUIT_GAP(1);
end;;
N8C8Roots:=function(c)
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
N8C8Decode:=a->List(a,row->List(row,v->v[1]/v[2]));;
N8C8Poly:=function(coeff,k)
    return coeff[1]+k*coeff[2]+(k*(k-1)/2)*coeff[3];
end;;
N8C8Arithmetic:=function(c)
    local B,H,U,rank,i,j,pivots,pivot,last,part,residual,z,den,nums,equation,
          candidates,values,k,good,eq;
    B:=c.columns;H:=c.H;U:=c.U;rank:=c.rank;
    if U*B<>H or AbsInt(DeterminantMat(U))<>1 then
        N8C8Fail("Hermite transformation");fi;
    pivots:=[];last:=0;
    for i in [1..Length(H)] do
        pivot:=PositionProperty(H[i],x->x<>0);
        if i<=rank then
            if pivot=fail or pivot<=last or H[i][pivot]<0 then
                N8C8Fail("Hermite echelon shape");fi;
            Add(pivots,pivot);last:=pivot;
        elif pivot<>fail then N8C8Fail("Hermite rank");fi;
    od;
    if List(pivots,i->i-1)<>c.pivots or rank<>Length(B) then
        N8C8Fail("degree7 injectivity");fi;
    part:=N8C8Decode(c.particular);residual:=N8C8Decode(c.residual);
    for j in [1..3] do
        if part[j]*B+residual[j]<>c.coefficients[j] or
           ForAny(pivots,i->residual[j][i]<>0) then
            N8C8Fail("rational polynomial reduction");fi;
    od;
    z:=part*U^-1;
    for i in [1..rank] do
        den:=Lcm(List(z,row->DenominatorRat(row[i])));
        nums:=List(z,row->den*row[i]);
        if [den,nums]<>c.congruences[i] then N8C8Fail("integrality congruence");fi;
    od;
    equation:=fail;
    for i in [1..Length(B[1])] do
        eq:=List(residual,row->row[i]);
        if ForAny(eq,x->x<>0) then equation:=eq;break;fi;
    od;
    if equation=fail or c.mode<>"finite_points" or c.period<>fail then
        N8C8Fail("missing quadratic cokernel obstruction");fi;
    candidates:=N8C8Roots(equation);
    if candidates<>c.candidates then N8C8Fail("quadratic root list");fi;
    values:=[];
    for k in candidates do
        good:=ForAll(N8C8Poly(residual,k),x->x=0);
        for i in [1..rank] do
            if not IsInt(N8C8Poly(List(z,row->[row[i]]),k)[1]) then good:=false;fi;
        od;
        if good then Add(values,k);fi;
    od;
    if values<>c.values then N8C8Fail("complete integral parameter list");fi;
end;;

# nq stores its lower central series as suffixes of the defining pcp.
# On gamma_s with 2s>class these coordinates add, so integer row-lattice
# membership is exactly subgroup membership. Check the suffix and support.
N8C8Membership:=function(group,degree,columns,target)
    local pcp,gens,lcs,low,suffix,cut,allcoords,row,rows,rhs,solution,product,i;
    pcp:=Pcp(group);gens:=GeneratorsOfPcp(pcp);
    if gens<>GeneratorsOfGroup(group) or
       ForAny(RelativeOrdersOfPcp(pcp),n->n<>0) then
        N8C8Fail("unexpected ambient pcp");fi;
    lcs:=LowerCentralSeriesOfGroup(group);low:=QuoInt(degree,2)+1;
    if Length(lcs)>degree+1 then N8C8Fail("nilpotency class bound");fi;
    suffix:=GeneratorsOfGroup(lcs[low]);cut:=Length(gens)-Length(suffix);
    if suffix<>gens{[cut+1..Length(gens)]} then
        N8C8Fail("lower central pcp suffix");fi;
    allcoords:=List(Concatenation(columns,[target]),g->ExponentsByPcp(pcp,g));
    for row in allcoords do
        if ForAny(row{[1..cut]},n->n<>0) then
            N8C8Fail("increment outside certified abelian tail");fi;
    od;
    rows:=List(allcoords{[1..Length(columns)]},row->row{[cut+1..Length(gens)]});
    rhs:=Last(allcoords){[cut+1..Length(gens)]};
    solution:=SolutionIntMat(rows,rhs);
    if solution=fail then return false;fi;
    if solution*rows<>rhs then N8C8Fail("integer tail solution");fi;
    product:=One(group);
    for i in [1..Length(columns)] do product:=product*columns[i]^solution[i];od;
    if product<>target then N8C8Fail("tail solution group product");fi;
    return true;
end;;

N8C8Positive:=0;;
for item in N8C8Witnesses do
    Print("BEGIN WITNESS ",N8C8Positive+1,"\n");
    group:=N8C8Group(item[1],item[2]);;
    if Comm(N8C8Eval(group,item[4]),N8C8Eval(group,item[5]))<>
       N8C8Eval(group,item[3]) then N8C8Fail("word witness");fi;
    N8C8Positive:=N8C8Positive+1;
    Print("CHECKED WITNESS ",N8C8Positive,"\n");
od;
N8C8Count:=0;;N8C8Negative:=0;;
for item in N8C8Steps do
    Print("BEGIN LINEAR ",N8C8Count+1,"\n");
    group:=N8C8Group(item[1],item[2]);;
    x:=N8C8Eval(group,item[4]);;y:=N8C8Eval(group,item[5]);;
    base:=Comm(x,y);;delta:=base^-1*N8C8Eval(group,item[3]);;
    corrections:=[];
    for axis in item[6] do
        h:=N8C8Eval(group,axis[2]);
        if axis[1]=0 then Add(corrections,base^-1*Comm(x*h,y));
        else Add(corrections,base^-1*Comm(x,y*h));fi;
    od;
    soluble:=N8C8Membership(group,item[2],corrections,delta);
    if soluble<>item[7] then N8C8Fail("linear branch membership");fi;
    N8C8Count:=N8C8Count+1;
    if not soluble then N8C8Negative:=N8C8Negative+1;fi;
od;
N8C8Samples:=0;;N8C8NoParameters:=0;;hall:=[];;
for item in N8C8Polynomials do
    Print("BEGIN POLYNOMIAL ",N8C8Samples/5+1,"\n");
    c:=item.certificate;
    N8C8Arithmetic(c);
    if Length(c.values)=0 then N8C8NoParameters:=N8C8NoParameters+1;fi;
    group:=N8C8Group(item.rank,7);;
    hall:=List(N8C8Halls[7],w->N8C8Eval(group,w));;
    central:=function(coords)
        local ans,i;
        ans:=One(group);
        for i in [1..Length(coords)] do ans:=ans*hall[i]^coords[i];od;
        return ans;
    end;;
    x0:=N8C8Eval(group,item.x0);;y0:=N8C8Eval(group,item.y0);;
    target:=N8C8Eval(group,item.word);;
    u:=List(N8C8Halls[2],w->N8C8Eval(group,w));;
    v:=List(N8C8Halls[5],w->N8C8Eval(group,w));;
    for sample in item.samples do
        k:=sample[1];coords:=item.vector+k*item.kernel;x:=x0;y:=y0;
        for i in [1..Length(u)] do x:=x*u[i]^coords[i];od;
        for i in [1..Length(v)] do y:=y*v[i]^coords[Length(u)+i];od;
        if x<>N8C8Eval(group,sample[2]) or y<>N8C8Eval(group,sample[3]) then
            N8C8Fail("affine parameter group lifts");fi;
        if Comm(x,y)^-1*target<>central(N8C8Poly(c.coefficients,k)) then
            N8C8Fail("degree7 quadratic coefficients");fi;
        N8C8Samples:=N8C8Samples+1;
    od;
    base:=Comm(x0,y0);axes:=Concatenation(List(N8C8Halls[3],w->[0,w]),
                                      List(N8C8Halls[6],w->[1,w]));;
    for i in [1..Length(axes)] do
        h:=N8C8Eval(group,axes[i][2]);
        if axes[i][1]=0 then change:=base^-1*Comm(x0*h,y0);
        else change:=base^-1*Comm(x0,y0*h);fi;
        if change<>central(c.columns[i]) then N8C8Fail("degree7 correction lattice");fi;
    od;
od;
Print("PASS N8 class8 GAP: ",N8C8Positive," witnesses; ",N8C8Count,
      " linear decisions (",N8C8Negative," negative); ",Length(N8C8Polynomials),
      " polynomial decisions (",N8C8NoParameters," empty); ",N8C8Samples," samples\n");
QUIT_GAP(0);
