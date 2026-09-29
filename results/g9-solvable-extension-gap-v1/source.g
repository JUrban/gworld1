# Native Magnus rows for the metabelian deck group; exact outer edge flows.
Read("research/certificates/G9-solvable-extension/fixtures.g");;
G9SFail:=function(s) Print("FAIL ",s,"\n");FORCE_QUIT_GAP(1);end;;
G9SCheck:=function()
    local rank,t,one,mon,mul,inv,refl,letter,fromdata,clean,add,wordflow,
          height,endpoint,translate,reflectedges,decode,geometry,fixtures,
          recd,w,u,spans,g,h,parse,checks,control,zero,expected;
    checks:=0;
    for rank in [2,3] do
        t:=List([1..rank],i->Indeterminate(Rationals,i));
        one:=Concatenation([One(t[1])],List(t,x->Zero(x)));
        mon:=p->Product([1..rank],j->t[j]^p[j]);
        mul:=function(g,h)
            return Concatenation([g[1]*h[1]],g{[2..rank+1]}+g[1]*h{[2..rank+1]});
        end;
        inv:=g->Concatenation([1/g[1]],-g{[2..rank+1]}/g[1]);
        refl:=function(g)
            local q,subs;subs:=ShallowCopy(t);subs[1]:=1/t[1];
            q:=List(g,x->Value(x,t,subs));q[2]:=-q[2]/t[1];return q;
        end;
        letter:=function(s)
            local q,j;q:=ShallowCopy(one);j:=AbsInt(s);
            if s>0 then q[1]:=t[j];q[j+1]:=One(t[1]);
            else q[1]:=1/t[j];q[j+1]:=-1/t[j];fi;return q;
        end;
        fromdata:=function(g)
            local q,e;q:=Concatenation([mon(g[1])],List(t,x->Zero(x)));
            for e in g[2] do q[e[2]+2]:=q[e[2]+2]+e[3]*mon(e[1]);od;
            return q;
        end;
        clean:=function(edges)
            local result;result:=Filtered(edges,e->e[3]<>0);Sort(result);return result;
        end;
        add:=function(edges,p,j,c)
            local k;k:=PositionProperty(edges,e->e[1]=p and e[2]=j);
            if k=fail then Add(edges,[p,j,c]);else edges[k][3]:=edges[k][3]+c;fi;
        end;
        wordflow:=function(w)
            local p,edges,s,j;p:=one;edges:=[];
            for s in w do
                j:=AbsInt(s);
                if s<0 then p:=mul(p,letter(s));fi;
                add(edges,p,j,SignInt(s));
                if s>0 then p:=mul(p,letter(s));fi;
            od;
            return [p,clean(edges)];
        end;
        parse:=function(g)
            return [fromdata(g[1]),clean(List(g[2],e->[fromdata(e[1]),e[2]+1,e[3]]))];
        end;
        height:=function(p)
            local v,h,n;v:=Value(p[1],t,Concatenation([2],List([2..rank],i->1)));h:=0;n:=0;
            while v<>1 do
                if v>1 then v:=v/2;h:=h+1;else v:=2*v;h:=h-1;fi;
                n:=n+1;if n>1000 then G9SFail("nonmonomial height");fi;
            od;return h;
        end;
        endpoint:=function(edges,start)
            local keys,counts,put,e,nz;
            keys:=[];counts:=[];
            put:=function(p,c)
                local i;i:=Position(keys,p);
                if i=fail then Add(keys,p);Add(counts,c);else counts[i]:=counts[i]+c;fi;
            end;
            for e in edges do put(e[1],-e[3]);put(mul(e[1],letter(e[2])),e[3]);od;
            put(start,1);nz:=Filtered([1..Length(keys)],i->counts[i]<>0);
            if Length(nz)<>1 or counts[nz[1]]<>1 then G9SFail("noncommutative endpoint");fi;
            return keys[nz[1]];
        end;
        translate:=function(edges,p)
            return List(edges,e->[mul(p,e[1]),e[2],e[3]]);
        end;
        reflectedges:=function(edges)
            local result,e,p,c;result:=[];
            for e in edges do
                p:=refl(e[1]);c:=e[3];
                if e[2]=1 then p:=mul(p,letter(-1));c:=-c;fi;
                add(result,p,e[2],c);
            od;return clean(result);
        end;
        decode:=function(g,spans)
            local old,new,lo,hi,sign,out,span,chunk,finish,delta,piece,e,upper;
            old:=one;new:=one;lo:=0;sign:=1;out:=[];
            upper:=function(e)
                if e[2]=1 then return height(e[1])+1;else return height(e[1]);fi;
            end;
            for span in spans do
                hi:=lo+span;chunk:=Filtered(g[2],e->lo<upper(e) and upper(e)<=hi);
                finish:=endpoint(chunk,new);
                if height(finish)<>hi then G9SFail("chunk endpoint height");fi;
                delta:=mul(inv(new),finish);piece:=translate(chunk,inv(new));
                if sign=-1 then delta:=refl(delta);piece:=reflectedges(piece);fi;
                for e in translate(piece,old) do add(out,e[1],e[2],e[3]);od;
                old:=mul(old,delta);new:=finish;lo:=hi;sign:=-sign;
            od;
            if new<>g[1] or ForAny(g[2],e->upper(e)<=0 or upper(e)>lo) then G9SFail("outer support");fi;
            return [old,clean(out)];
        end;
        geometry:=function(w)
            local h,s;h:=[0];
            for s in w do
                if AbsInt(s)=1 then Add(h,Last(h)+SignInt(s));else Add(h,Last(h));fi;
            od;return h;
        end;
        fixtures:=Filtered(G9SolvableFixtures,r->r[1]=rank);
        if mul(letter(1),letter(2))=mul(letter(2),letter(1)) then G9SFail("commutative deck collapse");fi;
        for recd in fixtures do
            w:=recd[3];u:=recd[4];spans:=recd[5];g:=wordflow(w);h:=wordflow(u);
            if recd[2]<>3 or g<>parse(recd[6]) or h<>parse(recd[7]) then G9SFail("native outer flow");fi;
            if decode(h,spans)<>g then G9SFail("noncommutative flow recovery");fi;
            if Length(w)<>Length(u) or ForAny(geometry(w){[2..Length(w)+1]},x->x<=0) or
               ForAny(geometry(u){[2..Length(u)+1]},x->x<=0) or Maximum(geometry(u))<>Sum(spans) or
               Last(geometry(u))<>Sum(spans) or ForAny([1..Length(spans)-1],i->spans[i]<=spans[i+1]) then G9SFail("geometry");fi;
            checks:=checks+1;
        od;
        if rank=2 then
            for control in G9SolvableRelations do
                g:=wordflow(control[2]);
                if control[1]=1 and (g[1]=one or g[2]=[]) then G9SFail("first derived control");fi;
                if control[1]=2 and (g[1]<>one or g[2]=[]) then G9SFail("second derived control");fi;
                if control[1]=3 and (g[1]<>one or g[2]<>[]) then G9SFail("third derived relation");fi;
            od;
        fi;
    od;
    Print("native_metabelian_deck_recoveries=",checks," derived_controls=",Length(G9SolvableRelations),"\n");
    Print("PASS G9 SOLVABLE FLOWS GAP\n");
end;;
G9SCheck();;
QUIT;
