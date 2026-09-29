# Reconstruct each saved endpoint from a terminal special pair; no CBraid.
Read("research/certificates/B9-positive-parameters/endpoints-v1.g");
(function()
    local f,x,action,shift,inv,shelf,eps,power,base,pairs,images,
          i,j,r,k,matches,a,c,d,w,z,counts,total,maxk,n,b;
    f:=FreeGroup(18);x:=GeneratorsOfGroup(f);
    action:=function(word)
        local out,j,i,a,b;
        out:=ShallowCopy(x);
        for j in word do
            i:=AbsInt(j);a:=out[i];b:=out[i+1];
            if j>0 then out[i]:=a*b*a^-1;out[i+1]:=a;
            else out[i]:=b;out[i+1]:=b^-1*a*b;fi;
        od;
        return out;
    end;
    shift:=w->List(w,j->SignInt(j)*(AbsInt(j)+1));
    inv:=w->List(Reversed(w),j->-j);
    shelf:=function(a,b)
        return Concatenation(a,shift(b),[1],inv(shift(a)));
    end;
    eps:=w->Sum(List(w,SignInt));
    power:=function(k)
        return ListWithIdenticalEntries(k,1);
    end;
    base:=[[],[2],[1,2],[1,1,-2]];
    pairs:=[[[],[]],[[],[1]],[[1],[1]],[[1,1,-2],[]]];
    # All four base colors are explicit terms over 1.
    if action(shelf([],[]))<>action([1]) or
       action(shelf([1],[]))<>action([1,1,-2]) then Error("Base terms");fi;
    images:=List(base,w->action(Concatenation(w,[2,1],inv(shift(w)))));
    if Length(Set(images))<>4 then Error("Four cosets must be distinct");fi;
    for i in [1..4] do
        a:=pairs[i][1];c:=pairs[i][2];
        if action(Concatenation(a,shift(c)))<>action(base[i]) then Error("Base decomposition");fi;
        # An inverse step needs S(d)=c^-1 a S(c) sigma1^-1.
        # The first two cannot divide because epsilon(a)=0.
        if i<=2 then
            if eps(a)<>0 then Error("Zero-exponent terminal test");fi;
        else
            w:=Concatenation(inv(c),a,shift(c),[-1]);
            z:=1;
            for j in w do
                n:=AbsInt(j);
                if z=n then z:=n+1;elif z=n+1 then z:=n;fi;
            od;
            if z=1 then Error("Terminal obstruction must move first strand");fi;
        fi;
    od;
    counts:=[0,0,0,0];total:=0;maxk:=0;
    for r in B9EndpointRecords do
        matches:=[];
        for i in [1..4] do
            k:=eps(r[1])-eps(base[i]);
            if k>=0 and action(r[1])=action(Concatenation(base[i],power(k))) then
                Add(matches,[i,k]);
            fi;
        od;
        if Length(matches)<>1 then Error("Unique terminal representative");fi;
        i:=matches[1][1];k:=matches[1][2];
        a:=pairs[i][1];c:=pairs[i][2];
        for j in [1..k] do
            d:=shelf(a,c);c:=a;a:=d;
        od;
        if action(a)<>action(r[2]) or action(c)<>action(r[3]) then
            Error("Saved colors differ from explicit special terms");
        fi;
        if action(Concatenation(a,shift(c)))<>action(r[1]) then
            Error("Endpoint decomposition");
        fi;
        if eps(a)+eps(c)<>eps(r[1]) then Error("Exponent certificate");fi;
        counts[i]:=counts[i]+1;total:=total+k;maxk:=Maximum(maxk,k);
    od;
    # Artin identity giving the universal positive-ray reduction, plus controls.
    if action([2,1,2])<>action([1,2,1]) then Error("Artin identity");fi;
    if action([1,2])=action([2,1]) then Error("Wrong-coset control");fi;
    if action([2,2])=action([2,1]) then Error("Rejected-word control");fi;
    Print("Terminal representative counts ",counts,"; forward steps ",total,
          "; largest step count ",maxk,"\n");
    Print("All46 saved endpoints reconstructed from explicit special base terms\n");
    Print("PASS independent GAP B9 terminal-parameter certificates\n");
end)();
QUIT;
