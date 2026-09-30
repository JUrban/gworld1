# N9(a): fixed ambient group, failed encoding, and a coproduct clarification

28 September 2026, approximately 18:09–18:21 UTC. No answer to the
fixed-group question is obtained. This is a source audit and a failed
reduction, not an additional whole-entry or partial candidate.

## Exact question and source limits

The original `sources/raw/probnil.html`, the complete N9 paragraph and
its actual screenshot were read. Part (a) asks for decidability for
each fixed finitely generated nilpotent group. The N9 background in
`sources/raw/Back2.html` explicitly distinguishes this from uniform
decidability as the ambient group varies. Part (b) is marked solved.

Roman'kov, *Diophantine questions in the class of finitely generated
nilpotent groups*, J. Group Theory 19 (2016), 497–514,
[DOI 10.1515/jgth-2016-0504](https://doi.org/10.1515/jgth-2016-0504),
was read through the web-extracted text of the
[author-uploaded copy](https://www.researchgate.net/publication/300075306_Diophantine_questions_in_the_class_of_finitely_generated_nilpotent_groups).
The introduction, definitions, Corollaries 3.2–3.3 and Theorem 3.4 were
checked. **The original paper PDF was not downloaded or visually
inspected.** The local publisher PDF request returned HTTP 202 with no
bytes; the author-page request returned HTTP 403. This limitation
matters for interpreting the printed product notation below.

Corollary 3.3 uses a fixed direct product with a rank-two free nilpotent
group to transfer commutator undecidability to endomorphism orbits.
Theorem 3.4 concerns the uniform retract problem. The extracted proof
calls its construction a “central amalgamated direct product”.
That literal interpretation has the obstruction below, with an
elementary repair that retains the uniform theorem.

Myasnikov's [2016 lecture slides](https://www.macs.hw.ac.uk/~lc45/Conferences/2016/Slides_for_web/Miasnikov_Diablerets.pdf)
independently repeat the uniform assertion and the displayed product
construction on slide 35. The full PDF is archived as
`literature/raw/N9-Myasnikov-2016-slides.pdf`; physical PDF page 65
(the fully revealed overlay of slide 35) was rendered and viewed.
This confirms the displayed notation, not an additional definition of
that notation. No complete proof audit of Roman'kov's Diophantine
construction is claimed.

## Central direct products do not give the stated retraction

Let G be any class-at-most-two group, let w be central in G, and let
N be the free class-two group on x,y. Write z=[x,y]. Throughout this
note the commutator is x^-1 y^-1 x y; in class two it agrees with
xyx^-1y^-1, the convention used in the source.

Consider the ordinary central product

    D_w = (G × N) / <(w^-1,z)>.

The factor G embeds: if (g,1)=(w^-n,z^n), then n=0 because z has
infinite order, and therefore g=1. The images of x and y commute with
all of G. Consequently, if r:D_w→G fixes G, both r(x) and r(y) belong
to Z(G). Thus

    w = r([x,y]) = [r(x),r(y)] = 1.

Conversely w=1 permits the retraction killing x and y. So this literal
central product retracts onto G **exactly when w=1**, rather than when
w is an arbitrary commutator. For example, taking G itself to be the
integral Heisenberg group on a,b and w=[a,b] gives a nontrivial
commutator for which the asserted retraction cannot exist. The
suggested images x→a,y→b violate cross-commutation with G.

This is a qualification about the construction as described in the
accessible text. It is not a refutation of the uniform theorem, and
the original PDF terminology should still be checked before an
external assertion about the printed proof.

## An explicit repair

For this repair assume w∈G', as required of any possible commutator.
Centrality only in G would not by itself imply centrality in a
coproduct. Replace G×N by the coproduct C=G ⊔_2 N in the variety of groups of
nilpotency class at most two. Equivalently, take the ordinary free
product and impose all weight-three commutators. Set

    E_w = C / <[x,y]w^-1>.

Both factors embed in C, for example by their canonical retractions.
The added relator is central. The homomorphism C→N killing G maps
it to [x,y], which has infinite order. Hence

    <[x,y]w^-1> ∩ G = {1},

so G still embeds in E_w. This argument does not require G to be
torsion-free.

If w=[u,v] in G, the identity on G and x→u,y→v define a
homomorphism C→G by the coproduct property. It kills the added
relator and descends to a retraction E_w→G. Conversely a retraction
sends [x,y]=w to a commutator expression for w in G. Therefore

    G is a retract of E_w  iff  w is a commutator in G.

For finitely generated G, a finite presentation of E_w is effective:
use generators for G and x,y, the old relators, all weight-three
commutators in this finite alphabet, and [x,y]w^-1. There are no
cross-commutation relations between x,y and G.

Applying the prior fixed-group commutator-undecidability result gives
the prior **uniform** retract-undecidability assertion. The ambient
group E_w still varies with w. Nothing here turns it into a negative
answer to N9(a).

## Why one proposed fixed-ambient encoding fails

Suppose B is fixed and H_c≤B are retracts, all containing a fixed
element z. An equation with coefficients in H_c has a solution in B
if and only if it has a solution in H_c: apply the retraction to a
solution, or include a solution in B. In particular,

    z is a commutator in H_c  iff  z is a commutator in B.

This is independent of c. Thus embedding variable copies H_c in a
fixed base B as retracts, while interpreting the varying target as the
same common central element z, cannot encode undecidability. This
rules out the attempted automorphism/shear construction from this
work period.

More concretely, adjoining x,y to B in the class-two coproduct and
imposing [x,y]=z leads to exactly the same obstruction: any retraction
onto H_c restricts to a retraction of B, and its commutator condition
is constant in c. Other embeddings might work, but none is supplied.

The older attempt H_c=<G,[x,y]w(c)^-1> in a fixed coproduct also
fails. Its new central generator survives independently modulo G',
whereas H_c'=G'. A retraction would force [x,y]w(c)^-1 into G',
contradicting that independence. These failed routes should not be
reused as fixed-group reductions.

## Exact computational check and limits

`scripts/check_n9_coproduct_repair.g` uses GAP/nq over the integers,
with G the free class-two group of rank two and w=[a,b]^c for
c=-2,0,1,3. It constructs both presentations. For each corrected
coproduct quotient it verifies the inclusion and the retraction
x→a^c,y→b, including the identity composite on the base generators.
Its Hirsch length is 9. The central-product quotient has Hirsch
length 5 and contains the base group of Hirsch length 3, with its
commutator still of infinite order.

GAP rejects the proposed central-product assignment in all four
cases. Even for c=0, that particular assignment y→b violates
cross-commutation; the actual retraction x,y→1 is checked separately
and exists exactly for c=0. The proof above excludes **every**
retraction for c≠0; failure of one attempted map alone would not do so.

Run `n9-coproduct-repair-v1` completed but produced GAP parser
warnings for loop-assigned global variables. Its exact checker is
preserved with its logs. Moving those variables into a function's
local scope gave `n9-coproduct-repair-v2`, which passed in 1.93 seconds
with empty stderr. Both used one core, 8 GB and a 180-second limit.
There is no random seed or bounded mathematical enumeration.

Reproduce with:

```sh
python3 scripts/run_recorded.py --name n9-coproduct-repair-repeat \
  --cores 1 --memory-gb 8 --timeout 180 \
  --expect 'PASS N9 central-product obstruction and coproduct repair' \
  -- bin/gap -q --quitonbreak scripts/check_n9_coproduct_repair.g
```

The finite checks support the presentation distinction and examples.
They do not prove undecidability or settle a fixed ambient group.
Novelty is not claimed for the repair or the elementary equation
reflection lemma. No external specialist review has occurred.
