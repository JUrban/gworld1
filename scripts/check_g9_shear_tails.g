# Native flow reconstruction of disjoint shear tails; no Python invocation.
Read("research/certificates/G9-steiner-seeds-v1/fixtures.g");
Read("research/certificates/G9-steiner-completion-v1/fixtures.g");
Read("research/certificates/G9-shear-tails-v1/fixtures.g");
(function()
 local compute,act,shear,normal,words,data,row,r,p,e,keys,values,seen,groups,
       index,g,h,expected,low,high,tail,sign,boundary,choices,best,base,n,k,
       pair,w,other,controlCount,compositionCount,terms,termKeys,pos,
       assignments,oi,old,first,counts,degree,term,delta,horizontal,evaluate,
       lowerValue,upperValue,excluded;
 compute:=function(word)
  local point,maximum,ks,vs,a,axis,sgn,key,pos,active,edges,level,cross,x1,x2,d,u,v;
  point:=[0,0];maximum:=0;ks:=[];vs:=[];
  for a in word do
   axis:=AbsInt(a);sgn:=SignInt(a);
   if axis<1 or axis>2 then Error("Bad word letter");fi;
   if sgn<0 then point[axis]:=point[axis]-1;fi;
   key:=[point[1],point[2],axis];pos:=Position(ks,key);
   if pos=fail then Add(ks,key);Add(vs,sgn);else vs[pos]:=vs[pos]+sgn;fi;
   if sgn>0 then point[axis]:=point[axis]+1;fi;
   if point[1]<=0 then Error("Not a strict bridge prefix");fi;
   maximum:=Maximum(maximum,point[1]);
  od;
  if point[1]<>maximum or maximum<1 then Error("Bridge endpoint");fi;
  active:=Filtered([1..Length(ks)],i->vs[i]<>0);
  edges:=SortedList(List(active,i->Concatenation(ks[i],[vs[i]])));
  for level in [0..maximum-1] do
   cross:=Filtered(edges,e->e[3]=1 and e[1]=level);
   if Sum(cross,e->e[4])<>1 then Error("Vertical flux");fi;
   if level=0 and cross<>[[0,0,1,1]] then Error("Initial edge");fi;
   if level>0 and Length(cross)=1 then Error("Not an atom");fi;
  od;
  u:=fail;v:=fail;d:=fail;
  if maximum>=3 then
   x1:=Minimum(List(Filtered(edges,e->e[3]=1 and e[1]=1),e->e[2]));
   x2:=Minimum(List(Filtered(edges,e->e[3]=1 and e[1]=2),e->e[2]));
   d:=x2-x1;u:=x1-d;v:=point[2]-x1-(maximum-1)*d;
  fi;
  return rec(height:=maximum,u:=u,v:=v,d:=d,edges:=edges,cost:=Length(word),
             vertical:=Number(word,a->AbsInt(a)=1));
 end;
 act:=function(word,left,right)
  if word[1]<>1 then Error("Initial a required");fi;
  return Concatenation([1],ListWithIdenticalEntries(AbsInt(left),2*SignInt(left)),
         word{[2..Length(word)]},ListWithIdenticalEntries(AbsInt(right),2*SignInt(right)));
 end;
 shear:=function(word,k)
  local positive,negative,out,a;
  positive:=ListWithIdenticalEntries(AbsInt(k),2*SignInt(k));negative:=-Reversed(positive);out:=[];
  for a in word do
   if a=1 then Add(out,1);Append(out,positive);
   elif a=-1 then Append(out,negative);Add(out,-1);else Add(out,a);fi;
  od;
  return out;
 end;
 normal:=function(word)
  local d,n;
  d:=compute(word);if d.height<3 then Error("Two internal levels required");fi;
  n:=compute(act(shear(word,-d.d),-d.u,-d.v));
  if [n.height,n.u,n.v,n.d]<>[d.height,0,0,0] then Error("Normalization coordinates");fi;
  return [n.height,n.edges];
 end;
 words:=G9AtomWords;data:=List(words,compute);
 if Length(words)<>G9ShearTails.original_seed_count or
    Length(words)<>G9TwoEnded.original_atoms then Error("Seed binding");fi;
 excluded:=List([1,2],h->[h,Number(data,r->r.height=h)]);
 if excluded<>G9ShearTails.excluded_height_counts then Error("Excluded heights");fi;
 keys:=[];seen:=[];groups:=List(words,w->0);controlCount:=0;compositionCount:=0;
 termKeys:=[];values:=[];
 for g in [1..Length(G9ShearTails.orbit_records)] do
  row:=G9ShearTails.orbit_records[g];Add(keys,[row.height,row.canonical_flow]);
  for p in row.points do
   index:=p[1]+1;r:=data[index];Add(seen,index);groups[index]:=g;
   if [index-1,r.u,r.v,r.d,r.cost,r.vertical]<>p or r.height<>row.height or
      normal(words[index])<>[row.height,row.canonical_flow] then Error("Seed normalization");fi;
  od;
  low:=Minimum(List(row.points,p->p[4]));high:=Maximum(List(row.points,p->p[4]));
  if row.d_interval<>[low,high] or row.occupied_d<>Set(List(row.points,p->p[4])) then
   Error("Occupied shear interval");fi;
  if List(row.tails,t->t.sign)<>[1,-1] then Error("Both disjoint tails required");fi;
  for tail in row.tails do
   sign:=tail.sign;if sign=1 then boundary:=high+1;else boundary:=low-1;fi;
   choices:=List(row.points,p->[p[5]+p[6]*AbsInt(boundary-p[4]),p[6],p[1],boundary-p[4]]);
   best:=Minimum(choices);
   if [tail.first_cost,tail.vertical_letters,tail.input_index,tail.start_shear]<>best or
      tail.start_shear*sign<=0 then Error("Tail cost/seed choice");fi;
   e:=[tail.vertical_letters,tail.first_cost];pos:=Position(termKeys,e);
   if pos=fail then Add(termKeys,e);Add(values,1);else values[pos]:=values[pos]+1;fi;
   index:=tail.input_index+1;r:=data[index];
   for n in [0,1,3] do
    k:=tail.start_shear+sign*n;base:=shear(words[index],k);
    for pair in [[0,0],[-2,1],[1,-2]] do
     w:=act(base,pair[1],pair[2]);other:=compute(w);
     if [other.height,other.u,other.v,other.d,other.cost]<>
        [row.height,r.u+pair[1],r.v+pair[2],boundary+sign*n,
         tail.first_cost+tail.vertical_letters*n+Sum(pair,AbsInt)] or
        normal(w)<>[row.height,row.canonical_flow] or
        compute(shear(act(words[index],pair[1],pair[2]),k)).edges<>other.edges then
      Error("Tail group/coordinate/cost/commutation control");fi;
     controlCount:=controlCount+1;
    od;
   od;
  od;
  w:=words[row.points[1][1]+1];
  if compute(shear(shear(w,2),-3)).edges<>compute(shear(w,-1)).edges or
     compute(shear(shear(w,1),-1)).edges<>compute(w).edges then Error("Shear action");fi;
  compositionCount:=compositionCount+2;
 od;
 if SortedList(seen)<>Filtered([1..Length(data)],i->data[i].height>=3) or
    Length(Set(keys))<>Length(keys) or Length(seen)<>G9ShearTails.covered_seeds or
    Length(keys)<>G9ShearTails.shear_orbits then Error("Complete distinct shear partition");fi;
 assignments:=[];
 for oi in [1..Length(G9TwoEnded.orbit_records)] do
  old:=G9TwoEnded.orbit_records[oi];
  if old.height>=3 then
   first:=old.points[1][4]+1;g:=groups[first];delta:=data[first].d;
   for p in old.points do
    index:=p[4]+1;
    if groups[index]<>g or data[index].d<>delta then Error("Old entire boundary orbit");fi;
   od;
   Add(assignments,[oi-1,g-1,delta]);
  fi;
 od;
 if assignments<>G9ShearTails.old_orbit_assignments or
    Length(assignments)<>G9ShearTails.covered_old_orbits or
    Length(Set(List(assignments,p->p{[2,3]})))<>Length(assignments) then Error("Old alphabet coverage");fi;
 for g in [1..Length(keys)] do
  if Set(List(Filtered(assignments,p->p[2]=g-1),p->p[3]))<>
     G9ShearTails.orbit_records[g].occupied_d then Error("Missing old shear coordinate");fi;
 od;
 terms:=SortedList(List([1..Length(termKeys)],i->Concatenation(termKeys[i],[values[i]])));
 if terms<>G9ShearTails.additional_terms or
    G9ShearTails.old_rational_numerator<>G9TwoEnded.rational_numerator then Error("Rational series binding");fi;
 counts:=[];
 for degree in [0..40] do
  expected:=0;
  for term in terms do
   if degree>=term[2] then
    for n in [0..QuoInt(degree-term[2],term[1])] do
     horizontal:=degree-term[2]-n*term[1];
     if horizontal=0 then expected:=expected+term[3];
     else expected:=expected+4*horizontal*term[3];fi;
    od;
   fi;
  od;
  Add(counts,expected);
 od;
 if counts<>G9ShearTails.additional_counts_through_40 or counts{[1..15]}<>List([1..15],i->0) then
  Error("Additional series coefficients");fi;
 evaluate:=function(t)
  return Sum([1..Length(G9TwoEnded.rational_numerator)],i->G9TwoEnded.rational_numerator[i]*t^(i-1))/(1-t)^2
   +((1+t)/(1-t))^2*Sum(terms,p->p[3]*t^p[2]/(1-t^p[1]));
 end;
 lowerValue:=evaluate(G9ShearTails.denominator/G9ShearTails.lower_numerator);
 upperValue:=evaluate(G9ShearTails.denominator/G9ShearTails.root_upper_numerator);
 if lowerValue<1 or upperValue>=1 or G9ShearTails.root_upper_numerator<>G9ShearTails.lower_numerator+1 or
    G9ShearTails.lower_numerator<=G9TwoEnded.lower_numerator then Error("New exact lower bound");fi;
 if [controlCount,compositionCount]<>[G9ShearTails.checks.tail_boundary_controls,G9ShearTails.checks.shear_compositions] then
  Error("Control coverage");fi;
 Print("SHEAR_ORBITS=",Length(keys)," SEEDS=",Length(seen)," OLD_ORBITS=",Length(assignments),
       " TAIL_CONTROLS=",controlCount," COMPOSITION_CONTROLS=",compositionCount,"\n");
 Print("ADDITIONAL_TERMS=",terms,"\n");
 Print("LOWER=",G9ShearTails.lower_numerator,"/",G9ShearTails.denominator,
       " ROOT_UPPER=",G9ShearTails.root_upper_numerator,"/",G9ShearTails.denominator,"\n");
 Print("PASS native GAP G9 disjoint shear tails\n");
end)();
QUIT;
