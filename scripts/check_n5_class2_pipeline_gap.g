# Loaded after the unchanged N5 rational Lie replay functions and fresh inputs.
if LoadPackage("nq")<>true or LoadPackage("polycyclic")<>true then Error("packages");fi;

N5C2Sat:=function(rows)
    local sm;
    if Length(rows)=0 or RankMat(rows)=0 then return [];fi;
    sm:=SmithNormalFormIntegerMatTransforms(rows);
    if sm.rowtrans*rows*sm.coltrans<>sm.normal then Error("Smith identity");fi;
    return (sm.coltrans^-1){[1..sm.rank]};
end;
N5C2Primitive:=function(rows)
    local sm,i;
    if Length(rows)=0 then return true;fi;
    sm:=SmithNormalFormIntegerMat(rows);
    return ForAll([1..RankMat(rows)],i->AbsInt(sm[i][i])=1);
end;
N5C2Word:=function(g,gens,coords)
    local value,i;
    value:=One(g);
    for i in [1..Length(gens)] do value:=value*gens[i]^coords[i];od;
    return value;
end;
N5C2Replay:=function(item)
    local data,r,s,n,f,x,rels,i,j,k,w,pres,ep,g,gens,zz,
          branch,a,b,q,rows,side,rank,idx,cons,vec,pairs,bases,
          w1,w2,joined,possible,require1,require2,rr,factors,
          aa,bb,sub,projections,masks,mask,pp,seen,saved,full,
          witness,verified,classes;
    data:=item.result;r:=data.quotient_rank;s:=data.center_rank;n:=r+s;
    if n=0 then
        if data.answer<>false then Error("trivial group");fi;
        Print("GAP class2 trivial group\n");return [0,0];
    fi;
    f:=FreeGroup(n);x:=GeneratorsOfGroup(f);rels:=[];
    for i in [1..n] do for j in [i+1..n] do
        w:=Comm(x[i],x[j]);
        if j<=r then for k in [1..s] do w:=w*x[r+k]^-data.beta[i][j][k];od;fi;
        Add(rels,w);
    od;od;
    if r=0 then
        g:=AbelianPcpGroup(List([1..s],i->0));gens:=GeneratorsOfGroup(g);
    else
        pres:=f/rels;ep:=NqEpimorphismNilpotentQuotient(pres,2);g:=Image(ep);
        gens:=List(GeneratorsOfGroup(pres),y->Image(ep,y));
    fi;
    if HirschLength(g)<>n or Size(TorsionSubgroup(g))<>1 then Error("group model");fi;
    zz:=Subgroup(g,gens{[r+1..n]});
    if zz<>Centre(g) then Error("full center");fi;
    verified:=0;
    for branch in data.branches do
        a:=TransposedMat(branch.quotient_bases[1]);
        b:=TransposedMat(branch.quotient_bases[2]);
        q:=TransposedMat(branch.quotient_projection);
        if r>0 then
            if Length(a)<>RankMat(q) or Length(b)<>r-RankMat(q) then Error("rational support ranks");fi;
            for rows in a do if rows*q<>rows then Error("first support");fi;od;
            for rows in b do if rows*q<>List([1..r],i->0) then Error("second support");fi;od;
            if not N5C2Primitive(a) or not N5C2Primitive(b) then Error("unsaturated supports");fi;
            idx:=AbsInt(DeterminantMat(Concatenation(a,b)));
        else idx:=1;fi;
        if idx<>branch.quotient_index then Error("support index");fi;
        if idx<>1 then
            if branch.outcome<>"quotient_lattice_obstruction" then Error("wrong quotient rejection");fi;
            verified:=verified+1;continue;
        fi;
        cons:=[];
        for side in [1,2] do
            if side=1 then bases:=a;else bases:=b;fi;
            for i in [1..Length(bases)] do for j in [i+1..Length(bases)] do
                vec:=List([1..s],k->Sum([1..r],ii->Sum([1..r],jj->bases[i][ii]*bases[j][jj]*data.beta[ii][jj][k])));
                Add(cons,[side,vec,0]);
                aa:=N5C2Word(g,gens,Concatenation(bases[i],List([1..s],k->0)));
                bb:=N5C2Word(g,gens,Concatenation(bases[j],List([1..s],k->0)));
                if Comm(aa,bb)<>N5C2Word(g,gens,Concatenation(List([1..r],k->0),vec)) then Error("actual group defect");fi;
            od;od;
        od;
        if cons<>branch.constraints then Error("central constraints");fi;
        w1:=N5C2Sat(List(Filtered(cons,v->v[1]=1),v->v[2]));
        w2:=N5C2Sat(List(Filtered(cons,v->v[1]=2),v->v[2]));
        joined:=Concatenation(w1,w2);
        possible:=N5LieRank(joined)=Length(joined) and N5C2Primitive(joined);
        require1:=Length(a)=0;require2:=Length(b)=0;
        if possible then
            possible:=ForAny([Length(w1)..s-Length(w2)],rr->
                             (not require1 or rr>0) and (not require2 or rr<s));
        fi;
        if possible<>(branch.outcome="decomposition") then Error("independent central decision");fi;
        if possible then
            factors:=List(branch.factor_generators,vs->Subgroup(g,List(vs,v->N5C2Word(g,gens,v))));
            aa:=factors[1];bb:=factors[2];
            if Size(aa)=1 or Size(bb)=1 or Size(Intersection(aa,bb))<>1 or ClosureGroup(aa,bb)<>g then
                Error("actual direct factors");fi;
            if not ForAll(GeneratorsOfGroup(aa),xx->ForAll(GeneratorsOfGroup(bb),yy->Comm(xx,yy)=One(g))) then Error("cross commutators");fi;
        fi;
        verified:=verified+1;
    od;
    if not data.answer then
        # The Lie replay checks that these are indecomposable rational
        # factors. Exhaust every partition and compare distinct supports.
        projections:=data.rational.projections;
        masks:=Tuples([0,1],Length(projections));seen:=[];
        for mask in masks do
            pp:=NullMat(n,n,Rationals);
            for i in [1..Length(mask)] do pp:=pp+mask[i]*projections[i];od;
            if r=0 then q:=[];else q:=pp{[1..r]}{[1..r]};fi;
            AddSet(seen,q);
        od;
        saved:=Set(List(data.branches,v->v.quotient_projection));
        if seen<>saved then Error("incomplete negative branch list");fi;
    fi;
    if data.answer<>item.expected then Error("expected result");fi;
    Print("GAP class2 ",item.name,": ",data.answer,"; ",verified," branch decisions\n");
    if data.answer then return [verified,1];else return [verified,0];fi;
end;

N5C2LieCounts:=List(N5LieFixtures,N5LieReplay);;
N5C2Counts:=List(N5Class2Fixtures,N5C2Replay);;
Print("PASS N5 class2 GAP: ",Length(N5C2Counts)," groups; ",Sum(N5C2Counts,v->v[1])," branches; ",Sum(N5C2Counts,v->v[2])," decompositions\n");
QUIT;
