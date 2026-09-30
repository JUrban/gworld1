# Independently reconstruct finite orbit data and the infinite-tail polynomial.
# No larger bridge enumeration and no Python implementation are used.
Read("research/certificates/G9-bridge-atoms/fixtures.g");
Read("research/certificates/G9-horizontal-completion-v1/fixtures.g");
(function()
    local compute,appendpower,words,data,w,d,r,point,index,keys,seen,corekeys,
          centers,tails,numerator,counts,degree,low,high,costs,y,value,selected,
          i,j,base,delta,padded,other,orbitChecks,suffixChecks,centralChecks,
          evaluate,z,lowerValue,upperValue;
    compute:=function(word)
        local p,maximum,ks,vs,a,axis,sign,k,pos,active,edges,core,h,cross;
        p:=[0,0];maximum:=0;ks:=[];vs:=[];
        for a in word do
            axis:=AbsInt(a);sign:=SignInt(a);
            if sign<0 then p[axis]:=p[axis]-1;fi;
            k:=[p[1],p[2],axis];pos:=Position(ks,k);
            if pos=fail then Add(ks,k);Add(vs,sign);else vs[pos]:=vs[pos]+sign;fi;
            if sign>0 then p[axis]:=p[axis]+1;fi;
            if p[1]<=0 then Error("Not a strict halfspace word");fi;
            maximum:=Maximum(maximum,p[1]);
        od;
        if p[1]<>maximum or maximum<1 then Error("Not a bridge");fi;
        active:=Filtered([1..Length(ks)],i->vs[i]<>0);
        edges:=SortedList(List(active,i->Concatenation(ks[i],[vs[i]])));
        for h in [0..maximum-1] do
            cross:=Filtered(edges,e->e[3]=1 and e[1]=h);
            if Sum(cross,e->e[4])<>1 then Error("Bad vertical flux");fi;
            if h>0 and Length(cross)=1 then Error("Not an atom");fi;
        od;
        core:=Filtered(edges,e->e[3]<>2 or e[1]<>maximum);
        return rec(height=maximum,y=p[2],cost=Length(word),core=core,edges=edges);
    end;
    appendpower:=function(word,k)
        return Concatenation(word,ListWithIdenticalEntries(AbsInt(k),2*SignInt(k)));
    end;
    words:=G9AtomWords;data:=List(words,compute);
    if Length(data)<>G9Horizontal.original_atoms then Error("Atom input count");fi;
    degree:=Length(G9Horizontal.central_coefficients)-1;
    centers:=List([0..degree],i->0);tails:=ShallowCopy(centers);
    seen:=[];corekeys:=[];orbitChecks:=0;suffixChecks:=0;centralChecks:=0;
    for r in G9Horizontal.orbit_records do
        Add(corekeys,[r.height,r.core]);
        if Length(Set(List(r.points,p->p[1])))<>Length(r.points) then Error("Repeated endpoint");fi;
        base:=r.points[1][3]+1;
        for point in r.points do
            index:=point[3]+1;d:=data[index];Add(seen,index);
            if [d.y,d.cost]<>point{[1,2]} or d.height<>r.height or d.core<>r.core then
                Error("Original word orbit binding");fi;
            # Compare actual complete flows after adding the required horizontal suffix.
            other:=compute(appendpower(words[base],d.y-data[base].y));
            if other.edges<>d.edges then Error("Common core did not give asserted right power");fi;
            orbitChecks:=orbitChecks+1;
        od;
        low:=Minimum(List(r.points,p->p[1]));high:=Maximum(List(r.points,p->p[1]));
        if low<>r.low or high<>r.high then Error("Endpoint range");fi;
        costs:=[];
        for y in [low..high] do
            value:=Minimum(List(r.points,p->p[2]+AbsInt(y-p[1])));
            Add(costs,value);centers[value+1]:=centers[value+1]+1;
            selected:=r.chosen_indices[y-low+1]+1;
            if not selected in List(r.points,p->p[3]+1) then Error("Unbound representative");fi;
            padded:=appendpower(words[selected],y-data[selected].y);
            other:=compute(padded);
            if Length(padded)<>value or other.core<>r.core or other.height<>r.height or other.y<>y then
                Error("Central representative/atom");fi;
            centralChecks:=centralChecks+1;
        od;
        if costs<>r.costs or costs[1]+1<>r.left_tail_start or
           costs[Length(costs)]+1<>r.right_tail_start then Error("Envelope or tail start");fi;
        tails[r.left_tail_start+1]:=tails[r.left_tail_start+1]+1;
        tails[r.right_tail_start+1]:=tails[r.right_tail_start+1]+1;
        for point in r.points do
            if costs[point[1]-low+1]>point[2] then Error("Old letter lost at its old cost");fi;
        od;
        for y in [low-1,low-3,high+1,high+3] do
            if y<low then selected:=r.chosen_indices[1]+1;value:=costs[1]+low-y;
            else selected:=r.chosen_indices[Length(costs)]+1;value:=costs[Length(costs)]+y-high;fi;
            padded:=appendpower(words[selected],y-data[selected].y);other:=compute(padded);
            if Length(padded)<>value or other.core<>r.core or other.height<>r.height or other.y<>y then
                Error("Tail representative/atom");fi;
            suffixChecks:=suffixChecks+1;
        od;
    od;
    if SortedList(seen)<>[1..Length(words)] or Length(Set(corekeys))<>Length(corekeys) or
       Length(corekeys)<>G9Horizontal.distinct_orbits then Error("Complete disjoint orbit grouping");fi;
    if centers<>G9Horizontal.central_coefficients or tails<>G9Horizontal.tail_coefficients then
        Error("Rational generating function coefficients");fi;
    numerator:=[];counts:=[];
    for i in [0..degree] do
        value:=centers[i+1]+tails[i+1];if i>0 then value:=value-centers[i];fi;
        Add(numerator,value);Add(counts,centers[i+1]+Sum(tails{[1..i+1]}));
    od;
    if numerator<>G9Horizontal.rational_numerator or counts<>G9Horizontal.extended_initial_counts or
       counts{[1..Length(G9AtomCounts)]}<>G9AtomCounts or
       G9AtomCounts<>G9Horizontal.original_cost_counts then Error("Series identity or old counts");fi;
    evaluate:=z->Sum([0..degree],i->centers[i+1]*z^i)+Sum([0..degree],i->tails[i+1]*z^i)/(1-z);
    lowerValue:=evaluate(G9Horizontal.denominator/G9Horizontal.lower_numerator);
    upperValue:=evaluate(G9Horizontal.denominator/G9Horizontal.root_upper_numerator);
    if lowerValue<1 or upperValue>=1 or
       G9Horizontal.root_upper_numerator<>G9Horizontal.lower_numerator+1 then Error("Rational root bounds");fi;
    Print("ORIGINAL_ATOMS=",Length(words)," ORBITS=",Length(corekeys)," ORBIT_EQUALITIES=",orbitChecks,
          " CENTRAL_ATOMS=",centralChecks," TAIL_CONTROLS=",suffixChecks,"\n");
    Print("lower=",G9Horizontal.lower_numerator,"/",G9Horizontal.denominator,
          " alphabet_root_below=",G9Horizontal.root_upper_numerator,"/",G9Horizontal.denominator,"\n");
    Print("PASS independent GAP G9 horizontal atom completion\n");
end)();
QUIT;
