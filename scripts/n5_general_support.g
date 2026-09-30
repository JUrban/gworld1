# Rational-support preimages, using column Lie coordinates and actual
# conjugation to upper unitriangular integral matrices.
Read("scripts/n5_general_malcev_input.g");

N5SupportImageFlag:=function(adjoints)
    local n,levels,current,next,a,v,rows,level;
    n:=Length(adjoints);levels:=[];current:=IdentityMat(n,Rationals);
    while Length(current)>0 do
        Add(levels,current);next:=[];
        for a in adjoints do for v in current do Add(next,v*TransposedMat(a));od;od;
        if RankMat(next)=0 then current:=[];
        else current:=BasisVectors(Basis(VectorSpace(Rationals,next)));fi;
        if Length(levels)>n then Error("adjoint image filtration not nilpotent");fi;
    od;
    rows:=[];
    for level in Reversed(levels) do for v in level do
        if RankMat(Concatenation(rows,[v]))>Length(rows) then Add(rows,v);fi;
    od;od;
    if Length(rows)<>n then Error("incomplete triangularizing basis");fi;
    return TransposedMat(rows);
end;

N5RationalSupport:=function(model,c,p)
    local g,h,adjoints,change,inverse,gens,logs,mats,x,v,a,n,i,j,den,d,
          integral,target,imageIso,images,hom,kernel,z,kmap,k,support;
    g:=model.group;h:=model.data.hirsch_length;gens:=GeneratorsOfGroup(g);
    z:=Centre(g);kmap:=NaturalHomomorphismByNormalSubgroup(g,z);k:=Image(kmap);
    if h=0 then
        return rec(kernel:=g,quotient:=kmap,support:=k,
            data:=rec(matrix_dimension:=0,denominator:=1,image_hirsch_length:=0,
                kernel_hirsch_length:=HirschLength(g),support_hirsch_length:=HirschLength(k)));
    fi;
    if p*p<>p then Error("support input not a projection");fi;
    adjoints:=List(c,TransposedMat);
    for a in adjoints do
        if p*a<>a*p then Error("support projection not in centroid");fi;
    od;
    change:=N5SupportImageFlag(adjoints);inverse:=change^-1;
    logs:=List(gens,model.log_of);mats:=[];
    for x in logs do
        v:=x*TransposedMat(IdentityMat(h,Rationals)-p);
        a:=Sum([1..h],i->v[i]*adjoints[i]);
        Add(mats,inverse*N5MatrixExp(a)*change);
    od;
    for a in mats do for i in [1..h] do for j in [1..i] do
        if (i=j and a[i][j]<>1) or (i<>j and a[i][j]<>0) then
            Error("support matrix not upper unitriangular");
        fi;
    od;od;od;
    den:=Lcm(List(Concatenation(List(mats,Concatenation)),DenominatorRat));
    d:=DiagonalMat(List([0..h-1],i->den^i));
    integral:=List(mats,a->d^-1*a*d);
    if not ForAll(integral,a->ForAll(Concatenation(a),IsInt)) then
        Error("denominator conjugation failed");
    fi;
    if ForAll(integral,a->a=IdentityMat(h,Rationals)) then
        target:=AbelianPcpGroup([]);images:=List(gens,x->One(target));
    else
        imageIso:=IsomorphismUpperUnitriMatGroupPcpGroup(Group(integral,IdentityMat(h,Rationals)));
        target:=Image(imageIso);images:=List(integral,a->Image(imageIso,a));
    fi;
    hom:=GroupHomomorphismByImages(g,target,gens,images);
    if hom=fail then Error("support map does not respect presentation");fi;
    if Image(hom)<>target then Error("support map not onto constructed image");fi;
    kernel:=Kernel(hom);
    if not IsSubgroup(kernel,z) or not IsSubgroup(kernel,model.torsion) then
        Error("support map does not kill center and torsion");
    fi;
    support:=Image(kmap,kernel);
    return rec(kernel:=kernel,quotient:=kmap,support:=support,homomorphism:=hom,
        data:=rec(matrix_dimension:=h,denominator:=den,
            image_hirsch_length:=HirschLength(target),kernel_hirsch_length:=HirschLength(kernel),
            support_hirsch_length:=HirschLength(support),triangular_basis:=N5RationalData(change),
            integral_matrices:=integral));
end;
