# N9 closing fixed-group proof audit

30 September 2026, approximately 02:23--02:34 UTC. Same-agent review
within the original research window. No new gap was identified in the
checked implications; correctness and novelty await specialist review.

Read the complete current proof, isolated-input supplement and audit.
Reread the full original nilpotent-group HTML and N9 background, and
actually viewed the retained N9 statement image. Reread the archived
DPRM formalization paper's Theorem 8.3 and its local proof, together with
the start of the following section explaining the natural/integer
variable conversion. No new source-page image inspection or full audit
of the DPRM/Coq development is claimed. The previous 2016/2017 scope
audit and its stated source-access limits remain in force.

## Fixed data versus input data

A single nonrecursive computably enumerable set S containing 0 and 1
is chosen first. DPRM supplies a **fixed** polynomial P(n,y), with
existential integer variables obtained by replacing natural unknowns
by sums of four squares. Its circuit, labels, linear constraints on
alternating matrices, full integer kernel basis, and group presentation
are all fixed before the parameter n arrives. Only the two words

    a=x0,    b_n=x1^(3n+1)x2^-1

vary. Their ordinary word encoding is computable; a polynomial-time
reduction or short universal numerical presentation is not required.
This is the distinction between the candidate and the credited prior
class-wide result in which the ambient group varies.

## The arithmetic and group interfaces

Write d=M01, x=M02 and t=3n+1. The selected four-coordinate Pfaffian
and the input equation give d M23=x squared and t d-x=1. Hence

    d (M23-t squared d+2t)=1.

Thus d is 1 or -1; divisibility of x by 3 excludes -1 and forces
d=1, x=3n. A rank-at-most-two alternating matrix with this unit pivot
has integral coordinates Mij=ui vj-vi uj. The circuit constraints then
recover all additions, multiplications, constants and repeated wires.
Conversely an integer circuit solution produces such a rank-two matrix.
The use of the **full** integer kernel is essential: clearing each
rational basis vector's denominators independently would not suffice.

The fixed group law on Z^D times Z^s is given by an explicit bilinear
central cocycle. It establishes consistency, torsion-freeness and unique
normal forms for the presented class-two group. The fixed parameter-zero
witness ensures that the commutator of a and b_n is nonzero for every
natural n, including parameters outside S. Thus each input subgroup is
the rank-two free class-two group and its centre is cyclic.

A retraction sends every ambient central generator into that cyclic
centre. Its exponent coordinates satisfy the linear circuit kernel;
fixing the subgroup commutator supplies the unit equation and hence
the Diophantine witness. Conversely the rank-two matrix gives the
homomorphism xi maps to a^ui b_n^vi and the stated central images.
The normalizing coordinates send x0 to a, x1 to b_n and x2 to
b_n^(3n). Consequently both subgroup generators are fixed exactly;
there is no omitted central correction in this check. All defining
commutator relations are respected by the kernel expansion.

## Isolation does not trivialize the reduction

The circuit kernel L is saturated because it is an integer linear
kernel. A basis extends to a basis of the ambient lattice. Its row
matrix therefore has an integer right inverse, so the commutator
columns generate the entire central coordinate lattice. Thus G'=Z^s
and G/G'=Z^D; this does **not** require identifying Z(G) with Z^s.

The fixed solutions at parameters 0 and 1 give coefficients mu0,mu1.
For every n, mu(n)=(1-n)mu0+n mu1 pairs to 1 with the commutator
coordinate q_n. Therefore q_n is primitive even when n is not in S.
The two abelianized subgroup generators span a primitive rank-two
lattice, using the coordinate minor of determinant -1. These two facts,
together with centrality of G', prove the stated root-closure of H_n:
if g^k lies in H_n, first match its abelianized image and then use
primitivity of the central cyclic subgroup.

This interpolation imposes no rank-two condition. Its displayed
four-coordinate Pfaffian is 9n(1-n), so separate splittings of the
abelian layers cannot be mistaken for group retractions. The fixed
ambient construction, isolated inputs and both primitive graded images
therefore remain compatible with undecidability.

The universal numerical DPRM circuit/presentation is not expanded,
and the retained toy groups do not prove undecidability. Lean checks
the integer normalization fragment, not this whole reduction. Part (b)
and the uniform version of (a) remain credited prior answers; the
potentially new claim is the fixed ambient group. No new computation,
candidate count, or bibliographic conclusion follows from this reread.
