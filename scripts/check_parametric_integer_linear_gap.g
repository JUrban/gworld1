# Independently check complete finite/periodic certificates in GAP.
if not IsBound(ParametricIntegerFile) then Error("Set fixture path");fi;
ParametricIntegerFixtures:=[];;Read(ParametricIntegerFile);;+(function()
 local tvar,Poly,Mat,Coefs,Eval,EvalMat,IRoots,IntegralPoly,Direct,Require,Abs,Eq,
       item,P,b,D,U,V,Vi,beta,m,n,r,M,roots,i,j,x,candidates,check,z,q,rem,N,R,
       dc,rc,lead,lower,total,rb,B,K,Z,L,free,zero,cong,rhs,sol,ell,residues,
       expected,actual,samples,finiteChecks,modChecks,systems,witnesses;
 tvar:=Indeterminate(Rationals,"T");
 Require:=function(ok,s)if not ok then Error(s);fi;end;
 Abs:=x->Maximum(x,-x);
 Eq:=function(A,B)
  return Length(A)=Length(B) and ForAll([1..Length(A)],i->Length(A[i])=Length(B[i]) and
   ForAll([1..Length(A[i])],j->IsZero(A[i][j]-B[i][j])));
 end;
 Poly:=function(data)return Sum([1..Length(data)],i->data[i][1]/data[i][2]*tvar^(i-1));end;
 Mat:=data->List(data.entries,row->List(row,Poly));
 Coefs:=function(p)
  if IsRat(p) then return [p];fi;
  return CoefficientsOfUnivariatePolynomial(p);
 end;
 Eval:=function(p,t)if IsRat(p) then return p;fi;return Value(p,t);end;
 EvalMat:=function(A,t)return List(A,row->List(row,p->Eval(p,t)));end;
 IntegralPoly:=p->ForAll(Coefs(p),IsInt);
 IRoots:=function(p)
  local factors,f,c,out;
  if Length(Coefs(p))<=1 then Require(not IsZero(p),"Roots of zero");return [];fi;
  factors:=Factors(p);out:=[];
  for f in factors do
   c:=Coefs(f);
   if Length(c)=2 and IsInt(-c[1]/c[2]) then AddSet(out,-c[1]/c[2]);fi;
  od;return out;
 end;
 Direct:=function(A,b)
  local x;
  x:=SolutionIntMat(TransposedMat(A),List(b,r->r[1]));
  if x<>fail then Require(ForAll(x,IsInt) and x*TransposedMat(A)=List(b,r->r[1]),"Integer solver witness");fi;
  return x;
 end;
 systems:=0;samples:=0;finiteChecks:=0;modChecks:=0;witnesses:=0;
 for item in ParametricIntegerFixtures do
  P:=Mat(item.P);b:=Mat(item.b);D:=Mat(item.D);U:=Mat(item.U);V:=Mat(item.V);
  Vi:=Mat(item.Vi);beta:=Mat(item.beta);m:=item.P.rows;n:=item.P.cols;r:=item.rank;M:=item.M;
  Require(Eq(U*P*V,D) and Eq(U*b,beta),"Polynomial Smith identity");
  Require(Length(Coefs(DeterminantMat(U)))=1 and not IsZero(DeterminantMat(U)),"U not polynomial unimodular");
  Require(Eq(V*Vi,IdentityMat(n)),"V inverse identity");
  Require(IsInt(M) and M>0 and ForAll(Concatenation(Vi),x->IntegralPoly(M*x)),"Inverse denominator");
  Require(ForAll(Concatenation(P),IntegralPoly) and ForAll(Concatenation(b),IntegralPoly),"Input denominator not cleared");
  for i in [1..m] do for j in [1..n] do
   if i=j and i<=r then Require(not IsZero(D[i][j]),"Zero rank entry");
   else Require(IsZero(D[i][j]),"Not diagonal");fi;
  od;od;
  roots:=[];for i in [1..r] do UniteSet(roots,IRoots(D[i][i]));od;
  Require(roots=item.rank_drop,"Incomplete rank-drop set");
  if item.mode="finite_zero_row" then
   i:=item.critical_row+1;Require(i>r and not IsZero(beta[i][1]),"Invalid zero-row obstruction");
   candidates:=Union(IRoots(beta[i][1]),roots);
  elif item.mode="finite_fraction" then
   i:=item.critical_row+1;q:=Poly(item.quotient);rem:=Poly(item.remainder);
   N:=item.N;R:=Poly(item.R);B:=item.bound;
   Require(i<=r and not IsZero(rem) and IsZero(beta[i][1]-q*D[i][i]-rem),"Polynomial division");
   dc:=Coefs(D[i][i]);rc:=Coefs(R);
   Require(Length(Coefs(rem))<Length(dc),"Improper remainder degree");
   Require(N>0 and IsInt(N) and IntegralPoly(N*M*q) and IsZero(R-N*M*rem),"Fraction denominator clearing");
   lead:=Abs(Last(dc));lower:=Sum(dc{[1..Length(dc)-1]},Abs);total:=Sum(rc,Abs);
   rb:=1+Sum(rc{[1..Length(rc)-1]},Abs)/Abs(Last(rc));
   Require(B>=1 and B>=2*lower/lead and B>=2*total/lead and B>=rb,"Insufficient finite bound");
   candidates:=Union([-B..B],roots);
  else
   Require(item.mode="periodic","Unknown certificate mode");
   Require(ForAll([r+1..m],i->IsZero(beta[i][1])),"Unresolved zero row");
   K:=item.K;Z:=Mat(item.Z);L:=Mat(item.L);free:=n-r;
   Require(K>0 and IsInt(K) and ForAll(Concatenation(Z),IntegralPoly) and ForAll(Concatenation(L),IntegralPoly),"Bad congruence denominator");
   Require(Eq(P*Z,K*b),"Particular polynomial solution");
   if free>0 then
    Require(Eq(P*L,NullMat(m,free)),"Kernel polynomial solution");
    Require(Eq(L,List(V,row->K/M*row{[r+1..n]})),"Incomplete free columns");
   else Require(item.L.cols=0,"Wrong free dimension");fi;
   zero:=Vi*Z;
   for i in [1..r] do Require(IsZero(D[i][i]*zero[i][1]-K*beta[i][1]),"Forced transformed solution");od;
   for i in [r+1..n] do Require(IsZero(zero[i][1]),"Particular free coordinate");od;
   Require(List(item.residue_checks,x->x.residue)=[0..K-1],"Incomplete residue list");
   residues:=[];
   for check in item.residue_checks do
    cong:=List([1..n],i->Concatenation(List([1..free],j->Eval(L[i][j],check.residue)),
                    List([1..n],j->K*IdentityMat(n)[i][j])));
    rhs:=-EvalMat(Z,check.residue);sol:=Direct(cong,rhs);
    Require((sol=fail)=(check.ell=fail),"Residue decision mismatch");
    if check.ell<>fail then
     ell:=check.ell;Require(Length(ell)=free and ForAll(ell,x->IsInt(x) and x>=0 and x<K),"Residue witness format");
     for i in [1..n] do Require((Eval(Z[i][1],check.residue)+Sum([1..free],j->Eval(L[i][j],check.residue)*ell[j])) mod K=0,"Residue witness failed");od;
     Add(residues,check.residue);
    fi;modChecks:=modChecks+1;
   od;
   Require(residues=item.accepted_residues,"Wrong accepted residue set");
   Require(List(item.rank_drop_checks,x->x.t)=roots,"Missing rank-drop checks");
   for check in item.rank_drop_checks do
    sol:=Direct(EvalMat(P,check.t),EvalMat(b,check.t));
    Require((sol=fail)=(check.witness=fail),"Rank-drop decision mismatch");
    if check.witness<>fail then Require(check.witness*TransposedMat(EvalMat(P,check.t))=List(EvalMat(b,check.t),x->x[1]),"Rank-drop witness failed");fi;
    finiteChecks:=finiteChecks+1;
   od;
  fi;
  if item.mode<>"periodic" then
   Require(List(item.finite_checks,x->x.t)=candidates,"Incomplete finite check interval");
   expected:=[];
   for check in item.finite_checks do
    sol:=Direct(EvalMat(P,check.t),EvalMat(b,check.t));
    Require((sol=fail)=(check.witness=fail),"Finite decision mismatch");
    if check.witness<>fail then
     Require(check.witness*TransposedMat(EvalMat(P,check.t))=List(EvalMat(b,check.t),x->x[1]),"Finite witness failed");
     Add(expected,check.t);
    fi;finiteChecks:=finiteChecks+1;
   od;
   Require(expected=item.accepted,"Wrong finite accepted set");
  fi;
  for x in item.sample_parameters do
   actual:=Direct(EvalMat(P,x),EvalMat(b,x))<>fail;
   if item.mode<>"periodic" then expected:=x in item.accepted;
   elif x in roots then expected:=First(item.rank_drop_checks,z->z.t=x).witness<>fail;
   else expected:=x mod item.K in item.accepted_residues;fi;
   Require(actual=expected,"Specialization mismatch");samples:=samples+1;
  od;
  if item.witness<>fail then
   check:=item.witness;
   Require(ForAll(check.witness,IsInt) and check.witness*TransposedMat(EvalMat(P,check.t))=List(EvalMat(b,check.t),x->x[1]),"Final witness failed");
   witnesses:=witnesses+1;
  fi;
  systems:=systems+1;Print(item.name," verified\n");
 od;
 Print("PASS parametric integers GAP: ",systems," complete systems; ",finiteChecks," finite checks; ",
       modChecks," residue checks; ",samples," specializations; ",witnesses," final witnesses\n");
end)();
QUIT_GAP(0);
