# Independent native integer/polynomial replay. No Python solver imported.
# The small rational-root helper follows the existing GAP checker pattern
# at e7f9c4d; every seed box, residue orbit and polynomial is rebuilt here.
Read("research/certificates/N8-curve-arithmetic/fixtures.g");;
(function()
 local Require,CeilRoot,Allowed,Poly,Coefs,IRoots,Eval,
       row,d,n,h,j,box,seeds,x,w,w2,M,cycle,i,k,good,seen,refs,
       witness,point,decision,count,positive,negative,seedcount,states,
       skipped,tvar,rvar,zvar,a,b,c,f,A,G,H,roots,cs,u,v,ww,
       tt,zz,rr,lhs,rhs,grid,factorcount,totalgrid;
 Require:=function(ok,msg)if not ok then Error(msg);fi;end;
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
 Require(count=N8CurveFixtures.totals.pell_systems and positive=N8CurveFixtures.totals.positive
  and negative=N8CurveFixtures.totals.negative and seedcount=N8CurveFixtures.totals.seeds
  and states=N8CurveFixtures.totals.residue_states and skipped=N8CurveFixtures.totals.exclusions_avoided
  and factorcount=N8CurveFixtures.totals.factor_identities and totalgrid=N8CurveFixtures.totals.congruence_grid,"Totals mismatch");
 Print("PASS N8 constrained curve arithmetic GAP: ",count," complete Pell decisions (",positive," positive, ",negative," negative), ",seedcount," seeds, ",states," residue states, ",factorcount," polynomial identities, ",totalgrid," congruence controls\n");
end)();
QUIT_GAP(0);
