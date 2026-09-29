# M0: the Jacobian criterion in the stated convention, with inverse words

29 September 2026, approximately 23:46–23:57 UTC. This supplements the
[existing M0 proof](proof.md). It checks the precise classical dependency
and supplies a direct constructive derivation in the proof's left-Fox,
column-matrix convention. The criterion is Bachmuth's prior theorem, not a
new result of this experiment. The M0 candidate and its novelty status are
unchanged.

## 1. The primary statement and the convention conversion

Reread Gupta–Gupta–Roman'kov, *Primitivity in Free Groups and Free Metabelian
Groups* (1992), the introduction and Lemma1 on printed p.517, and viewed
that archived page again. The lemma states the square Jacobian basis
criterion for a finite-rank free metabelian group. It does not assert that
an arbitrary single unimodular column is primitive. The source uses right
Fox derivatives and a matrix whose rows correspond to the proposed basis.
The archived PDF has SHA256
`dc3536e389c00979ada4b283fe4367dfe70fc47a1e2033b05f9846e03e587459`.

Here is the exact conversion. Put R=Z[X1^±1,...,Xn^±1], and let iota be
its involution Xi -> Xi^-1. Write d_i for the left derivative and r_i for
the source's right derivative. For any word w,

    r_i(w) = bar(w) Xi^-1 iota(d_i(w)).                    (1)

Both sides equal delta_ij on a generator xj and satisfy the right product
rule r_i(uv)=r_i(u)bar(v)+r_i(v). This proves (1), including inverses.
For generator images w1,...,wn, if J has their left columns and J_R has
the right rows, then

    J_R = diag(bar(w1),...,bar(wn)) iota(J)^t
                                      diag(X1^-1,...,Xn^-1). (2)

All diagonal factors are units. Thus the invertibility criteria are
exactly equivalent, also before the IA normalization. No field evaluation
or commutative approximation beyond the prescribed abelianized Fox ring
is involved in this conversion.

## 2. Integral flows give the full Magnus image

Here is a direct proof of the criterion's sufficiency, avoiding a further
black-box use of the source's derivative convention. Let F have free basis
x1,...,xn and let Gamma be the Cayley graph of Z^n in that basis. A word
w lifts to a path from 0 to its exponent vector e(w). Its signed integral
edge chain has components exactly D(w): the coefficient of X^v in d_i(w)
is the net number of traversals of the directed edge v -> v+e_i.

The map

    w -> (bar(w),D(w)),
    (X^a,u)(X^b,v)=(X^(a+b),u+X^a v)                     (3)

has kernel F''. To see this directly, a word in its kernel first has
zero exponent vector, so is a loop in Gamma. The graph is the covering
of the basis rose corresponding to F', and its fundamental group is F'.
The signed edge-chain map of loops is the abelianization map to H1(Gamma,Z).
A zero chain is therefore exactly an element of [F',F']=F''. This also
proves the converse. Thus (3) is faithful on M_n=F/F''.

Its image consists of **all** pairs (X^a,v) satisfying

    lambda v = X^a-1,       lambda=(X1-1,...,Xn-1).       (4)

Necessity is the boundary formula. For sufficiency, choose the canonical
coordinate path p from 0 to a. The finite chain c=v-D(p) has zero boundary.
Reverse edges with negative coefficients, keeping positive multiplicities.
This is a finite balanced directed multigraph. Successively follow edges
until returning to the starting vertex, subtract that closed trail, and
repeat. Balance prevents getting stuck elsewhere. This terminates in
finitely many integral closed trails, possibly in disconnected components.

For each trail choose a coordinate path q from 0 to its starting vertex.
The based word q(trail)q^-1 has exactly that trail's signed chain: the two
connector chains cancel. Multiply these based loops and then p. The
resulting word has exponent vector a and chain v. This proves (4) without
assuming that the original support was connected.

This is a terminating construction over the integers. If c has total
absolute coefficient sum N, and all its incident vertices have l1 distance
at most B from 0, the constructed word has length at most
||a||_1+N(1+2B), before free reduction. Put B=0 if N=0. This is a size bound,
not a practical complexity assertion for the preceding matrix inversion.

## 3. Constructing an inverse from an invertible IA Jacobian

Suppose phi is IA and J=J_phi is invertible over R. The Fox identity is
lambda J=lambda, so lambda J^-1=lambda. For each column v_j of J^-1,

    lambda v_j=Xj-1.

By (4) construct a word u_j with abelianization Xj and derivative v_j.
The substitution psi(xj)=u_j is an endomorphism of M_n by its defining
universal property. It is IA and J_psi=J^-1. The left Fox chain rule gives

    J_(phi after psi)=J J^-1=I,
    J_(psi after phi)=J^-1 J=I.

