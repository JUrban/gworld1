# Independent GAP reconstruction and parsing of all actual TPTP inputs.
# Group axioms are checked as identities in a free group; no theorem-prover
# answer is trusted by this input audit.  Negative controls use GAP/nq.
LoadPackage("nq");;
F20EFail:=function(s) Print("FAIL F20 encoding: ",s,"\n");FORCE_QUIT_GAP(1);end;;
F20EMul:=function(a,b) return Concatenation("mul(",a,",",b,")");end;;
F20EComm:=function(a,b)
    return F20EMul(F20EMul(Concatenation("inv(",a,")"),Concatenation("inv(",b,")")),F20EMul(a,b));
end;;
F20EName:=function(i)
    local s;s:=String(i);while Length(s)<3 do s:=Concatenation("0",s);od;
    return Concatenation("c",s);
end;;
F20EExpect:=function(st,ch)
    if st.s[st.pos]<>ch then F20EFail("unexpected parse character");fi;
    st.pos:=st.pos+1;
end;;
F20EParse:=function(st,hall,gens)
    local start,t,a,b,i;
    start:=st.pos;
    while st.pos<=Length(st.s) and st.s[st.pos] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_" do
        st.pos:=st.pos+1;
    od;
    t:=st.s{[start..st.pos-1]};
    if t="mul" then
        F20EExpect(st,'(');a:=F20EParse(st,hall,gens);F20EExpect(st,',');
        b:=F20EParse(st,hall,gens);F20EExpect(st,')');return a*b;
    elif t="inv" then
        F20EExpect(st,'(');a:=F20EParse(st,hall,gens);F20EExpect(st,')');return a^-1;
    elif t="one" then return One(gens[1]);
    elif t="X" then return gens[3];
    elif t="Y" then return gens[4];
    elif t="Z" then return gens[5];
    elif Length(t)=4 and t[1]='c' then
        i:=Int(t{[2..4]});return hall[i].word;
    fi;
    F20EFail(Concatenation("unknown token ",t));
end;;
F20ETerm:=function(hall,weight,i)
    local p;
    if hall[i].weight<weight then return F20EName(i);fi;
    p:=hall[i].parents;
    return F20EComm(F20ETerm(hall,weight,p[1]),F20ETerm(hall,weight,p[2]));
