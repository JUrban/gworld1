# Independent word substitution into a larger weighted nilpotent group.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
N8SHalls:=function(gens,description)
 local hall,i,pair;
 hall:=[];
 for i in [1..Length(description)] do
  pair:=description[i][2];
  if Length(pair)=0 then Add(hall,gens[i]);
  else Add(hall,Comm(hall[pair[1]+1],hall[pair[2]+1]));fi;
 od;
 return hall;
end;
N8SElement:=function(hall,terms)
 local ans,item;
 ans:=One(hall[1]);
 for item in terms do ans:=ans*hall[item[1]+1]^item[2];od;
 return ans;
end;
Read("research/certificates/N8-universal-gauges/specialization-target.g");
Read("research/certificates/N8-universal-gauges/13c12scaled/fixtures.g");
N8SRun:=function(target,universal)
 local free,fhall,relators,group,gens,A,B,T,S,cases,parameters,pair,
       hall,row,plus,minus,back,forward,total,inverses,changed;
 free:=FreeGroup(2);fhall:=N8SHalls(GeneratorsOfGroup(free),target[4]);
 relators:=List(target[6],i->fhall[i+1]);
 group:=NilpotentQuotient(free/relators,QuoInt(target[3],target[1]));
 if HirschLength(group)<>target[5] or Size(TorsionSubgroup(group))<>1 then
  Error("Target rank/torsion mismatch");fi;
 gens:=GeneratorsOfGroup(group){[1..2]};A:=gens[1];B:=gens[2];
 T:=Comm(B,A);S:=Comm(T,A);
 cases:=[[1,1,0,0],[2,3,0,0],[-1,1,0,0],[1,-1,0,0],
         [1,1,1,1],[2,3,-2,3],[-1,3,2,-1],[2,-1,-1,2]];
 total:=0;inverses:=0;changed:=0;
 for parameters in cases do
  pair:=[A^parameters[1]*T^parameters[3],T^parameters[2]*S^parameters[4]];
  if Comm(pair[1],pair[2])=One(group) then Error("Degenerate target pair");fi;
  hall:=N8SHalls(pair,universal[4]);
  if not ForAll(universal[6],i->hall[i+1]=One(group)) then
   Error("Universal boundary does not vanish");fi;
  for row in universal[7] do
   plus:=List(row[3],terms->N8SElement(hall,terms));
   minus:=List(row[4],terms->N8SElement(hall,terms));
   if Comm(plus[1],plus[2])<>Comm(pair[1],pair[2]) or
      Comm(minus[1],minus[2])<>Comm(pair[1],pair[2]) then
    Error("Specialization changed commutator");fi;
   back:=List(row[4],terms->N8SElement(N8SHalls(plus,universal[4]),terms));
   forward:=List(row[3],terms->N8SElement(N8SHalls(minus,universal[4]),terms));
   if back<>pair or forward<>pair then Error("Specialized inverse failed");fi;
   if plus<>pair then changed:=changed+1;fi;
   total:=total+1;inverses:=inverses+4;
  od;
 od;
 if changed<>total then Error("A substitution unexpectedly acted trivially");fi;
 Print("PASS N8 universal specialization: rank ",target[5],"; ",Length(cases),
       " pairs; ",total," substitutions; ",inverses," inverse equalities; ",
       changed," nontrivial substitutions\n");
end;
N8SRun(N8UniversalTarget,N8UniversalFixture);
QUIT;
