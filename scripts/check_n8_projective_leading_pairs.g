# Independent group/subgroup reconstruction; does not read Python Hall matrices.
if LoadPackage("nq") <> true then Error("nq required"); fi;
Read("research/certificates/N8-projective-leading-pairs/fixtures-v1.g");
F := FreeGroup(2);;
N := NilpotentQuotient(F, 5);;
gens := GeneratorsOfGroup(N);;
EvalWord := function(word)
  local value, letter;
  value := One(N);
  for letter in word do
    if letter > 0 then value := value * gens[letter];
    else value := value * gens[-letter]^-1; fi;
  od;
  return value;
end;;
positives := 0;; negatives := 0;;
for row in N8ProjectiveLeadingBranches do
  if row{[1..2]} <> [2,5] then Error("unexpected scope"); fi;
  target := EvalWord(row[3]);;
  base := Comm(EvalWord(row[4]), EvalWord(row[5]));;
  residual := base^-1 * target;;
  corrections := List(row[6], EvalWord);;
  if not ForAll(corrections, c -> ForAll(gens, a -> Comm(c,a) = One(N)))
     then Error("noncentral correction"); fi;
  if not ForAll(gens, a -> Comm(residual,a) = One(N))
     then Error("noncentral residual"); fi;
  soluble := residual in Subgroup(N, corrections);;
  if soluble <> (row[7] = 1) then Error("integer lift decision differs"); fi;
  if soluble then positives := positives + 1; else negatives := negatives + 1; fi;
od;
for row in N8ProjectiveLeadingFixtures do
  if Comm(EvalWord(row[4]),EvalWord(row[5])) <> EvalWord(row[3])
     then Error("witness mismatch"); fi;
od;
Print("PASS N8 GAP projective complete leading pairs: ", positives,
      " positive and ", negatives, " negative central lifts; ",
      Length(N8ProjectiveLeadingFixtures), " group witnesses\n");
QUIT;
