# Iterated-adjoint family: scope, evidence and reproduction

28 September 2026. Candidate argument:
`problems/N8/iterated-adjoint-proof.md`. First uniform argument approximately
19:47--19:52 UTC; explicit recognition and full proof completed during the
20:00--20:22 continuation. This extends the **same partial N8(b) candidate**.
Independent specialist review and novelty assessment remain outstanding.

The precise new scope is every finite rank and every class c>=6, for
targets whose nonzero degree-(c-2) leading term is ad_z^(c-4)(T), with
nonzero rational z in L1 and T in L2. The later coordinates are arbitrary.
This is not all of gamma_(c-2), and does not answer general N8(b).
The full original statement, background and rendering have been audited
in the preceding N8 work; the original source and hashes are unchanged.

## Proof and implementation audit

The argument has three separate components: uniqueness of the leading
degree-one direction; parity of the first correction kernel in a free
alphabet on which ad_z shifts generators; and a nonzero final quadratic
obstruction when that kernel is a line. The functional sending T_j to
A+(-2)^j B gives the exact obstruction value 1-4^m. It kills the full
final correction image, not just a tested subspace. The group weight
bounds leave exactly two correction layers, so all surviving choices
are finite or integral linear systems.

The structural dependencies are the delta-stable free basis proved in
Section 1 of the class-nine note, its credited ordinary homogeneous
Shirshov lemma and free-metabelian torsion-free module theorem, and the
earlier exact leading-factor normalization. The special-family theorem
does not depend on completing the separate all-target class-nine
computational benchmark. The finite checks below do not replace any
all-rank part of the written argument.

`scripts/n8_iterated_adjoint.py` recognizes rational scope first, using
block-quadratic directions and exact linear algebra. It then retains
every signed integral leading scale. A missing integral leading pair
would be a negative decision within the recognized scope. Inputs outside
the theorem return `answer=None`; they are not classified as noncommutators.
The earlier version-one implementation checked integral pairs first;
although its bounded tests passed, it could not by itself justify this
recognition distinction. Its sources are retained beside the version-one
logs, and the final implementation is version two.

The first and final systems use integral Hall coordinates, never just
rational membership. An exceptional first kernel is primitive in the
full integral lattice. Every polynomial certificate contains the complete
integer root list and divisibility conditions. No height cutoff or
discarded infinite parameter is used. Practical complexity is not claimed.

## Completed finite checks

| Run | Scope | Seconds |
| --- | --- | ---: |
| `n8-iterated-adjoint-jet-v1` | n=1,...,16: exact parity ranks, eight telescoping identities and eight nonzero obstructions | 0.12 |
| `n8-iterated-adjoint-class10-rank2-v2` | 5 supported decisions and 2 outside-scope controls | 8.15 |
| `n8-iterated-adjoint-class11-rank2-v2` | 5 supported decisions and 2 outside-scope controls | 74.31 |
| `n8-iterated-adjoint-class7-rank3-v1` | 5 supported decisions with mixed z,T and 2 outside-scope controls | 38.15 |
| `n8-iterated-adjoint-scope-v1` | 16 signed scales compared with the earlier factor routine; two nonzero same-degree outside-scope commutators | 2.53 |

Each supported group suite has three constructed positive cases and two
negative last-layer perturbations. The positive cases include first
parameters -1 and 2 and a nonprimitive leading pair. The rank-three
fixture uses z involving generators 1 and 3, and T involving all three
generators. The scope controls also require nonintegral rational T in
some integral leading-scale branches; imposing integral T would be wrong.

The two additional outside-scope controls lie in L'' at the same leading
degree as the theorem, yet are explicit group commutators. They confirm
that `None` has the intended meaning. Their verification is a recognition
check, not another positive decision by the special-family solver.

The class-eleven Python run has a scheduled faulthandler snapshot in
stderr and completed normally. The other final Python runs have empty
stderr. The earlier class-ten/class-eleven version-one outputs remain
available but overlap the final suites and add no independent target count.

## Independent GAP replay

GAP/nq builds its own free nilpotent quotients and checks actual words,
correction columns, integer membership, polynomial parameter samples,
Hermite certificates, congruences and complete integer parameter lists.
The reused checker retains the legacy marker `PASS N8 class9 GAP`, but
the quotient ranks/classes come from each fixture: the class-eleven
replay is actually in class eleven, not class nine.

| Run | Verified certificates | Seconds |
| --- | --- | ---: |
| `n8-iterated-adjoint-class10-gap-v1` | 3 witnesses; 14 linear decisions, 4 negative | 12.81 |
| `n8-iterated-adjoint-class11-gap-v1` | 3 witnesses; 7 linear decisions; 7 polynomial branches, 4 empty; 35 samples | 158.40 |
| `n8-iterated-adjoint-class7-rank3-gap-v1` | 3 witnesses; 7 linear decisions; 7 polynomial branches, 4 empty; 35 samples | 25.45 |

The class-eleven component-arithmetic replay reproduced the same evidence
in 158.76 seconds. It is a comparison on the same data, not seven additional
decisions. All independent group replays have empty stderr and normal
termination with the expected marker.

The final three datasets therefore contain 15 supported target decisions,
with nine independently checked witnesses and six negative targets,
plus six elementary outside-scope controls. Their independent audit has
28 linear decisions (four negative), 14 polynomial certificates (eight
empty), and 70 group parameter samples. These are checks of the candidate
proof and implementation, not independent specialist proof review.

The new independent GAP support-component arithmetic also agreed with
GAP's original integer solver on 216 affine systems and its determinant
routine on 24 matrices, with four boundary controls. The first run passed
with a local-variable parser warning; its source and stderr are preserved.
Version two declared that loop variable locally and passed in 1.98 seconds
with empty stderr. The integer obstruction `[2,0],[0,3]` versus `[1,0]`
is among the explicit controls, so rational solubility cannot pass as
integer solubility.

## Reproduction, sources and limits

Exact commands and actual process outcomes are in `results/NAME/process.json`.
All runs used one CPU and an 8 GB process limit through the recorded runner,
within the original shared budget. The target generator accepts `--rank`,
`--class` and a fresh `--directory`. The exporter
`scripts/export_n8_class9_gap.py targets DIRECTORY` serializes any retained
Hall degree range; it does not recompute mathematical decisions. The GAP
wrappers select the saved certificate directories explicitly. Gzip
compression keeps the sparse polynomial files small without omitting them.

Bounded searches on 28 September for `free nilpotent single commutator
algorithm`, `commutator equation free nilpotent decidability` and
`nilpotent iterated adjoint commutator equation` found no matching theorem
for this family. The general and class-two literature must not be confused
with this particular higher-class scope. Absence from these searches is
not proof of novelty; the claim remains provisional.

No argument from Kourovka was newly imported. No subagents, outside
contacts, external review or push were used. This adds no whole-entry
candidate and no established novel result; it extends the existing one
partial N8(b) candidate.
