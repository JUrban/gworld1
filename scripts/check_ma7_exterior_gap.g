# Independent native GAP structure-constant algebra and finite-field ranks.
Read("research/certificates/MA7-exterior/fixtures.g");
MA7Check := function(data)
  local n,d,f,dim,mons,tab,i,j,k,ij,alg,basis,one,zero,decode,
    ident,mat,fac,target,zmat,q,qr,boundary,expected,rankz;
  n:=data[1]; d:=data[2]; f:=GF(3);
  mons:=[[]];
  for i in [1..d] do Add(mons,[i]); od;
  for i in [1..d] do for j in [i+1..d] do Add(mons,[i,j]); od; od;
  dim:=Length(mons);
  tab:=EmptySCTable(dim,Zero(f));
  for i in [1..dim] do
    SetEntrySCTable(tab,1,i,[One(f),i]);
    SetEntrySCTable(tab,i,1,[One(f),i]);
  od;
  for i in [1..d] do for j in [i+1..d] do
    ij:=Position(mons,[i,j]);
    SetEntrySCTable(tab,i+1,j+1,[One(f),ij]);
    SetEntrySCTable(tab,j+1,i+1,[-One(f),ij]);
  od; od;
  alg:=AlgebraByStructureConstants(f,tab);
  basis:=BasisVectors(Basis(alg)); one:=basis[1]; zero:=Zero(alg);
  decode:=function(terms)
    local a,t;
    a:=zero;
    for t in terms do a:=a+(t[1]*One(f))*basis[Position(mons,t[2])]; od;
    return a;
  end;
  ident:=List([1..n],i->List([1..n],j->zero));
  for i in [1..n] do ident[i][i]:=one; od;
  mat:=StructuralCopy(ident);
  for fac in data[3] do
    target:=StructuralCopy(ident);
    target[fac[1]][fac[2]]:=decode(fac[3]);
    mat:=mat*target;
  od;
  target:=List(data[4],row->List(row,decode));
  if mat<>target then Error("elementary product mismatch"); fi;
  if mat[1][2]<>one then Error("off-diagonal unit missing"); fi;
  zmat:=data[5]*One(f); rankz:=RankMat(zmat);
  if rankz<>d then Error("bivector rank mismatch"); fi;
  for k in [1..Length(data[6])] do
    q:=data[6][k]*One(f); qr:=RankMat(q);
    expected:=RankMat(q*zmat*TransposedMat(q));
    if qr<>d-2*n*n or expected<>data[7][k] or expected<2 then
      Error("quotient rank mismatch");
    fi;
  od;
  boundary:=data[8]*One(f);
  if RankMat(boundary)<>d/2 or RankMat(boundary*zmat*TransposedMat(boundary))<>0 then
    Error("boundary control mismatch");
  fi;
  Print("PASS MA7 GAP exterior: dimension=",dim," factors=",Length(data[3]),
        " z_rank=",rankz," quotient_checks=",Length(data[6])," boundary=0\n");
end;
MA7Check(MA7Fixture);
QUIT_GAP(0);
