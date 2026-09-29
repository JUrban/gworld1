# Independently check every pair in the seven finite ambient groups.
Read("research/certificates/F20-finite-images/fixtures-v1.g");

F20FiniteImagesCheck := function()
  local f, freegens, words, weights, parents, w, oldlen, i, j, rels,
        targets, eaWord, ebWord, row, name, degree, expected, gens, reps,
        elements, g, classes, allclasses, classsizes, counts, accepted,
        ai, bi, a, b, base, ea, eb, vals, nontrivial, control, output,
        outpath, outstream, start, n;
  f := FreeGroup("a", "b"); freegens := GeneratorsOfGroup(f);
  words := ShallowCopy(freegens); weights := [1,1]; parents := [[0,0],[0,0]];
  for w in [2..7] do
    oldlen := Length(words);
    for i in [1..oldlen] do
      for j in [1..i-1] do
        if weights[i]+weights[j]=w and (parents[i][2]=0 or parents[i][2]<=j) then
          Add(words,Comm(words[i],words[j])); Add(weights,w); Add(parents,[i,j]);
        fi;
      od;
    od;
  od;
  if List([1..7],w->Number(weights,x->x=w))<>[2,1,2,3,6,9,18] then
    Error("Hall cardinalities");
  fi;
  rels := Filtered([1..Length(words)],i->weights[i]=6);
  targets := Filtered([1..Length(words)],i->weights[i]=7);
  eaWord := Comm(freegens[2],freegens[1]); ebWord := eaWord;
  for i in [1..4] do
    eaWord := Comm(eaWord,freegens[1]); ebWord := Comm(ebWord,freegens[2]);
  od;
  if not Position(words,eaWord) in rels or not Position(words,ebWord) in rels then
    Error("The two pruning words must be imposed relators");
  fi;
  output := [];
  for row in F20FiniteImages do
    start := Runtime(); name := row[1]; degree := row[2]; expected := row[3];
    gens := List(row[4],PermList); reps := List(row[5],PermList);
    elements := List(row[7],PermList); g := Group(gens);
    if Size(g)<>expected or Set(elements)<>Set(Elements(g)) then
      Error("Incomplete or incorrect finite group enumeration: ",name);
    fi;
    classes := List(reps,a->ConjugacyClass(g,a));
    classsizes := List(classes,Size);
    allclasses := Union(List(classes,c->Set(Elements(c))));
    if classsizes<>row[6] or Sum(classsizes)<>expected or allclasses<>Set(elements) then
      Error("Conjugacy transversal is not complete/disjoint: ",name);
    fi;
    counts := [0,0,0,0,0]; accepted := [];
    for ai in [1..Length(reps)] do
      a := reps[ai];
      for bi in [1..Length(elements)] do
        b := elements[bi]; counts[1] := counts[1]+1;
        base := Comm(b,a);
        if base=One(g) then
          counts[2] := counts[2]+1;
        else
          ea := base; eb := base;
          for i in [1..4] do ea := Comm(ea,a); eb := Comm(eb,b); od;
          if ea=One(g) and eb=One(g) then
            counts[3] := counts[3]+1;
            # Evaluate the actual independently constructed free words.
            vals := List(words,w->MappedWord(w,freegens,[a,b]));
            if vals[Position(words,eaWord)]<>ea or vals[Position(words,ebWord)]<>eb then
              Error("Pruning convention mismatch");
            fi;
            if ForAll(rels,i->vals[i]=One(g)) then
              counts[4] := counts[4]+1;
              nontrivial := Filtered(targets,i->vals[i]<>One(g));
              Add(accepted,[ai,bi,nontrivial]);
              if not IsEmpty(nontrivial) then counts[5] := counts[5]+1; fi;
            fi;
          fi;
        fi;
      od;
    od;
    if counts<>row[8] or accepted<>row[9] then
      Error("Pair-by-pair replay mismatch: ",name);
    fi;
    control := Filtered(targets,i->MappedWord(words[i],freegens,gens)<>One(g));
    if IsEmpty(control) or control<>row[10] then Error("Omitted-relator control"); fi;
    Add(output,[name,degree,expected,Length(reps),counts,Length(accepted),Runtime()-start]);
    Print(name," verified classes=",Length(reps)," counts=",counts,
          " ms=",Runtime()-start,"\n");
  od;
  outpath := "research/certificates/F20-finite-images/gap-checks-v2.json";
  if IsExistingFile(outpath) then Error("Refusing overwrite"); fi;
  outstream := OutputTextFile(outpath,false);
  SetPrintFormattingStatus(outstream,false);
  PrintTo(outstream,String(output),"\n");
  CloseStream(outstream);
  Print("PASS F20 independent finite-image pair replay\n");
end;
F20FiniteImagesCheck();
QUIT;
