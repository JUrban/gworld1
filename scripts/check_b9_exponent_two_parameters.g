# Verify every branch of the filtered probe independently of Python/CBraid.
Read("research/certificates/B9/height4-fixtures.g");
Read("research/certificates/B9-exponent-two-parameters/fixtures-v2.g");
(function()
    local f,x,action,shift,inv,shelf,minimum,deleteLast,actions,allowed,
          i,j,r,s,row,u,v,c,ca,A,actual,counts,h,hh,n,rank,boundary,exceptions;
    f:=FreeGroup(7);x:=GeneratorsOfGroup(f);
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
    minimum:=function(out)
        local n;
        for n in [1..7] do
            if ForAll([n+1..7],i->out[i]=x[i]) and
               ForAll([1..n],i->ForAll(LetterRepAssocWord(out[i]),j->AbsInt(j)<=n)) then
                return n;
            fi;
        od;
        Error("Ambient support");
    end;
    deleteLast:=function(w,n)
        local pos,out,j,i;
        pos:=n;out:=[];
        for j in w do
            i:=AbsInt(j);
            if pos=i then pos:=i+1;
            elif pos=i+1 then pos:=i;
            else
                if pos<i then Add(out,SignInt(j)*(i-1));else Add(out,j);fi;
            fi;
        od;
        if pos<>n then Error("Deleting a nonfixed strand");fi;
        return out;
    end;
    actions:=List(B9Records,r->action(r[1]));allowed:=[];
    for i in [1..52] do
        for j in [1..52] do
            r:=B9Records[i][4];s:=B9Records[j][4];
            if (s=1 and r<=2) or (s>=2 and r=s+1) then Add(allowed,[i,j]);fi;
        od;
    od;
    if allowed<>List(B9ExponentTwoRecords,r->r{[1,2]}) then Error("Probe coverage");fi;
    counts:=[0,0,0];exceptions:=0;
    for row in B9ExponentTwoRecords do
        i:=row[1];j:=row[2];u:=B9Records[i][1];v:=B9Records[j][1];
        r:=B9Records[i][4];s:=B9Records[j][4];
        c:=shelf(v,[]);ca:=action(c);
        if row[3]="last_generator_obstruction" then
            if s<2 or actions[i][s+1]=ca[s+1] then Error("Missing obstruction");fi;
            counts[1]:=counts[1]+1;
        else
            if row[3]="u_equals_c" then
                if actions[i]<>ca then Error("False u=c");fi;
                A:=Concatenation(c,[1]);counts[2]:=counts[2]+1;
            else
                A:=Concatenation(shelf(u,[]),shift(c));counts[3]:=counts[3]+1;
            fi;
            actual:=action(A);
            if actual<>action(row[4]) or actual<>action(row[6]) or
               minimum(actual)<>row[5] then Error("Direct support certificate");fi;
            if row[3]="remaining_direct_check" and s>=2 then
                h:=Concatenation(inv(u),c);rank:=minimum(action(h));
                hh:=h;
                for n in Reversed([rank+1..7]) do hh:=deleteLast(hh,n);od;
                if action(hh)<>action(h) then Error("Lower-strand difference");fi;
                if actions[i]=ca then Error("Need distinct special braids");fi;
                Print("Distinct special u,c: source indices ",i,",",j,
                      "; strands ",r,",",minimum(ca),"; difference strands ",rank,
                      "; h=",hh,"\n");
                exceptions:=exceptions+1;
            fi;
        fi;
    od;
    boundary:=[2,1,1,-2,-3,2,2,-3];
    if action(Concatenation(shelf([2,1],[]),shift(shelf([1],[]))))<>
       action(boundary) or minimum(action(boundary))<>4 then Error("Pure boundary control");fi;
    # A compact counterexample to extending the B2 coset-rigidity lemma to B4.
    v:=shelf([],shelf([1],[]));
    u:=shelf([],shelf(shelf([1],[]),[]));c:=shelf(v,[]);
    h:=[3,3,2,-1,-2,1,-2,-3,-3];
    if action(u)=action(c) or minimum(action(u))<>5 or minimum(action(c))<>5 or
       action(Concatenation(inv(u),c))<>action(h) or minimum(action(h))<>4 then
        Error("Compact higher-strand rigidity counterexample");
    fi;
    if minimum(action(Concatenation(shelf(u,[]),shift(c))))<>5 then
        Error("The rigidity counterexample must not be a B4 solution");
    fi;
    Print("All268 filtered cases checked: obstruction/equal/direct counts ",counts,
          "; distinct same-last-image examples ",exceptions,"\n");
    Print("PASS independent GAP B9 exponent-two parameter branches\n");
end)();
QUIT;
