# GA3: an elementary construction of the separating element

30 September 2026, during the original 48-hour run. This supplements
Section 2 of [the candidate proof](proof.md). It replaces the use of
density of pairs of hyperbolic endpoints by a finite avoidance argument
and two conjugations. The statement and candidate count do not change.
This is an internal proof simplification, not independent review or a
separate novelty claim.

## 1. The exact geometric statement

Let a group K act isometrically on a real tree X. Assume that there is
a hyperbolic element, that K preserves neither an end nor a line, and
that the pointwise stabilizer of every nondegenerate tripod is trivial.
For every finite C contained in K minus {1}, there are a hyperbolic h,
disjoint half-tree neighborhoods U+, U- of its respective ends, and an
integer N >= 1 such that, for all c in C and n >= N,

    c(U+ union U-) intersect (U+ union U-) = empty,
    h^n(boundary X minus U-) subset U+,
    h^(-n)(boundary X minus U+) subset U-.

In addition h^n U+ is contained in U+ and h^(-n) U- is contained in U-.
The boundary means ends represented by geodesic rays. A half-tree
neighborhood means the ends eventually lying in one specified component
of X minus a point. Neither local compactness nor completeness of X is
assumed.

Here is a more specific choice. Once a,b are hyperbolic elements with
disjoint pairs of ends, h can be taken as

    g = a^k b a^(-k),          0 <= k <= 2|C|,
    h = g^m a g^(-m),          m a sufficiently large positive integer.

The bound is only on the finite choice of k. No bound on m or N in terms
of |C| alone is asserted, and no algorithm for arbitrary presentations
or unspecified tree actions is claimed.

## 2. Independent hyperbolic elements exist

Start with a hyperbolic a and its two-end set E. Consider the K-invariant
family of all translates of E. If two of them are disjoint, conjugating
both back by the translate defining the first gives E and a disjoint
translate. The latter is the endpoint set of a conjugate b of a.

Otherwise the two-element sets in this family pairwise intersect. Such
a family either has a common point or consists of the three edges of
a triangle. To check this, choose two different members {x,y},{x,z}.
If a third does not contain x, it must be {y,z}, and every member meeting
these three must be one of these three. If no such third exists, x is
common to all members. A family with only one member is handled separately.

The intersection of the entire family is K-invariant. If it has one
point, K fixes an end; if it has two, K preserves their joining line.
In the triangle case K preserves a three-element set of ends. A positive
power of a fixes these three individually, which is impossible: a
hyperbolic tree isometry has exactly its two axis ends as fixed ends.
All cases contradict the assumptions. Hence a,b as required exist.

The facts about a hyperbolic isometry used here follow directly from
its translation on its axis. An end other than the two axis ends has
a finite attachment point on that axis; the translation moves that
point, so cannot fix the end. The same observation applies to every
nonzero power.

## 3. Avoid every constant with a finite list of endpoints

Every nonidentity c in K fixes at most two ends. Three fixed ends would
make c fix their unique central branch point and each of the three rays
from it pointwise. It would then fix a nondegenerate tripod, contrary
to the hypothesis.

For k=0,...,2|C|, the ends

    xi_k = a^k b+

are all distinct. Equality for k != l would make b+ a fixed end of
the hyperbolic isometry a^(k-l), whereas b+ is different from a+,a-.
At most 2|C| ends are fixed by some member of C. Consequently one xi_k
is fixed by none. Choose that k and set g=a^k b a^(-k), so g+=xi_k.

There is a neighborhood V of g+ with cV intersect V empty for every
c in C. Explicitly, for each c choose disjoint neighborhoods O_c of g+
and W_c of c g+, and take

    V0 = intersection over c in C of (O_c intersect c^(-1) W_c).

Then V0 is a neighborhood of g+ and cV0 intersect V0 is empty. Refine
V0 to the ends of the forward component at a point q on the axis of g;
call this half-tree neighborhood V. For C empty any such V works.
Hausdorffness and the neighborhood refinement follow by separating
distinct tree rays beyond their common initial segment. No compactness
or density assertion is used.

