if LoadPackage("nq")<>true or LoadPackage("polycyclic")<>true then FORCE_QUIT_GAP(1);fi;
N5Example:=function(m,kind)
    local f,a,b,t,g;
    f:=FreeGroup(3);a:=f.1;b:=f.2;t:=f.3;
    g:=NilpotentQuotient(f/[Comm(a,b)/t,t^m,Comm(a,t),Comm(b,t)],2);
    if kind=1 then return DirectProduct(g,AbelianPcpGroup([0]));fi;
    if kind=2 then return DirectProduct(g,AbelianPcpGroup([2]));fi;
    return g;
end;
N5Product:=function(g,gens,coords)
    local x,i;
    x:=One(g);
    for i in [1..Length(gens)] do x:=x*gens[i]^coords[i];od;
    return x;
end;
N5Word:=function(g,gens,word)
    local x,s;
    x:=One(g);
    for s in word do x:=x*gens[AbsInt(s)]^SignInt(s);od;
    return x;
end;
