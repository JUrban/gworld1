# Independent verification of rewriting relations and the finite upper bound.
# This does not require the generator's enumeration to be exhaustive.
Read("research/certificates/G9-forbidden-upper/fixtures.g");;
G9UFail:=function(s) Print("FAIL ",s,"\n");FORCE_QUIT_GAP(1);end;;
G9UCheck:=function()
    local t,magnus,shortlex,contains,patterns,states,prefix,w,rel,i,j,a,
          row,transitions,word,pos,k,v,av,p,q,checked;
    t:=List([1,2],i->Indeterminate(Rationals,i));
    magnus:=function(w)
        local out,s,j;
        out:=[One(t[1]),Zero(t[1]),Zero(t[1])];
        for s in w do
            if not s in [-2,-1,1,2] then G9UFail("invalid letter");fi;
            j:=AbsInt(s);
            if s>0 then out[j+1]:=out[j+1]+out[1];out[1]:=out[1]*t[j];
            else out[1]:=out[1]/t[j];out[j+1]:=out[j+1]-out[1];fi;
        od;
        return out;
    end;
    shortlex:=function(u,w)
        return Length(u)<Length(w) or (Length(u)=Length(w) and u<w);
    end;
    contains:=function(w,p)
        local i;
        if Length(w)<Length(p) then return false;fi;
        for i in [1..Length(w)-Length(p)+1] do
            if w{[i..i+Length(p)-1]}=p then return true;fi;
        od;
        return false;
    end;
    if G9UpperAlphabet<>[-2,-1,1,2] then G9UFail("alphabet order");fi;
    for rel in G9UpperRelations do
        if not shortlex(rel[2],rel[1]) then G9UFail("nondecreasing relation");fi;
        if magnus(rel[1])<>magnus(rel[2]) then G9UFail("false Magnus relation");fi;
    od;
    patterns:=Set(List(G9UpperRelations,r->r[1]));
    if Length(patterns)<>Length(G9UpperRelations) or [] in patterns then G9UFail("bad patterns");fi;
    states:=[[]];
    for w in patterns do
        for i in [1..Length(w)-1] do AddSet(states,w{[1..i]});od;
    od;
    Sort(states,shortlex);
    if states<>G9UpperStates then G9UFail("prefix state set");fi;
    if ForAny(states,w->ForAny(patterns,p->contains(w,p))) then G9UFail("unsafe state");fi;
    transitions:=[];
    for prefix in states do
        row:=[];
        for a in G9UpperAlphabet do
            word:=Concatenation(prefix,[a]);
            if ForAny(patterns,p->contains(word,p)) then Add(row,-1);
            else
                pos:=fail;
                for i in [1..Length(word)+1] do
                    w:=word{[i..Length(word)]};j:=Position(states,w);
                    if j<>fail then pos:=j-1;break;fi;
                od;
                if pos=fail then G9UFail("missing suffix state");fi;
                Add(row,pos);
            fi;
        od;
        Add(transitions,row);
    od;
    if transitions<>G9UpperTransitions then G9UFail("transition table");fi;
    v:=G9UpperVector;p:=G9UpperBound[1];q:=G9UpperBound[2];
    if Length(v)<>Length(states) or ForAny(v,x->not IsInt(x) or x<=0) or
       not IsInt(p) or not IsInt(q) or q<=0 or p<=q or p>=3*q then G9UFail("invalid comparison data");fi;
    av:=List(transitions,row->Sum(Filtered(row,j->j>=0),j->v[j+1]));
    if ForAny([1..Length(v)],i->q*av[i]>p*v[i]) then G9UFail("comparison inequality");fi;
    Print("native_relations=",Length(patterns)," states=",Length(states),
          " independently_reconstructed_transitions=",4*Length(states),"\n");
    Print("upper=",p,"/",q," positive_integer_inequalities=",Length(v),"\n");
    Print("PASS G9 FORBIDDEN UPPER GAP\n");
end;;
G9UCheck();;
QUIT;
