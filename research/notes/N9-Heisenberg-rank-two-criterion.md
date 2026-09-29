# N9: an integral rank-two criterion for a two-generator nonabelian retract

29 September2026. Structural reduction and restricted examples, not a
decision procedure for the full fixed-ambient problem N9(a). No new
solution count or novelty assertion. No Kourovka material is used.

Let G be a finitely generated torsion-free group of class at most two,
written in central-extension coordinates

    x1,...,xd, z1,...,zs,
    [xi,xj] = product_l zl^(B_l[i,j]),    [xi,zl]=[zl,zm]=1.

The B_l are fixed integral alternating d-by-d matrices. Every element
has a unique normal form x1^a1 ... xd^ad z1^g1 ... zs^gs. Such a
presentation exists by choosing a basis of Z(G) and lifts of a basis
of G/Z(G); the latter is torsion-free. More generally the argument
works for any presentation of the displayed form with unique normal
coordinates, even if the listed z's are a smaller central subgroup.
Our commutator is [a,b]=a^-1 b^-1 a b.

Let h1=x^alpha z^gamma and h2=x^beta z^delta not commute, and put

    H=<h1,h2>,       c=[h1,h2]=z^q,
    q_l=alpha^T B_l beta.

Then H is an integral Heisenberg group on h1,h2. Indeed every word
collects as h1^a h2^b c^t. Commuting a supposed relation with h1 and
h2 forces a=b=0, since c has infinite order, and then t=0.

**Criterion.** H is a retract of G if and only if there is an integer
vector lambda in Z^s such that

    lambda dot q = 1,
    rank_Q M(lambda) = 2,        M(lambda)=sum_l lambda_l B_l.    (1)

In particular, the central coordinates gamma,delta of the two generators
do not affect the existence of a retraction. The dependence on their
noncentral coordinates is through the central commutator vector q.

## Necessity

Let r:G->H fix H. Since z_l is central in G and r is onto H,
r(z_l) lies in Z(H)=<c>. Write r(z_l)=c^lambda_l and

    r(x_i)=h1^u_i h2^v_i c^t_i.

Preservation of the commutator relations gives

    M(lambda)[i,j]=u_i v_j-v_i u_j.                              (2)

Fixing c gives lambda dot q=1. Therefore M(lambda) is nonzero
and has rank exactly two. These are integral equations: replacing
lambda by an arbitrary rational vector would lose a necessary condition.

## Sufficiency, including the integer central corrections

Assume (1). Set

    u_i=e_i^T M beta,       v_i=alpha^T M e_i.

These are integers. Since alpha^T M beta=1, alternatingness gives

    alpha dot u=1,   alpha dot v=0,
    beta dot u=0,    beta dot v=1.                              (3)

A rank-two alternating form is determined by this normalized pair on
the quotient by its radical. Consequently M[i,j]=u_i v_j-v_i u_j.
Equivalently, this identity follows by applying its vanishing four-by-four
Pfaffians to alpha,beta,e_i,e_j and using M(alpha,beta)=1.

For a vector a in Z^d define the integer polynomial

    Q(a)=sum_i binom(a_i,2) u_i v_i
          +sum_(i<j) a_i a_j v_i u_j.

The binomial expression a_i(a_i-1)/2 is integral also for negative a_i.
Put

    A=Q(alpha)-gamma dot lambda,
    D=Q(beta)-delta dot lambda,
    t_i=A u_i+D v_i.                                         (4)

Define r(z_l)=c^lambda_l and r(x_i)=h1^u_i h2^v_i c^t_i.
Equation(2) verifies every defining commutator relation, and all central
relations hold, so this assignment is a homomorphism to H.

