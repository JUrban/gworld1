if LoadPackage("polycyclic")<>true then FORCE_QUIT_GAP(1);fi;
Read("research/certificates/N5-central/fixtures.g");
N5Eval:=function(gens,v)
    local g,i;
    g:=One(gens[1]);
    for i in [1..Length(gens)] do g:=g*gens[i]^v[i];od;
    return g;
end;
checked:=0;
for fixture in N5Fixtures do
    g:=AbelianPcpGroup(fixture[1]);;gens:=GeneratorsOfGroup(g);;p:=fixture[2];;
    images:=List([1..Length(gens)],j->N5Eval(gens,List(p,row->row[j])));;
    others:=List([1..Length(gens)],j->gens[j]/images[j]);;
    a:=Subgroup(g,images);;b:=Subgroup(g,others);;
    if Size(Intersection(a,b))<>1 or ClosureGroup(a,b)<>g then FORCE_QUIT_GAP(1);fi;
    if fixture[4][1]=1 and Size(a)=1 then FORCE_QUIT_GAP(1);fi;
    if fixture[4][2]=1 and Size(b)=1 then FORCE_QUIT_GAP(1);fi;
    for cc in fixture[3] do
        if cc[1]=1 then factor:=a;else factor:=b;fi;
        dz:=Subgroup(g,List(gens,x->x^cc[3]));;
        if not N5Eval(gens,cc[2]) in ClosureGroup(factor,dz) then FORCE_QUIT_GAP(1);fi;
    od;
    checked:=checked+1;
od;
Print("PASS N5 GAP central projections: ",checked,"\n");
QUIT;
