# F20: exact integral first-homology tests in finite regular covers.
# No assertion of completeness is made by the final process marker.
# The relators are ONLY the weight-c Hall commutators, without definitions
# for new generators. Commutator convention: [u,v]=u^-1 v^-1 u v.
if not IsBound(F20CoverOrders) then F20CoverOrders:=[1..32];fi;
if not IsBound(F20CoverWeights) then F20CoverWeights:=[5,6];fi;
if not IsBound(F20CoverOutput) then
    F20CoverOutput:="research/certificates/F20-cover-homology/checks-v2.json";
fi;
F20CoverFail:=function(s) Print("FAIL ",s,"\n");FORCE_QUIT_GAP(1);end;;
F20CoverHall:=function(c)
    local F,g,h,w,i,j,size;
    F:=FreeGroup(2);g:=GeneratorsOfGroup(F);
    h:=[rec(weight:=1,parents:=[],word:=g[1]),
        rec(weight:=1,parents:=[],word:=g[2])];
    for w in [2..c+1] do
        size:=Length(h);
        for i in [1..size] do for j in [1..i-1] do
            if h[i].weight+h[j].weight=w and
               (Length(h[i].parents)=0 or h[i].parents[2]<=j) then
                Add(h,rec(weight:=w,parents:=[i,j],
                          word:=Comm(h[i].word,h[j].word)));
            fi;
        od;od;
    od;
    return rec(hall:=h,
        relators:=List(Filtered(h,t->t.weight=c),t->LetterRepAssocWord(t.word)),
        targets:=List(Filtered(h,t->t.weight=c+1),t->LetterRepAssocWord(t.word)));
end;;
F20CoverWalk:=function(trans,word,start)
    local n,v,row,s,j,next;
    n:=Length(trans[1]);v:=start;row:=List([1..2*n],i->0);
    for s in word do
        j:=AbsInt(s);
        if s>0 then
            row[2*(v-1)+j]:=row[2*(v-1)+j]+1;
            v:=trans[j][v];
        else
            next:=trans[j+2][v];
            row[2*(next-1)+j]:=row[2*(next-1)+j]-1;
            v:=next;
        fi;
    od;
    if v<>start then F20CoverFail("word does not close in finite quotient");fi;
    return row;
end;;
F20CoverRemainder:=function(basis,row)
    local v,h,p,q;
    v:=ShallowCopy(row);
    for h in basis do
        p:=PositionProperty(h,x->x<>0);
        q:=QuoInt(v[p],h[p]);
        v:=v-q*h;
    od;
    return v;
end;;
F20CoverTest:=function(trans,data)
    local n,rows,w,v,basis,targets,residues;
    n:=Length(trans[1]);rows:=[];
    for w in data.relators do for v in [1..n] do
        Add(rows,F20CoverWalk(trans,w,v));
    od;od;
    if Length(rows)=0 then basis:=[];
    else basis:=Filtered(HermiteNormalFormIntegerMat(rows),h->ForAny(h,x->x<>0));fi;
    targets:=List(data.targets,w->F20CoverWalk(trans,w,1));
    residues:=List(targets,w->F20CoverRemainder(basis,w));
    return rec(rank:=Length(basis),betti:=n+1-Length(basis),
               surviving:=Filtered([1..Length(residues)],i->ForAny(residues[i],x->x<>0)),
               residues:=residues);
end;;
F20CoverMain:=function()
    local out,first,n,id,Q,g,elems,trans,c,data,answer,total,hits,allData,
          control,controls,F,a,b,w,genid,entry;
    if IsExistingFile(F20CoverOutput) then F20CoverFail("output already exists");fi;
    out:=OutputTextFile(F20CoverOutput,false);SetPrintFormattingStatus(out,false);
    PrintTo(out,"[\n");first:=true;total:=0;hits:=0;controls:=0;
    # Empty presentation and one commutator: a nonzero cycle must survive.
    trans:=[[2,1],[1,2],[2,1],[1,2]];
    F:=FreeGroup(2);a:=F.1;b:=F.2;
    control:=rec(relators:=[],targets:=[LetterRepAssocWord(Comm(b,a))]);
    answer:=F20CoverTest(trans,control);
    if answer.surviving<>[1] or answer.betti<>3 then F20CoverFail("free-cover control");fi;
    Add(control.relators,control.targets[1]);
    answer:=F20CoverTest(trans,control);
    if answer.surviving<>[] or answer.betti<>2 then F20CoverFail("torus-cover control");fi;
    controls:=2;
    # Integral, not rational, membership: 2[z] does not kill [z].
    control.relators:=[Concatenation(control.targets[1],control.targets[1])];
    answer:=F20CoverTest(trans,control);
    if answer.surviving<>[1] then F20CoverFail("torsion control");fi;
    controls:=controls+1;
    allData:=List(F20CoverWeights,F20CoverHall);
    for n in F20CoverOrders do
        for id in [1..NumberSmallGroups(n)] do
            Q:=SmallGroup(n,id);
            if not IsNilpotentGroup(Q) then continue;fi;
            g:=ShallowCopy(MinimalGeneratingSet(Q));
            if Length(g)>2 then continue;fi;
            while Length(g)<2 do Add(g,One(Q));od;
            if Size(Group(g))<>n then F20CoverFail("generation");fi;
            elems:=Elements(Q);
            trans:=List(Concatenation(g,List(g,x->x^-1)),
                        s->List(elems,x->Position(elems,x*s)));
            genid:=List(g,x->Position(elems,x));
            for entry in [1..Length(allData)] do
                c:=F20CoverWeights[entry];data:=allData[entry];
                if NilpotencyClassOfGroup(Q)>=c then continue;fi;
                answer:=F20CoverTest(trans,data);
                if c<=5 and answer.surviving<>[] then F20CoverFail("known positive control");fi;
                total:=total+1;hits:=hits+Length(answer.surviving);
                if not first then PrintTo(out,",\n");fi;first:=false;
                PrintTo(out,"{\"order\":",n,",\"small_group_id\":",id,
                    ",\"weight\":",c,",\"generators\":",genid,
                    ",\"transitions\":",trans,",\"relation_rank\":",answer.rank,
                    ",\"betti\":",answer.betti,",\"surviving_targets\":",answer.surviving);
                if answer.surviving<>[] then
                    PrintTo(out,",\"residues\":",answer.residues);
                fi;
                PrintTo(out,"}");
                Print("F20 COVER [",n,",",id,"] c=",c," betti=",answer.betti,
                      " survivors=",answer.surviving,"\n");
            od;
        od;
    od;
    PrintTo(out,"\n]\n");CloseStream(out);
    Print("PASS bounded F20 cover homology: ",total," covers; ",controls,
          " controls; ",hits," surviving target records (not a theorem marker)\n");
end;;
F20CoverMain();
QUIT_GAP(0);
