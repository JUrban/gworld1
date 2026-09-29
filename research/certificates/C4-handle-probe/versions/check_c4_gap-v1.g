# Independent direct interval scan and rewrite, with faithful Artin-action checks.
Read("research/certificates/C4-handle-probe/gap-fixtures.g");
C4Free := function(w)
    local out,a;
    out:=[];
    for a in w do
        if Length(out)>0 and out[Length(out)]=-a then Remove(out);
        else Add(out,a); fi;
    od;
    return out;
end;
C4First := function(w)
    local p,q,j,middle;
    for q in [2..Length(w)] do
        j:=AbsInt(w[q]);
        for p in Reversed([1..q-1]) do
            if w[p]=-w[q] then
                middle:=w{[p+1..q-1]};
                if ForAll(middle,a->not AbsInt(a) in [j-1,j]) then
                    return [p,q];
                fi;
            fi;
        od;
    od;
    return fail;
end;
C4Reduce := function(w,h)
    local p,q,j,e,middle,a,expanded,raw,out,signs;
    p:=h[1];q:=h[2];j:=AbsInt(w[p]);e:=SignInt(w[p]);
    signs:=Set(List(Filtered(w{[p+1..q-1]},a->AbsInt(a)=j+1),SignInt));
    if Length(signs)>1 then Error("Nonpermitted first handle"); fi;
    middle:=[];expanded:=0;
    for a in w{[p+1..q-1]} do
        if AbsInt(a)=j+1 then
            Append(middle,[-e*(j+1),SignInt(a)*j,e*(j+1)]);
            expanded:=expanded+1;
        else Add(middle,a); fi;
    od;
    raw:=Concatenation(w{[1..p-1]},middle,w{[q+1..Length(w)]});
    out:=C4Free(raw);
    return [out,[p,q,j,expanded,Length(raw),Length(out),(Length(raw)-Length(out))/2]];
end;
C4F:=FreeGroup(5);;C4x:=GeneratorsOfGroup(C4F);;
C4pos:=[];;C4neg:=[];;
for j in [1..4] do
    ys:=ShallowCopy(C4x);;ys[j]:=C4x[j]*C4x[j+1]/C4x[j];;ys[j+1]:=C4x[j];;
    Add(C4pos,GroupHomomorphismByImagesNC(C4F,C4F,C4x,ys));;
    ys:=ShallowCopy(C4x);;ys[j]:=C4x[j+1];;ys[j+1]:=C4x[j+1]^-1*C4x[j]*C4x[j+1];;
    Add(C4neg,GroupHomomorphismByImagesNC(C4F,C4F,C4x,ys));;
od;
C4Action:=function(w)
    local out,j,aut;
    out:=ShallowCopy(C4x);
    for j in Reversed(w) do
        if j>0 then aut:=C4pos[j];else aut:=C4neg[-j];fi;
        out:=List(out,a->Image(aut,a));
    od;
    return out;
end;
# Verify the algebraic substitution for both signs, and commuting/interverse controls.
for j in [1..4] do
    if C4Action([j,-j])<>C4x then Error("Inverse control"); fi;
    for k in [1..4] do
        if AbsInt(j-k)>1 and C4Action([j,k])<>C4Action([k,j]) then Error("Commutation control");fi;
    od;
od;
for j in [1..3] do
    for e in [-1,1] do for d in [-1,1] do
        if C4Action([e*j,d*(j+1),-e*j])<>C4Action([-e*(j+1),d*j,e*(j+1)]) then
            Error("Signed handle substitution control");fi;
    od;od;
od;
if C4Action([1])=C4Action([-1]) or C4Action([1,2])=C4Action([2,1]) then
    Error("Negative Artin controls");fi;
# Include empty and inverse-pair controls independently of exported examples.
if C4First([])<>fail or C4First([1,-1])<>[1,2] or
   C4Reduce([1,-1],[1,2])[1]<>[] then Error("Boundary control");fi;
nsteps:=0;;nactions:=0;;
for r in C4Fixtures do
    w:=C4Free(r[2]);;count:=0;;expanded:=0;;peakraw:=Length(w);;peak:=Length(w);;
    while C4First(w)<>fail do
        z:=C4Reduce(w,C4First(w));;w:=z[1];;count:=count+1;;
        if count>Length(r[8]) or z[2]<>r[8][count] then Error("Trace mismatch ",r[1]," ",count);fi;
        expanded:=expanded+z[2][4];;peakraw:=Maximum(peakraw,z[2][5]);;peak:=Maximum(peak,Length(w));;
    od;
    if [w,count,expanded,peakraw,peak]<>r{[3..7]} then Error("Summary mismatch ",r[1]);fi;
    if Length(r[2])<=16 then
        if C4Action(r[2])<>C4Action(w) then Error("Faithful action mismatch ",r[1]);fi;
        nactions:=nactions+1;
    fi;
    nsteps:=nsteps+count;
od;
Print("PASS C4 independent GAP replay: ",Length(C4Fixtures)," records, ",nsteps," steps, ",nactions," faithful Artin pairs; signed local rules and negative controls\n");
QUIT;
