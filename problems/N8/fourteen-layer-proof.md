# N8: fourteen final layers by one-parameter tails

29 September 2026. **Candidate argument under audit; not yet adopted in
the claims ledger.** The proposed scope is c-d<=13, where d is a nonzero
target's leading degree. Combined with the leading-degree-ten theorem,
this would cover all targets through class 24. General N8 remains separate.

Use the setup, finite integral leading-pair enumeration and homogeneous
kernel lemmas of the preceding proofs. For a normalized branch put
d=p+q, p<=q and n=c-d. Exceptions are the one-dimensional nonzero kernels
at offsets 0<t<q-p; they cannot be consecutive and have a nonzero quadratic
cokernel obstruction at 2t. Nielsen and later kernels have the already
constructed exact universal substitutions.

The existing `parametric-tail-proof.md` covers n<=9 and any branch whose
first remaining exception t>=3 satisfies n<=2t+3. It retains every later
coordinate jointly and does not require later exceptions to be separated.
The new discussion therefore only needs 10<=n<=13.

## 1. A polynomially parametrized linear tail

Suppose a pair x_T,y_T, T in Z, has polynomial integral Hall exponents and
agrees with the target g below degree d+s. Allow every still-free correction
on the first factor at weights >=p+s and on the second at weights >=q+s.
If 2s>n, the entire tail equation has the form

    P(T) z=b(T),       T,z integral.                 (1)

Indeed a term with one free increment from each factor has weight at least
d+2s. Two increments from just the first or second factor have respective
bounds d+p+2s and d+q+2s. All exceed c. Thus every remaining unknown occurs
linearly, including every later exceptional kernel direction. The relative
error lies in gamma_(d+s); since 2(d+s)>c, its Hall coordinates are obtained
by a fixed rational linear map from the truncated tensor coefficients.
Finite Hall collection therefore gives rational polynomial P,b.

The initial exponents may now be quadratic polynomials, so the earlier
linear-parameter interpolation bound cannot be reused without change.
For each varying Hall exponent f_i(T), let R_i=deg f_i and let w_i be its
Hall weight. Put rho=max_i(R_i/w_i), or zero for a constant family.
Every nonconstant occurrence of f_i has weight at least w_i and parameter
degree at most R_i. Products, inverses, and the truncated commutator
therefore have parameter degree <=floor(c*rho). Relative-error collection
in this abelian tail is linear, so the same bound holds for P,b. Symbolic
collection or one more integer sample than this proved bound determines
them exactly. This is a weight argument, not an observed interpolation fit.

The previously proved and audited one-parameter integer-linear decision
theorem solves (1), retaining all parameters and constructing a witness.
An injective homogeneous map is not required anywhere in this final tail.

## 2. First remaining exception at offset 3

Process offsets 1 and 2 by their isolated quadratic obstructions, retaining
all integral roots and kernel residues. If the next exception is t>=5,
n<=13<=2t+3 already gives the previous tail algorithm. Consider t=3.

If no exception occurs at 5, the separated block below 6 has only the
first exceptional parameter. Its nonzero quadratic at 6 fixes that
parameter to a finite set. Any new exception at 6 is retained. For each
choice, the next exception is >=6 and hence lies in the previous tail
range. If no exception remains, the universal finite-residue procedure
finishes the branch. This uses only the first separated-block step, not
an assertion that all subsequent exceptions are separated.

If an exception occurs at 5, the complete integral block through 5 has
at most two free parameters after any universal translations are quotiented.
Use exactly the lattice and torsion-coset construction in Sections 2--3 of
`two-exception-proof.md`, which concerns only this block. It does not depend
on what kernels occur after 6. A rank-zero/one quotient, a fixed first
parameter, or a vanishing second cokernel coefficient gives finitely many
choices for the first parameter. Coordinates below 5 are then fixed;
restart the full remaining problem at 5. The first remaining exception
is at least 5, so the old bound n<=2*5+3 applies, even with further kernels.
Discarding earlier higher-coordinate restrictions may duplicate solutions
but introduces no false positive: the whole target equation is solved again.

In the remaining rank-two case the offset-6 cokernel equation is

    q(T)+S B=0,       B!=0,

with q quadratic and B constant. One coordinate forces S to be a rational
polynomial in T; all other compatibility equations are retained. A nonzero
one gives a finite root set and is treated as above. Otherwise enumerate
all congruence classes making S and the chosen block coordinates integral.
Offset 6 is injective because offset 5 is exceptional. The constant-matrix
polynomial-family procedure retains every allowed residue and its unique
polynomial integral lift through 6. The resulting pair agrees with g
below degree d+7, and all its coordinates are polynomial in one integer
parameter. Every further unknown starts at offset 7. Since 14>n, Section 1
finishes the branch, including any third or later exceptional kernel.

## 3. First remaining exception at offset 4

Offset 5 is injective. At most one of 6 and 7 is exceptional. If neither
is, the first separated-block quadratic at 8 fixes the first parameter;
all later exceptions are >=8 and the old tail range suffices.

Otherwise the block below 8 has at most two exceptional parameters. Use
the same complete integer quotient construction. If the first parameter
is fixed, restart with the later exception, which is >=6, and apply the
old bound. The only remaining case again expresses the later parameter
S as a rational polynomial in T using a nonzero constant cokernel column.
Retain every residue that makes the chosen block integral.

Now keep **all** coordinates at offset 8 and above as free unknowns. The
pair from the block agrees with the target below d+8. Since 16>n, Section 1
decides the complete remaining system. In particular offset 8 may itself
be exceptional: no injectivity or exact universal substitution at 8 is
needed for this last linear-tail reduction. All remaining cokernel and
integer-lifting conditions are enforced by (1).

## 4. Scope and outstanding audit

These cases exhaust the first remaining exception. Finite initial choices
and exact substitutions preserve all solutions; every final integer
witness is checked by the original group equation. The proposal therefore
gives a terminating decision algorithm for n<=13, subject to the previously
credited structural dependencies and this new argument's audit.

For c<=24, either d<=10, covered in arbitrary class by the two-exception
theorem, or d>=11 and c-d<=13. Identity, abelian cases and targets outside
the derived subgroup are treated as before. General N8 and novelty remain
unresolved. The uniform branch algorithm is not implemented end to end.

Computational work should independently check a full three-exception range
and actual polynomial group tails beyond n=9, with the new degree bound.
The earlier failed perturbation must not be used as a surviving B!=0 group
branch. Finite group tests support the reductions but cannot replace this
all-rank proof or its inherited structural lemmas.
