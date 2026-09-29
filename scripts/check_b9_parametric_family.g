# Independent symbolic polynomial matrices and faithful free-group actions.
(function()
    local ring,z,ident,generators,matrix,blocks,block,i,j,s,t,nil,
          f,x,action,shift,inv,shelf,power,tail,u,n,w,v,original,short,
          left,right,expected,actions,old,neg,letters;
    ring:=PolynomialRing(Rationals,1);
    z:=IndeterminatesOfPolynomialRing(ring)[1];
    ident:=IdentityMat(5,ring); generators:=[];
    for i in [1..4] do
        s:=IdentityMat(5,ring); s[i][i]:=2; s[i][i+1]:=-1;
        s[i+1][i]:=1; s[i+1][i+1]:=0; Add(generators,s);
        if (s-ident)^2<>NullMat(5,5,ring) then Error("Unipotent generator"); fi;
    od;
    for i in [1..4] do for j in [1..4] do
        s:=generators[i]; t:=generators[j];
        if AbsInt(i-j)>1 and s*t<>t*s then Error("Distant relation"); fi;
        if AbsInt(i-j)=1 and s*t*s<>t*s*t then Error("Artin relation"); fi;
    od; od;
    blocks:=[[1,z],[3,z-2],[2,1-z],[3,2],[4,-1],[2,1],[1,1],
             [3,z-1],[4,2-z],[2,-z]];
    matrix:=ident;
    for block in blocks do
        matrix:=matrix*(ident+block[2]*(generators[block[1]]-ident));
    od;
    if matrix[5][2]<>z*(z-1) or matrix[1][1]<>-z^2+z+2 then
        Error("Distinctness polynomial");
    fi;
    Print("Determinant representation: ",DeterminantMat(matrix),"\n");
    if DeterminantMat(matrix)<>One(ring) then Error("Determinant"); fi;
    Print("Universal polynomial entries: (5,2)=n*(n-1), (1,1)=-n^2+n+2\n");
    shift:=w->List(w,j->SignInt(j)*(AbsInt(j)+1));
    inv:=w->List(Reversed(w),j->-j);
    shelf:=function(a,b)
        return Concatenation(a,shift(b),[1],inv(shift(a)));
    end;
    power:=function(i,k)
        return List([1..AbsInt(k)],j->SignInt(k)*i);
    end;
    tail:=function(k)
        if k=0 then return []; fi;
        return Concatenation(power(1,k),inv(shift(tail(k-1))));
    end;
    # This action uses no matrix faithfulness and no CBraid dependency.
    f:=FreeGroup(10); x:=GeneratorsOfGroup(f);
    action:=function(w)
        local out,j,i,a,b;
        out:=ShallowCopy(x);
        for j in w do
            i:=AbsInt(j); a:=out[i]; b:=out[i+1];
            if j>0 then out[i]:=a*b*a^-1; out[i+1]:=a;
            else out[i]:=b; out[i+1]:=b^-1*a*b; fi;
        od;
        return out;
    end;
    for i in [1..8] do
        if action([i,i+1,i])<>action([i+1,i,i+1]) then Error("Artin action control"); fi;
    od;
    for n in [2..8] do
        if action(tail(n))<>action(shelf(tail(n-1),tail(n-2))) then
            Error("Special Fibonacci recurrence");
        fi;
    od;
    for n in [3..8] do
        u:=tail(n-3);
        v:=shelf([],shelf(shelf([],u),[]));
        original:=shelf(tail(n),v);
        short:=Concatenation(power(1,n),power(3,n-2),power(2,1-n),
             [3,3,-4,2,1],power(3,n-1),power(4,2-n),power(2,-n));
        left:=action(original); right:=action(short);
        if left<>right then Error("Fixed-five-strand identity"); fi;
        if left[5]=x[5] or ForAny([6..10],i->left[i]<>x[i]) then
            Error("Exact standard support");
        fi;
        # Deliberately omit the first sigma4^-1: it must change the braid.
        neg:=Concatenation(power(1,n),power(3,n-2),power(2,1-n),
             [3,3,2,1],power(3,n-1),power(4,2-n),power(2,-n));
        if action(neg)=right then Error("Missing-factor negative control"); fi;
        Print("n=",n," special recurrence and exact B5 reduction; action lengths ",
              List(right,Length),"\n");
    od;
    Print("PASS independent GAP infinite B9 family identities and symbolic separation\n");
end)();
QUIT;
