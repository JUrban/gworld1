# Audit: general type-one third-from-last targets

29 September 2026, before the original deadline. Candidate proof:
[type1-third-proof.md](type1-third-proof.md). This is internal mathematical
review and independent software replay, not outside specialist review.

## Statement and recognized scope

The complete frozen `sources/raw/probnil.html` and the N8 background in
`Back2.html` were reread. The actual original statement image was viewed
again. Only part(a) has a known negative answer in arbitrary class-two
nilpotent groups; the background credits Roman'kov2016 with the affirmative
free class-two case. Part(b) asks for every finitely generated free
nilpotent group. Our new algorithm covers c>=6 and nonzero targets of leading
degree c-2 for which **no normalized integral leading pair has first weight
at least two**. This condition is decidable using the complete finite
leading-pair algorithms. Nonzero metabelian image of the leading term is
a sufficient condition. A list with no leading pairs gives a negative
answer. Other leading types and other layers return unsupported, never a
false negative. This enlarges the same partial N8 candidate; it does not
answer the full question or add a problem count.

All finite ranks are in the mathematical statement; ranks zero/one have
no nonzero targets in the specified layer. The executed group cases use
ranks two and three only. Older central, penultimate, degree-two and
all-target class3--10 arguments remain separate. The new mixed-shape cases
in classes11 and12 go beyond the two earlier pure differential-chain
families.

## Separate internal proof review

1. Exact Nielsen moves, finite rational factor directions and **every
   signed integral scale** are retained. Equal-weight Hermite sublattices
   matter for recognizing excluded types even though this solver does not
   lift them. Completeness remains dependent on the earlier written
   leading-pair proof; the alternative projective-fibre proof also supplies
   a finite rational procedure.
2. The support argument uses separate variables for successive positions,
   not a single derivative variable. If a D word begins with another seed,
   its appended-U coefficient is independent of the last position variable;
   divisibility by their sum forces it to vanish. Ordering all outside
   letters before U-chain letters then permits Lyndon triangularity to
   remove internal outside letters too. Two independent U directions can
   be chosen simultaneously in one seed basis. Their chain subalgebras
   have zero intersection. Injectivity of delta handles U=0.
3. The double-primitive equations were checked by comparing first and
   last letters. They force cyclic invariance of each of D,V,W. Every
   nonlinear Lie polynomial maps to zero in the cyclic-word quotient;
   a cyclically invariant vector in that kernel vanishes in characteristic
   zero. The associative counterexample D=t^n,V=W=0 shows why the Lie
   hypothesis cannot be dropped.
4. The differential-chain embedding is injective by uniquely decipherable
   least words. Original weights z=1,t=2 remove the ordinary degree-one
   exception when q>2. Taking the greatest chain bracket length handles
   D with mixed lengths: projected [L3,D] is one length too short to cancel
   the quadratic obstruction. No assumption that D is a pure iterated
   adjoint is used.
5. The first integer kernel is the full primitive lattice, not an arbitrary
   rational parametrization or a bounded parameter search. The residual
   is quadratic by the weight estimates; the quadratic term is nonzero
   in a rational cokernel. All integer roots and the full final integral
   membership conditions are tested. Denominator and congruence data are
   retained. Positive factors are checked against the original group word.

The free delta-chain basis imports the torsion-free free metabelian module
and homogeneous Shirshov facts credited in `class9-proof.md`; the precise
Lyndon reference is in `research/notes/N8-general-first-kernel.md`.
No new Kourovka argument or code is imported. The all-degree proof remains
written mathematics, not a formal proof or a consequence of bounded tests.

## Executed controls

All positive/negative statements below are within the recognized scope;
unsupported controls are counted separately. The seed is9292600+10r+c.
Exact truncated integral Magnus arithmetic is compared with GAP4.16.1/nq
nilpotent quotients. Python dependencies are copied into each artifact's
`versions/` before mathematical work starts.

| Rank, class | Records | Positive | Negative | Unsupported | Linear decisions | Quadratic certificates |
|---|---:|---:|---:|---:|---:|---:|
|2,11|8|3|2|3|7|5|
|2,12|7|2|2|3|10|0|
|3,7|6|2|2|2|10|0|

