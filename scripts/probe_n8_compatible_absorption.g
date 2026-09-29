# Bounded first-successor-compatible Lie deformation, not a group solution.
(function()
 local A,g,Bracket,E,i,D,D1,V3,V4,V5,Q,B,Words,Lyndon,Expand,
       LieBasis,weights,U,V,cols,span,joint,dim,dimq,dimb,dimqb,coord;
 A:=FreeAssociativeAlgebraWithOne(Rationals,2,"a");g:=GeneratorsOfAlgebraWithOne(A);
 Bracket:=function(x,y)return x*y-y*x;end;
 E:=[g[2]];for i in [1..6] do Add(E,Bracket(g[1],Last(E)));od;D:=E[7];
 D1:=2*Bracket(E[1],E[4])+3*Bracket(E[2],E[3]);
 V3:=-Bracket(E[1],E[6])+Bracket(E[2],E[5])-Bracket(E[3],E[4]);
 V4:=-2*Bracket(E[1],Bracket(E[1],E[3]))+Bracket(E[2],Bracket(E[1],E[2]));
 V5:=-Bracket(E[3],E[6])+Bracket(E[4],E[5]);
 if not IsZero(Bracket(E[1],D)+Bracket(g[1],V3)) or
    not IsZero(Bracket(E[3],D)+Bracket(g[1],V5)) then Error("Kernel identities");fi;
 if not IsZero(Bracket(E[1],D1)+Bracket(g[1],V4)) then Error("Early compatibility");fi;
 Q:=Bracket(E[1],V3);B:=Bracket(E[3],D1);
 weights:=[1,4];
 Words:=function(n)
  local out,i,w;out:=[];if n=0 then return [[]];fi;
  for i in [1..2] do
   if weights[i]<=n then for w in Words(n-weights[i]) do Add(out,Concatenation([i],w));od;fi;
  od;return out;
 end;
 Lyndon:=function(w)
  local i;for i in [2..Length(w)] do if not w<w{[i..Length(w)]} then return false;fi;od;return true;
 end;
 Expand:=function(w)
  local i;if Length(w)=1 then return g[w[1]];fi;
  for i in [2..Length(w)] do if Lyndon(w{[i..Length(w)]}) then
   return Bracket(Expand(w{[1..i-1]}),Expand(w{[i..Length(w)]}));fi;od;
  Error("Lyndon split");
 end;
 LieBasis:=n->List(Filtered(Words(n),Lyndon),Expand);
 U:=LieBasis(7);V:=LieBasis(16);
 cols:=Concatenation(List(U,u->Bracket(u,D)),List(V,v->Bracket(g[1],v)));
 span:=VectorSpace(Rationals,cols);dim:=Dimension(span);
 dimq:=Dimension(VectorSpace(Rationals,Concatenation(cols,[Q])));
 dimb:=Dimension(VectorSpace(Rationals,Concatenation(cols,[B])));
 dimqb:=Dimension(VectorSpace(Rationals,Concatenation(cols,[Q,B])));
 Print("early-compatible D1; domain dimensions ",Length(U),"+",Length(V),
  "; ranks A6,Q,B,QB = ",[dim,dimq,dimb,dimqb],"\n");
 if dimq=dim+1 and dimb=dim+1 and dimqb=dim+1 then
  joint:=Concatenation(BasisVectors(Basis(span)),[B]);
  coord:=Coefficients(Basis(VectorSpace(Rationals,joint),joint),Q);
  Print("Q modulo A6 equals ",Last(coord)," times B\n");
 fi;
 Print("PASS N8 compatible absorption probe: early compatibility and complete rational ranks\n");
end)();
QUIT_GAP(0);
