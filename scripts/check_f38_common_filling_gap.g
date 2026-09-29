Read("research/certificates/F38-common-filling/fixtures.g");;
(function()
 local Require,Eval,Graph,one,F,gens,basis,H,number,positive,quotients,
       edges,adj,vertices,n,rank,s,a,t,i,u,w,start,finish,seen,pending,v;
 Require:=function(ok,s) if not ok then Print("FAIL carrier ",s,"\n");FORCE_QUIT_GAP(1);fi;end;
 Eval:=function(gens,word)
  local x,result;result:=One(gens[1]);
  for x in word do result:=result*gens[AbsInt(x)]^SignInt(x);od;return result;
 end;
 Graph:=function(edges,basis,gens)
  local n,adj,s,a,t,row,vertices,i,w,v,H,paths,queue,labels,label,other,loops;
  n:=1+Maximum(Concatenation(List(edges,e->[e[1],e[3]])));
  adj:=List([1..n],i->rec());
  for row in edges do
   s:=row[1]+1;a:=row[2];t:=row[3]+1;
   Require(a>0 and not IsBound(adj[s].(String(a))) and not IsBound(adj[t].(String(-a))),"folded graph");
   adj[s].(String(a)):=t;adj[t].(String(-a)):=s;
  od;
  paths:=List([1..n],i->fail);paths[1]:=[];queue:=[1];
  for v in queue do
   for label in RecNames(adj[v]) do
    other:=adj[v].(label);
    if paths[other]=fail then paths[other]:=Concatenation(paths[v],[Int(label)]);Add(queue,other);fi;
   od;
  od;
  Require(Length(queue)=n,"connected graph");
  H:=Subgroup(F,basis);
  Require(RankOfFreeGroup(H)=Length(edges)-n+1 and Length(basis)=RankOfFreeGroup(H),"basis rank");
  # An independent spanning tree supplies all edge-loop generators.
  for row in edges do
   w:=Eval(gens,paths[row[1]+1])*gens[row[2]]*Eval(gens,paths[row[3]+1])^-1;
   Require(w in H,"independent edge loop in proposed basis subgroup");
  od;
  for w in basis do
   v:=1;
   for a in LetterRepAssocWord(w) do
    Require(IsBound(adj[v].(String(a))),"basis word has no graph lift");v:=adj[v].(String(a));
   od;
   Require(v=1,"basis loop closed");
  od;
 end;
 quotients:=0;positive:=0;
 for one in F38CarrierQuotients do
  F:=FreeGroup(one[1]);gens:=GeneratorsOfGroup(F);basis:=List(one[4],w->Eval(gens,w));
  Graph(one[3],basis,gens);
  Require(Eval(basis,one[5])=Eval(gens,one[2]),"quotient target coordinates");quotients:=quotients+1;
 od;
 for one in F38CarrierWitnesses do
  F:=FreeGroup(one[1]);gens:=GeneratorsOfGroup(F);basis:=List(one[5],w->Eval(gens,w));
  Graph(one[4],basis,gens);
  Require(Eval(basis,one[6])=Eval(gens,one[2]),"first carrier word");
  u:=Eval(gens,one[8]);
  Require(Eval(basis,one[7])=u*Eval(gens,one[3])*u^-1,"conjugate second carrier word");
  positive:=positive+1;
 od;
 Print("PASS F38 carrier GAP graphs: ",quotients," quotients; ",positive," positive carriers\n");
end)();;
# This verifies two-sided automorphism inverses and all finite/infinite
# conjugacy-orbit certificates; the common checker exits GAP on completion.
Read("scripts/check_f38_stabilizer_obstruction_gap.g");
