# Verify every listed atom using native Magnus Laurent-polynomial entries.
Read("research/certificates/G9-bridge-atoms/fixtures.g");;
G9AFail:=function(s) Print("FAIL ",s,"\n");FORCE_QUIT_GAP(1);end;;
G9ACheck:=function()
    local t,rows,counts,w,p,maximum,keys,values,s,j,sgn,key,i,row,h,
          active,crossing,total,flowpoly,mon,q,degree,test,lengths;
    t:=List([1,2],i->Indeterminate(Rationals,i));rows:=[];
    counts:=List(G9AtomCounts,x->0);
    for w in G9AtomWords do
        p:=[0,0];maximum:=0;keys:=[];values:=[];
        row:=[One(t[1]),Zero(t[1]),Zero(t[1])];
        for s in w do
            j:=AbsInt(s);sgn:=SignInt(s);
            if s<0 then p[j]:=p[j]-1;fi;
            key:=[p[1],p[2],j];i:=Position(keys,key);
            if i=fail then Add(keys,key);Add(values,sgn);else values[i]:=values[i]+sgn;fi;
            if s>0 then p[j]:=p[j]+1;fi;
            if p[1]<=0 then G9AFail("not strict halfspace");fi;
            maximum:=Maximum(maximum,p[1]);
            if s>0 then row[j+1]:=row[j+1]+row[1];row[1]:=row[1]*t[j];
            else row[1]:=row[1]/t[j];row[j+1]:=row[j+1]-row[1];fi;
        od;
        if p[1]<>maximum then G9AFail("not a bridge");fi;
        active:=Filtered([1..Length(keys)],i->values[i]<>0);
        flowpoly:=[Zero(t[1]),Zero(t[1])];
        for i in active do
            key:=keys[i];mon:=values[i]*t[1]^key[1]*t[2]^key[2];
            flowpoly[key[3]]:=flowpoly[key[3]]+mon;
        od;
        if row{[2,3]}<>flowpoly or row[1]<>t[1]^p[1]*t[2]^p[2] then G9AFail("native Magnus disagreement");fi;
        for h in [0..maximum-1] do
            crossing:=Filtered(active,i->keys[i][3]=1 and keys[i][1]=h);
            if Sum(crossing,i->values[i])<>1 then G9AFail("net flow through level");fi;
            if h>0 and Length(crossing)=1 then G9AFail("listed word is decomposable");fi;
        od;
        Add(rows,row);counts[Length(w)+1]:=counts[Length(w)+1]+1;
    od;
    if Length(Set(rows))<>Length(rows) then G9AFail("duplicate metabelian elements");fi;
    if counts<>G9AtomCounts then G9AFail("count vector");fi;
    degree:=Length(counts)-1;q:=G9AtomLower[2];
    test:=x->Sum([1..degree],l->counts[l+1]*q^l*x^(degree-l))-x^degree;
    if test(G9AtomLower[1])<0 or test(G9AtomLower[1]+1)>=0 then G9AFail("rational root enclosure");fi;
    Print("distinct_native_Magnus_rows=",Length(rows)," verified_counts=",counts,"\n");
    Print("lower=",G9AtomLower[1],"/",G9AtomLower[2]," polynomial_root_below=",G9AtomLower[1]+1,"/",G9AtomLower[2],"\n");
    Print("PASS G9 BRIDGE ATOM GAP\n");
end;;
G9ACheck();;
QUIT;
