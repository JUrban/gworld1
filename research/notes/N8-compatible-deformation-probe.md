# N8: an early-compatible deformation with independent late obstructions

29 September 2026, approximately 14:55--14:58 UTC. A bounded Lie probe,
not a new solution, a group fixture, or a scope promotion.

The older suggested B!=0 perturbation of D=ad_a^4(e) failed at the first
successor equation. Here is a different example which clears that first
obstacle, but still does not absorb the quadratic obstruction.

Use the free Lie algebra on a,e of weights 1,4. Put E_i=ad_a^i(e), C=a,
D=E_6, and choose the fixed next component

    D_1=2[E_0,E_3]+3[E_1,E_2].

The first and second exceptional directions are

    U_3=E_0, V_3=-[E_0,E_5]+[E_1,E_4]-[E_2,E_3],
    U_5=E_2, V_5=-[E_2,E_5]+[E_3,E_4].

At the first successor, take U_4=0 and

    V_4=-2[E_0,[E_0,E_2]]+[E_1,[E_0,E_1]].

Jacobi gives [U_3,D_1]+[a,V_4]=0. Thus this perturbation, unlike the older
example, does not already force the first parameter at offset 4 in this
Lie model. In the bracket of

    a+T U_3+S U_5,
    D+D_1+T V_3+T V_4+S V_5,

the T and S terms through offset 5 cancel. The remaining offset-6 terms
apart from a fixed target residual and the new linear corrections are

    T^2 Q+S B,
    Q=[U_3,V_3], B=[U_5,D_1].

The full homogeneous map A_6 has domain L_7 plus L_16, of dimensions
1 and 10. A native GAP free-associative-algebra calculation, using every
Lyndon word in both domains, gives

    rank(A_6)=11,
    rank(A_6,Q)=12,
    rank(A_6,B)=12,
    rank(A_6,Q,B)=13.

So Q and B are independently nonzero in the cokernel. Projecting modulo
B leaves a nonzero quadratic coefficient in T; for any fixed target this
again forces finitely many T. This is not a surviving unbounded absorbed
quadratic branch. It does show that early compatibility and B!=0 alone
are insufficient to establish such a branch.

`scripts/probe_n8_compatible_absorption.g` verifies both kernel identities,
the explicit successor lift, and the complete rational ranks. The recorded
run `n8-compatible-absorption-probe-v1` passes in 2.026006 seconds with
empty stderr. This probe has one implementation, not two independent
implementations. No full group lift, integer period calculation or later
target equations were tested. None of the fourteen-layer proof relies on
this proposed example being an unbounded branch.

A useful next question is whether earlier compatibility systematically
forces the first quadratic obstruction to remain independent of all later
linear parameter columns. These two failed examples are not a proof of
that general statement. A systematic complete deformation calculation,
with all earlier equations retained, would be needed before proposing
such a stronger result.
