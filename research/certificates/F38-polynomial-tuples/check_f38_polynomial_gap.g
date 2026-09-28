# Independent rational-span, path and free-group replay of F38 certificates.
# No Python implementation is loaded. This is not a recompression solver.
Read("research/certificates/F38-polynomial-tuples/fixtures.g");;

F38Assert := function(ok, message)
    if not ok then Error(message); fi;
end;;
F38Apply := function(matrix, counts)
    return List(matrix, row -> row * counts);
end;;
F38Support := function(counts)
    return Filtered([1..Length(counts)], i -> counts[i] <> 0) - 1;
end;;
F38Monomial := function(counts, exponents)
    return Product([1..Length(counts)], i -> counts[i]^exponents[i]);
end;;
F38Lift := function(c, counts)
    return List(c.monomials, e -> F38Monomial(counts, e));
end;;
F38Polynomial := function(c, counts)
    return Sum(c.polynomial, term -> term[1] * F38Monomial(counts, term[2]));
end;;
F38InSpan := function(rows, vector)
    return SolutionMat(rows, vector) <> fail;
end;;
F38Block := function(c, state, support)
    local found;
    found := Filtered(c.basis, b -> b.state = state and b.support = support);
    F38Assert(Length(found) = 1, "missing or duplicate support block");
    return found[1];
end;;
F38Replay := function(c, record, target)
    local state, counts, ei, edge;
    counts := c.seed;
    if IsEmpty(record.path) then
        F38Assert(target in c.initials, "empty path not at initial state");
        state := target;
    else
        state := c.edges[record.path[1]+1][1];
        F38Assert(state in c.initials, "path does not start initially");
    fi;
    for ei in record.path do
        edge := c.edges[ei+1];
        F38Assert(state = edge[1], "disconnected witness path");
        counts := F38Apply(c.matrices[edge[3]+1], counts);
        state := edge[2];
    od;
    F38Assert(state = target and counts = record.counts, "incorrect path counts");
    return counts;
end;;

F38CheckCase := function(c)
    local n, degree, b, record, counts, rows, state, edge, target, transformed,
          terminal, accepted, nonzero, value, closures, total, alphabetSize,
          componentCount, mi, i, j, expected, letter, component, actualSeed;
    n := Length(c.seed);
    F38Assert(n>0 and ForAll(c.seed, x -> IsInt(x) and x>=0), "bad seed");
    F38Assert(ForAll(c.matrices, m -> Length(m)=n and ForAll(m, row ->
        Length(row)=n and ForAll(row, x -> IsInt(x) and x>=0))), "bad matrix");
    if IsBound(c.tuple_morphisms) then
        alphabetSize:=c.tuple_alphabet_size;
        componentCount:=Length(c.tuple_seeds);
        F38Assert(n=alphabetSize*componentCount,"bad tuple dimension");
        actualSeed:=List([1..n],i->0);
        for component in [0..componentCount-1] do
            actualSeed[component*alphabetSize+c.tuple_seeds[component+1]+1]:=1;
        od;
        F38Assert(actualSeed=c.seed,"tuple seeds mismatch");
        for mi in [1..Length(c.tuple_morphisms)] do
            for i in [0..n-1] do
                for j in [0..n-1] do
                    expected:=0;
                    if QuoInt(i,alphabetSize)=QuoInt(j,alphabetSize) then
                        letter:=i mod alphabetSize;
                        expected:=Number(c.tuple_morphisms[mi][j mod alphabetSize+1],
                                         x->x=letter);
                    fi;
                    F38Assert(c.matrices[mi][i+1][j+1]=expected,
                              "wrong component incidence matrix");
                od;
            od;
        od;
    fi;
    degree := Maximum(Concatenation([0], List(Filtered(c.polynomial,
        term -> term[1]<>0), term -> Sum(term[2]))));
    F38Assert(c.degree=degree, "wrong degree");
    F38Assert(Length(c.monomials)=Binomial(n+degree,degree), "missing monomials");
    F38Assert(Length(Set(c.monomials))=Length(c.monomials), "duplicate monomials");
    F38Assert(ForAll(c.monomials,e -> Length(e)=n and Sum(e)<=degree and
        ForAll(e,x -> IsInt(x) and x>=0)), "invalid monomial");
    terminal := [0..n-1];
    if IsBound(c.terminal_indices) then terminal := c.terminal_indices; fi;
    nonzero := false; closures := 0; total := 0;
    for b in c.basis do
        rows := [];
        for record in b.records do
            counts := F38Replay(c,record,b.state);
            F38Assert(F38Support(counts)=b.support,"wrong support");
            Add(rows,F38Lift(c,counts));
        od;
        F38Assert(RankMat(rows)=Length(rows),"dependent alleged basis");
        b.checked_rows := rows;
        total := total+Length(rows);
        accepted := b.state in c.finals and ForAll(b.support, i -> i in terminal);
        if accepted then
            for record in b.records do
                value := F38Polynomial(c,record.counts);
                if value<>0 then nonzero := true; fi;
            od;
        fi;
    od;
    for state in c.initials do
        b := F38Block(c,state,F38Support(c.seed));
        F38Assert(F38InSpan(b.checked_rows,F38Lift(c,c.seed)),"missing seed vector");
    od;
    for b in c.basis do
        for edge in Filtered(c.edges,e -> e[1]=b.state) do
            for record in b.records do
                transformed := F38Apply(c.matrices[edge[3]+1],record.counts);
                target := F38Block(c,edge[2],F38Support(transformed));
                F38Assert(F38InSpan(target.checked_rows,F38Lift(c,transformed)),
                    "span not closed under a transition");
                closures := closures+1;
            od;
        od;
    od;
    F38Assert(c.vanishes=(not nonzero),"incorrect identity decision");
    F38Assert(c.vanishes=c.expected,"unexpected control result");
    if nonzero then
        counts := F38Replay(c,c.witness,c.witness.state);
        F38Assert(c.witness.state in c.finals and
            ForAll(F38Support(counts),i -> i in terminal),"witness is not accepted");
        F38Assert(F38Polynomial(c,counts)=c.witness.value and c.witness.value<>0,
            "invalid nonzero witness");
    else
        F38Assert(c.witness=fail,"unexpected witness");
    fi;
    Print(c.name,": basis=",total," closures=",closures," identity=",c.vanishes,"\n");
    return [total,closures];
