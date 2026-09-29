# Independent direct enumeration in GAP's free group; no signed-graph code.
Read("research/certificates/F41-piece-covers/fixtures.g");
F := FreeGroup("a", "b");;
letters := [F.1, F.1^-1, F.2, F.2^-1];;
levels := [[One(F)]];;
for n in [1..7] do
  next := [];;
  for w in levels[n] do
    for a in letters do
      v := w*a;;
      if Length(v) = n then Add(next, v); fi;
    od;
  od;
  if Length(next) <> 4*3^(n-1) or Length(Set(next)) <> Length(next) then
    Error("Free word enumeration failed");
  fi;
  Add(levels, next);
od;
checked := 0;;
for record in F41PieceFixtures do
  n := record[1];; count := 0;;
  for w in levels[n+1] do
    rep := LetterRepAssocWord(w);;
    ok := true;;
    for fixed in record[2] do
      if rep[fixed[1]] <> fixed[2] then ok := false; fi;
    od;
    for p in record[3] do
      first := rep{[p[1]..p[1]+p[2]-1]};;
      second := rep{[p[3]..p[3]+p[2]-1]};;
      if p[4] = -1 then second := -Reversed(second); fi;
      if first <> second then ok := false; break; fi;
    od;
    if ok then count := count+1; fi;
  od;
  if count <> record[4] then Error("Independent piece count disagrees"); fi;
  if record[5] = 0 then
    if count <> 0 then Error("Inconsistent signed scheme has a word"); fi;
  elif count > 4*3^(record[5]-1) then Error("Tree count exceeded"); fi;
  checked := checked+1;
od;
Print("PASS F41 GAP piece covers: ", checked, " exact independent word counts\n");
QUIT;
