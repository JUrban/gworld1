# N9 fixed-group candidate: scope, proof and verification audit

29 September2026. Initial structural lead approximately20:02--20:04 UTC;
toy group replay completed20:12 UTC; universal normalization checked in
Lean at20:18:41 UTC. All precede the original30 September10:04:49 UTC
deadline. Candidate proof: [proof.md](proof.md). External specialist review
and novelty assessment remain outstanding.

## Statement fidelity and prior scope

The full frozen `sources/raw/probnil.html`, exact N9 fragment and complete
N9 paragraph in `sources/raw/Back2.html` were reread. The actual archived
rendering `research/statement-audits/N9/statement.png` was viewed again.
The original question fixes the ambient group, then supplies a finitely
generated subgroup. Its background expressly says that uniform
undecidability as the ambient group varies leaves this fixed-group
question open. The candidate uses one fixed presentation and varies only
the word x1^(3n+1)x2^-1.

Roman'kov, *Diophantine questions in the class of finitely generated
nilpotent groups*, J. Group Theory19 (2016),497--514,
[DOI10.1515/jgth-2016-0504](https://doi.org/10.1515/jgth-2016-0504),
is credited for the prior uniform theorem. The previously read author
text and Myasnikov's2016 slides distinguish that assertion. The earlier
note `research/notes/N9-fixed-ambient-and-coproduct.md` records the precise
source limitations and the failed fixed-base attempts. This proof does
not depend on the interpretation of the product notation discussed there.

Part(b) is prior: Roman'kov--Khisamiev--Konyrkhanova, *Algebraically and
verbally closed subgroups and retracts of finitely generated nilpotent
groups*, Siberian Math. J.58 (2017),536--545,
[primary article record](https://www.mathnet.ru/php/archive.phtml?jrnid=smj&option_lang=eng&paperid=2889&wshow=paper).
Its abstract explicitly reports the finite-rank free-nilpotent retract
algorithm. The primary record is archived as `N9-free-prior-2017.html`;
the complete2017 proof has not been independently audited here. The
website also marks exactly this subpart solved. It is never counted as
a new result.

## Imported arithmetic theorem

The substantive external input is DPRM: a fixed computably enumerable
set admits one polynomial with a free input parameter and finitely many
existential unknowns. The polynomial does not change with that parameter.

- James P. Jones, *Universal diophantine equation*, J. Symbolic Logic47(3)
  (September1982),549--571,
  [publisher extract](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/universal-diophantine-equation/113EBF3D928DFC6011C52BECAE81A087).
  The extract's prose was read; its online2014 date is not the publication
  year. The full article was not read, and two formula-image requests
  failed, so those images are not claimed inspected.
- Dominique Larchey-Wendling and Yannick Forster, *Hilbert's Tenth Problem
  in Coq (Extended Version)*, LMCS18(1),35 (2022),
  [arXiv2003.04604v5](https://arxiv.org/abs/2003.04604v5).
  Archived PDF hash
  `63d9a8767917e6902f3d5b59e43f7822331819522547770be2927ad0c5abbd65`.
  Introduction, Theorem8.3 and its proof, Theorem9.5 and Section9.2 were
  read. The actual printed page35:21 was rendered and viewed. Theorem8.3
  explicitly supplies a single equation with parameters; four-square
  substitution changes existential natural variables to integer variables.
  The paper's Coq development was not downloaded, built or independently
  checked in this task. DPRM and Lagrange are imported prior theorems.

The parameter n remains natural and is not replaced by four squares.
The unknowns and every gate value are integral. This avoids inadvertently
using rational Diophantine solvability or a polynomial depending on n.

## Adversarial proof checks

1. **Fixed versus variable data.** S,P,the circuit,D,the linear equations,
   the full lattice basis and presentation are all chosen before n. Only
   two supplied subgroup words change. The construction neither varies a
   quotient nor invokes a decision algorithm uniform over ambient groups.
2. **Integer normalization.** The square Pfaffian gives d*w=x^2 and the
   subgroup gives t*d-x=1. Their exact consequence is
   d*(w-t^2*d+2*t)=1. This covers d=0 and nonunit d. The factor3 excludes
   d=-1. Lean checks this implication for all integer inputs, not a range
   of tested coefficients.
3. **Circuit consistency.** Every wire has its own disjoint U,V pair.
   Its axis equations give(z,0),(0,z) after normalization. Both signs in
   the multiplication gate follow from the alternating form. Negative
   constants, repeated inputs, zero values and reuse of an earlier wire
   cause no division or exception. Acyclic evaluation gives the converse.
4. **Lattice saturation.** L is the full integer kernel. A rational basis
   multiplied by separate denominators could miss matrices and invalidate
   sufficiency. The toy certificate instead supplies a unimodular
   transformation of the transposed constraint matrix, whose zero rows
   produce the complete integer kernel.
5. **Presentation consistency.** The bilinear central cocycle realizes
   all generators with unique integer coordinates. Thus no implicit extra
   relation, torsion or collapse of the central basis is assumed away.
6. **Input subgroups.** A solution at parameter0 proves q_n nonzero for
   every natural n. The two-generator subgroup has no relation beyond
   class-two nilpotency, by commuting any proposed relation with its two
   generators. Hence its centre is exactly the infinite cyclic group
   generated by their commutator.
7. **Necessity.** A retraction is onto its subgroup, so all ambient central
   generators map into that subgroup's centre. Integral powers give the
   lambda vector. Commutator preservation gives a decomposable alternating
   form; fixing the actual commutator gives the affine normalization.
8. **Sufficiency.** The prescribed images satisfy every group relator.
   In this construction the images of x0,x1,x2 are respectively a,b,b^(3n),
   so both input generators are fixed exactly, including central
   coordinates. No omitted central correction or extension theorem is used.
9. **Earlier obstruction.** None of the varying subgroups is assumed to
   be a retract. Their commutators vary; no fixed common target equation
   is reflected through a family of pre-existing retracts. The previous
   failed reductions therefore do not apply.
10. **Conclusion and counting.** A decision procedure for the single G
    would decide S via an ordinary computable word map. This answers(a),
    beyond the prior uniform result. Whole-entry coverage includes prior(b)
    with credit; it is one candidate entry, not two discoveries.

No mathematical gap was found in this internal audit. That judgment is
not independent specialist validation. A retract here is a semidirect
factor, not necessarily a direct factor; no assertion about undecidability
of direct decomposition is being made.

## Exact computations and their limits

All computations used `scripts/run_recorded.py`, one CPU each, at most8GB
reserved memory per job. All jobs are terminal. Native GAP is4.16.1 with
nq2.5.11. Python uses exact SymPy/FLINT integers and rational ranks.

| Run | Outcome | Mathematical scope |
| --- | --- | --- |
| n9-heisenberg-retracts-v1 | pass |17 general-criterion positive witnesses; four algebraic negative controls; seed2026092920 |
| n9-heisenberg-retracts-gap-v1 | pass |17 native group retractions; exact obstruction polynomials and central vectors |
| n9-fixed-circuit-v1 | pass,0.67s |Fixed toy circuit, complete integer kernel, seven witnesses and wrong-sign control |
| n9-fixed-circuit-gap-v1 | pass,25.50s |Independently reconstructed constraints/kernel; one actual group and all seven retractions |
| n9-normalization-lean-v1 | unsuccessful |Lean subprocess exit134 before proof diagnostics; raw logs preserved |
| n9-normalization-lean-v2 | pass,7.30s |Universal integer normalization and three related elementary statements; axiom audit |

Every successful run has empty stderr. The first Lean run used5GB with
no explicit Lean thread setting; the second used8GB and
`LEAN_NUM_THREADS=1`. The source was unchanged. These observations do not
diagnose the first abort conclusively.

The toy circuit is(y+1)^2=p, with five wires p,y,1,y+1,square and the
final linear zero condition square-p=0. It has14 noncentral coordinates,
23 independent linear constraints on91 upper entries, and a saturated
kernel of rank68. The resulting fixed group has Hirsch length82.
The seven pairs(n,y) are(9,-4),(4,-3),(1,-2),(0,-1),(1,0),(4,1),(9,2).
GAP builds the group once and checks every homomorphism, its image,
fixed subgroup generators and idempotence. The parameter values-1,2,3
give noncommuting subgroups but no square solutions by elementary integer
arithmetic. GAP checks the subgroup inputs, not an exhaustive search for
all homomorphisms; their nonretract conclusion uses the written reverse
implication.

The wrong-sign control removes the factor3 and uses t=n+1. At n=2,
the negative of a normalized matrix with p=4,y=1 then satisfies the
incorrect affine condition with d=-1. Both programs confirm this false
positive. The actual modulus-three system rejects it.

`research/certificates/N9-fixed-circuit/Normalization.lean` proves the
normalization for arbitrary integers, its existential equivalence, the
wedge Pfaffian identity and the multiplication-gate identity. Lean4.24.0
runs with `--trust=0` against Mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. Every declaration's transitive
axioms are restricted to propext, Classical.choice and Quot.sound.
No sorry or new axiom is allowed. Only Mathlib infrastructure is reused
from the existing S5 workspace; no S5 mathematical result is imported.
This is **not** a formalization of the group construction, DPRM or the
complete undecidability reduction.

The numeric universal DPRM polynomial and its full group presentation
have not been generated. The general proof gives an effective construction;
the implementation and GAP checks instantiate a small illustrative circuit.
No computational complexity bound is claimed.

## Reproduction and evidence

Use fresh run names and output paths or a clean checkout for generator
scripts, which deliberately refuse to overwrite their certificate output.
The recorded process JSON contains every exact command and resource limit.
For Lean, use the existing pinned binary directory on PATH and set
`LEAN_NUM_THREADS=1`; run `scripts/check_n9_normalization_lean.py` through
the recorder. On another machine the standalone Lean file can be checked
with `lake env lean --trust=0` in the same Mathlib revision.

`research/certificates/N9-fixed-circuit/manifest-v1.json` binds the proof,
audit, statement evidence, sources, scripts, fixtures and raw process logs.
The general Heisenberg criterion and the initial universal lead are retained
as development records. No Kourovka proof or private correspondence was used.

Targeted searches on29 September included combinations of "retract problem",
"fixed", "nilpotent", "undecidable", "Heisenberg" and Roman'kov, including
recent dates. They recovered the prior uniform result, the free-nilpotent
algorithm and unrelated retraction notions; no matching prior fixed-group
answer was located. This is a bounded search, not a novelty guarantee.

Statement fidelity: checked. Proof status: internally audited candidate,
with independent computational implementations and a limited Lean lemma.
Novelty: unverified. Independent external mathematical review: pending.
