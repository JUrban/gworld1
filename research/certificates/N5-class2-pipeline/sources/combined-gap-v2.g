Read("research/certificates/N5-class2-pipeline/v2/certificate.g");
N5LieRank:=function(rows)
    if Length(rows)=0 then return 0;fi;
    return RankMat(rows);
end;
N5LieSpan:=function(rows)
    if Length(rows)=0 or N5LieRank(rows)=0 then return [];fi;
    return BasisVectors(Basis(VectorSpace(Rationals,rows)));
end;
N5LiePoly:=function(coeffs)
    return UnivariatePolynomial(Rationals,coeffs);
end;
N5LieEval:=function(coeffs,a)
    local out,i;
    out:=NullMat(Length(a),Length(a),Rationals);
    for i in Reversed([1..Length(coeffs)]) do
        out:=out*a+coeffs[i]*IdentityMat(Length(a),Rationals);
    od;
    return out;
end;

N5LieReplay:=function(fixture)
    local c,n,r,table,i,j,k,entries,alg,bas,e,right,change,inverse,
          d,stemBasis,stemRight,mat,eqrows,unit,centroidRows,centroid,
          gram,degree,radical,radMats,productRows,powerRows,step,a,b,
          chosen,charpoly,factors,foundFactors,recordFactors,crt,
          allProjections,p,q,zero,total,dims,lower,current,next,
          fullRight,row,derived,center,comm,coords,zspace,count;
    c:=fixture.structure_constants;n:=Length(c);r:=fixture.result;
    if n=0 then
        if r.factor_dimensions<>[] or r.dimension<>0 then Error("zero input");fi;
        Print("GAP Lie replay zero\n");return [0,0,0];
    fi;
    table:=EmptySCTable(n,0,"antisymmetric");
    for i in [1..n] do for j in [i+1..n] do
        entries:=[];
        for k in [1..n] do
            if c[i][j][k]<>0 then Append(entries,[c[i][j][k],k]);fi;
        od;
        SetEntrySCTable(table,i,j,entries);
    od;od;
    alg:=LieAlgebraByStructureConstants(Rationals,table);
    bas:=Basis(alg);e:=BasisVectors(bas);
    for i in [1..n] do for j in [1..n] do
        if Coefficients(bas,e[i]*e[j])<>c[i][j] then Error("original bracket mismatch");fi;
        for k in [1..n] do
            if (e[i]*e[j])*e[k]+(e[j]*e[k])*e[i]+(e[k]*e[i])*e[j]<>Zero(alg) then
                Error("Jacobi failure");
            fi;
        od;
    od;od;
    right:=List(e,y->List(e,x->Coefficients(bas,x*y)));
    current:=IdentityMat(n,Rationals);
    for step in [1..n] do
        next:=[];
        for row in current do for mat in right do Add(next,row*mat);od;od;
        current:=N5LieSpan(next);
        if Length(current)=0 then break;fi;
    od;
    if Length(current)<>0 or step<>r.nilclass then Error("nilpotency class");fi;
    change:=TransposedMat(r.basis_change);inverse:=change^-1;
    fullRight:=List([1..n],j->change*Sum([1..n],i->change[j][i]*right[i])*inverse);
    d:=r.stem_dimension;
    for i in [d+1..n] do
        if fullRight[i]<>NullMat(n,n,Rationals) then Error("complement not central");fi;
    od;
    for mat in fullRight do for row in mat do
        if ForAny([d+1..n],i->row[i]<>0) then Error("stem not an ideal");fi;
    od;od;
    if d>0 then
        stemRight:=List([1..d],i->fullRight[i]{[1..d]}{[1..d]});
        derived:=N5LieSpan(Concatenation(stemRight));
        eqrows:=[];
        # The common left kernel of right adjoints is the center.
        for i in [1..d] do Add(eqrows,Concatenation(List(stemRight,a->a[i])));od;
        center:=NullspaceMat(eqrows);
        if N5LieRank(Concatenation(derived,center))<>Length(derived) then Error("nonstem center");fi;
        # Reconstruct the entire centroid as the adjoint commutant.
        eqrows:=[];
        for i in [1..d] do for j in [1..d] do
            unit:=NullMat(d,d,Rationals);unit[i][j]:=1;
            Add(eqrows,Concatenation(List(stemRight,a->Concatenation(unit*a-a*unit))));
        od;od;
        centroidRows:=NullspaceMat(eqrows);
        centroid:=List(r.centroid_basis,TransposedMat);
        if Length(centroidRows)<>Length(centroid) or
           N5LieRank(Concatenation(centroidRows,List(centroid,Concatenation)))<>Length(centroid) or
           N5LieRank(List(centroid,Concatenation))<>Length(centroid) then Error("centroid not complete");fi;
        gram:=List(centroid,a->List(centroid,b->TraceMat(a*b)));
        if gram<>r.trace_gram then Error("trace form mismatch");fi;
        degree:=RankMat(gram);
        if degree<>r.semisimple_dimension then Error("semisimple dimension");fi;
        radical:=NullspaceMat(gram);
        radMats:=List(radical,v->Sum([1..Length(v)],i->v[i]*centroid[i]));
        # Verify the actual radical certificate is an ideal, nilpotent,
        # and contains every centroid commutator; no trace theorem is
        # being inferred from just an output dimension.
        zspace:=List(radMats,Concatenation);
        for a in centroid do for b in centroid do
            comm:=Concatenation(a*b-b*a);
            if N5LieRank(Concatenation(zspace,[comm]))<>Length(zspace) then Error("noncommutative semisimple quotient");fi;
        od;od;
        for a in radMats do for b in centroid do
            if N5LieRank(Concatenation(zspace,[Concatenation(a*b),Concatenation(b*a)]))<>Length(zspace) then
                Error("radical not ideal");fi;
        od;od;
        powerRows:=zspace;
        for step in [1..Length(centroid)+1] do
            if Length(powerRows)=0 then break;fi;
            productRows:=[];
            for row in powerRows do
                a:=List([1..d],i->row{[(i-1)*d+1..i*d]});
                for b in radMats do Add(productRows,Concatenation(a*b));od;
            od;
            powerRows:=N5LieSpan(productRows);
        od;
        if Length(powerRows)<>0 then Error("radical not nilpotent");fi;
        chosen:=Sum([1..Length(centroid)],i->r.chosen_k^(i-1)*centroid[i]);
        if chosen<>TransposedMat(r.separating_element) then Error("separating element");fi;
        charpoly:=CharacteristicPolynomial(chosen);
        if charpoly<>N5LiePoly(r.characteristic) then Error("characteristic polynomial");fi;
        factors:=Factors(charpoly);
        if Product(factors)<>charpoly then Error("factor product");fi;
        if ForAny(factors,f->LeadingCoefficient(f)<>1) then
            Print("Normalizing rational polynomial factors for ",fixture.name,": ",factors,"\n");
        fi;
        factors:=List(Filtered(factors,f->DegreeOfUnivariateLaurentPolynomial(f)>0),
                      f->f/LeadingCoefficient(f));
        foundFactors:=Set(factors);
        if Sum(foundFactors,DegreeOfUnivariateLaurentPolynomial)<>degree then Error("characters not separated");fi;
        recordFactors:=[];
        for row in r.irreducible_factors do
            for i in [1..row[2]] do Add(recordFactors,N5LiePoly(row[1]));od;
        od;
        # SymPy's QQ factor_list can return primitive integral factors
        # with a separate rational content. Ideals and CRT polynomials
        # are unchanged by these nonzero scalar factors.
        recordFactors:=List(recordFactors,f->f/LeadingCoefficient(f));
        if Product(recordFactors)<>charpoly then Error("certificate monic factor product");fi;
        if SortedList(recordFactors)<>SortedList(factors) then
            Print("Factor comparison diagnostic ",fixture.name,"\nGAP factors: ",factors,
                  "\nCertificate factors: ",recordFactors,"\nCharacteristic: ",charpoly,"\n");
            Error("independent rational factorization");
        fi;
        crt:=List(r.crt_polynomials,coeffs->N5LieEval(coeffs,chosen));
    else
        centroid:=[];degree:=0;crt:=[];
    fi;
    allProjections:=List(r.projections,TransposedMat);
    zero:=NullMat(n,n,Rationals);total:=zero;
    for p in allProjections do
        if p*p<>p or RankMat(p)=0 then Error("projection");fi;
        for mat in right do if p*mat<>mat*p then Error("projection not centroid");fi;od;
        for q in allProjections do
            if p<>q and p*q<>zero then Error("nonorthogonal projections");fi;
        od;
        total:=total+p;
    od;
    if total<>IdentityMat(n,Rationals) then Error("projections not complete");fi;
    dims:=SortedList(List(allProjections,RankMat));
    if dims<>fixture.expected or dims<>r.factor_dimensions then Error("factor dimensions");fi;
    for i in [1..Length(crt)] do
        p:=change*allProjections[i]*inverse;
        if p{[1..d]}{[1..d]}<>crt[i] then Error("CRT projection binding");fi;
    od;
    Print("GAP Lie replay ",fixture.name,": ",dims,"; centroid ",Length(centroid),"; reduced dimension ",degree,"\n");
    return [n,Length(allProjections),degree];
end;


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
