# Independent nq checks of saved homogeneous kernels and quadratic obstructions.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
Read("research/certificates/N8-class8/kernel-fixtures.g");
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
N8KHalls:=function(group,r,d)
    local words;
    words:=First(N8C8KernelHalls,row->row[1]=[r,d])[2];
    return List(words,w->N8KEval(group,w));
end;;
N8KLift:=function(group,r,d,coords)
    local h,ans,i;
    h:=N8KHalls(group,r,d);ans:=One(group);
    for i in [1..Length(h)] do ans:=ans*h[i]^coords[i];od;
    return ans;
end;;
N8KFail:=function(message)
    Print("FAIL ",message,"\n");FORCE_QUIT_GAP(1);
end;;
N8KCount:=0;;
for row in N8C8KernelRows do
    r:=row[1];p:=row[2];q:=row[3];j:=row[4];
    group:=N8KGroup(r,p+q+j);
    c:=N8KLift(group,r,p,row[5]);d:=N8KLift(group,r,q,row[6]);
    columns:=Concatenation(List(N8KHalls(group,r,p+j),u->Comm(u,d)),
                           List(N8KHalls(group,r,q+j),v->Comm(c,v)));
    subgroup:=Subgroup(group,columns);
    if not IsAbelian(subgroup) or Length(columns)-HirschLength(subgroup)<>row[7] then
        N8KFail("homogeneous correction kernel rank");fi;
    N8KCount:=N8KCount+1;
od;
N8OCount:=0;;
for row in N8C8ObstructionRows do
    r:=row[1];group:=N8KGroup(r,7);
    z:=N8KLift(group,r,1,row[2]);t:=N8KLift(group,r,2,row[3]);
    d:=N8KLift(group,r,4,row[4]);q:=N8KLift(group,r,7,row[5]);
    if Comm(t,Comm(t,Comm(z,t)))<>q then N8KFail("quadratic obstruction word");fi;
    columns:=Concatenation(List(N8KHalls(group,r,3),u->Comm(u,d)),
                           List(N8KHalls(group,r,6),v->Comm(z,v)));
    before:=HirschLength(Subgroup(group,columns));
    after:=HirschLength(Subgroup(group,Concatenation(columns,[q])));
    if [before,after]<>row[6] or before<>Length(columns) or after<>before+1 then
        N8KFail("nonzero rational cokernel");fi;
    N8OCount:=N8OCount+1;
od;
Print("PASS N8 class8 kernel GAP: ",N8KCount," kernels; ",N8OCount," quadratic obstructions\n");
QUIT_GAP(0);
