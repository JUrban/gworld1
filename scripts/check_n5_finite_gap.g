if LoadPackage("smallgrp")<>true then FORCE_QUIT_GAP(1);fi;
Read("research/certificates/N5-finite/input.g");
Read("research/certificates/N5-finite/witnesses.g");
N5Product:=function(g,gens,coords)
    local x,i;
    x:=One(g);
    for i in [1..Length(gens)] do x:=x*gens[i]^coords[i];od;
    return x;
end;
N5Verify:=function(witness)
    local item,g,pc,zgens,parts,p,corrections,side,images,j,lifts,subgroups,a,b;
    item:=N5FiniteInput[witness[1]];g:=SmallGroup(item[1],item[2]);pc:=Pcgs(g);
    zgens:=List(item[5],v->N5Product(g,pc,v));parts:=item[6][witness[2]];
    p:=witness[3];corrections:=witness[4];subgroups:=[];
    for side in [1,2] do
        images:=List([1..Length(zgens)],j->N5Product(g,zgens,List(p,row->row[j])));
        if side=2 then images:=List([1..Length(zgens)],j->zgens[j]/images[j]);fi;
        lifts:=List(parts[side][4],v->N5Product(g,pc,v));
        for j in [1..Length(lifts)] do lifts[j]:=lifts[j]*N5Product(g,zgens,corrections[side][j]);od;
        Add(subgroups,Subgroup(g,Concatenation(images,lifts)));
    od;
    a:=subgroups[1];b:=subgroups[2];
    if Size(a)=1 or Size(b)=1 or Size(a)*Size(b)<>Size(g) or Size(Intersection(a,b))<>1 then return false;fi;
    if not ForAll(GeneratorsOfGroup(a),x->ForAll(GeneratorsOfGroup(b),y->Comm(x,y)=One(g))) then return false;fi;
    return ClosureGroup(a,b)=g;
end;
for witness in N5FiniteWitnesses do
    if not N5Verify(witness) then FORCE_QUIT_GAP(1);fi;
od;
Print("PASS N5 GAP finite decompositions: ",Length(N5FiniteWitnesses),"\n");
QUIT;