Neither a+ nor a- equals g-: the two ends of g are a^k b+ and a^k b-,
and a fixes each of a+,a-. In fact the endpoint pairs of a and g are
disjoint. Let p+,p- be the finite attachment points of a+,a- to the
axis of g. Translation by g^m moves both attachment points past q
for all sufficiently large m. The corresponding rays therefore lie
eventually in the forward component defining V. Thus

    g^m a+, g^m a- are both in V.

Set h=g^m a g^(-m). These two distinct ends are h+,h-. Choose disjoint
half-tree neighborhoods U+,U- of them contained in V. The avoidance
condition follows immediately from cV intersect V being empty.

This is the step that replaces the previous density-of-endpoint-pairs
input. Only the finite list of xi_k and translation on one axis are
needed; a limit set need not be introduced.

## 4. The uniform power bound is just translation on the axis

Choose the defining points r-,r+ for U-,U+ on the axis of h, in this
order toward h+, and put D=d(r-,r+). They can be taken sufficiently
far in the respective directions to ensure U-,U+ are contained in V.
Let ell>0 be the translation length of h. Choose an integer N >= 1
with N ell > D.

An end outside U- either is h+ or has its attachment point to the
axis at r- or farther toward h+. Translation by h^n, n >= N, puts
that attachment point strictly beyond r+, so the image is in U+.
This proves the first uniform inclusion. Reversing the orientation
proves the second. The same argument gives the two invariant-neighborhood
inclusions. It applies to the entire boundary, not merely a sampled
set of ends, and uses no properness hypothesis.

Together Sections 2--4 prove the geometric statement.

## 5. Application to the unchanged GA3 candidate

Section 1 of the original proof supplies this real-tree action for a
finitely generated nonabelian subgroup K of the given Lambda-free G.
That step still uses Guirardel's scalar-change facts, CSA and his
Fact 5.1 with its explicit arbitrary-Lambda remark. Those dependencies
are not replaced here.

Given the finite set of nontrivial alternating syllables C, use the
elementary separator above. For a cyclic core a1 b1 ... at bt and
zeta in U-, read its image under the conjugation map from right to left:

    U- --h^(-n)--> U- --bt--> outside (U+ union U-)
       --h^n--> U+ --at--> outside (U+ union U-).

Every remaining pair repeats these inclusions. The final image is in
a1 U+, disjoint from U-, so is different from zeta. One h and N work
for all the finitely many words. The unchanged proof handles cores
in one factor, conjugates of cyclic cores, and extension from K to G.

Thus Rybak's boundary-density lemma and general hyperbolic-space
north-south statement are no longer necessary imports for this step.
They remain credited sources of the related prior mechanism in the
historical proof and audit; this elementary specialization is not a
claim to have discovered tree ping-pong. The existing finite free-group
checks are unchanged and do not verify the general collapse argument.

## 6. Audit and evidence boundary

The complete archived GA3 HTML and exact fragment were reread, and the
retained statement image was actually viewed in this work period. The
literal abelian exception, arbitrary generation and no-inversion
convention are unchanged. Guirardel's Fact 5.1, its general-Lambda
remark and local proof were reread in the retained text; there was no
new visual inspection of his PDF and no claim of a new source theorem.

The adversarial checks in the written argument are: the finite family
may be an invariant triangle rather than a star; avoidance concerns
both ends of h, although only g+ is initially selected; m must move
both attachment points; the final dynamics require the full complement
of U-, not just U+; and the first application of h^(-n) requires
invariance of U- itself. All are addressed explicitly above. The k
bound does not bound the later powers. Tripod fixators must be trivial;
an arbitrary nonfaithful action would not supply the finite fixed-end
bound.

This is a universal written proof, without a new computational test or
formal verification. Its purpose is to remove a dependency, not to
inflate the candidate tally. All original correctness and novelty
qualifications remain. Source/artifact hashes are retained in
`research/certificates/GA3-elementary-separator/manifest-v1.json`.
