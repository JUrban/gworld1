# Independent specialization of the formal maps and full block period lattice.
# Load the independently constructed class26 GAP workspace before this script.
if not IsBound(N8PreparedGroup) or not IsBound(N8DelayedQuadraticFile)
   or not IsBound(N8DelayedPeriodsFile) then Error("Set group/block/period inputs");fi;
Read(N8DelayedQuadraticFile);;Read(N8DelayedPeriodsFile);;
Read("research/certificates/N8-three-exception-gauges-c26-v2/fixtures.g");;
(function()
 local block,periods,gauges,G,Require,Poly,Mat,hall,gens,i,h,Element,Correct,
       base,probe,formalImages,Images,Prefix,low,rows,A,J,End,L,H,U,record,
       gauge,sign,images,back,j,k,vec,z,counts,pair,expected,actual,tail,
       blockcolumns,terminalvector,index,step,probeaxes;
 block:=N8DelayedQuadratic;periods:=N8DelayedPeriods;gauges:=N8UniversalFixture;
 G:=N8PreparedGroup;
 Require:=function(ok,msg)if not ok then Error(msg);fi;end;
 Require(block.class_bound=26 and block.weights=[1,4] and HirschLength(G)=680,
         "Wrong ambient group");
 Require(ForAll(RelativeOrdersOfPcp(Pcp(G)),x->x=0),"Ambient torsion");
 Require(gauges{[1..3]}=[1,10,26],"Wrong formal group");
 Poly:=function(data)
  Require(Length(data)=1,"Expected constant matrix");return data[1][1]/data[1][2];
 end;
 Mat:=data->List(data.entries,row->List(row,Poly));
 A:=Mat(block.A);J:=Mat(block.J);End:=Mat(block.Aend);
 gens:=GeneratorsOfGroup(G){[2,1]};hall:=[];
 for i in [1..block.retained] do
  h:=block.hall[i];
  if IsEmpty(h[2]) then Add(hall,gens[i]);
  else Add(hall,Comm(hall[h[2][1]+1],hall[h[2][2]+1]));fi;
 od;
 Require(ForAll(block.boundaries,i->Comm(hall[block.hall[i+1][2][1]+1],hall[block.hall[i+1][2][2]+1])=One(G)),"Ambient defining boundary relation");
 Print("Period ambient Hall words reconstructed\n");
 Element:=function(terms)
  local result,x;result:=One(G);
  for x in terms do result:=result*hall[x[1]+1]^x[2];od;return result;
 end;
 Correct:=function(pair,axes,vec)
  local result,k;result:=ShallowCopy(pair);
  for k in [1..Length(axes)] do
   result[axes[k][1]+1]:=result[axes[k][1]+1]*hall[axes[k][2]+1]^vec[k];
  od;return result;
 end;
 base:=List(block.base,Element);
 # A variable pair with one unit correction in each input at offset7.
 # It need not lie in the target fiber: universal maps preserve every
 # pair's commutator, and the same prefix bound applies to both inputs.
 probeaxes:=List([0,1],side->First(block.block_axes,x->x[1]=side and block.hall[x[2]+1][1]=[1,10][side+1]+7));
 probe:=Correct(base,probeaxes,[1,-1]);
 Print("Period base and unit-correction probe reconstructed\n");
 Images:=function(pair,maps)
  local words,i,h,result,row,x,value;words:=[];
  for i in [1..gauges[5]] do
   h:=gauges[4][i];
   if IsEmpty(h[2]) then Add(words,pair[i]);
   else Add(words,Comm(words[h[2][1]+1],words[h[2][2]+1]));fi;
  od;
  result:=[];
  for row in maps do
   value:=One(G);for x in row do value:=value*words[x[1]+1]^x[2];od;
   Add(result,value);
  od;return result;
 end;
 Require(List(periods.records,x->x.offset)=[9,11,13,15],"Missing periods");
 counts:=0;blockcolumns:=[];
 for k in [1..Length(periods.records)] do
  record:=periods.records[k];gauge:=gauges[7][k];
  Require([record.offset,record.power]=gauge{[1,2]},"Wrong universal power");
  vec:=record.block_translation;z:=record.kernel_coordinates;
  Require(ForAll(Concatenation(vec,z),IsInt) and z[1]=0,"Lost integrality/free coordinate");
  Require(List(J,row->row*z)=vec and ForAll(A*vec,IsZero),"Block lattice translation");
  expected:=List(block.block_axes,x->Sum(Filtered(record.prefix[x[1]+1],y->y[1]=x[2]),y->y[2]));
  Require(expected=vec,"Translation/prefix mismatch");
  if k<4 then Add(blockcolumns,z{[2..4]});
  else
   Require(ForAll(vec,IsZero),"Last universal should leave block fixed");
   terminalvector:=List(block.end_axes,x->Sum(Filtered(record.prefix[x[1]+1],y->y[1]=x[2]),y->y[2]));
   Require(not ForAll(terminalvector,IsZero) and ForAll(End*terminalvector,IsZero),"Last full terminal period");
   Require(Length(block.end_axes)-RankMat(End)=1,"Terminal kernel not one-dimensional");
   step:=Gcd(terminalvector);
   Require(step>0 and step=periods.terminal_period_step and terminalvector/step=periods.terminal_primitive
    and Gcd(periods.terminal_primitive)=1,"Terminal integral step/primitive basis");
  fi;
  for pair in [base,probe] do
   for sign in [1,-1] do
    Print("Checking specialized period ",record.offset," sign ",sign," case ",counts+1,"\n");
    images:=Images(pair,gauge[3+(1-sign)/2]);
    back:=Images(images,gauge[3+(1+sign)/2]);
    Require(back=pair,"Specialized inverse composition");
    Require(Comm(images[1],images[2])=Comm(pair[1],pair[2]),"Specialized exact commutator");
    for j in [1,2] do
     expected:=Element(List(record.prefix[j],x->[x[1],sign*x[2]]));
     actual:=pair[j]^-1*images[j];
     rows:=Filtered([1..block.retained],i->block.hall[i][1]>[1,10][j]+15);
     tail:=Subgroup(G,hall{rows});
     Require(expected^-1*actual in tail,"Incorrect specialized prefix translation");
    od;
    counts:=counts+1;
   od;
  od;
 od;
 L:=Mat(periods.L);H:=Mat(periods.H);U:=Mat(periods.U);
 Require(L=TransposedMat(blockcolumns),"Wrong period columns");
 Require(H=U*TransposedMat(L) and AbsInt(DeterminantMat(U))=1,"Incomplete period lattice");
 Require(ForAll([1..3],i->H[i][i]>0 and ForAll([1..i-1],j->H[i][j]=0)),"Invalid triangular residue rule");
 Require(periods.residue_bounds=List([1..3],i->H[i][i]),"Wrong residue bounds");
 index:=AbsInt(DeterminantMat(L));
 Require(index=periods.quotient_order and Product(periods.residue_bounds)=index,"Wrong quotient order");
 Print("PASS N8 delayed periods GAP: ",counts," exact map specializations; complete lattice quotient order ",index,"; terminal period ",step," (residues described, not enumerated)\n");
end)();
