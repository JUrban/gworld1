# Independent native free-associative-algebra replay; no Python matrices.
(function()
 local alg,letters,Bracket,Words,Lyndon,Expand,Basis,weights,a,e,es,i,D,
       V3,V5,Q,B,us,vs,columns,space,extended,cc;
 alg:=FreeAssociativeAlgebraWithOne(Rationals,2,"t");
 letters:=GeneratorsOfAlgebraWithOne(alg);weights:=[1,4];
 Bracket:=function(x,y)return x*y-y*x;end;
 Words:=function(n)
  local out,i,w;
  if n=0 then return [[]];fi;
  out:=[];
  for i in [1..2] do if weights[i]<=n then
   for w in Words(n-weights[i]) do Add(out,Concatenation([i],w));od;
  fi;od;return out;
 end;
 Lyndon:=function(w)
  local i;
  for i in [2..Length(w)] do
   if not w<w{[i..Length(w)]} then return false;fi;
  od;return true;
 end;
 Expand:=function(w)
  local i;
  if Length(w)=1 then return letters[w[1]];fi;
  for i in [2..Length(w)] do if Lyndon(w{[i..Length(w)]}) then
   return Bracket(Expand(w{[1..i-1]}),Expand(w{[i..Length(w)]}));
  fi;od;Error("Lyndon factorization failed");
 end;
 Basis:=n->List(Filtered(Words(n),Lyndon),Expand);
 a:=letters[1];e:=letters[2];es:=[e];
 for i in [1..4] do Add(es,Bracket(a,es[Length(es)]));od;
 D:=es[5];V3:=-Bracket(e,es[4])+Bracket(es[2],es[3]);
 V5:=-Bracket(es[3],es[4]);
 if Bracket(e,D)+Bracket(a,V3)<>Zero(alg) or
    Bracket(es[3],D)+Bracket(a,V5)<>Zero(alg) then Error("Kernel identity");fi;
 Q:=Bracket(e,V3);B:=Bracket(es[3],Bracket(e,es[2]));
 us:=Basis(7);vs:=Basis(14);
 columns:=Concatenation(List(us,x->Bracket(x,D)),List(vs,x->Bracket(a,x)));
 space:=VectorSpace(Rationals,columns);
 if Dimension(space)<>Length(columns) or Q in space or B in space then
  Error("Injectivity or nonzero obstruction failed");fi;
 extended:=VectorSpace(Rationals,Concatenation(columns,[B]));
 if not Q in extended then Error("Obstructions independent");fi;
 cc:=Coefficients(BasisNC(extended,Concatenation(columns,[B])),Q);
 Print("offset6 dimensions ",Length(us),"+",Length(vs)," -> ",Length(Basis(15)),
       "; rank ",Dimension(space),"; Q modulo A = ",cc[Length(cc)]," B\n");
 Print("PASS N8 parameter transmission GAP: full offset6 injection; two nonzero dependent obstructions; two kernel identities\n");
end)();
QUIT_GAP(0);
