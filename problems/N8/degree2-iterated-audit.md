# Audit of the degree-two iterated-adjoint family

28 September 2026, approximately 21:03 UTC. This audits the candidate
in `degree2-iterated-proof.md`, extending the same partial N8(b) result
to the family ad_C^(n+1)(T), C in L2 and T in L3, in every odd class
c=2n+7>=9. It is not a full solution of N8(b), specialist review, or
confirmation of novelty.

## Statement and proof review

The original nilpotent-group HTML, exact N8 paragraph and its rendered
image were reread. The star applies to (a); (b) asks for every finitely
generated free nilpotent group. The family considered here is explicitly
partial, with arbitrary later coordinates and integral group factors.

The written argument was checked for the following potential gaps:

- Degree-one factors are excluded for every rational direction z using
  a z-stable free alphabet, not by testing only the original generators.
- Projection onto the free algebra on C,T excludes every leading type
  except (2,2n+3). Quotienting by another degree-two direction proves
  uniqueness of C's line.
- A compatible degree-lexicographic leading-word argument proves freeness
  of the ad_C jet alphabet. Injectivity holds on its ideal, while the
  exceptional centralizer line QC is explicitly removed.
- The block-quadratic nonvanishing lemma and its Klyachko dependency are
  retained. Rational recognition occurs before integral leading-factor
  enumeration; nonintegral D0 is a negative input within the family.
- The first correction has zero kernel for odd n and one rational kernel
  direction for positive even n. Full integral solution lattices, both
  signs and nonprimitive leading scales are retained.
- The final quadratic coefficient survives modulo the entire rational
  last-layer image. The proof kills L4 explicitly under the jet map;
  it does not reuse the different degree argument of the first family.
- The group weight calculation excludes all other nonlinear terms.
  All integral roots and lattice congruences are tested. Unsupported
  inputs return `None`, which is never interpreted as `False`.

This is a same-agent proof review. The all-rank/all-class assertion rests
on the written argument and credited structural results, not extrapolation
from the following finite computations.

## Recorded exact Python checks

Every run below has normal exit zero and its expected marker.

| Run suffix after `n8-degree2-iterated-` | Scope | Seconds |
| --- | --- | ---: |
| `lead-n2-v1` | Rank 2, class 11: all leading types, first kernel, obstruction | 4.78 |
| `lead-n3-v1` | Rank 2, class 13: all leading types and first kernel | 74.72 |
| `class11-rank2-v1` | Five supported group decisions and three scope controls | 53.47 |
| `class13-rank2-v1` | Five supported group decisions and three scope controls | 164.27 |
| `class9-rank3-v1` | Five supported group decisions and three scope controls | 97.55 |

The structural probes retain exactly two signed leading pairs, of type
(2,q). In class eleven the first map has rank 31 on 32 columns and
the obstruction raises the final rank from 59 to 60. In class thirteen
the first map has rank 101 on 101 columns.

Each group suite has three positive cases, including a nonprimitive
leading pair, and two negative last-layer perturbations. The rank-three
suite uses a mixed degree-two C. All suites include a nonzero commutator
of the same leading degree from the degree-one family, which must be
recognized as outside the present family, plus identity and degree-one
controls. In total this is 15 supported decisions and nine controls.
The construction seed is stored in each `checks.json`.

The class-thirteen Python and rank-three Python logs include scheduled
faulthandler stack snapshots. Their authoritative process records show
normal completion; these snapshots are not computation timeouts.

## Independent GAP replay and its incomplete benchmark

The separate GAP checker reconstructs Hall words in its free group and
nilpotent quotients. It checks actual word witnesses, all retained linear
membership decisions, Hermite identities, complete integral parameter
lists, final correction columns and polynomial samples. The integer
membership checker retains its abelian-tail and integral-lattice checks.

| Run suffix | Completed independent evidence | Seconds |
| --- | --- | ---: |
| `class11-rank2-gap-v1` | 3 witnesses; 7 linear decisions; 7 polynomial certificates, 4 empty; 35 samples | 15.77 |
| `class9-rank3-gap-v1` | 3 witnesses; 14 linear decisions, 4 negative | 162.88 |

Both exited zero with the expected marker and empty stderr. Together
they cover ten supported targets, including four negative targets, and
both parity cases. Totals: six witnesses, 21 linear decisions, seven
polynomial certificates and 35 samples. The scope controls themselves
were checked in Python, not independently replayed by GAP.

`class13-rank2-gap-v1` timed out after 600.02 seconds, exit -9. It built
the class-thirteen quotient and verified the Hall cache, but reported no
completed witness. This run is retained as incomplete and contributes
no independent target or witness count. Its Python decisions are not
promoted to independently replayed decisions. No efficiency guarantee
is part of the theorem.

## Reproduction and scope limits

Exact commands, seeds, return codes, timestamps, stdout/stderr and their
hashes are retained under `results/` and `research/certificates/`.
The implementation is `scripts/n8_degree2_iterated.py`; the test generator
and independent GAP wrappers use the same `degree2_iterated` stem.
The previous shared arithmetic modules were not modified for this family.
Each run requested one core and an 8 GB per-process limit.

A further bounded primary-source search for free-nilpotent single
commutator algorithms found class-two equations, general undecidability
results and previous problem statements, but no matching theorem for
this family. This is not an exhaustive novelty audit. All prior-class
credit and the original N8 qualifications remain in force.

The class-nine part overlaps the previous all-target class-nine result.
The new scope is the specified family in odd classes eleven and above.
The tally remains three whole-entry and two partial candidates, with
zero established novel results. No new Kourovka transfer, subagent,
external review, contact or push was used.
