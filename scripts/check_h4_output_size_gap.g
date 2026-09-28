if LoadPackage("polycyclic")<>true then FORCE_QUIT_GAP(1);fi;
Read("research/certificates/H4-output-size/fixtures.g");
H4Fail:=function(message) Print("FAIL ",message,"\n");FORCE_QUIT_GAP(1);end;;
H4Main:=function()
    local H4Checked,H4Presentations,item,n,r,rels,M,Q,expected,x,inverseTwo,t,G,gens,rel,value,letter,F,fgens,frels,P;
H4Checked:=0;;H4Presentations:=0;;
for item in H4Fixtures do
    n:=item[1];r:=item[2];rels:=item[3];M:=item[4];Q:=item[5];expected:=item[6];
    if Q<>2^n or M<>2^Q-1 or expected<>M*Q then H4Fail("parameters");fi;
    if n>4 then continue;fi;
    Print("BEGIN H4 finite model ",n," order ",expected,"\n");
    x:=PermList(Concatenation([2..M],[1]));;
    inverseTwo:=(M+1)/2;;
    t:=PermList(List([0..M-1],z->(inverseTwo*z) mod M+1));;
    G:=Group(x,t);;gens:=Concatenation([x],List([0..n],i->t^(2^i)));;
    if Order(x)<>M or Order(t)<>Q or Size(G)<>expected then H4Fail("affine model order");fi;
    for rel in rels do
        value:=One(G);
        for letter in rel do value:=value*gens[AbsInt(letter)]^SignInt(letter);od;
        if value<>One(G) then H4Fail("defining relation");fi;
    od;
    if t*x*t^-1<>x^2 then H4Fail("action convention");fi;
    H4Checked:=H4Checked+1;
    if n<=3 then
        F:=FreeGroup(r);;fgens:=GeneratorsOfGroup(F);;
        frels:=List(rels,w->Product(w,a->fgens[AbsInt(a)]^SignInt(a)));;
        P:=F/frels;;
        if Size(P)<>expected then H4Fail("independent finitely presented group order");fi;
        H4Presentations:=H4Presentations+1;
    fi;
    Print("H4 MODEL VERIFIED ",n,"\n");
od;
Print("PASS H4 GAP: ",H4Checked," affine groups and ",H4Presentations,
      " independent presentation orders\n");
end;;
H4Main();
QUIT_GAP(0);
