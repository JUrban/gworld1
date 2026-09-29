# Independent actual group verification and exact obstruction polynomials.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
Read("research/certificates/N9-Heisenberg/fixtures-v1.g");
(function()
    local build,word,r,forms,d,s,data,g,y,h1,h2,c,images,i,l,hom,h,
          checks,ng,q,ring,vars,m,pf,minors,a,b,kind;
    build:=function(forms)
        local d,s,f,x,rel,i,j,l,w,p,ep,g,y;
        d:=Length(forms[1]); s:=Length(forms); f:=FreeGroup(d+s);
        x:=GeneratorsOfGroup(f); rel:=[];
        for i in [1..d+s] do for j in [i+1..d+s] do
            w:=Comm(x[i],x[j]);
            if j<=d then
                for l in [1..s] do w:=w*x[d+l]^-forms[l][i][j]; od;
            fi;
            Add(rel,w);
        od; od;
        p:=f/rel; ep:=NqEpimorphismNilpotentQuotient(p,2);
        g:=Image(ep); y:=List(GeneratorsOfGroup(p),a->Image(ep,a));
        if HirschLength(g)<>d+s or Size(TorsionSubgroup(g))<>1 then Error("Presentation"); fi;
        return [g,y];
    end;
    word:=function(y,a,z)
        local w,i;
        w:=One(y[1]);
        for i in [1..Length(a)] do w:=w*y[i]^a[i]; od;
        for i in [1..Length(z)] do w:=w*y[Length(a)+i]^z[i]; od;
        return w;
    end;
    checks:=0;
    for r in N9Positive do
        forms:=r[1]; d:=Length(forms[1]); s:=Length(forms);
        data:=build(forms); g:=data[1]; y:=data[2];
        h1:=word(y,r[2],r[3]); h2:=word(y,r[4],r[5]); c:=Comm(h1,h2);
        h:=Subgroup(g,[h1,h2]);
        if c=One(g) or HirschLength(h)<>3 then Error("Heisenberg subgroup"); fi;
        images:=List([1..d],i->h1^r[7][i]*h2^r[8][i]*c^r[9][i]);
        Append(images,List(r[6],l->c^l));
        for i in [1..d+s] do
            if images[i]<>word(y,r[10][i][1],r[10][i][2]) then Error("Coordinate comparison"); fi;
        od;
        hom:=GroupHomomorphismByImages(g,g,y,images);
        if hom=fail or Image(hom,h1)<>h1 or Image(hom,h2)<>h2 or Image(hom)<>h then
            Error("Not a retraction");
        fi;
        for i in [1..d+s] do
            if Image(hom,images[i])<>images[i] then Error("Not idempotent"); fi;
        od;
        checks:=checks+1;
    od;
    Print("Actual GAP/nq retractions checked: ",checks,"\n");
    for ng in N9Negative do
        kind:=ng[1]; forms:=ng[2]; a:=ng[3]; b:=ng[4];
        d:=Length(a); s:=Length(forms); data:=build(forms); g:=data[1]; y:=data[2];
        h1:=word(y,a,List([1..s],i->0)); h2:=word(y,b,List([1..s],i->0));
        c:=Comm(h1,h2); q:=List(forms,m->a*m*b);
        if c=One(g) or c<>word(y,List([1..d],i->0),q) then Error("Negative commutator"); fi;
        ring:=PolynomialRing(Rationals,s); vars:=IndeterminatesOfPolynomialRing(ring);
        m:=Sum([1..s],l->vars[l]*forms[l]);
        if d=4 then pf:=m[1][2]*m[3][4]-m[1][3]*m[2][4]+m[1][4]*m[2][3]; fi;
        if kind="product_2_3" then
            if pf<>vars[1]*vars[2] or q<>[2,3] then Error("Product obstruction"); fi;
            minors:=[];
            for i in [1..d] do for l in [i+1..d] do Add(minors,a[i]*b[l]-a[l]*b[i]); od; od;
            if Gcd(minors)<>1 or Gcd(q)<>1 then Error("Primitive lattice controls"); fi;
        elif kind="symplectic_rank4" then
            if pf<>vars[1]^2 or q<>[1] then Error("Symplectic obstruction"); fi;
        elif kind="anisotropic_pfaffian" then
            if pf<>vars[1]^2+vars[2]^2 or q<>[1,0] then Error("Anisotropic obstruction"); fi;
        elif kind="central_root" then
            if q<>[2] then Error("Central divisibility"); fi;
        else Error("Unknown negative case"); fi;
        Print("Exact obstruction polynomial checked: ",kind," central vector ",q,"\n");
    od;
    Print("PASS independent GAP N9 Heisenberg retracts and obstructions\n");
end)();
QUIT;
