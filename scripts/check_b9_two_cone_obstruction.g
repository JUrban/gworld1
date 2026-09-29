# Faithful free-group verification, independent of CBraid normal forms.
(function()
    local f,x,action,shift,inv,shelf,A,u2,a,word,positive2,positive1,w;
    f:=FreeGroup(5);x:=GeneratorsOfGroup(f);
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
    A:=[2,1,1,-2];u2:=[1,1,-2];a:=shelf([2,1],[]);
    # All three colors are explicit special terms: (tau2 shelf 1,1,sigma1).
    if action(Concatenation(a,[3]))<>action(A) then Error("Special decomposition");fi;
    if action(shelf([],[1]))<>action([2,1]) then Error("Inverse coloring step");fi;
    positive2:=[[1,1],[1,2],[2,1],[2,2]];
    positive1:=[[1],[2]];
    if Sum(List(A,SignInt))<>2 then Error("Exponent two");fi;
    if ForAny(positive2,w->action(A)=action(w)) then Error("First cone exclusion");fi;
    word:=Concatenation(inv(u2),A);
    if Sum(List(word,SignInt))<>1 then Error("Exponent one");fi;
    if ForAny(positive1,w->action(word)=action(w)) then Error("Second cone exclusion");fi;
    # A positive control for the extra cone; exclude neither cone accidentally.
    if action(Concatenation(inv(u2),u2,[1]))<>action([1]) then
        Error("Extra-cone positive control");
    fi;
    Print("A=sigma2 sigma1^2 sigma2^-1 has special decomposition ",a,",1,sigma1\n");
    Print("All four positive exponent-two words and both exponent-one words excluded\n");
    Print("PASS independent GAP B9 two-cone obstruction\n");
end)();
QUIT;
