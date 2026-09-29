# Independent reconstruction in GAP's free associative and polynomial algebras.
# No Python coefficient matrices or nullspaces are read.
(function()
 local algebra,e,Bracket,Words,Lyndon,Expand,BasisPairs,Restriction,Rank,
       m,k,db,vb,columns,nz,basis,rows,null,coeff,D,V,Q,images,rank,
       expected,records,record,x,small,space;
 algebra:=FreeAssociativeAlgebraWithOne(Rationals,12,"E");
 e:=GeneratorsOfAlgebraWithOne(algebra);
 Bracket:=function(a,b)return a*b-b*a;end;
 Words:=function(total,length)
  local out,i,w;out:=[];
  if total<0 then return out;fi;
  if length=0 then if total=0 then return [[]];else return out;fi;fi;
  for i in [0..total] do for w in Words(total-i,length-1) do
   Add(out,Concatenation([i+1],w));
  od;od;return out;
 end;
 Lyndon:=function(w)
  local j;for j in [2..Length(w)] do if not w<w{[j..Length(w)]} then return false;fi;od;
  return true;
 end;
 Expand:=function(w)
  local j,a,b;
  if Length(w)=1 then return [e[w[1]],e[w[1]+1]];fi;
  for j in [2..Length(w)] do if Lyndon(w{[j..Length(w)]}) then
   a:=Expand(w{[1..j-1]});b:=Expand(w{[j..Length(w)]});
   return [Bracket(a[1],b[1]),Bracket(a[2],b[1])+Bracket(a[1],b[2])];
  fi;od;Error("No Lyndon split");
 end;
 BasisPairs:=function(total,length)
  return List(Filtered(Words(total,length),Lyndon),Expand);
 end;
 x:=List([1..4],i->Indeterminate(Rationals,Concatenation("z",String(i))));
 Restriction:=function(poly,length)
  local data,j,w,vars,mon,out;
  vars:=Concatenation([x[1]],x{[2..length]},[-2*x[1]-Sum(x{[2..length]})],[x[1]]);
  data:=CoefficientsAndMagmaElements(poly);out:=Zero(x[1]);
  for j in [1,3..Length(data)-1] do
   w:=LetterRepAssocWord(data[j]);
   if Length(w)<>length+2 then Error("Wrong E-letter count");fi;
   mon:=Product([1..Length(w)],i->vars[i]^(w[i]-1));
   out:=out+data[j+1]*mon;
  od;return out;
 end;
 Rank:=function(polys)
  local nonzero;nonzero:=Filtered(polys,p->not IsZero(p));
  if IsEmpty(nonzero) then return 0;fi;
  return Dimension(VectorSpace(Rationals,nonzero));
 end;
 records:=[];
 for m in [1..4] do for k in [0..10] do
  db:=BasisPairs(k,m);vb:=BasisPairs(k-1,m+1);
  columns:=Concatenation(List(db,p->Bracket(e[1],p[1])),List(vb,p->p[2]));
  nz:=Filtered(columns,p->not IsZero(p));
  if IsEmpty(columns) then null:=[];
  elif IsEmpty(nz) then null:=IdentityMat(Length(columns),Rationals);
  else
   basis:=Basis(VectorSpace(Rationals,nz));
   rows:=List(columns,p->Coefficients(basis,p));null:=NullspaceMat(rows);
  fi;
  images:=[];space:=[];
  for coeff in null do
   D:=Sum([1..Length(db)],i->coeff[i]*db[i][1],Zero(algebra));
   V:=Sum([1..Length(vb)],i->-coeff[Length(db)+i]*vb[i][1],Zero(algebra));
   if IsZero(D) then Error("Projected kernel not injective");fi;
   if Bracket(e[1],D)<>Sum([1..Length(vb)],i->-coeff[Length(db)+i]*vb[i][2],Zero(algebra)) then
    Error("Differential identity");fi;
   Q:=Bracket(e[1],V);Add(images,Restriction(Q,m));Add(space,D);
  od;
  if Rank(space)<>Length(null) then Error("D directions dependent");fi;
  rank:=Rank(images);expected:=Length(null);
  if m=1 and k=0 then expected:=expected-1;fi;
  if rank<>expected then Error("Restriction kernel",m,k,rank,expected);fi;
  record:=[m,k,Length(db),Length(vb),Length(null),rank];Add(records,record);
  Print("space m,k,dimD,dimV,compatible,rank = ",record,"\n");
 od;od;
 # Non-Lie control: the excluded constant positional polynomial exists at m=2.
 if not IsZero(Restriction(Bracket(e[1],Zero(algebra)),2)) then Error("Zero control");fi;
 PrintTo("research/certificates/N8-diagonal-quadratic-gap-v1.g","N8DiagonalGap := ",records,";\n");
 Print("PASS N8 independent diagonal restriction: 44 complete Lie spaces\n");
end)();
QUIT_GAP(0);
