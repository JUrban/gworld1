# F24 and automatic-group scope refresh

28 September 2026, approximately 21:24–21:29 UTC. This is bibliographic
triage and a scope check, not a new solution. The original F24 and H5
fragments, linked background, and rendered paragraphs were inspected.

## F24(b) is a prior full positive answer

Diao–Feighn, *The Grushko decomposition of a finite graph of finite rank
free groups: an algorithm*, Geometry & Topology 9 (2005), 1835–1880,
[publisher PDF](https://msp.org/gt/2005/9-4/gt-v9-n4-p02-s.pdf), Theorem 1.2,
computes the Grushko decomposition in this class. Their introduction
explicitly identifies F24(b) as a consequence (printed p.1837).
Thus arbitrary finite-rank amalgamated subgroups are covered, not merely
the cyclic case mentioned in the website background. Exclude this named
subpart from new-result counts.

Read the introduction, the input convention in section 2.7, subgroup
representations in sections 2.8–2.9, and the algorithm and Theorem 2.8
in section 2.10. The full proof in later sections was not independently
audited or implemented here. The exact source is archived as
`literature/raw/F24-DiaoFeighn2005.pdf` with retrieval metadata and hash.

The background already reports a negative answer to F24(a), attributed
to an adjustment of Miller's construction. Its original proof was not
newly inspected. F24(c) remains unresolved here. In particular, replacing
arbitrary embeddings by the identical double F *_H F would narrow its
scope: the identical-double malnormality criterion is insufficient for
the original arbitrary amalgamation problem. No such restricted argument
is counted as a new answer.

## H5 and nearby questions: recognition is not a decision procedure

Rees, *The development of the theory of automatic groups*,
[arXiv:2205.14911](https://arxiv.org/abs/2205.14911), printed pp.15–16,
describes a hyperbolicity procedure which terminates precisely on the
positive cases. A supplied automatic structure does not turn this into
a terminating negative test. The official
[Magma documentation](https://docs.magma-maths.org/FinitelyPresentedGroups/AutomaticAndHyperbolicGroups/hyperbolic-groups.html)
likewise treats a false result from its bounded attempt as inconclusive.
Neither is a full H5 answer.

Read Rees pp.13–16, 17–18 and 26–27. The survey keeps H6/H7 open in
2022, and distinguishes automatic from biautomatic hypotheses for soluble
groups and direct factors. In particular, the cited soluble biautomatic
theorem does not settle H16; the direct-factor question is already a
subcase of H10. These are dated scope checks, not certification that no
later resolution exists. Targeted current searches supplied no full
answer. CAT(0) examples that are not biautomatic, and Cayley-automatic
examples, cannot be substituted for ordinary automatic examples.

## H4: comparison with polynomial hyperbolicity certificates

Holt–Linton–Neunhöffer–Parker–Pfeiffer–Roney-Dougal,
[*Polynomial-time proofs that groups are hyperbolic*](https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/24863/pregroups_accepted.pdf?isAllowed=y&sequence=1),
archived author manuscript dated 22 July 2020, explicitly permits its
polynomial procedure to fail on hyperbolic input (introduction, pp.1–4).
Its additional word-problem-solver test also need not succeed. It neither
provides uniform polynomial Dehn conversion for all hyperbolic inputs nor
contradicts the explicit-output obstruction in `problems/H4/proof.md`.
The manuscript discusses exponential costs of one brute-force conversion;
that is not a lower bound for every possible output presentation. Only
the abstract/introduction and targeted passages were read in this pass.

No candidate scope or tally changes: four whole-entry candidates, two
partial candidates, zero established novel results. No mathematical
argument or code was imported from Kourovka.
