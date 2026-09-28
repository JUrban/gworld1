# Single commutators in free nilpotent groups of class six

Candidate extension, 28 September 2026. In every finite rank r, the
single-commutator problem in `F_r/gamma_7(F_r)` is decidable, with factors
constructed on a positive answer. This remains partial scope of N8(b),
which asks about every nilpotency class. Independent review and a fuller
novelty audit remain outstanding.

Use `[x,y]=x^-1 y^-1 x y` and write L_j for the degree-j component of the
free integral Lie ring on V=Z^r. Rational vector-space arguments below
are explicitly over Q; all decisions in the group use integer Hall
coordinates. Rank at most one is immediate. The preceding arbitrary-class
algorithms already handle nonzero degree-two targets and targets in
gamma_5, including gamma_6. The only new branches have first nonzero
degree three or four.

## 1. An injective degree-five bracket map

The map

    L_2(Q) tensor L_3(Q) -> L_5(Q),    A tensor B -> [A,B],

is injective. To prove this, embed its domain into `V_Q tensor^5`, with
the degree-two and degree-three factors in the first and last blocks.
Let T belong to the kernel. The bracket is T minus its rotation by two
positions. Hence T is invariant under that rotation, and therefore under
all cyclic rotations because gcd(2,5)=1.

Since L_2 consists of skew tensors, transposing the first two positions
negates T. Conjugating this transposition by cyclic rotations proves
the same for every adjacent transposition. Thus T is totally alternating.
But alternation in three positions annihilates every element of L_3:
one checks this on `[u,[v,w]]` by expansion, equivalently by Jacobi.
Applying alternation to the last three positions of T therefore gives
both zero and 6T. In characteristic zero this forces T=0.

This proof does not assert injectivity for arbitrary degree pairs. It is
the particular coprimality and alternating-tensor argument for (2,3).

## 2. The metabelian module kernel in degree four

Use the module representation from the class-five proof. Put
`S=Q[t_1,...,t_r]` and take the free S-module with basis e_i. In the
semidirect Lie algebra where the linear polynomial space acts by
multiplication, map `X_i` to `(t_i,e_i)`. Write mu for the module
component of a derived Lie element. Then

    mu([X_i,X_j]) = t_i*e_j-t_j*e_i,
    mu([z,D]) = ell_z*mu(D)    for z in L_1, D in L',
    mu([C,D]) = 0             for C,D in L'.

We require the exact statement

    ker(mu restricted to L_4(Q)) = [L_2(Q),L_2(Q)].

The right side is contained in the kernel and has dimension
`binomial(dim L_2,2)`: its exterior-square map is injective by splitting
degree-four tensor words into two length-two blocks.

For completeness, count the image directly. It is precisely the space
of homogeneous polynomial vectors `(P_1,...,P_r)` of degree three
satisfying `sum t_i*P_i=0`. The basic syzygies `t_i*e_j-t_j*e_i` generate
this space over S, so every such degree-three vector is a sum of their
quadratic multiples. These multiples are images of the iterated brackets
`[X_k,[X_l,[X_i,X_j]]]`.

Here is an elementary justification of the syzygy assertion. Induct on
r. Set t_r=0 and express the first r-1 specialized components by basic
syzygies using the induction hypothesis. Subtract their extensions;
then each of the first r-1 components is divisible by t_r, say
`P_i=t_r*Q_i`. The relation forces `P_r=-sum_(i<r) t_i*Q_i`, which is a
sum of the remaining basic syzygies. Degrees are preserved throughout.

The map from degree-three polynomial vectors to degree-four polynomials,
`(P_i)->sum t_i P_i`, is onto. Therefore

    dim mu(L_4) = r*binomial(r+2,3)-binomial(r+3,4).

Subtracting this from Witt's formula `dim L_4=(r^4-r^2)/4` gives exactly
`binomial(r*(r-1)/2,2)=binomial(dim L_2,2)`. The included subspace above
therefore exhausts the kernel. Only standard free-Lie dimensions are
used; the degree-four kernel statement has now been proved explicitly.

## 3. Three new zero-kernel statements

Put E=L_2(Q). For nonzero z in L_1(Q), the map
`f=ad_z:E->L_3(Q)` is injective, as proved in the class-five argument by
the associative centralizer of a generator. Identify `[E,E]` with
`Lambda^2 E` and identify `[E,L_3]` with `E tensor L_3` using Section 1.
Under these identifications, ad_z sends the alternating tensor
`A tensor B-B tensor A` to

    A tensor f(B)-B tensor f(A).

In particular, it is `(id tensor f)` on that alternating tensor.

**C.** For Y in E nonzero, the map

    L_3 + L_4 -> L_5,   (U,V) -> [U,Y]+[z,V]