end;;

F38Word := function(gens, letters)
    local word, i;
    word := One(gens[1]);
    for i in letters do word := word * gens[AbsInt(i)]^SignInt(i); od;
    return word;
end;;
F38CyclicLength := function(word)
    local letters, first, last;
    letters := LetterRepAssocWord(word);
    first:=1; last:=Length(letters);
    while last-first>=1 and letters[first]=-letters[last] do
        first:=first+1; last:=last-1;
    od;
    return last-first+1;
end;;
F38CheckWords := function(records)
    local record, f, gens, images, matrix, determinant, lengths, g, word,
          differingSingular, nonzeroDeterminants, nonzeroGates;
    differingSingular:=0; nonzeroDeterminants:=0; nonzeroGates:=0;
    for record in records do
        f:=FreeGroup(record.rank); gens:=GeneratorsOfGroup(f);
        images:=List(record.images,w -> F38Word(gens,w));
        matrix:=TransposedMat(List(images,w ->
            List([1..record.rank],i -> ExponentSumWord(w,gens[i]))));
        determinant:=DeterminantMat(matrix);
        lengths:=[];
        for word in [record.u,record.v] do
            g:=MappedWord(F38Word(gens,word),gens,images);
            Add(lengths,F38CyclicLength(g));
        od;
        F38Assert(determinant=record.determinant and lengths=record.lengths,
            "free-group value mismatch");
        F38Assert(determinant*(lengths[1]-lengths[2])=record.gated_value,
            "gated polynomial mismatch");
        if determinant=0 and lengths[1]<>lengths[2] then
            differingSingular:=differingSingular+1;
        fi;
        if determinant<>0 then nonzeroDeterminants:=nonzeroDeterminants+1; fi;
        if record.gated_value<>0 then nonzeroGates:=nonzeroGates+1; fi;
    od;
    F38Assert(differingSingular>0 and nonzeroDeterminants>0 and nonzeroGates>0,
        "missing controls");
    return [Length(records),differingSingular,nonzeroDeterminants,nonzeroGates];
end;;

F38Totals := List(F38Cases,F38CheckCase);;
Print("SPAN_TOTALS=",Sum(F38Totals),"\n");
Print("WORD_TOTALS=",F38CheckWords(F38Words),"\n");
Print("PASS F38 GAP independent polynomial and free-word replay\n");
QUIT;
