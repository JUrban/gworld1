# Load after N5LieReplay and the mixed certificate in the combined input.
if LoadPackage("nq")<>true or LoadPackage("polycyclic")<>true then Error("packages");fi;
N5MixWord:=function(g,gens,vector)
    local value,i;
    value:=One(g);
    for i in [1..Length(gens)] do value:=value*gens[i]^vector[i];od;
    return value;
end;
N5MixCanonical:=function(p,nf,orders)
    local a,i,j;
    a:=List(p,ShallowCopy);
    for i in [nf+1..Length(a)] do for j in [1..Length(a)] do
        a[i][j]:=a[i][j] mod orders[i-nf];
    od;od;
    return a;
end;
N5MixQuotients:=function(data)
    local qo,nf,nt,r,n,projections,qset,mask,p,q,elements,options,j,
          cols,lcols,tcols,delta,i,ok,all,key,orders;
    qo:=data.quotient_orders;nf:=Number(qo,x->x=0);r:=Length(qo);nt:=r-nf;
    orders:=qo{[nf+1..r]};n:=data.rational.dimension;
    projections:=data.rational.projections;qset:=[];
    for mask in Tuples([0,1],Length(projections)) do
        if n=0 then p:=[];else p:=NullMat(n,n,Rationals);fi;
        for i in [1..Length(mask)] do p:=p+mask[i]*projections[i];od;
        if nf=0 then q:=[];else q:=p{[1..nf]}{[1..nf]};fi;
        # An integral idempotent is equivalent to a complementary pair
        # of saturated quotient lattices.
        if ForAll(Concatenation(q),IsInt) then AddSet(qset,q);fi;
    od;
    elements:=Cartesian(List(orders,d->[0..d-1]));options:=[];
    for j in [1..nt] do
        Add(options,Filtered(elements,v->ForAll([1..nt],i->orders[j]*v[i] mod orders[i]=0)));
    od;
    all:=[];
    for q in qset do for lcols in Tuples(elements,nf) do for tcols in Cartesian(options) do
        cols:=[];
        for j in [1..nf] do Add(cols,Concatenation(List([1..nf],i->q[i][j]),lcols[j]));od;
        for j in [1..nt] do Add(cols,Concatenation(List([1..nf],i->0),tcols[j]));od;
        if r=0 then p:=[];ok:=true;
        else
            p:=TransposedMat(cols);delta:=p*p-p;
            ok:=ForAll([1..r],i->ForAll([1..r],j->
                 (i<=nf and delta[i][j]=0) or (i>nf and delta[i][j] mod qo[i]=0)));
        fi;
        if ok then AddSet(all,p);fi;
    od;od;od;
    return all;
