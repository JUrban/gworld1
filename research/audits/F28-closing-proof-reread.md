# F28 closing proof audit

30 September 2026, approximately 02:38--02:40 UTC. Same-agent closing
review; no new gap was identified. Novelty and specialist review remain
outstanding, and this is not a new candidate.

Read the full current proof, original audit and matrix Lean audit.
Reread the complete original free-group HTML, the F28 background link,
the GA5 statement and its background. Actually viewed the retained F28
statement image. GA5's normal-subgroup condition is weaker than F28's
arbitrary-subgroup condition and is not substituted for it.

The Schreier basis gives an actual index-two domain. The projective
ping-pong sets are strict for every nonzero integral power of A or B,
so the matrix representation is faithful. The three generator identities
include the minus sign in the third identity; passing to PSL removes it
without changing the conjugation map. The image index-two calculation
is valid in the free basis b,c with c=b-inverse a, although that extra
index condition is not required by the question.

If f(H) is contained in H, every positive iterate is defined for each
individual h in H. Its exact determinant-one rational conjugate has an
integral lift differing only by sign. Thus the invariant-energy argument
really applies to an infinite integral matrix sequence, without a
finite-generation, normality or equality f(H)=H hypothesis. The four
linear forms in the sum of squares recover all four entries with a
uniform integral bound. Repetition propagates back through invertible
conjugation and makes the initial matrix commute with a positive power.

The recurrence for Q-powers has an odd Q-coefficient for every positive
exponent; no scalar power is missed. Commutation therefore reduces to
c=-2b, d=a-b. The determinant-one form
(a-b/2) squared +7b squared/4 excludes every nonzero integral b and
leaves exactly plus or minus the identity. Faithfulness finishes the
argument element by element for arbitrary H.

The final Lean theorem has only the integral recurrence and initial
determinant hypotheses, rather than assuming boundedness or periodicity.
Its written free-group/PSL bridge remains outside Lean. No compilation or
finite enumeration was rerun: the existing successful checks were not
challenged by a changed source or new computational concern. No fresh
literature search or novelty conclusion is claimed in this pass.
