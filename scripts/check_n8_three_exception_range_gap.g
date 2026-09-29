# Generic independent checker adapted from check_n8_exceptional_boundary_gap.g at 30e9e7b.
# Independent GAP associative-algebra kernel computation.
Read("research/certificates/N8-three-exception-range/fixtures.g");;
(function()
 local one,weights,algebra,gens,Bracket,Expr,Words,Lyndon,Expand,Basis,
       SpanDim,Weight,C,D,p,q,row,us,vs,cols,nul,direction,count,dirs;
 count:=0;dirs:=0;
 for one in N8BoundaryFixtures do
  weights:=one[2];algebra:=FreeAssociativeAlgebraWithOne(Rationals,Length(weights),"j");
  gens:=GeneratorsOfAlgebraWithOne(algebra);
  Bracket:=function(a,b)return a*b-b*a;end;
  Expr:=function(e)
   if IsInt(e) then return gens[e];fi;
   if e[1]="+" then return Expr(e[2])+Expr(e[3]);fi;
   if e[1]="-" then return Expr(e[2])-Expr(e[3]);fi;
   return Bracket(Expr(e[1]),Expr(e[2]));
  end;
  Weight:=function(e)
   if IsInt(e) then return weights[e];fi;
   if e[1]="+" or e[1]="-" then
    if Weight(e[2])<>Weight(e[3]) then Error("Inhomogeneous expression");fi;
    return Weight(e[2]);fi;
   return Weight(e[1])+Weight(e[2]);
  end;
  Words:=function(n)
   local out,i,w;
   if n=0 then return [[]];fi;
   out:=[];
   for i in [1..Length(weights)] do
    if weights[i]<=n then for w in Words(n-weights[i]) do Add(out,Concatenation([i],w));od;fi;
   od;return out;
  end;
  Lyndon:=function(w)
   local i;
   for i in [2..Length(w)] do if not w<w{[i..Length(w)]} then return false;fi;od;
   return true;
  end;
  Expand:=function(w)
   local i;
   if Length(w)=1 then return gens[w[1]];fi;
   for i in [2..Length(w)] do if Lyndon(w{[i..Length(w)]}) then
    return Bracket(Expand(w{[1..i-1]}),Expand(w{[i..Length(w)]}));fi;od;
   Error("Lyndon split");
  end;
  Basis:=n->List(Filtered(Words(n),Lyndon),Expand);
  SpanDim:=function(columns)
   local nz;
   nz:=Filtered(columns,c->c<>Zero(algebra));
   if IsEmpty(nz) then return 0;fi;
   return Dimension(VectorSpace(Rationals,nz));
  end;
  C:=Expr(one[3]);D:=Expr(one[4]);p:=Weight(one[3]);q:=Weight(one[4]);
  if List(one[5],r->r[1])<>[1..q-p-1] then Error("Incomplete offset range");fi;
  for row in one[5] do
   us:=Basis(p+row[1]);vs:=Basis(q+row[1]);
   cols:=Concatenation(List(us,x->Bracket(x,D)),List(vs,x->Bracket(C,x)));
   nul:=Length(cols)-SpanDim(cols);
   if [Length(us),Length(vs),nul]<>row{[2..4]} then Error("Kernel mismatch");fi;
   if nul>0 and row[1]>q-3*p then Error("Minimal-weight bound failed");fi;
   count:=count+1;
  od;
  for direction in one[6] do
   if Weight(direction[2])<>p+direction[1] or Weight(direction[3])<>q+direction[1]
      or Bracket(C,Expr(direction[3]))<>Bracket(Expr(direction[2]),D) then
    Error("Direction mismatch");fi;
   dirs:=dirs+1;
  od;
  Print(one[1]," complete range verified\n");
 od;
 Print("PASS N8 three-exception range GAP: ",count," kernels; ",dirs," directions\n");
end)();
QUIT_GAP(0);
