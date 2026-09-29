if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
Read("research/certificates/N8-odd-adjoint-lead/fixtures.g");
N8OddEval:=function(g,w)
    local result,gens,i;
    result:=One(g);gens:=GeneratorsOfGroup(g);
    for i in w do result:=result*gens[AbsInt(i)]^SignInt(i);od;
    return result;
end;
Read("research/certificates/N8-odd-adjoint-lead/hall-trees.g");
N8OddValues:=[];
N8OddBuild:=function(g)
    local row,gens;
    N8OddValues:=[];gens:=GeneratorsOfGroup(g);
    for row in N8OddHallTrees do
        if row[2]=0 then Add(N8OddValues,gens[row[3]]);
        else Add(N8OddValues,Comm(N8OddValues[row[2]],N8OddValues[row[3]]));fi;
    od;
end;
N8OddH:=function(g,d)
    return N8OddValues{Filtered([1..Length(N8OddHallTrees)],i->N8OddHallTrees[i][1]=d)};
end;
N8OddLift:=function(g,d,coordinates)
    local halls,result,i;
    halls:=N8OddH(g,d);result:=One(g);
    for i in [1..Length(halls)] do result:=result*halls[i]^coordinates[i];od;
    return result;
end;
N8OddRun:=function()
    local g,z,t,d,v,q,columns,product,i,ranks;
    g:=NilpotentQuotient(FreeGroup(2),10);N8OddBuild(g);
    z:=N8OddLift(g,1,N8OddData[1]);t:=N8OddLift(g,2,N8OddData[2]);
    d:=N8OddLift(g,8,N8OddData[3]);v:=N8OddLift(g,9,N8OddData[4]);
    if Comm(z,v)<>Comm(t,d) then Error("kernel identity");fi;
    columns:=Concatenation(List(N8OddH(g,2),u->Comm(u,d)),List(N8OddH(g,9),u->Comm(z,u)));
    if Length(columns)-HirschLength(Subgroup(g,columns))<>1 then Error("kernel dimension");fi;
    product:=One(g);
    for i in [1..Length(columns)] do product:=product*columns[i]^N8OddData[6][i];od;
    if product<>One(g) then Error("kernel direction");fi;
    Print("PASS first kernel and direction\n");
    g:=NilpotentQuotient(FreeGroup(2),11);N8OddBuild(g);
    z:=N8OddLift(g,1,N8OddData[1]);t:=N8OddLift(g,2,N8OddData[2]);
    d:=N8OddLift(g,8,N8OddData[3]);v:=N8OddLift(g,9,N8OddData[4]);q:=N8OddLift(g,11,N8OddData[5]);
    if Comm(t,v)<>q then Error("obstruction word");fi;
    columns:=Concatenation(List(N8OddH(g,3),u->Comm(u,d)),List(N8OddH(g,10),u->Comm(z,u)));
    ranks:=[HirschLength(Subgroup(g,columns)),HirschLength(Subgroup(g,Concatenation(columns,[q])))];
    if ranks<>N8OddData[7] or ranks[2]<>ranks[1]+1 then Error("cokernel obstruction");fi;
    Print("PASS N8 GAP odd-adjoint lead: class11/rank2 kernel and nonzero cokernel\n");
end;
N8OddRun();
QUIT;
