# Set N8C9Directory before reading this checker.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
Read(Concatenation(N8C9Directory,"/fixtures.g"));
if IsExistingFile(Concatenation(N8C9Directory,"/polynomial-fixtures.g")) then
    Read(Concatenation(N8C9Directory,"/polynomial-fixtures.g"));
else
    Read(Concatenation(N8C9Directory,"/polynomial-fixtures.g.gz"));
fi;
N8C9Groups:=rec();;
N8C9Group:=function(r,c)
    local key;
    key:=Concatenation(String(r),"_",String(c));
    if not IsBound(N8C9Groups.(key)) then
        N8C9Groups.(key):=NilpotentQuotient(FreeGroup(r),c);
    fi;
    return N8C9Groups.(key);
end;;
N8C9Eval:=function(group,word)
    local ans,gens,s;
    ans:=One(group);gens:=GeneratorsOfGroup(group);
    for s in word do ans:=ans*gens[AbsInt(s)]^SignInt(s);od;
    return ans;
end;;
N8C9Fail:=function(message)
    Print("FAIL ",message,"\n");FORCE_QUIT_GAP(1);
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
N8C9Arithmetic:=function(c,require_injective)
    local B,H,U,rank,i,j,pivots,pivot,last,part,residual,z,den,nums,equation,
          candidates,values,k,good,eq;
    B:=c.columns;H:=c.H;U:=c.U;rank:=c.rank;
    if U*B<>H or AbsInt(DeterminantMat(U))<>1 then
        N8C9Fail("Hermite transformation");fi;
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
    z:=part*U^-1;
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

N8C9Positive:=0;;
for item in N8C9Witnesses do
    group:=N8C9Group(item[1],item[2]);;
    if Comm(N8C9Eval(group,item[4]),N8C9Eval(group,item[5]))<>
       N8C9Eval(group,item[3]) then N8C9Fail("word witness");fi;
    N8C9Positive:=N8C9Positive+1;
od;
N8C9Count:=0;;N8C9Negative:=0;;
for item in N8C9Steps do
    group:=N8C9Group(item[1],item[2]);;
    x:=N8C9Eval(group,item[4]);;y:=N8C9Eval(group,item[5]);;
    base:=Comm(x,y);;delta:=base^-1*N8C9Eval(group,item[3]);;
    corrections:=[];
    for axis in item[6] do
        h:=N8C9Eval(group,axis[2]);
        if axis[1]=0 then Add(corrections,base^-1*Comm(x*h,y));
        else Add(corrections,base^-1*Comm(x,y*h));fi;
    od;
    subgroup:=Subgroup(group,corrections);;
    if not IsAbelian(subgroup) then N8C9Fail("nonabelian linear increments");fi;
    soluble:=delta in subgroup;
    if soluble<>item[7] then N8C9Fail("linear branch membership");fi;
    N8C9Count:=N8C9Count+1;
    if not soluble then N8C9Negative:=N8C9Negative+1;fi;
od;
N8C9Samples:=0;;N8C9NoParameters:=0;;hall:=[];;
for item in N8C9Polynomials do
    c:=item.certificate;
    N8C9Arithmetic(c,item.q=4);
    if Length(c.values)=0 then N8C9NoParameters:=N8C9NoParameters+1;fi;
    group:=N8C9Group(item.rank,item.degree);;
    hall:=List(N8C9Halls[item.degree],w->N8C9Eval(group,w));;
    central:=function(coords)
        local ans,i;
        ans:=One(group);
        for i in [1..Length(coords)] do ans:=ans*hall[i]^coords[i];od;
        return ans;
    end;;
    x0:=N8C9Eval(group,item.x0);;y0:=N8C9Eval(group,item.y0);;
    target:=N8C9Eval(group,item.word);;
    u:=List(N8C9Halls[2],w->N8C9Eval(group,w));;
    v:=List(N8C9Halls[item.q+1],w->N8C9Eval(group,w));;
    for sample in item.samples do
        k:=sample[1];coords:=item.vector+k*item.kernel;x:=x0;y:=y0;
        for i in [1..Length(u)] do x:=x*u[i]^coords[i];od;
        for i in [1..Length(v)] do y:=y*v[i]^coords[Length(u)+i];od;
        if x<>N8C9Eval(group,sample[2]) or y<>N8C9Eval(group,sample[3]) then
            N8C9Fail("affine parameter group lifts");fi;
        if Comm(x,y)^-1*target<>central(N8C9Poly(c.coefficients,k)) then
            N8C9Fail("quadratic coefficients");fi;
        N8C9Samples:=N8C9Samples+1;
    od;
    base:=Comm(x0,y0);axes:=Concatenation(List(N8C9Halls[3],w->[0,w]),
                                      List(N8C9Halls[item.q+2],w->[1,w]));;
    for i in [1..Length(axes)] do
        h:=N8C9Eval(group,axes[i][2]);
        if axes[i][1]=0 then change:=base^-1*Comm(x0*h,y0);
        else change:=base^-1*Comm(x0,y0*h);fi;
        if change<>central(c.columns[i]) then N8C9Fail("polynomial correction lattice");fi;
    od;
od;
Print("PASS N8 class9 GAP: ",N8C9Positive," witnesses; ",N8C9Count,
      " linear decisions (",N8C9Negative," negative); ",Length(N8C9Polynomials),
      " polynomial decisions (",N8C9NoParameters," empty); ",N8C9Samples," samples\n");
QUIT_GAP(0);
