# Independent native rational matrices and explicit shelf words.
Read("research/certificates/B9/height4-fixtures.g");
(function()
    local shift,inv,shelf,wp,gens,i,g,image,w,u,v,a,expected,indices,j,row,
          directw,directu,directv;
    shift:=w->List(w,j->SignInt(j)*(AbsInt(j)+1));
    inv:=w->List(Reversed(w),j->-j);
    shelf:=function(a,b)return Concatenation(a,shift(b),[1],inv(shift(a)));end;
    wp:=function(w,n)
        local p,j,i,x;
        p:=[1..n];for j in w do i:=AbsInt(j);x:=p[i];p[i]:=p[i+1];p[i+1]:=x;od;
        return p;
    end;
    gens:=[];
    for i in [1..6] do
        g:=IdentityMat(7,Rationals);
        g[i][i]:=2;g[i][i+1]:=-1;g[i+1][i]:=1;g[i+1][i+1]:=0;
        Add(gens,g);
    od;
    image:=function(w)
        local out,j;
        out:=IdentityMat(7,Rationals);
        for j in w do out:=out*gens[AbsInt(j)]^SignInt(j);od;
        return out;
    end;
    indices:=[15,19,36,48];
    expected:=[[0,19792,9720274,-13909026,2550488,1668004,-49531],
               [0,17616,8670908,-12407474,2275096,1488058,-44203],
               [0,54608,26787792,-38331410,7028896,4596582,-136467],
               [0,-942,-463712,663540,-121670,-79580,2365]];
    for j in [1..4] do
        u:=shelf(B9Records[indices[j]][1],[]);
        v:=shelf(B9Records[9][1],[]);
        a:=Concatenation(shelf(u,[]),shift(shelf(v,[])));
        if wp(u,6)<>[1,2,5,6,4,3] or wp(v,5)<>[1,4,5,3,2]
            or wp(a,7)<>[2,3,1,4,5,6,7] then Error("Lift permutation");fi;
        if Maximum(List(u,AbsInt))<>5 or Maximum(List(v,AbsInt))<>4
            or Maximum(List(a,AbsInt))<>6 then Error("Word support");fi;
        row:=image(a)[7];
        if row<>expected[j] or row=[0,0,0,0,0,0,1] then Error("Last row obstruction");fi;
        Print("fixture ",indices[j]," last row ",row," minimum strands 6,5,7\n");
    od;
    # First lift has this short explicit term, independent of fixture specialness.
    directw:=shelf(shelf(shelf([],[]),[]),[]);
    directv:=shelf(directw,[]);
    directu:=shelf(shelf([],directw),[]);
    # Compare literal words in a free group, allowing only free cancellation.
    g:=FreeGroup(6);gens:=GeneratorsOfGroup(g);
    w:=w->Product(List(w,j->gens[AbsInt(j)]^SignInt(j)));
    if w(directw)<>w(B9Records[9][1])
        or w(directv)<>w(shelf(B9Records[9][1],[]))
        or w(directu)<>w(shelf(B9Records[15][1],[])) then
        Error("Explicit special term dictionary");fi;
    Print("PASS independent GAP B9 general permutation special lifts\n");
end)();
QUIT;
