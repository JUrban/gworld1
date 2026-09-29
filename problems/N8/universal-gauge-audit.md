# Audit: universal commutator-preserving substitutions

29 September 2026. This extends the existing N8(b) partial candidate.
The full argument is in `universal-gauge-proof.md`. It is a candidate proof,
not specialist validation or established novelty. No additional entry is
counted: the portfolio remains eight whole-entry coverage candidates,
two partial candidates and zero established novel results.

## Scope and proof audit

The branch condition is separation of consecutive nonzero pre-Nielsen
kernel offsets, t'>=2t. This holds for every leading weight gap <=5,
so all targets of nonzero leading degree <=7 are covered in arbitrary
class. The union with the existing six-final-layer theorem covers every
target in classes <=13. Existing arbitrary-class families and free-generator
branches are retained. Overlapping exceptional offsets remain unresolved.

The audit checks the following points in the written argument:

- The two leading coefficients need not be ambient free generators.
  The structural kernel lemma uses a different graded-tail algebra in
  which they are free generators; the resulting substitution is subsequently
  evaluated as two group words. It need not extend to an ambient automorphism.
- The correction of [a,b] to log([exp(a),exp(b)]) is degreewise and exact
  through the declared truncation. The homogeneous error is in the derived
  Lie algebra, spanned by brackets with the two generators. Conjugation
  then preserves the full group commutator, not just its leading bracket.
- Weighted Hall collection retains a torsion-free quotient. The integral
  power argument clears coordinates of both forward and inverse generator
  images. It does not infer lattice preservation from rational invertibility.
- Every integral kernel direction receives a nonzero integral period.
  All cosets of the resulting finite-index lattice are kept. The actual
  Nielsen period and the actual affine-line parameter step are retained.
- Between an exceptional offset t and 2t, exact substitutions act by
  constant translations on the unknown block. Their dependence on unknown
  corrections starts after that block. Successive cancellation proves
  they span the full fiber kernel over Q; integer Smith/Hermite reduction
  consequently gives finitely many affine lines, not an unjustified
  single representative.
- At 2t, only the two offset-t corrections can contribute the quadratic
  term. The earlier nonzero obstruction survives every higher affine
  correction. A new exceptional kernel exactly at 2t is handled at the
  next stage, after the preceding parameter is fixed.
- If 2t is beyond the remaining class, the entire remaining system is
  solved jointly. No arbitrary intermediate witness is fixed.
- The cutoff consequences check every normalized leading type. For c<=13,
  either d<=7 or c-d<=5. Identity, rank <=1 and targets outside the derived
  subgroup are accounted for separately.

The general-offset structural lemmas remain proof dependencies with their
previous audits and bounded independent tests. The present tests do not
independently certify every inference in those lemmas or this assembly.

## Exact construction

`scripts/n8_universal_gauges.py` constructs a complete weighted Hall basis
in the rational tensor algebra, the degreewise substitution and its inverse,
and every homogeneous kernel direction in each declared offset range.
It integrates each direction, searches factorial powers, collects both
directions into integral group words, and verifies the claimed leading
increment, two-sided inverse and exact commutator identity.
No randomized choices or floating-point arithmetic are used.

| Fixture | Weights | Class bound | Offsets and kernel dimensions | Maps | Selected powers |
|---|---|---:|---|---:|---|
| 11c6 | 1,1 | 6 | 2:1; 3:0; 4:3 | 4 | 1,1,1,1 |
| 12c8 | 1,2 | 8 | 2:0; 3:1; 4:0; 5:1 | 2 | 1,24 |
| 13c10 | 1,3 | 10 | 4:1; 5:0; 6:1 | 2 | 1,24 |
| 23c12scaled | 2,3 | 12 | 4:0; 5:1; 6:0; 7:0 | 1 | 2 |
| 13c12scaled | 1,3 | 12 | 4:1; 5:0; 6:1; 7:0; 8:2 | 4 | 6,362880,720,720 |
| 11c8 | 1,1 | 8 | 4:3; 5:0; 6:6 | 9 | 24,24,24,2,2,2,1,2,2 |

The two scaled fixtures divide the primitive rational directions by two
and six, respectively. All 22 constructions pass. The retained 41 rejected
smaller powers expose fractional group coordinates; they are not silently
rounded. The largest chosen power is 9!, within the declared finite search
cap 12!. The proof of termination is independent of that computational cap.

Construction elapsed times were 1.474, 0.772, 0.871, 0.221, 15.319 and
153.389 seconds in the table's order. Exact directions, collected forward
and inverse words, dimensions and rejected powers are in
`../../research/certificates/N8-universal-gauges/`. The JSON directions use
tensor words in log A,log B. GAP fixtures use zero-based Hall indices in
the stored descriptions and integer exponents; the verifier converts indices
explicitly. Commutators throughout are x^-1*y^-1*x*y.

