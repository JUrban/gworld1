# Independent GAP reconstruction of complete minimum Whitehead graphs.
# These checks do not establish the imported graded shortening theorem.
Read("research/certificates/F38-bounded/fixtures.g");;
F38BFail:=function(s) Print("FAIL ",s,"\n");FORCE_QUIT_GAP(1);end;;
F38BEval:=function(images,word)
    local out,x;
    out:=One(images[1]);
    for x in word do out:=out*images[AbsInt(x)]^SignInt(x);od;
    return out;
end;;
F38BClass:=function(word)
    local w,n;
    w:=LetterRepAssocWord(word);
    while Length(w)>1 and w[1]=-Last(w) do w:=w{[2..Length(w)-1]};od;
    n:=Length(w);if n=0 then return [];fi;
    return Minimum(List([0..n-1],i->Concatenation(w{[i+1..n]},w{[1..i]})));
end;;
F38BCompose:=function(f,g)
    return [List(g[1],w->F38BEval(f[1],LetterRepAssocWord(w))),
            List(f[2],w->F38BEval(g[2],LetterRepAssocWord(w)))];
end;;
F38BInverse:=function(f) return [f[2],f[1]];end;;
F38BCheckAuto:=function(f,gens)
    if F38BCompose(f,F38BInverse(f))<>[gens,gens] or
       F38BCompose(F38BInverse(f),f)<>[gens,gens] then
        F38BFail("bad inverse");
    fi;
end;;
F38BMoves:=function(rank,gens)
    local out,perm,signs,images,rev,i,x,a,A,alphabet;
    out:=[];
    for perm in PermutationsList([1..rank]) do
        for signs in Tuples([-1,1],rank) do
            images:=List([1..rank],i->gens[perm[i]]^signs[i]);rev:=[];
            for i in [1..rank] do rev[perm[i]]:=gens[i]^signs[i];od;
            AddSet(out,[images,rev]);
        od;
    od;
    alphabet:=Concatenation([-rank..-1],[1..rank]);
    for a in alphabet do
        for A in Combinations(Difference(alphabet,[a,-a])) do
            images:=[];rev:=[];
            for x in [1..rank] do
                if x=AbsInt(a) then images[x]:=gens[x];rev[x]:=gens[x];
                else
                    images[x]:=gens[x];rev[x]:=gens[x];
                    if -x in A then
                        images[x]:=gens[AbsInt(a)]^-SignInt(a)*images[x];
                        rev[x]:=gens[AbsInt(a)]^SignInt(a)*rev[x];
                    fi;
                    if x in A then
                        images[x]:=images[x]*gens[AbsInt(a)]^SignInt(a);
                        rev[x]:=rev[x]*gens[AbsInt(a)]^-SignInt(a);
                    fi;
                fi;
            od;
            AddSet(out,[images,rev]);
        od;
    od;
    RemoveSet(out,[gens,gens]);
    for images in out do F38BCheckAuto(images,gens);od;
    return out;
end;;
F38BGraph:=function(rank,fixed)
    local F,gens,moves,mu,u,changed,f,v,nodes,paths,i,j,step,loop,
          loops,edges,old;
    F:=FreeGroup(rank);gens:=GeneratorsOfGroup(F);moves:=F38BMoves(rank,gens);
    mu:=[gens,gens];u:=F38BClass(F38BEval(gens,fixed));changed:=true;
    while changed do
        changed:=false;
        for f in moves do
            v:=F38BClass(F38BEval(f[1],u));
            if Length(v)<Length(u) then
                u:=v;mu:=F38BCompose(f,mu);changed:=true;break;
            fi;
        od;
    od;
    nodes:=[u];paths:=[[gens,gens]];loops:=[];edges:=0;i:=1;
    while i<=Length(nodes) do
        for f in moves do
            v:=F38BClass(F38BEval(f[1],nodes[i]));
            if Length(v)<Length(u) then F38BFail("nonminimum root");fi;
            if Length(v)=Length(u) then
                edges:=edges+1;step:=F38BCompose(f,paths[i]);j:=Position(nodes,v);
                if j=fail then Add(nodes,v);Add(paths,step);j:=Length(nodes);fi;
                loop:=F38BCompose(F38BInverse(paths[j]),step);
                old:=F38BCompose(F38BInverse(mu),F38BCompose(loop,mu));
                if F38BClass(F38BEval(old[1],fixed))<>
                   F38BClass(F38BEval(gens,fixed)) then F38BFail("loop transport");fi;
                AddSet(loops,old[1]);
            fi;
        od;
        i:=i+1;
    od;
    return rec(gens:=gens,loops:=loops,vertices:=Length(nodes),edges:=edges,
               moves:=Length(moves));
end;;
F38BLift:=function(word,b,a)
    local start,state,x,valid;
    for start in [0,1] do
        state:=start;valid:=true;
        for x in word do
            if AbsInt(x)=b then
                if x>0 and state=0 then state:=1;
                elif x<0 and state=1 then state:=0;
                else valid:=false;break;fi;
            elif state=1 and AbsInt(x)<>a then valid:=false;break;
            fi;
        od;
        if valid and state=start then return true;fi;
    od;
    return false;