end;
N5MixReplay:=function(item)
    local data,qo,zo,r,s,n,nf,nz,f,x,rels,i,j,k,w,pres,ep,g,gens,
          central,qmap,quot,qgens,expected,record,a,b,value,branch,pgens,
          sides,projections,side,pr,lifts,relrows,sm,rank,torsion,position,
          row,defect,centralImages,factors,corrected,zp,corr,known,
          arithcount,relcount,crosscount,positive,sub,all,saved,pcols,
          qrank,rad;
    data:=item.result;qo:=data.quotient_orders;zo:=data.center_orders;
    r:=Length(qo);s:=Length(zo);n:=r+s;nf:=Number(qo,x->x=0);nz:=Number(zo,x->x=0);
    if r=0 then
        g:=AbelianPcpGroup(zo);gens:=GeneratorsOfGroup(g);
    else
        f:=FreeGroup(n);x:=GeneratorsOfGroup(f);rels:=[];
        for i in [1..n] do for j in [i+1..n] do
            w:=Comm(x[i],x[j]);
            if j<=r then for k in [1..s] do w:=w*x[r+k]^-data.beta[i][j][k];od;fi;
            Add(rels,w);
        od;od;
        for i in [1..s] do if zo[i]>0 then Add(rels,x[r+i]^zo[i]);fi;od;
        for i in [1..r] do if qo[i]>0 then
            w:=x[i]^qo[i];for k in [1..s] do w:=w*x[r+k]^-data.powers[i][k];od;Add(rels,w);
        fi;od;
        pres:=f/rels;ep:=NqEpimorphismNilpotentQuotient(pres,2);g:=Image(ep);
        gens:=List(GeneratorsOfGroup(pres),y->Image(ep,y));
    fi;
    central:=Subgroup(g,gens{[r+1..n]});
    if central<>Centre(g) or HirschLength(central)<>nz or
       Size(TorsionSubgroup(central))<>Product(Filtered(zo,d->d>0)) then Error("central coordinate model");fi;
    qmap:=NaturalHomomorphismByNormalSubgroup(g,central);quot:=Image(qmap);
    qgens:=List(gens{[1..r]},a->Image(qmap,a));
    if HirschLength(quot)<>nf or Size(TorsionSubgroup(quot))<>Product(Filtered(qo,d->d>0)) then Error("quotient coordinate model");fi;
    if HirschLength(g)<>nf+nz then Error("Hirsch length");fi;
    arithcount:=0;relcount:=0;crosscount:=0;positive:=0;
    for record in item.arithmetic do
        a:=N5MixWord(g,gens,record.a);b:=N5MixWord(g,gens,record.b);
        if a*b<>N5MixWord(g,gens,record.product) or a^-1<>N5MixWord(g,gens,record.inverse)
           or a^record.exponent<>N5MixWord(g,gens,record.power) then Error("coordinate arithmetic");fi;
        arithcount:=arithcount+3;
    od;
    for branch in data.branches do
        if r=0 then pcols:=[];else pcols:=TransposedMat(branch.projection);fi;
        pgens:=List(pcols,v->N5MixWord(quot,qgens,v));
        projections:=[Subgroup(quot,pgens),Subgroup(quot,List([1..r],i->qgens[i]/pgens[i]))];
        sides:=List(branch.quotient_generators,vs->Subgroup(quot,List(vs,v->N5MixWord(quot,qgens,v))));
        if sides<>projections or ClosureGroup(sides[1],sides[2])<>quot or Size(Intersection(sides[1],sides[2]))<>1 then Error("quotient factors");fi;
        lifts:=List(branch.quotient_generators,vs->List(vs,v->N5MixWord(g,gens,Concatenation(v,List([1..s],i->0)))));
        if branch.outcome="cross_commutator_obstruction" then
            record:=branch.cross_witness;
            value:=Comm(lifts[1][record[1]+1],lifts[2][record[2]+1]);
            if value=One(g) or value<>N5MixWord(g,gens,Concatenation(List([1..r],i->0),record[3])) then Error("cross witness");fi;
            crosscount:=crosscount+1;continue;
        fi;
        if not ForAll(lifts[1],a->ForAll(lifts[2],b->Comm(a,b)=One(g))) then Error("missed cross obstruction");fi;
        for side in [1,2] do
            pr:=branch.presentations[side];known:=List(pr.lifts,v->N5MixWord(g,gens,v));
            if known<>lifts[side] then Error("lift binding");fi;
            if Length(known)=0 then relrows:=[];else relrows:=TransposedMat(pr.relation_basis);fi;
            if Length(relrows)=0 then rank:=0;torsion:=1;
            else sm:=SmithNormalFormIntegerMat(relrows);rank:=RankMat(sm);
                torsion:=Product(List([1..rank],i->AbsInt(sm[i][i])));
            fi;
            if Length(known)-rank<>HirschLength(sides[side]) or torsion<>Size(TorsionSubgroup(sides[side])) then Error("incomplete abelian relation lattice");fi;
            position:=0;
            for row in relrows do
                position:=position+1;value:=N5MixWord(g,known,row);
                if Image(qmap,value)<>One(quot) or row<>pr.exponents[position] or
                   value<>N5MixWord(g,gens,Concatenation(List([1..r],i->0),pr.defects[position])) then Error("power relation defect");fi;
                relcount:=relcount+1;
            od;
            for i in [1..Length(known)] do for j in [i+1..Length(known)] do
                position:=position+1;value:=Comm(known[i],known[j]);
                if pr.exponents[position]<>List(known,v->0) or
                   value<>N5MixWord(g,gens,Concatenation(List([1..r],i->0),pr.defects[position])) then Error("commutator relation defect");fi;
                relcount:=relcount+1;
            od;od;
            if position<>Length(pr.defects) then Error("extra defects");fi;
        od;
        if branch.outcome="decomposition" then
            factors:=List(branch.factor_generators,vs->Subgroup(g,List(vs,v->N5MixWord(g,gens,v))));
            for side in [1,2] do
                if side=1 then zp:=branch.central_projection;else zp:=IdentityMat(s,Rationals)-branch.central_projection;fi;
                if s=0 then centralImages:=[];else centralImages:=List(TransposedMat(zp),v->N5MixWord(g,gens,Concatenation(List([1..r],i->0),v)));fi;
                corrected:=[];
                for i in [1..Length(lifts[side])] do
                    corr:=N5MixWord(g,gens,Concatenation(List([1..r],i->0),branch.corrections[side][i]));
                    Add(corrected,lifts[side][i]*corr);
                od;
                if Subgroup(g,Concatenation(centralImages,corrected))<>factors[side] then Error("corrected factor binding");fi;
            od;
            if Size(factors[1])=1 or Size(factors[2])=1 or Size(Intersection(factors[1],factors[2]))<>1 or
               ClosureGroup(factors[1],factors[2])<>g or not ForAll(GeneratorsOfGroup(factors[1]),a->ForAll(GeneratorsOfGroup(factors[2]),b->Comm(a,b)=One(g))) then Error("actual group decomposition");fi;
            positive:=positive+1;
        fi;
    od;
    if not data.answer then
        all:=N5MixQuotients(data);
        saved:=Set(List(data.branches,b->N5MixCanonical(b.projection,nf,qo{[nf+1..r]})));
        if all<>saved then Error("incomplete quotient projection enumeration");fi;
    fi;
    if nf+nz=0 then
        if Length(DirectFactorsOfGroup(Image(IsomorphismPcGroup(g))))>1 then expected:=true;else expected:=false;fi;
        if expected<>data.answer then Error("independent finite-group decision");fi;
    fi;
    if data.answer<>item.expected then Error("expected mathematical fixture");fi;
    Print("GAP mixed ",item.name,": ",data.answer,"; ",Length(data.branches)," quotient branches; ",relcount," defects\n");
    return [arithcount,relcount,crosscount,positive];
end;

N5MixLieChecks:=List(N5LieFixtures,N5LieReplay);;
N5MixChecks:=List(N5MixedFixtures,N5MixReplay);;
Print("PASS N5 mixed class2 GAP: ",Length(N5MixChecks)," fixtures; totals ",Sum(N5MixChecks),"\n");
QUIT;
