# F34(a)/F38(a): implemented equation and language interfaces

30 September 2026, approximately 06:52–07:05 UTC. This is a shared
implementation supplement, not a new candidate result or an outside review.
The full constrained-equation-to-EDT0L construction remains unimplemented.

## What is now executable

[`f34_f38_language_interface.py`](../../scripts/f34_f38_language_interface.py)
implements the two interfaces around that missing construction:

1. `compile_equations` takes a positive rank and signed input words. It
   produces explicit monoid equations with involution, regular constraints,
   and a projection back to the original variables. It accepts F34's
   equation `u(X)=V`, with V positive, or F38's equations
   `P^-1 u(X) P=U`, `Q^-1 v(X) Q=V`, with U,V cyclically reduced.
2. `grammar_case` takes an explicitly supplied finite controlled tuple
   grammar. It constructs separate component incidence matrices and the
   exact determinant polynomial (F34), or determinant times cyclic-length
   difference (F38). `test_grammar` invokes the existing exact span checker
   and reconstructs an actual tuple along a retained nonzero path.
3. `verify_problem_witness` checks that tuple against all original equations
   and regular constraints and separately recomputes its group meaning.

The interface does **not** generate a complete solution grammar from the
compiled equations. Every grammar result explicitly reports
`complete_problem_decision: false`. Universal vanishing on a supplied
grammar does not establish a negative F34 answer or an affirmative F38
answer unless the missing completeness requirement has been supplied.
The tests deliberately include an incomplete identity-only grammar and an
empty grammar, neither of which is allowed to produce a full decision.

An actual validated nonzero tuple has useful one-sided meaning even from
an incomplete grammar. For F34 it gives an injective endomorphism with
positive image of the input, to which the candidate's Stallings argument
applies. For F38 it distinguishes cyclic lengths under an injective
endomorphism; the passage to a distinguishing automorphism still imports
KLSS Corollary 1.4. This interface does not itself construct that
automorphism or the F34 spanning-tree basis.

## Exact equation reduction

For each long group product introduce reduced prefix variables. A product
XY=Z is replaced by the three literal monoid equations

```
X = S T,     Y = inverse(T) R,     Z = S R.
```

Every reduced group solution extends: T is the maximally cancelled suffix
of X, and S,R are the remaining prefix and suffix. Conversely, literal
solutions satisfy XY=ST T^-1 R=SR=Z in the group. Signed variable tokens
denote reversal with inversion. Empty and one-token products are handled
directly. Thus the reduction preserves the entire projected original
solution relation, not just whether a solution exists. Auxiliary variables
are existentially quantified and constrained to be reduced.

The finite recognizing monoid records (i) zero for an unreduced word,
otherwise its first and last letters or the empty-word identity, and
(ii) the two-bit set of signs occurring. Multiplication is concatenation:
the endpoint component becomes zero at an adjacent inverse pair, and the
sign component uses union. Involution reverses/inverts endpoints and swaps
the two sign bits. A carrier of size `4*(2+(2r)^2)` suffices; unattainable
carrier values do not change the recognized languages. Reducedness,
cyclic reducedness and positivity are explicit subsets. Enumerating
compatible values of this finite monoid is effective, but the code does
not implement the subsequent recompression graph.

## Grammar conventions and controls

Alphabet symbols are strings. `terminal_letters` maps exactly 2r symbols
to signed free generators. Every endomorphism explicitly supplies the
image of every symbol, including empty images for erasure. Seeds are
named tuple components; all original problem components are required.
Every supplied component has its own copy of the alphabet counts, even
if it does not occur in the polynomial. Consequently a nonterminal V
in F34, or a nonterminal conjugator P in F38, prevents tuple acceptance.
Filtering only components mentioned in the polynomial would be incorrect.

Control order must explicitly be `application` or `composition`. For the
latter, the automaton edges and initial/final roles are reversed before
applying matrices to count columns. Tuple reconstruction follows the
same actual application path. Noncommuting morphism controls distinguish
the two conventions.

The determinant is expanded in separate generator-image exponent sums.
The F38 length factor counts terminal letters of U minus those of V.
No test for determinant one, existence of a polynomial zero, or arbitrary
length equations is claimed. The finite support product retains terminal
filtering through erasing morphisms.

## Retained checks

