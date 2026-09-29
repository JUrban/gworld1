# N8: diagonal separation and a proposed general non-absorption argument

29 September 2026, approximately17:30--17:37 UTC. **Unadopted structural
lead.** The argument below could remove the restriction on the number of
exceptional offsets. It has not yet received the independent finite audit
or the adversarial group-coordinate review needed for scope promotion.
Current adopted scope remains the three-exception/class26 partial result.

## 1. A polynomial lemma

Let E_0,E_1,... freely generate an associative algebra over Q and set
delta(E_i)=E_(i+1). For a polynomial with exactly m letters E, encode the
coefficient of E_(i1)...E_(im) as the coefficient of
x1^i1...xm^im in a commutative polynomial. This is a linear positional
encoding, not an algebra homomorphism. Delta becomes multiplication by
the sum of the positional variables.

Suppose D has m letters and V has m+1 letters, and

    delta V = [E_0,D].

Let P(x1,...,xm) encode D. The encoding of V is

    (P(x2,...,x_(m+1))-P(x1,...,xm))/(x1+...+x_(m+1)).       (1)

It is a polynomial by the hypothesis. Thus P is invariant under

    (x1,...,xm) -> (x2,...,xm,-x1-...-xm).                  (2)

Equivalently, view P as a polynomial on the real hyperplane
H={y0+...+ym=0}, by P(y1,...,ym). It is invariant under cyclic
permutation of the m+1 coordinates.

Write Q=[E_0,V]. Restrict its positional encoding to

    x_(m+2)=x1,             x1+...+x_(m+2)=0.              (3)

**Lemma.** If this restriction is zero, then P is constant.

Put x=(x1,...,xm), S=sum x_i, and a=-S/2. Formula(1), applied to
Q, shows that its zero restriction implies

    2P(x)=P(x2,...,xm,a)+P(a,x1,...,x_(m-1)).              (4)

This identity follows first where a is nonzero by division, and then
everywhere as a polynomial identity. Using(2) in each term transforms
(4) into

    2P(x)=P(x+a e1)+P(x+a e_m).                           (5)

On H, let T_(i->j) halve coordinate y_i and add the other half to
y_j, leaving every other coordinate unchanged. Equation(5) is

    P(y)=(P(T_(0->1)y)+P(T_(0->m)y))/2.

Cyclic invariance gives the same equation with0 replaced by any i,
and its two cyclic neighbours as recipients. Each T preserves H and
does not increase the l1 norm.

Fix a closed l1 ball in H. The continuous real polynomial P attains
a maximum there. If y is a maximum point, the averaging identity and
the invariant ball imply that both outgoing neighbours of y are also
maximum points. Therefore every finite composition of these transfers
takes y to another maximum point.

There is a fixed composition B of the clockwise transfers which
strictly contracts H in the l1 norm. For instance perform a complete
cycle T_(0->1),T_(1->2),...,T_(m->0), and repeat it m+1 times.
Its matrix is column-stochastic and has every entry positive: mass
can follow a clockwise path from any coordinate to any other, while
the retained halves permit waiting. A path of length at most m fits
within two complete cycles. Let epsilon be its smallest entry and
n=m+1. Then

    B=epsilon J+(1-n epsilon) C,

where J is the all-ones matrix and, when the second coefficient is
nonzero, C is a nonnegative column-stochastic matrix. On H, Jy=0,
and hence ||By||_1 <= (1-n epsilon)||y||_1. If the coefficient is
zero B annihilates H directly. In either case B^k y tends to0.
Continuity shows that the maximum of P on the ball equals P(0).
The same reasoning for the minimum makes it P(0) as well. Every ball
is arbitrary, so P is constant on H, and hence in its m free variables.
This proves the lemma. It needs no extrapolation from finite ranks.

In the free Lie algebra on the E_i, a constant positional polynomial
corresponds to a multiple of E_0^m in the associative algebra. It is a
Lie polynomial only for m=1 (or it is zero). Therefore, except for
D=lambda E_0,V=0, every nonzero Lie solution has Q with nonzero
restriction(3). Nonhomogeneous inputs may be separated by E-letter
number and total E-index first; delta respects these gradings.

## 2. What this separates

Let R denote restriction(3) on a fixed E-letter number. It annihilates
delta of every polynomial with that many letters, since the total
positional sum is zero. Moreover, for any compatible length polynomial F,

    R([E_j,F]) = x1^j R([E_0,F]).                         (6)

This uses equality of the first and last positional variables.
Consequently, if [E_0,F_l] lies in im delta for each l, then all
[E_(j_l),F_l] have zero R-image. The nonzero quadratic Q from Section1
cannot lie in their span plus im delta.

