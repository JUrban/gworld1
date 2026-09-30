# Independent finite reconstruction, native rational matrices; no Python input.
(function()
    local low,last,comp,ext,sh,wordperm,shift,inv,shelf,q,a,f1,f,i,j,
          lhs,rhs,all,small,tau,bad,u,v,c,n,id,gens,g,image,uc,cc,count,
          ff,xx,action,aa;
    low:=function(a,i) if i<=3 then return a[i];else return i;fi;end;
    last:=function(q,i)
        if i=q+1 then return q+2;elif i=q+2 then return q+1;else return i;fi;
    end;
    comp:=function(p,q) return List(q,j->p[j]);end;
    ext:=p->Concatenation(p,[Length(p)+1]);
    sh:=p->Concatenation([1],List(p,j->j+1));
    wordperm:=function(w,n)
        local p,j,i,z;
        p:=[1..n];
        for j in w do i:=AbsInt(j);z:=p[i];p[i]:=p[i+1];p[i+1]:=z;od;
        return p;
    end;
    shift:=w->List(w,j->SignInt(j)*(AbsInt(j)+1));
    inv:=w->List(Reversed(w),j->-j);
    shelf:=function(a,b)return Concatenation(a,shift(b),[1],inv(shift(a)));end;
    count:=0;
    for q in [3..24] do
        all:=[];small:=[];
        for a in [[1,2,3],[2,3,1],[3,1,2]] do
            for f1 in [1..q+1] do
                f:=[f1,a[1]];
                for i in [3..q+1] do Add(f,low(a,last(q,f[Length(f)]+1)));od;
                if Set(f)<>[1..q+1] or Length(Set(f))<>q+1 then continue;fi;
                if f1<>low(a,last(q,f1+1)) then continue;fi;
                lhs:=comp(ext(f),Concatenation([2,1],[3..q+2]));
                rhs:=List(sh(f),j->low(a,last(q,j)));
                if lhs<>rhs then continue;fi;
                Add(all,[a,f]);
                if Position(f,1)<=2 then Add(small,[a,f]);fi;
            od;
        od;
        tau:=Concatenation([q+1],[1..q]);
        bad:=Concatenation([q+1,2,1],[3..q]);
        if all<>[[[1,2,3],tau],[[2,3,1],bad]] or small<>[[[1,2,3],tau]] then
            Error("Permutation recurrence");fi;
        if Number([1..q],j->tau[j+1]=j)<>q or Position(bad,1)<>3 then
            Error("Prior invariant interface");fi;
        u:=Reversed([1..q]);v:=Reversed([1..q-1]);c:=shelf(v,[]);
        if wordperm(u,q+1)<>tau or wordperm(c,q+1)<>Concatenation([1..q-1],[q+1,q]) then
            Error("Word dictionary");fi;
        if q<=12 then
            n:=q+1;id:=IdentityMat(n,Rationals);gens:=[];
            for i in [1..q] do
                g:=IdentityMat(n,Rationals);
                g[i][i]:=2;g[i][i+1]:=-1;g[i+1][i]:=1;g[i+1][i+1]:=0;
                Add(gens,g);
            od;
            image:=function(w)
                local out,j;
                out:=id;
                for j in w do out:=out*gens[AbsInt(j)]^SignInt(j);od;
                return out;
            end;
            uc:=List(image(u),r->r[n]);cc:=List(image(c),r->r[n]);
            if uc<>Concatenation(List([1..q-1],j->0),[-1,0]) or
               cc<>Concatenation([-2],List([1..q-2],j->-4),[-1,2]) then
                Error("Universal column interface");fi;
            if List(image(Concatenation(u,[1,-2,1])),r->r[n])<>uc then
                Error("Right subgroup column control");fi;
            count:=count+1;
        fi;
    od;
    ff:=FreeGroup(5);xx:=GeneratorsOfGroup(ff);
    action:=function(w)
        local out,j,i,a,b;
        out:=ShallowCopy(xx);
        for j in w do
            i:=AbsInt(j);a:=out[i];b:=out[i+1];
            if j>0 then out[i]:=a*b*a^-1;out[i+1]:=a;
            else out[i]:=b;out[i+1]:=b^-1*a*b;fi;
        od;
        return out;
    end;
    u:=[1,1,-2];v:=[1];aa:=Concatenation(shelf(u,[]),shift(shelf(v,[])));
    if action(aa)<>action(Concatenation(u,[1])) or action(aa){[4,5]}<>xx{[4,5]} then
        Error("q2 boundary");fi;
    u:=[3,2,1];v:=[2,1];aa:=Concatenation(shelf(u,[]),shift(shelf(v,[])));
    if wordperm(aa,5)<>[1..5] or action(aa)[5]=xx[5] then
        Error("Permutation-only control");fi;
    if count<>10 then Error("Matrix case coverage");fi;
    Print("22 permutation recurrences,10 native full matrix cases,q2/q3 controls\n");
    Print("PASS independent GAP B9 positive underlying interface checks\n");
end)();
QUIT;
