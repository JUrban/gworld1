# Independent replay of the full integer kernels and polynomial sections.
if not IsBound(N8PolynomialFamiliesFile) then Error("Set fixtures");fi;
Read(N8PolynomialFamiliesFile);;
(function()
 local t,Poly,Mat,Eq,Eval,EvalMat,IntegralPoly,Require,item,A,b,H,U,K,r,n,
       row,i,j,last,pivot,point,expected,systems,sections,scale;
 t:=Indeterminate(Rationals,"T");
 Require:=function(x,s)if not x then Error(s);fi;end;
 Poly:=data->Sum([1..Length(data)],i->data[i][1]/data[i][2]*t^(i-1));
 Mat:=data->List(data.entries,row->List(row,Poly));
 Eq:=function(A,B)
  return Length(A)=Length(B) and ForAll([1..Length(A)],i->Length(A[i])=Length(B[i]) and
   ForAll([1..Length(A[i])],j->IsZero(A[i][j]-B[i][j])));
 end;
 Eval:=function(p,x)if IsRat(p) then return p;fi;return Value(p,x);end;
 EvalMat:=function(A,x)return List(A,row->List(row,p->Eval(p,x)));end;
 IntegralPoly:=function(p)
  if IsRat(p) then return IsInt(p);fi;
  return ForAll(CoefficientsOfUnivariatePolynomial(p),IsInt);
 end;
 systems:=0;sections:=0;
 for item in N8PolynomialFamilies do
  A:=Mat(item.A);b:=Mat(item.b);H:=Mat(item.H);U:=Mat(item.U);K:=Mat(item.kernel);
  r:=item.rank;n:=item.A.cols;
  Require(ForAll(Concatenation(A),IsRat),"Matrix not constant");
  Require(RankMat(A)=r and Length(H)=n,"Incorrect rank/dimension");
  Require(ForAll(Concatenation(U),IsInt) and AbsInt(DeterminantMat(U))=1,"Not unimodular");
  Require(Eq(H,U*(item.integer_scale*TransposedMat(A))),"Hermite transformation");
  last:=0;
  for i in [1..n] do
   pivot:=PositionProperty(H[i],x->x<>0);
   if i<=r then
    Require(pivot<>fail and pivot>last and H[i][pivot]>0,"Hermite pivot");last:=pivot;
   else Require(pivot=fail,"Nonzero kernel row");fi;
  od;
  Require(item.kernel.rows=n and item.kernel.cols=n-r,"Kernel dimensions");
  for i in [1..n] do for j in [1..n-r] do
   Require(K[i][j]=U[r+j][i],"Incomplete integer kernel");
  od;od;
  scale:=item.certificate.input_scale;
  Require(Eq(Mat(item.certificate.P),scale*A) and Eq(Mat(item.certificate.b),scale*b),"Arithmetic input mismatch");
  if item.mode="finite" then
   Require(List(item.families,row->row.t)=item.certificate.accepted,"Missing finite parameter");
   for row in item.families do
    Require(ForAll(row.point,IsInt) and Eq(A*List(row.point,x->[x]),EvalMat(b,row.t)),"Finite section");
    sections:=sections+1;
   od;
  else
   Require(item.certificate.mode="periodic" and item.period=item.certificate.K and
    item.certificate.rank_drop=[],"Incorrect period or variable rank");
   Require(List(item.families,row->row.residue)=item.certificate.accepted_residues,"Missing residue");
   for row in item.families do
    point:=Mat(row.point);
    Require(ForAll(Concatenation(point),IntegralPoly),"Nonintegral polynomial section");
    Require(Eq(A*point,EvalMat(b,item.period*t+row.residue)),"Polynomial section identity");
    sections:=sections+1;
   od;
  fi;
  systems:=systems+1;
 od;
 Print("PASS N8 polynomial families GAP: ",systems," complete integer kernels; ",sections," exact polynomial or point sections\n");
end)();
QUIT_GAP(0);
