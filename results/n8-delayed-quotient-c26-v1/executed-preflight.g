# Independent class26 quotient and Hall-polynomial preflight.
# No constructor polynomial data is loaded.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
MakeReadWriteGlobal("USE_COMBINATORIAL_COLLECTOR");;
USE_COMBINATORIAL_COLLECTOR:=true;;
MakeReadOnlyGlobal("USE_COMBINATORIAL_COLLECTOR");;
(function()
 local c,hall,d,pending,i,j,a,b,retained,boundaries,needed,strings,h,input,G;
 c:=26;hall:=[[1,[]],[4,[]]];
 for d in [1..c+4] do
  pending:=[];
  for i in [1..Length(hall)] do
   a:=hall[i];
   for j in [1..i-1] do
    b:=hall[j];
    if a[1]+b[1]=d and (IsEmpty(a[2]) or a[2][2]<=j) then
     Add(pending,[d,[i,j]]);
    fi;
   od;
  od;Append(hall,pending);
 od;
 retained:=Number(hall,h->h[1]<=c);
 boundaries:=Filtered([1..Length(hall)],i->hall[i][1]>c and
  not IsEmpty(hall[i][2]) and ForAll(hall[i][2],j->j<=retained));
 needed:=Union([1..retained],boundaries);strings:=[];
 for i in [1..Length(hall)] do
  h:=hall[i];
  if not i in needed then Add(strings,"");
  elif IsEmpty(h[2]) then Add(strings,["a","b"][i]);
  else Add(strings,Concatenation("[",strings[h[2][1]],",",strings[h[2][2]],"]"));fi;
 od;
 input:=Concatenation("< b,a | ",JoinStringsWithSeparator(List(boundaries,i->strings[i]),", ")," >\n");
 Print("Prepared class26 weighted presentation: ",retained," Hall generators, ",Length(boundaries)," boundary relators\n");
 G:=NilpotentQuotient(:input_string:=input,class:=c);
 if retained<>680 or HirschLength(G)<>retained or not ForAll(RelativeOrdersOfPcp(Pcp(G)),x->x=0) then
  Error("Weighted rank/torsion");fi;
 if not IsWeightedCollector(Collector(G)) then Error("Collector weights");fi;
 Print("Quotient ready; computing native Hall multiplication polynomials\n");
 AddHallPolynomials(Collector(G));
 Print("PASS N8 weighted quotient preflight: class26, Hirsch length680, torsion-free\n");
end)();
QUIT_GAP(0);
