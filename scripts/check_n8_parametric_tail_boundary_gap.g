Read("research/certificates/N8-parametric-tail/boundary19/fixtures.g");;
(function()
 local data,A,gens,hall,h,u,v,expected,actual,item;
 data:=N8TailBoundary;A:=FreeAssociativeAlgebraWithOne(Rationals,2,"a");
 gens:=GeneratorsOfAlgebraWithOne(A);hall:=[];
 for h in data[1] do
  if IsEmpty(h[2]) then Add(hall,gens[Length(hall)+1]);
  else u:=hall[h[2][1]+1];v:=hall[h[2][2]+1];Add(hall,u*v-v*u);fi;
 od;
 u:=hall[data[2]+1];v:=hall[data[3]+1];expected:=u*v-v*u;
 actual:=Zero(A);
 for item in data[4] do actual:=actual+item[2]*Product(List(item[1],j->gens[j+1]));od;
 if expected<>actual or IsZero(actual) then Error("Mixed boundary bracket mismatch");fi;
 if data[1][data[2]+1][1]<>6 or data[1][data[3]+1][1]<>13 then Error("Boundary weights");fi;
 Print("PASS N8 parametric boundary GAP: nonzero weight19 mixed bracket; ",Length(data[4])," coefficients\n");
end)();
QUIT_GAP(0);
