# Independent native Laurent-polynomial Magnus check and flow decoder.
Read("research/certificates/G9-flow-unfolding/fixtures.g");;
G9Fail:=function(s) Print("FAIL ",s,"\n");FORCE_QUIT_GAP(1);end;;
G9Bit:=function(b) if b then return 1;else return 0;fi;end;;
G9Vars:=function(r) return List([1..r],i->Indeterminate(Rationals,i));end;;
G9Monomial:=function(t,v) return Product([1..Length(t)],i->t[i]^v[i]);end;;
G9Magnus:=function(t,w)
    local row,s,j,m;
    row:=Concatenation([One(t[1])],List(t,x->Zero(x)));
    for s in w do
        j:=AbsInt(s);
        if s>0 then
            row[j+1]:=row[j+1]+row[1];row[1]:=row[1]*t[j];
        else
            row[1]:=row[1]/t[j];row[j+1]:=row[j+1]-row[1];
        fi;
    od;
    return row;
end;;
G9FlowPolynomial:=function(t,edges)
    local result,e;
    result:=List(t,x->Zero(x));
    for e in edges do result[e[2]+1]:=result[e[2]+1]+e[3]*G9Monomial(t,e[1]);od;
    return result;
end;;
G9Heights:=function(w)
    local h,s;h:=[0];
    for s in w do Add(h,Last(h)+G9Bit(AbsInt(s)=1)*SignInt(s));od;
    return h;
end;;
G9Endpoint:=function(rank,edges,start)
    local vertices,values,add,e,q,nz;
    vertices:=[];values:=[];
    add:=function(v,c)
        local i;i:=Position(vertices,v);
        if i=fail then Add(vertices,ShallowCopy(v));Add(values,c);else values[i]:=values[i]+c;fi;
    end;
    for e in edges do
        add(e[1],-e[3]);q:=ShallowCopy(e[1]);q[e[2]+1]:=q[e[2]+1]+1;add(q,e[3]);
    od;
    add(start,1);nz:=Filtered([1..Length(values)],i->values[i]<>0);
    if Length(nz)<>1 or values[nz[1]]<>1 then G9Fail("flow boundary");fi;
    return vertices[nz[1]];
end;;
G9Decode:=function(t,edges,spans)
    local rank,oldstart,newstart,lo,hi,sign,result,span,chunk,finish,F,localF,
          subs,j,delta,e,height;
    rank:=Length(t);oldstart:=List(t,x->0);newstart:=ShallowCopy(oldstart);
    lo:=0;sign:=1;result:=List(t,x->Zero(x));
    for span in spans do
        hi:=lo+span;
        chunk:=Filtered(edges,e->lo<e[1][1]+G9Bit(e[2]=0) and e[1][1]+G9Bit(e[2]=0)<=hi);
        finish:=G9Endpoint(rank,chunk,newstart);
        if finish[1]<>hi then G9Fail("wrong chunk endpoint");fi;
        F:=G9FlowPolynomial(t,chunk);
        localF:=List(F,x->x/G9Monomial(t,newstart));
        if sign=-1 then
            subs:=ShallowCopy(t);subs[1]:=t[1]^-1;
            localF:=List(localF,x->Value(x,t,subs));
            localF[1]:=-localF[1]/t[1];
        fi;
        for j in [1..rank] do result[j]:=result[j]+G9Monomial(t,oldstart)*localF[j];od;
        delta:=finish-newstart;delta[1]:=sign*delta[1];oldstart:=oldstart+delta;
        newstart:=finish;lo:=hi;sign:=-sign;
    od;
    if ForAny(edges,e->e[1][1]+G9Bit(e[2]=0)<=0 or e[1][1]+G9Bit(e[2]=0)>lo) then G9Fail("stray flow edge");fi;
    return result;
end;;
G9Main:=function()
    local G9Balls,G9Bounds,G9Checked,G9Counts,G9Degree,G9H,G9Height,G9Images,G9J,G9Left,G9Letters,G9M,G9N,G9Next,G9P,G9Product,G9Products,G9Q,G9Rank,G9Right,G9Rows,G9S,G9Sizes,G9T,G9Test,G9U,G9W,G9Record,G9Spec,G9Depth,G9Row,G9Image;
