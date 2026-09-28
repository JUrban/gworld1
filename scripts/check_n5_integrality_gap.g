if LoadPackage("polycyclic")<>true then FORCE_QUIT_GAP(1);fi;
Read("research/certificates/N5-integrality/fixtures.g");
N5AuditEval:=function(gens,v)
    local value,i;
    value:=One(gens[1]);
    for i in [1..Length(gens)] do value:=value*gens[i]^v[i];od;
    return value;
end;
N5AuditProjection:=function(fixture)
    local g,gens,p,images,others,a,b,cc,factor,dz;
    g:=AbelianPcpGroup(fixture[1]);gens:=GeneratorsOfGroup(g);p:=fixture[2];
    images:=List([1..Length(gens)],j->N5AuditEval(gens,List(p,row->row[j])));
    others:=List([1..Length(gens)],j->gens[j]/images[j]);
    a:=Subgroup(g,images);b:=Subgroup(g,others);
    if Size(Intersection(a,b))<>1 or ClosureGroup(a,b)<>g then Error("bad splitting");fi;
    if fixture[4][1]=1 and Size(a)=1 then Error("first factor trivial");fi;
    if fixture[4][2]=1 and Size(b)=1 then Error("second factor trivial");fi;
    for cc in fixture[3] do
        if cc[1]=1 then factor:=a;else factor:=b;fi;
        dz:=Subgroup(g,List(gens,x->x^cc[3]));
        if not N5AuditEval(gens,cc[2]) in ClosureGroup(factor,dz) then Error("constraint failed");fi;
    od;
end;
N5AuditLifts:=function(fixture)
    local g,gens,e,defects,side,p,images,part,zs,ok,i,j,value,exists,corrections;
    g:=AbelianPcpGroup(fixture[1]);gens:=GeneratorsOfGroup(g);
    e:=fixture[2];defects:=fixture[3];side:=fixture[4];p:=fixture[5];
    images:=List([1..Length(gens)],j->N5AuditEval(gens,List(p,row->row[j])));
    if side=2 then images:=List([1..Length(gens)],j->gens[j]/images[j]);fi;
    part:=Subgroup(g,images);exists:=false;
    for zs in Tuples(Elements(g),Length(e[1])) do
        ok:=true;
        for i in [1..Length(e)] do
            value:=N5AuditEval(gens,defects[i]);
            for j in [1..Length(zs)] do value:=value*zs[j]^e[i][j];od;
            if not value in part then ok:=false;break;fi;
        od;
        if ok then exists:=true;break;fi;
    od;
    if exists<>(fixture[6]=1) then Error("direct lift enumeration disagrees");fi;
    if exists then
        corrections:=List(fixture[7],v->N5AuditEval(gens,v));
        for i in [1..Length(e)] do
            value:=N5AuditEval(gens,defects[i]);
            for j in [1..Length(corrections)] do value:=value*corrections[j]^e[i][j];od;
            if not value in part then Error("constructed corrections failed");fi;
        od;
    fi;
end;
Perform(N5IntegrityFixtures,N5AuditProjection);
Perform(N5LiftFixtures,N5AuditLifts);
Print("PASS N5 GAP integrality audit: ",Length(N5IntegrityFixtures)," projections; ",Length(N5LiftFixtures)," direct lift decisions\n");
QUIT;
