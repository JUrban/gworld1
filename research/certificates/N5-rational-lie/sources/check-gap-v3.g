# Independent native GAP Lie-algebra and rational-matrix replay.
Read("research/certificates/N5-rational-lie/v1/certificate.g");

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

N5LieCounts:=List(N5LieFixtures,N5LieReplay);;
# A centroid operator on H3 + H3 has two eigenvalues but nonzero
# nilpotent parts. Using only the squarefree polynomial gives a false
# projection; Hermite interpolation using the repeated factors works.
N5Jordan:=NullMat(6,6,Rationals);;
N5Jordan[1][3]:=1;;N5Jordan[4][6]:=1;;
for N5Idx in [4..6] do N5Jordan[N5Idx][N5Idx]:=1;od;
if N5Jordan*N5Jordan=N5Jordan then Error("squarefree shortcut control");fi;
N5TrueProjection:=3*N5Jordan^2-2*N5Jordan^3;;
if N5TrueProjection<>DiagonalMat([0,0,0,1,1,1]) then Error("repeated-factor CRT control");fi;
Print("GAP repeated-factor control: naive projector rejected, corrected projector exact\n");
Print("PASS N5 rational Lie GAP: ",Length(N5LieCounts)," fixtures; ",Sum(N5LieCounts,x->x[2])," factors\n");
QUIT;
