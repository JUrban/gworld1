# N8: a one-parameter tail through overlapping kernels

29 September 2026. **Candidate extension with completed finite fixture
audit.** Independent class-15 and class-18 group and arithmetic replay
passes; see `parametric-tail-audit.md` for exact scope and failures. The
general branch algorithm is not implemented end to end. No novelty or
specialist approval is asserted.

## Candidate extension

In a finite-rank free nilpotent group of class c, a normalized commutator
branch with first remaining exceptional offset t>=3 is decidable if

    c-p-q <= 2t+3.                                      (1)

Here the two leading factors have nonzero weights p<=q and nonzero
bracket. Earlier offsets have already been fixed in finitely many branches,
and an exceptional offset means a nonzero kernel before q-p. A positive
decision constructs factors. Together with the existing exact-substitution
algorithm and the isolated treatment of offsets 1,2, this covers all
targets in the ten final layers c-d<=9, where d is the target's leading
degree. Combining this with the leading-degree-eight theorem gives all
targets in classes c<=18. General N8(b) remains unresolved.

Part (a) is not included: Roman'kov's prior negative result concerns general
finitely generated class-two groups. The free class-two case is prior too.
The full original HTML, exact N8 fragment, linked background and actual
archived rendering were rechecked during this extension.

## 1. Retain the complete integral line

We use the finite leading-pair enumeration and homogeneous kernel lemmas
from `universal-gauge-proof.md`, with their existing prior credits. Put
d=p+q and n=c-d. At a pre-Nielsen exceptional t the full homogeneous map

    A_t(U,V)=[U,D]+[C,V]

has a one-dimensional rational kernel, and A_(t+1) is injective. In fixed
integral Hall coordinates, solving the layer at t gives either no solution
or all solutions v+kK, k in Z, with K primitive in the integral kernel.

If n<t+1 there is no successor equation and the remaining equations are
already linear; solve them jointly as in the earlier tail argument.
Otherwise the successor equation is affine linear in k and its own
correction coordinates w. Products of two variable increments first appear
at offset 2t, so for t>=2 they do not appear at t+1. The present application
uses t>=3; t=1 is handled separately below.

Solve the entire integer system for (k,w). Since A_(t+1) is injective,
its rational kernel has dimension at most one, and projection to k is
injective on that kernel. Thus the exact solution set is empty, a point,
or an integral affine line

    (k,w) = v_0 + T J,    T in Z.                        (2)

In the line case J is a primitive integral generator of the complete joint
kernel and its k coordinate m is nonzero. Neither m nor the origin k_0 is
replaced by a rational normalization. Smith normal form gives (2), including
all divisibility conditions. A point is the same construction with T fixed.

Apply these two layers as actual ordered Hall group corrections, obtaining
a pair x_T,y_T whose commutator agrees with the target g through degree
d+t+1. Every solution extending the fixed earlier branch is represented
by one such integer T and higher integral Hall coordinates. There is no
discarded later exceptional parameter and no finite truncation of T.

## 2. Every remaining unknown occurs linearly

Set s=t+2. All unfixed corrections on the first factor have weight at
least p+s; on the second they have weight at least q+s. Write their full
ordered Hall-coordinate vector as z in Z^N. Coordinates too deep to affect
the commutator can be set to zero. All other coordinates, including later
exceptional directions, remain among the N variables.

Use the rational truncated free associative algebra with each original
group generator represented by its exponential. This is a faithful
realization of the free nilpotent group and its Malcev completion. Each
Hall word h of weight w has log(h) of weight at least w; h^z is the finite
exponential of z log(h). Group products, inverses and commutators therefore
have rational polynomial coordinates in T,z.

A term involving two remaining first-factor increments has weight at least

    2(p+s)+q = d+p+2s;

two second-factor increments require weight at least d+q+2s. A term
involving one increment from each factor has weight at least d+2s. A
commutator term involving only one side must also contain a letter from
the other side: on setting that entire factor to the identity it vanishes.
This justifies the extra q or p in the first two bounds, including repeated
powers of a single correction coordinate. Extra letters, earlier fixed
corrections, and conjugations never lower weight.

