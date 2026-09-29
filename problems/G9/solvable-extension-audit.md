# G9 free-solvable extension: audit and evidence

29 September 2026, before the original deadline. This supplements the
metabelian proof committed as `8a62095`; it does not replace its proof,
certificates or fixed numerical endpoints.

The argument in `solvable-extension-proof.md` uses the general faithful
flow criterion for F/R' over the labelled Cayley graph of F/R. The
assumptions R<=ker(exponent sum in a_1) and invariance under inversion of
a_1 are essential. They are automatic for R=F^(d-1), d>=2. Neither an
arbitrary quotient nor an arbitrary generating set is asserted to meet
them. The effectiveness assertion takes a word-problem algorithm for the
deck group as input; for free solvable groups it is constructed by the
usual recursive flow induction. No promise-recognition algorithm is given.

The general proof's delicate point is noncommutative order. Relative
endpoints are z_i^-1 z_(i+1); original endpoints update by multiplying
on the right of the current original start. Flow translation acts on
edge bases on the left. Reflection of the first-axis edge changes its
base to sigma(q)a_1^-1, with that generator on the right. Replacing these
rules by commutative coordinate arithmetic would be incorrect.

## Verification

`scripts/g9_solvable_flows.py` implements exact recursively nested flow
representations, without importing a free-solvable group package. It
stores the lower quotient endpoint and its finite edge flow. Exact
group multiplication, inversion and reflection are implemented recursively.
`check_g9_solvable_flows.py` checks recovery in four bounded suites:

| Rank | Derived length | Exhaustive reduced-word radius | Words enumerated | Recovery checks including longer controls |
|---|---|---|---|---|
| 2 | 2 | 7 | 4,373 | 663 |
| 2 | 3 | 7 | 4,373 | 663 |
| 3 | 3 | 5 | 4,687 | 567 |
| 2 | 4 | 5 | 485 | 105 |

There are 1,998 recovery checks. Rank-two derived-length-two results
also agree with the separate earlier lattice-flow implementation.
There are 1,335 checks with explicitly noncommuting lower-quotient
generators. Inversion, endpoint recovery and reflected word equality
are checked in the same suites. Longer strict paths include repeated
cancellations, horizontal loops and downward pieces; the seed is
929260955. Three words of lengths 4,20,84 are verified trivial in
derived lengths 1,2,3 respectively and nontrivial in the next quotient.
This prevents confusing equality in adjacent derived quotients.

The independent GAP implementation represents the metabelian deck group
by native Laurent-polynomial Magnus rows over the rationals. It computes
the *outer* flow from each word, reconstructs every relative endpoint
from its boundary, applies the native deck automorphism, and recovers
the original outer flow. It does not use Python's recursively nested
representation for those calculations. It compares its results with
68 exported examples in ranks two and three, all at derived length
three. It also checks the three relation controls: the first is still
nontrivial in the deck group, the second vanishes there but has nonzero
outer flow, and the third has zero outer flow. Nontriviality in derived
length four is checked by Python, not independently by this GAP program.

The explicit negative-control script deliberately replaces left flow
translation by right translation, then separately reverses the product
order in the reflection formula. Both changes produce incorrect recovered
flows on the verified fixtures. Counts and witness words are retained in
`order-controls.json`. This tests whether the fixture family detects the
noncommutative distinction that motivated the extension.

Four recorded jobs, each one core and 8 GB reservation:

- `g9-solvable-extension-v1`: pass, 0.722 seconds.
- `g9-solvable-extension-gap-v1`: failed, 1.876 seconds. GAP attempted
  an unsupported ordering of symbolic rational expressions. It returned
  zero but emitted an error and no marker; correctly recorded as failed.
  Exact source retained beside the logs.
- `g9-solvable-extension-gap-v2`: pass, 4.283 seconds, empty stderr.
  The correction compares finite flows by exact coefficient equality
  without ordering native symbolic entries; expected outputs unchanged.
- `g9-solvable-order-controls-v1`: pass, 0.220 seconds, empty stderr.

Every job is terminal. These bounded checks do not prove the arbitrary-R
theorem or replace specialist review of the induction. No fine-precision
growth computation has been performed.

## Prior work and counting

Guba math/0508422 Lemma 3 already states the general flow theorem used
here; its text was read again. Classical Hammersley–Welsh unfolding and
the recursive Magnus word-problem method retain their prior credits.
Arzhantseva–Guba–Guyot math/0406013 provides earlier lower bounds for
F/R' and convergence results for free solvable growth; its main theorem
was reread. We do not claim that broad growth context as new.

Searches combining free-solvable growth with computable/computability
and Hammersley–Welsh did not locate an exact matching approximation
theorem. The novelty assessment is still provisional. No new literature
download or specialist review is claimed for this extension.

The GroupWorld count remains **six whole-entry candidates, four partial
candidates, zero established novel results**. This is a stronger general
theorem behind the same G9 partial candidate, not a solution of another
entry or of the exact-value question. No Kourovka mathematical argument,
subagent, external contact or push was used.
