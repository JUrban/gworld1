# N8: a possible fourteen-final-layer extension

29 September 2026, approximately 14:21 UTC. **Unverified and uncounted.**
The current candidate is the two-exception theorem (leading degree <=10
in arbitrary class; with the old ten-final-layer result, class <=20).
This note suggests combining the new parameter elimination with the old
one-parameter linear-tail solver. It is not an adopted scope change.

Let n=c-p-q<=13. As before, process exceptional offsets 1 and 2 by their
isolated quadratic obstructions. If the first remaining exception t>=5,
the existing condition n<=2t+3 already suffices. The only new cases are
t=3 and t=4.

For t=3, before its first quadratic at 6 there can be only one other
exception, at 5. If none occurs, the first parameter is fixed by the
usual quadratic, and every later first exception has offset at least 6.
If 5 occurs, use the full two-parameter block through offset 5. A fixed
first parameter leaves the later exception at offset at least 5, already
inside the old one-parameter-tail range. In the unbounded case, q(T)+S B=0
with B!=0 expresses S polynomially in T. Offset 6 is injective because
offset 5 is exceptional. Its unique coordinates are therefore polynomial
in T after all divisibility residues are retained. Every remaining unknown
starts at offset 7. Since 2*7>13, the whole remaining group tail is linear
over the one parameter T and can be decided by the existing P(T)z=b(T)
algorithm, irrespective of how many further homogeneous kernels occur.

For t=4, there is at most one additional exception among 5,6,7: offset 5
is injective, and 6,7 cannot both be exceptional. Use the full block below
offset 8. Finite first-parameter cases restart at an exception >=6, where
the old tail bound suffices. If the later parameter is eliminated as a
polynomial in T, retain every coordinate at offset 8 and above as unknown.
Their interactions start at offset 16>13. It should therefore be possible
to use the same complete one-parameter linear-tail solver without requiring
the offset-8 kernel to be universal or injective. The block pair need only
agree with the target below offset 8.

This would cover n<=13, and hence class <=24 when combined with leading
degree <=10. Points still requiring a full proof/audit:

- Make the fixed-parameter restart precise when additional exceptional
  offsets remain; the current two-exception theorem assumes no others.
- Retain every integer residue when S(T) and the injective offset-6 lift
  have rational coefficients, including rank-zero/one block quotients.
- Reprove polynomial degree bounds for the new family, whose already fixed
  coordinates can now be quadratic or higher in T.
- Check the entire actual group tail, not only the first obstruction;
  supply an independent fixture with at least three exceptional offsets.

A genuine three-exception leading pattern is suggested by generators a,e
of weights 1,4, E_i=ad_a^i(e), C=a, D=E_6 (weight 10). The identities are

    U_3=E_0, V_3=-[E_0,E_5]+[E_1,E_4]-[E_2,E_3],
    U_5=E_2, V_5=-[E_2,E_5]+[E_3,E_4],
    U_7=E_4, V_7=-[E_4,E_5].

Jacobi telescoping gives [U_i,D]+[C,V_i]=0 in each case. These explicit
identities have not been computationally checked in this new note, nor
has the full kernel range or any group fixture been constructed. They
describe a test to perform, not a class-24 certificate.