Condition (1) says 2s=2t+4>n. All three bounds therefore exceed c=d+n.
Consequently every coefficient of the commutator, and of its relative
error against [x_T,y_T], is affine linear in the entire vector z. Polynomial
dependence on T is allowed. This is a formal weight argument, not an
inference from testing one-coordinate increments.

More explicitly let h_T=[x_T,y_T]. There are polynomial tensor vectors B_j
such that

    h_T^(-1) [x(T,z),y(T,z)] = 1 + sum_j z_j B_j(T).     (3)

Each B_j has weight at least d+s. Also h_T^(-1)g is in gamma_(d+s), because
the first two varying layers were solved in (2). As 2(d+s)>c, that tail
subgroup is abelian and the products of any two of its augmentation terms
vanish in the truncated tensor algebra. Its integral Hall coordinates
are additive, and conversion from tensor coefficients is a fixed rational
linear map. Equation (3) is therefore equivalent to

    P(T) z = b(T),    T in Z, z in Z^N,                 (4)

for effectively computable rational polynomial P,b. Clearing constant
denominators preserves exactly the integer solutions. This argument does
not presume that the later exceptional direction can be integrated to an
exact commutator-preserving substitution.

One can compute P,b symbolically by finite collection. Alternatively there
is a proved interpolation bound: every occurrence of T in the two retained
layers has weight at least p+t. Therefore all tensor coefficients have
degree at most floor(c/(p+t)) in T. The relative tail collection is linear,
so the same bound holds for P,b. Evaluating at one more distinct integer
than this bound identifies the polynomials exactly. Computing enough
samples without proving such a bound would not suffice.

The prior arithmetic theorem, written and implemented in
`parametric-integer-proof.md`, decides (4) completely and constructs a
witness. Every such witness gives integral Hall group factors and the
original commutator equality. Conversely every original solution produced
one of the integer parameter/coordinate tuples retained above. This proves
the proposed branch decision under (1), conditional only on the explicitly
imported earlier leading-pair and exceptional-kernel lemmas.

## 3. Why this covers all ten final layers

Assume n<=9. Process the finitely many leading branches using the preceding
exact-substitution algorithm. Layers with injective correction maps are
ordinary integer linear solves. At the Nielsen offset and later kernels,
retain the complete finite residue set of the exact universal substitutions.

If an exceptional offset t=1 occurs, its nonzero quadratic obstruction is
tested at offset 2. There is no intermediate offset; the successor is
injective. Every surviving parameter is fixed by an exact integer-root
test, and the branch proceeds. If n<2 the remaining system is linear.

If an exceptional offset t=2 occurs, offset 3 is injective. The finite
affine-line argument through the block below offset 4 and its nonzero
quadratic obstruction at offset 4 apply verbatim from the separated-kernel
proof. There is no possible other exceptional offset strictly between 2
and 4. A new exceptional kernel at offset 4 is retained and treated at
the next stage; it cannot cancel the earlier cokernel obstruction. If
n<4, the remaining system is linear.

Thus either these steps finish the branch, no exceptional offset remains,
or its first remaining exceptional offset satisfies t>=3. Then
n<=9<=2t+3, so Sections 1–2 finish it without a separation hypothesis.
All reductions retain every integral residue, line, and polynomial root;
each preliminary stage fixes more layers. This is a terminating algorithm,
not merely a semidecision search for witnesses.

For c<=18 and a nonidentity target in the derived subgroup, either d<=8,
covered in arbitrary class by `exceptional-boundary-proof.md`, or d>=9,
when c-d<=9. The identity and abelian/rank-zero cases are immediate, and
targets outside the derived subgroup are rejected. This explains precisely
the candidate all-target class-18 consequence and its dependence on the
earlier arbitrary-leading-pair enumeration.

## 4. What still needs separate scrutiny

The complete algorithm over every leading branch and ambient rank is not
implemented end to end. Weighted two-generator fixtures test the first
overlap and exact group-to-polynomial conversion, not every ambient Hall
component. The proof above, rather than those fixtures, supplies the general
rank/class claim. Its deep inherited free-Lie structural dependencies still
require specialist review. The arithmetic ingredient is prior and credited;
limited literature searches do not establish novelty of the application.
