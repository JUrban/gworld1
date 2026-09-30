# Reconstruct flows, disjoint two-ended orbits, representatives and rational GF.
# This checker does not invoke Python or perform a larger bridge enumeration.
Read("research/certificates/G9-bridge-atoms/fixtures.g");
G9OriginalWords:=G9AtomWords;
Read("research/certificates/G9-two-ended-completion-v1/fixtures.g");
G9OriginalTwoEnded:=G9TwoEnded;
Read("research/certificates/G9-steiner-seeds-v1/fixtures.g");
Read("research/certificates/G9-steiner-completion-v1/fixtures.g");
(function()
    local compute,act,envelope,checktarget,words,data,record,d,point,index,
          seen,corekeys,centers,strips,quadrants,numerator,counts,degree,
          xmin,xmax,zmin,zmax,x,z,value,selected,other,base,k,ell,
          costs,row,i,j,boundary,item,distance,cornerX,cornerZ,distances,
          orbitChecks,centralChecks,stripChecks,quadrantChecks,actionChecks,
          oneChecks,evaluate,lowerValue,upperValue,expected,zero,replacement,prior,oldData,oldWord,replacementChecks;
    compute:=function(word)
        local p,maximum,ks,vs,a,axis,sign,key,pos,active,edges,core,h,cross,x;
        p:=[0,0];maximum:=0;ks:=[];vs:=[];
        for a in word do
            axis:=AbsInt(a);sign:=SignInt(a);
            if sign<0 then p[axis]:=p[axis]-1;fi;
            key:=[p[1],p[2],axis];pos:=Position(ks,key);
            if pos=fail then Add(ks,key);Add(vs,sign);else vs[pos]:=vs[pos]+sign;fi;
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
            if h=0 and cross<>[[0,0,1,1]] then Error("Initial vertical edge");fi;
            if h>0 and Length(cross)=1 then Error("Not an atom");fi;
        od;
        if maximum=1 then x:=0;core:=[];
        else
            cross:=Filtered(edges,e->e[3]=1 and e[1]=1);
            x:=Minimum(List(cross,e->e[2]));
            core:=Filtered(edges,e->not (e[3]=1 and e[1]=0)
                              and not (e[3]=2 and e[1] in [1,maximum]));
            core:=List(core,e->[e[1],e[2]-x,e[3],e[4]]);
        fi;
        return rec(height:=maximum,y:=p[2],x:=x,z:=p[2]-x,
                   cost:=Length(word),core:=core,edges:=edges);
    end;
    act:=function(word,k,ell)
        if word[1]<>1 then Error("Initial a required");fi;
        return Concatenation([1],ListWithIdenticalEntries(AbsInt(k),2*SignInt(k)),
            word{[2..Length(word)]},ListWithIdenticalEntries(AbsInt(ell),2*SignInt(ell)));
    end;
    envelope:=function(record,x,z)
        return Minimum(List(record.points,p->[p[3]+AbsInt(x-p[1])+AbsInt(z-p[2]),p[4]+1]));
    end;
    checktarget:=function(record,x,z,expected)
        local choice,d,w,other;
        choice:=envelope(record,x,z);
        if choice[1]<>expected then Error("Exterior envelope formula");fi;
        d:=data[choice[2]];
        w:=act(words[choice[2]],x-d.x,z-d.z);other:=compute(w);
        if Length(w)<>expected or [other.height,other.core,other.x,other.z]<>
           [record.height,record.core,x,z] then Error("Exterior atom representative");fi;
    end;
    words:=G9AtomWords;data:=List(words,compute);
    if Length(data)<>G9TwoEnded.original_atoms then Error("Atom input count");fi;
    if words{[1..Length(G9OriginalWords)]}<>G9OriginalWords then Error("Original seed prefix changed");fi;
    replacementChecks:=0;
    for replacement in G9ShortenedSeedRecords do
        prior:=G9OriginalTwoEnded.orbit_records[replacement.orbit_index+1];
        if replacement.original_input<>prior.chosen_indices[replacement.x-prior.rectangle[1]+1]
           [replacement.z-prior.rectangle[3]+1] then Error("Original central representative binding");fi;
        oldData:=data[replacement.original_input+1];
        oldWord:=act(G9OriginalWords[replacement.original_input+1],replacement.x-oldData.x,replacement.z-oldData.z);
        other:=compute(oldWord);d:=data[replacement.new_input_index+1];
        if other.edges<>d.edges or Length(oldWord)<>replacement.original_cost or
           d.cost<>replacement.shortened_cost or d.cost>=Length(oldWord) or d.cost<=14 or
           [d.height,d.core,d.x,d.z]<>[prior.height,prior.core,replacement.x,replacement.z] or
           words[replacement.new_input_index+1]<>replacement.word then Error("Shortened seed equality");fi;
        replacementChecks:=replacementChecks+1;
    od;
    if List(G9ShortenedSeedRecords,r->r.new_input_index+1)<>
       [Length(G9OriginalWords)+1..Length(words)] then Error("Unverified new seed");fi;
    Print("SHORTENED_REPRESENTATIVES=",replacementChecks,"\n");
    degree:=Length(G9TwoEnded.central_coefficients)-1;
    centers:=List([0..degree],i->0);strips:=ShallowCopy(centers);quadrants:=ShallowCopy(centers);
    centers[2]:=1;strips[3]:=2;
    seen:=[];corekeys:=[];orbitChecks:=0;centralChecks:=0;
    stripChecks:=0;quadrantChecks:=0;actionChecks:=0;oneChecks:=0;
    if Length(Set(List(G9TwoEnded.height_one_points,p->p[1])))<>
       Length(G9TwoEnded.height_one_points) then Error("Height-one duplicate");fi;
    zero:=false;
    for point in G9TwoEnded.height_one_points do
        index:=point[3]+1;d:=data[index];Add(seen,index);
        other:=compute(Concatenation([1],ListWithIdenticalEntries(AbsInt(d.y),2*SignInt(d.y))));
        if d.height<>1 or [d.y,d.cost]<>point{[1,2]} or d.cost<>1+AbsInt(d.y) or
           other.edges<>d.edges then Error("Height-one orbit");fi;
        if d.y=0 then zero:=true;fi;
        oneChecks:=oneChecks+1;
    od;
    if not zero then Error("Missing height-one seed");fi;
    for record in G9TwoEnded.orbit_records do
        Add(corekeys,[record.height,record.core]);
        if Length(Set(List(record.points,p->p{[1,2]})))<>Length(record.points) then
            Error("Repeated orbit coordinate");fi;
        base:=record.points[1][4]+1;
        for point in record.points do
            index:=point[4]+1;d:=data[index];Add(seen,index);
            if [d.x,d.z,d.cost]<>point{[1,2,3]} or d.height<>record.height or
               d.core<>record.core or d.height<2 then Error("Original orbit binding");fi;
            other:=compute(act(words[base],d.x-data[base].x,d.z-data[base].z));
            if other.edges<>d.edges then Error("Full-flow orbit equality");fi;
            orbitChecks:=orbitChecks+1;
        od;
        if compute(act(act(words[base],-2,3),1,-2)).edges<>
           compute(act(words[base],-1,1)).edges then Error("Action composition");fi;
        actionChecks:=actionChecks+1;
        xmin:=Minimum(List(record.points,p->p[1]));xmax:=Maximum(List(record.points,p->p[1]));
        zmin:=Minimum(List(record.points,p->p[2]));zmax:=Maximum(List(record.points,p->p[2]));
        if record.rectangle<>[xmin,xmax,zmin,zmax] then Error("Bounding rectangle");fi;
        costs:=[];
        for x in [xmin..xmax] do
            row:=[];
            for z in [zmin..zmax] do
                value:=envelope(record,x,z)[1];Add(row,value);centers[value+1]:=centers[value+1]+1;
                selected:=record.chosen_indices[x-xmin+1][z-zmin+1]+1;
                if not selected in List(record.points,p->p[4]+1) then Error("Unknown chosen input");fi;
                other:=compute(act(words[selected],x-data[selected].x,z-data[selected].z));
                if [other.height,other.core,other.x,other.z,other.cost]<>
                   [record.height,record.core,x,z,value] then Error("Central representative");fi;
                centralChecks:=centralChecks+1;
            od;
            Add(costs,row);
        od;
        if costs<>record.costs then Error("Central cost envelope");fi;
        for point in record.points do
            if costs[point[1]-xmin+1][point[2]-zmin+1]>point[3] then Error("Old cost increased");fi;
        od;
        boundary:=Concatenation(List([zmin..zmax],z->[xmin,z,-1,0]),
                    List([zmin..zmax],z->[xmax,z,1,0]),
                    List([xmin..xmax],x->[x,zmin,0,-1]),
                    List([xmin..xmax],x->[x,zmax,0,1]));
        for item in boundary do
            x:=item[1];z:=item[2];value:=costs[x-xmin+1][z-zmin+1];
            strips[value+2]:=strips[value+2]+1;
            for distance in [1,3] do
                checktarget(record,x+distance*item[3],z+distance*item[4],value+distance);
                stripChecks:=stripChecks+1;
            od;
        od;
        for cornerX in [[xmin,-1],[xmax,1]] do
            for cornerZ in [[zmin,-1],[zmax,1]] do
                x:=cornerX[1];z:=cornerZ[1];value:=costs[x-xmin+1][z-zmin+1];
                quadrants[value+3]:=quadrants[value+3]+1;
                for distances in [[1,1],[2,3]] do
                    checktarget(record,x+distances[1]*cornerX[2],z+distances[2]*cornerZ[2],value+Sum(distances));
                    quadrantChecks:=quadrantChecks+1;
                od;
            od;
        od;
    od;
    if SortedList(seen)<>[1..Length(words)] or Length(Set(corekeys))<>Length(corekeys) or
       Length(corekeys)<>G9TwoEnded.rank_two_orbits then Error("Complete disjoint orbit grouping");fi;
    if centers<>G9TwoEnded.central_coefficients or strips<>G9TwoEnded.strip_coefficients or
       quadrants<>G9TwoEnded.quadrant_coefficients then Error("Rational coefficients");fi;
    numerator:=[];counts:=[];
    for i in [0..degree] do
        value:=centers[i+1]+strips[i+1]+quadrants[i+1];
        if i>0 then value:=value-2*centers[i]-strips[i];fi;
        if i>1 then value:=value+centers[i-1];fi;
        Add(numerator,value);
        Add(counts,centers[i+1]+Sum([0..i],j->strips[j+1]+(i-j+1)*quadrants[j+1]));
    od;
    if numerator<>G9TwoEnded.rational_numerator or counts<>G9TwoEnded.extended_initial_counts or
       counts{[1..Length(G9AtomCounts)]}<>G9AtomCounts or
       G9AtomCounts<>G9TwoEnded.original_cost_counts then Error("Series identity and original counts");fi;
    evaluate:=function(t)
        return Sum([0..degree],i->centers[i+1]*t^i)+Sum([0..degree],i->strips[i+1]*t^i)/(1-t)
            +Sum([0..degree],i->quadrants[i+1]*t^i)/(1-t)^2;
    end;
    lowerValue:=evaluate(G9TwoEnded.denominator/G9TwoEnded.lower_numerator);
    upperValue:=evaluate(G9TwoEnded.denominator/G9TwoEnded.root_upper_numerator);
    if lowerValue<1 or upperValue>=1 or
       G9TwoEnded.root_upper_numerator<>G9TwoEnded.lower_numerator+1 then Error("Rational root interval");fi;
    expected:=G9TwoEnded.checks;
    if [orbitChecks,centralChecks,stripChecks,quadrantChecks,actionChecks]<>
       [expected.original_flow_equalities,expected.central_representatives,
        expected.strip_controls,expected.quadrant_controls,expected.action_compositions] then Error("Check coverage");fi;
    Print("ORIGINAL_ATOMS=",Length(words)," HEIGHT_ONE=",oneChecks," TWO_ENDED_ORBITS=",Length(corekeys),
          " ORBIT_EQUALITIES=",orbitChecks," CENTRAL_ATOMS=",centralChecks,
          " STRIP_CONTROLS=",stripChecks," QUADRANT_CONTROLS=",quadrantChecks,
          " ACTION_CONTROLS=",actionChecks,"\n");
    Print("lower=",G9TwoEnded.lower_numerator,"/",G9TwoEnded.denominator,
          " alphabet_root_below=",G9TwoEnded.root_upper_numerator,"/",G9TwoEnded.denominator,"\n");
    Print("PASS independent GAP G9 Steiner atom completion\n");
end)();
QUIT;