The [Python checker](../../scripts/check_f34_f38_language_interface.py)
uses all reduced rank-two image words of length at most two in seven
input systems. It accepts 1,433 original solution tuples and rejects 590
that fail the positive-output requirement. Each accepted tuple is lifted
and checked, and changing its last original component is rejected.
The finite monoid is checked on 7,225 word pairs, 85 inversions and 255
regular-language membership conditions, including unreduced words.

Thirteen grammar controls cover an infinite unary positive relation,
erasure, empty/incomplete languages, wrong equations, nonpositive tuples,
composition order, rank-two determinant six, singular unequal-length
tuples, nonsingular equal-length tuples, and nonterminal components absent
from the polynomial. Four nonzero tuples also pass the original problem
witness check. The unary family is handcrafted; it is not output of a
general equation solver.

The separate [GAP checker](../../scripts/check_f34_f38_language_gap.g)
loads exported data without calling the Python implementation. It checks:

- 18,072 literal monoid equations, 2,300 native free-group equations and
  28,560 variable constraints for all 1,433 tuples;
- every supplied seed, component incidence matrix and terminal filter;
- 480 determinant/length-polynomial evaluations on separately generated
  count vectors, including additional rank-three F34 and F38 polynomials;
- path reachability, 31 independent lifted basis vectors, 19 transition
  closure checks, and the accepted identity/nonidentity certificates.

The random arithmetic samples use GAP's Mersenne Twister with seed
340380930, 32 samples per case, and counts from zero through four.
These are additional controls, not a proof of polynomial identity or
of an unbounded group theorem. The closure certificate concerns the
entire specified grammar; bounded sampling is not used to establish
that closure.

The GAP replay succeeded in 9.401 seconds at one CPU and an 8 GB
per-process address-space limit. Its stderr contains GAP's warnings
about globals first assigned inside the top-level loop, not errors.
The exact stderr is retained; it is not described as empty. The initial
Python run took 6.792 seconds. Across these jobs, at most two CPU slots
and 16 GB of requested memory reservations overlapped. These reservations
are not a measurement or cgroup bound on aggregate resident memory.

Two failed GAP invocations are retained. The first was started before
the export completed and could not open its input. The second encountered
an invalid multiple-argument arrow-function abbreviation. Both had zero
GAP exit status but error output and no completion marker; the process
wrapper rejected them. The corrected full replay passed. No mathematical
counterexample was discarded.

## Artifacts and regeneration

The [certificate directory](../../research/certificates/F34-F38-language-interface-v1/)
contains the original tuple data, complete grammar certificates, numeric
GAP export, summaries, source snapshots and hash manifest. The initial
pretty-printed `cases.json` exceeded the repository blob limit because
the monomial arrays carried extensive whitespace. Its exact bytes were
moved to ignored `large-artifacts/`; the retained compact JSON contains
the same parsed data and is below 90 MB. `packaging.json` records both
hashes and sizes. Reformatting the compact data with Python's
`json.dumps(data, indent=2)+'\n'` reproduces the original bytes exactly;
this was checked before packaging. The omitted formatted copy adds no
mathematical data.

The v1 equation/grammar checker source and original interface source are
preserved under `sources/`. The current interface additionally requires
every original tuple component at grammar validation. A recorded
packaging check confirms unchanged matrix/polynomial inputs for all 13
certificates and rejects a missing V in all 13 cases. The original failed
GAP source is preserved separately. Exact process receipts and log hashes
are bound by the manifest.

For regeneration in a fresh working copy, run the Python checker with a
fresh output directory through `scripts/run_recorded.py`, then export its
`cases.json` with `export_f34_f38_language_gap.py`. The GAP script's two
input paths identify the retained fixture directory; adjust both if
using a different regeneration directory. Run each dependent stage only
after its predecessor has completed. The packaging script records the
whitespace transformation for the retained paths and refuses to replace
an existing archived formatted copy.

The proof and source-import requirements remain those in the
[closing dependency audit](../../research/audits/F34-F38-closing-proof-reread.md).
Rechecking Ciobanu–Zetzsche, *Slice closures of indexed languages and word
equations with counting constraints*, [arXiv:2405.07911](https://arxiv.org/abs/2405.07911),
found it already credited in the earlier audit; no new novelty conclusion
or implementation was obtained from that search. Candidate counts remain
ten whole entries, two partial entries and zero established novel results.
