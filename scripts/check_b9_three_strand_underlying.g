# Native GAP reconstruction; does not read the Python certificate or a term list.
(function()
    local compose,ip,extend,sh,nu,perms,cases,vwords,uwords,shift,inv,shelf,
          wordperm,u,v,up,vp,ap,unknown,known,survivors,f,x,action,c,image,
          uc,cc,gens,g,i,j,h,id,n,only;
    compose:=function(p,q) return List(q,j->p[j]); end;
    extend:=p->Concatenation(p,[Length(p)+1]);
    sh:=p->Concatenation([1],List(p,j->j+1));
    ip:=function(p)
        local q,s;
        q:=sh(p); s:=Concatenation([2,1],[3..Length(p)+1]);
        return compose(compose(extend(p),s),List([1..Length(q)],j->Position(q,j)));
    end;
    nu:=p->Number([1..Length(p)-1],j->p[j+1]=j);
    perms:=List(Elements(SymmetricGroup(4)),p->List([1..4],j->j^p));
    cases:=Set(Filtered(perms,p->nu(p)=2));
    if Length(perms)<>24 or cases<>[[1,4,2,3],[2,1,4,3],[3,1,2,4]] then
        Error("Complete permutation coverage");
    fi;
    shift:=w->List(w,j->SignInt(j)*(AbsInt(j)+1));
    inv:=w->List(Reversed(w),j->-j);
    shelf:=function(a,b)
        return Concatenation(a,shift(b),[1],inv(shift(a)));
    end;
    wordperm:=function(w,n)
        local p,j,i,a;
        p:=[1..n];
        for j in w do
            i:=AbsInt(j); a:=p[i];p[i]:=p[i+1];p[i+1]:=a;
        od;
        return p;
    end;
    vwords:=[[1,1,-2],[2,1]];
    uwords:=Concatenation(List(vwords,v->shelf(v,[])),[[3,2,1]]);
    unknown:=0;
    for up in cases do for v in vwords do
        ap:=compose(ip(up),sh(ip(wordperm(v,3))));
        if ap{[4,5]}=[4,5] then Error("Unknown-sector survivor"); fi;
        unknown:=unknown+1;
        Print("nu2 u=",up," v=",v," A=",ap,"\n");
    od; od;
    f:=FreeGroup(5);x:=GeneratorsOfGroup(f);
    action:=function(w)
        local out,j,i,a,b;
        out:=ShallowCopy(x);
        for j in w do
            i:=AbsInt(j);a:=out[i];b:=out[i+1];
            if j>0 then out[i]:=a*b*a^-1;out[i+1]:=a;
            else out[i]:=b;out[i+1]:=b^-1*a*b; fi;
        od;
        return out;
    end;
    id:=IdentityMat(4,Rationals);gens:=[];
    for i in [1..3] do
        g:=IdentityMat(4,Rationals);
        g[i][i]:=2;g[i][i+1]:=-1;g[i+1][i]:=1;g[i+1][i+1]:=0;
        Add(gens,g);
    od;
    for i in [1..3] do for j in [1..3] do
        if AbsInt(i-j)=1 and gens[i]*gens[j]*gens[i]<>gens[j]*gens[i]*gens[j] then
            Error("Artin matrix relation");
        fi;
        if AbsInt(i-j)>1 and gens[i]*gens[j]<>gens[j]*gens[i] then
            Error("Distant matrix relation");
        fi;
    od;od;
    image:=function(w)
        local out,j;
        out:=id;
        for j in w do out:=out*gens[AbsInt(j)]^SignInt(j);od;
        return out;
    end;
    known:=0;survivors:=[];
    for u in uwords do for v in vwords do
        c:=shelf(v,[]);g:=Concatenation(shelf(u,[]),shift(c));
        ap:=wordperm(g,5);
        if ap<>compose(ip(wordperm(u,4)),sh(ip(wordperm(v,3)))) then
            Error("Word/permutation dictionary");
        fi;
        known:=known+1;
        if ap{[4,5]}=[4,5] then
            Add(survivors,[u,v]);
            if action(u)[4]=action(c)[4] then Error("Artin obstruction");fi;
            uc:=List(image(u),r->r[4]);cc:=List(image(c),r->r[4]);
            if uc<>[0,0,-1,0] or cc<>[-2,-4,-1,2] then Error("Matrix obstruction");fi;
            if action(g)[5]=x[5] then Error("Fifth-strand negative control");fi;
            Print("Survivor x4 images: ",action(u)[4]," vs ",action(c)[4],"\n");
            Print("Survivor column4: ",uc," vs ",cc,"\n");
        fi;
    od;od;
    if survivors<>[[[3,2,1],[2,1]]] or unknown<>6 or known<>6 then Error("Coverage");fi;
    u:=[3,2,1];
    if List(image(Concatenation(u,[1,-2,1])),r->r[4])<>List(image(u),r->r[4]) then
        Error("Right B3 column control");fi;
    Print("PASS independent GAP B9 three-strand underlying exclusion\n");
end)();
QUIT;
