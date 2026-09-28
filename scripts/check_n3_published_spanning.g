# Audit of the spanning assertion in GSW (2003), Proposition 3.5, p.232.
# This is not a counterexample to torsion-freeness or to problem N3.
if LoadPackage("nq")=fail then Error("nq unavailable"); fi;
SetInfoLevel(InfoWarning,0);

# Exact integer matrix witness. Commutator convention: x^-1*y^-1*x*y.
N3Unit := function(i,j)
    local m;
    m := IdentityMat(4,Integers);
    m[i][j] := 1;
    return m;
end;
a := N3Unit(2,3);; b := N3Unit(1,2);; c := N3Unit(3,4);;
w := Comm(b,a);; z := Comm(w,c);;
if w<>N3Unit(1,3) or z<>N3Unit(1,4) then
    Error("Matrix commutators differ from the claimed witness");
fi;
if Comm(w,a)<>One(w) or Comm(w,b)<>One(w) then
    Error("The two-generator image is not class two");
fi;
if z=One(z) or z[1][3]<>0 or z[1][4]<>1 then
    Error("Matrix separation failed");
fi;
Print("Integer matrices: [b,a]=I+E13, [[b,a],c]=I+E14;\n",
      "[[b,a],a]=[[b,a],b]=I. The E14 coordinate separates z from <w>.\n");

# Independent free nilpotent group calculation of the missing normal conjugate.
f := FreeGroup(3);; g := NilpotentQuotient(f,3);;
x := GeneratorsOfGroup(g){[1..3]};; w := Comm(x[2],x[1]);;
z := Comm(w,x[3]);;
k := NormalClosure(g,Subgroup(g,[w]));;
d := Subgroup(g,[w,Comm(w,x[1]),Comm(w,x[2])]);;
lcs := LowerCentralSeries(g);;
if not z in k or not z in lcs[3] or z in d then
    Error("Missing-conjugate separation failed in the free class-three group");
fi;
kd := Intersection(k,lcs[3]);; dd := Intersection(d,lcs[3]);;
if HirschLength(kd)<>3 or HirschLength(dd)<>2 then
    Error("Unexpected intersection ranks");
fi;
# Positive controls: listed commutators lie in both normal and ordinary subgroups.
for t in [Comm(w,x[1]),Comm(w,x[2])] do
    if not t in k or not t in d then Error("Listed-generator control failed"); fi;
od;
Print("Free rank-three class-three group: z in K intersect gamma3, z not in D;\n",
      "Hirsch ranks (K intersect gamma3,D intersect gamma3)=(3,2).\n");
Print("PASS N3 published spanning assertion counterexample\n");
QUIT;
