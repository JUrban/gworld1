Read("research/certificates/M0-constructor/checks.g");

CheckM0Constructor := function(records)
    local recd, n, free, gens, word, makeMats, evaluate, images, basis, undo,
          f, poly, root, decode, chi, mats, value, deriv, i, j, count, autos,
          symbolic, ring, variables, norm, normInv, normalized, jac, delta,
          expectedDelta, monomial, pair;
    count := 0; autos := 0; symbolic := 0;
    for recd in records do
        n := Length(recd.images); free := FreeGroup(n); gens := GeneratorsOfGroup(free);
        word := function(w)
            local result, a;
            result := One(free);
            for a in w do result := result*gens[AbsInt(a)]^SignInt(a); od;
            return result;
        end;
        images := List(recd.images, word);
        if Length(recd.normalization)>0 then
            norm := List(recd.normalization, word);
            normInv := List(recd.normalization_inverse, word);
            for i in [1..n] do
                if MappedWord(norm[i],gens,normInv)<>gens[i] or
                   MappedWord(normInv[i],gens,norm)<>gens[i] then
                    Error("Normalization inverse certificate failed");
                fi;
            od;
            normalized := List(images, w -> MappedWord(w,gens,norm));
            for i in [1..n] do
                for j in [1..n] do
                    if (i=j and ExponentSumWord(normalized[i],gens[j])<>1) or
                       (i<>j and ExponentSumWord(normalized[i],gens[j])<>0) then
                        Error("Normalization is not IA");
                    fi;
                od;
            od;
        fi;
        if recd.status="nonautomorphism_certificate" then
            f := GF(recd.p^(Length(recd.modulus)-1));
            poly := function(a)
                local z, c;
                z := Zero(f);
                for c in Reversed(recd.modulus) do z := z*a+c*One(f); od;
                return z;
            end;
            root := First(Elements(f), a -> IsZero(poly(a)));
            if root=fail then Error("No modulus root"); fi;
            decode := function(a)
                local z, t;
                z := Zero(f); t := One(f);
                while a>0 do
                    z := z+(a mod recd.p)*t;
                    a := QuoInt(a,recd.p); t := t*root;
                od;
                return z;
            end;
            chi := List(recd.chi, decode);
            mats := [];
            for i in [1..n] do
                value := IdentityMat(n+1,f);
                value[1][1] := chi[i]; value[1][i+1] := One(f);
                Add(mats,value);
            od;
            evaluate := w -> MappedWord(w,gens,mats);
            basis := List(recd.basis,word); undo := List(recd.inverse,word);
            for i in [1..n] do
                if MappedWord(basis[i],gens,undo)<>gens[i] or
                   MappedWord(undo[i],gens,basis)<>gens[i] then
                    Error("Witness free basis certificate failed");
                fi;
            od;
            value := evaluate(basis[1]); deriv := value[1]{[2..n+1]};
            if deriv<>List(recd.expected,decode) or ForAll(deriv,IsZero) then
                Error("Primitive Fox column failed");
            fi;
            value := MappedWord(basis[1],gens,images);
            if value<>word(recd.image_word) then Error("Image word mismatch"); fi;
            value := evaluate(value);
            if not ForAll(value[1]{[2..n+1]},IsZero) then
                Error("Image Fox column did not vanish");
            fi;
            count := count+1;
        elif recd.status="metabelian_automorphism" then
            # Independently verify the exact normalized determinant as a
            # multivariate rational function, with no finite-field sampling.
            ring := PolynomialRing(Rationals,n);
            variables := IndeterminatesOfPolynomialRing(ring);
            mats := [];
            for i in [1..n] do
                value := IdentityMat(n+1,Rationals);
                value[1][1] := variables[i]; value[1][i+1] := 1;
                Add(mats,value);
            od;
            jac := List(normalized,w -> MappedWord(w,gens,mats)[1]{[2..n+1]});
            delta := DeterminantMat(jac);
            expectedDelta := Zero(ring);
            for pair in recd.determinant do
                monomial := pair[2]*One(ring);
                for i in [1..n] do monomial := monomial*variables[i]^pair[1][i]; od;
                expectedDelta := expectedDelta+monomial;
            od;
            if delta<>expectedDelta or Length(recd.determinant)<>1 or
               AbsInt(recd.determinant[1][2])<>1 then
                Error("Unit determinant certificate failed");
            fi;
            autos := autos+1; symbolic := symbolic+1;
        elif recd.status<>"inconclusive_bound" then
            Error("Unexpected status");
        fi;
    od;
    Print("PASS M0 constructor GAP certificates: ",count," witnesses, ",
          autos," unit determinants, ",Length(records)-count-autos," inconclusive controls\n");
end;

CheckM0Constructor(M0ConstructorRecords);
QUIT_GAP(0);
