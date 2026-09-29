# A dependent would-be free generator cannot be moved independently.
if LoadPackage("nq")<>true then FORCE_QUIT_GAP(1);fi;
group:=NilpotentQuotient(FreeGroup(2),4);;
gens:=GeneratorsOfGroup(group);;
a:=gens[1];; b:=gens[2];;
z:=Comm(b,a);; d:=Comm(z,a);; e:=Comm(z,b);;
u:=Comm(d,a);; v:=Comm(d,b);; w:=Comm(e,b);;
kgens:=[a,z,d,e,u,v,w];;
subgroup:=Subgroup(group,kgens);;
images:=ShallowCopy(kgens);; images[3]:=d*u;;
if u=One(group) or d=One(group) then Error("Trivial negative control");fi;
if Comm(images[2],images[1])=images[3] then Error("Control relation unchanged");fi;
bad:=GroupHomomorphismByImages(subgroup,subgroup,kgens,images);;
if bad<>fail then Error("GAP accepted the dependent-generator substitution");fi;
identity:=GroupHomomorphismByImages(subgroup,subgroup,kgens,kgens);;
if identity=fail or not ForAll(kgens,x->Image(identity,x)=x) then
    Error("Identity control failed");
fi;
Print("PASS N8 weighted GAP negative: dependent substitution rejected; identity accepted\n");
QUIT;
