# The common group/linear/arithmetic definitions are loaded by the driver.
Read(Concatenation(N8C9Directory,"/coupled-fixtures.g.gz"));;
N8TenCentral:=function(group,degree,coords)
    local ans,h,i;
    h:=List(N8C9Halls[degree],w->N8C9Eval(group,w));ans:=One(group);
    if Length(h)<>Length(coords) then N8C9Fail("central coordinate width");fi;
    for i in [1..Length(h)] do if coords[i]<>0 then ans:=ans*h[i]^coords[i];fi;od;
    return ans;
end;;
N8TenApply:=function(group,pair,p,q,j,coords)
    local x,y,u,v,i;
    x:=pair[1];y:=pair[2];
    u:=List(N8C9Halls[p+j],w->N8C9Eval(group,w));
    v:=List(N8C9Halls[q+j],w->N8C9Eval(group,w));
    if Length(coords)<>Length(u)+Length(v) then N8C9Fail("correction width");fi;
    for i in [1..Length(u)] do if coords[i]<>0 then x:=x*u[i]^coords[i];fi;od;
    for i in [1..Length(v)] do
        if coords[Length(u)+i]<>0 then y:=y*v[i]^coords[Length(u)+i];fi;
    od;
    return [x,y];
end;;
N8TenColumns:=function(group,pair,p,q,j)
    local x,y,base,ans,h,w;
    x:=pair[1];y:=pair[2];base:=Comm(x,y);ans:=[];
    for w in N8C9Halls[p+j] do
        h:=N8C9Eval(group,w);Add(ans,Comm(base,h)*Comm(h,y));
    od;
    for w in N8C9Halls[q+j] do
        h:=N8C9Eval(group,w);Add(ans,Comm(x,h)^base*Comm(base,h));
    od;
    return ans;
end;;
N8TenCoupledMatrix:=function(row)
    return Concatenation(row.columns,[-row.coefficients[2]]);
end;;
N8TenCheckAffine:=function(matrix,rhs,base,kernel)
    local nullity,v;
    if base*matrix<>rhs then N8C9Fail("coupled particular");fi;
    nullity:=Length(matrix)-RankMat(matrix);
    if nullity<>Length(kernel) or nullity>1 then N8C9Fail("coupled kernel dimension");fi;
    for v in kernel do
        if ForAny(v*matrix,x->x<>0) or Gcd(v)<>1 or Last(v)=0 then
            N8C9Fail("complete primitive coupled kernel");fi;
    od;
end;;
N8TenRun:=function()
    local row,group,pair0,pair,target,actual,i,sample,k,matrix,sol,c,
          coupledCount,coupledNegative,polyCount,emptyCount,sampleCount,lateCount,
          coords,chosen,base,direction;
    coupledCount:=0;coupledNegative:=0;polyCount:=0;
    emptyCount:=0;sampleCount:=0;lateCount:=0;
    for row in N8C10Coupled do
        group:=N8C9Group(row.rank,9);
        pair0:=[N8C9Eval(group,row.x0),N8C9Eval(group,row.y0)];
        target:=N8C9Eval(group,row.word);
        actual:=N8TenColumns(group,pair0,1,5,3);
        if actual<>List(row.columns,v->N8TenCentral(group,9,v)) then
            N8C9Fail("coupled correction columns");fi;
        for sample in row.samples do
            k:=sample[1];pair:=N8TenApply(group,pair0,1,5,2,row.vector+k*row.kernel);
            if pair<>List(sample{[2,3]},w->N8C9Eval(group,w)) or
               Comm(pair[1],pair[2])^-1*target<>
               N8TenCentral(group,9,row.coefficients[1]+k*row.coefficients[2]) then
                N8C9Fail("coupled affine residual");fi;
        od;
        matrix:=N8TenCoupledMatrix(row);
        sol:=N8C9IntegerSolution(matrix,row.coefficients[1]);
        if (sol=fail)<>(row.solution=fail) then N8C9Fail("coupled integer solvability");fi;
        if sol=fail then coupledNegative:=coupledNegative+1;
        else N8TenCheckAffine(matrix,row.coefficients[1],row.solution[1],row.solution[2]);fi;
        coupledCount:=coupledCount+1;Print("COUPLED ",coupledCount," VERIFIED\n");
    od;
    for row in N8C9Polynomials do
        c:=row.certificate;N8C9Arithmetic(c,row.q=4);
        group:=N8C9Group(row.rank,row.degree);
        pair0:=[N8C9Eval(group,row.x0),N8C9Eval(group,row.y0)];
        target:=N8C9Eval(group,row.word);
        if row.kind="polynomial_late" then
            lateCount:=lateCount+1;
            chosen:=First(N8C10Coupled,r->r.word=row.word and r.x0=row.x0 and
                          r.y0=row.y0 and r.vector=row.vector and r.kernel=row.kernel);
            if chosen=fail or chosen.solution=fail then N8C9Fail("missing coupled stage");fi;
            N8TenCheckAffine(N8TenCoupledMatrix(chosen),chosen.coefficients[1],
                             row.coupled_base,[row.coupled_direction]);
            if not ForAny(c.residual[3],v->v[1]<>0) then N8C9Fail("late quadratic obstruction");fi;
            actual:=N8TenColumns(group,pair0,1,5,4);
        else actual:=N8TenColumns(group,pair0,1,row.q,2);fi;
        if actual<>List(c.columns,v->N8TenCentral(group,row.degree,v)) then
            N8C9Fail("polynomial correction columns");fi;
        for sample in row.samples do
            k:=sample[1];
            if row.kind="polynomial_late" then
                coords:=row.coupled_base+k*row.coupled_direction;
                pair:=N8TenApply(group,pair0,1,5,2,row.vector+Last(coords)*row.kernel);
                pair:=N8TenApply(group,pair,1,5,3,coords{[1..Length(coords)-1]});
            else pair:=N8TenApply(group,pair0,1,row.q,1,row.vector+k*row.kernel);fi;
            if pair<>List(sample{[2,3]},w->N8C9Eval(group,w)) or
               Comm(pair[1],pair[2])^-1*target<>
               N8TenCentral(group,row.degree,N8C9Poly(c.coefficients,k)) then
                N8C9Fail("polynomial lifts or coefficients");fi;
            sampleCount:=sampleCount+1;
        od;
        if Length(c.values)=0 then emptyCount:=emptyCount+1;fi;
        polyCount:=polyCount+1;Print("POLYNOMIAL ",polyCount," VERIFIED\n");
    od;
    Print("PASS N8 full class10 GAP: ",N8C9Positive," witnesses; ",N8C9Count,
          " linear decisions (",N8C9Negative," negative); ",coupledCount,
          " coupled (",coupledNegative," negative); ",polyCount," polynomial (",
          emptyCount," empty, ",lateCount," late); ",sampleCount," polynomial samples\n");
end;;
N8TenRun();;
QUIT_GAP(0);
