Read("research/certificates/M0/checks.g");

CheckM0Records := function(records)
    local recd, field, root, decode, poly, n, free, gens, word, basis, undo,
          chi, mats, evaluate, jac, images, deriv, i, j, value, count;
    count := 0;
    for recd in records do
        field := GF(recd.p^(Length(recd.modulus)-1));
        poly := function(a)
            local z, c;
            z := Zero(field);
            for c in Reversed(recd.modulus) do z := z*a+c*One(field); od;
            return z;
        end;
        root := First(Elements(field), a -> IsZero(poly(a)));
        if root=fail then Error("No modulus root"); fi;
        decode := function(a)
            local z, t;
            z := Zero(field); t := One(field);
            while a>0 do
                z := z+(a mod recd.p)*t;
                a := QuoInt(a,recd.p); t := t*root;
            od;
            return z;
        end;
        n := Length(recd.chi);
        free := FreeGroup(n); gens := GeneratorsOfGroup(free);
        word := w -> Product(w, a -> gens[AbsInt(a)]^SignInt(a));
        basis := List(recd.basis, word); undo := List(recd.inverse, word);
        for i in [1..n] do
            if MappedWord(basis[i],gens,undo)<>gens[i] or
               MappedWord(undo[i],gens,basis)<>gens[i] then
                Error("Free basis certificate failed");
            fi;
        od;
        chi := List(recd.chi, decode);
        # Independent evaluation in affine matrices, rather than a Fox scan.
        mats := [];
        for i in [1..n] do
            value := IdentityMat(n+1,field);
            value[1][1] := chi[i]; value[1][i+1] := One(field);
            Add(mats,value);
        od;
        evaluate := w -> MappedWord(w,gens,mats);
        value := evaluate(basis[1]);
        deriv := value[1]{[2..n+1]};
        if deriv<>List(recd.expected,decode) then Error("Fox mismatch"); fi;
        if ForAll(deriv,IsZero) then Error("Primitive derivative vanished"); fi;
        if recd.kind="automorphism_control" then
            jac := List(basis,w -> evaluate(w)[1]{[2..n+1]});
            if RankMat(jac)<>n then Error("Automorphism Jacobian singular"); fi;
        fi;
        if Length(recd.images)>0 then
            images := List(recd.images,word);
            for i in [1..n] do
                for j in [1..n] do
                    if (i=j and ExponentSumWord(images[i],gens[j])<>1) or
                       (i<>j and ExponentSumWord(images[i],gens[j])<>0) then
                        Error("Example is not IA");
                    fi;
                od;
            od;
            jac := List(images,w -> evaluate(w)[1]{[2..n+1]});
            if RankMat(jac)>=n then Error("Expected singular matrix"); fi;
            value := evaluate(MappedWord(basis[1],gens,images));
            if not ForAll(value[1]{[2..n+1]},IsZero) then
                Error("Image Fox derivative did not vanish");
            fi;
        fi;
        count := count+1;
    od;
    Print("PASS M0 GAP affine-matrix and free-basis checks: ",count," records\n");
end;

CheckM0Records(M0Records);
QUIT_GAP(0);
