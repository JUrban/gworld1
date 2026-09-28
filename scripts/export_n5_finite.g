if LoadPackage("smallgrp")<>true then FORCE_QUIT_GAP(1);fi;
Reset(GlobalMersenneTwister,9282614);
N5Product:=function(g,gens,coords)
    local x,i;
    x:=One(g);
    for i in [1..Length(gens)] do x:=x*gens[i]^coords[i];od;
    return x;
end;
N5Word:=function(g,gens,word)
    local x,s;
    x:=One(g);
    for s in word do x:=x*gens[AbsInt(s)]^SignInt(s);od;
    return x;
end;
N5Export:=function(order,id)
    local g,z,zgens,orders,tuples,zelements,projection,k,subs,branches,
          y1,y2,x1,x2,side,parts,iso,fp,lifts,rels,e,defects,rel,row,s,
          value,pos,expected,pc;
    g:=SmallGroup(order,id);
    if not IsNilpotentGroup(g) then return fail;fi;
    pc:=Pcgs(g);z:=Centre(g);zgens:=IndependentGeneratorsOfAbelianGroup(z);
    orders:=List(zgens,Order);tuples:=Cartesian(List(orders,d->[0..d-1]));
    zelements:=List(tuples,v->N5Product(g,zgens,v));
    if Length(Set(zelements))<>Size(z) then Error("central basis");fi;
    projection:=NaturalHomomorphismByNormalSubgroup(g,z);k:=Image(projection);
    subs:=NormalSubgroups(k);branches:=[];
    for y1 in subs do for y2 in subs do
        if Size(y1)*Size(y2)<>Size(k) or Size(Intersection(y1,y2))<>1 then continue;fi;
        if not ForAll(GeneratorsOfGroup(y1),a->ForAll(GeneratorsOfGroup(y2),b->Comm(a,b)=One(k))) then continue;fi;
        x1:=PreImage(projection,y1);x2:=PreImage(projection,y2);
        if not ForAll(GeneratorsOfGroup(x1),a->ForAll(GeneratorsOfGroup(x2),b->Comm(a,b)=One(g))) then continue;fi;
        parts:=[];
        for side in [y1,y2] do
            if Size(side)=1 then Add(parts,[[],[],1,[],[]]);continue;fi;
            iso:=IsomorphismFpGroup(side);fp:=Image(iso);
            lifts:=List(GeneratorsOfGroup(fp),a->PreImagesRepresentative(projection,PreImagesRepresentative(iso,a)));
            rels:=List(RelatorsOfFpGroup(fp),LetterRepAssocWord);e:=[];defects:=[];
            for rel in rels do
                row:=List(lifts,a->0);
                for s in rel do row[AbsInt(s)]:=row[AbsInt(s)]+SignInt(s);od;
                Add(e,row);value:=N5Word(g,lifts,rel);pos:=Position(zelements,value);
                if pos=fail then Error("noncentral relator defect");fi;
                Add(defects,tuples[pos]);
            od;
            Add(parts,[e,defects,0,List(lifts,a->ExponentsOfPcElement(pc,a)),rels]);
        od;
        Add(branches,parts);
    od;od;
    if Length(DirectFactorsOfGroup(g))>1 then expected:=1;else expected:=0;fi;
    return [order,id,expected,orders,List(zgens,a->ExponentsOfPcElement(pc,a)),branches];
end;
N5Exported:=[];
for order in [4,6,8,9,12,16,27,32] do
    for id in [1..NumberSmallGroups(order)] do
        item:=N5Export(order,id);
        if item=fail then continue;fi;
        Add(N5Exported,item);
        stream:=OutputTextFile("research/certificates/N5-finite/input.json",false);
        SetPrintFormattingStatus(stream,false);PrintTo(stream,N5Exported,"\n");CloseStream(stream);
        Print("Exported SmallGroup(",order,",",id,"): ",Length(item[6])," lifting branches; oracle ",item[3],"\n");
    od;
od;
Print("PASS N5 finite group exports: ",Length(N5Exported),"\n");
QUIT;
