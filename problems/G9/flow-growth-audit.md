# G9 flow-growth audit

29 September 2026, during the original run ending 30 September at
10:04:49 UTC. First approximation argument approximately 09:19–09:23;
the final finite upper-bound GAP check ended at 09:45:20 UTC.

## Statement and outcome

The complete original `sources/raw/probgrowth.html`, the G9 section of
`sources/raw/Back2.html`, and the actual captured G9 paragraph were read.
The short original asks for the growth rate of the rank-r free metabelian
group. The background's comparison with lattice walks and the free-group
rate specifies the standard free basis. We define the constant explicitly
using balls, retain arbitrary finite rank, and do not substitute minimal
growth over generating sets or equivalence of exponential functions.

The candidate proof is `flow-growth-proof.md`. It supplies a terminating
uniform approximation algorithm, with an explicit two-sided error bound,
and the finite rank-two enclosure

    2.658596558 <= lambda_2 <= 2.943737759.

This is one **partial G9 candidate**. There is no closed-form constant,
rational growth series, efficient general algorithm, fine-precision run,
best-known-bound claim, or established novelty claim. The all-rank proof
has been internally audited but not independently reviewed by a specialist.

## Mathematical audit

The key extra assertion beyond classical path unfolding is recovery from
the *total edge flow*. Positive edges are indexed by their lower endpoint
and coordinate axis; upper edge height is z_1+1 for first-axis edges and
z_1 for the others. A strict bridge has no horizontal edge at its initial
height. Consequently successive pieces occupy disjoint edge bands even
though their boundary vertices can coincide. Restricting a flow to a band
and taking its boundary recovers the endpoint. Reflection reverses both
first-axis orientation and the edge base point. These details are needed
to undo unfolding without knowing the original word or cut times.

The last-extremum cuts give strictly decreasing positive spans, including
when horizontal steps or cancelled excursions occur. The span list has
partition rather than composition growth. Splitting an arbitrary word
at a global height minimum and prepending one first-axis step to each
half gives x^-1 y=w, with total cost at most n+2. The resulting partition
factor is subexponential, and the proof gives a rational radius selection
rule for any requested accuracy. Ball enumeration uses equality of flows,
not an unproved efficient shortest-word algorithm.

For the lower certificate, atom cuts are defined using nonzero net edge
coefficients, not the number of visits in a selected path. In a product
of atoms, separating cuts are exactly the factor boundaries. Horizontal
flow on a terminal level belongs to the preceding factor; the next factor
has no horizontal edge there. This establishes unique factorization for
the chosen alphabet even when atom heights differ. Chosen word costs need
only bound group length from above. Exhaustiveness and global geodesicity
are unnecessary for the certified lower bound.

For the upper certificate, every forbidden word has a strictly smaller
word for the same element in a fixed shortlex order. Local replacement
therefore excludes it from *all* least representatives, independently of
whether the bounded generator found every possible relation. Counting an
overlanguage of these representatives bounds balls. The positive-vector
matrix inequality is exact; no floating-point spectral estimate enters.

## Computations

All commands, times, actual exits and output hashes are retained under
`results/g9-*`. All jobs used one CPU core, sequentially, with reservations
between 2 and 16 GB; the largest was the 18-letter C++ enumeration. The
maximum successful runtime was 70.855 seconds. All are now terminal.

| Check | Coverage | Result |
|---|---|---|
| Python flow unfolding | Rank 2 through length 10; rank 3 through 6; rank 1 through 8; 17,121 unfolding recoveries including three deliberate longer controls | Pass |
| Fixed-height concatenation | 7,023 rank-two, 4,042 rank-three and 8 rank-one products | Pass |
| Independent GAP unfolding | 243 sampled/control words, 24 products, 24 exact rational bounds; independently enumerated rank-two balls through radius 8 and rank-three balls through 4 | Pass on v3 |
| C++ bridge enumeration v1 | Rank 2 through length 14 and 18; latter has 71,944,028 half-space words, 31,414,056 bridges, 25,323,719 distinct bridge flows | Pass |
| C++ atom enumeration v2 | Through length 14; all bridge counts agree with v1 | Pass |
| Python explicit atom certificate | Same 1,003,970 half-space words and 496,000 bridges as C++; 21,483 distinct atoms | Pass |
| Independent GAP atoms | Every listed word's strict geometry, native Magnus entry, cut condition, distinctness, cost counts and exact polynomial inequalities | Pass |
| Python forbidden certificate | 118,097 reduced words through length 10; ball size 111,979; 648 forbidden relations and 1,968 states | Pass |
| Independent GAP upper bound | All 648 native Magnus equalities and shortlex decreases; all 7,872 transitions independently reconstructed; all 1,968 integer vector inequalities | Pass |

