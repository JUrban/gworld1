N8C9Fail:=function(s) Print("FAIL ",s,"\n");FORCE_QUIT_GAP(1);end;;
Read("scripts/n8_gap_integer_components.g");
CheckComponents:=function()
    local rng,n,m,i,j,matrix,rhs,a,b,cases,detcases;
    rng:=RandomSource(IsMersenneTwister,9282670);cases:=0;detcases:=0;
    for n in [1..8] do
        for m in [1..9] do
            for j in [1..3] do
                matrix:=List([1..n],i->List([1..m],k->Random(rng,[-2..2])));
                if j=2 then
                    for i in [1..n] do
                        for k in [1..m] do
                            if i mod 2<>k mod 2 then matrix[i][k]:=0;fi;
                        od;
                    od;
                fi;
                if j=3 then rhs:=List([1..n],i->Random(rng,[-2..2]))*matrix;
                else rhs:=List([1..m],i->Random(rng,[-3..3]));fi;
                a:=SolutionIntMat(matrix,rhs);b:=N8C9IntegerSolution(matrix,rhs);
                if (a=fail)<>(b=fail) then N8C9Fail("membership disagreement");fi;
                if b<>fail and b*matrix<>rhs then N8C9Fail("solution identity");fi;
                cases:=cases+1;
                if n=m then
                    if N8C9Unimodular(matrix)<>(AbsInt(DeterminantMat(matrix))=1) then
                        N8C9Fail("unimodularity disagreement");fi;
                    detcases:=detcases+1;
                fi;
            od;
        od;
    od;
    if N8C9IntegerSolution([[2,0],[0,3]],[1,0])<>fail or
       N8C9IntegerSolution([[0,0]],[0,1])<>fail or
       N8C9IntegerSolution([],[0,1])<>fail or
       N8C9IntegerSolution([],[0,0])<>[] then N8C9Fail("boundary controls");fi;
    Print("PASS GAP integer components: ",cases," affine comparisons; ",detcases,
          " determinant comparisons; 4 boundary controls; seed9282670\n");
end;;
CheckComponents();;
QUIT_GAP(0);
