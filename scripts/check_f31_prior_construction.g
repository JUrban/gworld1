LoadPackage("fga");;
(function()
    local n,F,a,b,D,x,g,h,colors,common,i,v,w,label,edges,e,basis,G,H,A,
          eqcount,counter,phi,psi;
    eqcount:=0;
    for n in [2..12] do
        F:=FreeGroup("a","b");a:=F.1;b:=F.2;
        D:=FreeGroup(n);x:=GeneratorsOfGroup(D);
        colors:=List([0..n-1],i->a^-i*b^i);
        common:=List([1..n-1],i->colors[i+1]^2);
        g:=Concatenation([a],common);h:=Concatenation([b],common);
        G:=Subgroup(F,g);H:=Subgroup(F,h);
        if RankOfFreeGroup(G)<>n or RankOfFreeGroup(H)<>n then Error("Image ranks");fi;
        phi:=GroupHomomorphismByImages(D,F,x,g);
        psi:=GroupHomomorphismByImages(D,F,x,h);
        basis:=Concatenation(x{[2..n]},List([1..n-1],i->x[1]^i*x[i+1]*x[1]^-i));
        A:=Subgroup(D,basis);
        if RankOfFreeGroup(A)<>2*n-2 then Error("Colored subgroup rank");fi;
        if ForAny(basis,w->Image(phi,w)<>Image(psi,w)) then Error("Equalizer membership");fi;
        if Image(phi,x[1])=Image(psi,x[1]) then Error("Nonmember control");fi;
        edges:=List([1..n-1],i->[i,1,i+1]);
        for i in [1..n-1] do Add(edges,[1,i+1,1]);Add(edges,[i+1,i+1,i+1]);od;
        for e in edges do
            v:=e[1];label:=e[2];w:=e[3];
            if g[label]<>colors[v]*h[label]*colors[w]^-1 then Error("Coloring equation");fi;
            eqcount:=eqcount+1;
        od;
        if Length(Set(colors))<>n then Error("Injective coloring");fi;
        Print("n=",n," image ranks=",n,",",n," free-factor candidate rank=",2*n-2,"\n");
    od;
    F:=FreeGroup(2);a:=F.1;b:=F.2;
    counter:=Subgroup(F,[a^2,b,a*b*a^-1]);
    if RankOfFreeGroup(counter)<>3 or RankOfFreeGroup(F)<>2 then Error("Rank control");fi;
    if eqcount<>198 then Error("Coverage");fi;
    Print("198 coloring equations; rank3-in-rank2 negative control\n");
    Print("PASS independent GAP prior F31 construction\n");
end)();
QUIT;