end;;
F20EDir:="research/certificates/F20-equational/inputs-v1/";;
F20ETotal:=0;;F20EClauses:=0;;
for weight in [5,6] do
    F:=FreeGroup(5);;gens:=GeneratorsOfGroup(F);;
    hall:=[rec(weight:=1,parents:=[],word:=gens[1]),rec(weight:=1,parents:=[],word:=gens[2])];;
    for w in [2..weight+1] do
        old:=Length(hall);;
        for i in [1..old] do for j in [1..i-1] do
            if hall[i].weight+hall[j].weight=w and
               (Length(hall[i].parents)=0 or hall[i].parents[2]<=j) then
                Add(hall,rec(weight:=w,parents:=[i,j],word:=Comm(hall[i].word,hall[j].word)));
            fi;
        od;od;
    od;
    targets:=Filtered([1..Length(hall)],i->hall[i].weight=weight+1);;
    negative:=First([1..Length(hall)],i->hall[i].weight=weight-1);;
    if Length(targets)<>[9,18][weight-4] then F20EFail("target count");fi;
    # The selected negative is demonstrably nonidentity in an actual
    # class-(weight-1) nilpotent quotient which satisfies every killed relator.
    F2:=FreeGroup(2);;ng:=GeneratorsOfGroup(F2);;
    N:=NilpotentQuotient(F2,weight-1);;nn:=GeneratorsOfGroup(N);;
    mapN:=GroupHomomorphismByImages(F,N,gens,[nn[1],nn[2],One(N),One(N),One(N)]);;
    if Image(mapN,hall[negative].word)=One(N) then F20EFail("negative control vanished");fi;
    for i in Filtered([1..Length(hall)],i->hall[i].weight=weight) do
        if Image(mapN,hall[i].word)<>One(N) then F20EFail("nilpotent model relator");fi;
    od;
    for encoding in ["collect","inverse"] do
        for number in [1..Length(targets)+1] do
            if number<=Length(targets) then kind:="target";target:=targets[number];
            else kind:="negative-control";target:=negative;fi;
            num:=String(number);if Length(num)=1 then num:=Concatenation("0",num);fi;
            filename:=Concatenation(F20EDir,"w",String(weight),"-",encoding,"-",kind,"-",num,".p");;
            lines:=SplitString(StringFile(filename),"\n");;seen:=[];;
            for line in lines do
                if Length(line)=0 or line[1]='%' then continue;fi;
                first:=Position(line,',');;name:=line{[5..first-1]};;
                begin:=PositionSublist(line,",(");;body:=line{[begin+2..Length(line)-3]};;
                role:=line{[first+1..begin-1]};;
                st:=rec(s:=body,pos:=1);;left:=F20EParse(st,hall,gens);;
                neq:=false;;if st.s[st.pos]='!' then neq:=true;st.pos:=st.pos+1;fi;
                F20EExpect(st,'=');;right:=F20EParse(st,hall,gens);;
                if st.pos<>Length(body)+1 then F20EFail("trailing term text");fi;
                if name="goal" then
                    if not neq or role<>"negated_conjecture" then F20EFail("goal role");fi;
                    parents:=hall[target].parents;;a:=F20ETerm(hall,weight,parents[1]);;b:=F20ETerm(hall,weight,parents[2]);;
                    if encoding="collect" then expected:=Concatenation(F20EMul(a,b),"!=",F20EMul(b,a));
                    else expected:=Concatenation(F20ETerm(hall,weight,target),"!=one");fi;
                    if body<>expected then F20EFail("goal formula");fi;
                    if not (left^-1*right in [hall[target].word,hall[target].word^-1]) then
                        F20EFail("goal group interpretation");
                    fi;
                elif PositionSublist(name,"def_")=1 or PositionSublist(name,"rel_")=1 then
                    if neq or role<>"axiom" then F20EFail("presentation role");fi;
                    i:=Int(name{[5..Length(name)]});;h:=hall[i];;a:=F20ETerm(hall,weight,h.parents[1]);;b:=F20ETerm(hall,weight,h.parents[2]);;
                    if h.weight=weight then
                        if name{[1..4]}<>"rel_" then F20EFail("wrong killed weight");fi;
                        if encoding="collect" then expected:=Concatenation(F20EMul(a,b),"=",F20EMul(b,a));
                        else expected:=Concatenation(F20EComm(a,b),"=one");fi;
                        if not (left^-1*right in [h.word,h.word^-1]) then F20EFail("relator interpretation");fi;
                    elif h.weight>1 and h.weight<weight then
                        if name{[1..4]}<>"def_" or left<>right then F20EFail("bad definition");fi;
                        if encoding="collect" then expected:=Concatenation(F20EMul(a,b),"=",F20EMul(F20EMul(b,a),F20EName(i)));
                        else expected:=Concatenation(F20EName(i),"=",F20EComm(a,b));fi;
                    else F20EFail("unexpected presentation weight");fi;
                    if expected<>body then F20EFail("presentation formula");fi;
                else
                    if neq or role<>"axiom" or left<>right then F20EFail("false group identity");fi;
                    if not name in ["assoc","left_id","right_id","left_inv","right_inv","inv_inv","inv_prod","inv_one"] then
                        F20EFail("unrecognized extra axiom");
                    fi;
                fi;
                if name in seen then F20EFail("duplicate name");fi;Add(seen,name);
                F20EClauses:=F20EClauses+1;
            od;
            expectedNames:=Concatenation(["assoc","left_id","right_id","left_inv","right_inv","inv_inv","inv_prod","inv_one","goal"],
                List(Filtered([1..Length(hall)],i->hall[i].weight>1 and hall[i].weight<weight),i->Concatenation("def_",F20EName(i){[2..4]})),
                List(Filtered([1..Length(hall)],i->hall[i].weight=weight),i->Concatenation("rel_",F20EName(i){[2..4]})));;
            if Set(seen)<>Set(expectedNames) then F20EFail("missing axiom or relator");fi;
            F20ETotal:=F20ETotal+1;
        od;
    od;
od;
Print("PASS F20 independent TPTP input audit: ",F20ETotal," files, ",F20EClauses," clauses, two nilpotent negative models\n");
QUIT;
