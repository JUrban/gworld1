# N8: a univariate parametric integer-lattice route through overlaps

29 September2026, developed approximately12:25--12:29UTC. **Unverified
new lead. No scope promotion from this note.** The current counted N8
scope is recorded in `problems/N8/exceptional-boundary-proof.md` and
the earlier proofs. No implementation or independent replay of this
parametric decision step exists yet.

## 1. Algebraic decision lemma to audit and implement

Given an integer polynomial matrix P(T) and polynomial vector b(T),
one should be able to decide

    exists t in Z, z in Z^n: P(t) z = b(t).             (1)

More strongly, the set of allowed t should be effectively eventually
periodic, with finitely many exceptional integer values. This is the
one-parameter *linear* problem, not arbitrary polynomial Diophantine
solvability. A proposed elementary argument follows.

Compute Smith normal form over Q[T], with unimodular polynomial matrices
U,V and U P V=diag(d_1,...,d_r,0). Keep the complete transformations, not
just invariant factors. Their determinants are nonzero constants. Set
beta=U b and exclude the finitely many integer roots of the nonzero d_i
for separate direct integer-lattice tests.

For rows j>r, beta_j(t)=0 is required. A nonzero such polynomial leaves
only finitely many integer roots to check. Otherwise the forced transformed
coordinates are y_i=beta_i(t)/d_i(t). Since z=V(t)y is integral,
y=V(t)^(-1)z has denominators dividing one fixed integer M, obtained from
the coefficients of V^(-1).

If some beta_i/d_i is not a polynomial over Q, polynomial division gives
q_i(T)+r_i(T)/d_i(T), deg r_i<deg d_i and r_i!=0. Clear the fixed denominators
of M*q_i. For sufficiently large |t|, the resulting nonzero proper fraction
has absolute value less than1 and cannot be an integer. Include a root bound
for r_i. Thus every possible t in this case lies in an explicit finite
interval, and can be checked by ordinary integer Smith/Hermite operations.

If every forced ratio is polynomial, use the polynomial particular vector
y_0 and the free transformed coordinates. An integral z necessarily has
free y coordinates in (1/M)Z. Write them l/M. Clear the constant coefficient
denominators in

    z = V(T)y_0(T) + V_free(T) l/M.

Integrality becomes a finite linear congruence modulo a fixed K. It depends
only on t mod K and l mod K. Enumerating these finite residues decides
which arithmetic progressions work and constructs witnesses. The finitely
many excluded rank-drop values are tested separately. This would prove (1).

Audit tasks: exact transformation/inverse computation over Q[T]; explicit
root/fraction bounds; rank-zero and rectangular matrices; no real/rational
root substitution for integer roots; periodic congruences with nonprimitive
steps; construction and verification of z; rejected/inconsistent controls.
It may be a standard parametric-arithmetic result, so investigate credit
before presenting it as new. The proof argument above needs a separate
written audit before use.

## 2. Application to the remaining commutator corrections

Let n=c-p-q. Suppose t is the first not-yet-fixed exceptional offset.
Its full integral layer solution is v+kK. By the consecutive-offset lemma,
A_(t+1) is injective. Solving the next layer jointly with k gives either
no solution, one point, or an integral affine line

    k=k_0+mT,   correction_(t+1)=v_0+T*J,  m!=0.

Earlier corrections are fixed. Apply these two actual Hall corrections.
All remaining coordinates start at offset s=t+2. If n<=2t+3, two of
these remaining corrections cannot interact in the commutator, since
2s>n; same-factor interactions are still later. Their interactions with
the retained parameter T merely make the linear columns polynomial in T.
The full exact remaining equations should therefore have the form (1),
after clearing fixed denominators of the Hall polynomials.

Unlike premature quadratic filtering, this keeps the later exceptional
parameters among the linear unknowns. In particular it does not discard
the offset5 parameter when processing the first overlap at t=3.

The weight bound q>=3p+t implies d=p+q>=t+4. Thus when n<=2t+3,
the varying commutator tail is abelian:2(d+t)>d+n. This helps justify
one simultaneous coordinate equation. One must still explicitly verify
the absence of products of two *remaining* unknowns in actual group Hall
coordinates; polynomial dependence on T alone is allowed.

If valid, this handles every first unresolved exceptional offset t>=3
when n<=9. Offsets1 and2 can already be finitely settled by their isolated
quadratic obstructions (their successors are injective), with exact
universal kernels handled by residues. The prospective consequence is
all ten final layers c-d<=9, and, with the new leading-degree-eight bound,
all targets in classes<=18. **These are prospective only, not counted.**

Next: implement/test the parametric integer-lattice lemma, independently
replay its positive and negative certificates; then implement actual
commutator branch fixtures with overlapping offsets3,5 and retained
parameter-dependent columns. Include cases outside the present class14
scope, prove completeness, and audit before changing any claim ledger.
