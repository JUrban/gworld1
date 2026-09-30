# Native exact polynomial reconstruction of the universal partner obstruction.
Read("research/certificates/B9-family-first-column-v1/fixtures.g");
(function()
    local ring,n,id,gens,i,j,g,h,blocks,block,beta,shiftinv,first,
          column,unit,coeff,expected,positive;
    ring:=PolynomialRing(Rationals,1);
    n:=IndeterminatesOfPolynomialRing(ring)[1];
    id:=IdentityMat(6,ring); gens:=[];
    for i in [1..5] do
        g:=IdentityMat(6,ring);
        g[i][i]:=2; g[i][i+1]:=-1; g[i+1][i]:=1; g[i+1][i+1]:=0;
        if (g-id)^2<>NullMat(6,6,ring) or g*(2*id-g)<>id then
            Error("Integer power/inverse identity");
        fi;
        Add(gens,g);
    od;
    for i in [1..5] do for j in [1..5] do
        g:=gens[i]; h:=gens[j];
        if AbsInt(i-j)=1 and g*h*g<>h*g*h then Error("Artin relation"); fi;
        if AbsInt(i-j)>1 and g*h<>h*g then Error("Distant relation"); fi;
    od; od;
    blocks:=[[1,n],[3,n-2],[2,1-n],[3,2],[4,-1],[2,1],[1,1],
             [3,n-1],[4,2-n],[2,-n]];
    beta:=id;
    for block in blocks do beta:=beta*(id+block[2]*(gens[block[1]]-id)); od;
    shiftinv:=id;
    for block in Reversed(blocks) do
        shiftinv:=shiftinv*(id-block[2]*(gens[block[1]+1]-id));
    od;
    unit:=List([1..6],i->Zero(ring)); unit[1]:=One(ring);
    for i in [2..5] do
        if gens[i]*unit<>unit or (2*id-gens[i])*unit<>unit then
            Error("Shifted partner must fix first column vector");
        fi;
    od;
    if shiftinv*unit<>unit then Error("Shifted inverse"); fi;
    first:=beta*gens[1]*shiftinv; column:=first*unit;
    if column<>beta*gens[1]*unit then Error("First color expansion"); fi;
    for i in [1..6] do
        coeff:=B9FamilyFirstColumn[i];
        expected:=Sum([1..Length(coeff)],j->coeff[j]*n^(j-1));
        if column[i]<>expected then Error("Python column mismatch"); fi;
    od;
    if column[5]<>n*(n-1) or
       CoefficientsOfUnivariatePolynomial(Value(column[5],n+3))<>[6,5,1] then
        Error("Universal positive obstruction");
    fi;
    for i in [1..2] do for j in [4..6] do
        if gens[i][j]<>id[j] or (2*id-gens[i])[j]<>id[j] then
            Error("B3 has identity tail");
        fi;
    od; od;
    positive:=gens[1]*gens[2];
    if positive*unit<>gens[1]*unit or positive[1]=gens[1][1] or
       ForAny([4..6],i->(positive*unit)[i]<>0) then
        Error("Valid partner and column-versus-row controls");
    fi;
    Print("I1(beta_n) first-column coordinate5 = n*(n-1)\n");
    Print("For n=m+3, coefficients [6,5,1] are strictly positive\n");
    Print("PASS GAP B9 family arbitrary-partner obstruction\n");
end)();
QUIT;
