# Complete first-successor-compatible two-e deformation spaces in fixed weights.
# A bounded Lie probe only; no general theorem or actual group family is claimed.
(function()
 local alg,g,Bracket,Words,Lyndon,Expand,BasisWords,BasisLie,VectorRows,
       q,E,i,j,D,V3,quadratic,dbasis,vbasis,early,coordinates,null,
       compatible,basis,late,images,rank,rankq,rankb,rankqb,rows,record,records;
 alg:=FreeAssociativeAlgebraWithOne(Rationals,2,"a");g:=GeneratorsOfAlgebraWithOne(alg);
 Bracket:=function(x,y)return x*y-y*x;end;
 Words:=function(a,e)
  local result,w;result:=[];
  if a=0 and e=0 then return [[]];fi;
  if a>0 then for w in Words(a-1,e) do Add(result,Concatenation([1],w));od;fi;
  if e>0 then for w in Words(a,e-1) do Add(result,Concatenation([2],w));od;fi;
  return result;
 end;
 Lyndon:=function(w)
  local i;for i in [2..Length(w)] do if not w<w{[i..Length(w)]} then return false;fi;od;
  return true;
 end;
 Expand:=function(w)
  local i;if Length(w)=1 then return g[w[1]];fi;
  for i in [2..Length(w)] do if Lyndon(w{[i..Length(w)]}) then
   return Bracket(Expand(w{[1..i-1]}),Expand(w{[i..Length(w)]}));fi;od;
  Error("Lyndon split");
 end;
 BasisWords:=function(a,e)return Filtered(Words(a,e),Lyndon);end;
 BasisLie:=function(a,e)return List(BasisWords(a,e),Expand);end;
 records:=[];
 for q in [8,10..20] do
  E:=[g[2]];for i in [1..q-4] do Add(E,Bracket(g[1],Last(E)));od;D:=E[q-3];
  V3:=Zero(alg);
  for i in [0..(q-4)/2-1] do V3:=V3+(-1)^(i+1)*Bracket(E[i+1],E[q-4-i]);od;
  if not IsZero(Bracket(E[1],D)+Bracket(g[1],V3)) then Error("First kernel identity");fi;
  quadratic:=Bracket(E[1],V3);
  dbasis:=BasisLie(q-7,2);vbasis:=BasisLie(q-8,3);
  early:=Concatenation(List(vbasis,x->Bracket(g[1],x)),List(dbasis,x->Bracket(E[1],x)));
  basis:=Basis(VectorSpace(Rationals,early));
  coordinates:=List(early,x->Coefficients(basis,x));null:=NullspaceMat(coordinates);
  compatible:=List(null,row->Sum([1..Length(dbasis)],i->row[Length(vbasis)+i]*dbasis[i],Zero(alg)));
  if not IsEmpty(compatible) then compatible:=BasisVectors(Basis(VectorSpace(Rationals,compatible)));fi;
  late:=List(BasisLie(q-6,3),x->Bracket(g[1],x));
  images:=List(compatible,x->Bracket(E[3],x));
  rank:=Dimension(VectorSpace(Rationals,late));
  rankq:=Dimension(VectorSpace(Rationals,Concatenation(late,[quadratic])));
  rankb:=Dimension(VectorSpace(Rationals,Concatenation(late,images)));
  rankqb:=Dimension(VectorSpace(Rationals,Concatenation(late,images,[quadratic])));
  if rankq<>rank+1 then Error("Exceptional quadratic absent");fi;
  record:=rec(q:=q,deformation_dimension:=Length(dbasis),successor_domain_dimension:=Length(vbasis),
     compatible_dimension:=Length(compatible),early_matrix:=coordinates,early_kernel:=null,
     ranks:=[rank,rankq,rankb,rankqb],absorbed_by_compatible_space:=rankqb=rankb);
  Add(records,record);
  Print("q=",q," full two-e deformation dimension=",Length(dbasis),
    " compatible dimension=",Length(compatible)," ranks A,Q,B,QB=",record.ranks,
    " absorption=",record.absorbed_by_compatible_space,"\n");
 od;
 PrintTo("research/certificates/N8-successor-compatible-space-v1.g","N8CompatibleSpace := ",records,";\n");
 Print("PASS N8 complete successor-compatible Lie spaces: ",Length(records)," cases; bounded probe only\n");
end)();
QUIT_GAP(0);
