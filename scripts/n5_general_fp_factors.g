Read("scripts/n5_general_factor_checker.g");
N5GeneralFpFactors:=function(model,input,result)
    local g,pc,zgens,answer,p,branch,factors,words,side,proj,images,lifts,j;
    if not result.answer then return fail;fi;
    g:=model.group;pc:=GeneratorsOfPcp(Pcp(g));
    N5VerifyGeneralFactors(g,input,result);
    zgens:=List(input.central_generator_exponents,v->N5GeneralOrderedWord(g,pc,v));
    answer:=result.branches[result.witness_branch];branch:=input.branches[answer.branch];
    p:=answer.central_projection;factors:=[];words:=[];
    for side in [1,2] do
        proj:=p;if side=2 then proj:=IdentityMat(Length(p),Rationals)-p;fi;
        images:=List([1..Length(zgens)],j->N5GeneralOrderedWord(g,zgens,List(proj,row->row[j])));
        lifts:=List(branch.parts[side].lifts,v->N5GeneralOrderedWord(g,pc,v));
        for j in [1..Length(lifts)] do
            lifts[j]:=lifts[j]*N5GeneralOrderedWord(g,zgens,answer.corrections[side][j]);
        od;
        images:=Filtered(Concatenation(images,lifts),x->x<>One(g));
        Add(factors,Subgroup(g,images));
        Add(words,List(images,x->PreImagesRepresentative(model.epimorphism,x)));
        if List(words[side],x->Image(model.epimorphism,x))<>images then
            Error("original generator factor-word binding");fi;
    od;
    return rec(factors:=factors,words:=words);
end;
