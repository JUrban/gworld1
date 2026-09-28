# Independent rational-rank certificates through integer polynomials and mod251.
# Full modular rank is a certified lower bound on rational rank. For the
# one-dimensional kernels, an exact nonzero integer relation gives the upper
# bound. The obstruction matrices have full row rank, including the extra row.
Read(Concatenation(N8C9Directory,"/kernel-fixtures.g"));
N8MFail:=function(message)
    Print("FAIL ",message,"\n");FORCE_QUIT_GAP(1);
end;;
N8MBracket:=function(a,b) return a*b-b*a;end;;
N8MRun:=function()
    local r,A,gens,F,fgens,hall,bydegree,weight,new,i,j,a,b,words,evalword,
          lift,delta,modrank,row,p,q,offset,c,d,cols,relation,rank,n,z,t,quad,
          v0,before,after,kcount,ocount,prime;
    r:=N8C9KernelData.rank;prime:=251;
    A:=FreeAssociativeAlgebraWithOne(Rationals,r);
    gens:=GeneratorsOfAlgebraWithOne(A);
    if Length(gens)<>r then N8MFail("algebra generator count");fi;
    F:=FreeGroup(r);fgens:=GeneratorsOfGroup(F);
    evalword:=function(w)
        local ans,s;
        ans:=One(F);
        for s in w do ans:=ans*fgens[AbsInt(s)]^SignInt(s);od;
        return ans;
    end;
    hall:=List([1..r],i->rec(weight:=1,pair:=fail,value:=gens[i],word:=fgens[i]));
    for weight in [2..9] do
        new:=[];
        for i in [1..Length(hall)] do
            a:=hall[i];
            for j in [1..i-1] do
                b:=hall[j];
                if a.weight+b.weight<>weight then continue;fi;
                if a.pair<>fail and a.pair[2]>j then continue;fi;
                Add(new,rec(weight:=weight,pair:=[i,j],value:=N8MBracket(a.value,b.value),
                            word:=Comm(a.word,b.word)));
            od;
        od;
        Append(hall,new);
    od;
    bydegree:=List([1..9],d->Filtered(hall,h->h.weight=d));
    for d in [1..9] do
        words:=List(N8C9Halls[d],evalword);
        if words<>List(bydegree[d],h->h.word) then N8MFail("Hall word agreement");fi;
    od;
    Print("HALL verified rank",r," through9\n");
    lift:=function(d,coords)
        local ans,i;
        ans:=Zero(A);
        for i in [1..Length(coords)] do
            if coords[i]<>0 then ans:=ans+coords[i]*bydegree[d][i].value;fi;
        od;
        return ans;
    end;
    delta:=function(z,t,n)
        local i;
        for i in [1..n] do t:=N8MBracket(z,t);od;
        return t;
    end;
    modrank:=function(polynomials)
        local supports,monomials,poly,ext,i,vector,matrix,fieldzero,fieldone,pos;
        supports:=List(polynomials,CoefficientsAndMagmaElements);
        monomials:=[];
        for ext in supports do
            for i in [1,3..Length(ext)-1] do Add(monomials,ext[i]);od;
        od;
        monomials:=Set(monomials);matrix:=[];
        fieldzero:=Zero(GF(prime));fieldone:=One(GF(prime));
        for ext in supports do
            vector:=ListWithIdenticalEntries(Length(monomials),fieldzero);
            for i in [1,3..Length(ext)-1] do
                if not IsInt(ext[i+1]) then N8MFail("noninteger tensor coefficient");fi;
                pos:=PositionSorted(monomials,ext[i]);
                vector[pos]:=ext[i+1]*fieldone;
            od;
            ConvertToVectorRep(vector,prime);Add(matrix,vector);
        od;
        return RankMat(matrix);
    end;
    kcount:=0;
    for row in N8C9KernelData.records do
        p:=row.p;q:=row.q;offset:=row.j;c:=lift(p,row.C);d:=lift(q,row.D);
        cols:=Concatenation(List(bydegree[p+offset],h->N8MBracket(h.value,d)),
                            List(bydegree[q+offset],h->N8MBracket(c,h.value)));
        rank:=modrank(cols);
        if rank<>Length(cols)-row.expected then N8MFail("modular kernel rank");fi;
        if row.expected=1 then
            if not IsBound(row.predicted_direction) or
               ForAll(row.predicted_direction,x->x=0) then N8MFail("missing exact relation");fi;
            relation:=Zero(A);
            for i in [1..Length(cols)] do
                if row.predicted_direction[i]<>0 then
                    relation:=relation+row.predicted_direction[i]*cols[i];
                fi;
            od;
            if relation<>Zero(A) then N8MFail("integer kernel relation");fi;
        elif row.expected<>0 then N8MFail("unsupported kernel dimension");fi;
        kcount:=kcount+1;Print("KERNEL ",kcount," ",row.test," mod",prime," rank",rank,"\n");
    od;
    ocount:=0;
    for row in N8C9KernelData.obstructions do
        z:=lift(1,row.z);t:=lift(2,row.T);d:=lift(6,row.D);quad:=lift(9,row.Q);
        if d<>delta(z,t,4) then N8MFail("exceptional leading term");fi;
        v0:=N8MBracket(t,delta(z,t,3))-N8MBracket(delta(z,t,1),delta(z,t,2));
        if quad<>N8MBracket(t,v0) then N8MFail("obstruction polynomial");fi;
        cols:=Concatenation(List(bydegree[3],h->N8MBracket(h.value,d)),
                            List(bydegree[8],h->N8MBracket(z,h.value)));
        before:=modrank(cols);after:=modrank(Concatenation(cols,[quad]));
        if before<>Length(cols) or after<>before+1 or [before,after]<>row.ranks then
            N8MFail("rationally independent obstruction");fi;
        ocount:=ocount+1;Print("OBSTRUCTION ",ocount," mod",prime," ranks",before,",",after,"\n");
    od;
    Print("PASS N8 class9 modular GAP: rank",r,"; ",kcount," kernels; ",ocount," obstructions\n");
end;;
N8MRun();;
QUIT_GAP(0);