This generalizes the previously proved evaluation-at(1,-2,1) lemma:
D need no longer be a single even derivative E_k. It still does not,
by itself, identify every column of an actual group lifting problem.

## 3. Proposed normalization of an actual first-exception block

Use the inherited N8 notation: leading Lie terms C,D have weights
p<=q, d=p+q, and t<q-p is the first still-free exceptional offset.
All pair coordinates below t have been fixed. Suppose the target class
reaches at least d+2t. Work over Q in the truncated Malcev Lie algebra;
write X=log x, Y=log y.

**Normalization to check carefully.** The graded Lie algebra L_(>=p)
is free by Shirshov--Witt. Choose a homogeneous free basis containing
C; every nonzero degree-p vector can be included, because no bracket
in this algebra has degree p. A filtered substitution changing C to
C plus the already fixed terms of X of offsets1,...,t-1, and fixing
the other free basis elements, is invertible after finite truncation.
Its inverse makes X=C modulo weight p+t. It acts as the identity on
the associated graded, keeps the leading C,D and first kernel direction,
and is fixed independently of every block parameter. This is a rational
coordinate change for the proof, not an asserted integral automorphism
of the original group.

For the convention [x,y]=x^-1 y^-1 x y, the part of log[x,y] linear in
Y is

    (1-exp(-ad X))Y = [X,Z],
    Z=h(ad X)Y,        h(z)=(1-exp(-z))/z, h(0)=1.          (7)

Every remaining term has at least two Y occurrences and at least one
X occurrence. Since a variable increment first occurs at offset t,
its variable-dependent terms of this kind have weight at least
p+2q+t > p+q+2t, because q>p+t>t. Thus through weight d+2t these
remaining terms are fixed on the whole block. The variable equations
are exactly those of [X,Z] with a fixed adjusted target.

The changes of coordinates are affine in the block parameters through
the required input weights. Two variable X increments have weight at
least2(p+t)>p+2t; two variable Y increments have weight at least
2(q+t)>q+2t. The nonlinear parameter terms in h(ad X)Y start above
q+2t as well. The leading Z term remains D. These bounds must be
audited against the integer block conventions before using the argument
in the full algorithm. For separation alone rational coordinates suffice;
the actual algorithm still uses the full original integer block lattice.

## 4. Proposed separation from *all* later block columns

Take the graded free Lie subalgebra

    A=Q C + direct_sum_(j>=p+t) L_j.

It is closed. C and a basis of L_(p+t) are independent in its
abelianization and extend to a homogeneous free basis. In particular
the nonzero first-coordinate kernel direction U can be chosen as one
such basis element. The inherited inner-solution theorem applied to
[U,D]+[C,V]=0 places D,V in Lie(C,U). Project A onto this two-generator
Lie algebra, killing the other homogeneous free basis elements.
All X,Z components needed in the block belong to A after Section3's
normalization, including arbitrary particular solutions at offset t.

Use the chain E_j=(ad C)^j U and delta=ad C. Let D_m be the component
of D of greatest E-letter number m. Its corresponding kernel component
V_(m+1) satisfies delta V_(m+1)=-[E_0,D_m]. Since q>p+t, D_m is not
a scalar E_0. Section1, with the harmless sign change, says that the
restriction R of [E_0,V_(m+1)] is nonzero.

Every projected first-coordinate component at an offset i<=2t has
at most one E letter, since two such letters have weight2(p+t)>p+2t.
It is therefore either zero or a scalar E_j with p j=i-t; pure C
terms have the wrong weight. This applies to all particular solutions
and every parameter direction, not only homogeneous exceptional lines.
The image of [L_(p+2t),D] has at most m+1 E letters; the other part
of A_(2t) is killed by R. Thus R in E-letter number m+2 annihilates
the complete last linear correction image.

Adapt the full affine block lattice so its first exceptional coefficient
is k0+bT with b nonzero, and all other directions have zero at offset t.
Let F_j be the E-letter-(m+1) component of the fixed Z coordinate at
offset j, for0<=j<t. In particular F_0=0 by maximality of m.
At offset t+j<2t the coefficient of T in the already-satisfied equation
[X,Z]=target, projected to E-letter number m+2 and then by R, is a
triangular convolution:

    b R([E_0,F_j]) + sum_(i=t+1)^(t+j)
        b_i x1^((i-t)/p) R([E_0,F_(t+j-i)]) = 0.           (8)

