if LoadPackage("nq")<>true or LoadPackage("polycyclic")<>true then FORCE_QUIT_GAP(1);fi;
N5CheckBound:=function(a,b)
    local g,z,projection,k,s,y,preimages,i,factor,t,qmap,q,zmap,composite,ki,bound;
    g:=DirectProduct(a,b);z:=Centre(g);projection:=NaturalHomomorphismByNormalSubgroup(g,z);
    k:=Image(projection);s:=TorsionSubgroup(k);y:=[];preimages:=[];
    for i in [1,2] do Add(y,Image(projection,Image(Embedding(g,i))));od;
    for i in [1,2] do
        # The preimage of rational support i is the kernel of projection to
        # the OTHER torsion-free quotient modulo its centre.
        if i=1 then factor:=b;else factor:=a;fi;
        t:=TorsionSubgroup(factor);qmap:=NaturalHomomorphismByNormalSubgroup(factor,t);q:=Image(qmap);
        zmap:=NaturalHomomorphismByNormalSubgroup(q,Centre(q));
        composite:=Projection(g,3-i)*qmap*zmap;
        ki:=Image(projection,Kernel(composite));
        if ki<>ClosureGroup(y[i],s) then Error("rational support preimage mismatch");fi;
        bound:=Index(ki,y[i]);
        if bound>Size(s) then Error("finite index bound failed");fi;
        Add(preimages,ki);
        Print("Support ",i,": index ",bound," <= torsion-kernel size ",Size(s),"\n");
    od;
    if Intersection(preimages[1],preimages[2])<>s then Error("kernel mismatch");fi;
    if Size(Intersection(y[1],y[2]))<>1 or ClosureGroup(y[1],y[2])<>k then Error("quotient decomposition");fi;
    return true;
end;
heis:=NilpotentQuotient(FreeGroup(2),2);;
class3:=NilpotentQuotient(FreeGroup(2),3);;
d8:=Image(IsomorphismPcpGroup(SmallGroup(8,3)));;
q8:=Image(IsomorphismPcpGroup(SmallGroup(8,4)));;
N5CheckBound(heis,d8);
N5CheckBound(DirectProduct(class3,AbelianPcpGroup([4])),DirectProduct(heis,q8));
N5CheckBound(DirectProduct(heis,d8),DirectProduct(class3,q8));
Print("PASS N5 rational support bounds: 3 products, 6 support preimages\n");
QUIT;
