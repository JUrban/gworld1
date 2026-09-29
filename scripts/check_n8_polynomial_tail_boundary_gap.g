# Independent leading-Lie certificate replay; the four full group products
# are computed by the Python constructor, not by this checker.
Read("research/certificates/N8-polynomial-group-tail/boundary25/fixtures.g");;
(function()
 local data,A,gens,B,Iter,u,v,actual,expected,row,weights;
 data:=N8PolynomialTailBoundary;weights:=[1,4];
 if data[1]<>[4,13] then Error("Boundary setup");fi;
 A:=FreeAssociativeAlgebraWithOne(Rationals,2,"a");gens:=GeneratorsOfAlgebraWithOne(A);
 B:=function(x,y)return x*y-y*x;end;
 Iter:=function(n)local i,e;e:=gens[2];for i in [1..n] do e:=B(gens[1],e);od;return e;end;
 u:=Iter(4);v:=Iter(13);expected:=B(u,v);actual:=Zero(A);
 for row in data[2] do
  if Sum(row[1],i->weights[i+1])<>25 then Error("Wrong mixed weight");fi;
  actual:=actual+row[2]*Product(List(row[1],i->gens[i+1]));
 od;
 if actual<>expected or IsZero(actual) then Error("Mixed boundary bracket");fi;
 Print("PASS N8 polynomial tail boundary GAP: nonzero weight25 leading mixed bracket; ",Length(data[2])," coefficients\n");
end)();
QUIT_GAP(0);