end;;
F38BRun:=function()
    local graphs,keys,row,key,index,graph,rank,F,gens,orbit,images,w,i,j,x,
          f,mat,finite,negative,transitions,nodes,edges,loops,
          b,a,n,values,power,growth,twists,ranktwo,A,B,C,ell,expr,word,length;
    graphs:=[];keys:=[];finite:=0;negative:=0;transitions:=0;
    nodes:=0;edges:=0;loops:=0;twists:=0;ranktwo:=0;
    for row in F38BoundedFixtures do
        rank:=row[1];
        if row[4]=1 then
            key:=[rank,row[2]];index:=Position(keys,key);
            if index=fail then
                graph:=F38BGraph(rank,row[2]);Add(keys,key);Add(graphs,graph);
                nodes:=nodes+graph.vertices;edges:=edges+graph.edges;
                loops:=loops+Length(graph.loops);
                Print("GRAPH rank=",rank," vertices=",graph.vertices,
                      " edges=",graph.edges," loop maps=",Length(graph.loops),"\n");
            else graph:=graphs[index];fi;
            gens:=graph.gens;orbit:=Set(row[5]);
            if not F38BClass(F38BEval(gens,row[3])) in orbit then F38BFail("missing initial class");fi;
            for w in orbit do
                if F38BClass(F38BEval(gens,w))<>w then F38BFail("noncanonical orbit");fi;
                for images in graph.loops do
                    if not F38BClass(F38BEval(images,w)) in orbit then
                        F38BFail("full stabilizer loop leaves finite orbit");
                    fi;
                    transitions:=transitions+1;
                od;
            od;
            finite:=finite+1;
        else
            F:=FreeGroup(rank);gens:=GeneratorsOfGroup(F);
            f:=List(row[5],part->List(part,w->F38BEval(gens,w)));
            F38BCheckAuto(f,gens);
            if F38BClass(F38BEval(f[1],row[2]))<>F38BClass(F38BEval(gens,row[2])) or
               F38BClass(F38BEval(f[1],row[3]))=F38BClass(F38BEval(gens,row[3])) then
                F38BFail("fixed/moved witness");
            fi;
            for i in [1..rank] do
                w:=LetterRepAssocWord(f[1][i]);
                for j in [1..rank] do
                    mat:=(Number(w,x->x=j)-Number(w,x->x=-j)) mod 3;
                    if (i=j and mat<>1) or (i<>j and mat<>0) then F38BFail("level three");fi;
                od;
            od;
            negative:=negative+1;
        fi;
    od;
    for row in F38FactorTwists do
        rank:=row[1];F:=FreeGroup(rank);gens:=GeneratorsOfGroup(F);
        w:=row[2];b:=row[3];a:=row[4];n:=row[5];values:=[];
        for power in [n,n+1] do
            images:=ShallowCopy(gens);images[b]:=gens[b]*gens[a]^power;
            Add(values,Length(F38BClass(F38BEval(images,w))));
        od;
        if values<>row[6] or values[2]-values[1]<>row[7] then F38BFail("Nielsen lengths");fi;
        if F38BLift(w,b,a)<>(row[7]=0) then F38BFail("zero-growth graph");fi;
        if (F38BLift(w,b,1) and F38BLift(w,b,2))<>ForAll(w,x->AbsInt(x)<>b) then
            F38BFail("two twists fail to exclude complementary letter");
        fi;
        twists:=twists+1;
    od;
    F:=FreeGroup(2);gens:=GeneratorsOfGroup(F);
    for row in F38RankTwo do
        f:=List(row[1],part->List(part,w->F38BEval(gens,w)));F38BCheckAuto(f,gens);
        A:=f[1][1];B:=f[1][2];C:=B*A*B^-1;ell:=Length(F38BClass(A));
        if Length(F38BClass(A*C^-1))<>4 or ell<>row[4] then F38BFail("commutator boundary");fi;
        expr:=row[2];word:=F38BEval([gens[1],gens[2]*gens[1]*gens[2]^-1],expr);
        if LetterRepAssocWord(word)<>row[3] then F38BFail("carrier expression");fi;
        length:=Length(F38BClass(F38BEval(f[1],row[3])));
        if length<>row[5] or length>3*Length(expr)*ell then F38BFail("rank-two bound");fi;
        ranktwo:=ranktwo+1;
    od;
    Print("PASS F38 BOUNDED GAP graphs=",Length(graphs)," nodes=",nodes,
          " edges=",edges," loop_maps=",loops," finite_orbits=",finite,
          " loop_orbit_transitions=",transitions," negative_witnesses=",negative,
          " factor_twists=",twists," rank_two_bounds=",ranktwo,"\n");
end;;
F38BRun();;
QUIT_GAP(0);
