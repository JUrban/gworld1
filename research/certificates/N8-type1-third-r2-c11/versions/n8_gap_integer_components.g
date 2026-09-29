# Exact disconnected-support decomposition, independent of the Python HNF code.
# This file is read after N8C9Fail has been defined by the certificate checker.
N8C9Components:=function(matrix)
    local n,m,parent,owner,root,i,j,a,b,groups,key,result,row;
    n:=Length(matrix);if n=0 then return [];fi;m:=Length(matrix[1]);
    parent:=[1..n];owner:=ListWithIdenticalEntries(m,0);
    root:=function(i)
        while parent[i]<>i do parent[i]:=parent[parent[i]];i:=parent[i];od;
        return i;
    end;
    for i in [1..n] do
        for j in [1..m] do
            if matrix[i][j]=0 then continue;fi;
            if owner[j]=0 then owner[j]:=i;
            else a:=root(i);b:=root(owner[j]);if a<>b then parent[b]:=a;fi;fi;
        od;
    od;
    groups:=rec();result:=[];
    for i in [1..n] do
        key:=String(root(i));
        if not IsBound(groups.(key)) then
            groups.(key):=rec(rows:=[],columns:=[]);Add(result,groups.(key));
        fi;
        Add(groups.(key).rows,i);
    od;
    for j in [1..m] do
        if owner[j]<>0 then Add(groups.(String(root(owner[j]))).columns,j);fi;
    od;
    return result;
end;;
N8C9IntegerSolution:=function(matrix,rhs)
    local components,answer,covered,part,rows,solution,i;
    if Length(matrix)=0 then
        if ForAll(rhs,x->x=0) then return [];else return fail;fi;
    fi;
    components:=N8C9Components(matrix);
    answer:=ListWithIdenticalEntries(Length(matrix),0);
    covered:=ListWithIdenticalEntries(Length(rhs),false);
    for part in components do
        for i in part.columns do covered[i]:=true;od;
        if Length(part.columns)=0 then continue;fi;
        rows:=List(part.rows,i->matrix[i]{part.columns});
        solution:=SolutionIntMat(rows,rhs{part.columns});
        if solution=fail then return fail;fi;
        for i in [1..Length(part.rows)] do answer[part.rows[i]]:=solution[i];od;
    od;
    if ForAny([1..Length(rhs)],i->not covered[i] and rhs[i]<>0) then return fail;fi;
    if answer*matrix<>rhs then N8C9Fail("component integer solution");fi;
    return answer;
end;;
N8C9Unimodular:=function(matrix)
    local part,n;
    n:=Length(matrix);
    if ForAny(matrix,row->Length(row)<>n) then return false;fi;
    for part in N8C9Components(matrix) do
        if Length(part.rows)<>Length(part.columns) or
           AbsInt(DeterminantMat(List(part.rows,i->matrix[i]{part.columns})))<>1 then
            return false;
        fi;
    od;
    return true;
end;;
N8C9SparseProduct:=function(vector,matrix)
    local answer,i;
    answer:=ListWithIdenticalEntries(Length(matrix[1]),0);
    for i in [1..Length(vector)] do
        if vector[i]<>0 then answer:=answer+vector[i]*matrix[i];fi;
    od;
    return answer;
end;;