The rank-two ball counts through radius 10 are
`1,5,17,53,161,485,1457,4345,12893,38065,111979`.
The first group collisions occur at radius 7; checking only smaller balls
would not distinguish the free metabelian group from the free group.
The independent GAP enumeration includes that radius and radius 8.
The rank-one counts are exactly 2n+1. The seeded reservoir uses 9292609.
Longer controls include five-piece unfolding with repeated cancellations,
a commutator-of-commutators zero-flow relation, rank-three horizontal
loops, and an explicitly rejected non-half-space path.

The fixed-height length-18 alphabet alone gives 2.622033 and does not
exceed the website's quoted number. It is retained as an earlier probe,
not confused with the stronger mixed-height atom construction. The atom
root is between 2.658596558 and 2.658596559: only its *lower* enclosure
endpoint is used to bound the group constant from below. Its upper root
endpoint is not a group upper bound.

## Failures retained

`g9-flow-unfolding-gap-v1` failed because GAP has no `Int(boolean)` method;
it also emitted unbound-global warnings. v2 failed on a duplicated local
variable name while wrapping the checker in a function. Both GAP processes
returned zero but lacked the expected marker and emitted errors, so the
runner correctly classified them as failures. Their exact script versions
are preserved as `source.g` beside their logs. v3 corrects these language
errors and passed with empty stderr. No mathematical expected output was
weakened. The other recorded checks passed with empty stderr.

## Prior work and reading limits

- Guba, *Strict dead end elements in free soluble groups*,
  [math/0508422](https://arxiv.org/abs/math/0508422), Lemma 3, page 5:
  faithful flow criterion, crediting Droms–Lewin–Servatius. The lemma was
  read and its page viewed. We do not use the subsequent efficient
  shortest-path claim.
- Duminil-Copin–Ganguly–Hammond–Manolescu,
  [*Bounding the number of self-avoiding walks: Hammersley–Welsh with
  polygon insertion*](https://math.berkeley.edu/~alanmh/papers/HammersleyWelsh.pdf),
  Section 2: classical unfolding and partition count. Lemmas 2.1–2.2 were
  read and the proof page viewed. They concern walks; the flow-recovery
  argument is supplied separately here.
- Arzhantseva–Guba–Guyot,
  [*Growth rates of amenable groups*](https://arxiv.org/abs/math/0406013):
  introduction, main lower-bound statements and free-soluble corollaries
  read. These supply important prior context, not a full-paper audit or
  an exact free-metabelian constant.
- Löh, [Bourbaki exposition 1206](https://www.bourbaki.fr/TEXTES/Exp1206-Loh.pdf),
  Proposition 2.7 and Appendix B; Bodart–Osin,
  [arXiv:2404.17840v3](https://arxiv.org/pdf/2404.17840v3), Section 3.1,
  Lemma 3.2: general upper semicomputability was checked in text. This
  must not be conflated with the two-sided effective approximation claimed
  here. No visual/full-proof audit of these two documents is claimed.
- Guttmann–Conway, [*Square lattice self-avoiding walks and polygons*](https://cpb-ap-se2.wpmucdn.com/blogs.unimelb.edu.au/dist/0/310/files/2019/09/sawc.pdf),
  September 2001 preprint, pages 16–17 viewed, especially Section 5.3.
  The downloaded PDF has a garbled extracted text layer. The actual page
  discusses numerical estimates near 2.6381585, including values biased
  by a conjectured exponent. We therefore do not endorse the site's
  description of its quoted decimal as an established rigorous lower
  bound. Our certificate does not depend on that assertion. This was a
  targeted reading, not an audit of the whole enumeration paper.

Targeted searches for free-metabelian growth, computability, bridge and
unfolding methods, and the new endpoint numbers found no exact prior
match. That is not proof of novelty or of an optimal numerical bound.
The frozen site's historical number is only a comparison; its status
as a rigorous lower bound is not assumed in our argument.

No Kourovka mathematical result was imported. Local source snapshots,
finite certificates, the failed scripts and complete process records are
covered by the accompanying manifests. The rendering tool's original
`visual_inspection: pending` field is unchanged; a separate dated record
records actual viewing. No outside contact, push or subagent was used.
