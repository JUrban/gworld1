# Independent native word, morphism, determinant and span replay.
# Neither recompression nor the correctness of a full solution grammar is checked.
Read("research/certificates/F34-F38-language-interface-v1/equation-tuples.g");;
Read("research/certificates/F34-F38-language-interface-v1/language-cases.g");;
GWAssert:=function(ok,msg) if not ok then Error(msg); fi; end;;
GWInvert:=w->List(Reversed(w),a->-a);;
GWTokens:=function(tokens,values)
    local out,t;
    out:=[];
    for t in tokens do
        if t>0 then Append(out,values[t]); else Append(out,GWInvert(values[-t])); fi;
    od;
    return out;
end;;
GWWord:=function(gens,letters)
    local w,a;
    w:=One(gens[1]);
    for a in letters do w:=w*gens[AbsInt(a)]^SignInt(a); od;
    return w;
end;;
GWEquationCount:=0;; GWGroupCount:=0;; GWConstraintCount:=0;;
for recd in GWLanguageTuples do
    gens:=GeneratorsOfGroup(FreeGroup(recd.rank));;
    for i in [1..Length(recd.values)] do
        letters:=recd.values[i];;
        GWAssert(LetterRepAssocWord(GWWord(gens,letters))=letters,"not reduced");
        kind:=recd.constraints[i];;
        if kind="positive" then GWAssert(ForAll(letters,a->a>0),"not positive"); fi;
        if kind="cyclic" then
            GWAssert(IsEmpty(letters) or letters[1]<>-letters[Length(letters)],"not cyclic");
        fi;
        GWConstraintCount:=GWConstraintCount+1;
    od;
    for equation in recd.equations do
        GWAssert(GWTokens(equation[1],recd.values)=GWTokens(equation[2],recd.values),
                 "strict monoid equation failed");
        GWEquationCount:=GWEquationCount+1;
    od;
    for equation in recd.groups do
        GWAssert(GWWord(gens,GWTokens(equation[1],recd.values))=
                 GWWord(gens,recd.values[equation[2]]),"native original equation failed");
        GWGroupCount:=GWGroupCount+1;
    od;
od;
GWMonomial:=(x,e)->Product([1..Length(x)],i->x[i]^e[i]);;
GWPoly:=(c,x)->Sum(c.polynomial,t->t[1]*GWMonomial(x,t[2]));;
GWLift:=(c,x)->List(c.monomials,e->GWMonomial(x,e));;
GWApply:=(m,x)->List(m,row->row*x);;
GWSupport:=x->Filtered([1..Length(x)],i->x[i]<>0)-1;;
GWBlock:=function(c,q,s)
    local found;
    found:=Filtered(c.basis,b->b.state=q and b.support=s);
    GWAssert(Length(found)=1,"missing/duplicate support block");
    return found[1];
end;;
GWReplay:=function(c,recd,q)
    local x,state,e,index;
    x:=c.seed;
    if IsEmpty(recd.path) then state:=q;
    else state:=c.edges[recd.path[1]+1][1]; fi;
    GWAssert(state in c.initials,"noninitial path");
    for index in recd.path do
        e:=c.edges[index+1];
        GWAssert(e[1]=state,"disconnected path");
        state:=e[2]; x:=GWApply(c.matrices[e[3]+1],x);
    od;
    GWAssert(state=q and x=recd.counts,"incorrect path vector");
    return x;
