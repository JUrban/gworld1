# Independent faithful actions for the small-strand deductions.
Read("research/certificates/B9/height4-fixtures.g");
(function()
    local f,x,action,shift,inv,shelf,power,eps,tau,rightpower,
          r,w,e,n,target,k,short,a,b,three,one,four,images,counts;
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
    shift:=w->List(w,j->SignInt(j)*(AbsInt(j)+1));
    inv:=w->List(Reversed(w),j->-j);
    shelf:=(a,b)->Concatenation(a,shift(b),[1],inv(shift(a)));
    power:=(i,k)->List([1..AbsInt(k)],j->SignInt(k)*i);
    eps:=w->Sum(List(w,SignInt));
    tau:=function(k)
        if k=0 then return []; fi;
        return Reversed([1..k]);
    end;
    rightpower:=function(w,k)
        local out,j;
        if k<1 then Error("Right power index"); fi;
        out:=w;
        for j in [2..k] do out:=shelf(w,out); od;
        return out;
    end;
    counts:=[0,0,0,0,0];
    for r in B9Records do
        w:=r[1]; n:=r[4]; e:=eps(w);
        if e<0 or e>=n then Error("Exponent bound"); fi;
        if action(rightpower(w,n-e))<>action(tau(n-1)) then
            Error("Strand right-power identity");
        fi;
        counts[e+1]:=counts[e+1]+1;
    od;
    Print("All52 finite fixtures satisfy strand right-power identity; exponent counts ",counts,"\n");
    three:=[[],[1],[1,1,-2],[2,1]];
    images:=List(three,action);
    if Length(Set(images))<>4 then Error("Three-strand distinction"); fi;
    one:=List(three,w->shelf(w,[]));
    if Length(Set(List(one,action)))<>4 or ForAny(one,w->eps(w)<>1) then
        Error("Four-strand exponent-one list");
    fi;
    four:=List([[],[2],[1,2],[1,1,-2]],
        a->Concatenation(a,[2,1],inv(shift(a))));
    if Length(Set(List(four,action)))<>4 or ForAny(four,w->eps(w)<>2) then
        Error("Four-strand exponent-two lower bound");
    fi;
    for w in four do
        if action(shelf(w,w))<>action([3,2,1]) then Error("Four-strand square"); fi;
    od;
    for n in [3..8] do
        short:=Concatenation(power(1,n),power(3,n-2),power(2,1-n),
             [3,3,-4,2,1],power(3,n-1),power(4,2-n),power(2,-n));
        if eps(short)<>3 or action(shelf(short,short))<>action([4,3,2,1]) then
            Error("Infinite-family right-square control");
        fi;
    od;
    # The root equation alone is not a specialness criterion. At k=0,
    # this includes sigma2, excluded by the positive-special classification.
    for k in [-5..8] do
        w:=Concatenation(power(1,k),power(2,1-k));
        if action(shelf(w,w))<>action([2,1]) then Error("Non-exhaustive root family"); fi;
    od;
    if action(shelf([2],[2]))=action([3,2,1]) then Error("Wrong-target control"); fi;
    Print("PASS independent GAP B9 small-strand and right-power controls\n");
end)();
QUIT;