Terms with a nonintegral exponent are absent. Terms involving variable
Z and fixed X of positive offset cannot occur here: X has no positive
offset below t, and those products start at2t. The [C,-] term is killed
by R. Starting from F_0=0, induction on j and b!=0 give

    R([E_0,F_j])=0,                   0<=j<t.              (9)

Now consider the coefficient of any other block parameter S at offset
2t. It begins at some s>t. Its projected first-coordinate contributions
are scalar E_j, paired only with fixed Z coordinates of offsets
2t-i<t. Formula(6) and(9) annihilate every such contribution. Its
second-coordinate contributions pair with C or with fixed X coordinates
of offsets<t; the former are killed by R and the latter are zero.
Therefore R annihilates every later block column, including any
universal columns, while it does not annihilate the coefficient of T^2.

**Proposed conclusion:** in the first quadratic equation

    q(T)+B S=0 modulo im A_(2t),

q_2 is outside the rational span of all columns of B, regardless of
how many later exceptional offsets occur. A rational scalar functional
annihilating B then yields a nonzero quadratic in T and finitely many
integer first-parameter values.

## 5. Possible algorithmic consequence, not yet adopted

For each first remaining exception, solve the full integer block through
2t-1. If its first coefficient is fixed, retain that prefix and restart.
Otherwise the proposed separation fixes its free integer parameter to
finitely many values; retain each and restart with the next offset.
When the class stops before2t, all remaining coordinates enter jointly
linearly. Once all pre-Nielsen exceptions have been passed, the already
proved exact universal periods give finitely many residues at every
remaining layer. This would terminate through any finite class.

No rational coordinate normalization is used to discard integer points.
The algorithm would compute q_2 and B from the actual group block, and
find the separating functional by rational linear algebra; Sections3--4
would prove its existence. Forgetting higher block restrictions after
fixing the first parameter only repeats possible solutions, as in the
existing two- and three-exception algorithms.

This consequence remains **uncounted** pending a full review of the
normalization, parameter flags, BCH weight bounds, projection and
convolution argument, plus independently reconstructed finite examples.
Neither a general N8 solution nor established novelty is asserted here.

## 7. Coordinate audit, 18:05--18:16 UTC

The following clarifications address the most immediate possible gaps;
they do not yet promote the general decision claim.

1. **Free basis and normalization.** Both free Lie algebras used above
   are graded subalgebras of the full, untruncated ambient free Lie
   algebra. Apply Shirshov--Witt there, and then truncate. In L_(>=p),
   the degree-p vector C is outside the derived subalgebra. A homogeneous
   basis of the abelianization containing C lifts to a homogeneous free
   basis. The substitution for C has identity associated graded, so
   its inverse is obtained successively in each of the finitely many
   degrees under consideration. The substitution is fixed before any
   block parameters are chosen. It is a linear map on Lie elements,
   so it cannot create a product of parameters absent from the input.
   No integral-lattice equivalence is asserted or required.

2. **The enlarged subalgebra matters.** A must contain the entire
   degree-(p+t) component, not just Q U. An arbitrary particular
   first-factor correction at t need not be proportional to U. In A,
   the degree-(p+t) component is outside [A,A]: the only lower degree
   is Q C, whose bracket with itself vanishes. Thus C,U extend to a
   homogeneous free basis of A, and the remaining first particular
   correction can be projected legitimately. The credited
   Remeslennikov--Stoehr inner-solution theorem applies because C,U
   are actual basis elements of A and D,V lie in A. Infinite rank is
   harmless: the relation uses finitely many free basis letters.

3. **Affine logarithmic coordinates.** In a Hall-coordinate block whose
   first varying coordinates have weights p+t and q+t, any product of
   two first-factor parameter increments in its logarithm has weight
   at least 2(p+t)>p+2t. In the second factor the bound is
   2(q+t)>q+2t. Fixed factors of positive weight only increase these
   bounds. Therefore the required X and Y components are affine in
   all block parameters. In h(ad X)Y, a term involving two varying X
   increments has weight at least q+2(p+t)>q+2t; a term involving
   varying X and Y increments has weight at least p+q+2t>q+2t.
   Hence Z is affine through its required weight too. All the changes
   preserve the first nonzero offset of a parameter direction.

4. **Terms with two Y occurrences.** They may be nonzero constants:
   they must be subtracted, not omitted from log[x,y]. Every such term
   containing at least one variable increment has weight at least
   p+2q+t. Since q>p+t, this exceeds d+2t. Thus their coefficients
   are identical for every point of the affine block through the
   target degree. This justifies differentiating only [X,Z].

