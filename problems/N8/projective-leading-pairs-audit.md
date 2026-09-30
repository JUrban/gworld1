# N8: complete projective leading pairs and a scale-sensitive group example

30 September 2026, during the original run. This supplements Section 2 of
the [general candidate proof](general-proof.md). It does not change that
proof or its scope. The complete arbitrary-rank group algorithm remains
unimplemented, and correctness and novelty still require specialist review.

## What is implemented

The earlier [projective-factor audit](projective-factor-audit.md) implements
the finite projective charts and their exact rational points. Its primitive
integral first factors suffice for its central-target purpose. They do not
alone supply the complete leading branches needed for a noncentral target.

The new `scripts/n8_projective_leading_pairs.py` retains, for every rational
direction, its primitive integral C0 and the unique D0 with [C0,D0]=W.
If D0 is integral, it returns (k C0,D0/k) for every positive and negative
divisor k of the gcd of D0's coordinates. A nonintegral D0 is rejected,
as required by the proof. Both signs and every scale allocation are kept.
For equal weights it uses the existing exterior/Hermite construction,
returning representatives modulo the exact commutator-preserving SL2(Z)
pair transformations. No block-quadratic/Klyachko factor routine is called
by this route. Some shared modules also contain that older routine; the
comparison checker explicitly calls it as a second finite-list calculation.

Completeness still rests on the written projective-fibre, rational-point
and integral-lattice arguments. The new module implements this first stage;
it does not implement the later exceptional-parameter recursion.

## A complete small example where primitive normalization loses solutions

Use group commutators [x,y]=x^-1 y^-1 x y in N=F(a,b)/gamma_6(F(a,b)).
Set z=[b,a], d=[z,a], and

    g = [a^2 z, d^3].

The leading term is W=6[a,d] of degree four. In rank two, L2 is
one-dimensional, so there is no equal-weight (2,2) factor. The type-(1,3)
binary-quadratic calculation has only the first-factor line Qa: write
Z=[b,a] and expand [s a+t b, u[Z,a]+v[Z,b]]. The three coefficients
are su, sv+tu, tv in the corresponding degree-four basis. The target
su=6, sv+tu=tv=0 forces t=v=0. Thus the complete normalized pairs are

    C=k a, D=(6/k)d,       k in {1,-1,2,-2,3,-3,6,-6}.

Here and below a,z,d also denote their leading Lie coordinates when
used in brackets or coordinate vectors. To give an explicit certificate,
put e=[z,b], h=[d,a], i=[d,b], j=[e,b]. Use the ordered degree-five
Hall basis

    E1=[d,z], E2=[e,z], E3=[h,a],
    E4=[h,b], E5=[i,b], E6=[j,b].

For the base group lifts x0=a^k, y0=d^(6/k), the four possible central
correction columns, from the weight-two first-factor coordinate z and
weight-four second-factor coordinates h,i,j, are

    -(6/k)E1,   -k E3,   -k(E1+E4),   -k(E2+E5).

The residual [x0,y0]^-1 g has coordinates

    -3 E1 + 3(k-2) E3.

These formulas also follow directly from group commutator identities.
All degree-five terms are central, [a,d] has degree four, and

    [a^k,d^l] = [a,d]^(kl) [a,d,a]^(l k(k-1)/2),
    [a^2 z,d^3] = [a^2,d^3] [z,d]^3.

The leading coordinates of [a,d,a] and [z,d] are -E3 and -E1.
Substituting l=6/k gives the residual above, for negative k as well.
Higher corrections cannot affect degree five, so these are the full
integer lift conditions for each branch.

The E4 and E5 equations force the last two correction coefficients to
vanish. The first two coefficients must then be k/2 and 6/k-3.
Consequently the branch is soluble exactly for k=2,-2,6,-6. In
particular, both primitive branches k=1,-1 fail. Keeping only primitive
first factors would reject this known commutator. This is a boundary
control for that shortcut, not a flaw found in the general proof: its
signed-divisor step already retains the successful branches.

## Checks and evidence

The Python checker passed nine Lie cases, retaining 80 pairs or Hermite
representatives in total. Eight unequal-weight lists were compared in
full, including both signs, against the separate block-quadratic routine.
They include two rational directions with content six, irrational
directions with no rational factor, a repeated direction with content
twelve, and five generated examples in ranks two/three with weights
(1,2), (2,3) and (3,4). The equal-weight rank-three index-six example
has twelve Hermite representatives. Every returned pair's bracket was
checked exactly; that equal-weight routine is shared, not independent.

For the noncentral example, Python computed all eight integer correction
systems and constructed witnesses for all four successful branches. A
separate GAP/nq checker reconstructed the free nilpotent group and tested
membership of each residual in its central correction subgroup. It did
not read the Python Hall matrices or use its integer solver. All four
positive and four negative lift decisions agree, and all four constructed
group witnesses satisfy the original commutator equation.

Recorded sequential jobs each requested one CPU and 2 decimal GB:

- `n8-projective-leading-pairs-v1`: passed in 1.022 seconds, empty stderr.
- `n8-projective-leading-pairs-gap-v1`: passed in 1.876 seconds. GAP emitted
  a syntax warning about the loop-global `residual` captured in an arrow
  function. It is assigned before that function is called; the warning is
  retained and was inspected. No GAP error or break loop occurred.

The read-only process observation found all 690 recorded receipts terminal,
an empty registry and no remaining workers in its observed scope. It is
an observation at this checkpoint, not a prohibition on later work.

Sources and outputs are bound by
`research/certificates/N8-projective-leading-pairs/manifest-v1.json`.
The original full nilpotent-problem page and N8 paragraph were reread;
the retained N8 statement rendering was actually viewed. No new literature
or novelty conclusion is asserted. This remains a same-agent audit with
separate computational reconstructions, not outside review.

For replay, use a separate review copy and fresh output paths, preserving
the existing `checks-v1.json` and `fixtures-v1.g` before regeneration.
The exact commands are in the process receipts. The experiment's runner
refuses research after its original deadline; later verification must be
dated as review, with no clock reset.