For completeness, multiplication in H coordinates is

    (a,b,t)(a',b',t')=(a+a', b+b', t+t'-a'b).

Thus the central coordinate obtained by substituting r(x_i) into x^a
is a dot t-Q(a). Equations(3)--(4) show that the images of h1,h2
have respectively coordinates(1,0,0) and(0,1,0). Hence r fixes them
and is a retraction. In particular, no unresolved central divisibility
condition is hidden after solving(1): the integral vectors u,v already
give a right inverse for the two-row matrix with rows alpha,beta.

## A completely decidable special case

Take G to be a finite direct product of k integral Heisenberg groups,
with factor generators a_j,b_j and central generators z_j=[a_j,b_j].
Then B_j is the standard alternating block in factor j, and

    rank M(lambda)=2 times the number of nonzero lambda_j.

For a noncommuting pair h1,h2, criterion(1) is therefore equivalent to

    q_j=+1 or -1 for at least one j,                           (5)

where q_j is the determinant of the two abelian coordinate vectors
in factor j. Formula(4) explicitly constructs the retraction whenever
this happens. This decides this two-generator nonabelian case for
arbitrarily many factors; it is not asserted to decide arbitrary
subgroups of arbitrary fixed nilpotent groups.

For example, in the product on a,b and d,e, put

    h1=a^2 d^3,     h2=b e.

Their commutator has central vector(2,3), which is primitive, and the
two abelian coordinate vectors span a primitive rank-two lattice (their
two-by-two minors include2 and3). Nevertheless H is not a retract:
neither coordinate of q is a unit, so(5) fails. A Bézout solution such
as lambda=(-1,1) satisfies lambda dot q=1 but gives a rank-four form.
Thus primitive abelian image and primitive central commutator do not
together suffice.

Two further transparent obstructions distinguish the rank condition.
If G has four noncentral generators and one central generator, with
B1=J direct-sum J, every nonzero M has rank four, so G has no
two-generator nonabelian retract. If instead B1 has nonzero upper entries
B1[1,2]=B1[3,4]=1 and B2 has entries B2[1,3]=1,B2[2,4]=-1,
the Pfaffian of lambda1 B1+lambda2 B2 is lambda1^2+lambda2^2.
Again no nonzero rational rank-two form exists. Changing the latter
minus sign to plus gives lambda1^2-lambda2^2 and permits rank-two
forms, illustrating why the precise form matters.

## What remains

For a general fixed G, (1) asks for an integral point on a fixed
quadratic cone cut by the varying equation lambda dot q=1. The cone
is given by all four-by-four Pfaffians of M(lambda). This reformulation
does not supply a general terminating integer-point algorithm or an
undecidability reduction. Also q is the commutator of the actual input
pair; it must not be treated as an arbitrary independent parameter
without an embedding argument. These are the remaining gaps in using
this route for N9(a).

The original complete nilpotent page and N9 background were reread.
The prior fixed/uniform distinction and original visual audit remain
as recorded in `N9-fixed-ambient-and-coproduct.md`. Targeted searches
for Heisenberg retracts and alternating-form retract criteria mostly
returned unrelated topological retractions and the previously checked
nilpotent sources. No exhaustive novelty search is claimed. The special
cases and elementary criterion may be familiar; they are research tools
here, not counted new solutions.

## Exact checks,29 September2026

`probe_n9_heisenberg_retracts.py`, seed2026092920, constructs17 positive
retractions in exact integral normal coordinates, including negative
coordinates, central shifts, unimodular basis changes and mixed alternating
forms. `check_n9_heisenberg_retracts.g` independently constructs the actual
GAP/nq presentations, verifies torsion-freeness and Hirsch lengths, and
checks the image, fixed subgroup generators and idempotence of all17 maps.
It also verifies the four negative controls' exact obstruction polynomials
and central vectors. Their universal nonexistence assertions use the
written algebra above, not bounded enumeration.

The two recorded jobs `n9-heisenberg-retracts-v1` and
`n9-heisenberg-retracts-gap-v1` passed with empty stderr. Their source,
fixtures and raw process records are retained. Python and GAP provide
independent implementations; this is not independent specialist review.

A later route to the full fixed-group question appears in
`problems/N9/fixed-ambient-lead.md`. It supplies a proposed encoding of
the restricted actual commutator vectors q, addressing the specific gap
identified above. The initial lead remains separately labelled pending
its full audit; these special cases alone do not solve N9(a).
