# Driver for export or replay. Set N5InputMode and N5InputOutput before Read.
Read("scripts/n5_class2_input.g");
Read("research/certificates/N5-class2-mixed/v1/certificate.g");
if not IsBound(N5InputSolutions) then N5InputSolutions:=[];fi;
N5InputPresentation:=function(data,redundant)
    local r,s,n,f,x,rels,i,j,k,w,old,new,ng;
    r:=Length(data.quotient_orders);s:=Length(data.center_orders);n:=r+s;
    f:=FreeGroup(n);x:=GeneratorsOfGroup(f);rels:=[];
    for i in [1..n] do for j in [i+1..n] do
        w:=Comm(x[i],x[j]);
        if j<=r then for k in [1..s] do w:=w*x[r+k]^-data.beta[i][j][k];od;fi;
        Add(rels,w);
    od;od;
    for i in [1..s] do if data.center_orders[i]>0 then
        Add(rels,x[r+i]^data.center_orders[i]);fi;od;
    for i in [1..r] do if data.quotient_orders[i]>0 then
        w:=x[i]^data.quotient_orders[i];
        for k in [1..s] do w:=w*x[r+k]^-data.powers[i][k];od;
        Add(rels,w);
    fi;od;
    if redundant then
        new:=FreeGroup(n+1);ng:=GeneratorsOfGroup(new);old:=ng{[1..n]};
        if n>1 then old[1]:=old[1]*old[2]^2;fi;
        rels:=List(rels,w->MappedWord(w,x,old));
        Add(rels,ng[n+1]^-1*N5InputWord(new,old,List(old,w->1)));f:=new;
    fi;
    return f/rels;
end;

N5InputModels:=function()
    local out,item,p,m,variant,name,f;
    out:=[];
    for item in N5MixedFixtures do
        for variant in [false,true] do
            if variant and not item.name in ["trivial","C6","Q8_Z","G2","H3_D8_sheared","center_glue2"] then continue;fi;
            name:=item.name;if variant then name:=Concatenation(name,"_redundant");fi;
            Print("converting ",name,"\n");
            p:=N5InputPresentation(item.result,variant);m:=N5FpClassTwo(p,true);
            Add(out,rec(name:=name,expected:=item.expected,model:=m));
        od;
    od;
    f:=FreeGroup(1);p:=f/[];
    Add(out,rec(name:="Z",expected:=false,model:=N5FpClassTwo(p,true)));
    return out;
end;

N5InputJson:=function(x)
    local keys;
    if IsBool(x) or IsInt(x) then return String(x);fi;
    if IsString(x) and Length(x)>0 then
        return Concatenation("\"",ReplacedString(ReplacedString(x,"\\","\\\\"),"\"","\\\""),"\"");
    fi;
    if IsList(x) then return Concatenation("[",JoinStringsWithSeparator(List(x,N5InputJson),","),"]");fi;
    if IsRecord(x) then
        keys:=RecNames(x);Sort(keys);
        return Concatenation("{",JoinStringsWithSeparator(List(keys,k->
            Concatenation(N5InputJson(k),":",N5InputJson(x.(k)))),","),"}");
    fi;
    Error("unsupported JSON value");
end;

N5InputMain:=function()
    local models,out,item,m,data,a,b,u,v,k,i,arith,records,count,positive,
          source,relators,words,answer,found,stream,g,pcf,invalid,f,x;
    models:=N5InputModels();out:=[];count:=0;positive:=0;
    # Native class-three input is rejected, and fp input without the
    # promise returns fail before invoking nq.
    f:=FreeGroup(2);x:=GeneratorsOfGroup(f);
    g:=Image(NqEpimorphismNilpotentQuotient(f/[],3));
    if N5ClassTwoCoordinates(g)<>fail or N5FpClassTwo(f/[],false)<>fail then
        Error("input boundary rejection failed");fi;
    for item in models do
        m:=item.model;data:=m.data;
        if N5InputMode="export" then
            arith:=[];source:=GeneratorsOfGroup(m.presentation);
            for k in [1..10] do
                a:=N5InputWord(m.presentation,source,List([1..Length(source)],i->(i*k+2) mod 7-3));
                b:=N5InputWord(m.presentation,source,List([1..Length(source)],i->(i+2*k) mod 5-2));
                u:=Image(m.epimorphism,a);v:=Image(m.epimorphism,b);
                Add(arith,rec(a:=m.encode(u),b:=m.encode(v),product:=m.encode(u*v),
                    inverse:=m.encode(u^-1),exponent:=k-6,power:=m.encode(u^(k-6))));
            od;
            relators:=List(RelatorsOfFpGroup(m.presentation),ExtRepOfObj);
            records:=rec(name:=item.name,expected:=item.expected,data:=data,arithmetic:=arith,
                fp_generators:=Length(source),fp_relators:=relators,
                source_generator_coordinates:=List(source,w->m.encode(Image(m.epimorphism,w))),
                used_cyclic_abelianization:=m.used_cyclic_abelianization);
            Add(out,records);
        else
            found:=Filtered(N5InputSolutions,r->r.name=item.name);
            if Length(found)<>1 then Error("solution identity");fi;
            answer:=found[1].result;
            if answer.answer<>item.expected or answer.quotient_orders<>data.quotient_orders or
               answer.center_orders<>data.center_orders or answer.beta<>data.beta or
               answer.powers<>data.powers then Error("solution input binding");fi;
            if answer.answer then
                words:=N5InputFactors(m,answer);positive:=positive+1;
                Add(out,rec(name:=item.name,factor_words:=List(words.words,ws->
                    List(ws,w->ExtRepOfObj(UnderlyingElement(w))))));
            fi;
        fi;
        count:=count+1;
        Print("checked ",item.name," mode=",N5InputMode,"\n");
    od;
    stream:=OutputTextFile(N5InputOutput,false);SetPrintFormattingStatus(stream,false);
    PrintTo(stream,N5InputJson(rec(records:=out,models:=count,positive_factors:=positive,
        invalid_controls:=2)),"\n");CloseStream(stream);
    Print("PASS N5 input ",N5InputMode,": ",count," models, ",positive," positive factors\n");
end;
N5InputMain();
QUIT;
