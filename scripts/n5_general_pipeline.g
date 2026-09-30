Read("scripts/n5_general_support.g");

N5GeneralOrderedWord:=function(g,gens,v)
    local w,i;
    w:=One(g);
    for i in [1..Length(gens)] do w:=w*gens[i]^v[i];od;
    return w;
end;
N5GeneralLetterWord:=function(g,gens,letters)
    local w,i;
    w:=One(g);
    for i in letters do w:=w*gens[AbsInt(i)]^SignInt(i);od;
    return w;
end;

N5BoundedNormalSupports:=function(k,ki,s)
    local bound,iso,fp,iterator,sub,h,out,examined;
    bound:=Size(s);out:=[];examined:=0;
    if bound=1 then return rec(subgroups:=[ki],examined:=1);fi;
    iso:=IsomorphismFpGroup(ki);fp:=Image(iso);
    iterator:=LowIndexSubgroupsFpGroupIterator(fp,bound);
    while not IsDoneIterator(iterator) do
        sub:=NextIterator(iterator);examined:=examined+1;
        h:=Subgroup(k,List(GeneratorsOfGroup(sub),x->PreImagesRepresentative(iso,x)));
        if Index(ki,h)>bound then Error("low-index enumerator exceeded bound");fi;
        # Every genuine direct factor of K is normal in K, hence in Ki;
        # its conjugacy class in Ki is a singleton and is not omitted.
        if IsNormal(k,h) and ClosureGroup(h,s)=ki then Add(out,h);fi;
    od;
    return rec(subgroups:=out,examined:=examined);
end;

N5GeneralCentralData:=function(model,c,projections)
    local g,z,zpc,orders,positions,zgens,pc,kmap,k,s,subsets,seen,cachekeys,cache,
          getsubs,subset,p,h,ki1,ki2,u,v,stats,branches,allindices,idx,normal,
          y1,y2,x1,x2,parts,side,iso,fp,lifts,rels,e,defects,rel,row,i,value;
    g:=model.group;h:=model.data.hirsch_length;pc:=Pcp(g);
    z:=Centre(g);zpc:=Pcp(z,"snf");orders:=RelativeOrdersOfPcp(zpc);
    positions:=Concatenation(Filtered([1..Length(orders)],i->orders[i]=0),
                            Filtered([1..Length(orders)],i->orders[i]>1));
    orders:=orders{positions};zgens:=GeneratorsOfPcp(zpc){positions};
    kmap:=NaturalHomomorphismByNormalSubgroup(g,z);k:=Image(kmap);s:=TorsionSubgroup(k);
    cachekeys:=[];cache:=[];
    getsubs:=function(ki)
        local pos,found;
        pos:=Position(cachekeys,ki);
        if pos<>fail then return cache[pos].subgroups;fi;
        found:=N5BoundedNormalSupports(k,ki,s);
        Add(cachekeys,ki);Add(cache,found);
        return found.subgroups;
    end;
    seen:=[];branches:=[];allindices:=[];
    stats:=rec(rational_partitions:=0,distinct_support_pairs:=0,subgroup_pairs:=0,
               not_direct_product:=0,cross_commutator_obstructions:=0);
    for subset in Combinations([1..Length(projections)]) do
        stats.rational_partitions:=stats.rational_partitions+1;
        if h=0 then p:=[];else p:=NullMat(h,h,Rationals);fi;
        for i in subset do p:=p+projections[i];od;
        u:=N5RationalSupport(model,c,p);
        if h=0 then v:=u;else v:=N5RationalSupport(model,c,IdentityMat(h,Rationals)-p);fi;
        ki1:=Image(kmap,u.kernel);ki2:=Image(kmap,v.kernel);
        if [ki1,ki2] in seen then continue;fi;
        Add(seen,[ki1,ki2]);stats.distinct_support_pairs:=stats.distinct_support_pairs+1;
        idx:=Index(k,ClosureGroup(ki1,ki2));Add(allindices,idx);
        if idx<>1 then continue;fi;
        for y1 in getsubs(ki1) do for y2 in getsubs(ki2) do
            stats.subgroup_pairs:=stats.subgroup_pairs+1;
            if not IsTrivial(Intersection(y1,y2)) or ClosureGroup(y1,y2)<>k or
               not IsTrivial(CommutatorSubgroup(y1,y2)) then
                stats.not_direct_product:=stats.not_direct_product+1;continue;
            fi;
            x1:=PreImage(kmap,y1);x2:=PreImage(kmap,y2);
            if not IsTrivial(CommutatorSubgroup(x1,x2)) then
                stats.cross_commutator_obstructions:=stats.cross_commutator_obstructions+1;continue;
            fi;
            parts:=[];
            for side in [y1,y2] do
                if IsTrivial(side) then
                    Add(parts,rec(exponents:=[],defects:=[],require_nontrivial_center:=true,
                                  lifts:=[],relators:=[]));continue;
                fi;
                iso:=IsomorphismFpGroup(side);fp:=Image(iso);
                lifts:=List(GeneratorsOfGroup(fp),a->PreImagesRepresentative(kmap,PreImagesRepresentative(iso,a)));
                rels:=List(RelatorsOfFpGroup(fp),LetterRepAssocWord);e:=[];defects:=[];
                for rel in rels do
                    row:=List(lifts,a->0);
                    for i in rel do row[AbsInt(i)]:=row[AbsInt(i)]+SignInt(i);od;
                    Add(e,row);value:=N5GeneralLetterWord(g,lifts,rel);
                    if not value in z then Error("lifted relation is not central");fi;
                    Add(defects,ExponentsByPcp(zpc,value){positions});
                od;
                Add(parts,rec(exponents:=e,defects:=defects,require_nontrivial_center:=false,
                    lifts:=List(lifts,a->ExponentsByPcp(pc,a)),relators:=rels));
            od;
            Add(branches,rec(partition:=subset,parts:=parts));
        od;od;
    od;
    stats.enumerations:=List(cache,x->rec(conjugacy_classes:=x.examined,
        normal_full_support_subgroups:=Length(x.subgroups)));
    stats.support_generation_indices:=allindices;
    return rec(center_orders:=orders,central_generator_exponents:=List(zgens,a->ExponentsByPcp(pc,a)),
        pcp_relative_orders:=RelativeOrdersOfPcp(pc),torsion_kernel_order:=Size(s),
        branches:=branches,statistics:=stats);
end;