G9Checked:=0;;
for G9Record in G9UnfoldingFixtures do
    G9Rank:=G9Record[1];;G9T:=G9Vars(G9Rank);;G9W:=G9Record[2];;G9U:=G9Record[3];;G9S:=G9Record[4];;
    G9H:=G9Heights(G9W);;G9J:=G9Heights(G9U);;
    if Length(G9W)<>Length(G9U) or Minimum(G9H{[2..Length(G9H)]})<=0 or
       Minimum(G9J{[2..Length(G9J)]})<=0 or Maximum(G9J)<>Last(G9J) or Sum(G9S)<>Last(G9J) or
       ForAny([1..Length(G9S)-1],i->G9S[i]<=G9S[i+1]) then G9Fail("halfspace/bridge geometry");fi;
    G9M:=G9Magnus(G9T,G9W);;G9N:=G9Magnus(G9T,G9U);;
    if G9M{[2..G9Rank+1]}<>G9FlowPolynomial(G9T,G9Record[5]) or
       G9N{[2..G9Rank+1]}<>G9FlowPolynomial(G9T,G9Record[6]) then G9Fail("native Magnus versus supplied flow");fi;
    if G9Decode(G9T,G9Record[6],G9S)<>G9M{[2..G9Rank+1]} then G9Fail("independent flow-only decoder");fi;
    G9Checked:=G9Checked+1;;
od;
G9Products:=0;;
for G9Record in G9ConcatenationFixtures do
    G9Rank:=G9Record[1];;G9Height:=G9Record[2];;G9T:=G9Vars(G9Rank);;
    G9Left:=G9Magnus(G9T,G9Record[3]);;G9Right:=G9Magnus(G9T,G9Record[4]);;
    G9Product:=G9Magnus(G9T,Concatenation(G9Record[3],G9Record[4]));;
    for G9W in G9Record{[3,4]} do
        G9H:=G9Heights(G9W);;
        if Minimum(G9H{[2..Length(G9H)]})<=0 or Maximum(G9H)<>G9Height or Last(G9H)<>G9Height then G9Fail("code geometry");fi;
    od;
    if G9Product[1]<>G9Left[1]*G9Right[1] or
       G9Product{[2..G9Rank+1]}<>G9Left{[2..G9Rank+1]}+G9Left[1]*G9Right{[2..G9Rank+1]} then G9Fail("Magnus multiplication");fi;
    G9Products:=G9Products+1;;
od;
G9Bounds:=0;;
for G9Record in G9CodeBounds do
    G9P:=G9Record[3];;G9Q:=G9Record[4];;G9Counts:=G9Record[5];;G9Degree:=Maximum(List(G9Counts,p->p[1]));;
    G9Test:=p->Sum(G9Counts,c->c[2]*G9Q^c[1]*p^(G9Degree-c[1]))-p^G9Degree;;
    if G9Test(G9P)<0 or G9Test(G9P+1)>=0 then G9Fail("rational root bound");fi;
    G9Bounds:=G9Bounds+1;;
od;
G9T:=G9Vars(2);;
if G9Magnus(G9T,G9ZeroFlowRelation)<>[One(G9T[1]),Zero(G9T[1]),Zero(G9T[1])] then G9Fail("metabelian relation control");fi;
# Independent exact balls, with native Laurent entries, through first collisions.
G9Balls:=[];;
for G9Spec in [[2,8,[1,5,17,53,161,485,1457,4345,12893]],[3,4,[1,7,37,187,937]]] do
    G9Rank:=G9Spec[1];;G9T:=G9Vars(G9Rank);;G9Rows:=[G9Magnus(G9T,[])];;G9Sizes:=[1];;
    G9Letters:=Concatenation([1..G9Rank],[-G9Rank..-1]);;
    G9Images:=List(G9Letters,s->G9Magnus(G9T,[s]));;
    for G9Depth in [1..G9Spec[2]] do
        G9Next:=ShallowCopy(G9Rows);;
        for G9Row in G9Rows do
            for G9Image in G9Images do
                Add(G9Next,Concatenation([G9Row[1]*G9Image[1]],G9Row{[2..G9Rank+1]}+G9Row[1]*G9Image{[2..G9Rank+1]}));
            od;
        od;
        G9Rows:=Set(G9Next);;Add(G9Sizes,Length(G9Rows));
    od;
    if G9Sizes<>G9Spec[3] then G9Fail("independent ball enumeration");fi;
    Add(G9Balls,[G9Rank,G9Sizes]);
od;
Print("unfoldings=",G9Checked," products=",G9Products," rational_bounds=",G9Bounds," balls=",G9Balls,"\n");
Print("PASS G9 FLOW UNFOLDING GAP\n");
end;;
G9Main();;
QUIT;
