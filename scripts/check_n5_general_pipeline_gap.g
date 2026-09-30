Read("scripts/n5_general_pipeline.g");
Read("scripts/n5_general_support_fixtures.g");
Read("research/certificates/N5-general-pipeline/replay-v1.g");
N5VerifyGeneralFactors:=function(g,input,result)
    local pc,zgens,answer,branch,p,parts,groups,centers,side,proj,images,lifts,j,rels,r,a,b;
    pc:=GeneratorsOfPcp(Pcp(g));
    if RelativeOrdersOfPcp(Pcp(g))<>input.pcp_relative_orders then Error("native pcp basis changed");fi;
    zgens:=List(input.central_generator_exponents,v->N5GeneralOrderedWord(g,pc,v));
    if Subgroup(g,zgens)<>Centre(g) then Error("central basis changed");fi;
    for answer in result.branches do
        if not answer.answer then continue;fi;
        branch:=input.branches[answer.branch];p:=answer.central_projection;parts:=branch.parts;
        groups:=[];centers:=[];
        for side in [1,2] do
            proj:=p;
            if side=2 then proj:=IdentityMat(Length(p),Rationals)-p;fi;
            images:=List([1..Length(zgens)],j->N5GeneralOrderedWord(g,zgens,List(proj,row->row[j])));
            Add(centers,Subgroup(g,images));
            lifts:=List(parts[side].lifts,v->N5GeneralOrderedWord(g,pc,v));
            for j in [1..Length(lifts)] do
                lifts[j]:=lifts[j]*N5GeneralOrderedWord(g,zgens,answer.corrections[side][j]);
            od;
            for r in parts[side].relators do
                if not N5GeneralLetterWord(g,lifts,r) in centers[side] then
                    Error("corrected relation outside chosen central factor");fi;
            od;
            Add(groups,Subgroup(g,Concatenation(images,lifts)));
        od;
        a:=groups[1];b:=groups[2];
        if IsTrivial(a) or IsTrivial(b) or not IsTrivial(Intersection(a,b)) or
           not IsTrivial(CommutatorSubgroup(a,b)) or ClosureGroup(a,b)<>g then
            Error("returned factors do not give a nontrivial direct product");fi;
        if Intersection(a,Centre(g))<>centers[1] or Intersection(b,Centre(g))<>centers[2] then
            Error("factor center intersection mismatch");fi;
    od;
    return Number(result.branches,r->r.answer);
end;
N5CheckGeneralPipeline:=function()
    local fixtures,i,input,result,total,count;
    fixtures:=N5SupportFixtures();total:=0;
    for i in [1..Length(fixtures)] do
        input:=N5GeneralPipelineInputs[i];result:=N5GeneralPipelineResults[i];
        if fixtures[i].name<>input.name or input.name<>result.name then Error("fixture binding");fi;
        count:=N5VerifyGeneralFactors(fixtures[i].group,input,result);total:=total+count;
        if (count>0)<>result.answer then Error("missing positive branch");fi;
        Print(input.name,": native direct products checked ",count,"\n");
    od;
    Print("PASS N5 general pipeline GAP factors: ",Length(fixtures)," groups; ",total," decompositions\n");
end;
N5CheckGeneralPipeline();
QUIT;