The class11 leading factor is the sum of a nonzero linear derivative-chain
term and the earlier cubic odd-adjoint term. Its first correction has
nullity one. Besides a corrected witness, the suite retains the signed
nonprimitive scale pair x=z^2, y=d^-3. Class12 uses a mixed term with first
nullity zero. Rank3 uses two independent degree-two seeds and also has
nullity zero. Each suite includes final-layer and first-layer negative
perturbations. Rank2 suites include a commutator with a different integral
leading type; all suites include identity and degree-one scope controls.

The first class12 attempt timed out at180.362s with no completed case;
exit-9, missing marker, exact source, Hall words and partial stdout are
retained in `results/n8-type1-third-r2-c12-v1/` and
`research/certificates/N8-type1-third-r2-c12/`. It is not passing evidence.
The redundant associative leading-pair equations were replaced by exact
integral Hall equations, with reconstruction checks for every coordinate
conversion. A separate comparison agrees on24 complete old/new leading-pair
lists in ranks2,3, mixed/equal types, signed scales and perturbations.
That job passed in0.871s. The optimized class12 suite passed in58.413s.
The other two Python suites passed in100.801s and3.732s respectively.

The class11 GAP replay passed in34.636s:3 witnesses,7 linear decisions
(2 negative),5 polynomial decisions(2 empty),25 group parameter samples,
5 first nullities and6 metabelian scope tests. It verified the complete
primitive first affine line for every polynomial certificate, not just
sampled witnesses. The rank3 replay passed in3.681s:2 witnesses,10 linear
decisions(4 negative),4 first nullities and4 metabelian scope tests.

The class12 v2 GAP replay passed in172.807s:2 witnesses,10 linear
decisions(4 negative),4 first nullities and5 metabelian scope tests.
All seven successful new jobs, including the leading-coordinate comparison,
have actual exit0, expected markers and empty stderr. Total group replay:
7 witnesses,27 linear decisions(10 negative),5 polynomial certificates
(2 empty),25 parameter samples,13 first nullities and15 scope tests.

## Reproduction and limits

The Python driver is `scripts/check_n8_type1_third.py`, using
`--rank R --class-bound C --directory FRESH_DIRECTORY`. Use the recorded
runner with one core,8GB and180s. Current implementation:
`scripts/n8_type1_third.py`; leading enumeration:
`scripts/n8_leading_pairs_hall.py`. The older class11/rank3 artifacts
preserve the earlier equivalent tensor-coordinate leading enumerator.

Export saved records with `scripts/export_n8_type1_third_gap.py DIRECTORY`.
The successful replay drivers are
`check_n8_type1_third_r2_c11_gap.g`,
`check_n8_type1_third_r3_c7_gap.g`, and the class12 v2 driver
`check_n8_type1_third_r2_c12_v2_gap.g`. The unused class12 v1 driver names
the incomplete artifact and is retained only as provenance. Mathematical
jobs have exact command, CPU, memory, timestamps, actual exit and output
hashes under `results/`. Each complete artifact has a SHA256 manifest,
including exact Python dependencies and GAP checker/helper sources.

GAP independently checks group equalities, full integer linear membership,
first-map nullities, primitive affine lines, unimodular Hermite identities,
complete rational cokernels, integer roots and congruences, final correction
columns and leading metabelian exclusions. Five parameter values per
polynomial check its degree-at-most-two formula once the written degree
bound is used. It does not independently enumerate every rational leading
factor direction or prove the universal weight/support statements.

The earlier primary-source novelty audit remains provisional. Targeted
queries found no matching general stratum theorem; that does not certify
novelty. The cyclic/support argument, leading-factor theorem and full scope
still need independent specialist review. Counts remain six whole-entry
and three partial candidates, zero established novel results.

Bibliographic follow-up in the next work period: the support lemma is a
direct consequence of the prior Remeslennikov--Stöhr2007 inner-solution
theorem, read in Altassan2013 Theorem3.3. Section7 of the supporting note
gives the exact Lazard-embedding reduction. This supplies an alternative
prior proof and corrects any suggestion that the support lemma itself is
new; it does not resolve the group-stratum novelty question.
