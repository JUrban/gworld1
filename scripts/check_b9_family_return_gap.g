# Independent polynomial and exact constant-matrix obstruction, all n>=3.
Read("research/certificates/B9-family-return/fixtures-v2.g");
Read("research/certificates/B9/height4-fixtures.g");
(function()
    local ring,n,id,gens,i,j,g,h,blocks,block,beta,image,shift,inv,shelf,
          item,c,value,values,pol,expected,factor,five,positiveControl;
    ring:=PolynomialRing(Rationals,1);
    n:=IndeterminatesOfPolynomialRing(ring)[1];
    id:=IdentityMat(5,ring); gens:=[];
    for i in [1..4] do
        g:=IdentityMat(5,ring);
        g[i][i]:=2; g[i][i+1]:=-1; g[i+1][i]:=1; g[i+1][i+1]:=0;
        if (g-id)^2<>NullMat(5,5,ring) then Error("Unipotence"); fi;
        Add(gens,g);
    od;
    for i in [1..4] do for j in [1..4] do
        g:=gens[i]; h:=gens[j];
        if AbsInt(i-j)=1 and g*h*g<>h*g*h then Error("Artin relation"); fi;
        if AbsInt(i-j)>1 and g*h<>h*g then Error("Distant relation"); fi;
    od; od;
    blocks:=[[1,n],[3,n-2],[2,1-n],[3,2],[4,-1],[2,1],[1,1],
             [3,n-1],[4,2-n],[2,-n]];
    beta:=id;
    for block in blocks do beta:=beta*(id+block[2]*(gens[block[1]]-id)); od;
    factor:=n*(n-1)*((n-1)^2+1);
    if beta[1][5]<>factor then Error("Family last-column entry"); fi;
    pol:=Value(factor,n+4);
    if CoefficientsOfUnivariatePolynomial(pol)<>[120,142,64,13,1] or
       Value(factor,3)<>30 then Error("Universal lower bound"); fi;
    image:=function(word)
        local m,a;
        m:=id;
        for a in word do m:=m*(id+SignInt(a)*(gens[AbsInt(a)]-id)); od;
        return m;
    end;
    shift:=w->List(w,i->SignInt(i)*(AbsInt(i)+1));
    inv:=w->List(Reversed(w),i->-i);
    shelf:=function(a,b)
        return Concatenation(a,shift(b),[1],inv(shift(a)));
    end;
    if Length(B9FamilyReturn)<>10 then Error("Ten inputs"); fi;
    values:=[];
    for item in B9FamilyReturn do
        if item[2]<>B9Records[item[1]][1] then Error("Original witnessed word"); fi;
        c:=image(shelf(item[2],[])); value:=Value(c[1][5],0);
        if value<>item[3] or value=30 or value>=120 then Error("Smaller input gap"); fi;
        Add(values,value);
    od;
    if values<>[0,0,0,0,-2,0,-2,2,34,12] then Error("Constant entry list"); fi;
    five:=List([1..5],i->Zero(ring)); five[5]:=One(ring);
    for i in [1..3] do
        if gens[i]*(2*id-gens[i])<>id or gens[i]*five<>five or
           (2*id-gens[i])*five<>five then Error("Right B4 column invariant"); fi;
    od;
    positiveControl:=gens[4]*gens[3];
    if positiveControl*five<>gens[4]*five or positiveControl[5]=gens[4][5] then
        Error("Column-versus-row control");
    fi;
    Print("Family (1,5)=n*(n-1)*((n-1)^2+1); n=3 gives30\n");
    Print("At n=m+4 coefficients are [120,142,64,13,1], all positive\n");
    Print("Ten c entries: ",values,"; maximum34\n");
    Print("PASS independent GAP B9 all-parameter family-return obstruction\n");
end)();
QUIT;
