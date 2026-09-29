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
cnf(def_003,axiom,(mul(c002,c001)=mul(mul(c001,c002),c003))).
cnf(def_004,axiom,(mul(c003,c001)=mul(mul(c001,c003),c004))).
cnf(def_005,axiom,(mul(c003,c002)=mul(mul(c002,c003),c005))).
cnf(def_006,axiom,(mul(c004,c001)=mul(mul(c001,c004),c006))).
cnf(def_007,axiom,(mul(c004,c002)=mul(mul(c002,c004),c007))).
cnf(def_008,axiom,(mul(c005,c002)=mul(mul(c002,c005),c008))).
cnf(rel_009,axiom,(mul(c004,c003)=mul(c003,c004))).
cnf(rel_010,axiom,(mul(c005,c003)=mul(c003,c005))).
cnf(rel_011,axiom,(mul(c006,c001)=mul(c001,c006))).
cnf(rel_012,axiom,(mul(c006,c002)=mul(c002,c006))).
cnf(rel_013,axiom,(mul(c007,c002)=mul(c002,c007))).
cnf(rel_014,axiom,(mul(c008,c002)=mul(c002,c008))).
cnf(goal,negated_conjecture,(mul(c006,c003)!=mul(c003,c006))).
