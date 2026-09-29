# New structural checks of the already archived toy circuit.
# This is not a search for retractions or a universal undecidability proof.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
Read("research/certificates/N9-fixed-circuit/fixtures-v1.g");
(function()
    local d,s,forms,kernel,ui,rank,right,pairs,l,k,i,j,b,
          r0,r1,mu0,mu1,poln,q,mu,interpolant,pf,
          f,x,rels,w,ep,g,gens,zsub,der,abmap,ab,
          n,a,bn,c,h,hd,hab,ainv,cinv,neg,negativeAb;
    d:=N9Circuit[1]; rank:=N9Circuit[3]; ui:=N9Circuit[6];
    kernel:=N9Circuit[7]; forms:=N9Circuit[8]; s:=Length(forms);
    pairs:=Combinations([1..d],2);
    if d<>14 or s<>68 then Error("Toy dimensions"); fi;
    right:=List(ui,row->row{[rank+1..Length(pairs)]});
    if kernel*right<>IdentityMat(s) then Error("Integral right inverse"); fi;
    for l in [1..s] do
        b:=NullMat(d,d);
        for k in [1..Length(pairs)] do
            i:=pairs[k][1]; j:=pairs[k][2];
            b[i][j]:=kernel[l][k]; b[j][i]:=-kernel[l][k];
        od;
        if b<>forms[l] then Error("Form coordinates"); fi;
    od;
    r0:=First(N9CircuitRetractions,r->r[1]=0);
    r1:=First(N9CircuitRetractions,r->r[1]=1 and r[2]=0);
    mu0:=r0[3]; mu1:=r1[3];
    if Sum([1..s],l->mu0[l]*forms[l])<>r0[8] or
       Sum([1..s],l->mu1[l]*forms[l])<>r1[8] or
       r0[8][1][2]<>1 or r1[8][1][2]<>1 or
       r0[8][1][3]<>0 or r1[8][1][3]<>3 then Error("Two witnesses"); fi;
    poln:=Indeterminate(Rationals,"n");
    q:=List(forms,b->(3*poln+1)*b[1][2]-b[1][3]);
    mu:=(1-poln)*mu0+poln*mu1;
    Print("Polynomial pairing: ",Sum([1..s],l->mu[l]*q[l]),
          "; equals scalar 1: ",Sum([1..s],l->mu[l]*q[l])=1,"\n");
    if Sum([1..s],l->mu[l]*q[l])<>One(poln) then Error("Polynomial unit pairing"); fi;
    interpolant:=(1-poln)*r0[8]+poln*r1[8];
    pf:=interpolant[1][2]*interpolant[3][4]
        -interpolant[1][3]*interpolant[2][4]
        +interpolant[1][4]*interpolant[2][3];
    if pf<>9*poln*(1-poln) then Error("Interpolation rank obstruction"); fi;
    if Sum([1..s],l->mu[l]*(2*q[l]))=One(poln) then Error("Doubled-vector control"); fi;
    Print("All-parameter polynomial unit pairing and integral right inverse checked\n");
    Print("Interpolated witness Pfaffian is 9*n*(1-n), not identically zero\n");
    f:=FreeGroup(d+s); x:=GeneratorsOfGroup(f); rels:=[];
    for i in [1..d+s] do for j in [i+1..d+s] do
        w:=Comm(x[i],x[j]);
        if j<=d then
            for l in [1..s] do w:=w*x[d+l]^-forms[l][i][j]; od;
        fi;
        Add(rels,w);
    od; od;
    f:=f/rels; ep:=NqEpimorphismNilpotentQuotient(f,2);
    g:=Image(ep); gens:=List(GeneratorsOfGroup(f),x->Image(ep,x));
    if HirschLength(g)<>d+s or Size(TorsionSubgroup(g))<>1 then Error("Toy group"); fi;
    zsub:=Subgroup(g,gens{[d+1..d+s]}); der:=DerivedSubgroup(g);
    if zsub<>der or not IsAbelian(der) then Error("Derived group equals central lattice"); fi;
    abmap:=NaturalHomomorphismByNormalSubgroup(g,der); ab:=Image(abmap);
    if AbelianInvariants(ab)<>List([1..d],i->0) then Error("Free abelianization"); fi;
    for n in [-1,0,1,2,3,4,9] do
        a:=gens[1]; bn:=gens[2]^(3*n+1)*gens[3]^-1;
        c:=Comm(a,bn); h:=Subgroup(g,[a,bn]); hd:=DerivedSubgroup(h);
        if HirschLength(h)<>3 or hd<>Subgroup(g,[c]) or
           Intersection(h,der)<>hd then Error("Lower-central intersection"); fi;
        hab:=Image(abmap,h);
        ainv:=AbelianInvariants(ab/hab); cinv:=AbelianInvariants(der/hd);
        if ainv<>List([1..d-2],i->0) or
           cinv<>List([1..s-1],i->0) then Error("Primitive graded subgroups"); fi;
        q:=List(forms,b->(3*n+1)*b[1][2]-b[1][3]);
        if Gcd(q)<>1 or Gcd(2*q)<>2 then Error("Primitive and doubled vectors"); fi;
        Print("n=",n,": rank-three subgroup, exact intersection and both torsion-free graded quotients\n");
    od;
    # Explicit nonisolated control, using the final n=9 subgroup.
    neg:=Subgroup(g,[a^2,bn]);
    if a in neg or not a^2 in neg then Error("Nonisolated control"); fi;
    negativeAb:=AbelianInvariants(ab/Image(abmap,neg));
    if not 2 in negativeAb then Error("Nonprimitive abelian control"); fi;
    Print("Nonisolated control <a^2,b> has a missing square root and abelian torsion 2\n");
    Print("PASS N9 isolated-input structural checks\n");
end)();
QUIT;
