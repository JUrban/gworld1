# Independent evaluation of central group lifts in GAP/nq.
if LoadPackage("nq") <> true then Error("nq required"); fi;
Read("research/certificates/N8-projective-factors/fixtures.g");
checked := 0;;
for row in N8ProjectiveFixtures do
  F := FreeGroup(row[1]);;
  N := NilpotentQuotient(F, row[2]);;
  gens := GeneratorsOfGroup(N);;
  values := [];;
  for word in row{[3..5]} do
    value := One(N);;
    for letter in word do
      if letter > 0 then value := value * gens[letter];
      else value := value * gens[-letter]^-1; fi;
    od;
    Add(values, value);
  od;
  if Comm(values[2], values[3]) <> values[1] then Error("Group witness mismatch"); fi;
  if values[1] = One(N) then Error("Unexpected identity control"); fi;
  checked := checked + 1;
od;
Print("PASS N8 GAP projective factors: ", checked, " central group witnesses\n");
QUIT;
