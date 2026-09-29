# N8(b): free leading generators and arbitrary-class commutator branches

Candidate argument, 29 September 2026, first developed about 10:12--10:20 UTC.
This extends the existing partial candidate; it does not decide every target.
The construction and proof are separate from the bounded implementation tests.
Independent specialist review and novelty assessment remain outstanding.

Use N=F_r/gamma_(c+1), finite r,c, integral Hall coordinates, and
[x,y]=x^-1 y^-1 x y. Let L be the full free graded rational Lie algebra
on r generators, and L_Z its integral Hall lattice. Fix nonzero homogeneous
C in (L_Z)_p and D in (L_Z)_q, p<=q, with [C,D]!=0 and p+q<=c.

**Branch theorem.** The equation [x,y]=g with x having leading term C
and y having leading term D is decidable, with factors on acceptance,
in either of the following cases:

1. p=q (so C,D are independent).
2. p<q and D has nonzero image in A/[A,A], where

       A = Q*C + direct_sum_(j>p) L_j.                 (1)

The test in (2) is finite rational linear algebra through degree q.
It always passes when p<q<=2p. In particular, all targets with first
nonzero lower-central coordinate in degree three are decidable in every
class: their normalized leading factors have weights (1,2).
Equal-weight branches are also decidable in every class. A failed branch
test never rejects an unexamined leading type of the original equation.

## 1. A weighted free Lie algebra containing all possible factors

For p=q instead use

       A = Q*C + Q*D + direct_sum_(j>p) L_j.           (2)

These are graded Lie subalgebras. Their positive-degree abelianizations
have homogeneous bases which can be lifted to free homogeneous bases
of A. Indeed the lifts generate by induction on degree, are irredundant,
and are free by the classical homogeneous Shirshov lemma. Thus C,D can
be included in such a free basis in case (2), and in case (1) precisely
under the stated nonzero-image hypothesis. The two different degrees
give independent abelianization classes. Through degree c, complements
to [A,A]_j and all their brackets are obtained by rational linear algebra.
No computation in infinitely many degrees is necessary.

For (1), [A,A] has no homogeneous component of degree <=2p: the only
possible smaller bracket is [C,C]=0. This proves the sufficient bound
q<=2p. It also shows why a blanket assertion for all unequal weights
would be unjustified. For example D=[C,E], deg E>p, fails the hypothesis.

Choose integral Hall lifts x0,y0 of C,D. Work in the subgroup

       K = <x0,y0,gamma_(p+1)(N)>       if p=q,
       K = <x0,gamma_(p+1)(N)>          if p<q.        (3)

The second group already contains y0. Every allowed pair belongs to K.
Membership in K amounts to zero coordinates below p and membership of
the degree-p coordinate in Z*C+Z*D, or Z*C, respectively. Thus membership
is effective, even when C,D are nonprimitive. The lists x0,y0 followed
by all ambient Hall generators of weights >p (or just x0 followed by
that tail) give unique integral product coordinates for K. Commutators
raise weight; these are torsion-free central-series coordinates.

Use the rational Malcev completion of N, with Lie algebra L truncated
above c. Its BCH realization sends original group generators to exp(X_i).
The Lie algebra of K is exactly A truncated above c: it contains every
layer >p, and log(x0), log(y0) have the stated leading terms. Replace the
free homogeneous generators C,D of A by log(x0),log(y0); retain homogeneous
lifts for the other free generators. This gives an isomorphism from the
weighted free Lie algebra truncated above c to the Lie algebra of K.
Its associated graded map is the original isomorphism; finite filtered
linear algebra therefore proves both surjectivity and injectivity.
Write b_C,b_D for these two actual, possibly inhomogeneous free generators.

## 2. Rational corrections become integral after taking powers

For t>=1 and E in an ambient Hall basis of L_(p+t), define the rational
Lie automorphism

       b_C -> b_C+E, all other free generators fixed. (4)

Similarly for F in a Hall basis of L_(q+t), define b_D -> b_D+F. Omit
degrees exceeding c. All E,F lie in A. Although they may themselves
involve b_C or b_D, these substitutions are automorphisms: they increase
weight by at least t, and successive weight corrections give their
inverses. On the whole filtered Lie algebra their matrices are I+T with
T strictly increasing weight. Thus they are rational unipotent maps and
act identically on every associated graded component.

Here is an elementary integral-power lemma, including effectivity.
Let alpha be any such rational unipotent automorphism. In a fixed rational
basis,

       alpha^n = sum_(k=0)^c binomial(n,k) T^k         (5)

for every integer n. For each generator k_i of the central-series basis
of K, the product coordinates of exp(alpha^n(log(k_i))) in that basis
are rational polynomials in n. This follows directly from finite BCH
arithmetic and triangular coordinate conversion. At n=0 all coordinates
are integers. Choose a positive integer M divisible by every denominator
of every nonconstant coefficient of these finitely many polynomials.
Then each coordinate at n=M and n=-M is integral. Hence alpha^M and
alpha^-M both send the generators of K into K, proving alpha^M(K)=K.

