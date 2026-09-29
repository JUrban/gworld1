# Independent lattice, gate and actual fixed-group retraction replay.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
Read("research/certificates/N9-fixed-circuit/fixtures-v1.g");
(function()
    local d,a,rank,h,u,ui,kernel,forms,s,pairs,i,j,l,k,b,m,rows,
          add,slots,slot,r,flat,coords,pivot,last,f,x,rels,w,ep,g,gens,
          h1,h2,c,sub,images,hom,values,z,rv,ru,wrong,unguarded,q;
    d:=N9Circuit[1]; a:=N9Circuit[2]; rank:=N9Circuit[3];
    h:=N9Circuit[4]; u:=N9Circuit[5]; ui:=N9Circuit[6];
    kernel:=N9Circuit[7]; forms:=N9Circuit[8]; s:=Length(forms);
    if d<>14 or s<>68 or rank<>23 then Error("Fixed circuit dimensions"); fi;
    pairs:=Combinations([1..d],2);
    rows:=[];
    add:=function(terms)
        local row,term,ij,sign;
        row:=List(pairs,p->0);
        for term in terms do
            ij:=term{[1,2]}; sign:=1;
            if ij[1]>ij[2] then ij:=Reversed(ij); sign:=-1; fi;
            row[Position(pairs,ij)]:=row[Position(pairs,ij)]+sign*term[3];
        od;
        Add(rows,row);
    end;
    # p,y,one,y+one,square; zero-based paper indices are shifted by one.
    slots:=[[5,6],[7,8],[9,10],[11,12],[13,14]];
    for slot in slots do
        add([[1,slot[1],1]]);
        add([[2,slot[2],1]]);
        add([[2,slot[1],1],[1,slot[2],1]]);
    od;
    add([[1,10,1],[1,2,-1]]);
    add([[1,12,1],[1,8,-1],[1,10,-1]]);
    add([[11,12,1],[1,14,-1]]);
    add([[1,14,1],[1,6,-1]]);
    add([[1,4,1]]); add([[2,3,1]]);
    add([[2,4,1],[1,3,-1]]); add([[1,3,1],[1,6,-3]]);
    if rows<>a then Error("Independent gate reconstruction"); fi;
    if u*TransposedMat(a)<>h or AbsInt(DeterminantMat(u))<>1 or
       u*ui<>IdentityMat(Length(pairs)) then Error("Unimodular certificate"); fi;
    last:=0;
    for i in [1..rank] do
        pivot:=PositionProperty(h[i],x->x<>0);
        if pivot=fail or pivot<=last or h[i][pivot]<1 then Error("Row echelon rank"); fi;
        last:=pivot;
    od;
    if ForAny(h{[rank+1..Length(pairs)]},r->ForAny(r,x->x<>0)) or
       kernel<>u{[rank+1..Length(pairs)]} then Error("Full kernel certificate"); fi;
    for l in [1..s] do
        b:=NullMat(d,d);
        for k in [1..Length(pairs)] do
            i:=pairs[k][1]; j:=pairs[k][2];
            b[i][j]:=kernel[l][k]; b[j][i]:=-kernel[l][k];
        od;
        if b<>forms[l] then Error("Group form basis"); fi;
    od;
    Print("Independent fixed gates and full saturated integer kernel checked\n");
    for r in N9CircuitRetractions do
        m:=r[8]; flat:=List(pairs,ij->m[ij[1]][ij[2]]);
        if a*flat<>List(a,x->0) or RankMat(m)<>2 or
           Sum([1..s],l->r[3][l]*forms[l])<>m then Error("Circuit witness matrix"); fi;
        if (3*r[1]+1)*m[1][2]-m[1][3]<>1 or m[1][2]<>1 or
           m[1][3]<>3*r[1] then Error("Parameter normalization"); fi;
        values:=List(slots,slot->m[1][slot[2]]);
        if values<>[r[1],r[2],1,r[2]+1,(r[2]+1)^2] or
           values[5]<>values[1] then Error("Recovered arithmetic values"); fi;
        for slot in slots do
            if m[slot[1]][2]<>m[1][slot[2]] or m[1][slot[1]]<>0 or
               m[2][slot[2]]<>0 then Error("Axis normalization"); fi;
        od;
    od;
    wrong:=N9WrongSign; unguarded:=StructuralCopy(a);
    unguarded[Length(a)][Position(pairs,[1,6])]:=-1;
    flat:=List(pairs,ij->wrong[ij[1]][ij[2]]);
    if RankMat(wrong)<>2 or unguarded*flat<>List(a,x->0) or
       a*flat=List(a,x->0) or 3*wrong[1][2]-wrong[1][3]<>1 or
       wrong[1][2]<>-1 or wrong[1][6]<>-4 then Error("Wrong-sign control"); fi;
    Print("Integral circuit witnesses and necessary modulus-three guard checked\n");
    f:=FreeGroup(d+s); x:=GeneratorsOfGroup(f); rels:=[];
    for i in [1..d+s] do for j in [i+1..d+s] do
        w:=Comm(x[i],x[j]);
        if j<=d then
            for l in [1..s] do w:=w*x[d+l]^-forms[l][i][j]; od;
        fi;
        Add(rels,w);
    od; od;
    f:=f/rels; ep:=NqEpimorphismNilpotentQuotient(f,2);
    g:=Image(ep); gens:=List(GeneratorsOfGroup(f),x->Image(ep,x));
    if HirschLength(g)<>d+s or Size(TorsionSubgroup(g))<>1 then Error("Fixed group"); fi;
    Print("One fixed torsion-free class-two group: Hirsch length ",HirschLength(g),"\n");
    for r in N9CircuitRetractions do
        h1:=gens[1]; h2:=gens[2]^(3*r[1]+1)*gens[3]^-1;
        c:=Comm(h1,h2); sub:=Subgroup(g,[h1,h2]);
        q:=List(forms,b->(3*r[1]+1)*b[1][2]-b[1][3]);
        if c=One(g) or q<>r[4] or Sum([1..s],l->r[3][l]*q[l])<>1 or
           c<>Product([1..s],l->gens[d+l]^q[l]) or HirschLength(sub)<>3 then
            Error("Input subgroup");
        fi;
        images:=List([1..d],i->h1^r[5][i]*h2^r[6][i]*c^r[7][i]);
        Append(images,List(r[3],l->c^l));
        hom:=GroupHomomorphismByImages(g,g,gens,images);
        if hom=fail or Image(hom,h1)<>h1 or Image(hom,h2)<>h2 or Image(hom)<>sub then
            Error("Not a retraction");
        fi;
        if ForAny(images,x->Image(hom,x)<>x) then Error("Not idempotent"); fi;
        Print("Actual retraction for n=",r[1],", y=",r[2]," checked\n");
    od;
    # These are algebraic negative cases by reverse extraction in the proof.
    # Here only their genuine noncommuting input subgroups are checked.
    for k in [-1,2,3] do
        h1:=gens[1]; h2:=gens[2]^(3*k+1)*gens[3]^-1;
        if Comm(h1,h2)=One(g) or HirschLength(Subgroup(g,[h1,h2]))<>3 then
            Error("Negative parameter subgroup");
        fi;
    od;
    Print("Negative-parameter subgroup inputs checked; no bounded nonexistence inference\n");
    Print("PASS independent GAP N9 fixed-circuit lattice and retractions\n");
end)();
QUIT;
