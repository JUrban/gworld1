if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
Read("research/certificates/N8-class7/fixtures.g");
Read("research/certificates/N8-class7/quadratic-fixtures.g");
N8C7Groups:=rec();;
N8C7Group:=function(r,c)
    local key;
    key:=Concatenation(String(r),"_",String(c));
    if not IsBound(N8C7Groups.(key)) then
        N8C7Groups.(key):=NilpotentQuotient(FreeGroup(r),c);
    fi;
    return N8C7Groups.(key);
end;;
N8C7Eval:=function(group,word)
    local ans,gens,s;
    ans:=One(group);gens:=GeneratorsOfGroup(group);
    for s in word do ans:=ans*gens[AbsInt(s)]^SignInt(s);od;
    return ans;
end;;
N8C7Fail:=function(message)
    Print("FAIL ",message,"\n");FORCE_QUIT_GAP(1);
end;;
N8C7Roots:=function(c)
    local a,b,d,delta,s,roots,n;
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
N8C7NegArithmetic:=0;;
for item in N8C7Arithmetic do
    A:=item[1];D:=item[2];S:=item[3];T:=item[4];coeff:=item[5];rank:=item[6];
    if S*A*T<>D or AbsInt(DeterminantMat(S))<>1 or
       AbsInt(DeterminantMat(T))<>1 then N8C7Fail("Smith certificate");fi;
    for i in [1..Length(D)] do
        for j in [1..Length(D[1])] do
            if i<>j and D[i][j]<>0 then N8C7Fail("nondiagonal Smith matrix");fi;
            if i=j and ((i<=rank)<>(D[i][j]<>0)) then
                N8C7Fail("Smith rank");
            fi;
        od;
    od;
    transformed:=List(coeff,v->S*v);;
    equation:=fail;
    for i in [rank+1..Length(A)] do
        row:=List(transformed,v->v[i]);
        if ForAny(row,n->n<>0) then equation:=row;break;fi;
    od;
    if equation<>fail then
        candidates:=N8C7Roots(equation);
        if candidates<>item[7] or item[8]<>fail then N8C7Fail("integer roots");fi;
    else
        exponent:=1;
        for i in [1..rank] do exponent:=Lcm(exponent,AbsInt(D[i][i]));od;
        if item[8]<>2*exponent or item[7]<>fail then N8C7Fail("period");fi;
        candidates:=[0..2*exponent-1];
    fi;
    selected:=fail;
    for k in candidates do
        rhs:=transformed[1]+k*transformed[2]+(k*(k-1)/2)*transformed[3];
        good:=true;
        for i in [1..Length(rhs)] do
            if i<=rank then
                if rhs[i] mod D[i][i]<>0 then good:=false;fi;
            elif rhs[i]<>0 then good:=false;fi;
        od;
        if good then selected:=k;break;fi;
    od;
    if selected<>item[9] then N8C7Fail("quadratic membership decision");fi;
    if selected=fail then N8C7NegArithmetic:=N8C7NegArithmetic+1;fi;
od;
N8C7Positive:=0;;
for item in N8C7Witnesses do
    group:=N8C7Group(item[1],item[2]);;
    if Comm(N8C7Eval(group,item[4]),N8C7Eval(group,item[5]))<>
       N8C7Eval(group,item[3]) then N8C7Fail("word witness");fi;
    N8C7Positive:=N8C7Positive+1;
od;
N8C7Count:=0;;N8C7Negative:=0;;
for item in N8C7Steps do
    group:=N8C7Group(item[1],item[2]);;
    x:=N8C7Eval(group,item[4]);;y:=N8C7Eval(group,item[5]);;
    base:=Comm(x,y);;delta:=base^-1*N8C7Eval(group,item[3]);;
    corrections:=[];
    for axis in item[6] do
        h:=N8C7Eval(group,axis[2]);
        if axis[1]=0 then Add(corrections,base^-1*Comm(x*h,y));
        else Add(corrections,base^-1*Comm(x,y*h));fi;
    od;
    subgroup:=Subgroup(group,corrections);;
    if not IsAbelian(subgroup) then N8C7Fail("linear tail nonabelian");fi;
    soluble:=delta in subgroup;
    if soluble<>item[7] then N8C7Fail("linear tail membership");fi;
    N8C7Count:=N8C7Count+1;
    if not soluble then N8C7Negative:=N8C7Negative+1;fi;
od;
group:=N8C7Group(2,7);;
N8C7Hall:=List(N8C7Hall7,w->N8C7Eval(group,w));;
N8C7Central:=function(coords)
    local ans,i;
    ans:=One(group);
    for i in [1..Length(coords)] do ans:=ans*N8C7Hall[i]^coords[i];od;
    return ans;
end;;
N8C7Samples:=0;;
for item in N8C7Quadratics do
    target:=N8C7Eval(group,item[1]);;
    x0:=N8C7Eval(group,item[2]);;y0:=N8C7Eval(group,item[3]);;
    for sample in item[9] do
        k:=sample[1];v:=item[4]+k*item[5];x:=x0;y:=y0;
        for i in [1..Length(item[6])] do x:=x*N8C7Eval(group,item[6][i])^v[i];od;
        for i in [1..Length(item[7])] do
            y:=y*N8C7Eval(group,item[7][i])^v[Length(item[6])+i];
        od;
        if x<>N8C7Eval(group,sample[2]) or y<>N8C7Eval(group,sample[3]) then
            N8C7Fail("parameterized factor lifts");
        fi;
        base:=Comm(x,y);delta:=base^-1*target;
        coeff:=item[10];rhs:=coeff[1]+k*coeff[2]+(k*(k-1)/2)*coeff[3];
        if delta<>N8C7Central(rhs) then N8C7Fail("quadratic interpolation");fi;
        for i in [1..Length(item[8])] do
            axis:=item[8][i];h:=N8C7Eval(group,axis[2]);
            if axis[1]=0 then change:=base^-1*Comm(x*h,y);
            else change:=base^-1*Comm(x,y*h);fi;
            if change<>N8C7Central(item[11][i]) then N8C7Fail("fixed final lattice");fi;
        od;
        N8C7Samples:=N8C7Samples+1;
    od;
od;
# Independently confirm that the four Lie columns have no integral relation
# using the torsion-free class-six quotient and its own pc coordinates.
group:=N8C7Group(2,6);;
u:=N8C7Eval(group,N8C7Minor[1][1]);;
v:=N8C7Eval(group,N8C7Minor[2][1]);;w:=N8C7Eval(group,N8C7Minor[2][2]);;
columns:=[Comm(v,w)];;
for word in N8C7Minor[3] do Add(columns,Comm(u,N8C7Eval(group,word)));od;
if HirschLength(Subgroup(group,columns))<>4 then N8C7Fail("degree-six injection");fi;
Print("PASS N8 class7 GAP: ",N8C7Positive," witnesses; ",N8C7Count,
      " linear steps (",N8C7Negative," negative); ",Length(N8C7Arithmetic),
      " arithmetic cases (",N8C7NegArithmetic," negative); ",N8C7Samples,
      " parameter samples\n");
QUIT;
