# Native checks of an explicit all-rank written construction.
# Finite nilpotent examples supplement, not prove, the all-class argument.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
(function()
    local rank,f,x,k,w,images,i,j,t,letters,edges,cyclicEdges,cycle,
          signed,si,sj,left,right,counts,cls,fp,ep,n,ng,ni,map,
          a5,els,a,b,ug,vg,h,witness,phi,word;
    edges:=function(word)
        local a,res,i;
        a:=LetterRepAssocWord(word); res:=[];
        for i in [1..Length(a)-1] do
            AddSet(res,Set([a[i],-a[i+1]]));
        od;
        return res;
    end;
    for rank in [2..5] do
        f:=FreeGroup(rank); x:=GeneratorsOfGroup(f);
        k:=Product(x,a->a^2)*x[1];
        w:=k*x[2]*k^-1*x[2]^-1;
        if Length(k)<>2*rank+1 or Length(w)<>4*rank+4 then Error("Block lengths"); fi;
        cycle:=List([1..rank],i->Set([i,-i]));
        for i in [1..rank-1] do AddSet(cycle,Set([i,-(i+1)])); od;
        AddSet(cycle,Set([rank,-1])); cycle:=Set(cycle);
        if Length(cycle)<>2*rank or edges(k)<>cycle then Error("Spanning cycle"); fi;
        images:=[];
        for i in [1..rank] do
            t:=x[(i mod rank)+1];
            word:=x[i]^2*w*x[i]^-1*t*x[i]^-1*t^-1*x[i];
            letters:=LetterRepAssocWord(word);
            if Length(word)<>4*rank+11 or letters[1]<>i or
               letters[Length(letters)]<>i then Error("Protected ends"); fi;
            counts:=List(x,a->ExponentSumWord(word,a));
            if counts<>List([1..rank],j->KroneckerDelta(i,j)) then Error("Identity abelianization"); fi;
            if not IsSubset(edges(word),cycle) or not IsSubset(edges(word^-1),cycle) then
                Error("Protected internal cycle");
            fi;
            Add(images,word);
        od;
        signed:=Concatenation(images,List(images,a->a^-1));
        counts:=0;
        for si in [1..2*rank] do for sj in [1..2*rank] do
            left:=signed[si]; right:=signed[sj];
            if right<>left^-1 then
                if Length(left*right)<>Length(left)+Length(right) then Error("Boundary cancellation"); fi;
                counts:=counts+1;
            fi;
        od; od;
        # Positive control: the identity tuple has correct abelianization,
        # but lacks a spanning blocking cycle and contains primitives.
        if ForAny(x,a->IsSubset(edges(a),cycle)) then Error("Primitive control"); fi;
        Print("rank",rank,": length",Length(images[1]),", identity abelianization, ",
            counts," noncancelling boundaries; blocking cycle protected\n");
        if rank<=3 then
            fp:=f/[];
            for cls in [1..4] do
                ep:=NqEpimorphismNilpotentQuotient(fp,cls); n:=Image(ep);
                ng:=List(GeneratorsOfGroup(fp),a->Image(ep,a));
                ni:=List(images,a->MappedWord(a,x,ng));
                if Subgroup(n,ni)<>n then Error("Nilpotent image not whole"); fi;
                map:=GroupHomomorphismByImages(n,n,ng,ni);
                if map=fail or not IsBijective(map) then Error("Nilpotent map not an automorphism"); fi;
                Print("  class",cls,": Hirsch length",HirschLength(n),", induced automorphism verified\n");
            od;
        fi;
    od;
    # Separate finite nonnilpotent witness if one exists among A5 images.
    # Absence here would not refute the universal word argument.
    f:=FreeGroup(2); x:=GeneratorsOfGroup(f);
    k:=x[1]^2*x[2]^2*x[1]; w:=k*x[2]*k^-1*x[2]^-1;
    images:=List([1,2],i->x[i]^2*w*x[i]^-1*x[3-i]*x[i]^-1*x[3-i]^-1*x[i]);
    a5:=AlternatingGroup(5); els:=AsList(a5); witness:=fail;
    for a in els do
        if witness<>fail then break; fi;
        for b in els do
            if Group(a,b)=a5 then
                ug:=MappedWord(images[1],x,[a,b]); vg:=MappedWord(images[2],x,[a,b]);
                h:=Group(ug,vg);
                if not a in h then witness:=[a,b,ug,vg,Size(h)]; break; fi;
            fi;
        od;
    od;
    if witness=fail then
        Print("No A5 separator in the bounded complete pair search; not needed by proof\n");
    else
        Print("A5 separator [a,b,u,v,|image H|]=",witness,"\n");
    fi;
    Print("PASS F39 unimodular blocking construction and nilpotent controls\n");
end)();
QUIT;
