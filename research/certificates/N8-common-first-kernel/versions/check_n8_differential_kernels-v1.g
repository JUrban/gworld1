# Independently rebuild weighted Lyndon bases, differentiate recursively, and
# compute rational spans in GAP's native free associative algebra.
JAlgebra:=FreeAssociativeAlgebraWithOne(Rationals,66,"j");;
Jx:=GeneratorsOfAlgebraWithOne(JAlgebra);;
if Length(Jx)<>66 then Error("Generator convention");fi;
JBracket:=function(a,b)return a*b-b*a;end;
JWords:=function(n,seeds)
 local out,j,s,v;
 if n=0 then return [[]];fi;
 out:=[];
 for j in [0..n-2] do for s in [0..seeds-1] do
  for v in JWords(n-j-2,seeds) do Add(out,Concatenation([32*s+j+1],v));od;
 od;od;
 return out;
end;
JIsLyndon:=function(w)
 local i;
 for i in [2..Length(w)] do if not w<w{[i..Length(w)]} then return false;fi;od;
 return true;
end;
JExpand:=function(w)
 local i,p,q;
 if Length(w)=1 then return [Jx[w[1]],Jx[w[1]+1]];fi;
 for i in [2..Length(w)] do if JIsLyndon(w{[i..Length(w)]}) then
  p:=JExpand(w{[1..i-1]});q:=JExpand(w{[i..Length(w)]});
  return [JBracket(p[1],q[1]),JBracket(p[2],q[1])+JBracket(p[1],q[2])];
 fi;od;
 Error("No Lyndon split");
end;
JBasis:=function(n,seeds)
 return List(Filtered(JWords(n,seeds),JIsLyndon),JExpand);
end;
JNullity:=function(columns)
 local nz;
 nz:=Filtered(columns,c->c<>Zero(JAlgebra));
 if Length(nz)=0 then return Length(columns);fi;
 return Length(columns)-Dimension(VectorSpace(Rationals,nz));
end;
JCommon:=function(q)
 local ds,vs,cols,single,d,v,answer;
 ds:=JBasis(q,2);vs:=JBasis(q+1,2);
 cols:=[];single:=[];
 for d in ds do
  Add(cols,Jx[65]*JBracket(Jx[1],d[1])+Jx[66]*JBracket(Jx[33],d[1]));
  Add(single,JBracket(Jx[1],d[1]));
 od;
 for v in vs do
  Add(cols,Jx[65]*v[2]);Add(cols,Jx[66]*v[2]);Add(single,v[2]);
 od;
 answer:=[JNullity(cols),JNullity(single)];
 if answer<>[0,[1,0,1,0,1,1,2,1,4][q-1]] then Error("Common result",q,answer);fi;
 Print("common q=",q," dimensions=",[Length(ds),Length(vs)]," kernels=",answer,"\n");
end;
JDouble:=function(q)
 local ds,vs,ws,cols,d,v,w,expected,answer;
 ds:=JBasis(q,1);vs:=JBasis(q+1,1);ws:=JBasis(q+2,1);
 cols:=[];
 for d in ds do Add(cols,Jx[65]*JBracket(Jx[1],d[1]));od;
 for v in vs do Add(cols,Jx[65]*v[2]-Jx[66]*JBracket(Jx[1],v[1]));od;
 for w in ws do Add(cols,Jx[66]*w[2]);od;
 expected:=0;if q=2 then expected:=1;fi;
 answer:=JNullity(cols);
 if answer<>expected then Error("Double primitive result",q,answer);fi;
 Print("double q=",q," dimensions=",[Length(ds),Length(vs),Length(ws)]," kernel=",answer,"\n");
end;
for q in [2..10] do JCommon(q);od;
for q in [2..14] do JDouble(q);od;
Print("PASS N8 independent differential kernel GAP checks:9 common,13 double; boundary and nonzero-kernel controls\n");
QUIT;
