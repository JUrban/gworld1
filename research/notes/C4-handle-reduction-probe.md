# C4: exact FullHRed probe and limits of the length-bound route

Status: bounded computational investigation; no answer to C4, no new candidate.

## Original scope and chosen algorithm

The complete frozen `sources/raw/probcomplex.html` and the C4 background in
`Back2.html` were read; the actual C4 statement rendering was produced and
viewed in `research/statement-audits/C4/`. C4 asks for a subexponential time
bound for Dehornoy's braid word-problem algorithm. The background explicitly
distinguishes this from the known quadratic automatic-group algorithm.
A faster alternative algorithm therefore does not answer this question.

We implement the specific **FullHRed** strategy of Dehornoy, *A Fast Method
for Comparing Braids*, Advances in Mathematics 125 (1997), 200–235, author
preprint https://dehornoy.lmno.cnrs.fr/Papers/Dfo.pdf (printed preprint pp23–25).
It chooses the handle whose right endpoint is first, applies the local
substitution (1.4), then completely freely reduces. Initial free reduction
is separately recorded; all main probe inputs were already freely reduced.
GreedyHRed, convex, coarse, and divide-and-conquer variants are distinct.

A handle sigma_j^e v sigma_j^(-e) permits interior indices below j-1 as well
as above j; it does **not** require all interior indices to exceed j.
The interior excludes j-1 and j, and a permitted handle has a single sign
among occurrences of j+1. Each sigma_(j+1)^d is replaced by
sigma_(j+1)^(-e) sigma_j^d sigma_(j+1)^e. Other letters are unchanged.
The first-ending handle is permitted by the paper's lemma.

The source's exact nine-step example is reproduced, including every
intermediate word. Signed letters encode Artin generators; uppercase means
inverse. Report columns labelled strands, and the numeric keys of
`champions`, refer to the **ambient** 1+maximum generator index. Dehornoy's
intrinsic width subtracts the minimum occupied index; these need not coincide.
The implementation's variable `width` uses the ambient convention. Its
width<=3 length assertion is valid for that subset, not a computation of
intrinsic width for shifted inputs.

## Prior results that constrain this investigation

Dehornoy Proposition4.5(i), preprint pp27–28, already proves a quadratic
HF-step bound in width3. The familiar conjugates
(b^2 a^2)^m b (a^(-2) b^(-2))^m are already the paper's quadratic example.
Proposition4.5(ii) supplies a cubic **length** bound for a **coarse** variant
in width4, not a time bound for the local FullHRed implementation.

The more general linear-length Conjecture4.4 in the old paper is not an
available lemma. Dehornoy–Wiest, *On word reversing in braid groups* (2004),
https://dehornoy.lmno.cnrs.fr/Papers/Dhg.pdf, Proposition2 gives arbitrarily
long freely reduced words from the fixed four-strand word B a c b using
left/right reversing and monotone equivalences. Thus that broader proposed
route is false. The counterexample does not follow the prescribed handle
strategy and does **not** answer C4 negatively. Their Conjecture12 restricts
monotone transformations to commutations and retains a proposed linear
space bound. Even that space bound alone is not a subexponential time bound.

The source's separate assertions concerning existence of short sigma-definite
representatives also do not control the path taken by FullHRed. A bounded
web search did not find a full answer to C4; this is not certification that
it remains open as of the run date.

## Reproducible bounded observations

`scripts/c4_handle_probe.py` uses seed20260929 and caps each word at20000
HF steps or after-free length20000. Search score is lexicographic
(expanded adjacent letters, HF steps, peak after-free length); the selected
best record is not necessarily a maximum for each individual coordinate.

- Exhaustive freely reduced B3 words of lengths1–8:13120 evaluations.
- Exhaustive freely reduced B4 words of lengths1–6:23436 evaluations.
- 204 conjugation-family evaluations: eleven recorded patterns, every
  indicated central generator, powers1,2,4,8,16,24. Some inputs can coincide.
- 9072 seeded mutation evaluations in ambient B4/B5 at raw lengths24,48,96.
  Freely reduced input length can be smaller; each is saved explicitly.
- Total45832 evaluations; zero capped observations. This is an evaluation
  count, not a count of distinct words or an asymptotic statement.

Selected champion records:

| Ambient group | Input length | HF steps | Expanded letters | Peak after free reduction |
|---|---:|---:|---:|---:|
| B3 |193|1152|2256|193|
| B4 |241|1777|3493|241|
| B5 |84|665|845|128|

The B3 champion is the published quadratic family. The B4 champion is a
conjugate of a by (abCbc)^24. The finite observations do not distinguish
polynomial from exponential worst-case growth. No theorem is inferred by
fitting these values, and no further blind increase of these samples is
currently justified.

## Independent checks and exact evidence

The Python fixture, full probe and exporter completed with actual exit0,
expected markers, and empty stderr. Their respective runtimes were0.069,
26.406 and1.524 seconds. Exact source versions, output records and process
metadata are retained.

`scripts/check_c4_gap.g` uses a separate direct interval search for the
first handle, its own local rewrite and free reduction. It replays235
selected records, checking all22501 step endpoints, generator indices,
expansion counts, lengths and cancellation counts, plus the final words.
These include the published example, all family records, the exhaustive
score-selected records and mutation champions. It does not independently
repeat every word in the exhaustive search or the random search decisions.

GAP also checks67 input/output pairs of input length<=16 using the faithful
Artin action on a free group of rank5. All four signed versions of each
adjacent local rule, inverse/commuting controls, and noncommuting/unequal
negative controls pass. Long-word equality is supported by the replayed
algebraic rules, not by materializing their potentially huge Artin images.
The GAP run completed in14.768seconds, actual exit0, marker present, empty
stderr. These are internal independently implemented computations, not an
outside review or an asymptotic proof.

Runs: `results/c4-handle-fixture-v1`, `c4-handle-probe-v1`,
`c4-export-checks-v1`, `c4-gap-replay-v1`.
Artifacts: `research/certificates/C4-handle-probe/`.

## Reading record and next mathematical obstacle

The original full HTML/background and rendered C4 statement were inspected.
For Dfo, the introduction, Section1 definitions and Section4 were read as
text; printed pages5,25,27 were actually viewed. The Section2–3 termination
proof was not fully re-audited. The separate Dhn convergence note was read
through its definitions/main-lemma outline (pp1–5), with no image inspection;
it reverses the main-generator convention and was not used as the algorithm
specification. For Dhg, the introduction, definitions and Section5 were read
as text and pages2,15 were viewed; its complete counterexample proof has not
been independently rechecked. All three original PDFs and retrieval metadata
are archived, with hashes.

Further C4 work needs a monotone potential specific to the actual reduction
strategy, a proved slow family, or a genuine new structural bound. The false
unrestricted reversing-length conjecture and short representative existence
cannot supply that missing argument. Preserve this tool for a concrete new
lead; return to the wider unresolved portfolio in the meantime.
