# Native free-associative GAP arithmetic; independently enumerate Lie bases.
Read("research/certificates/N8-third-structure/fixtures.g");;
(function()
 local Require,one,weights,algebra,gens,Bracket,Expr,Words,Lyndon,Expand,Basis,
       SpanDim,C,D,U,V,p,q,Weight,us,vs,cols,nul,final,dim,dim2,count,obstruct;
 Require:=function(ok,s)if not ok then Print("FAIL ",s,"\n");FORCE_QUIT_GAP(1);fi;end;
 count:=0;obstruct:=0;
 for one in N8ThirdStructure do
  weights:=one[2];algebra:=FreeAssociativeAlgebraWithOne(Rationals,Length(weights),"j");
  gens:=GeneratorsOfAlgebraWithOne(algebra);
  Bracket:=function(a,b)return a*b-b*a;end;
  Expr:=function(e)
   if IsInt(e) then return gens[e];fi;
   if e[1]="+" then return Expr(e[2])+Expr(e[3]);fi;
   return Bracket(Expr(e[1]),Expr(e[2]));
  end;
  Weight:=function(e)
   if IsInt(e) then return weights[e];fi;
   if e[1]="+" then Require(Weight(e[2])=Weight(e[3]),"inhomogeneous");return Weight(e[2]);fi;
   return Weight(e[1])+Weight(e[2]);
  end;
  Words:=function(n)
   local out,i,w;
   if n=0 then return [[]];fi;
   out:=[];
   for i in [1..Length(weights)] do
    if weights[i]<=n then for w in Words(n-weights[i]) do Add(out,Concatenation([i],w));od;fi;
   od;
   return out;
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
    return Bracket(Expand(w{[1..i-1]}),Expand(w{[i..Length(w)]}));
   fi;od;
   Error("Lyndon split");
  end;
  Basis:=n->List(Filtered(Words(n),Lyndon),Expand);
  SpanDim:=function(columns)
   local nz;
   nz:=Filtered(columns,c->c<>Zero(algebra));
   if IsEmpty(nz) then return 0;fi;
   return Dimension(VectorSpace(Rationals,nz));
  end;
  C:=Expr(one[3]);U:=Expr(one[4]);D:=Expr(one[5]);p:=Weight(one[3]);q:=Weight(one[5]);
  us:=Basis(p+1);vs:=Basis(q+1);
  cols:=Concatenation(List(us,x->Bracket(x,D)),List(vs,x->Bracket(C,x)));
  nul:=Length(cols)-SpanDim(cols);
  Require(nul=one[6] and [Length(us),Length(vs)]=one[8],"first kernel");
  if one[7] then
   V:=Bracket(U,Bracket(C,U));Require(Bracket(C,V)=Bracket(U,D),"exceptional direction");
   us:=Basis(p+2);vs:=Basis(q+2);
   final:=Concatenation(List(us,x->Bracket(x,D)),List(vs,x->Bracket(C,x)));
   dim:=SpanDim(final);dim2:=SpanDim(Concatenation(final,[Bracket(U,V)]));
   Require([Length(us),Length(vs)]=one[9] and dim=one[10] and dim2=dim+1,"quadratic obstruction");
   obstruct:=obstruct+1;
  fi;
  count:=count+1;Print(one[1]," kernel=",nul," verified\n");
 od;
 Print("PASS N8 general third structure GAP: ",count," first kernels; ",obstruct," quadratic obstructions\n");
end)();
QUIT_GAP(0);