5. **Last correction and the target coordinates.** After the earlier
   block equations are satisfied, the commutator/target error starts
   at degree d+2t. Its degree-(d+2t) group Hall coordinates equal its
   degree-(d+2t) logarithmic coordinates: brackets with the fixed
   lower commutator have still greater degree. The filtered
   normalization is identity on this degree of such an error. Thus
   the functional constructed in Sections 3--4 acts on the actual
   group cokernel, not merely on an unrelated Lie equation.

6. **The induction uses earlier equations.** For j<t, the coefficient
   of T in the degree d+t+j equation has contributions from varying
   X paired with fixed Z. Varying Z paired with a positive-offset
   fixed X would require that X-offset to be below t; it is zero
   after normalization. Pairing with C is a delta image. There are
   no products of two varying coordinates in these degrees. After
   projection to m+2 E letters and restriction, exactly the convolution
   (8) remains. This is why arbitrary deformations need not work,
   but deformations in a surviving full block do.

7. **All later directions, not only exceptional ones.** A parameter
   with zero first-exception component has zero pair coordinates
   through offset t, because the first homogeneous kernel is a line.
   Its first nonzero offset is therefore >t. At degree d+2t, its
   varying X can pair only with Z-offsets <t, which the convolution
   eliminated. Its varying Z can pair only with C or with zero
   X-offsets <t. This includes arbitrary mixtures of later kernel
   directions and universal directions. No classification of them
   as individual adjoints is assumed; only their projected X
   components have at most one E letter.

8. **Nonzero quadratic and constants.** The T direction begins with
   b(U,V). Its quadratic coefficient at d+2t is b^2[U,V]. The highest
   E-letter part is b^2[E_0,V_(m+1)], which survives the polynomial
   lemma. The corresponding D_m cannot have constant positional
   polynomial: for m>1 a nonzero power U^m is not a Lie element;
   for m=1 it would have weight p+t, whereas q>p+t. Both the full
   last correction image and all later columns are killed by R.

The scalar functional can be found in the actual finite-dimensional
group-coordinate cokernel by rational linear algebra; its construction
need not compute an infinite homogeneous free basis or the projection.

## 8. Simpler proposed recursion

There is no need to quotient the *first-exception block* by universal
translations if Section 4 is correct. Keep its whole affine integer
lattice. Adapt an integral basis to the first-exception integer
coefficient k. If its image is a point, the complete prefix through t
is fixed. If its image is k0+b Z, choose the full basis with
k=k0+bT and all other directions having zero first component.
The separating scalar quadratic has finitely many integer roots T.
Each fixes the entire prefix through t. Restart at t+1, leaving all
higher coordinates free again. Discarding earlier higher-block
restrictions can repeat possible branches but cannot discard an
original solution; accepting still requires the full group equation.

Thus every first exception would give finitely many fixed prefixes,
even with arbitrarily many other block parameters. The recursion
strictly advances the fixed offset. If the class ends before 2t,
solve the remaining full integer linear system. After the last
pre-Nielsen exception use the previously established finite universal
period procedure. This would require neither the constrained-curve
lemma nor a bound on the number of exceptional offsets.

Remaining work before adopting this conclusion: a fresh adversarial
read of the full assembly and inherited leading-pair/universal-tail
dependencies, and tests addressing general leading D and nonzero
fixed lower X components. The new finite group fixture below is
deliberately a test of the nonzero later-column issue, not all of these
other generalizations.

## 9. Independent finite evidence completed at 18:13 UTC

GAP independently reconstructs all 44 Lie spaces using its native
free associative algebra, recursive Lie differentiation, rational
nullspaces and a commutative polynomial ring. It does not import
Python coefficient matrices or kernels. All six dimension columns
agree exactly with Python. The only restriction kernel is the stated
scalar exception. See `N8-diagonal-separation-audit.md` for the actual
group construction, process records and explicit limits.

## 6. Initial finite evidence

`scripts/probe_n8_diagonal_quadratic.gapless.py` constructs every Lyndon
basis vector with E-letter number1,...,4 and E-index sum0,...,10.
It solves delta V=[E_0,D] over Q using exact integer FLINT nullspaces,
then substitutes(3) symbolically and computes the complete restriction
rank. All44 spaces pass; the only kernel is D=E_0,V=0. The largest
compatible space tested has dimension13, with full restriction rank13.
The output is `research/certificates/N8-diagonal-quadratic-v1.json`.
The recorded run passed in0.972seconds on one core/6GB with empty stderr.
These finite tests initially suggested Section1; they do not establish
Sections3--5 and do not replace the proposed general proof.
