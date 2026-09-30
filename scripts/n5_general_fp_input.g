Read("scripts/n5_general_malcev_input.g");
if LoadPackage("nq")<>true then Error("nq required");fi;

N5GeneralNativeSignature:=function(g)
    local pc,iso,fp;
    pc:=Pcp(g);iso:=IsomorphismFpGroup(g);fp:=Image(iso);
    return rec(relative_orders:=RelativeOrdersOfPcp(pc),
        presentation_generator_exponents:=List(GeneratorsOfGroup(fp),x->ExponentsByPcp(pc,PreImagesRepresentative(iso,x))),
        presentation_relators:=List(RelatorsOfFpGroup(fp),LetterRepAssocWord));
end;

N5FpNilpotent:=function(p,promisedNilpotent)
    local ep,a,orders,cyclic,model,pc;
    if promisedNilpotent<>true then return fail;fi;
    if not IsFpGroup(p) then Error("finite presentation required");fi;
    if Length(GeneratorsOfGroup(p))=0 then
        a:=AbelianPcpGroup([]);ep:=GroupHomomorphismByImagesNC(p,a,[],[]);
        SetIsSurjective(ep,true);cyclic:=true;
    else
        ep:=NqEpimorphismNilpotentQuotient(p,1);a:=Image(ep);
        orders:=Filtered(RelativeOrdersOfPcp(Pcp(a,"snf")),d->d<>1);
        cyclic:=Length(orders)<=1;
        # Nilpotency + cyclic abelianization implies cyclicity; otherwise
        # no class parameter means compute the largest nilpotent quotient.
        if not cyclic then ep:=NqEpimorphismNilpotentQuotient(p);fi;
    fi;
    model:=N5GeneralMalcevInput(Image(ep));
    model.presentation:=p;model.epimorphism:=ep;model.used_cyclic_abelianization:=cyclic;
    pc:=Pcp(model.group);
    model.data.original_generator_images:=List(GeneratorsOfGroup(p),x->ExponentsByPcp(pc,Image(ep,x)));
    model.data.native_signature:=N5GeneralNativeSignature(model.group);
    return model;
end;
