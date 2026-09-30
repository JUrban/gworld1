# Finite-presentation and native pcp input for the N5 class-two pipeline.
# The fp interface REQUIRES the class-at-most-two promise. It does not
# recognize that promise by looking at a nilpotent quotient.
if LoadPackage("nq")<>true or LoadPackage("polycyclic")<>true then
    Error("nq and polycyclic required");
fi;

N5InputWord:=function(g,gens,v)
    local w,i;
    w:=One(g);
    for i in [1..Length(gens)] do w:=w*gens[i]^v[i];od;
    return w;
end;

N5ClassTwoCoordinates:=function(g)
    local z,zpc,qpc,zo,qo,zi,qi,zgens,qgens,central,encode,decode,data,
          beta,powers,i,j,all;
    if not IsPcpGroup(g) then Error("native pcp group required");fi;
    z:=Centre(g);
    if not IsSubgroup(z,DerivedSubgroup(g)) then return fail;fi;
    zpc:=Pcp(z,"snf");qpc:=Pcp(g,z,"snf");
    zo:=RelativeOrdersOfPcp(zpc);qo:=RelativeOrdersOfPcp(qpc);
    zi:=Concatenation(Filtered([1..Length(zo)],i->zo[i]=0),
                     Filtered([1..Length(zo)],i->zo[i]>1));
    qi:=Concatenation(Filtered([1..Length(qo)],i->qo[i]=0),
                     Filtered([1..Length(qo)],i->qo[i]>1));
    zgens:=GeneratorsOfPcp(zpc){zi};qgens:=GeneratorsOfPcp(qpc){qi};
    zo:=zo{zi};qo:=qo{qi};all:=Concatenation(qgens,zgens);
    central:=function(w)
        local e;
        if not w in z then Error("noncentral input to central coordinates");fi;
        e:=ExponentsByPcp(zpc,w){zi};
        if N5InputWord(g,zgens,e)<>w then Error("central coordinate recovery");fi;
        return e;
    end;
    decode:=v->N5InputWord(g,all,v);
    encode:=function(w)
        local e,tail,v;
        if not w in g then Error("coordinate input outside group");fi;
        e:=ExponentsByPcp(qpc,w){qi};
        tail:=N5InputWord(g,qgens,e)^-1*w;
        v:=Concatenation(e,central(tail));
        if decode(v)<>w then Error("whole coordinate recovery");fi;
        return v;
    end;
    beta:=List(qgens,x->List(qgens,y->central(Comm(x,y))));
    powers:=[];
    for i in [1..Length(qo)] do
        if qo[i]=0 then Add(powers,List(zo,d->0));
        else Add(powers,central(qgens[i]^qo[i]));fi;
    od;
    data:=rec(quotient_orders:=qo,center_orders:=zo,beta:=beta,powers:=powers);
    return rec(group:=g,center:=z,generators:=all,data:=data,
               encode:=encode,decode:=decode);
end;

N5FpClassTwo:=function(p,promisedClassAtMostTwo)
    local ep,a,orders,cyclic,model;
    if promisedClassAtMostTwo<>true then return fail;fi;
    if not IsFpGroup(p) then Error("finite presentation required");fi;
    if Length(GeneratorsOfGroup(p))=0 then
        a:=AbelianPcpGroup([]);
        ep:=GroupHomomorphismByImagesNC(p,a,[],[]);
        SetIsSurjective(ep,true);
        model:=N5ClassTwoCoordinates(a);
        model.presentation:=p;model.epimorphism:=ep;
        model.used_cyclic_abelianization:=true;
        return model;
    fi;
    # A class-two group with cyclic abelianization is cyclic: write each
    # generator as a power of one lift times a central derived element.
    # This also avoids the installed nq cyclic/class-two assertion failure.
    ep:=NqEpimorphismNilpotentQuotient(p,1);a:=Image(ep);
    orders:=Filtered(RelativeOrdersOfPcp(Pcp(a,"snf")),d->d<>1);
    cyclic:=Length(orders)<=1;
    if not cyclic then ep:=NqEpimorphismNilpotentQuotient(p,2);fi;
    model:=N5ClassTwoCoordinates(Image(ep));
    if model=fail then Error("nilpotent quotient failed its class-two check");fi;
    model.presentation:=p;model.epimorphism:=ep;
    model.used_cyclic_abelianization:=cyclic;
    return model;
end;

N5InputFactors:=function(model,result)
    local branch,factors,words;
    if not result.answer then return fail;fi;
    branch:=result.branches[result.witness_branch+1];
    factors:=List(branch.factor_generators,vs->
        Subgroup(model.group,List(vs,model.decode)));
    if IsTrivial(factors[1]) or IsTrivial(factors[2]) or
       not IsTrivial(CommutatorSubgroup(factors[1],factors[2])) or
       not IsTrivial(Intersection(factors[1],factors[2])) or
       ClosureGroup(factors[1],factors[2])<>model.group then
        Error("returned generators do not give a nontrivial direct product");
    fi;
    words:=List(branch.factor_generators,vs->List(vs,v->
        PreImagesRepresentative(model.epimorphism,model.decode(v))));
    if not ForAll([1,2],i->List(words[i],w->Image(model.epimorphism,w))=
            List(branch.factor_generators[i],model.decode)) then
        Error("factor words do not map to returned elements");
    fi;
    return rec(factors:=factors,words:=words);
end;
