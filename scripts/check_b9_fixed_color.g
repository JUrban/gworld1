# Native free-group verification of all fixed-color finite certificates.
Read("research/certificates/B9-fixed-color-decisions-v2/fixtures.g");
Read("research/certificates/B9/height4-fixtures.g");
(function()
    local F,X,action,equal,inv,shift,red,shelf,eps,delete,unshift,
          classify,checkfraction,pi,record,r,base,difference,actual,expected,
          c,k,i,n,sols,source,counts,specialChecks,colorSteps,failedDivisions,
          good,bad,productChecks,reversalChecks,knownParameters,I2,knownImages;
    F:=FreeGroup(32);X:=GeneratorsOfGroup(F);
    action:=function(word)
        local out,a,i,b,d;
        out:=ShallowCopy(X);
        for a in word do
            i:=AbsInt(a);if i=0 or i>=Length(X) then Error("Word/rank bound");fi;
            b:=out[i];d:=out[i+1];
            if a>0 then out[i]:=b*d*b^-1;out[i+1]:=b;
            else out[i]:=d;out[i+1]:=d^-1*b*d;fi;
        od;
        return out;
    end;
    equal:=function(a,b)return action(a)=action(b);end;
    inv:=w->List(Reversed(w),j->-j);
    shift:=w->List(w,j->SignInt(j)*(AbsInt(j)+1));
    red:=function(word)
        local out,a;
        out:=[];
        for a in word do
            if not IsEmpty(out) and out[Length(out)]=-a then Remove(out);else Add(out,a);fi;
        od;
        return out;
    end;
    shelf:=function(a,b)return red(Concatenation(a,shift(b),[1],inv(shift(a))));end;
    I2:=a->red(Concatenation(a,[2,1],inv(shift(a))));
    knownParameters:=[[],[2],[1,2],[1,1,-2]];
    knownImages:=List(knownParameters,a->action(I2(a)));
    eps:=w->Sum(List(w,SignInt));
    delete:=function(word,n,keep)
        local labels,out,a,i,j,temp;
        labels:=[1..n];out:=[];
        for a in word do
            i:=AbsInt(a);
            if labels[i] in keep and labels[i+1] in keep then
                j:=Number(labels{[1..i]},v->v in keep);Add(out,SignInt(a)*j);
            fi;
            temp:=labels[i];labels[i]:=labels[i+1];labels[i+1]:=temp;
        od;
        return [red(out),labels];
    end;
    unshift:=function(word)
        local n,d;
        n:=Maximum(Concatenation([2],List(word,a->AbsInt(a)+1)));
        d:=delete(word,n,[2..n]);
        if d[2][1]<>1 or not equal(word,shift(d[1])) then return fail;fi;
        return d[1];
    end;
    checkfraction:=function(word,fraction)
        local negative,a;
        negative:=false;
        for a in fraction do
            if a<0 then negative:=true;elif negative then Error("Not a positive-negative fraction");fi;
        od;
        if not equal(word,fraction) then Error("Fraction changed braid");fi;
    end;
    specialChecks:=0;colorSteps:=0;failedDivisions:=0;
    classify:=function(r)
        local n,e,perm,a,i,nu,power,colors,position,pair,test,d,next,answer,j,expected;
        specialChecks:=specialChecks+1;
        n:=Maximum(Concatenation([2],List(r.word,a->AbsInt(a)+1)));e:=eps(r.word);
        if n<>r.ambient_rank or e<>r.exponent then Error("Specialness input binding");fi;
        if r.reason="exponent_permutation" then
            perm:=();for a in r.word do i:=AbsInt(a);perm:=(i,i+1)*perm;od;
            nu:=Number([1..n-1],j->(j+1)^perm=j);
            if e=nu or r.special or List([1..n],j->j^perm)<>r.permutation then Error("Exponent-permutation obstruction");fi;
            return false;
        elif r.reason="zero_exponent" then
            if e<>0 or r.special<>equal(r.word,[]) then Error("Zero-exponent specialness");fi;
            return r.special;
        elif r.reason="positive_word" then
            if not ForAll(r.word,a->a>0) then Error("Nonpositive input in positive case");fi;
            answer:=equal(r.word,Reversed([1..n-1]));
            if r.special<>answer then Error("Positive-special classification");fi;
            return answer;
        elif r.reason="right_power" then
            if e<1 or e>=n then Error("Power range");fi;
            power:=r.word;
            for j in [1..n-e-1] do power:=shelf(r.word,power);od;
            if not equal(power,r.power) or equal(power,Reversed([1..n-1])) or r.special then
                Error("Right-power obstruction");fi;
            return false;
        fi;
        if not r.reason in ["failed_division","complete_coloring"] then Error("Unknown classification method");fi;
        checkfraction(r.word,r.fraction);colors:=List([1..n],j->[]);
        for position in [1..Length(r.fraction)] do
            a:=r.fraction[position];i:=AbsInt(a);pair:=colors{[i,i+1]};
            if a>0 then expected:=[shelf(pair[1],pair[2]),pair[1]];
            else
                test:=red(Concatenation(inv(pair[2]),pair[1],shift(pair[2]),[-1]));d:=unshift(test);
                if d=fail then
                    if r.reason<>"failed_division" or r.special or position-1<>r.failure_position or
                       Length(r.trace)<>position-1 or not equal(test,r.failed_shift_word) then Error("Failed division evidence");fi;
                    failedDivisions:=failedDivisions+1;return false;
                fi;
                expected:=[pair[2],d];
            fi;
            if position>Length(r.trace) then Error("Missing coloring step");fi;
            next:=r.trace[position];
            if next.position<>position-1 or Length(next.next_pair)<>2 or
               not ForAll([1,2],j->equal(expected[j],next.next_pair[j])) then Error("Coloring step equality");fi;
            colors[i]:=next.next_pair[1];colors[i+1]:=next.next_pair[2];colorSteps:=colorSteps+1;
        od;
        if r.reason<>"complete_coloring" or Length(r.trace)<>Length(r.fraction) or
           not ForAll([1..n],j->equal(colors[j],r.final_colors[j])) then Error("Complete coloring binding");fi;
        answer:=ForAll([2..n],j->equal(colors[j],[]));
        if answer and not equal(colors[1],r.word) then Error("Special output is not input");fi;
        if answer<>r.special then Error("Final coloring decision");fi;
        return answer;
    end;
    for record in B9FixedColor.controls do classify(record.classification);od;
    reversalChecks:=0;
    for record in B9FixedColor.reversal_controls do
        checkfraction(record.word,record.fraction);reversalChecks:=reversalChecks+1;
    od;
    productChecks:=0;
    for record in B9FixedColor.product_controls do
        actual:=delete(record.word,5,[1,2,3])[1];expected:=delete(record.h,5,[1,2,3])[1];
        if not equal(actual,record.parameter) or not equal(expected,record.tail) or
           not ForAll(expected,a->AbsInt(a)=2) or not equal(actual,Concatenation(record.A,expected)) then
            Error("Groupoid deletion product");fi;
        productChecks:=productChecks+1;
    od;
    good:=0;bad:=0;sols:=0;
    if List(B9FixedColor.records,r->r.source_index)<>[0..Length(B9Records)-1] then Error("Original first-color coverage");fi;
    for record in B9FixedColor.records do
        source:=B9Records[record.source_index+1][1];n:=record.ambient_rank;
        if not equal(record.word,source) or record.status<>"complete" or n<3 or
           ForAny(record.word,a->AbsInt(a)>=n) then Error("Input/scope binding");fi;
        actual:=delete(record.word,n,[1,2,3]);
        if not equal(actual[1],record.parameter) or actual[2]<>record.input_endpoint_labels then Error("Parameter deletion");fi;
        difference:=Concatenation(inv(record.word),actual[1]);base:=unshift(difference);
        if not equal(difference,record.difference) then Error("Shifted difference binding");fi;
        if base=fail then
            if record.reason<>"no_parabolic_factorization" or not IsEmpty(record.candidates) or
               not IsEmpty(record.solutions) then Error("Impossible factorization output");fi;
            bad:=bad+1;continue;
        fi;
        good:=good+1;
        if record.reason<>"finite_specialness_tests" or not equal(base,record.base_second) or
           List(record.candidates,r->r.power_index)<>[-eps(base)..n-2-eps(base)] then Error("Finite candidate coverage");fi;
        expected:=[];
        for r in record.candidates do
            k:=r.power_index;c:=Concatenation(base,ListWithIdenticalEntries(AbsInt(k),SignInt(k)));
            if not equal(c,r.word) or eps(c)<0 or eps(c)>n-2 then Error("Candidate coset or exponent");fi;
            if classify(r) then Add(expected,r);fi;
        od;
        if Length(expected)<>Length(record.solutions) then Error("Missing fibre answer");fi;
        for i in [1..Length(expected)] do
            r:=record.solutions[i];k:=expected[i].power_index;
            if k<>r.power_index or not equal(r.word,expected[i].word) or
               not equal(Concatenation(record.word,shift(r.word)),r.parameter_word) or
               not equal(r.parameter_word,Concatenation(actual[1],ListWithIdenticalEntries(AbsInt(k),2*SignInt(k)))) then
                Error("Solution parameter equality");fi;
            sols:=sols+1;
            if not action(I2(r.parameter_word)) in knownImages then Error("Additional parameter coset found");fi;
        od;
    od;
    if good+bad<>52 or good<>18 or bad<>34 or sols<>16 then Error("Decision totals");fi;
    Print("INPUTS=",good+bad," NO_FACTORIZATION=",bad," FACTORIZABLE=",good,
          " SECOND_COLORS=",sols," SPECIALNESS_CHECKS=",specialChecks,
          " COLOR_STEPS=",colorSteps," FAILED_DIVISIONS=",failedDivisions,
          " REVERSAL_CONTROLS=",reversalChecks," PRODUCT_CONTROLS=",productChecks,"\n");
    Print("PASS independent GAP B9 fixed color decisions\n");
end)();
QUIT;
