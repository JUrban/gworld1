% F20, rank two; [u,v]=u^-1 v^-1 u v.
% Constants cNNN name Hall commutators; they are not variables.
% No relation of weight greater than the requested weight is assumed.
cnf(assoc,axiom,(mul(mul(X,Y),Z)=mul(X,mul(Y,Z)))).
cnf(left_id,axiom,(mul(one,X)=X)).
cnf(right_id,axiom,(mul(X,one)=X)).
cnf(left_inv,axiom,(mul(inv(X),X)=one)).
cnf(right_inv,axiom,(mul(X,inv(X))=one)).
cnf(inv_inv,axiom,(inv(inv(X))=X)).
cnf(inv_prod,axiom,(inv(mul(X,Y))=mul(inv(Y),inv(X)))).
cnf(inv_one,axiom,(inv(one)=one)).
cnf(def_003,axiom,(c003=mul(mul(inv(c002),inv(c001)),mul(c002,c001)))).
cnf(def_004,axiom,(c004=mul(mul(inv(c003),inv(c001)),mul(c003,c001)))).
cnf(def_005,axiom,(c005=mul(mul(inv(c003),inv(c002)),mul(c003,c002)))).
cnf(def_006,axiom,(c006=mul(mul(inv(c004),inv(c001)),mul(c004,c001)))).
cnf(def_007,axiom,(c007=mul(mul(inv(c004),inv(c002)),mul(c004,c002)))).
cnf(def_008,axiom,(c008=mul(mul(inv(c005),inv(c002)),mul(c005,c002)))).
cnf(rel_009,axiom,(mul(mul(inv(c004),inv(c003)),mul(c004,c003))=one)).
cnf(rel_010,axiom,(mul(mul(inv(c005),inv(c003)),mul(c005,c003))=one)).
cnf(rel_011,axiom,(mul(mul(inv(c006),inv(c001)),mul(c006,c001))=one)).
cnf(rel_012,axiom,(mul(mul(inv(c006),inv(c002)),mul(c006,c002))=one)).
cnf(rel_013,axiom,(mul(mul(inv(c007),inv(c002)),mul(c007,c002))=one)).
cnf(rel_014,axiom,(mul(mul(inv(c008),inv(c002)),mul(c008,c002))=one)).
cnf(goal,negated_conjecture,(mul(mul(inv(c005),inv(c004)),mul(c005,c004))!=one)).
