# Native symmetric groups and exhaustive pairs, not the Python recurrence.
(function()
    local comp,ext,sh,wp,ip,nu,bounds,prev,n,k,small,rows,p,q,allf,allg,
          f,g,a,count,exceptions,high,expected,first,seen;
    comp:=function(p,q)return List(q,j->p[j]);end;
    ext:=p->Concatenation(p,[Length(p)+1]);
    sh:=p->Concatenation([1],List(p,j->j+1));
    wp:=function(w,n)
        local p,i,x,j;
        p:=[1..n];
        for j in w do i:=AbsInt(j);x:=p[i];p[i]:=p[i+1];p[i+1]:=x;od;
        return p;
    end;
    ip:=function(p,k)
        local sp;
        sp:=sh(p);
        return comp(comp(ext(p),wp(Reversed([1..k]),Length(p)+1)),
                    List([1..Length(sp)],j->Position(sp,j)));
    end;
    nu:=p->Number([1..Length(p)-1],j->p[j+1]=j);
    bounds:=[[[[1]]]];prev:=[[1]];
    for n in [2..7] do
        rows:=[[[1..n]],Set(List(prev,p->ip(p,1)))];
        small:=List(Elements(SymmetricGroup(n-1)),p->List([1..n-1],j->j^p));
        for k in [2..n-1] do Add(rows,Set(List(small,p->ip(p,k))));od;
        for k in [0..n-1] do
            rows[k+1]:=Filtered(rows[k+1],p->nu(p)=k and Position(p,1)<=2);
        od;
        Add(bounds,rows);prev:=Union(rows);
    od;
    expected:=[[5,2,0],[6,2,0],[8,3,1],[16,8,5]];
    seen:=false;
    for q in [3..6] do
        allg:=Union(bounds[q]);allf:=Union(bounds[q+1]);
        count:=0;exceptions:=0;high:=0;
        for g in allg do for f in allf do
            a:=comp(ip(f,1),sh(ip(g,1)));
            if a{[4..q+2]}<>[4..q+2] then continue;fi;
            # A has exponent two, hence even parity, an independent condition.
            if not a{[1..3]} in [[1,2,3],[2,3,1],[3,1,2]] then continue;fi;
            count:=count+1;
            if a{[1..3]}<>[1,2,3] or nu(f)<>nu(g)+1 then
                exceptions:=exceptions+1;
                if g[q]<>q or f[q+1]<>q+1 then high:=high+1;fi;
            fi;
            if q=5 and g=[1,4,5,3,2] and f=[1,2,5,6,4,3] then
                if a<>[2,3,1,4,5,6,7] or nu(g)<>1 or nu(f)<>1 then
                    Error("Counterexample interface");fi;
                seen:=true;
            fi;
        od;od;
        if [count,exceptions,high]<>expected[q-2] then Error("Exhaustive pair counts");fi;
        Print("q=",q," bounds=",Length(allg),",",Length(allf),
              " survivors/exceptions/high=",[count,exceptions,high],"\n");
    od;
    if not seen then Error("Missing nonpure necessary permutation pair");fi;
    Print("PASS independent GAP B9 general permutation bounds\n");
end)();
QUIT;
