# AUX2 and OR15 prior answers; FP1 remains separate

29 September 2026. Source/status correction only; no discovery count.
The complete frozen auxiliary, one-relator and finitely presented pages
were read, and the actual original AUX2, OR15 and FP1 paragraphs were
rendered and viewed. There are no linked background paragraphs for these
three entries. The frozen source is unchanged.

## AUX2

The question asks for an algorithm taking positive integers m,n and deciding
whether Hanna Neumann's inequality holds for all subgroups of those ranks.
It has the constant affirmative algorithm, by the prior Hanna Neumann
theorem. The ranks are positive, so there is no zero-rank input exception.

Primary source actually checked:
[Joel Friedman, *Sheaves on Graphs, Their Homological Invariants, and a Proof
of the Hanna Neumann Conjecture*, arXiv:1105.0129](https://arxiv.org/abs/1105.0129),
Chapter2, Section2.1, Theorem2.1. Read the statement, inequality(2.3) and
surrounding explanation; viewed printed page57 (physical PDF page64).
The full proof was not independently audited. Friedman's and Mineyev's
independent proofs are prior work. An attempted direct browser opening of
Mineyev's author PDF encountered a verification page; that was not treated
as a reading of his proof. Friedman supplies sufficient primary evidence.

## OR15

[Henry Wilton, *Surface groups among cubulated hyperbolic and one-relator
groups*, arXiv:2406.02121v3](https://arxiv.org/abs/2406.02121v3), Theorem D,
states that an **infinite** one-relator group with every infinite-index
subgroup free is free or a surface group. Here the author defines surface
groups as fundamental groups of closed aspherical surfaces. The finite-index
one-relator hypothesis in the website is unnecessary for this conclusion.

Read the introduction, Theorem D and Section4.2, including Theorems4.3/4.5
and the proof of D; viewed printed page3. The proof separates primitivity
rank>2, where hyperbolicity and cubulation apply, from primitivity rank2,
where a nonfree two-generator subgroup has finite index and the earlier
Gardam--Kielak--Logan theorem applies. The imported deep theorems and the
full52-page argument were not independently verified here.

This retires the intended **infinite nonfree** surface-characterization
problem as prior. Preserve the exact qualification: the website does not
explicitly exclude free or finite groups. If one-relator presentations are
allowed redundant generators, a free group has one, and satisfies both
subgroup hypotheses while not being a closed aspherical surface group.
Finite cyclic groups also require a convention/exception. These elementary
literal cases are not counted as new counterexamples. The theorem gives
the substantive classification with its explicit infinitude/free exceptions.

Do not replace “every subgroup” by “every finitely generated subgroup”.
Wilton's Remark0.3 explains the difference: BS(1,2) has a nonfree
infinite-index subgroup isomorphic to Z[1/2], while its finitely generated
infinite-index subgroups are cyclic or trivial.

## FP1 and A1

[Kegel--Li--Ren, *Small undecidable groups and unrecognizable4-manifolds*,
arXiv:2609.10461v1](https://arxiv.org/abs/2609.10461v1),9 September2026,
is directly relevant recent progress, not a solution of either entry.
Theorem1.1 supplies a three-generator nine-relator group with unsolvable
word problem. Theorems1.3/1.4 give Adian--Rabin families with respectively
four generators/eleven relators and two generators/ten relators.
Neither family is balanced. The paragraph immediately before Theorem1.3
explicitly leaves balanced Adian--Rabin families open. Two generators
must also not be confused with A1's request for two **relators**.

Read the abstract, introduction through Section1.6, the statements and
their scope; viewed printed page2. The paper's own AI-use and Lean
formalization disclosures were read, but the repository was not built
or audited here. This is a primary-source status check, not independent
verification of that formalization or a transfer from the Kourovka run.

## Artifacts

Full PDFs, extracted text and retrieval/hash records are archived with
prefixes `AUX2-Friedman1105.0129`, `OR15-Wilton2406.02121v3` and
`FP1-KegelLiRen2609.10461v1` under `literature/raw/`. Viewed theorem pages
are under `literature/figures/`; actual problem renderings are under
`research/statement-audits/`. The Friedman text extraction emitted a
font-type mismatch warning; the relevant actual page was inspected and
the mathematical statement is legible there. No mathematical computation
was needed for these status corrections.
