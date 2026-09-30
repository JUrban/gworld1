# Native nilpotent pcp group -> rational Malcev Lie algebra, all classes.
# Exact arithmetic; the installed Polycyclic matrix representation is trusted
# algebraic machinery. This does not implement the complete N5 group decision.
if LoadPackage("polycyclic")<>true then Error("polycyclic required");fi;

N5MatrixLog:=function(m)
    local n,u,p,l,k;
    n:=Length(m);u:=m-IdentityMat(n,Rationals);p:=u;l:=0*u;
    for k in [1..n-1] do l:=l+(-1)^(k+1)*p/k;p:=p*u;od;
    if p<>0*u then Error("matrix is not unipotent of asserted degree");fi;
    return l;
end;

N5MatrixExp:=function(x)
    local n,p,e,k;
    n:=Length(x);p:=IdentityMat(n,Rationals);e:=p;
    for k in [1..n-1] do p:=p*x/k;e:=e+p;od;
    if p*x<>0*x then Error("matrix is not nilpotent of asserted degree");fi;
    return e;
end;

N5RationalData:=function(x)
    if IsInt(x) then return x;fi;
    if IsRat(x) then return String(x);fi;
    if IsList(x) then return List(x,N5RationalData);fi;
    Error("expected rational scalar or array");
end;

N5GeneralMalcevInput:=function(g)
    local t,quotient,q,series,q0,back,rho,gs,mats,logs,flat,basis,c,i,j,
          n,h,coordinates,matrixOf,logOf,checks,w,a,b,v,data;
    if not IsPcpGroup(g) or not IsNilpotentGroup(g) then
        Error("native nilpotent pcp group required");
    fi;
    t:=TorsionSubgroup(g);
    quotient:=NaturalHomomorphismByNormalSubgroup(g,t);q:=Image(quotient);
    h:=HirschLength(q);
    if h=0 then
        if not IsTrivial(q) then Error("finite torsion-free quotient nontrivial");fi;
        return rec(group:=g,torsion:=t,quotient:=quotient,rational_group:=q,
            data:=rec(hirsch_length:=0,torsion_order:=Size(t),nilclass:=0,
                matrix_dimension:=1,relative_orders:=[],matrices:=[],logs:=[],
                structure_constants:=[],word_checks:=[]));
    fi;
    series:=UpperCentralSeriesOfGroup(q);
    if series[1]<>q or not IsTrivial(Last(series)) then
        Error("unexpected upper central series orientation");
    fi;
    q0:=PcpGroupBySeries(series,"snf");
    back:=q0!.bijection;
    if Source(back)<>q0 or Range(back)<>q then
        Error("unexpected rebase bijection direction");
    fi;
    if not ForAll(RelativeOrdersOfPcp(Pcp(q0)),d->d=0) then
        Error("upper central rebase retained finite relative orders");
    fi;
    gs:=GeneratorsOfGroup(q0);
    if Length(gs)<>h then Error("rebased generator count not Hirsch length");fi;
    rho:=UnitriangularMatrixRepresentation(q0);
    mats:=List(gs,x->Image(rho,x));n:=Length(mats[1]);
    if not IsMatrixRepresentation(q0,mats) then Error("matrix relation check");fi;
    logs:=List(mats,N5MatrixLog);flat:=List(logs,Concatenation);
    if RankMat(flat)<>h then Error("logarithms are linearly dependent");fi;
    basis:=Basis(VectorSpace(Rationals,flat),flat);
    coordinates:=function(x)
        local v;
        v:=Coefficients(basis,Concatenation(x));
        if v=fail or Sum([1..h],i->v[i]*logs[i])<>x then
            Error("matrix outside rational Malcev span");
        fi;
        return v;
    end;
    c:=List([1..h],i->List([1..h],j->coordinates(logs[i]*logs[j]-logs[j]*logs[i])));
    for i in [1..h] do
        if N5MatrixExp(logs[i])<>mats[i] then Error("exp/log round trip");fi;
        if Image(back,PreImagesRepresentative(back,Image(back,gs[i])))<>Image(back,gs[i]) then
            Error("rebase word round trip");
        fi;
    od;
    matrixOf:=w->Image(rho,PreImagesRepresentative(back,Image(quotient,w)));
    logOf:=w->coordinates(N5MatrixLog(matrixOf(w)));
    checks:=[];
    for i in [1..h] do
        j:=i mod h+1;a:=gs[i];b:=gs[j];
        for w in [a^-2*b^3,Comm(a,b),a*b^-1*a*b] do
            v:=N5MatrixLog(Image(rho,w));
            if N5MatrixExp(v)<>Image(rho,w) then Error("word round trip");fi;
            Add(checks,rec(exponents:=ExponentsByPcp(Pcp(q0),w),
                          matrix:=Image(rho,w),log_coordinates:=N5RationalData(coordinates(v))));
        od;
    od;
    data:=rec(hirsch_length:=h,torsion_order:=Size(t),nilclass:=NilpotencyClassOfGroup(q),
        matrix_dimension:=n,relative_orders:=RelativeOrdersOfPcp(Pcp(q0)),
        matrices:=mats,logs:=N5RationalData(logs),
        structure_constants:=N5RationalData(c),word_checks:=checks);
    return rec(group:=g,torsion:=t,quotient:=quotient,rational_group:=q,
        rebased_group:=q0,rebase_to_quotient:=back,matrix_representation:=rho,
        matrix_of:=matrixOf,log_of:=logOf,basis:=basis,log_matrices:=logs,data:=data);
end;
