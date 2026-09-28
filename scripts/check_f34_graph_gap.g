# Independent graph/basis/automorphism replay; not the full decision algorithm.
LoadPackage("fga");;
Read("research/certificates/F34-positivity/fixtures.g");;
(function()
    local Require,Word,Inv,record,F,gens,images,image,matrix,determinant,
          graph,nv,tree,paths,changed,eid,e,source,target,label,outgoing,
          outside,basis,expected,H,K,autoImages,autoSubgroup,result,
          vertex,letters,collapsed,i,edgeId,positiveCount,controlCount,
          identityCount,nonSurjectiveCount,mixedCount;
    Require:=function(ok,message) if not ok then Error(message); fi; end;
    Word:=function(group,word)
        local result,a;
        result:=One(group);
        for a in word do
            result:=result*GeneratorsOfGroup(group)[AbsInt(a)]^SignInt(a);
        od;
        return result;
    end;
    Inv:=word->-Reversed(word);
    positiveCount:=0;controlCount:=0;identityCount:=0;
    nonSurjectiveCount:=0;mixedCount:=0;
    for record in F34Records do
        F:=FreeGroup(record.rank);gens:=GeneratorsOfGroup(F);
        images:=List(record.images,w->Word(F,w));
        matrix:=TransposedMat(List(images,w->List(gens,a->ExponentSumWord(w,a))));
        determinant:=DeterminantMat(matrix);
        Require(determinant=record.determinant,"determinant mismatch");
        image:=MappedWord(Word(F,record.word),gens,images);
        Require(image=Word(F,record.image),"image mismatch");
        if record.status="singular_scope_control" then
            Require(determinant=0,"wrong singular scope control");
            if record.name="singular_injective_positive" then
                Require(RankOfFreeGroup(Subgroup(F,images))=record.rank,
                        "singular injective control has wrong rank");
            fi;
            controlCount:=controlCount+1;
        elif record.status="image_not_positive_scope_control" then
            Require(ForAny(LetterRepAssocWord(image),a->a<0),"image was positive");
            controlCount:=controlCount+1;
        else
            Require(record.status="positive_automorphism_witness" and determinant<>0,
                    "unsupported witness");
            Require(ForAll(LetterRepAssocWord(image),a->a>0),"image not positive");
            graph:=record.graph;nv:=graph.vertices;tree:=graph.tree;
            Require(Length(tree)=nv-1 and Length(Set(tree))=Length(tree),"bad tree size");
            outgoing:=[];
            for e in graph.edges do
                source:=e[1];label:=e[2];target:=e[3];
                Require(source in [0..nv-1] and target in [0..nv-1]
                        and label in [1..record.rank],"bad edge");
                Add(outgoing,[source,label]);Add(outgoing,[target,-label]);
            od;
            Require(Length(Set(outgoing))=Length(outgoing),"graph not folded");
            paths:=List([1..nv],i->fail);paths[1]:=[];
            changed:=true;
            while changed do
                changed:=false;
                for eid in tree do
                    e:=graph.edges[eid];source:=e[1]+1;target:=e[3]+1;label:=e[2];
                    if paths[source]<>fail and paths[target]=fail then
                        paths[target]:=Concatenation(paths[source],[label]);changed:=true;
                    elif paths[target]<>fail and paths[source]=fail then
                        paths[source]:=Concatenation(paths[target],[-label]);changed:=true;
                    fi;
                od;
            od;
            Require(ForAll(paths,p->p<>fail),"tree does not span");
            outside:=Filtered([1..Length(graph.edges)],eid->not eid in tree);
            Require(Length(outside)=record.rank,"wrong graph rank");
            basis:=[];
            for eid in outside do
                e:=graph.edges[eid];
                Add(basis,Word(F,Concatenation(paths[e[1]+1],[e[2]],Inv(paths[e[3]+1]))));
            od;
            Require(basis=List(graph.basis,w->Word(F,w)),"tree basis mismatch");
            H:=Subgroup(F,images);K:=Subgroup(F,basis);
            Require(RankOfFreeGroup(H)=record.rank,"image rank incorrect");
            Require(ForAll(images,w->w in K) and ForAll(basis,w->w in H),
                    "basis generates different subgroup");
            autoImages:=List(record.automorphism_images,w->Word(F,w));
            autoSubgroup:=Subgroup(F,autoImages);
            Require(ForAll(gens,a->a in autoSubgroup),"claimed automorphism not onto");
            Require(List(autoImages,w->MappedWord(w,gens,basis))=images,
                    "coordinate conversion mismatch");
            result:=MappedWord(Word(F,record.word),gens,autoImages);
            Require(result=Word(F,record.positive_word) and
                    ForAll(LetterRepAssocWord(result),a->a>0),"positive witness invalid");
            letters:=LetterRepAssocWord(image);vertex:=0;collapsed:=[];
            Require(Length(letters)=Length(record.positive_path),"wrong path length");
            for i in [1..Length(letters)] do
                edgeId:=record.positive_path[i];Require(edgeId>0,"backwards positive edge");
                e:=graph.edges[edgeId];
                Require(e[1]=vertex and e[2]=letters[i],"wrong positive traversal");
                vertex:=e[3];
                if not edgeId in tree then Add(collapsed,Position(outside,edgeId)); fi;
            od;
            Require(vertex=0 and collapsed=record.positive_word,"wrong tree collapse");
            positiveCount:=positiveCount+1;
            if IsEmpty(record.word) then identityCount:=identityCount+1;fi;
            if AbsInt(determinant)>1 then nonSurjectiveCount:=nonSurjectiveCount+1;fi;
            if ForAny(record.word,a->a<0) then mixedCount:=mixedCount+1;fi;
        fi;
    od;
    Require(positiveCount=270 and controlCount=3,"fixture count changed");
    Print("COUNTS=[",positiveCount,",",controlCount,",",identityCount,",",
          nonSurjectiveCount,",",mixedCount,"]\n");
    Print("PASS F34 GAP graph bases and positive automorphisms\n");
end)();
QUIT;
