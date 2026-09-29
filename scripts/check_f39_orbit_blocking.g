# Controls for the stronger bounded-orbit variant, distinct from primitive-only fixtures.
(function()
    local spec,r,l,f,x,k,block,w,images,i,t,rep,signed,a,b,n,
          contains,letters,marker;
    contains:=function(a,b)
        local i;
        if Length(a)<Length(b) then return false; fi;
        return ForAny([1..Length(a)-Length(b)+1],i->a{[i..i+Length(b)-1]}=b);
    end;
    for spec in [[2,2],[3,3],[4,1]] do
        r:=spec[1]; l:=spec[2]; f:=FreeGroup(r); x:=GeneratorsOfGroup(f);
        k:=Product(x,a->a^2)*x[1]; block:=k^(l+1);
        w:=block*x[2]*block^-1*x[2]^-1;
        images:=[];
        for i in [1..r] do
            t:=x[(i mod r)+1];
            Add(images,x[i]^2*w*x[i]^-1*t*x[i]^-1*t^-1*x[i]);
        od;
        signed:=Concatenation(images,List(images,a->a^-1));
        for i in [1..r] do
            rep:=LetterRepAssocWord(images[i]);
            if Length(rep)<>2*(2*r+1)*(l+1)+9 or rep[1]<>i or
               rep[Length(rep)]<>i then Error("Length/end formula"); fi;
            if List(x,a->ExponentSumWord(images[i],a))<>IdentityMat(r)[i] then
                Error("Unimodular formula");
            fi;
        od;
        for a in signed do
            letters:=LetterRepAssocWord(a);
            if not contains(letters,LetterRepAssocWord(block)) and
               not contains(letters,LetterRepAssocWord(block^-1)) then Error("Missing orbit block"); fi;
            for b in signed do
                if b<>a^-1 and Length(a*b)<>Length(a)+Length(b) then Error("Boundary"); fi;
            od;
        od;
        # Dropping below the L+1 repeat threshold is not certified here.
        if contains(LetterRepAssocWord(k^l),LetterRepAssocWord(block)) then Error("Threshold control"); fi;
        Print("rank",r,", L",l,": protected block length",Length(block),
            ", generator length",Length(images[1]),"; both inverse directions checked\n");
    od;
    Print("PASS F39 bounded-orbit construction controls\n");
end)();
QUIT;