## Independent GAP group checks

`scripts/check_n8_universal_gauges_gap.g` imports the Hall-word descriptions
and integer images, constructs weighted nilpotent groups using GAP/nq, and
does not import Python matrices or tensor arithmetic. Each presentation
kills the boundary Hall words; GAP checks torsion-freeness and the complete
retained Hirsch rank, then verifies the boundary words. Each map and inverse
must be a genuine group homomorphism. Both compositions and both commutator
images are checked exactly.

The five smaller groups have retained ranks 23,17,16,11,29. All 13 maps,
52 inverse equalities and five wrong-Nielsen controls pass in 6.339 seconds.
The separate class-eight group has rank71; its nine maps,36 inverse equalities
and one wrong-Nielsen control pass in45.570 seconds. In total: six groups,
22 maps,88 inverse equalities,44 commutator-image equalities and six controls.
The wrong move x->x*y is rejected; the exact Nielsen move is x->y*x.

The first GAP run failed: `GeneratorsOfGroup` returned the full polycyclic
list, but only two images were supplied. The log, false process status and
executed source are retained in `results/n8-universal-gap-v1/`; this is a
verifier error, not a failed mathematical identity. The corrected five-group
run has one harmless parser warning for the fixture global assigned by
`Read`; its executed source is retained in `n8-universal-gap-v2/`. Initializing
that global removes the warning for the final class-eight replay. The final
replay has empty stderr. No failed run is discarded.

## Decomposable leading coefficients

`scripts/check_n8_universal_specialization_gap.g` constructs the separate
weighted target group Gamma_(1,2,12), of Hirsch rank79, from its Hall boundary
presentation. Write its generators A,B and put T=[B,A], S=[T,A]. The eight
actual pairs are

    (A^m T^u, T^k S^v),
    (m,k,u,v) = (1,1,0,0), (2,3,0,0), (-1,1,0,0), (1,-1,0,0),
                (1,1,1,1), (2,3,-2,3), (-1,3,2,-1), (2,-1,-1,2).

Their leading weights are1,3. Their heavier leading coefficient k[B,A]
is decomposable in Q*A+L_(>1), the precise restriction of the earlier
weighted-orbit approach. All four maps from `13c12scaled` are evaluated as
word substitutions on each pair. Every boundary relation vanishes, every
commutator is nontrivial, both substituted commutators agree with the
original, and substitution of the inverse words recovers both factors in
both orders. All32 substitutions are nontrivial. The32 cases,128 inverse
equalities and64 commutator equalities pass in17.881seconds with empty stderr.
This is pair evaluation, not an attempted automorphism of the ambient group.

The target-presentation export passed in0.218seconds. All commands, resource
reservations, output hashes and statuses are in `results/n8-universal-*`.
Construction jobs used one core/8GB; target export used one core/4GB.
At most three construction jobs ran together (3cores/24GB); the final two
GAP jobs used2cores/16GB together. All jobs are terminal. The checks validate
these finite constructions, not the entire new decision algorithm. No
end-to-end implementation of its residue enumeration and exceptional-block
quotient is claimed.

## Statement and primary sources

The full archived `sources/raw/probnil.html`, exact N8 fragment and linked
background paragraph were reread during this work period. The actual
archived N8 rendering was re-viewed. Part(a)'s general nilpotent negative
answer is distinguished from part(b)'s free nilpotent question; the linked
background credits Roman'kov's prior class-two free result. The frozen
website's older open-status sentence is not a current novelty guarantee.

The Altassan2013 printedp24 image was re-viewed, confirming Theorem3.3's
free-basis coefficient hypothesis and finite/countably infinite rank scope.
The original Remeslennikov--Stohr theorem and homogeneous Shirshov lemma
remain credited as in the previous N8 proofs and source audits.

Yusuke Kuno, *A combinatorial construction of symplectic expansions*,
[arXiv:1009.2219v2](https://arxiv.org/abs/1009.2219), was archived with
SHA256 `56f6f53824f6231222b687572d531181fba3a83f05b1f59203969742d839edc4`.
The introduction, Theorem1.1 and beginning of the definitions were read;
actual PDFp2 was viewed. That page credits Massuyeau's Lemma2.16 for the
earlier degreewise construction. Kuno gives a canonical algorithm. The
original Massuyeau paper and Kuno's full proof were not audited here.
Our finite weighted recursion is written out, including conversion to our
commutator convention. `N8-Kuno-page1.png` was generated but not visually
inspected; no claim of viewing that page is made.

Targeted searches for free-nilpotent commutator equations and symplectic
expansions did not locate a matching full extension. This is a limited
search, not evidence sufficient to establish novelty. The assembled result
still requires external mathematical and bibliographic review. No Kourovka
argument, subagent, push or author contact was used.
