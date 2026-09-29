# Independent exact replay in weighted nilpotent group presentations.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
if not IsBound(N8UniversalFiles) then Error("Set fixture paths explicitly");fi;
N8UHalls:=function(gens,description)
 local hall,i,pair;
 hall:=[];
 for i in [1..Length(description)] do
  pair:=description[i][2];
  if Length(pair)=0 then Add(hall,gens[i]);
  else Add(hall,Comm(hall[pair[1]+1],hall[pair[2]+1]));fi;
 od;
 return hall;
end;
N8UElement:=function(hall,terms)
 local ans,item;
 ans:=One(hall[1]);
 for item in terms do ans:=ans*hall[item[1]+1]^item[2];od;
 return ans;
end;
N8UTotal:=0;;N8UInverse:=0;;N8UNegative:=0;;N8UGroups:=0;;
for filename in N8UniversalFiles do
 Read(filename);item:=N8UniversalFixture;
 p:=item[1];q:=item[2];c:=item[3];description:=item[4];retained:=item[5];
 free:=FreeGroup(2);fhall:=N8UHalls(GeneratorsOfGroup(free),description);
 relators:=List(item[6],i->fhall[i+1]);
 group:=NilpotentQuotient(free/relators,QuoInt(c,p));
 gens:=GeneratorsOfGroup(group);hall:=N8UHalls(gens,description);
 if HirschLength(group)<>retained or Size(TorsionSubgroup(group))<>1 then
  Error("Weighted quotient rank/torsion mismatch");
 fi;
 if not ForAll(item[6],i->hall[i+1]=One(group)) then Error("Boundary relation failure");fi;
 comm:=Comm(gens[1],gens[2]);
 if comm=One(group) then Error("Lost commutator");fi;
 for row in item[7] do
  plus:=List(row[3],terms->N8UElement(hall,terms));
  minus:=List(row[4],terms->N8UElement(hall,terms));
  f:=GroupHomomorphismByImages(group,group,gens,plus);
  b:=GroupHomomorphismByImages(group,group,gens,minus);
  if f=fail or b=fail then Error("Images not homomorphisms");fi;
  for i in [1..2] do
   if Image(f,Image(b,gens[i]))<>gens[i] or Image(b,Image(f,gens[i]))<>gens[i] then
    Error("Inverse compositions failed");fi;
   N8UInverse:=N8UInverse+2;
  od;
  if Comm(plus[1],plus[2])<>comm or Comm(minus[1],minus[2])<>comm then
   Error("Exact commutator not fixed");fi;
  N8UTotal:=N8UTotal+1;
 od;
 # Right multiplication is not the commutator-preserving Nielsen move.
 if p+2*q<=c then
  if Comm(gens[1]*gens[2],gens[2])=comm then Error("Wrong Nielsen control passed");fi;
  N8UNegative:=N8UNegative+1;
 fi;
 N8UGroups:=N8UGroups+1;
 Print("weighted group ",p,",",q," class bound ",c," rank ",retained," maps ",Length(item[7]),"\n");
od;
Print("PASS N8 universal GAP: ",N8UGroups," weighted groups; ",N8UTotal," maps; ",
 N8UInverse," inverse checks; ",N8UNegative," wrong-Nielsen controls\n");
QUIT;
