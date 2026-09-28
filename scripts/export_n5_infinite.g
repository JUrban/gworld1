Read("scripts/n5_infinite_examples.g");
N5ExportInfinite:=function(m,kind,expected)
    local g,z,zpcp,zgens,orders,positions,projection,k,isoK,subs,branches,
          y1,y2,x1,x2,side,parts,iso,fp,lifts,rels,e,defects,rel,row,s,
          value,coords,pc;
    g:=N5Example(m,kind);pc:=Pcp(g);z:=Centre(g);zpcp:=Pcp(z,"snf");
    orders:=RelativeOrdersOfPcp(zpcp);
    positions:=Concatenation(Filtered([1..Length(orders)],i->orders[i]=0),Filtered([1..Length(orders)],i->orders[i]<>0));
    orders:=orders{positions};zgens:=GeneratorsOfPcp(zpcp){positions};
    projection:=NaturalHomomorphismByNormalSubgroup(g,z);k:=Image(projection);
    if Size(k)=infinity then Error("example must have finite central quotient");fi;
    isoK:=IsomorphismPermGroup(k);projection:=projection*isoK;k:=Image(projection);
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
                Add(e,row);value:=N5Word(g,lifts,rel);
                if not value in z then Error("noncentral defect");fi;
                coords:=ExponentsByPcp(zpcp,value);Add(defects,coords{positions});
            od;
            Add(parts,[e,defects,0,List(lifts,a->ExponentsByPcp(pc,a)),rels]);
        od;
        Add(branches,parts);
    od;od;
    Print("Example m=",m," kind=",kind,"; Hirsch=",HirschLength(g),"; centre orders=",orders,"; quotient size=",Size(k),"; branches=",Length(branches),"\n");
    return [m,kind,expected,orders,List(zgens,a->ExponentsByPcp(pc,a)),branches];
end;
N5Exported:=[];
for parameters in [[1,0,1],[2,0,0],[3,0,0],[4,0,0],[2,1,1],[2,2,1],[3,2,1]] do
    Add(N5Exported,CallFuncList(N5ExportInfinite,parameters));
    stream:=OutputTextFile("research/certificates/N5-infinite/input.json",false);
    SetPrintFormattingStatus(stream,false);PrintTo(stream,N5Exported,"\n");CloseStream(stream);
od;
Print("PASS N5 infinite group exports: ",Length(N5Exported),"\n");
QUIT;