This is constructive without explicitly forming the polynomials: test
successive factorial powers 1!,2!,3!,... on the finite basis of K and
its inverse images by exact rational BCH collection. Eventually all pass
by the denominator argument. This search terminates; testing only forward
images would not suffice. For (4), the first changed coordinate of alpha^M
is M E. The analogous D correction is M F.

For every t and every E,F choose one such power. Their finite collection
generates a subgroup U of Aut(K). Its elements act trivially on each
ambient weight layer. Commuting maps which raise weights by t and s
raises weights by at least t+s. Hence U is nilpotent of class at most c-1;
all its elements, compositions, inverses and equality tests are effective
as rational matrices or by their action on the finite basis of K.

## 3. Finitely many pair orbits

Let P consist of all pairs with leading C,D. At offset t, the subcollection
above which raises weight by at least t changes the two next coordinates by

       (M_E E,0),   (0,M_F F)
       in (L_Z)_(p+t) + (L_Z)_(q+t).                 (6)

This formula holds for every pair already matched at earlier offsets.
For example log(x)=b_C+terms of weight >=p+1. A map raising weight by t
acts on that tail only in weights >=p+t+1. Its degree-(p+t) effect is
therefore exactly its change on b_C. The same reasoning applies to y.
In particular this is valid when p<q, despite the unequal factor weights.

The vectors (6) span a finite-index integral lattice of the full next
coordinate space. Retain a finite set of its coset representatives,
append the corresponding actual Hall corrections to the current pairs,
and continue for t=1,...,c-p. Ignore a coordinate whose degree exceeds c.
This produces finitely many actual pairs P_0. Inductively applying the
chosen integral automorphisms matches every pair in P to one in P_0.
Conversely U preserves P. Therefore the set of their commutators is
exactly the union, over (x_i,y_i) in P_0, of U-orbits of [x_i,y_i].

Integral powers can make these finite lists very large. Their size is
irrelevant to termination; replacing them by a single rational orbit
would lose necessary integral residue classes.

## 4. Deciding each orbit

Use the elementary algorithm in Sections 2--3 of
`independent-abelianization-proof.md`, now on K and its filtration
K intersect gamma_j(N). Reject g outside K first. At a current candidate
v and a finitely generated subgroup H of U fixing v modulo gamma_j,

       h -> v^-1 h(v) mod gamma_(j+1)

is a homomorphism to the integral layer. Integer lattice membership
decides whether the discrepancy to g can be corrected. On success,
correct v and replace H by the kernel. A finite generating set of that
kernel is the normal closure of generator commutators and the words
given by an integral basis of the column-matrix kernel. Include their
nested commutators with signed original generators through the nilpotency
bound c-1. Longer commutators vanish, so this is a finite, effective
normal closure. This proves both answers and termination, without a
general Diophantine or arithmetic-group oracle.

An orbit witness applied to the selected factors constructs the desired
pair. If all finitely many orbit tests fail, no pair in the stated branch
exists. All ambient layers and subgroup coordinate lattices are explicit.

## 5. Scope within the original equation

The prior complete leading-pair normalization gives finitely many
normalized integral pairs with p+q equal to the target's leading degree.
For unequal weights it retains every signed divisor allocation on each
possible rational first-factor line. For equal weights it retains all
oriented Hermite sublattices of the prescribed index. Exact Nielsen
moves preserve the commutator and remove dependent equal leading terms.
This reduction is unchanged; see the existing leading-pair proofs and
their separate audits.

If every normalized leading pair passes the present criterion, the
finite union of the branch algorithms decides the unrestricted target.
If some fail, a positive answer in a covered branch is still a genuine
solution, but failure of all covered branches is inconclusive about the
others. The identity and targets outside the commutator subgroup are
immediate boundary cases.

Degree three has only the type (1,2), so this proves the new complete
arbitrary-class target stratum. Degree two was already covered. In higher
degrees the theorem covers equal-weight branches, every type with
p<q<=2p, and the additional leading pairs passing the explicit
abelianization test. It is not an all-class solution of N8(b), and does
not affect the known negative answer to N8(a).

## Dependencies and review status

The homogeneous Shirshov lemma is imported, not proved here. Its exact
ordinary-Lie formulation is on printed p147 of Bryant--Kovacs--Stohr,
*Subalgebras of free restricted Lie algebras* (2005), archived as
`literature/raw/N8-Bryant-Kovacs-Stohr-2005.pdf`; that page was re-viewed
during this derivation. The positive-characteristic restricted-Lie
assertions in that paper are not used. Rational BCH/Malcev coordinates
and integral Hall collection are classical; the power-clearing and orbit
arguments required here are given above. No Kourovka material is imported.

The original N8 HTML, linked background and actual archived rendering
were reread/viewed. The background credits Roman'kov2016 for the class-two
case and the negative answer in arbitrary class-two groups. Targeted
current searches did not locate this precise higher-class reduction;
this is not an exhaustive novelty assessment. Computational scope and
any implementation failures will be recorded in `weighted-orbit-audit.md`.