has zero kernel. Applying mu to a kernel equation gives
`ell_z*mu(V)=0`, hence V belongs to `[E,E]` by Section 2. Let A be its
alternating tensor. Section 1 turns the equation into

    (id tensor f)(A) = Y tensor U.

Modulo f(E) in the second tensor factor, this forces U to lie in f(E).
Write U=f(T). Injectivity of id tensor f gives `A=Y tensor T`.
A nonzero pure tensor cannot be alternating over Q; since Y is nonzero,
T=0. Thus U=V=0.

**D.** For nonzero Y in L_3(Q), the map

    L_2 + L_4 -> L_5,   (U,V) -> [U,Y]+[z,V]

also has zero kernel. Again V lies in `[E,E]`, and the tensor equation is
`U tensor Y+(id tensor f)(A)=0`. If Y does not lie in f(E), projection
modulo f(E) gives U=0, hence A=V=0. If Y=f(T), injectivity gives
`A=-U tensor T`. Since T is nonzero and A alternating, U=0, again
forcing V=0.

**E.** For independent C,D in E, the map

    L_3 + L_3 -> L_5,   (U,V) -> [U,D]+[C,V]

has zero kernel. By Section 1 its equation is
`-D tensor U+C tensor V=0`. Independent linear functionals on C,D
give U=V=0.

All three statements over Q imply zero integral kernels. The actual
existence tests below still require integer linear algebra: a unique
rational solution need not be integral.

## 4. Leading degree three

The exact normalization and homogeneous factor enumeration in the
penultimate-layer proof give a finite complete list of integral leading
pairs `(z,Y)` of weights (1,2), with `[z,Y]=g_3`. All signed divisor
allocations are retained. Choose Hall lifts x0,y0 for each pair.

Matching degree four uses corrections in L_2+L_3. The earlier Kernel A
describes its rational kernel as `Q*(Y,0)` and its integral kernel as
`Z*(Y/content(Y),0)`. Compute an integer particular solution if there is
one. The exact move `(x,y)->(yx,y)` adds Y to the degree-two correction
of x, leaves y fixed, and preserves the full target commutator. Thus
every actual solution can be normalized to one of `content(Y)` integer
residues of the affine kernel parameter. No higher terms altered by the
move are fixed prematurely.

For each residue choose actual group lifts and recompute the full
commutator. Matching degree five now uses corrections in L_3+L_4 and
map C of Section 3. There is at most one solution; test its integrality
and retain it when it exists. Recompute again. Finally, matching degree
six uses corrections in L_4+L_5. This final step is an integer linear
system; its kernel no longer needs to be normalized because no higher
degree remains. Every accepted case supplies exact factors.

## 5. Leading degree four

There are two possible normalized weight types.

- For (1,3), enumerate all leading integral pairs `(z,Y_3)` by the
  complete homogeneous factor procedure. The degree-five correction
  in L_2+L_4 is injective by D, so its integral solution is unique when
  it exists. After incorporating it, degree six is a final linear
  correction in L_3+L_5.
- For (2,2), recover the rank-two exterior tensor in `Lambda^2 L_2`
  and enumerate every oriented Hermite sublattice representing its
  leading pairs. Their two leading terms C,D are independent because
  the target is nonzero. The degree-five correction in L_3+L_3 is
  injective by E. After that unique integral correction, degree six
  is a final linear correction in L_4+L_4.

All intermediate group lifts are recomputed exactly. The general
filtered correction identity from the preceding proofs says that the
first affected layer changes by `[U,D]+[C,V]`. Later terms are retained
in the actual group elements until the next matching step.

## 6. Termination, remaining branches and limits

Reject nonzero abelianization and accept the identity. Degree two is
handled by the previous all-class IA algorithm; degrees five and six
by the penultimate/central algorithms. Sections 4–5 cover every other
nontrivial target. Each uses a finite complete leading-pair list, finite
explicit residue sets, and integer linear systems. Exact normalization
shows every putative solution is represented. Thus both answers are
decidable and positive witnesses are constructible, uniformly in rank.

The specific injectivity lemmas must not be extended without proof.
For example, take C=a, U=[a,b], D=[a,[a,U]] and
V=-[U,[a,U]]. Jacobi gives `[U,D]+[C,V]=0`, with weights
(C,D)=(1,4) and (U,V)=(2,5). Both corrections are nonzero, and their
cross term [U,V] in degree seven is nonzero. This case illustrates a
remaining difficulty beyond class six; it is not covered by the
zero-kernel arguments above.

Implementation and verification are recorded in `scripts/n8_class6.py`
and the accompanying audit. This argument imports the previous N8
candidate lemmas, standard Hall/Witt theory and integer normal forms.
It does not claim those ingredients as new discoveries or settle the
remaining arbitrary-class problem.
