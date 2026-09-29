F2:=FreeGroup("a","b");; gg:=GeneratorsOfGroup(F2);;
F4:=FreeGroup("a1","b1","a2","b2");; xx:=GeneratorsOfGroup(F4);;
letters:=Concatenation(xx,List(xx,x->x^-1));;
layer:=[One(F4)];; words:=[];;
for k in [1..4] do
  next:=[];
  for w in layer do
    for s in letters do
      v:=w*s;
      if Length(v)=k then Add(next,v); fi;
    od;
  od;
  Append(words,next); layer:=next;
od;
if Length(words)<>3200 or Length(Set(words))<>3200 then Error("input ball"); fi;
pp:=gg[1]^5*gg[2]*gg[1]*gg[2]^2*gg[1];;
hh:=pp*gg[1]*gg[2]*pp^-1;;
checked:=0;;
for n in [1,2] do
  ims:=[gg[1],gg[2],hh^n*gg[1]*hh^-n,hh^n*gg[2]*hh^-n];
  phi:=GroupHomomorphismByImages(F4,F2,xx,ims);
  for w in words do
    if IsOne(Image(phi,w)) then Error("positive image killed"); fi;
    checked:=checked+1;
  od;
od;
for n in [1,2,7] do
  phi:=GroupHomomorphismByImages(F4,F2,xx,
    [gg[1],gg[2],gg[1]^n*gg[1]*gg[1]^-n,gg[1]^n*gg[2]*gg[1]^-n]);
  if not IsOne(Image(phi,xx[1]*xx[3]*xx[1]^-1*xx[3]^-1)) then Error("bad separator control"); fi;
od;
abelianControl:=AbelianGroup([0]);; z:=GeneratorsOfGroup(abelianControl)[1];;
for i in [-3..3] do
  for j in [-3..3] do
    if not IsOne(Comm(z^i,z^j)) then Error("abelian control"); fi;
  od;
od;
Print("PASS GA3 GAP ",checked," positive images; 3 bad separator controls; 49 abelian controls\n");
QUIT;
