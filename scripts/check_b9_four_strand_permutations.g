# Independent complete permutation bounds, with existing witnessed-word controls.
Read("research/certificates/B9/height4-fixtures.g");
(function()
    local comp,ext,sh,ip,wordperm,shift,inv,shelf,nu,p3,s3,s4,p4,p4all,p5,
          vs,u,v,ap,rows,e,tested,known,record,p,w,actual,known4;
    comp:=function(p,q)return List(q,j->p[j]);end;
    ext:=p->Concatenation(p,[Length(p)+1]);
    sh:=p->Concatenation([1],List(p,j->j+1));
    wordperm:=function(w,n)
        local p,j,i,a;
        p:=[1..n];
        for j in w do i:=AbsInt(j);a:=p[i];p[i]:=p[i+1];p[i+1]:=a;od;
        return p;
    end;
    ip:=function(p,k)
        local sp;
        sp:=sh(p);
        return comp(comp(ext(p),wordperm(Reversed([1..k]),Length(p)+1)),
            List([1..Length(sp)],j->Position(sp,j)));
    end;
    shift:=w->List(w,j->SignInt(j)*(AbsInt(j)+1));
    inv:=w->List(Reversed(w),j->-j);
    shelf:=function(a,b)return Concatenation(a,shift(b),[1],inv(shift(a)));end;
    nu:=p->Number([1..Length(p)-1],j->p[j+1]=j);
    p3:=Set(List([[],[1],[1,1,-2],[2,1]],w->wordperm(w,3)));
    s3:=List(Elements(SymmetricGroup(3)),p->List([1..3],j->j^p));
    s4:=List(Elements(SymmetricGroup(4)),p->List([1..4],j->j^p));
    p4:=[[[1,2,3,4]],Set(List(p3,p->ip(p,1))),
        Set(List(s3,p->ip(p,2))),Set(List(s3,p->ip(p,3)))];
    p4all:=Union(p4);
    p5:=[[[1,2,3,4,5]],Set(List(p4all,p->ip(p,1))),
        Set(List(s4,p->ip(p,2))),Set(List(s4,p->ip(p,3))),Set(List(s4,p->ip(p,4)))];
    if List(p4,Length)<>[1,4,3,1] or List(p5,Length)<>[1,9,12,4,1] then
        Error("Complete image set cardinalities");fi;
    for e in [0..3] do if ForAny(p4[e+1],p->nu(p)<>e) then Error("P4 invariant");fi;od;
    for e in [0..4] do if ForAny(p5[e+1],p->nu(p)<>e) then Error("P5 invariant");fi;od;
    vs:=Concatenation(List([[1,1,-2],[2,1]],w->wordperm(shelf(w,[]),4)),p4[3]);
    rows:=[];tested:=0;
    for v in vs do for e in [1..4] do for u in p5[e+1] do
        tested:=tested+1;
        ap:=comp(ip(u,1),sh(ip(v,1)));
        if ap{[4,5,6]}=[4,5,6] then Add(rows,[v,e,u,ap]);fi;
    od;od;od;
    if tested<>130 or rows<>[[[3,1,2,4],3,[4,1,2,3,5],[1,2,3,4,5,6]]] then
        Error("Complete surviving row");fi;
    # All ten already witnessed B4-or-smaller examples realize the full P4 bound.
    known:=Filtered(B9Records,r->r[4]<=4);
    if Length(known)<>10 then Error("Known inputs");fi;
    actual:=Set(List(known,r->wordperm(r[1],4)));
    if actual<>p4all then Error("All nine possible permutations realized");fi;
    known4:=Filtered(known,r->r[4]=4);
    for record in known4 do
        p:=wordperm(record[1],4);
        if p=[3,1,2,4] then Error("Known four-strand remaining input");fi;
        Print("known exact4 input=",record[1]," permutation=",p,"\n");
    od;
    Print("P4 upper bound is exactly realized by known words: ",Length(actual)," permutations\n");
    Print("130 pairs, unique necessary row: ",rows[1],"\n");
    Print("PASS independent GAP B9 four-strand permutation inventory\n");
end)();
QUIT;
