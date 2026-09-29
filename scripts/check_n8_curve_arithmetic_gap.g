# Independent native integer/polynomial replay. No Python solver imported.
# The small rational-root helper follows the existing GAP checker pattern
# at e7f9c4d; every seed box, residue orbit and polynomial is rebuilt here.
if not IsBound(N8CurveFixtureFile) then N8CurveFixtureFile:="research/certificates/N8-curve-arithmetic/v2/fixtures.g";fi;
Read(N8CurveFixtureFile);;
(function()
 local Require,CeilRoot,Allowed,Poly,Coefs,IRoots,Eval,SmallDet,
       row,d,n,h,j,box,seeds,x,w,w2,M,cycle,i,k,good,seen,refs,
       witness,point,decision,count,positive,negative,seedcount,states,
       skipped,tvar,rvar,zvar,a,b,c,f,A,G,H,roots,cs,u,v,ww,
       tt,zz,rr,lhs,rhs,grid,factorcount,totalgrid,
       remainder0,remainder1,term,power,m,qcoeff,hcoeff,sylvester,
       rrrow,resultant,points,intersections,pointcount;
 Require:=function(ok,msg)if not ok then Error(msg);fi;end;
 # The default matrix determinant method does not accept these mixed
 # integer/polynomial lists. Matrices are at most 5 by 5: use the exact
 # Leibniz formula, independently of SymPy's resultant construction.
 SmallDet:=function(mat)
  local len;len:=Length(mat);
  return Sum(PermutationsList([1..len]),p->
   (-1)^Sum([1..len],i->Number([i+1..len],j->p[i]>p[j]))*
   Product([1..len],i->mat[i][p[i]]));
 end;
 CeilRoot:=function(n)local q;q:=RootInt(n);if q*q<n then q:=q+1;fi;return q;end;
 Allowed:=function(conditions,p)
  return ForAll(conditions,r->Sum(r[1],v->v[1]*p[1]^v[2]*p[2]^v[3]) mod r[2]=0);
 end;
 count:=0;positive:=0;negative:=0;seedcount:=0;states:=0;skipped:=0;
 for row in N8CurveFixtures.pell do
  d:=row.d;n:=row.n;h:=row.unit[1];j:=row.unit[2];
  Require(d>0 and RootInt(d)^2<>d and n<>0,"Pell hypotheses");
  Require(h>0 and j>0 and h*h-d*j*j=1,"Norm-one integral unit");
  box:=QuoInt((h+j*CeilRoot(d)+1)*CeilRoot(AbsInt(n))+1,2);
  Require(box=row.bound,"Integer seed bound");
  seeds:=[];
  # Scan X and solve for W, independently of the constructor's W scan.
  for x in [-box..box] do
   w2:=x*x-n;
   if w2>=0 and w2 mod d=0 then
    w2:=QuoInt(w2,d);w:=RootInt(w2);
    if w*w=w2 and w<=box then AddSet(seeds,[x,w]);AddSet(seeds,[x,-w]);fi;
   fi;
  od;
  Require(seeds=row.seeds,"Incomplete Pell seed list");
  Require(row.modulus=Lcm(Concatenation([1],List(row.conditions,r->r[2]))),"Common modulus");
  M:=[[h,d*j],[j,h]];Require(DeterminantMat(M)=1,"Noninvertible transition");
  seen:=[];
  for cycle in row.cycles do
   Require(not IsEmpty(cycle.states) and Length(Set(cycle.states))=Length(cycle.states),"Orbit repeats");
   Require(Length(cycle.states)<=row.modulus^2,"Orbit length bound");
   good:=[];
   for i in [1..Length(cycle.states)] do
    point:=cycle.states[i];
    Require(ForAll(point,v->v>=0 and v<row.modulus),"Noncanonical state");
    Require(not point in seen,"Duplicate cycles");Add(seen,point);
    k:=i mod Length(cycle.states)+1;
    Require(List(M*point,v->v mod row.modulus)=cycle.states[k],"Missing orbit edge");
    if Allowed(row.conditions,point) then Add(good,i-1);fi;
   od;
   Require(good=cycle.good,"Allowed states incomplete");
   states:=states+Length(cycle.states);
  od;
  Require(Length(row.seed_refs)=Length(seeds),"Missing seed references");
  refs:=[];
  for i in [1..Length(seeds)] do
   k:=row.seed_refs[i];AddSet(refs,k[1]+1);
   Require(List(seeds[i],v->v mod row.modulus)=row.cycles[k[1]+1].states[k[2]+1],"Wrong seed orbit");
  od;
  Require(refs=[1..Length(row.cycles)],"Unseeded orbit");
  decision:=ForAny(row.cycles,r->not IsEmpty(r.good));
  Require(decision=row.decision and decision=(row.witness<>fail),"Complete decision mismatch");
  Require(ForAll(row.forbidden,p->p[1]^2-d*p[2]^2=n),"Excluded point off conic");
  if decision then
   witness:=row.witness;Require(witness.exponent>=0,"Unexpected exponent");
   point:=M^witness.exponent*seeds[witness.seed+1];
   Require(point=witness.pair and point[1]^2-d*point[2]^2=n,"Wrong norm witness");
   Require(Allowed(row.conditions,point) and not point in row.forbidden,"Invalid constrained witness");
   skipped:=skipped+witness.skipped;positive:=positive+1;
  else negative:=negative+1;fi;
  seedcount:=seedcount+Length(seeds);count:=count+1;
 od;
 tvar:=Indeterminate(Rationals,"T");rvar:=Indeterminate(Rationals,"R");zvar:=Indeterminate(Rationals,"Z");
 Poly:=v->Sum([1..Length(v)],i->v[i]*tvar^(i-1));
 Coefs:=function(p)if IsRat(p) then return [p];fi;return CoefficientsOfUnivariatePolynomial(p);end;
 Eval:=function(p,t)if IsRat(p) then return p;fi;return Value(p,t);end;
 IRoots:=function(p)
  local roots,part,cs;roots:=[];
  if Length(Coefs(p))<=1 then return roots;fi;
  for part in Factors(p) do
   cs:=Coefs(part);
   if Length(cs)=2 and IsInt(-cs[1]/cs[2]) then AddSet(roots,-cs[1]/cs[2]);fi;
  od;return roots;
 end;
 factorcount:=0;totalgrid:=0;
 for row in N8CurveFixtures.factors do
  a:=row.a;b:=Poly(row.b);c:=Poly(row.c);f:=Poly(row.F);A:=Poly(row.A);G:=Poly(row.G);
  Require(a<>0 and f=b*b-4*a*c,"Discriminant identity");
  Require((2*a*rvar+b)^2-f=4*a*(a*rvar^2+b*rvar+c),"Square completion");
  Require(A*A*G=f,"Squarefactor identity");
  if not IsZero(f) then
   Require(not IsZero(A) and not IsZero(G),"Invalid factorization");
   if Length(Coefs(G))>1 then Require(Length(Coefs(Gcd(G,Derivative(G))))=1,"Repeated residual root");fi;
   Require(IRoots(A)=row.roots,"Incomplete exceptional roots");
  else Require(IsZero(A) and IsZero(G) and IsEmpty(row.roots),"Zero-discriminant branch");fi;
  H:=Sum(row.H,v->v[1]*tvar^v[2]*zvar^v[3]);
  Require(H=(A*zvar-b)^2+2*a*tvar*(A*zvar-b)+8*a*a,"Congruence scaling identity");
  cs:=Coefs(G);
  if Length(cs)=3 then
   ww:=cs[1];v:=cs[2];u:=cs[3];Require(v*v-4*u*ww<>0,"Repeated quadratic root");
   Require((2*u*tvar+v)^2-u*(2*zvar)^2-(v*v-4*u*ww)=4*u*(G-zvar^2),"Pell reconstruction");
  fi;
  grid:=0;
  for tt in [-7..7] do for zz in [-7..7] do
   rr:=(Eval(A,tt)*zz-Eval(b,tt))/(2*a);
   if IsInt(rr) then
    lhs:=(rr^2+tt*rr+2) mod 5=0;
    rhs:=Sum(row.H,v->v[1]*tt^v[2]*zz^v[3]) mod (5*(2*a)^2)=0;
    Require(lhs=rhs,"Congruence equivalence");grid:=grid+1;
   fi;
  od;od;
  Require(grid=row.grid,"Grid coverage");totalgrid:=totalgrid+grid;factorcount:=factorcount+1;
 od;
 row:=N8CurveFixtures.wrong_modulus;
 Require(row.z^2=100 and row.a*row.r^2+10*row.t*row.r+5*row.t^2-5=0,"False-modulus control off curve");
 Require(row.original=row.r^2+row.t*row.r+2 and row.scaled=(2*row.a)^2*row.original,"False-modulus values");
 Require(row.original mod row.modulus<>0 and row.scaled mod row.modulus=0
  and row.scaled mod (row.modulus*(2*row.a)^2)<>0,"Wrong modulus was not rejected");
 intersections:=0;pointcount:=0;
 for row in N8CurveFixtures.intersections do
  d:=row.d;n:=row.n;Require(d>0 and RootInt(d)^2<>d and n<>0,"Conic hypotheses");
  remainder0:=0;remainder1:=0;
  for term in row.H do
   power:=term[1]*tvar^term[2]*((tvar^2-n)/d)^QuoInt(term[3],2);
   if term[3] mod 2=0 then remainder0:=remainder0+power;else remainder1:=remainder1+power;fi;
  od;
  Require(row.identical=(IsZero(remainder0) and IsZero(remainder1)),"Conic divisibility");
  m:=Maximum(List(row.H,v->v[3]));qcoeff:=[-d,0,tvar^2-n];
  hcoeff:=List([0..m],k->Sum(Filtered(row.H,v->v[3]=m-k),v->v[1]*tvar^v[2]));
  sylvester:=[];
  for i in [0..m-1] do
   rrrow:=List([1..m+2],k->0);for k in [1..3] do rrrow[i+k]:=qcoeff[k];od;Add(sylvester,rrrow);
  od;
  for i in [0..1] do
   rrrow:=List([1..m+2],k->0);for k in [1..m+1] do rrrow[i+k]:=hcoeff[k];od;Add(sylvester,rrrow);
  od;
  resultant:=SmallDet(sylvester);
  Require(resultant=Poly(row.resultant),"Independent Sylvester determinant");
  if row.identical then
   Require(IsZero(resultant) and IsEmpty(row.roots) and IsEmpty(row.points),"Identical conic branch");
  else
   Require(not IsZero(resultant),"Vanishing finite resultant");
   roots:=IRoots(resultant);Require(roots=row.roots,"Incomplete intersection candidates");
   points:=[];
   for x in roots do
    w2:=(x*x-n)/d;
    if IsInt(w2) and w2>=0 then
     w:=RootInt(w2);
     if w*w=w2 then
      for ww in Set([w,-w]) do
       if Sum(row.H,v->v[1]*x^v[2]*ww^v[3])=0 then AddSet(points,[x,ww]);fi;
      od;
     fi;
    fi;
   od;
   Require(points=row.points,"Incomplete finite intersection");pointcount:=pointcount+Length(points);
  fi;
  intersections:=intersections+1;
 od;
 Require(count=N8CurveFixtures.totals.pell_systems and positive=N8CurveFixtures.totals.positive
  and negative=N8CurveFixtures.totals.negative and seedcount=N8CurveFixtures.totals.seeds
  and states=N8CurveFixtures.totals.residue_states and skipped=N8CurveFixtures.totals.exclusions_avoided
  and factorcount=N8CurveFixtures.totals.factor_identities and totalgrid=N8CurveFixtures.totals.congruence_grid
  and intersections=N8CurveFixtures.totals.intersections and pointcount=N8CurveFixtures.totals.intersection_points,"Totals mismatch");
 Print("PASS N8 constrained curve arithmetic GAP: ",count," complete Pell decisions (",positive," positive, ",negative," negative), ",seedcount," seeds, ",states," residue states, ",factorcount," polynomial identities, ",totalgrid," congruence controls, ",intersections," conic intersections, ",pointcount," points; wrong-modulus control rejected\n");
end)();
QUIT_GAP(0);
