# Set N8C9Directory to the certificate directory before reading this script.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
Read(Concatenation(N8C9Directory,"/kernel-fixtures.g"));
N8KGroups:=rec();;
N8KGroup:=function(r,c)
    local key;
    key:=Concatenation(String(r),"_",String(c));
    if not IsBound(N8KGroups.(key)) then
        N8KGroups.(key):=NilpotentQuotient(FreeGroup(r),c);
    fi;
    return N8KGroups.(key);
end;;
N8KEval:=function(group,word)
    local ans,gens,s;
    ans:=One(group);gens:=GeneratorsOfGroup(group);
    for s in word do ans:=ans*gens[AbsInt(s)]^SignInt(s);od;
    return ans;
end;;
N8KHalls:=function(group,d)
    return List(N8C9Halls[d],w->N8KEval(group,w));
end;;
N8KLift:=function(group,d,coords)
    local h,ans,i;
    h:=N8KHalls(group,d);ans:=One(group);
    for i in [1..Length(h)] do
        if coords[i]<>0 then ans:=ans*h[i]^coords[i];fi;
    od;
    return ans;
end;;
N8KDelta:=function(z,t,n)
    local i;
    for i in [1..n] do t:=Comm(z,t);od;
    return t;
end;;
N8KFail:=function(message)
    Print("FAIL ",message,"\n");FORCE_QUIT_GAP(1);
end;;
N8KCount:=0;;r:=N8C9KernelData.rank;;
for row in N8C9KernelData.records do
    p:=row.p;q:=row.q;j:=row.j;group:=N8KGroup(r,p+q+j);
    c:=N8KLift(group,p,row.C);d:=N8KLift(group,q,row.D);
    columns:=Concatenation(List(N8KHalls(group,p+j),u->Comm(u,d)),
                           List(N8KHalls(group,q+j),v->Comm(c,v)));
    subgroup:=Subgroup(group,columns);
    if not IsAbelian(subgroup) or Length(columns)-HirschLength(subgroup)<>row.nullity then
        N8KFail("homogeneous correction kernel rank");fi;
    if IsBound(row.predicted_direction) then
        product:=One(group);
        for i in [1..Length(columns)] do
            product:=product*columns[i]^row.predicted_direction[i];
        od;
        if product<>One(group) then N8KFail("predicted kernel direction");fi;
    fi;
    N8KCount:=N8KCount+1;
od;
N8OCount:=0;;
for row in N8C9KernelData.obstructions do
    group:=N8KGroup(r,9);
    z:=N8KLift(group,1,row.z);t:=N8KLift(group,2,row.T);
    d:=N8KLift(group,6,row.D);quad:=N8KLift(group,9,row.Q);
    v0:=Comm(t,N8KDelta(z,t,3))*Comm(N8KDelta(z,t,1),N8KDelta(z,t,2))^-1;
    if Comm(t,v0)<>quad then N8KFail("quadratic obstruction word");fi;
    columns:=Concatenation(List(N8KHalls(group,3),u->Comm(u,d)),
                           List(N8KHalls(group,8),v->Comm(z,v)));
    before:=HirschLength(Subgroup(group,columns));
    after:=HirschLength(Subgroup(group,Concatenation(columns,[quad])));
    if [before,after]<>row.ranks or after<>before+1 then
        N8KFail("nonzero rational cokernel");fi;
    N8OCount:=N8OCount+1;
od;
Print("PASS N8 class9 kernel GAP: ",r,"; ",N8KCount," kernels; ",N8OCount," obstructions\n");
QUIT_GAP(0);