end;;
GWPolynomialSamples:=0;; GWClosureCount:=0;; GWBasisCount:=0;;
GWRandom:=RandomSource(IsMersenneTwister,340380930);;
for recd in GWLanguageCases do
    c:=recd.certificate;; k:=recd.alphabet_size;; n:=Length(c.seed);;
    GWAssert(n=k*Length(recd.selected),"wrong component dimension");
    actualSeed:=Concatenation(List(recd.seeds,w->List([1..k],i->Number(w,a->a=i))));;
    GWAssert(actualSeed=c.seed,"wrong tuple seed counts");
    actualTerminal:=Filtered([1..n],i->recd.terminal_letters[(i-1) mod k+1]<>0)-1;;
    GWAssert(actualTerminal=c.terminal_indices,"wrong terminal filter");
    for mi in [1..Length(recd.morphisms)] do
        for i in [1..n] do for j in [1..n] do
            expected:=0;;
            if QuoInt(i-1,k)=QuoInt(j-1,k) then
                expected:=Number(recd.morphisms[mi][(j-1) mod k+1],a->a=(i-1) mod k+1);
            fi;
            GWAssert(expected=c.matrices[mi][i][j],"incorrect incidence matrix");
        od; od;
    od;
    # Test the polynomial on arbitrary counts, independently of reachable paths.
    for sample in [1..32] do
        x:=List([1..n],i->Random(GWRandom,0,4));;
        bmat:=List([1..recd.rank],i->List([1..recd.rank],j->
            Sum(Filtered([1..k],a->recd.terminal_letters[a]=i),a->x[(j-1)*k+a])-
            Sum(Filtered([1..k],a->recd.terminal_letters[a]=-i),a->x[(j-1)*k+a])));;
        expected:=DeterminantMat(bmat);;
        if recd.problem="F38" then
            iu:=Position(recd.selected,"U");; iv:=Position(recd.selected,"V");;
            expected:=expected*Sum(Filtered([1..k],a->recd.terminal_letters[a]<>0),
                a->x[(iu-1)*k+a]-x[(iv-1)*k+a]);
        fi;
        GWAssert(GWPoly(c,x)=expected,"determinant/length polynomial mismatch");
        GWPolynomialSamples:=GWPolynomialSamples+1;
    od;
    if not recd.with_span then continue; fi;
    GWAssert(c.complete_problem_decision=false,"unexpected full decision claim");
    GWAssert(c.degree=Maximum(Concatenation([0],List(Filtered(c.polynomial,t->t[1]<>0),
             t->Sum(t[2])))),"wrong polynomial degree");
    GWAssert(Length(c.monomials)=Binomial(n+c.degree,c.degree) and
             Length(Set(c.monomials))=Length(c.monomials),"incomplete lift");
    GWAssert(ForAll(c.monomials,e->Length(e)=n and Sum(e)<=c.degree and
             ForAll(e,a->IsInt(a) and a>=0)),"invalid monomial");
    nonzero:=false;;
    for block in c.basis do
        block.rows:=[];
        for pathRecord in block.records do
            x:=GWReplay(c,pathRecord,block.state);;
            GWAssert(GWSupport(x)=block.support,"wrong support");
            Add(block.rows,GWLift(c,x));
            if block.state in c.finals and ForAll(block.support,i->i in c.terminal_indices)
                    and GWPoly(c,x)<>0 then nonzero:=true; fi;
        od;
        GWAssert(RankMat(block.rows)=Length(block.rows),"dependent basis");
        GWBasisCount:=GWBasisCount+Length(block.rows);
    od;
    for q in c.initials do
        block:=GWBlock(c,q,GWSupport(c.seed));;
        GWAssert(SolutionMat(block.rows,GWLift(c,c.seed))<>fail,"missing seed");
    od;
    for block in c.basis do
        for e in Filtered(c.edges,e->e[1]=block.state) do
            for pathRecord in block.records do
                x:=GWApply(c.matrices[e[3]+1],pathRecord.counts);;
                target:=GWBlock(c,e[2],GWSupport(x));;
                GWAssert(SolutionMat(target.rows,GWLift(c,x))<>fail,"nonclosed span");
                GWClosureCount:=GWClosureCount+1;
            od;
        od;
    od;
    GWAssert(c.vanishes=(not nonzero),"wrong identity result");
    if nonzero then
        x:=GWReplay(c,c.witness,c.witness.state);;
        GWAssert(c.witness.state in c.finals and
                 ForAll(GWSupport(x),i->i in c.terminal_indices) and
                 GWPoly(c,x)=c.witness.value and c.witness.value<>0,"bad witness");
    fi;
od;
Print("EQUATION_TUPLES=",Length(GWLanguageTuples)," MONOID=",GWEquationCount,
      " GROUP=",GWGroupCount," CONSTRAINTS=",GWConstraintCount,"\n");
Print("GRAMMAR_CASES=",Length(GWLanguageCases)," POLYNOMIAL_SAMPLES=",GWPolynomialSamples,
      " BASIS=",GWBasisCount," CLOSURES=",GWClosureCount,"\n");
Print("PASS F34 F38 independent GAP language interface\n");
QUIT;
