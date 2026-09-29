# Exact native group replay with compact relators and direct substitutions.
# The older verifier unnecessarily expands all free Hall words and builds
# homomorphism objects; this checks the same relations/compositions directly.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
Read("research/certificates/N8-three-exception-gauges-c26-v2/fixtures.g");;
(function()
 local item,Require,desc,kept,bound,needed,strings,i,h,input,G,gens,
       Halls,Element,hall,comm,row,plus,minus,hplus,hminus,back,forward,
       total,inverses,relations;
 item:=N8UniversalFixture;desc:=item[4];kept:=item[5];bound:=List(item[6],i->i+1);
 Require:=function(ok,msg)if not ok then Error(msg);fi;end;
 Require(item{[1..3]}=[1,10,26],"Wrong weighted target");
 needed:=Union([1..kept],bound);strings:=[];
 Require(ForAll(bound,i->ForAll(desc[i][2],j->j<kept)),"Omitted boundary parent");
 for i in [1..Length(desc)] do
  h:=desc[i];
  if not i in needed then Add(strings,"");
  elif IsEmpty(h[2]) then Add(strings,["a","b"][i]);
  else Add(strings,Concatenation("[",strings[h[2][1]+1],",",strings[h[2][2]+1],"]"));fi;
 od;
 input:=Concatenation("< b,a | ",JoinStringsWithSeparator(List(bound,i->strings[i]),", ")," >\n");
 Print("Prepared compact universal quotient\n");
 G:=NilpotentQuotient(:input_string:=input,class:=26);gens:=GeneratorsOfGroup(G){[2,1]};
 Require(HirschLength(G)=kept and ForAll(RelativeOrdersOfPcp(Pcp(G)),x->x=0),"Rank/torsion");
 Print("Universal quotient ready, Hirsch length ",kept,"\n");
 Halls:=function(pair)
  local hall,i,h;hall:=[];
  for i in [1..Length(desc)] do
   h:=desc[i];
   if not i in needed then Add(hall,One(G));
   elif IsEmpty(h[2]) then Add(hall,pair[i]);
   else Add(hall,Comm(hall[h[2][1]+1],hall[h[2][2]+1]));fi;
  od;return hall;
 end;
 Element:=function(hall,terms)
  local ans,h;ans:=One(G);
  for h in terms do Require(IsInt(h[2]),"Noninteger exponent");ans:=ans*hall[h[1]+1]^h[2];od;
  return ans;
 end;
 hall:=Halls(gens);Require(ForAll(bound,i->hall[i]=One(G)),"Boundary relations");
 comm:=Comm(gens[1],gens[2]);Require(comm<>One(G),"Commutator collapsed");
 total:=0;inverses:=0;relations:=0;
 Require(List(item[7],r->r[1])=[9,11,13,15],"Missing expected kernel map");
 for row in item[7] do
  plus:=List(row[3],terms->Element(hall,terms));minus:=List(row[4],terms->Element(hall,terms));
  hplus:=Halls(plus);hminus:=Halls(minus);
  Require(ForAll(bound,i->hplus[i]=One(G) and hminus[i]=One(G)),"Map does not preserve presentation");
  back:=List(row[4],terms->Element(hplus,terms));forward:=List(row[3],terms->Element(hminus,terms));
  Require(back=gens and forward=gens,"Inverse composition");
  Require(Comm(plus[1],plus[2])=comm and Comm(minus[1],minus[2])=comm,"Commutator preservation");
  total:=total+1;inverses:=inverses+4;relations:=relations+2*Length(bound);
  Print("Verified universal offset ",row[1],", exact integer power ",row[2],"\n");
 od;
 Require(Comm(gens[1]*gens[2],gens[2])<>comm,"Wrong Nielsen control accepted");
 Print("PASS N8 delayed gauges GAP: ",total," maps; ",inverses," inverse equalities; ",relations," image boundary relations; 1 wrong-Nielsen control\n");
end)();
QUIT_GAP(0);