Both compositions have the identity abelianization. Faithfulness in (3)
therefore makes both compositions the identity on every generator of M_n.
This constructs an actual inverse, rather than only recognizing a unit
determinant.

For completeness, the general square criterion follows as well. If phi
is an automorphism with inverse psi, then
I=J_phi bar(phi)(J_psi). Taking determinants over the commutative ring R
makes det(J_phi) a unit. Conversely, if J_phi is invertible, its augmentation
is a unimodular integer matrix B. Lift B^-1 to a free-group automorphism
beta. Then beta after phi is IA with invertible Jacobian, since bar(beta)
is a ring automorphism. Apply the preceding construction. If u is the
inverse of beta after phi, the inverse of phi is u after beta.

The primitive-column consequence used in the M0 proof follows already
from the necessary direction: a primitive word is one column of a basis
Jacobian, and a column of an invertible matrix cannot evaluate to zero
under a ring homomorphism to a field. No converse for a single column is
introduced. The finite-field primitive-detection argument remains the
controlling candidate-specific step.

## 4. Implementation and a free-group boundary control

`scripts/m0_flow_inverse.py` implements the IA normalization, exact Laurent
adjugate inversion, integral trail decomposition, word realization and
undoing of the normalization. It shares only the existing experiment's
integer polynomial/word primitives and normalization code. No Kourovka
argument or implementation is imported.

The check has16 deterministic input maps in ranks0–4. Cases include signed
Laurent exponents, nonzero disconnected cycles, multiple corrected
coordinates, compositions, and independent changes of basis in domain and
range. Three additional flow fixtures explicitly combine disconnected
cycles with signed multiplicities and nonzero endpoints. An invalid boundary
and an IA nonunit Jacobian are rejected. The largest inverse-generator
word in this suite has85 letters; no arbitrary-input size bound is inferred
from these examples.

The following example makes the distinction from free-group inversion
concrete. In F=<x,y,z>, let c=[y,z]=yzy^-1z^-1 and put

    phi(x)=x^2 c x^-1,    phi(y)=y,    phi(z)=z.

Its left Jacobian is I+X^2 D(c)e1^t. Since the first entry of D(c) is zero,
the added matrix squares to zero and the inverse is I-X^2 D(c)e1^t.
Thus on M_3 it has inverse given by x -> x^2 c^-1 x^-1, with y,z fixed.

The displayed map on F itself is not surjective. Map its generators to

    x=(1,2,3),     y=(3,4),     z=(2,3)

in S4, using right-action permutations. These generate S4, whereas all
three images of phi fix1 and generate only its S3 stabilizer. Hence
phi(F) is proper. This does **not** show that the induced metabelian
automorphism is wild: a different free-group lift could induce it. Nor
does a returned inverse pair failing free reduction prove that its input
map has no different inverse in F. The S4 obstruction is the proof for
this particular displayed free lift.

## 5. Independent replay, scope and retained evidence

The separate GAP checker uses native free words and exact affine matrices
over multivariate rational-function fields. Word-derived entries have
integral Laurent coefficients, so equality here faithfully checks their
integer Laurent equality. It verifies all84 generator compositions in both
orders in the Magnus representation, all free normalization identities,
and the assembly of the final inverse. Ten returned map/inverse pairs
fail literal free-group composition, while all pass the metabelian check.
Those ten are not claimed to be ten wild automorphisms.

GAP also reconstructs the three signed-flow certificates, verifies the
nonunit/incorrect-boundary controls, and verifies the S4-to-S3 obstruction.
A second GAP version adds84 exact left/right derivative conversions using
upper-row and lower-column affine matrices and equation(1). It did not
increase the input bounds. Both versions and outputs are retained.

Three recorded jobs, each one CPU,6GB per-process address-space cap,
180s timeout, all terminal with empty stderr:

| Run | Result |
| --- | --- |
| m0-flow-inverse-python-v1 | Passed in0.42s |
| m0-flow-inverse-gap-v1 | Passed in5.19s; inverse/flow/boundary scope |
| m0-flow-inverse-gap-v2 | Passed in5.99s; includes the new convention check |

The output paths are versioned and scripts refuse to overwrite generated
certificates. Use a fresh output directory/path and recorded-run name for
regeneration. The exact constructor, check sources, shared dependencies,
input/output data, primary page and all raw logs are bound by
`research/certificates/M0-flow-inverse/manifest-v1.json`.

The universal graph argument above supplies faithfulness and sufficiency;
finite matrix checks are not a substitute for it. This is an audit and a
constructive replay of a classical ingredient, not an independent specialist
review or a new novelty claim. The candidate count and original deadline
are unchanged.
