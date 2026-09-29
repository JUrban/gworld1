# Independent exact symbolic affine-matrix replay of the inverse words.
Read("research/certificates/M0-flow-inverse/fixtures-v1.g");
CheckM0FlowInverse := function()
  local row,n,f,gens,word,ring,vars,mats,inverseMats,value,i,j,eval,
    images,undo,norm,normInv,normalized,normalizedInv,first,second,
    freeIdentity,records,compositions,notFree,flowCount,control,expected,
    pair,monomial,endpoint,evalFactory,phiMats,psiMats,perms,phiPerms,
    source,imageGroup,field,finiteMats,jac,out,stream,path,counts;
  word := function(gens,w)
    local result,a;
    result:=One(gens[1]);
    for a in w do result:=result*gens[AbsInt(a)]^SignInt(a); od;
    return result;
  end;
  evalFactory := function(n,vars)
    local mats,inverseMats,i,value,one;
    one:=One(vars[1]);mats:=[];inverseMats:=[];
    for i in [1..n] do
      value:=IdentityMat(n+1)*one;
      value[1][1]:=vars[i];value[1][i+1]:=one;Add(mats,value);
      value:=IdentityMat(n+1)*one;
      value[1][1]:=vars[i]^-1;value[1][i+1]:=-vars[i]^-1;Add(inverseMats,value);
    od;
    return function(w)
      local result,a;
      result:=IdentityMat(n+1)*one;
      for a in LetterRepAssocWord(w) do
        if a>0 then result:=result*mats[a];else result:=result*inverseMats[-a];fi;
      od;
      return result;
    end;
  end;
  records:=0;compositions:=0;notFree:=0;flowCount:=0;out:=[];
  for row in M0FlowInverse do
    n:=Length(row[2]);
    if n=0 then
      if row[2]<>[] or row[3]<>[] or row[8]<>true then Error("Rank zero");fi;
      records:=records+1;Add(out,[row[1],n,0,true]);
    else
      f:=FreeGroup(n);gens:=GeneratorsOfGroup(f);
      images:=List(row[2],w->word(gens,w));undo:=List(row[3],w->word(gens,w));
      norm:=List(row[4],w->word(gens,w));normInv:=List(row[5],w->word(gens,w));
      normalized:=List(row[6],w->word(gens,w));normalizedInv:=List(row[7],w->word(gens,w));
      if List(norm,w->MappedWord(w,gens,normInv))<>gens or
         List(normInv,w->MappedWord(w,gens,norm))<>gens then Error("Normalization inverse");fi;
      if List(images,w->MappedWord(w,gens,norm))<>normalized or
         List(norm,w->MappedWord(w,gens,normalizedInv))<>undo then
        Error("Normalization or inverse assembly convention");fi;
      ring:=PolynomialRing(Rationals,n);vars:=IndeterminatesOfPolynomialRing(ring);
      eval:=evalFactory(n,vars);
      # Evaluate actual composed free words, not supplied determinants.
      first:=List(undo,w->MappedWord(w,gens,images));
      second:=List(images,w->MappedWord(w,gens,undo));
      for i in [1..n] do
        if eval(first[i])<>eval(gens[i]) or eval(second[i])<>eval(gens[i]) then
          Error("Nonidentity Magnus composition: ",row[1]);fi;
        compositions:=compositions+2;
      od;
      freeIdentity:=(first=gens and second=gens);
      if freeIdentity<>row[8] then Error("Free vs metabelian distinction");fi;
      if not freeIdentity then notFree:=notFree+1;fi;
      records:=records+1;Add(out,[row[1],n,2*n,freeIdentity]);
      Print(row[1]," exact two-sided compositions checked\n");
    fi;
  od;
  for control in M0FlowControls do
    n:=control[1];f:=FreeGroup(n);gens:=GeneratorsOfGroup(f);
    ring:=PolynomialRing(Rationals,n);vars:=IndeterminatesOfPolynomialRing(ring);
    eval:=evalFactory(n,vars);value:=eval(word(gens,control[4]));
    endpoint:=One(ring);
    for i in [1..n] do endpoint:=endpoint*vars[i]^control[2][i];od;
    if value[1][1]<>endpoint then Error("Flow endpoint");fi;
    for i in [1..n] do
      expected:=Zero(ring);
      for pair in control[3][i] do
        monomial:=pair[2]*One(ring);
        for j in [1..n] do monomial:=monomial*vars[j]^pair[1][j];od;
        expected:=expected+monomial;
      od;
      if not IsZero(value[1][i+1]-expected) then Error("Integral signed flow");fi;
    od;
    flowCount:=flowCount+1;
  od;
  # A nonunit negative control: singular at a nonzero finite character.
  field:=GF(3);f:=FreeGroup(3);gens:=GeneratorsOfGroup(f);
  eval:=evalFactory(3,[One(field),One(field),2*One(field)]);
  jac:=List(M0FlowNonunit,w->eval(word(gens,w))[1]{[2..4]});
  if not IsZero(DeterminantMat(jac)) then Error("Nonunit control");fi;
  ring:=PolynomialRing(Rationals,2);vars:=IndeterminatesOfPolynomialRing(ring);
  if IsZero((vars[1]-1)+(vars[2]-1)-(vars[1]-1)) then Error("Boundary control");fi;
  # The displayed free-group endomorphism is not onto: S4 onto S3.
  perms:=List(M0FlowSeparator[2],PermList);source:=Group(perms);
  phiPerms:=List(M0FlowSeparator[1],w->MappedWord(word(gens,w),gens,perms));
  imageGroup:=Group(phiPerms);
  if Size(source)<>M0FlowSeparator[3] or Size(imageGroup)<>M0FlowSeparator[4]
     or not ForAll(phiPerms,p->M0FlowSeparator[5]^p=M0FlowSeparator[5])
     or ForAll(perms,p->M0FlowSeparator[5]^p=M0FlowSeparator[5]) then
    Error("Finite separator for the free lift");fi;
  counts:=[records,compositions,notFree,flowCount,Size(source),Size(imageGroup)];
  path:="research/certificates/M0-flow-inverse/gap-checks-v1.json";
  if IsExistingFile(path) then Error("Refusing overwrite");fi;
  stream:=OutputTextFile(path,false);SetPrintFormattingStatus(stream,false);
  PrintTo(stream,String([counts,out]),"\n");CloseStream(stream);
  Print("counts=",counts,"\nPASS M0 independent integral-flow inverse replay\n");
end;
CheckM0FlowInverse();
QUIT;
